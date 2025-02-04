# Change History for cdc.json (Part 3)

### Changes from 9cd27cf to 452e48f (Part 3/8)
**Author:** Automated

**Date:** 2025-02-03 20:01:08+00:00

**Message:** Updated data: Mon Feb  3 20:01:08 UTC 2025

```diff
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates for the PLACES 2021 release in GIS-friendly format. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census 2010 ZCTA boundary file in a GIS system to produce maps for 29 measures at the ZCTA level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=024cf3f6f59e49fe8c70e0e5410fe3cf",
-            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2021 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21069,74 +20972,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9xb7-9z99/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9xb7-9z99/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9xb7-9z99/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9xb7-9z99/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
+            "identifier": "https://data.cdc.gov/api/views/9xb7-9z99",
+            "issued": "2022-10-11",
+            "keyword": [
+                "behaviors",
+                "gis",
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
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2021 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-09-09",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2022-09-03",
-            "modified": "2022-12-16",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "hhs region",
-                "hispanic origin",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "race",
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
-            "identifier": "https://data.cdc.gov/api/views/9xc7-3a4q",
             "description": "Deaths involving coronavirus disease 2019 (COVID-19) reported to NCHS by time-period, HHS region, race and Hispanic origin, and age groups (<65, 65-74. 75-84, 85+, and 65+).\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
-            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, Age 65plus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21144,58 +21045,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9xc7-3a4q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9xc7-3a4q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9xc7-3a4q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9xc7-3a4q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9xc7-3a4q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9xc7-3a4q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9xc7-3a4q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9xc7-3a4q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9xc7-3a4q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/9xc7-3a4q",
+            "issued": "2022-09-09",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hhs region",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2022-12-16",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2020-01-01/2022-09-03",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, Age 65plus"
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
-            "modified": "2025-01-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:healthus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
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
@@ -21203,56 +21121,52 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9xt5-u42s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9xt5-u42s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9xt5-u42s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9xt5-u42s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9xt5-u42s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9xt5-u42s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9xt5-u42s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9xt5-u42s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9xt5-u42s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/9xt5-u42s",
+            "issued": "2024-02-16",
+            "landingPage": "https://data.cdc.gov/d/9xt5-u42s",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "DQS Health, United States Dataset Footnote Lookup"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9y49-tura",
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
-            "identifier": "https://data.cdc.gov/api/views/9y49-tura",
             "description": "ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\" >laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul><li><a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\nFind details about surveillance population, case determination, surveillance evaluation, and more. </li> <li> <a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>\nGet official interpretations from reports and publications created from ABCs data.\n</li>                </ul>",
-            "title": "Active Bacterial Core surveillance (ABCs) Group A Streptococcus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21260,65 +21174,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9y49-tura/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9y49-tura/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9y49-tura/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9y49-tura",
+            "issued": "2021-06-23",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9y49-tura",
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
+            "title": "Active Bacterial Core surveillance (ABCs) Group A Streptococcus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9yc3-yir3",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "age <5",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/9yc3-yir3",
             "description": "NNDSS - Table II. Invasive Pneumococcal Diseases, Age <5 - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting years 2016 and 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years.",
-            "title": "NNDSS - Table II. Invasive Pneumococcal Diseases, Age <5",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21326,68 +21234,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9yc3-yir3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9yc3-yir3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9yc3-yir3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9yc3-yir3",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "age <5",
+                "invasive pneumococcal diseases",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9yc3-yir3",
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
+            "title": "NNDSS - Table II. Invasive Pneumococcal Diseases, Age <5"
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
-                "500cities",
-                "census",
-                "estimates",
-                "prevalence",
-                "tracts"
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
-            "identifier": "https://data.cdc.gov/api/views/9z78-nsfp",
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2016-relea/9z78-nsfp",
             "description": "This is the complete dataset for the 500 Cities project 2016 release. This dataset includes 2013, 2014 model-based small area estimates for 27 measures of chronic disease related to unhealthy behaviors (5), health outcomes (13), and use of preventive services (9). Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. It represents a first-of-its kind effort to release information on a large scale for cities and for small areas within those cities. It includes estimates for the 500 largest US cities and approximately 28,000 census tracts within these cities. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these measures include Behavioral Risk Factor Surveillance System (BRFSS) data (2013, 2014), Census Bureau 2010 census population data, and American Community Survey (ACS) 2009-2013, 2010-2014 estimates. More information about the methodology can be found at www.cdc.gov/500cities.\nNote: During the process of uploading the 2015 estimates, CDC found a data discrepancy in the published 500 Cities data for the 2014 city-level obesity crude prevalence estimates caused when reformatting the SAS data file to the open data format. . The small area estimation model and code were correct. This data discrepancy only affected the 2014 city-level obesity crude prevalence estimates on the Socrata open data file, the GIS-friendly data file, and the 500 Cities online application. The other obesity estimates (city-level age-adjusted and tract-level) and the Mapbooks were not affected. No other measures were affected. The correct estimates are update in this dataset on October 25, 2017.",
-            "title": "500 Cities: Local Data for Better Health, 2016 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21395,71 +21301,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9z78-nsfp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9z78-nsfp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9z78-nsfp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2016-relea/9z78-nsfp",
+            "identifier": "https://data.cdc.gov/api/views/9z78-nsfp",
+            "issued": "2023-07-18",
+            "keyword": [
+                "500cities",
+                "census",
+                "estimates",
+                "prevalence",
+                "tracts"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
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
+            "title": "500 Cities: Local Data for Better Health, 2016 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-28",
-            "keyword": [
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
-            "identifier": "https://data.cdc.gov/api/views/9z9x-g48e",
             "description": "Deaths involving coronavirus disease 2019 (COVID-19) reported to NCHS by week, sex, and race and Hispanic origin. Deaths occurred in the United States.",
-            "title": "AH Provisional COVID-19 Deaths by Week, Sex, and Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21467,58 +21371,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9z9x-g48e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9z9x-g48e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9z9x-g48e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/9z9x-g48e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9z9x-g48e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9z9x-g48e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/9z9x-g48e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/9z9x-g48e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/9z9x-g48e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/9z9x-g48e",
+            "issued": "2021-05-21",
+            "keyword": [
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
+                "united states",
+                "weekly"
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
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Week, Sex, and Race and Hispanic Origin"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/9ziv-gyv9",
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
-                "name": "data.cdc.gov"
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
@@ -21526,34 +21444,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9ziv-gyv9",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/9ziv-gyv9",
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
+            "title": "Factors affecting chlorinated product formation from sodium hypochlorite bleach and limonene reactions in the gas phase"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/a2mg-p2ni",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NIOSH/Division of Field Studies and Engineering Health Informatics Branch",
                 "hasEmail": "mailto:OHLSurveillance@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/a2mg-p2ni",
             "description": "Background: Twenty-two million workers are exposed to hazardous noise in the United States. The purpose of this study is to estimate the prevalence of hearing loss among U.S. industries.\n\nMethods: We examined 2000\u20132008 audiograms for male and female workers ages 18\u201365, who had higher occupational noise exposures than the general population. Prevalence and adjusted prevalence ratios (PRs) for hearing loss were estimated and compared across industries.\n\nResults: In our sample, 18% of workers had hearing loss. When compared with the Couriers and Messengers industry sub-sector, workers employed in Mining (PR = 1.65, CI = 1.57\u20131.73), Wood Product Manufacturing (PR = 1.65, CL = 1.61\u2013 1.70), Construction of Buildings (PR = 1.59, CI = 1.51\u20131.68), and Real Estate and Rental and Leasing (PR = 1.61, CL = 1.51\u20131.71) had higher risks for hearing loss.\n\nConclusions: Workers in the Mining, Manufacturing, and Construction industries need better engineering controls for noise and stronger hearing conservation strategies. More hearing loss research is also needed within traditional \u2018\u2018low-risk\u2019\u2019 industries like Real Estate.",
-            "title": "Prevalence of Hearing Loss in the United States by Industry, 2000-2008",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21561,38 +21479,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/a2mg-p2ni",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/a2mg-p2ni",
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
+            "title": "Prevalence of Hearing Loss in the United States by Industry, 2000-2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/a37y-w96i",
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
-            "identifier": "https://data.cdc.gov/api/views/a37y-w96i",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 8 - Denver",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21600,61 +21514,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a37y-w96i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a37y-w96i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a37y-w96i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
+            "identifier": "https://data.cdc.gov/api/views/a37y-w96i",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/a37y-w96i",
+            "modified": "2016-09-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
                 "Motor Vehicle"
-            ]
+            ],
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 8 - Denver"
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -21662,72 +21575,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a3gi-4phs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a3gi-4phs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a3gi-4phs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-                "name": "National Center for Health Statistics"
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
@@ -21735,69 +21643,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a5a8-jsrq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a5a8-jsrq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a5a8-jsrq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/a5a8-jsrq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a5a8-jsrq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a5a8-jsrq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a5a8-jsrq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a5a8-jsrq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a5a8-jsrq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-                "name": "data.cdc.gov"
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
@@ -21805,66 +21712,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a93x-tfzm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a93x-tfzm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a93x-tfzm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/a93x-tfzm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a93x-tfzm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a93x-tfzm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a93x-tfzm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a93x-tfzm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a93x-tfzm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/a9xa-yrhn",
-            "bureauCode": [
-                "009:00"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/a93x-tfzm",
             "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
             "keyword": [
                 "2020",
-                "hansen's disease",
-                "hantavirus infection",
-                "hantavirus pulmonary syndrome",
+                "crimean-congo hemorrhagic fever virus",
+                "ebola virus",
+                "guanarito virus",
                 "nedss",
                 "netss",
                 "nndss",
-                "non-hantavirus pulmonary syndrome",
+                "viral hemorrhagic fevers",
                 "wonder"
             ],
+            "landingPage": "https://data.cdc.gov/d/a93x-tfzm",
+            "modified": "2021-01-07",
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
+            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:00"
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
-            "identifier": "https://data.cdc.gov/api/views/a9xa-yrhn",
             "description": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes data for old world hantavirus infections, such as Seoul virus infections. Prior to 2015, this condition was not nationally notifiable and data for this condition was not submitted to CDC's National Notifiable Diseases Surveillance System (NNDSS).\n\u00b6 Includes data for Andes virus infections.",
-            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21872,65 +21779,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a9xa-yrhn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a9xa-yrhn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/a9xa-yrhn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/a9xa-yrhn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/aagc-37gx",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/aagc-37gx",
             "description": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21938,59 +21846,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aagc-37gx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aagc-37gx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aagc-37gx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/aagc-37gx",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "other serogroups",
+                "unknown serogroup",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/aagc-37gx",
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
+            "title": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup"
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
-                "name": "data.cdc.gov"
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
@@ -21998,64 +21912,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/abgz-qs4g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/abgz-qs4g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/abgz-qs4g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/abgz-qs4g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/abgz-qs4g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/abgz-qs4g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/abgz-qs4g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/abgz-qs4g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/abgz-qs4g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/abgz-qs4g",
+            "issued": "2022-11-17",
+            "keyword": [
+                "clostridioides difficile",
+                "haicviz"
+            ],
+            "landingPage": "https://data.cdc.gov/d/abgz-qs4g",
+            "modified": "2022-11-17",
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
+            "title": "HAICViz - CDI"
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
-                "name": "data.cdc.gov"
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
@@ -22063,64 +21972,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/acdz-tk8j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/acdz-tk8j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/acdz-tk8j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/acdz-tk8j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/acdz-tk8j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/acdz-tk8j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/acdz-tk8j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/acdz-tk8j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/acdz-tk8j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Legionellosis to Malaria"
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
-            "modified": "2023-08-25",
-            "keyword": [
-                "...",
-                "behavioral",
-                "brfss",
-                "county",
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
-            "identifier": "https://data.cdc.gov/api/views/acme-vg9e",
             "description": "2002-2010. BRFSS SMART County Prevalence land line only data. The Selected Metropolitan Area Risk Trends (SMART) project uses the Behavioral Risk Factor Surveillance System (BRFSS) to analyze the data of selected counties with 500 or more respondents. BRFSS data can be used to identify emerging health problems, establish and track health objectives, and develop and evaluate public health policies and programs. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct/data",
-            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) County Prevalence Data (2010 and prior)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22128,56 +22037,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/acme-vg9e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/acme-vg9e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/acme-vg9e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/acme-vg9e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/acme-vg9e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/acme-vg9e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/acme-vg9e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/acme-vg9e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/acme-vg9e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/acme-vg9e",
+            "issued": "2023-07-18",
+            "keyword": [
+                "...",
+                "behavioral",
+                "brfss",
+                "county",
+                "risk",
+                "smart",
+                "survey"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-08-25",
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
+            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) County Prevalence Data (2010 and prior)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/adnf-fpem",
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
-            "identifier": "https://data.cdc.gov/api/views/adnf-fpem",
             "description": "MicroRNAs are essential regulators of gene expression in humans and can control pathogenesis and host-virus interactions. Notably, the role of specific miRNAs during influenza virus infections are still ill-defined. The central goal of this study was to identify novel miRNAs and their target genes in response to influenza virus infections in airway epithelium. Human airway epithelial cells exposed to influenza virus induced several novel miRNAs that were identified using next generation sequencing (NGS) and their target genes by biochemical methods. NGS analysis predicted forty-two RNA sequences as possible miRNAs based on computational algorithms. Expression patterns of these putative miRNAs were further confirmed using RT-PCR in human bronchial epithelial cells (HBEpC) exposed to H1N1, H9N1(1P10) and H9N1 (1WF10) strains of influenza virus. A time course study showed significant downregulation of put-miR-34 in H1N1 and put-miR-35 in H9N1(1P10) infected cells, consistent with the NGS data. Additionally put-miR-34, and put-miR-35 showed a high fold enrichment in argonaute-immunoprecipitation compared to the controls, indicating their ability to form a complex with argonaute protein and RNA induced silencing complex (RISC), a typical mode of action found with miRNAs. Our earlier studies have shown that replication and survival of influenza virus is modulated by certain transcription factors, such as, NF-\u0138B. To identify the target(s) of these putative miRNAs, we screened 84 transcription factors that have a role in viral pathogenesis. Cells transfected with mimic of the put-miR-34 showed significant decrease in expression of Signal Transducers and Activators of Transcription 3 (STAT3), and the inhibitor of put-miR-34 showed significant increase in STAT3 expression and its phosphorylation. In addition, put-miR-34 had 76% homology to the untranslated region (UTR) of STAT3. NGS and PCR array data submitted to the Gene Ontology also predicted the role of transcription factors modulated by put-miR-34. Our data suggests that put-miR-34 could be a good target for the antiviral therapy as the hyperactivation or inactivation of STAT3 results in viral disease, as tightly regulated STAT3 function is central to health.",
-            "title": "Influenza virus induced novel miRNAs regulate the STAT pathway",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22185,44 +22103,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/adnf-fpem",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/adnf-fpem",
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
+            "title": "Influenza virus induced novel miRNAs regulate the STAT pathway"
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
-                "adults",
-                "dental cleaning",
-                "dental visits",
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
-            "identifier": "https://data.cdc.gov/api/views/aemk-wcbf",
+            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/NOHSS-Adult-Indicators-2010-And-Prior-BRFSS/aemk-wcbf",
             "description": "Data from BRFSS for indicators of adult oral health for 1999 and even years from 2002 through 2010. National estimates are represented by the median prevalence among 50 states and the District of Columbia data. Estimates are prepared from the BRFSS public use data sets. Estimates in this file are not age adjusted, and may differ slightly from estimates available from the BRFSS web site or Chronic Disease Indicators due to small differences in definition, age adjustment or rounding. For more information, see: http://www.cdc.gov/oralhealthdata/overview/Adult_Indicators.html",
-            "title": "NOHSS Adult Indicators - 2010 And Prior BRFSS",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22230,70 +22139,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aemk-wcbf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aemk-wcbf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aemk-wcbf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/aemk-wcbf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aemk-wcbf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aemk-wcbf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aemk-wcbf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aemk-wcbf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aemk-wcbf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/NOHSS-Adult-Indicators-2010-And-Prior-BRFSS/aemk-wcbf",
-            "theme": [
-                "Oral Health"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/aemt-mg7g",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-10-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
+            "identifier": "https://data.cdc.gov/api/views/aemk-wcbf",
+            "issued": "2023-07-18",
+            "keyword": [
+                "access to care",
+                "adults",
+                "dental cleaning",
+                "dental visits",
+                "tooth loss"
+            ],
+            "landingPage": "http://www.cdc.gov/oralhealth/",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "references": [
-                "COVID Data Tracker hospital data displays: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-nhsn   NHSN Hospital Data Reporting: COVID-19 Hospital Data Reporting | NHSN | CDC  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
+                "https://www.cdc.gov/oralhealthdata/"
             ],
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
+            "theme": [
+                "Oral Health"
+            ],
+            "title": "NOHSS Adult Indicators - 2010 And Prior BRFSS"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Weekly",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DHQP",
                 "hasEmail": "mailto:nhsn@cdc.gov (subject line: weekly NHSN hospital data)"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDC"
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
@@ -22301,60 +22206,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aemt-mg7g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aemt-mg7g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aemt-mg7g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aemt-mg7g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "CDC"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/aeq9-xksa",
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
-            "identifier": "https://data.cdc.gov/api/views/aeq9-xksa",
             "description": "Nanomaterials represent a new class of materials with numerous industrial applications. Considering the projected increase in the production and use of nanomaterials, a corresponding increase in occupational exposure to nanomaterials and their resulting adverse health effects should be anticipated among workers. There is substantial evidence in the literature, based on cell culture and animal studies, supporting the potential toxicity and detrimental health effects associated with exposure to nanomaterials. Intervention and/or prevention of adverse health effects associated with occupational exposure to toxic nanomaterials will be a major concern for health providers and regulatory and non-regulatory government agencies as the use of nanomaterials expand. A key element in the intervention and/or prevention of the adverse health effects associated with occupational exposure to toxic nanomaterials is a clear understanding of the molecular mechanisms underlying the pulmonary toxicity induced by nanomaterials.\n\nDue to its physicochemical and mechanical properties, nanocellulose has found many applications in manufactured goods in the paper and food industry, cosmetics, biomedicine, and pharmaceuticals. There is potential for human exposure to nanocellulose or products that contain nanocellulose both during the production and use of the materials that contain nanocellulose. The objectives of the current study were to determine lung toxicity potential of crystalline nanocellulose (CNC) and the molecular mechanisms underlying the toxicity. A rat inhalation exposure model was employed to determine the lung toxicity potential of CNC. Global gene expression profile in the lung and bioinformatic analysis of the gene expression data were conducted to determine the molecular mechanisms underlying the CNC-induced lung toxicity.",
-            "title": "Lung toxicity and gene expression changes in response to whole-body inhalation exposure to cellulose nanocrystal in rats",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22362,45 +22280,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/aeq9-xksa",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/aeq9-xksa",
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
+            "title": "Lung toxicity and gene expression changes in response to whole-body inhalation exposure to cellulose nanocrystal in rats"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-22",
-            "keyword": [
-                "immunization",
-                "pneumococcal",
-                "shingles",
-                "td",
-                "tdap",
-                "vaccination",
-                "vaccination coverage",
-                "vaxviews",
-                "zoster"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/aetd-68ew",
             "description": "Vaccination Coverage among Adults (18+ Years)\n\n\u2022 Data on adult vaccination coverage from the Behavioral Risk Factor Surveillance System (BRFSS) for the general population at the national, regional, and state levels by age groups.\n\n\u2022 Additional information available at https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html",
-            "title": "Vaccination Coverage among Adults (18+ Years)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22408,56 +22315,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aetd-68ew/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aetd-68ew/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aetd-68ew/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/aetd-68ew",
+            "issued": "2021-07-28",
+            "keyword": [
+                "immunization",
+                "pneumococcal",
+                "shingles",
+                "td",
+                "tdap",
+                "vaccination",
+                "vaccination coverage",
+                "vaxviews",
+                "zoster"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html",
+            "modified": "2025-01-22",
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
+            "title": "Vaccination Coverage among Adults (18+ Years)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-27",
-            "temporal": "1997/2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-27",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:healthus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/aewi-gwni",
             "description": "Data on asthma in children younger than age 18 in the United States, by selected characteristics. Data are from Health, United States. Source: National Center for Health Statistics, National Health Interview Survey.",
-            "title": "Asthma in children younger than age 18, by selected characteristics: United States.",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22465,68 +22383,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aewi-gwni/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aewi-gwni/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aewi-gwni/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/aewi-gwni",
+            "issued": "2024-09-27",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "temporal": "1997/2022",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "Asthma in children younger than age 18, by selected characteristics: United States."
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
-                "name": "data.cdc.gov"
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
@@ -22534,63 +22441,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/afja-b25e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/afja-b25e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/afja-b25e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/afja-b25e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza"
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
-            "temporal": "2019-20, 2020-21, 2021-22, 2022-23, 2023-24 & 2024-25",
-            "modified": "2025-01-31",
-            "keyword": [
-                "flu vaccination",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/agz7-4mvg",
             "description": "\u2022 Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race and Ethnicity, Medicare Fee-For-Service Beneficiaries, Adults aged 65 years and Older\n\n\u2022 Influenza vaccination coverage among Medicare fee-for-service beneficiaries 65 years and older is assessed using data files from the Medicare Fee-For-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS).",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22598,72 +22509,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/agz7-4mvg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/agz7-4mvg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/agz7-4mvg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/agz7-4mvg",
+            "issued": "2025-01-29",
+            "keyword": [
+                "flu vaccination",
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
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States- National",
+            "temporal": "2019-20, 2020-21, 2021-22, 2022-23, 2023-24 & 2024-25",
             "theme": [
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ahrf-yqdt",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "N/A",
-            "issued": "2024-10-04",
-            "@type": "dcat:Dataset",
-            "temporal": "October 1, 2024 - no specified end date",
-            "modified": "2025-01-31",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "disease burden",
-                "hospitalizations",
-                "illnesses",
-                "outpatient visits"
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
-            "identifier": "https://data.cdc.gov/api/views/ahrf-yqdt",
             "description": "This dataset represents preliminary estimates of cumulative U.S. COVID-19 disease burden for the 2024-2025 period, including illnesses, outpatient visits, hospitalizations, and deaths. The weekly COVID-19-associated burden estimates are preliminary and based on continuously collected surveillance data from patients hospitalized with laboratory-confirmed severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) infections. The data come from the Coronavirus Disease 2019 (COVID-19)-Associated Hospitalization Surveillance Network (COVID-NET), a surveillance platform that captures data from hospitals that serve about 10% of the U.S. population. Each week CDC estimates a range (i.e., lower estimate and an upper estimate) of COVID-19 -associated burden that have occurred since October 1, 2024. \n\n<b>Note:</b> Data are preliminary and subject to change as more data become available. Rates for recent COVID-19-associated hospital admissions are subject to reporting delays; as new data are received each week, previous rates are updated accordingly.\n\n<b>References</b>\n<ol><li>Reed C, Chaves SS, Daily Kirley P, et al. Estimating influenza disease burden from population-based surveillance data in the United States. PLoS One. 2015;10(3):e0118369. https://doi.org/10.1371/journal.pone.0118369\u202f </li><li>Rolfes, MA, Foppa, IM, Garg, S, et al. Annual estimates of the burden of seasonal influenza in the United States: A tool for strengthening influenza surveillance and preparedness. Influenza Other Respi Viruses. 2018; 12: 132\u2013 137. https://doi.org/10.1111/irv.12486</li><li>Tokars  JI, Rolfes  MA, Foppa  IM, Reed  C.  An evaluation and update of methods for estimating the number of influenza cases averted by vaccination in the United States.   Vaccine. 2018;36(48):7331-7337. doi:10.1016/j.vaccine.2018.10.026\u202f</li><li>Collier SA, Deng L, Adam EA, Benedict KM, Beshearse EM, Blackstock AJ, Bruce BB, Derado G, Edens C, Fullerton KE, Gargano JW, Geissler AL, Hall AJ, Havelaar AH, Hill VR, Hoekstra RM, Reddy SC, Scallan E, Stokes EK, Yoder JS, Beach MJ. Estimate of Burden and Direct Healthcare Cost of Infectious Waterborne Disease in the United States. Emerg Infect Dis. 2021 Jan;27(1):140-149. doi: 10.3201/eid2701.190676. PMID: 33350905; PMCID: PMC7774540.</li><li>Reed C, Kim IK, Singleton JA,\u202f et al. Estimated influenza illnesses and hospitalizations averted by vaccination\u2013United States, 2013-14 influenza season. MMWR Morb Mortal Wkly Rep. 2014 Dec 12;63(49):1151-4. https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6349a2.htm\u202f</li><li>Reed C, Angulo FJ, Swerdlow DL, et al. Estimates of the Prevalence of Pandemic (H1N1) 2009, United States, April\u2013July 2009. Emerg Infect Dis. 2009;15(12):2004-2007. https://dx.doi.org/10.3201/eid1512.091413 \u202f</li><li>Devine O, Pham H, Gunnels B, et al. Extrapolating Sentinel Surveillance Information to Estimate National COVID-19 Hospital Admission Rates: A Bayesian Modeling Approach. Influenza and Other Respiratory Viruses. https://onlinelibrary.wiley.com/doi/10.1111/irv.70026. Volume18, Issue10. October 2024.</li><li><a ref=\"https://www.cdc.gov/covid/php/covid-net/index.html\">COVID-NET | COVID-19 | CDC\u202f</a></li><li>https://www.cdc.gov/covid/hcp/clinical-care/systematic-review-process.html\u202f </li><li><a ref=\"https://academic.oup.com/pnasnexus/article/1/3/pgac079/6604394?login=false\">Excess natural-cause deaths in California by cause and setting: March 2020 through February 2021 | PNAS Nexus | Oxford Academic (oup.com)</a></li><li>Kruschke, J. K. 2011. Doing Bayesian data analysis: a tutorial with R and BUGS. Elsevier, Amsterdam, Section 3.3.5.</li></ol>",
-            "title": "Preliminary 2024-2025 U.S. COVID-19 Burden Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22671,58 +22579,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ahrf-yqdt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ahrf-yqdt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ahrf-yqdt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ahrf-yqdt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/ahrf-yqdt",
+            "issued": "2024-10-04",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "disease burden",
+                "hospitalizations",
+                "illnesses",
+                "outpatient visits"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ahrf-yqdt",
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
+            "title": "Preliminary 2024-2025 U.S. COVID-19 Burden Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/aian-amjw",
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
-                "name": "data.cdc.gov"
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
@@ -22730,52 +22648,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/aian-amjw",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/aian-amjw",
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
+            "title": "Biological effects of inhaled crude oil vapor. III. Pulmonary effects"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "keyword": [
-                "age",
-                "age group",
-                "census region",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "hispanic origin",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "place of death",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/aie4-agrk",
             "description": "Deaths involving coronavirus disease 2019 (COVID-19) by month of death, region, age, place of death, and race and Hispanic origin.",
-            "title": "AH Monthly Provisional COVID-19 Deaths, by Census Region, Age, and Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22783,45 +22684,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aie4-agrk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aie4-agrk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aie4-agrk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/aie4-agrk",
+            "issued": "2020-09-11",
+            "keyword": [
+                "age",
+                "age group",
+                "census region",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hispanic origin",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "place of death",
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
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Monthly Provisional COVID-19 Deaths, by Census Region, Age, and Race and Hispanic Origin"
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
@@ -22837,64 +22779,35 @@
                 "sexual violence",
                 "stalking"
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
-            "identifier": "https://data.cdc.gov/api/views/airz-k28h",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The fifth round of RANDS (RANDS 5) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from January 1, 2022 to March 9, 2022. RANDS 5 contained the embedded probe questions and experiments as in previous rounds of RANDS. It also examined responses to gender identity questions as well as different survey administrations of questions appearing in CDC\u2019s National Intimate Partner and Sexual Violence Survey (NISVS). RANDS 5 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 5 Restricted File",
-            "describedByType": "application/pdf",
+            "landingPage": "https://data.cdc.gov/d/airz-k28h",
+            "modified": "2023-04-20",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "mediaType": "text/html"
-                }
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS5-technical-documentation.pdf",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/akkj-j5ru",
             "description": "National Immunization Survey-Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent by week for the national-level view, and by month for the jurisdiction-level view.",
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Trends in Vaccination Status and Intent",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22902,44 +22815,91 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/akkj-j5ru/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/akkj-j5ru/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/akkj-j5ru/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/akkj-j5ru/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/akkj-j5ru",
+            "issued": "2022-07-06",
+            "keyword": [
+                "covid-19 vaccination",
+                "covid tracker",
+                "nis-acm"
+            ],
+            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccine-confidence",
+            "modified": "2023-08-03",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Trends in Vaccination Status and Intent"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DRH Public Inquiries",
+                "hasEmail": "mailto:PRAMSProposals@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2006/akmt-4qtj",
+            "description": "2006. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/akmt-4qtj/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/akmt-4qtj/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/akmt-4qtj/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/akmt-4qtj",
+            "issued": "2023-07-19",
             "keyword": [
                 "abuse",
                 "alcohol use",
@@ -22961,94 +22921,37 @@
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
-            "identifier": "https://data.cdc.gov/api/views/akmt-4qtj",
-            "description": "2006. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2006",
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
+            "modified": "2023-09-05",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/akmt-4qtj/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/akmt-4qtj/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/akmt-4qtj/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/akmt-4qtj/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "https://www.cdc.gov/prams/index.htm",
+                "https://www.cdc.gov/prams/pramstat/index.html"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2006/akmt-4qtj",
             "theme": [
                 "Maternal & Child Health"
-            ]
+            ],
+            "title": "CDC PRAMStat Data for 2006"
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
-            "identifier": "https://data.cdc.gov/api/views/akn2-qxic",
             "description": "<b>Note:</b> After May 3, 2024, this dataset will no longer be updated because hospitals are no longer required to report data on COVID-19 hospital admissions, hospital capacity, or occupancy data to HHS through CDC\u2019s National Healthcare Safety Network (NHSN). The related CDC COVID Data Tracker site was revised or retired on May 10, 2023.\n\n<b>Note:</b>\n<b>May 3,2024:</b> Due to incomplete or missing hospital data received for the April 21,2024 through April 27, 2024 reporting period, the COVID-19 Hospital Admissions Level could not be calculated for CNMI and will be reported as \u201cNA\u201d or \u201cNot Available\u201d in the COVID-19 Hospital Admissions Level data released on May 3, 2024.\n\nThis dataset represents COVID-19 hospitalization data and metrics aggregated to county or county-equivalent, for all counties or county-equivalents (including territories) in the United States. COVID-19 hospitalization data are reported to CDC\u2019s National Healthcare Safety Network, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN and included in this dataset represent aggregated counts and include metrics capturing information specific to COVID-19 hospital admissions, and inpatient and ICU bed capacity occupancy.\n\n<b>Reporting information:</b><ul><li>As of December 15, 2022, COVID-19 hospital data are required to be reported to  NHSN, which monitors national and local trends in healthcare system stress, capacity, and community disease levels for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Prior to December 15, 2022, hospitals reported data directly to the U.S. Department of Health and Human Services (HHS) or via a state submission for collection in the HHS Unified Hospital Data Surveillance System (UHDSS). </li><li>While CDC reviews these data for errors and corrects those found, some reporting errors might still exist within the data. To minimize errors and inconsistencies in data reported, CDC removes outliers before calculating the metrics. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks.</li><li>Many hospital subtypes, including acute care and critical access hospitals, as well as Veterans Administration, Defense Health Agency, and Indian Health Service hospitals, are included in the metric calculations provided in this report. Psychiatric, rehabilitation, and religious non-medical hospital types are excluded from calculations.  </li><li>Data are aggregated and displayed for hospitals with the same Centers for Medicare and Medicaid Services (CMS) Certification Number (CCN), which are assigned by CMS to counties based on the CMS Provider of Services files. </li> <li>Full details on COVID-19 hospital data reporting guidance can be found here: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf</li></ul>\n<b>Calculation of county-level hospital metrics:</b><ul><li>County-level hospital data are derived using calculations performed at the Health Service Area (HSA) level. An HSA is defined by CDC\u2019s National Center for Health Statistics as a geographic area containing at least one county which is self-contained with respect to the population\u2019s provision of routine hospital care. Every county in the United States is assigned to an HSA, and each HSA must contain at least one hospital. Therefore, use of HSAs in the calculation of local hospital metrics allows for more accurate characterization of the relationship between health care utilization and health status at the local level. </li><li>Data presented at the county-level represent admissions, hospital inpatient and ICU bed capacity and occupancy among hosp",
-            "title": "Weekly United States COVID-19 Hospitalization Metrics by County \u2013 ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23056,64 +22959,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/akn2-qxic/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/akn2-qxic/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/akn2-qxic/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/akn2-qxic/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/akn2-qxic/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/akn2-qxic/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/akn2-qxic/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/akn2-qxic/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/akn2-qxic/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "inpatient beds",
+                "ncird-corvd"
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
+                "name": "CDC"
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
-            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/child-coverage-vaccination.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024 & 2024-2025",
-            "modified": "2025-01-31",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -23121,65 +23034,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/amjr-ph5r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/amjr-ph5r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/amjr-ph5r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/amjr-ph5r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/amjr-ph5r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/amjr-ph5r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/amjr-ph5r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/amjr-ph5r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/amjr-ph5r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-                "name": "data.cdc.gov"
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
@@ -23187,66 +23101,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/an65-3p9b/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/an65-3p9b/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/an65-3p9b/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/an65-3p9b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/an65-3p9b",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/an65-3p9b",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, HHS Region 1 - Boston"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ap9g-4wiq",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "congenital",
-                "nedss",
-                "netss",
-                "nndss",
-                "primary and secondary",
-                "streptococcal toxic shock syndrome",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ap9g-4wiq",
             "description": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23254,68 +23161,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ap9g-4wiq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ap9g-4wiq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ap9g-4wiq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ap9g-4wiq",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "congenital",
+                "nedss",
+                "netss",
+                "nndss",
+                "primary and secondary",
+                "streptococcal toxic shock syndrome",
+                "syphilis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ap9g-4wiq",
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
+            "title": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary"
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
-                "ncird-corvd",
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
-                "name": "CDC"
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
@@ -23323,69 +23229,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ar8q-3jhn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ar8q-3jhn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ar8q-3jhn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ar8q-3jhn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ar8q-3jhn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ar8q-3jhn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ar8q-3jhn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ar8q-3jhn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ar8q-3jhn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "ncird-corvd",
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
+                "name": "CDC"
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
-                "name": "data.cdc.gov"
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
@@ -23393,67 +23300,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aspp-bzzu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aspp-bzzu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aspp-bzzu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/aspp-bzzu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aspp-bzzu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aspp-bzzu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/aspp-bzzu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/aspp-bzzu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/aspp-bzzu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable"
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
-                "name": "Centers for Disease Control and Prevention National Center for Chronic Disease Prevention and Health Promotion Division of Population Health Population Health Surveillance Branch"
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
@@ -23461,66 +23368,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/at7e-uhkc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/at7e-uhkc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/at7e-uhkc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/at7e-uhkc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/at7e-uhkc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/at7e-uhkc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/at7e-uhkc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/at7e-uhkc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/at7e-uhkc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2025-01-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention National Center for Chronic Disease Prevention and Health Promotion Division of Population Health Population Health Surveillance Branch"
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
-            "landingPage": "https://data.cdc.gov/d/axgy-8qey",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/axgy-8qey",
             "description": "NNDSS - TABLE 1AA.  Poliovirus infection, nonparalytic to Psittacosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1AA.  Poliovirus infection, nonparalytic to Psittacosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23528,66 +23436,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/axgy-8qey/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/axgy-8qey/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/axgy-8qey/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/axgy-8qey/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/axgy-8qey",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/axgy-8qey",
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
+            "title": "NNDSS - TABLE 1AA.  Poliovirus infection, nonparalytic to Psittacosis"
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
-                "name": "data.cdc.gov"
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
@@ -23595,45 +23502,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/axsa-zcg5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/axsa-zcg5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/axsa-zcg5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/axsa-zcg5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/axsa-zcg5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/axsa-zcg5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/axsa-zcg5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/axsa-zcg5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/axsa-zcg5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-medicaid.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-12-20",
-            "temporal": "2015/2017",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/NCHS-TMSIS-MATCH-STATUS.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 22) here: https://www.cdc.gov/nchs/data/datalinkage/2016-nhcs-cms-medicaid-linkage-methodology.pdf",
+            "describedByType": "application/pdf",
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with Medicaid and Children\u2019s Health Insurance Program (CHIP) claims data collected by the Centers for Medicare & Medicaid Services (CMS) Transformed Medicaid Statistical Information System (T-MSIS). Linkage of NHCS patient data with T-MSIS enrollment and claims data creates a new data resource that can support research studies focused on a wide range of patient health outcomes and the association of means-tested government insurance programs with health and health outcomes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ay69-birh",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-12-20",
             "keyword": [
                 "linked medicaid data",
                 "nhcs",
@@ -23644,63 +23584,37 @@
                 "sdoh-use-of-health-care",
                 "t-msis"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCHS Data Linkage Program",
-                "hasEmail": "mailto:DataLinkage@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-medicaid.htm",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/ay69-birh",
-            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with Medicaid and Children\u2019s Health Insurance Program (CHIP) claims data collected by the Centers for Medicare & Medicaid Services (CMS) Transformed Medicaid Statistical Information System (T-MSIS). Linkage of NHCS patient data with T-MSIS enrollment and claims data creates a new data resource that can support research studies focused on a wide range of patient health outcomes and the association of means-tested government insurance programs with health and health outcomes.",
-            "title": "National Hospital Care Survey (NHCS) linked to Centers for Medicare & Medicaid (CMS) Medicaid Data",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/NCHS-TMSIS-MATCH-STATUS.pdf"
             ],
-            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 22) here: https://www.cdc.gov/nchs/data/datalinkage/2016-nhcs-cms-medicaid-linkage-methodology.pdf",
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "temporal": "2015/2017",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Care Survey (NHCS) linked to Centers for Medicare & Medicaid (CMS) Medicaid Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/azgh-hvnt",
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
-            "identifier": "https://data.cdc.gov/api/views/azgh-hvnt",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days),  2012 & 2014, Region 4 - Atlanta",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23708,67 +23622,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/azgh-hvnt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/azgh-hvnt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/azgh-hvnt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/azgh-hvnt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/azgh-hvnt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/azgh-hvnt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/azgh-hvnt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/azgh-hvnt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/azgh-hvnt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/azgh-hvnt",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/azgh-hvnt",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days),  2012 & 2014, Region 4 - Atlanta"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/azmd-939x",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-13",
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
-            "identifier": "https://data.cdc.gov/api/views/azmd-939x",
             "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when restaurants in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data can be used to determine when restaurants in states and territories were subject to closing and reopening requirements through executive orders, administrative orders, resolutions, and proclamations for COVID-19. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level.\n\nThese data are derived from publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly close or reopen restaurants found by the CDC, COVID-19 Community Intervention & Critical Populations Task Force, Monitoring & Evaluation Team, Mitigation Policy Analysis Unit, and the CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 11, 2020 through August 15, 2021.  These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. Effective and expiration dates were coded using only the date provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Orders Closing and Reopening Restaurants Issued from March 11, 2020 through August 15, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23776,66 +23682,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/azmd-939x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/azmd-939x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/azmd-939x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/azmd-939x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/azmd-939x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/azmd-939x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/azmd-939x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/azmd-939x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/azmd-939x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/azmd-939x",
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
+            "landingPage": "https://data.cdc.gov/d/azmd-939x",
+            "modified": "2021-09-13",
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
+            "title": "U.S. State and Territorial Orders Closing and Reopening Restaurants Issued from March 11, 2020 through August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/azpx-5hzx",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/azpx-5hzx",
             "description": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23843,63 +23750,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/azpx-5hzx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/azpx-5hzx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/azpx-5hzx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/azpx-5hzx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/azpx-5hzx",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "hansen's disease",
+                "hantavirus infection",
+                "hantavirus pulmonary syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-hantavirus pulmonary syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/azpx-5hzx",
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
+            "title": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome"
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
-            "keyword": [
-                "age by sex",
-                "census estimates",
-                "osh"
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
@@ -23907,43 +23818,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b2jx-uyck/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b2jx-uyck/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b2jx-uyck/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b2jx-uyck/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b2jx-uyck/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b2jx-uyck/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b2jx-uyck/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b2jx-uyck/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b2jx-uyck/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Tobacco-Use/U-S-Census-Annual-Estimates-of-the-Resident-Popula/b2jx-uyck",
+            "identifier": "https://data.cdc.gov/api/views/b2jx-uyck",
+            "issued": "2025-01-31",
+            "keyword": [
+                "age by sex",
+                "census estimates",
+                "osh"
+            ],
+            "landingPage": "http://www.cdc.gov/STATESystem",
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
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/b2qj-y9ew",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS7-technical-documentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, and questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, along with questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/b2qj-y9ew",
             "issued": "2023-06-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2022",
-            "modified": "2023-06-06",
             "keyword": [
                 "chronic health conditions",
                 "disability",
@@ -23963,72 +23907,35 @@
                 "traumatic brain injury",
                 "vaccination"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/b2qj-y9ew",
+            "modified": "2023-06-06",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/b2qj-y9ew",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, and questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The seventh round of RANDS (RANDS 7) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from November 3, 2022 to December 12, 2022. RANDS 7 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on firearm safety, chronic health conditions, and health and civic behaviors, along with questions related to gender identity, traumatic brain injury and long symptoms of coronavirus disease (COVID-19). RANDS 7 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-                    "@type": "dcat:Distribution",
-                    "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS7-technical-documentation.pdf",
+            "temporal": "2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 7 Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b36e-ru3r",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "2014",
-                "cryptosporidiosis",
-                "dengue fever",
-                "dengue hemorrhagic fever",
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
-            "identifier": "https://data.cdc.gov/api/views/b36e-ru3r",
             "description": "NNDSS - Table II. Cryptosporidiosis to Dengue Hemorrhagic Fever - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd\ufffd Dengue Fever includes cases that meet criteria for Dengue Fever with hemorrhage, other clinical, and unknown case classifications. \ufffd\ufffd DHF includes cases that meet criteria for dengue shock syndrome (DSS), a more severe form of DHF.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue Hemorrhagic Fever",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24036,61 +23943,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b36e-ru3r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b36e-ru3r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b36e-ru3r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b4av-siev",
-            "bureauCode": [
-                "009:00"
-            ],
-            "issued": "2014-04-02",
-            "@type": "dcat:Dataset",
-            "modified": "2017-10-25",
+            "identifier": "https://data.cdc.gov/api/views/b36e-ru3r",
+            "issued": "2015-01-08",
             "keyword": [
-                "brain injury",
-                "head trauma",
-                "tbi",
-                "traumatic brain injury"
+                "2014",
+                "cryptosporidiosis",
+                "dengue fever",
+                "dengue hemorrhagic fever",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/b36e-ru3r",
+            "modified": "2015-08-27",
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
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue Hemorrhagic Fever"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:00"
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
-            "identifier": "https://data.cdc.gov/api/views/b4av-siev",
             "description": "Overall rates of TBI climbed slowly from 2001 through 2007, then spiked sharply in 2008 and continued to climb through 2010.  The increase in TBI rates in 2008 was much sharper for men (nearly 40% increase) than for women (20% increase).  In 2007, overall rates of TBI were 26% higher in men compared to women.  In 2008, that gap began to widen, reaching 61% in 2009 before narrowing to 29% in 2010.  Rates of overall TBI are largely driven by rates of TBI-related ED visits.",
-            "title": "Rates of TBI-related Emergency Department Visits, Hospitalizations, and Deaths by Sex - United States, 2001 \u2013 2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24098,59 +24010,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b4av-siev/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b4av-siev/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b4av-siev/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b4av-siev/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b4av-siev/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b4av-siev/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b4av-siev/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b4av-siev/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b4av-siev/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2017-10-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Traumatic Brain Injury "
-            ]
+            ],
+            "title": "Rates of TBI-related Emergency Department Visits, Hospitalizations, and Deaths by Sex - United States, 2001 \u2013 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b58h-s9zx",
+            "accrualPeriodicity": "Never",
             "bureauCode": [
                 "009:15"
             ],
-            "issued": "2020-07-20",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-25",
-            "keyword": [
-                "covid-19",
-                "provider relief fund"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HRSA Chief Data Officer",
                 "hasEmail": "mailto:PRFdata@hrsa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "HHS ASPA"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b58h-s9zx",
             "description": "The bipartisan CARES Act; the Paycheck Protection Program and Health Care Enhancement Act (PPPHCEA); and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act provided $178 billion in relief funds to hospitals and other healthcare providers on the front lines of the coronavirus response. The Department of Health and Human Services through the Health Resources and Services Administration is distributing two rounds of payments to hospitals in High Impact areas for positive COVID-19 admissions. In the first round of the High Impact Allocation, $12 billion was distributed to nearly 400 hospitals who provided inpatient care for 100 or more COVID-19 patients through April 10, 2020. $2 billion of these payments was distributed to these hospitals based on their Medicare disproportionate share and uncompensated care payments. In the second round of funding, $10 billion will be distributed to hospitals having over 161 COVID-19 admissions between January 1 and June 10, 2020.",
-            "title": "Provider Relief Fund COVID-19 High-Impact Payments",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24158,58 +24073,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b58h-s9zx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b58h-s9zx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b58h-s9zx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b58h-s9zx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/b58h-s9zx",
+            "issued": "2020-07-20",
+            "keyword": [
+                "covid-19",
+                "provider relief fund"
+            ],
+            "landingPage": "https://data.cdc.gov/d/b58h-s9zx",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Never",
+            "modified": "2021-01-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "HHS ASPA"
+            },
+            "spatial": "US",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "Provider Relief Fund COVID-19 High-Impact Payments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/b5mu-3rk7",
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
-            "identifier": "https://data.cdc.gov/api/views/b5mu-3rk7",
             "description": "Triclosan is an antimicrobial chemical incorporated into products that are applied to the skin of healthcare workers. Exposure to triclosan has previously been shown to be immunomodulatory and associated with allergic disease. Additionally, we have shown that exposure to triclosan dermally activates the NLRP3 inflammasome and disrupts the skin barrier integrity in mice. The skin is the largest organ in the body and plays an important role as a physical barrier and regulator of the immune system. Alterations in the barrier and immune regulatory functions of the skin have been demonstrated to increase the risk of sensitization and development of allergic disease. In this study, the impact of triclosan exposure on the skin barrier and keratinocyte function was investigated using a model of reconstructed human epidermis. The apical surface of reconstructed human epidermis was exposed to triclosan once for 6, 24, or 48 hours or daily for 5 consecutive days.",
-            "title": "Exposure to the antimicrobial chemical triclosan disrupts keratinocyte function and skin integrity in a model of reconstructed human epidermis",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24217,56 +24135,37 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b5mu-3rk7",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/b5mu-3rk7",
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
+            "title": "Exposure to the antimicrobial chemical triclosan disrupts keratinocyte function and skin integrity in a model of reconstructed human epidermis"
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
-            "issued": "2024-07-29",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2023",
-            "modified": "2024-12-13",
-            "references": [
-                "https://www.cdc.gov/nchs/data/nhis/SHS_Tech_Notes.pdf"
-            ],
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
                 "fn": "NCHS",
                 "hasEmail": "mailto:CDCINFO@CDC.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b5qi-b3hv",
-            "description": "Interactive Summary Health Statistics for Children provide annual estimates of selected health topics for children under age 18 years based on final data from the National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS NHIS Children Summary Statistics",
-            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "describedBy": "https://www.cdc.gov/nchs/data/nhis/SHS_Tech_Notes.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "Interactive Summary Health Statistics for Children provide annual estimates of selected health topics for children under age 18 years based on final data from the National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24274,53 +24173,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b5qi-b3hv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b5qi-b3hv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b5qi-b3hv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b5qi-b3hv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b5qi-b3hv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b5qi-b3hv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b5qi-b3hv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b5qi-b3hv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b5qi-b3hv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/nhis/SHS_Tech_Notes.pdf",
+            "identifier": "https://data.cdc.gov/api/views/b5qi-b3hv",
+            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "issued": "2024-07-29",
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
+            "landingPage": "https://www.cdc.gov/nchs/nhis/shs.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "annual",
+            "modified": "2024-12-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data/nhis/SHS_Tech_Notes.pdf"
+            ],
+            "rights": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "spatial": "United States",
+            "temporal": "2019-2023",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS NHIS Children Summary Statistics"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b5wa-ze9s",
-            "issued": "2024-12-06",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EMMA BAUBLY",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/b5wa-ze9s",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "CDT_INDIVIDUAL_LINEAGES_BY_WEEK_LOCAL_PIVOTED",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24328,67 +24249,50 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b5wa-ze9s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b5wa-ze9s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b5wa-ze9s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b5wa-ze9s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b5wa-ze9s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b5wa-ze9s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b5wa-ze9s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b5wa-ze9s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b5wa-ze9s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/b5wa-ze9s",
+            "issued": "2024-12-06",
+            "landingPage": "https://data.cdc.gov/d/b5wa-ze9s",
+            "modified": "2025-01-23",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "CDT_INDIVIDUAL_LINEAGES_BY_WEEK_LOCAL_PIVOTED"
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
-                "name": "National Center for Health Statistics"
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
@@ -24396,57 +24300,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b666-c5v5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b666-c5v5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b666-c5v5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b666-c5v5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b666-c5v5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b666-c5v5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b666-c5v5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b666-c5v5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b666-c5v5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/b68w-a53h",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b68w-a53h",
             "description": "We describe design and characterization of an aerosol NanoSpotTM collector, designed for collection of airborne particles on a microscopy substrate for direct electron microscopy, optical microscopy, and laser spectroscopy analysis. The collector implements a water-based, laminar-flow, condensation growth technique, followed by impaction onto an optical/electron microscopy substrate or a transmission electron microscopy grid for direct analysis. The compact design employs three parallel growth tubes allowing a sampling flow rate of 1.2 L min-1. Each of the three growth tubes consists of three-temperature regions, for controlling the water vapor saturation profile and exit dew point. Following the droplet growth, the three streams merge into one flow and a converging nozzle enhances focusing of the grown droplets into a tight beam, prior to their final impaction on the warm surface of the collection substrate. A miniscule sample deposition area is attained for effective coupling with microscopic and spectroscopic analysis. Experiments were conducted for the acquisition of the size-dependent collection efficiency, the uniformity of the spot deposit, the surface density distribution of the collected particles, and the aerosol concentration effect on the triple-tube NanoSpotTM Collector. Particles as small as 7 nm could be activated and collected on the electron microscopy stub. A spot deposit of approximately 0.7-mm diameter is formed for particles over a broad particle diameter range. The collected particle samples were analyzed using electron microscopy and Raman spectroscopy for the acquisition of the particle spatial distribution, the spot sample uniformity, and the analyte concentration. Finally, the NanoSpotTM collector\u2019s analytical measurement sensitivity for laser Raman analysis and the counting statistics for fiber count measurement using optical microscopy were calculated and were compared with those of the conventional aerosol sampling methods.",
-            "title": "NanoSpotTM Collector for Aerosol Sample Collection for Direct Microscopy and Spectroscopy Analysis-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24454,34 +24372,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b68w-a53h",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/b68w-a53h",
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
+            "title": "NanoSpotTM Collector for Aerosol Sample Collection for Direct Microscopy and Spectroscopy Analysis-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/b6fe-yq88",
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
-                "name": "data.cdc.gov"
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
@@ -24489,45 +24407,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b6fe-yq88",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/b6fe-yq88",
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
+            "title": "A Field-Portable Colorimetric Method for the Measurement of Peracetic Acid Vapors: A Comparison of Glass and Plastic Impingers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b6np-zdqj",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "congenital",
-                "nedss",
-                "netss",
-                "nndss",
-                "primary and secondary",
-                "streptococcal toxic shock syndrome",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b6np-zdqj",
             "description": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24535,63 +24442,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6np-zdqj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6np-zdqj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6np-zdqj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6np-zdqj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6np-zdqj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6np-zdqj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6np-zdqj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6np-zdqj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6np-zdqj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b6np-zdqj",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "congenital",
+                "nedss",
+                "netss",
+                "nndss",
+                "primary and secondary",
+                "streptococcal toxic shock syndrome",
+                "syphilis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/b6np-zdqj",
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
+            "title": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary"
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
-            "modified": "2025-01-31",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b6ny-6cd5",
             "description": "\u2022 Monthly Cumulative Percent of Persons Who Received \u22651 Influenza Vaccination Doses and Comparison Between 2024-25 and Two Previous Seasons, by Jurisdiction, United States.\n\n\u2022 Influenza (flu) vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly, in aggregate, by age group (https://www.cdc.gov/iis/about/).",
-            "title": "Monthly Cumulative Number and Percent of Who Received \u22651 Influenza Vaccination Doses and Comparison Between 2024-25 and Two Previous Seasons, by Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24599,72 +24510,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6ny-6cd5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6ny-6cd5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6ny-6cd5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/b6ny-6cd5",
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
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States- National",
+            "temporal": "2022-23, 2023-2024, & 2024-25",
             "theme": [
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Number and Percent of Who Received \u22651 Influenza Vaccination Doses and Comparison Between 2024-25 and Two Previous Seasons, by Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b6sy-qq3u",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/b6sy-qq3u",
             "description": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified) - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24672,64 +24579,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6sy-qq3u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6sy-qq3u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6sy-qq3u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6sy-qq3u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6sy-qq3u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6sy-qq3u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6sy-qq3u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6sy-qq3u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6sy-qq3u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b6sy-qq3u",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "botulism",
+                "foodborne",
+                "infant",
+                "nedss",
+                "netss",
+                "nndss",
+                "other (wound & unspecified)",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/b6sy-qq3u",
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
+            "title": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified)"
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -24737,66 +24647,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6uq-hdgz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6uq-hdgz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6uq-hdgz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6uq-hdgz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6uq-hdgz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6uq-hdgz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b6uq-hdgz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b6uq-hdgz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b6uq-hdgz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-                "name": "HHS ASPA"
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
@@ -24804,61 +24717,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b7pe-5nws/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b7pe-5nws/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b7pe-5nws/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b7pe-5nws/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b7pe-5nws/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b7pe-5nws/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b7pe-5nws/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b7pe-5nws/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b7pe-5nws/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "HHS ASPA"
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
-                "name": "https://www.cdc.gov/ncird/"
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
@@ -24866,61 +24779,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b8tp-jsmh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b8tp-jsmh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b8tp-jsmh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/b8tp-jsmh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b8tp-jsmh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b8tp-jsmh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/b8tp-jsmh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/b8tp-jsmh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/b8tp-jsmh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "https://www.cdc.gov/ncird/"
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
-            "landingPage": "https://data.cdc.gov/d/bbhn-4mdn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-08-05",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "children",
-                "health conditions",
-                "hus"
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
-            "identifier": "https://data.cdc.gov/api/views/bbhn-4mdn",
             "description": "Health, United States is an annual report on trends in health statistics, find more information at http://www.cdc.gov/nchs/hus.htm.",
-            "title": "Selected Trend Table from Health, United States, 2011. Health conditions among children under 18 years of age, by selected characteristics: United States, average annual, selected years 1997 - 1999 through 2008 - 2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24928,55 +24841,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bbhn-4mdn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bbhn-4mdn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bbhn-4mdn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bbhn-4mdn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bbhn-4mdn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bbhn-4mdn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bbhn-4mdn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bbhn-4mdn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bbhn-4mdn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bbhn-4mdn",
+            "issued": "2013-08-05",
+            "keyword": [
+                "children",
+                "health conditions",
+                "hus"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bbhn-4mdn",
+            "modified": "2015-08-27",
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
+            "title": "Selected Trend Table from Health, United States, 2011. Health conditions among children under 18 years of age, by selected characteristics: United States, average annual, selected years 1997 - 1999 through 2008 - 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/bc4h-zh8r",
-            "issued": "2023-06-29",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "v-safe inquiries team",
                 "hasEmail": "mailto:vsafe@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
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
@@ -24984,48 +24902,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bc4h-zh8r",
+            "issued": "2023-06-29",
+            "landingPage": "https://data.cdc.gov/d/bc4h-zh8r",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
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
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "gis",
-                "outcomes",
-                "places",
-                "prevalence",
-                "prevention",
-                "unhealthy",
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
-            "identifier": "https://data.cdc.gov/api/views/bdsk-unrd",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
             "description": "This dataset contains model-based ZIP Code tabulation Areas (ZCTA) level estimates for the PLACES project 2020 release in GIS-friendly format. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census 2010 ZCTA boundary file in a GIS system to produce maps for 27 measures at the ZCTA level. An ArcGIS Online feature service is also available at https://www.arcgis.com/home/item.html?id=8eca985039464f4d83467b8f6aeb1320 for users to make maps online or to add data to desktop GIS software.",
-            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25033,50 +24938,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bdsk-unrd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bdsk-unrd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bdsk-unrd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bdsk-unrd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
+            "identifier": "https://data.cdc.gov/api/views/bdsk-unrd",
+            "issued": "2023-07-19",
+            "keyword": [
+                "behaviors",
+                "gis",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "unhealthy",
+                "zcta",
+                "zip code"
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
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2020 release"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bdyv-z46f",
-            "issued": "2024-07-24",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/bdyv-z46f",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25084,60 +25005,51 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bdyv-z46f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bdyv-z46f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bdyv-z46f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bdyv-z46f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bdyv-z46f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bdyv-z46f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bdyv-z46f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bdyv-z46f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bdyv-z46f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/bdyv-z46f",
+            "issued": "2024-07-24",
+            "landingPage": "https://data.cdc.gov/d/bdyv-z46f",
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
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "accrualPeriodicity": "NA",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-06",
-            "@type": "dcat:Dataset",
-            "temporal": "1999-2018",
-            "modified": "2024-09-17",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/visualization/"
-            ],
-            "keyword": [
-                "dqs",
-                "nhanes"
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
-            "identifier": "https://data.cdc.gov/api/views/be3w-4inw",
+            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "description": "These data represent prevalence estimates of select infectious diseases from the National Health and Nutrition Examination Survey (NHANES). This version of the NHANES dataset is specific to visualization within the NCHS DQS.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS NHANES Select Infectious Diseases Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25145,70 +25057,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/be3w-4inw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/be3w-4inw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/be3w-4inw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "identifier": "https://data.cdc.gov/api/views/be3w-4inw",
+            "issued": "2024-02-06",
+            "keyword": [
+                "dqs",
+                "nhanes"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "NA",
+            "modified": "2024-09-17",
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
+            "title": "DQS NHANES Select Infectious Diseases Prevalence Estimates"
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
-                "name": "data.cdc.gov"
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
@@ -25216,61 +25123,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bfe6-2gyq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bfe6-2gyq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bfe6-2gyq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bfe6-2gyq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bfe6-2gyq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bfe6-2gyq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bfe6-2gyq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bfe6-2gyq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bfe6-2gyq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Mumps to Rabies, animal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bfqg-cb6d",
             "bureauCode": [
                 "009:15"
             ],
-            "issued": "2021-08-02",
-            "@type": "dcat:Dataset",
-            "modified": "2021-08-02",
-            "keyword": [
-                "cares act",
-                "coronavirus",
-                "covid-19",
-                "health system"
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
-            "identifier": "https://data.cdc.gov/api/views/bfqg-cb6d",
             "description": "The bipartisan CARES Act; and the Paycheck Protection Program and Health Care Enhancement Act (PPPHCEA); and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act provided $178 billion in relief funds to hospitals and other healthcare providers on the front lines of the coronavirus response. The Department of Health and Human Services through the Health Resources and Services Administration is allocating $2 billion in incentive payments to nursing home facilities that reduce both COVID-19 infection rates relative to their county and mortality rates against a national benchmark.",
-            "title": "Provider Relief Fund COVID-19 Nursing Home Quality Incentive Program",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25278,67 +25190,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bfqg-cb6d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bfqg-cb6d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bfqg-cb6d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bfqg-cb6d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bfqg-cb6d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bfqg-cb6d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bfqg-cb6d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bfqg-cb6d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bfqg-cb6d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bfqg-cb6d",
+            "issued": "2021-08-02",
+            "keyword": [
+                "cares act",
+                "coronavirus",
+                "covid-19",
+                "health system"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bfqg-cb6d",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2021-08-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "HRSA"
+            },
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "Provider Relief Fund COVID-19 Nursing Home Quality Incentive Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bhxw-k5sb",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bhxw-k5sb",
             "description": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25346,63 +25253,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bhxw-k5sb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bhxw-k5sb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bhxw-k5sb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bhxw-k5sb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bhxw-k5sb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bhxw-k5sb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bhxw-k5sb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bhxw-k5sb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bhxw-k5sb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bhxw-k5sb",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "hansen's disease",
+                "hantavirus infection",
+                "hantavirus pulmonary syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-hantavirus pulmonary syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bhxw-k5sb",
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
+            "title": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome"
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
-                "name": "National Center for Health Statistics"
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
@@ -25410,76 +25320,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bi63-dtpu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bi63-dtpu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bi63-dtpu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bi63-dtpu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bi63-dtpu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bi63-dtpu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bi63-dtpu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bi63-dtpu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bi63-dtpu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
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
-                "name": "CDC"
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
@@ -25487,58 +25387,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bigw-pgk2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bigw-pgk2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bigw-pgk2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
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
-                "name": "data.cdc.gov"
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
@@ -25546,38 +25464,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/biid-68vb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/biid-68vb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/biid-68vb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/biid-68vb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/biid-68vb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/biid-68vb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/biid-68vb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/biid-68vb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/biid-68vb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/biid-68vb",
+            "issued": "2018-08-03",
+            "landingPage": "https://data.cdc.gov/d/biid-68vb",
+            "modified": "2024-07-09",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "Science Clips"
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
+            "description": "Data on functional limitation (or functional difficulties) in adults age 18 and older in the United States, by selected characteristics. Data are from Health, United States. Source: National Center for Health Statistics, National Health Interview Survey. \nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/bjpq-vm2t/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/bjpq-vm2t/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/bjpq-vm2t/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/bjpq-vm2t",
             "issued": "2024-10-15",
-            "temporal": "2010/2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
             "keyword": [
                 "american indian and alaska native only",
                 "asian only",
@@ -25601,83 +25564,34 @@
                 "white non-hispanic",
                 "white only"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:healthus@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bjpq-vm2t",
-            "description": "Data on functional limitation (or functional difficulties) in adults age 18 and older in the United States, by selected characteristics. Data are from Health, United States. Source: National Center for Health Statistics, National Health Interview Survey. \nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Functional difficulties in adults age 18 and older, by selected characteristics: United States",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-05",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/bjpq-vm2t/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/bjpq-vm2t/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/bjpq-vm2t/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "temporal": "2010/2022",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Functional difficulties in adults age 18 and older, by selected characteristics: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bjsc-yd7n",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-28",
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
-            "identifier": "https://data.cdc.gov/api/views/bjsc-yd7n",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 3 - Philadelphia",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25685,65 +25599,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bjsc-yd7n/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bjsc-yd7n/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bjsc-yd7n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bjsc-yd7n/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bjsc-yd7n/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bjsc-yd7n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bjsc-yd7n/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bjsc-yd7n/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bjsc-yd7n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bjsc-yd7n",
+            "issued": "2016-09-28",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bjsc-yd7n",
+            "modified": "2016-09-28",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 3 - Philadelphia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bk9t-cq4b",
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
-                "non-congenital",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bk9t-cq4b",
             "description": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25751,111 +25659,124 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bk9t-cq4b/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bk9t-cq4b/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bk9t-cq4b/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bk9t-cq4b",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-congenital",
+                "wonder",
+                "yellow fever",
+                "zika virus disease"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bk9t-cq4b",
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
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/ahcd/about_ahcd.htm",
+            "accrualPeriodicity": "Database will not be updated again.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
-            "issued": "2022-11-16",
-            "@type": "dcat:Dataset",
-            "temporal": "1973-1981, 1985, 1989-2019",
-            "modified": "2023-11-21",
-            "references": [
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/",
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/namcs_public_use_files/"
-            ],
-            "keyword": [
-                "ambulatory-care",
-                "namcs",
-                "office-based physicians",
-                "physician office visits",
-                "physicians",
-                "visit characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:Ambcare@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bkbr-drkm",
             "description": "The National Ambulatory Medical Care Survey (NAMCS) is a national survey designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. Findings are based on a sample of visits to non-federally employed office-based physicians who are primarily engaged in direct patient care. Physicians in the specialties (including designated sub-specialties) of anesthesiology, pathology, and radiology are excluded from the survey. The survey was conducted annually from 1973 to 1981, again in 1985, and annually since 1989. \nData collection from the physician, rather than from the patient, provides an analytic base that expands information on ambulatory care collected through other NCHS surveys. Data about the physician and their practice characteristics are collected during a survey induction interview.\nFor survey years 1973 to 1991, there are two data files: one for patient visit data and a second for drug mention data. The second file is limited to those visits with mention of medication therapy. For the 1991 data, it is possible to link information on the drug file with information on the patient visit file. Beginning with the 1992 survey year through 2011, one main data file was produced annually that contains both patient visit and drug information.",
-            "title": "National Ambulatory Medical Care Survey, Public-use file, 1973-2019",
-            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/namcs_public_use_files/, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NAMCS/",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/namcs_public_use_files/",
-                    "description": "First link: NAMCS public-use data, 1973-1992\nSecond link: NAMCS public-use data, 1993-2016, 2018, 2019",
                     "@type": "dcat:Distribution",
+                    "description": "First link: NAMCS public-use data, 1973-1992\nSecond link: NAMCS public-use data, 1993-2016, 2018, 2019",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/namcs_public_use_files/",
+                    "mediaType": "text/html",
                     "title": "NAMCS public-use data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NAMCS/",
-                    "description": "First link: NAMCS public-use data, 1973-1992\nSecond link: NAMCS public-use data, 1993-2016, 2018, 2019",
                     "@type": "dcat:Distribution",
+                    "description": "First link: NAMCS public-use data, 1973-1992\nSecond link: NAMCS public-use data, 1993-2016, 2018, 2019",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NAMCS/",
+                    "mediaType": "text/html",
                     "title": "NAMCS public-use data"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/bkbr-drkm",
+            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/namcs_public_use_files/, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NAMCS/",
+            "issued": "2022-11-16",
+            "keyword": [
+                "ambulatory-care",
+                "namcs",
+                "office-based physicians",
+                "physician office visits",
+                "physicians",
+                "visit characteristics"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/about_ahcd.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Database will not be updated again.",
+            "modified": "2023-11-21",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "references": [
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/namcs_public_use_files/"
+            ],
+            "rights": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "spatial": "United States",
+            "temporal": "1973-1981, 1985, 1989-2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey, Public-use file, 1973-2019"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bkcm-ybyk",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/bkcm-ybyk",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25863,63 +25784,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bkcm-ybyk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bkcm-ybyk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bkcm-ybyk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bkcm-ybyk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bkcm-ybyk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bkcm-ybyk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bkcm-ybyk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bkcm-ybyk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bkcm-ybyk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/bkcm-ybyk",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/bkcm-ybyk",
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
-                "name": "data.cdc.gov"
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
@@ -25927,59 +25834,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bkwy-pyv3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bkwy-pyv3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bkwy-pyv3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bkwy-pyv3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bkwy-pyv3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bkwy-pyv3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bkwy-pyv3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bkwy-pyv3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bkwy-pyv3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bptw-uw4i",
-            "bureauCode": [
-                "009:00"
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
             ],
-            "issued": "2016-09-14",
+            "landingPage": "https://data.cdc.gov/d/bkwy-pyv3",
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
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B"
+        },
+        {
             "@type": "dcat:Dataset",
-            "modified": "2016-09-14",
-            "keyword": [
-                "cdc",
-                "centers for disease control and prevention"
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:00"
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
-            "identifier": "https://data.cdc.gov/api/views/bptw-uw4i",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 2 - New York",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25987,64 +25901,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bptw-uw4i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bptw-uw4i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bptw-uw4i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bptw-uw4i",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bptw-uw4i",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 2 - New York"
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
-                "name": "data.cdc.gov"
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
@@ -26052,65 +25961,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bqmb-vyka/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bqmb-vyka/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bqmb-vyka/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bqmb-vyka/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bqmb-vyka/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bqmb-vyka/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bqmb-vyka/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bqmb-vyka/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bqmb-vyka/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1H.  Cholera to Coccidioidomycosis"
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
-                "name": "data.cdc.gov"
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
@@ -26118,60 +26026,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bqse-bujd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bqse-bujd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bqse-bujd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bqse-bujd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bqse-bujd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bqse-bujd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bqse-bujd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bqse-bujd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bqse-bujd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
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
-            "modified": "2024-05-22",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination"
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
-            "identifier": "https://data.cdc.gov/api/views/brsb-akdp",
             "description": "Weekly Cumulative Updated 2023-24 COVID-19 Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years \n\n\u2022 Estimated COVID-19 vaccination coverage among Medicare fee-for-service beneficiaries >65 years is assessed using data files from the Medicare Fee-For-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS).\n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19. (https://www.cdc.gov/coronavirus/2019-ncov/vaccines/stay-up-to-date.html)\n\u2003",
-            "title": "Weekly Cumulative Updated 2023-24 COVID-19 Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26179,61 +26093,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/brsb-akdp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/brsb-akdp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/brsb-akdp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/brsb-akdp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/brsb-akdp",
+            "issued": "2024-02-14",
+            "keyword": [
+                "adults",
+                "covid-19 vaccination"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-05-22",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States- National",
+            "temporal": "2023-2024",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Updated 2023-24 COVID-19 Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/bst4-hnte",
-            "issued": "2023-11-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Kararo",
                 "hasEmail": "mailto:mnr0@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bst4-hnte",
             "description": "",
-            "title": "JMK_DHDS_POC",
-            "programCode": [
-                "009:030"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26241,62 +26159,52 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bst4-hnte/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bst4-hnte/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bst4-hnte/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/bst4-hnte",
+            "issued": "2023-11-20",
+            "landingPage": "https://data.cdc.gov/d/bst4-hnte",
+            "modified": "2023-11-20",
+            "programCode": [
+                "009:030"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "JMK_DHDS_POC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/btcp-84tv",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "acute",
-                "by type) a & b",
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
-            "identifier": "https://data.cdc.gov/api/views/btcp-84tv",
             "description": "NNDSS - Table II. Hepatitis (viral, acute, by type) A & B - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 Perinatal hepatitis C cases are not included in this table. These data will be included in the annual NNDSS tables on the NNDSS Data and Statistics page (https://wwwn.cdc.gov/nndss/data-and-statistics.html) beginning with data year 2018 and in the annual Summary of Viral Hepatitis, published online by CDC's Division of Viral Hepatitis, available at https://www.cdc.gov/hepatitis/statistics/2015surveillance/index.htm.",
-            "title": "NNDSS - Table II. Hepatitis (viral, acute, by type) A & B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26304,55 +26212,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/btcp-84tv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/btcp-84tv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/btcp-84tv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/btcp-84tv",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "acute",
+                "by type) a & b",
+                "hepatitis (viral",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/btcp-84tv",
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
+            "title": "NNDSS - Table II. Hepatitis (viral, acute, by type) A & B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/bucw-etpd",
-            "issued": "2024-12-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Physical Effects Research Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bucw-etpd",
             "description": "Over-exposure of the hand-arm system to intense vibration and force over time may cause degeneration of the vascular, neurological, and musculoskeletal systems in the fingers. A novel animal model using rat tails has been developed to understand the health effects on human fingers exposed to vibration and force when operating powered hand tools or workpieces. The biodynamic responses, such as vibration stress, strain, and power absorption density, of the rat tails can be used to help evaluate the health effects related to vibration and force and to establish a dose-effect relationship. While the biodynamic responses of cadaver rat tails have been investigated, the objective of the current study was to determine whether the biodynamic responses of living rat tails are different from those of cadaver rat tails, and whether the biodynamic responses of both living and cadaver tails change with exposure duration. To make direct comparisons, the responses of both cadaver and living rat tails were examined on four different testing stations. The transfer function of each tail under a given contact force (2 N) was measured at each frequency in the one-third octave bands from 20 to 1000 Hz, and used to calculate the mechanical system parameters of the tails. The transfer function was also measured at different exposure durations to determine the time dependency of the response. The biodynamic responses of both cadaver and living rat tails, and the modeling results and time dependency are presented in a manuscript of this study (Warren et al., 2024), the original datasets measured in each trial of the tests are documented in this data description.",
-            "title": "Rat-Tail Models for Studying Hand-Arm Vibration Syndrome:  A Comparison between Living and Cadaver Rat Tails",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26360,44 +26278,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bucw-etpd",
+            "issued": "2024-12-02",
+            "landingPage": "https://data.cdc.gov/d/bucw-etpd",
+            "modified": "2024-12-02",
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
+            "title": "Rat-Tail Models for Studying Hand-Arm Vibration Syndrome:  A Comparison between Living and Cadaver Rat Tails"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bugr-bbfr",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "flu",
-                "flu shot",
-                "flu vaccination",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bugr-bbfr",
             "description": "Because inventory reporting is no longer required, Vaccines.gov information will not be updated on this site after July 2024.",
-            "title": "Vaccines.gov: Flu vaccinating provider locations",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26405,66 +26313,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bugr-bbfr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bugr-bbfr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bugr-bbfr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bugr-bbfr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bugr-bbfr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bugr-bbfr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bugr-bbfr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bugr-bbfr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bugr-bbfr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bugr-bbfr",
+            "issued": "2021-10-27",
+            "keyword": [
+                "flu",
+                "flu shot",
+                "flu vaccination",
+                "providers",
+                "vaccination locations",
+                "vaccination sites",
+                "vaccinefinder",
+                "vaccines"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bugr-bbfr",
+            "modified": "2024-09-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Flu Vaccinations"
-            ]
+            ],
+            "title": "Vaccines.gov: Flu vaccinating provider locations"
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
@@ -26472,66 +26379,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bumh-rgsq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bumh-rgsq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bumh-rgsq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bumh-rgsq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/bve7-bjy2",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/bve7-bjy2",
             "description": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26539,66 +26446,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bve7-bjy2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bve7-bjy2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bve7-bjy2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bve7-bjy2",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/bve7-bjy2",
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
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bw3b-karf",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "chapare virus",
-                "crimean-congo hemorrhagic fever virus",
-                "ebola virus",
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
-            "identifier": "https://data.cdc.gov/api/views/bw3b-karf",
             "description": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Chapare virus to Ebola virus \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Chapare virus to Ebola virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26606,55 +26513,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bw3b-karf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bw3b-karf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bw3b-karf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bw3b-karf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bw3b-karf",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "chapare virus",
+                "crimean-congo hemorrhagic fever virus",
+                "ebola virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bw3b-karf",
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
+            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Chapare virus to Ebola virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/bwwd-cuna",
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
-            "identifier": "https://data.cdc.gov/api/views/bwwd-cuna",
             "description": "Aspergillus versicolor is ubiquitous in the environment and is particularly abundant in damp indoor spaces. Exposure to Aspergillus species, as well as other environmental fungi, has been linked to adverse health outcomes including asthma, allergy, and even local or disseminated infection. However, the pulmonary immunological mechanisms associated with repeated exposure to A. versicolor have remained relatively uncharacterized. Here, A. versicolor was cultured and desiccated on rice, then placed in an acoustical generator system to achieve aerosolization. Mice were challenged with titrated doses of aerosolized conidia to examine deposition, lymphoproliferative properties, and then the immunotoxicological response to repeated inhalation exposures. The necessary dose to induce lymphoproliferation, but not infection-like pathology, was identified. Further, it was determined that the dose was able to initiate localized immune responses. The data presented in this study demonstrate an optimized and reproducible method for delivering A. versicolor conidia to rodents via nose-only inhalation. Additionally, the feasibility of a long-term repeated exposure study was established.  This experimental protocol can be used in future studies to investigate physiological effects of repeated pulmonary exposure to fungal conidia utilizing a practical and relevant mode of delivery. In total, these data constitute an important foundation for subsequent research in the field.",
-            "title": "Optimization of Aspergillus versicolor culture and aerosolization in a murine model of inhalational fungal exposure",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26662,28 +26580,31 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bwwd-cuna",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/bwwd-cuna",
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
+            "title": "Optimization of Aspergillus versicolor culture and aerosolization in a murine model of inhalational fungal exposure"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bx8m-di6q",
-            "issued": "2024-07-24",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/bx8m-di6q",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26691,38 +26612,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bx8m-di6q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bx8m-di6q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bx8m-di6q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bx8m-di6q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bx8m-di6q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bx8m-di6q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bx8m-di6q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bx8m-di6q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bx8m-di6q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/bx8m-di6q",
+            "issued": "2024-07-24",
+            "landingPage": "https://data.cdc.gov/d/bx8m-di6q",
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
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Final counts of deaths by the month the deaths occurred and by select causes of death for 2014-2019.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/bxq8-mugm/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/bxq8-mugm/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/bxq8-mugm/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/bxq8-mugm",
             "issued": "2021-02-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2014/2019",
-            "modified": "2022-04-04",
             "keyword": [
                 "all causes",
                 "alzheimer disease",
@@ -26750,91 +26713,35 @@
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
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/bxq8-mugm/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/bxq8-mugm/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bxq8-mugm/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/bxq8-mugm/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
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
-            "landingPage": "https://data.cdc.gov/d/bytj-42x7",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "guanarito virus",
-                "junin virus",
-                "lassa virus",
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
-            "identifier": "https://data.cdc.gov/api/views/bytj-42x7",
             "description": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Guanarito virus to Viral hemorrhagic fevers, Lassa virus \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Guanarito virus to Viral hemorrhagic fevers, Lassa virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26842,49 +26749,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bytj-42x7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bytj-42x7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bytj-42x7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bytj-42x7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bytj-42x7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bytj-42x7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bytj-42x7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bytj-42x7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bytj-42x7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bytj-42x7",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "guanarito virus",
+                "junin virus",
+                "lassa virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bytj-42x7",
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
+            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Guanarito virus to Viral hemorrhagic fevers, Lassa virus"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bz96-hgr8",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/bz96-hgr8",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26892,52 +26813,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bz96-hgr8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bz96-hgr8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bz96-hgr8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/bz96-hgr8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bz96-hgr8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bz96-hgr8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/bz96-hgr8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/bz96-hgr8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/bz96-hgr8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/bz96-hgr8",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/bz96-hgr8",
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
-            "landingPage": "https://data.cdc.gov/d/c294-dri5",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Field Studies and Engineering Health Informatics Branch",
                 "hasEmail": "mailto:OHLSurveillance@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/c294-dri5",
             "description": "Background: The purpose of this study was to estimate the incidence and prevalence of hearing loss for noise-exposed U.S. workers by industry sector and 5-year time period, covering 30 years.\n\nMethods: Audiograms for 1.8 million workers from 1981-2010 were examined. Incidence and prevalence were estimated by industry sector and time period. The adjusted risk of incident hearing loss within each time period and industry sector as compared with a reference time period was also estimated.\n\nResults: The adjusted risk for incident hearing loss decreased over time when all industry sectors were combined. However, the risk remained high for workers in Healthcare and Social Assistance, and the prevalence was consistently high for Mining and Construction workers.\n\nConclusions: While progress has been made in reducing the risk of incident hearing loss within most industry sectors, additional efforts are needed within Mining, Construction and Healthcare and Social Assistance.",
-            "title": "Trends in Worker Hearing Loss by Industry Sector, 1981-2010",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26945,34 +26863,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/c294-dri5",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/c294-dri5",
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
+            "title": "Trends in Worker Hearing Loss by Industry Sector, 1981-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/c2hx-eeis",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Personal Protective Technology Laboratory, Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/c2hx-eeis",
             "description": "In 2003, the National Institute for Occupational Safety and Health (NIOSH) conducted a nationwide anthropometric survey of 3,997 subjects. The resulting head and face measurements were used to develop an anthropometric database detailing the face size distributions of respirator users using both traditional measurement methods and three-dimensional (3D) scanning systems. This database was used to establish fit test panels to be incorporated into NIOSH respirator certification and international standards. One of the panels developed, called the principal component analysis (PCA) panel, uses the first two principal components obtained from a set of 10 facial dimensions (age and race adjusted) and divides user population into five face-size categories. These 10 dimensions are associated with respirator fit and leakage and can predict the remaining face dimensions as well. Respirators designed to fit these panels are expected to accommodate more than 95% of the current U.S. civilian workers.\n\nFrom the 3,997 subje",
-            "title": "NIOSH Anthropometric Data and ISO Digital Headforms",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26980,55 +26898,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/c2hx-eeis",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/c2hx-eeis",
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
+            "title": "NIOSH Anthropometric Data and ISO Digital Headforms"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual (R/P1Y)",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "National Center for Health Statistics",
-            "issued": "2024-07-22",
-            "temporal": "1988/2020",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-11",
-            "keyword": [
-                "chronic conditions",
-                "female",
-                "health us",
-                "high blood pressure",
-                "hispanic",
-                "hypertension",
-                "male",
-                "mexican",
-                "national health and nutrition examination survey",
-                "nhanes",
-                "non-hispanic asian",
-                "non-hispanic black",
-                "non-hispanic white",
-                "poverty level",
-                "sdoh-access-to-health-care",
-                "sdoh-poverty-income",
-                "sdoh-use-of-health-care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:healthus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/c49c-tp7w",
             "description": "Data on hypertension in adults age 20 and older in the United States, by selected characteristics. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Hypertension in adults age 20 and older, by selected characteristics: United States.",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27036,56 +26934,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c49c-tp7w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c49c-tp7w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c49c-tp7w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "Annual (R/P1Y)",
+            "identifier": "https://data.cdc.gov/api/views/c49c-tp7w",
+            "issued": "2024-07-22",
+            "keyword": [
+                "chronic conditions",
+                "female",
+                "health us",
+                "high blood pressure",
+                "hispanic",
+                "hypertension",
+                "male",
+                "mexican",
+                "national health and nutrition examination survey",
+                "nhanes",
+                "non-hispanic asian",
+                "non-hispanic black",
+                "non-hispanic white",
+                "poverty level",
+                "sdoh-access-to-health-care",
+                "sdoh-poverty-income",
+                "sdoh-use-of-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "rights": "National Center for Health Statistics",
+            "temporal": "1988/2020",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Hypertension in adults age 20 and older, by selected characteristics: United States."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/c75w-3h6e",
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
-                "name": "data.cdc.gov"
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
@@ -27093,50 +27011,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/c75w-3h6e",
+            "issued": "2024-12-02",
+            "landingPage": "https://data.cdc.gov/d/c75w-3h6e",
+            "modified": "2024-12-02",
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
+            "title": "A High-throughput, Turbulent-mixing, Condensation Aerosol Concentrator for Direct Aerosol Collection as a Liquid Suspension"
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
-            "identifier": "https://data.cdc.gov/api/views/c76y-7pzg",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates for the PLACES 2022 release in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. These data can be joined with the census 2010 ZCTA boundary file in a GIS system to produce maps for 29 measures at the ZCTA level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27144,47 +27047,31 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/c76y-7pzg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c76y-7pzg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c76y-7pzg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/c76y-7pzg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c76y-7pzg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c76y-7pzg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/c76y-7pzg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c76y-7pzg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c76y-7pzg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
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
-            "issued": "2024-07-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/c76y-7pzg",
+            "issued": "2023-06-15",
             "keyword": [
                 "behaviors",
-                "disability",
                 "gis",
                 "health",
                 "outcomes",
@@ -27196,21 +27083,36 @@
                 "zcta",
                 "zip code"
             ],
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
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "theme": [
+                "500 Cities & Places"
+            ],
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2022 release"
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
-            "identifier": "https://data.cdc.gov/api/views/c7b2-4ecy",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the census 2010 ZCTA boundary file in a GIS system to produce maps for 36 measures at the ZCTA level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
-            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27218,56 +27120,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c7b2-4ecy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c7b2-4ecy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c7b2-4ecy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c7b2-4ecy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
+            "identifier": "https://data.cdc.gov/api/views/c7b2-4ecy",
+            "issued": "2024-07-15",
+            "keyword": [
+                "behaviors",
+                "disability",
+                "gis",
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
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2023 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/c8as-e7h6",
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
-                "name": "data.cdc.gov"
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
@@ -27275,66 +27193,55 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/c8as-e7h6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c8as-e7h6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c8as-e7h6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/c8as-e7h6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c8as-e7h6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c8as-e7h6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/c8as-e7h6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/c8as-e7h6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/c8as-e7h6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/c8as-e7h6",
+            "issued": "2022-03-23",
+            "landingPage": "https://data.cdc.gov/d/c8as-e7h6",
+            "modified": "2022-09-25",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
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
-                "name": "data.cdc.gov"
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
@@ -27342,64 +27249,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cah8-bpvk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cah8-bpvk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cah8-bpvk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cah8-bpvk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Lujo virus to Viral hemorrhagic fevers, Marburg virus"
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
-            "identifier": "https://data.cdc.gov/api/views/cchw-gdwa",
+            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/cchw-gdwa",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Success Rates dataset contains success rates for ART cycles started during the year indicated. Since ART success depends on whether patients are using their own eggs or donor eggs, success rates are included separately for these two groups. Success rates for patients using their own eggs are shown per intended retrieval, per actual retrieval, and per transfer. These success rates are reported as cumulative success rates, which take into account transfers that occur within 1 year after an egg retrieval. Since ART success depends on whether patients are using ART for the first time or had prior ART cycles, users can examine success rates for all \u201cPatients using their own eggs\u201d or for \u201cPatients with no prior ART using their own eggs.\u201d For new patients using ART for the first time, the success rates are also shown after 1, 2, or all intended egg retrievals during the reporting year. In addition, the average number of transfers per intended retrieval and the average number of intended retrievals per live-birth delivery are shown. Success rates for ART cycles that involve the transfer of embryos created from donor eggs or donated embryos are shown and are not cumulative. They are based on donor cycles started in the year indicated that had embryo transfers, regardless of when the donor eggs were retrieved. Success rates in this section are not presented by patient age group because previous data show that an intended parent\u2019s age does not substantially affect success when using donor eggs or donated embryos. The success rates are presented by types of embryos and eggs used in the transfer. This dataset excludes cycles that were considered research\u2014that is, cycles performed to evaluate new procedures.",
-            "title": "2022 Final Assisted Reproductive Technology (ART) Success Rates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27407,66 +27317,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cchw-gdwa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cchw-gdwa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cchw-gdwa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/cchw-gdwa",
+            "identifier": "https://data.cdc.gov/api/views/cchw-gdwa",
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
+            "title": "2022 Final Assisted Reproductive Technology (ART) Success Rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cds4-6y7t",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cds4-6y7t",
             "description": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Reporting jurisdictions were informed CDC could receive data for this condition in August 2019. Please note there will be a delay in reporting of case notifications for this condition to CDC.",
-            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27474,74 +27382,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cds4-6y7t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cds4-6y7t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cds4-6y7t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cds4-6y7t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cds4-6y7t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cds4-6y7t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cds4-6y7t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cds4-6y7t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cds4-6y7t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cds4-6y7t",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
+                "chancroid",
+                "chlamydia trachomatis infection",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/cds4-6y7t",
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
+            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
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
-                "respiratory disease",
-                "respiratory illness",
-                "respiratory virus response",
-                "respiratory-virus-response",
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
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cf5u-bm9w",
             "description": "The Coronavirus Disease 2019 (COVID-19) Hospitalization Surveillance Network (COVID-NET) a network that conducts active, population-based surveillance for laboratory-confirmed COVID-19-associated hospitalizations among children and adults. COVID-NET, along with the Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET) and the Influenza Hospitalization Surveillance Network (FluSurv-NET), comprise the Respiratory Virus Hospitalization Surveillance Network (RESP-NET). The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. COVID-NET is CDC\u2019s source for important data on rates of hospitalizations associated with COVID-19. Hospitalization rates show how many people in the surveillance area are hospitalized with COVID-19, compared to the total number of people residing in that area.\n\nData are preliminary and subject to change as more data become available. Data will be updated weekly.",
-            "title": "Monthly Rates of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27549,72 +27448,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cf5u-bm9w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cf5u-bm9w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cf5u-bm9w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cf5u-bm9w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cf5u-bm9w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cf5u-bm9w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cf5u-bm9w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cf5u-bm9w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cf5u-bm9w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "COVID-NET sites",
+            "identifier": "https://data.cdc.gov/api/views/cf5u-bm9w",
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
+                "respiratory disease",
+                "respiratory illness",
+                "respiratory virus response",
+                "respiratory-virus-response",
+                "respnet",
+                "resp-net",
+                "surveillance"
+            ],
+            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "spatial": "COVID-NET sites",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Monthly Rates of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System"
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
-            "temporal": "2022-23 and 2023-24 respiratory illness seasons (2 October 2022 through 31 August 2024; data from last 5 weeks of 2023-24 season not available)",
-            "@type": "dcat:Dataset",
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
-                "name": "CDC"
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
@@ -27622,63 +27526,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ch5i-63ve/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ch5i-63ve/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ch5i-63ve/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ch5i-63ve/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ch5i-63ve/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ch5i-63ve/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ch5i-63ve/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ch5i-63ve/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ch5i-63ve/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
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
+            "modified": "2024-12-26",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
             "spatial": "24 sites/health systems with a total of >100 participating hospitals located in 20 states and the District of Columbia",
-            "accrualPeriodicity": "Never",
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
-            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
-            "keyword": [
-                "beam",
-                "beam dashboard",
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
-            "identifier": "https://data.cdc.gov/api/views/ch83-ush6",
             "description": "The BEAM (Bacteria, Enterics, Amoeba, and Mycotics) Dashboard is an interactive tool to access and visualize data from the System for Enteric Disease Response, Investigation, and Coordination (SEDRIC). The BEAM Dashboard provides timely data on pathogen trends and serotype details to inform work to prevent illnesses from food and animal contact.",
-            "title": "BEAM Dashboard \u2013 Top 30 Most Common Serotypes",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27686,72 +27599,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ch83-ush6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ch83-ush6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ch83-ush6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/ch83-ush6",
+            "issued": "2022-12-15",
+            "keyword": [
+                "beam",
+                "beam dashboard",
+                "escherichia",
+                "salmonella"
+            ],
+            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-16",
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
+            "title": "BEAM Dashboard \u2013 Top 30 Most Common Serotypes"
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
-                "name": "National Center for Health Statistics"
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
@@ -27759,69 +27664,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/chcz-j2du/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/chcz-j2du/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/chcz-j2du/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/chcz-j2du/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-            "landingPage": "https://data.cdc.gov/d/chmz-4uae",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/chmz-4uae",
             "description": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes data for old world hantavirus infections, such as Seoul virus infections. Prior to 2015, this condition was not nationally notifiable and data for this condition was not submitted to CDC's National Notifiable Diseases Surveillance System (NNDSS).\n\u00b6 Includes data for Andes virus infections.",
-            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27829,55 +27736,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/chmz-4uae/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/chmz-4uae/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/chmz-4uae/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/chmz-4uae/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/chmz-4uae",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "hansen's disease",
+                "hantavirus infection",
+                "hantavirus pulmonary syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-hantavirus pulmonary syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/chmz-4uae",
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
+            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/chnh-3rdi",
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
-                "name": "data.cdc.gov"
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
@@ -27885,43 +27803,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/chnh-3rdi",
+            "issued": "2024-11-22",
+            "landingPage": "https://data.cdc.gov/d/chnh-3rdi",
+            "modified": "2024-11-22",
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
+            "title": "Efficacy of powered air-purifying respirators (PAPRs) for source control of simulated respiratory aerosols-dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ci7c-73kg",
+            "accrualPeriodicity": "Archive",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-26",
-            "keyword": [
-                "cases",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "ensemble",
-                "forecast",
-                "model"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Forecasting and Outbreak Analytics",
                 "hasEmail": "mailto:cfadata@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Forecasting and Outbreak Analytics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ci7c-73kg",
             "description": "This dataset contains forecasted weekly numbers of reported COVID-19 incident cases, incident deaths, and cumulative deaths in the United States, previously reported on COVID Data Tracker (https://covid.cdc.gov/covid-data-tracker/#datatracker-home). These forecasts were generated using mathematical models by CDC partners in the COVID-19 Forecast Hub (https://covid19forecasthub.org/doc/ensemble/). A CDC ensemble model was produced every week using the submitted models from that week at the national, and state/territory level. \n\n\nThis dataset is intended to mirror the observed and forecasted data, previously available for download on the CDC\u2019s COVID Data Tracker.  Mortality forecasts for both new and cumulative reported COVID-19 deaths were produced at the state and territory level and national level. Forecasts of new reported COVID-19 cases were produced at the county, state/territory, and national level. Please note that this dataset is not complete for every model, date, location or combination thereof. Specifically, county level submissions for COVID-19 incident cases were accepted, but not required, and are missing or incomplete for many models and dates.  State and territory-level forecasts are more complete, but not all models submitted forecasts for all locations, dates, and targets (new reported deaths, new reported cases, and cumulative reported deaths).  Forecasts for COVID-19 incident cases were discontinued in February 2022. Forecasts for COVID-19 cumulative and incident deaths were discontinued in March 2023.",
-            "title": "CDC COVID-19 Cases and Deaths Ensemble Forecast Archive",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27929,46 +27839,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ci7c-73kg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ci7c-73kg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ci7c-73kg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ci7c-73kg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "National",
+            "identifier": "https://data.cdc.gov/api/views/ci7c-73kg",
+            "issued": "2023-04-26",
+            "keyword": [
+                "cases",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "ensemble",
+                "forecast",
+                "model"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ci7c-73kg",
             "license": "http://creativecommons.org/licenses/by/4.0/legalcode",
-            "accrualPeriodicity": "Archive",
+            "modified": "2023-04-26",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Forecasting and Outbreak Analytics"
+            },
+            "spatial": "National",
             "theme": [
                 "Models"
-            ]
+            ],
+            "title": "CDC COVID-19 Cases and Deaths Ensemble Forecast Archive"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PLACES Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "description": "This dataset contains model-based place (incorporated and census designated places) level estimates for the PLACES 2021 release in GIS-friendly format. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 29 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=024cf3f6f59e49fe8c70e0e5410fe3cf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/cj8b-94cj/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/cj8b-94cj/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/cj8b-94cj/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cj8b-94cj",
+            "issued": "2022-10-11",
             "keyword": [
                 "behaviors",
                 "city",
@@ -27982,62 +27942,66 @@
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
-            "identifier": "https://data.cdc.gov/api/views/cj8b-94cj",
-            "description": "This dataset contains model-based place (incorporated and census designated places) level estimates for the PLACES 2021 release in GIS-friendly format. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 29 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=024cf3f6f59e49fe8c70e0e5410fe3cf",
-            "title": "PLACES: Place Data (GIS Friendly Format), 2021 release",
-            "programCode": [
-                "009:020"
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
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Craig Kassinger",
+                "hasEmail": "mailto:cak8@cdc.gov"
+            },
+            "description": "The Environmental Protection Agency (EPA) provides air pollution data about ozone and particulate matter (PM2.5) to CDC for the Tracking Network. The EPA maintains a database called the Air Quality System (AQS) which contains data from approximately 4,000 monitoring stations around the country, mainly in urban areas. Data from the AQS is considered the \"gold standard\" for determining outdoor air pollution. However, AQS data are limited because the monitoring stations are usually in urban areas or cities and because they only take air samples for some air pollutants every three days or during times of the year when air pollution is very high. CDC and EPA have worked together to develop a statistical model (Downscaler) to make modeled predictions available for environmental public health tracking purposes in areas of the country that do not have monitors and to fill in the time gaps when monitors may not be recording data. This data does not include \"Percent of population in counties exceeding NAAQS (vs. population in counties that either meet the standard or do not monitor PM2.5)\". Please visit the Tracking homepage for this information.View additional information for indicator definitions and documentation by selecting Content Area \"Air Quality\" and the respective indicator at the following website: http://ephtracking.cdc.gov/showIndicatorsData.action",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/cj8b-94cj/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/cjae-szjv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/cj8b-94cj/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/cjae-szjv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/cj8b-94cj/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/cjae-szjv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "500 Cities & Places"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "http://ephtracking.cdc.gov/",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/cjae-szjv",
             "issued": "2015-08-13",
-            "@type": "dcat:Dataset",
-            "modified": "2018-06-05",
             "keyword": [
                 "air pollution",
                 "air quality",
@@ -28069,90 +28033,35 @@
                 "tracking network",
                 "tracking program"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Craig Kassinger",
-                "hasEmail": "mailto:cak8@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Environmental Health Tracking Network"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cjae-szjv",
-            "description": "The Environmental Protection Agency (EPA) provides air pollution data about ozone and particulate matter (PM2.5) to CDC for the Tracking Network. The EPA maintains a database called the Air Quality System (AQS) which contains data from approximately 4,000 monitoring stations around the country, mainly in urban areas. Data from the AQS is considered the \"gold standard\" for determining outdoor air pollution. However, AQS data are limited because the monitoring stations are usually in urban areas or cities and because they only take air samples for some air pollutants every three days or during times of the year when air pollution is very high. CDC and EPA have worked together to develop a statistical model (Downscaler) to make modeled predictions available for environmental public health tracking purposes in areas of the country that do not have monitors and to fill in the time gaps when monitors may not be recording data. This data does not include \"Percent of population in counties exceeding NAAQS (vs. population in counties that either meet the standard or do not monitor PM2.5)\". Please visit the Tracking homepage for this information.View additional information for indicator definitions and documentation by selecting Content Area \"Air Quality\" and the respective indicator at the following website: http://ephtracking.cdc.gov/showIndicatorsData.action",
-            "title": "Air Quality Measures on the National Environmental Health Tracking Network",
+            "landingPage": "http://ephtracking.cdc.gov/",
+            "language": [
+                "English"
+            ],
+            "modified": "2018-06-05",
             "programCode": [
                 "009:032"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/cjae-szjv/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/cjae-szjv/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Environmental Health Tracking Network"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/cjae-szjv/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Environmental Health & Toxicology"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Air Quality Measures on the National Environmental Health Tracking Network"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cjin-8pa3",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
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
-            "identifier": "https://data.cdc.gov/api/views/cjin-8pa3",
             "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses. With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2012 have been variant influenza viruses.",
-            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28160,42 +28069,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjin-8pa3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cjin-8pa3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cjin-8pa3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjin-8pa3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cjin-8pa3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cjin-8pa3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjin-8pa3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cjin-8pa3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cjin-8pa3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cjin-8pa3",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a virus infections",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/cjin-8pa3",
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
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/cjr4-kj3n",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS4_technical_documentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The fourth round of RANDS (RANDS 4) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from July 17, 2020 to August 24, 2020. RANDS 4 contained the embedded probe questions and experiments as in previous rounds of RANDS, but had an emphasis on disability and the use of opioid pain relievers. RANDS 4 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/cjr4-kj3n",
             "issued": "2022-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2020",
-            "modified": "2023-04-20",
             "keyword": [
                 "activities of daily living",
                 "anxiety",
@@ -28213,106 +28155,70 @@
                 "sdoh-social-emotional",
                 "sdoh-workplace"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/cjr4-kj3n",
+            "modified": "2023-04-20",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/cjr4-kj3n",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The fourth round of RANDS (RANDS 4) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from July 17, 2020 to August 24, 2020. RANDS 4 contained the embedded probe questions and experiments as in previous rounds of RANDS, but had an emphasis on disability and the use of opioid pain relievers. RANDS 4 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 4 Restricted File",
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
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS4_technical_documentation.pdf",
+            "temporal": "2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 4 Restricted File"
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
                 "name": "HHS ASPE"
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
@@ -28320,67 +28226,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cpem-dkkm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cpem-dkkm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cpem-dkkm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cpem-dkkm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cpem-dkkm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cpem-dkkm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cpem-dkkm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cpem-dkkm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cpem-dkkm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "data.cdc.gov"
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
@@ -28388,67 +28295,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cqcc-kwwr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cqcc-kwwr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cqcc-kwwr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cqcc-kwwr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cqcc-kwwr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cqcc-kwwr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cqcc-kwwr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cqcc-kwwr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cqcc-kwwr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cr56-k9wj",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-04-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "animal model",
-                "ferret",
-                "flu",
-                "influenza",
-                "in vivo",
-                "ncird",
-                "ncird-id",
-                "pathogenesis",
-                "risk assessment",
-                "virus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jessica Belser",
                 "hasEmail": "mailto:jax6@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cr56-k9wj",
             "description": "Data from influenza A virus (IAV) infected ferrets (Mustela putorius furo) provides invaluable information towards the study of novel and emerging viruses that pose a threat to human health. This gold standard animal model can recapitulate many clinical signs of infection present in IAV-infected humans, support virus replication of human and zoonotic strains without prior adaptation, and permit evaluation of virus transmissibility by multiple modes. While ferrets have been employed in risk assessment settings for >20 years, results from this work are typically reported in discrete stand-alone publications, making aggregation of raw data from this work over time nearly impossible. Here, we describe a dataset of 728 ferrets inoculated with 126 unique IAV, conducted by a single research group (NCIRD/ID/IPB/Pathogenesis Laboratory Team) under a uniform experimental protocol. This collection of morbidity, mortality, and viral titer data represents the largest publicly available dataset to date of in vivo-generated IAV infection outcomes on a per-individual ferret level.\n\nPublished Data Descriptor for more information:\nKieran TJ, Sun X, Creager HM, Tumpey TM, Maine TR, Belser JA. 2024. An aggregated dataset of serial morbidity and titer measurements from influenza A virus-infected ferrets. Sci Data 11, 510. https://doi.org/10.1038/s41597-024-03256-6\n\nAdditional publications using and describing data:\nKieran TJ, Sun X, Maines TR, Beauchemin CAA, Belser JA. 2024. Exploring associations between viral titer measurements and disease outcomes in ferrets inoculated with 125 contemporary influenza A viruses. J Virol98:e01661-23.https://doi.org/10.1128/jvi.01661-23\n\nBelser JA, Kieran TJ, Mitchell ZA, Sun X, Mayfield K, Tumpey TM, Spengler JR, Maines TR. 2024. Key considerations to improve the normalization, interpretation and reproducibility of morbidity data in mammalian models of viral disease. Dis Model Mech; 17 (3): dmm050511. doi: https://doi.org/10.1242/dmm.050511\n\nKieran TJ, Sun X, Maines TR, Belser JA. 2024. Machine learning approaches for influenza A virus risk assessment identifies predictive correlates using ferret model in vivo data. Communications Biology 7, 927. https://doi.org/10.1038/s42003-024-06629-0",
-            "title": "An aggregated dataset of serially collected influenza A virus morbidity and titer measurements from virus-infected ferrets.",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28456,61 +28362,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cr56-k9wj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cr56-k9wj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cr56-k9wj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cr56-k9wj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cr56-k9wj",
+            "issued": "2024-04-08",
+            "keyword": [
+                "animal model",
+                "ferret",
+                "flu",
+                "influenza",
+                "in vivo",
+                "ncird",
+                "ncird-id",
+                "pathogenesis",
+                "risk assessment",
+                "virus"
+            ],
+            "landingPage": "https://data.cdc.gov/d/cr56-k9wj",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-07",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "National Center for Immunization and Respiratory Diseases"
-            ]
+            ],
+            "title": "An aggregated dataset of serially collected influenza A virus morbidity and titer measurements from virus-infected ferrets."
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
-                "name": "data.cdc.gov"
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
@@ -28518,65 +28431,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/crtu-weni/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/crtu-weni/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/crtu-weni/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2015-08-27",
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
+            "title": "Selected Trend Table from Health, United States, 2011. Diabetes prevalence and glycemic control among adults 20 years of age and over, by sex, age, and race and Hispanic origin: United States, selected years 1988 - 1994 through 2003 - 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ctu5-k6yz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/ctu5-k6yz",
             "description": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Please refer to the CDC WONDER publication for weekly updates to the footnote for this condition.",
-            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28584,65 +28492,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ctu5-k6yz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ctu5-k6yz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ctu5-k6yz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ctu5-k6yz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ctu5-k6yz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ctu5-k6yz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ctu5-k6yz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ctu5-k6yz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ctu5-k6yz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ctu5-k6yz",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "hepatitis c",
+                "influenza-associated pediatric mortality",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ctu5-k6yz",
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
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cucp-zsht",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "ehrlichia ewingii infection",
-                "ehrlichiosis and anaplasmosis",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cucp-zsht",
             "description": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Undetermined - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Undetermined",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28650,55 +28558,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cucp-zsht/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cucp-zsht/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cucp-zsht/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cucp-zsht/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cucp-zsht",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "ehrlichia ewingii infection",
+                "ehrlichiosis and anaplasmosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/cucp-zsht",
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
+            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Undetermined"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/cuyd-c53m",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cuyd-c53m",
             "description": "We investigated the suitability of graphitic carbon (GC) content of diesel particulate matter (DPM), measured using Raman spectroscopy, as a surrogate measure of elemental carbon (EC), determined by thermal optical analysis.  Raman spectra in the range of 800-1800 cm-1 (including the D mode at ~1322 cm-1 and the G mode at ~1595 cm-1) were used for GC identification and quantification. Raman spectra for two certified DPM standards (SRM 1650 and SRM 2975), two types of diesel engine exhaust soot, and three types of DPM-enriched workplace aerosols were obtained.",
-            "title": "Correlation between graphitic carbon and elemental carbon in diesel particulate matter in workplace atmospheres-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28706,47 +28624,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cuyd-c53m",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/cuyd-c53m",
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
+            "title": "Correlation between graphitic carbon and elemental carbon in diesel particulate matter in workplace atmospheres-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cvcu-witw",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "(age <5 years)",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cvcu-witw",
             "description": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html\r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28754,65 +28659,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cvcu-witw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cvcu-witw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cvcu-witw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cvcu-witw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cvcu-witw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cvcu-witw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cvcu-witw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cvcu-witw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cvcu-witw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cvcu-witw",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "(age <5 years)",
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
+            "landingPage": "https://data.cdc.gov/d/cvcu-witw",
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
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cw4r-vcr3",
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
-            "identifier": "https://data.cdc.gov/api/views/cw4r-vcr3",
             "description": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28820,71 +28728,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cw4r-vcr3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cw4r-vcr3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cw4r-vcr3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cw4r-vcr3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cw4r-vcr3",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe acute respiratory syndrome-associated coronavirus disease",
+                "shiga toxin-producing escherichia coli (stec)",
+                "shigellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/cw4r-vcr3",
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
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis"
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
@@ -28892,56 +28795,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cwsq-ngmh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cwsq-ngmh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cwsq-ngmh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cwsq-ngmh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/cygf-tgyd",
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
-            "identifier": "https://data.cdc.gov/api/views/cygf-tgyd",
             "description": "Allergic airway diseases are a growing concern in industrialized nations and can be influenced by fungal exposures. Pathogenic yeast species such as Cryptococcus neoformans are known to exacerbate allergic airway disease. Recent indoor assessments have identified Basidiomycota yeasts, including non-pathogenic species such as Vishniacozyma victoriae (syn. Cryptococcus victoriae), to be prevalent and potentially associated with asthma. However, the pulmonary immune response to repeated V. victoriae exposure was previously unexplored. This study aimed to compare the immunological impact of repeated pulmonary exposure to pathogenic and non-pathogenic Cryptococcus yeasts. Mice were repeatedly exposed to either C. neoformans, V. victoriae, or PBS control, and the immune responses were analyzed by measuring histopathological scores, and quantifications of immune cells in the bronchoalveolar lavage fluid or lung via flow cytometry, and cytokine concentrations in the lung. These findings highlight the importance of in vivo characterizations of exposures to frequently detected fungal organisms.",
-            "title": "Persisting Cryptococcus Yeast Species Vishniacozyma victoriae and Cryptococcus neoformans Elicit Unique Airway Inflammation in Mice Following Repeated Exposure",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28949,46 +28867,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cygf-tgyd",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/cygf-tgyd",
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
+            "title": "Persisting Cryptococcus Yeast Species Vishniacozyma victoriae and Cryptococcus neoformans Elicit Unique Airway Inflammation in Mice Following Repeated Exposure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cz39-ahbn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cz39-ahbn",
             "description": "NNDSS - Table 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1A.  Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28996,55 +28902,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cz39-ahbn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cz39-ahbn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/cz39-ahbn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/cz39-ahbn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cz39-ahbn",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/cz39-ahbn",
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
+            "title": "NNDSS - TABLE 1A.  Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/d29v-yfc2",
-            "issued": "2024-12-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-06",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Physical Effects Research Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/d29v-yfc2",
             "description": "Masonry work, a sub-specialty of the construction industry, consists of brick and block-laying. Masonry workers often perform these tasks daily using an elevated work platform (e.g., mast climbers). Mast climbers are elevating equipment used to replace traditional scaffolds. They have been available in the United States since the 1980s.  Mast climbers are capable of handling much greater loads of workers and materials than traditional scaffolding. They also make reaching greater heights much easier, thereby improving efficiency on construction projects. However, working on an unstable work platform at elevation can increase the risks of slips, trips and falls, including falls to a lower level. From 1990 to 2017, there were a total of 35 recorded fatalities associated with the use of mast climbers. Of the 35 fatalities, 13 were masonry workers (OSHA report).  Additionally, working on a mast climber can also create awkward working postures due to the confined nature of the workspace. Masonry work can be physically demanding. Concrete block can weigh between 9-27 kg. The rate of overexertion among masonry workers was 33.4 per 10,000 FTEs compared to the average rate of 21.5 per 10,000 FTEs in all industries (BLS data). Shoulder-assist exoskeletons present an attractive possibility to reduce MSD risks in masonry workers if the exoskeletons do not cause adverse effects to the workers\u2019 stability and balance. \n\nIn this study, we evaluated effects of three models of passive shoulder-assist exoskeletons on balance and shoulder muscle activity during a masonry task on a simulated mast climbing work platform. The balance-related parameters and shoulder muscle activities were compared when using or not using the exoskeletons. We want to evaluate the hypotheses that the exoskeletons (1) reduce shoulder muscle activity and (2) decrease the stability of the workers.",
-            "title": "Shoulder-Assist Exoskeleton Effects on Balance and Muscle Activity During a Block-laying Task on a Simulated Mast Climber",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29052,46 +28970,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
-            "theme": [
-                "National Institute for Occupational Safety and Health"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/BRFSS/",
-            "bureauCode": [
-                "009:20"
+            "identifier": "https://data.cdc.gov/api/views/d29v-yfc2",
+            "issued": "2024-12-06",
+            "landingPage": "https://data.cdc.gov/d/d29v-yfc2",
+            "modified": "2024-12-06",
+            "programCode": [
+                "009:034"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-19",
-            "references": [
-                "http://www.cdc.gov/BRFSS/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
+                "National Institute for Occupational Safety and Health"
             ],
-            "keyword": [
-                "age-adjusted",
-                "behavioral",
-                "brfss",
-                "factor",
-                "risk",
-                "surveillance",
-                "survey"
+            "title": "Shoulder-Assist Exoskeleton Effects on Balance and Muscle Activity During a Block-laying Task on a Simulated Mast Climber"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
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
@@ -29099,68 +29006,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d2rk-yvas/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d2rk-yvas/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d2rk-yvas/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/d2rk-yvas/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d2rk-yvas/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d2rk-yvas/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d2rk-yvas/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d2rk-yvas/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d2rk-yvas/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "ncird-corvd",
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
-                "name": "CDC"
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
@@ -29168,71 +29075,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d2tw-32xv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d2tw-32xv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d2tw-32xv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/d2tw-32xv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d2tw-32xv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d2tw-32xv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d2tw-32xv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d2tw-32xv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d2tw-32xv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "ncird-corvd",
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
+                "name": "CDC"
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
-                "name": "data.cdc.gov"
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
@@ -29240,61 +29145,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d2zt-4m8y/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d2zt-4m8y/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d2zt-4m8y/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/d2zt-4m8y/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d2zt-4m8y/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d2zt-4m8y/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d2zt-4m8y/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d2zt-4m8y/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d2zt-4m8y/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2021-03-01",
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
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype"
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
-                "name": "data.cdc.gov"
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
@@ -29302,64 +29214,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d3c4-tq79/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d3c4-tq79/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d3c4-tq79/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d3c4-tq79/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2018-11-27",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
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
-                "name": "data.cdc.gov"
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
@@ -29367,66 +29276,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d4v7-r7ct/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d4v7-r7ct/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d4v7-r7ct/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/d4v7-r7ct/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d4v7-r7ct/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d4v7-r7ct/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d4v7-r7ct/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d4v7-r7ct/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d4v7-r7ct/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis"
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
-                "name": "data.cdc.gov"
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
@@ -29434,66 +29341,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d69q-iyrb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d69q-iyrb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d69q-iyrb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/d69q-iyrb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d69q-iyrb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d69q-iyrb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d69q-iyrb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d69q-iyrb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d69q-iyrb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d6kj-devz",
-            "bureauCode": [
-                "009:00"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/d69q-iyrb",
             "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
             "keyword": [
                 "2015",
-                "congenital syndrome",
                 "mmwr",
+                "mumps",
                 "nedss",
                 "netss",
                 "nndss",
-                "rubella",
-                "salmonellosis",
+                "pertussis",
+                "rabies animal",
                 "wonder"
             ],
+            "landingPage": "https://data.cdc.gov/d/d69q-iyrb",
+            "modified": "2016-01-07",
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
+            "title": "NNDSS - Table II. Mumps to Rabies, animal"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:00"
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
-            "identifier": "https://data.cdc.gov/api/views/d6kj-devz",
             "description": "NNDSS - Table II. Rubella to Salmonellosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Rubella to Salmonellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29501,56 +29408,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d6kj-devz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d6kj-devz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d6kj-devz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/d6kj-devz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d6kj-devz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d6kj-devz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d6kj-devz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d6kj-devz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d6kj-devz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Rubella to Salmonellosis"
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
-                "name": "CDC"
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
@@ -29558,70 +29476,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d6p8-wqjm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d6p8-wqjm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d6p8-wqjm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/d6p8-wqjm",
+            "issued": "2022-03-22",
+            "landingPage": "https://data.cdc.gov/d/d6p8-wqjm",
+            "language": [
+                "English"
+            ],
+            "modified": "2023-06-09",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
             "spatial": "Select US Jurisdictions",
-            "accrualPeriodicity": "Monthly",
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
-            "landingPage": "https://data.cdc.gov/d/d7xj-2da2",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/d7xj-2da2",
             "description": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29629,62 +29537,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d7xj-2da2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d7xj-2da2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d7xj-2da2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/d7xj-2da2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d7xj-2da2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d7xj-2da2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/d7xj-2da2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/d7xj-2da2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/d7xj-2da2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/d7xj-2da2",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "other serogroups",
+                "unknown serogroup",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/d7xj-2da2",
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
+            "title": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d9eu-6czr",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-05-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
-            "keyword": [
-                "fact sheet",
-                "infographic",
-                "multiunit housing",
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
-            "identifier": "https://data.cdc.gov/api/views/d9eu-6czr",
             "description": "Explore the Going Smokefree Matters \u2013 Multiunit Housing Infographic which outlines key facts related to the effects of secondhand smoke exposure in multiunit housing.",
-            "title": "Going Smokefree Matters - Multiunit Housing Infographic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29692,41 +29603,41 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/d9eu-6czr",
+            "issued": "2016-05-03",
+            "keyword": [
+                "fact sheet",
+                "infographic",
+                "multiunit housing",
+                "secondhand smoke",
+                "smokefree"
+            ],
+            "landingPage": "https://data.cdc.gov/d/d9eu-6czr",
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
+            "title": "Going Smokefree Matters - Multiunit Housing Infographic"
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
-                "infant mortality rates",
-                "nchs",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ddsk-zebd",
             "description": "All birth data by race before 1980 are based on race of the child; starting in 1980, birth data by race are based on race of the mother. Birth data are used to calculate infant mortality rate.\r\n\r\nhttps://www.cdc.gov/nchs/data-visualization/mortality-trends/",
-            "title": "NCHS - Infant Mortality Rates, by Race: United States, 1915-2013",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29734,57 +29645,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ddsk-zebd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ddsk-zebd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ddsk-zebd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ddsk-zebd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/ddsk-zebd",
+            "issued": "2015-07-14",
+            "keyword": [
+                "infant mortality rates",
+                "nchs",
+                "race",
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
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "1915/2013",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Infant Mortality Rates, by Race: United States, 1915-2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/dgwc-f5xf",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Miner Health Branch (MHB), Spokane Mining Research Division (SMRD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dgwc-f5xf",
             "description": "A method for the quantification of airborne organic carbon (OC) and elemental carbon (EC) within aerosolized diesel particulate matter (DPM) is described in the article cited below. DPM is a known carcinogen encountered in many industrial workplaces (notably mining) and in the ambient atmosphere. The method described here collects DPM particles onto a quartz fiber filter, after which reflection-mode infrared spectra are measured on a mid-infrared Fourier transform (FT-IR) spectrometer. Several infrared absorption bands are investigated for their efficacy in quantifying OC and EC. The thermo-optical (T-O) method is used to calibrate a linear regression model to predict OC and EC from the infrared spectra. The calibrated model, generated from laboratory DPM samples, is then utilized to quantify OC and EC in\nmine samples obtained from two metal mine locations under a variety of operating conditions. The feasibility of further improving these results by partial least squares (PLS) regression was investigated. A single calibration that is broadly applicable would be considered an improvement over currently available portable instruments, which require aerosol-specific calibration.",
-            "title": "DPM OC, EC and FT-IR data (Quantifying elemental and organic carbon in diesel particulate matter by mid infrared spectrometry).",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29792,49 +29710,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dgwc-f5xf",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/dgwc-f5xf",
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
+            "title": "DPM OC, EC and FT-IR data (Quantifying elemental and organic carbon in diesel particulate matter by mid infrared spectrometry)."
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
-                "name": "National Center for Health Statistics"
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
@@ -29842,70 +29746,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dh32-cnpq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dh32-cnpq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dh32-cnpq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dh32-cnpq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dh32-cnpq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dh32-cnpq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dh32-cnpq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dh32-cnpq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dh32-cnpq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
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
-            "identifier": "https://data.cdc.gov/api/views/dj4t-wmry",
             "description": "Data on Low birthweight live births, by race and Hispanic origin of mother, state, and territory in the United States and U.S. dependent areas. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Birth File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Low birthweight live births, by race and Hispanic origin of mother, state, and territory: United States and U.S. dependent areas",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29913,62 +29819,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dj4t-wmry/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dj4t-wmry/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dj4t-wmry/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-            "landingPage": "https://aspe.hhs.gov/pdf-report/vaccine-hesitancy",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-05-13",
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
-                "name": "HHS/ASPE"
-            },
-            "identifier": "https://data.cdc.gov/api/views/djj9-kh3p",
             "description": "Due to the change in the survey instrument regarding intention to vaccinate, our estimates for \u201chesitant or unsure\u201d or \u201chesitant\u201d derived from April 14-26, 2021, are not directly comparable with prior Household Pulse Survey data and should not be used to examine trends in hesitancy.\n\nTo support state and local communication and outreach efforts, ASPE developed state, county, and sub-state level predictions of hesitancy rates(https://aspe.hhs.gov/pdf-report/vaccine-hesitancy) using the most recently available federal survey data.\n\nWe estimate hesitancy rates at the state level using the U.S. Census Bureau\u2019s Household Pulse Survey (HPS)(https://www.census.gov/programs-surveys/household-pulse-survey.html) data and utilize the estimated values to predict hesitancy rates in more granular areas using the Census Bureau\u2019s 2019 American Community Survey (ACS) 1-year Public Use Microdata Sample (PUMS)(https://www.census.gov/programs-surveys/acs/microdata.html). Public Use Microdata Areas (PUMA) level \u2013 PUMAs are geographic areas within each state that contain no fewer than 100,000 people. PUMAs can consist of part of a single densely populated county or can combine parts or all of multiple counties that are less densely populated.\n\nThe HPS is nationally representative and includes information on U.S. residents\u2019 intentions to receive the COVID-19 vaccine when available, as well as other sociodemographic and geographic (state, region and metropolitan statistical areas) information. The ACS is a nationally representative survey, and it provides key sociodemographic and geographic (state, region, PUMAs, county) information. We utilized data for the survey collection period May 26, 2021 \u2013 June 7, 2021, which the HPS refers to as Week 31.\n\n\nCounty and State Hesitancy Data - https://data.cdc.gov/Vaccinations/Vaccine-Hesitancy-for-COVID-19-County-and-local-es/q9mh-h2tw",
-            "title": "Vaccine Hesitancy for COVID-19: Public Use Microdata Areas (PUMAs)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29976,74 +29889,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/djj9-kh3p/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/djj9-kh3p/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/djj9-kh3p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/djj9-kh3p/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/djj9-kh3p/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/djj9-kh3p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/djj9-kh3p/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/djj9-kh3p/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/djj9-kh3p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/djj9-kh3p",
+            "issued": "2021-05-13",
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
+                "name": "HHS/ASPE"
+            },
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Vaccine Hesitancy for COVID-19: Public Use Microdata Areas (PUMAs)"
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
@@ -30051,91 +29951,99 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/djk3-k3zs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/djk3-k3zs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/djk3-k3zs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/djk3-k3zs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dkmg-ggf9",
-            "issued": "2017-06-27",
             "@type": "dcat:Dataset",
-            "modified": "2017-09-06",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "jwz3@cdc.gov",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/dkmg-ggf9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "Cleared HIE Assessment Codebook Word",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cdc.gov/download/dkmg-ggf9/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                     "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/dkmg-ggf9",
+            "issued": "2017-06-27",
+            "landingPage": "https://data.cdc.gov/d/dkmg-ggf9",
+            "modified": "2017-09-06",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "Cleared HIE Assessment Codebook Word"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dkyk-v5f5",
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
-            "identifier": "https://data.cdc.gov/api/views/dkyk-v5f5",
             "description": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30143,68 +30051,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dkyk-v5f5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dkyk-v5f5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dkyk-v5f5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dkyk-v5f5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dkyk-v5f5",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe acute respiratory syndrome-associated coronavirus disease",
+                "shiga toxin-producing escherichia coli (stec)",
+                "shigellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/dkyk-v5f5",
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
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dmnu-8erf",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-05-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-12-29/2023-07-29",
-            "modified": "2023-11-02",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "death rate",
-                "deaths",
-                "hhs region",
-                "mortality",
-                "nchs",
-                "nvss",
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
-            "identifier": "https://data.cdc.gov/api/views/dmnu-8erf",
             "description": "This file contains COVID-19 death counts and rates by jurisdiction of residence (U.S., HHS Region) and demographic characteristics (sex, age, race and Hispanic origin, and age/race and Hispanic origin). United States death counts and rates include the 50 states, plus the District of Columbia. \n\nDeaths with confirmed or presumed COVID-19, coded to ICD\u201310 code U07.1. Number of deaths reported in this file are the total number of COVID-19 deaths received and coded as of the date of analysis and may not represent all deaths that occurred in that period. Counts of deaths occurring before or after the reporting period are not included in the file.\n\nData during recent periods are incomplete because of the lag in time between when the death occurred and when the death certificate is completed, submitted to NCHS and processed for reporting purposes. This delay can range from 1 week to 8 weeks or more, depending on the jurisdiction and cause of death.\n\nDeath counts should not be compared across jurisdictions. Data timeliness varies by state. Some states report deaths on a daily basis, while other states report deaths weekly or monthly. \n\nThe ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.\n\nRates were calculated using the population estimates for 2021, which are estimated as of July 1, 2021 based on the Blended Base produced by the US Census Bureau in lieu of the April 1, 2020 decennial population count. The Blended Base consists of the blend of Vintage 2020 postcensal population estimates, 2020 Demographic Analysis Estimates, and 2020 Census PL 94-171 Redistricting File (see https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2020-2021/methods-statement-v2021.pdf).\n\nRate are based on deaths occurring in the specified week and are age-adjusted to the 2000 standard population using the direct method (see https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-08-508.pdf). These rates differ from annual age-adjusted rates, typically presented in NCHS publications based on a full year of data and annualized weekly age-adjusted rates which have been adjusted to allow comparison with annual rates. Annualization rates presents deaths per year per 100,000 population that would be expected in a year if the observed period specific (weekly) rate prevailed for a full year.\n\nSub-national death counts between 1-9 are suppressed in accordance with NCHS data confidentiality standards. Rates based on death counts less than 20 are suppressed in accordance with NCHS standards of reliability as specified in NCHS Data Presentation Standards for Proportions (available from: https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf.).",
-            "title": "Provisional COVID-19 death counts and rates, by jurisdiction of residence and demographic characteristics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30212,84 +30118,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dmnu-8erf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dmnu-8erf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dmnu-8erf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/dmnu-8erf",
+            "issued": "2023-05-10",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "death rate",
+                "deaths",
+                "hhs region",
+                "mortality",
+                "nchs",
+                "nvss",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://data.cdc.gov/d/dmnu-8erf",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-11-02",
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
+            "title": "Provisional COVID-19 death counts and rates, by jurisdiction of residence and demographic characteristics"
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
-            "temporal": "1997-01-01/2018-12-31",
-            "modified": "2023-08-29",
-            "keyword": [
-                "african americans",
-                "age",
-                "alaskan natives",
-                "american natives",
-                "asian continental ancestry group",
-                "continental population groups",
-                "dental care",
-                "european continental ancestry group",
-                "health insurance",
-                "health us",
-                "hispanic americans",
-                "medicaid",
-                "medically uninsured",
-                "oceanic ancestry group",
-                "poverty",
-                "prescription drugs",
-                "prescriptions",
-                "schools",
-                "sdoh-access-to-health-care",
-                "sdoh-higher-eduaction",
-                "sdoh-high-school",
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
-            "identifier": "https://data.cdc.gov/api/views/dmzy-x2ad",
             "description": "Data on delay or nonreceipt of needed medical care, nonreceipt of needed prescription drugs, or nonreceipt of needed dental care during the past 12 months due to cost by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health Interview Survey, Family Core, Sample Child, and Sample Adult questionnaires. Data for level of difficulty are from the 2010 Quality of Life, 2011-2017 Functioning and Disability, and 2018 Sample Adult questionnaires. For more information on the National Health Interview Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Delay or nonreceipt of needed medical care, prescription drugs, or dental care during the past 12 months due to cost: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30297,71 +30190,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dmzy-x2ad/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dmzy-x2ad/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dmzy-x2ad/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dmzy-x2ad/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/dmzy-x2ad",
+            "issued": "2022-04-28",
+            "keyword": [
+                "african americans",
+                "age",
+                "alaskan natives",
+                "american natives",
+                "asian continental ancestry group",
+                "continental population groups",
+                "dental care",
+                "european continental ancestry group",
+                "health insurance",
+                "health us",
+                "hispanic americans",
+                "medicaid",
+                "medically uninsured",
+                "oceanic ancestry group",
+                "poverty",
+                "prescription drugs",
+                "prescriptions",
+                "schools",
+                "sdoh-access-to-health-care",
+                "sdoh-higher-eduaction",
+                "sdoh-high-school",
+                "sdoh-poverty-income",
+                "sex"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-08-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "1997-01-01/2018-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Delay or nonreceipt of needed medical care, prescription drugs, or dental care during the past 12 months due to cost: United States"
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
-                "name": "National Center for Health Statistics"
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
@@ -30369,46 +30275,100 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dnhi-s2bf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dnhi-s2bf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dnhi-s2bf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dnhi-s2bf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dnhi-s2bf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dnhi-s2bf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dnhi-s2bf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dnhi-s2bf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dnhi-s2bf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DRH Public Inquiries",
+                "hasEmail": "mailto:PRAMSProposals@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2002/dnxe-zgxs",
+            "description": "2002.  Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/dnxe-zgxs/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/dnxe-zgxs/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/dnxe-zgxs/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dnxe-zgxs",
+            "issued": "2023-07-19",
             "keyword": [
                 "abuse",
                 "alcohol use",
@@ -30430,90 +30390,36 @@
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
-            "identifier": "https://data.cdc.gov/api/views/dnxe-zgxs",
-            "description": "2002.  Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2002",
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
+            "modified": "2023-09-06",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/dnxe-zgxs/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/dnxe-zgxs/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dnxe-zgxs/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/dnxe-zgxs/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "https://www.cdc.gov/prams/index.htm",
+                "https://www.cdc.gov/prams/pramstat/index.html"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2002/dnxe-zgxs",
             "theme": [
                 "Maternal & Child Health"
-            ]
+            ],
+            "title": "CDC PRAMStat Data for 2002"
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
-                "name": "data.cdc.gov"
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
@@ -30521,55 +30427,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dp9i-idru/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dp9i-idru/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dp9i-idru/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/dqgu-gg5d",
-            "issued": "2022-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Immunization Safety Office",
                 "hasEmail": "mailto:vsafe@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dqgu-gg5d",
             "description": "Users of the v-safe data are required to adhere to the following standards for the analysis and reporting of research data. All research results must be presented and/or published in a manner that protects the confidentiality of participants. v-safe data will not be presented and/or published in any way in which an individual can be identified. \n\nTherefore, users will:\n<ol>\n<li>Not attempt to link or permit others to link the data with individually identified records in another database.</li>\n<li>Not attempt to learn the identity of any participant in the data and will not deliberately combine these data with other CDC or non-CDC data for the purpose of matching records to identify individuals. If you should inadvertently discover the identity of any participant, you will ensure the identity of any participant is kept confidential, and will not be used in any publications and/or presentations.</li>\n<li>Not imply or state, either in written or oral form, that interpretations based on analysis of the data reflect official CDC policies or positions.</li>\n<li>Understand that sub-national analyses are not appropriate for this national sample and will not be conducted. </li>\n<li>Understand that v-safe is a voluntary self-enrollment program requiring smartphone access; therefore, information from v-safe might not be representative or generalizable to the US population.</li></ol>\nBy clicking on the weblink below to download and use these v-safe data, you signify your agreement to comply with the above-stated terms.\n\nv-safe is an active surveillance program to monitor the safety of COVID-19 vaccines during the period when the vaccines are authorized for use under Food and Drug Administration (FDA) Emergency Use Authorization (EUA) and after vaccine licensure. \n \nThese data include registrant information (deidentified), health check-in, and vaccination data collected through v-safe from 12/13/2020 to 06/30/2023. Please review the v-safe data user agreement before analyzing any v-safe data.",
-            "title": "v-safe COVID-19",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30577,45 +30495,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dqgu-gg5d",
+            "issued": "2022-11-30",
+            "landingPage": "https://data.cdc.gov/d/dqgu-gg5d",
+            "modified": "2024-10-31",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "v-safe COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ephtracking.cdc.gov/DataExplorer/#/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-19",
-            "temporal": "2001-2019",
-            "@type": "dcat:Dataset",
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
-                "name": "data.cdc.gov"
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
@@ -30623,67 +30530,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dqwm-pbi7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dqwm-pbi7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dqwm-pbi7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dqwm-pbi7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
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
+            "modified": "2023-09-19",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "spatial": "U.S. states",
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
-                "name": "data.cdc.gov"
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
@@ -30691,68 +30598,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/drfe-vxdh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/drfe-vxdh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/drfe-vxdh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/drfe-vxdh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/drfe-vxdh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/drfe-vxdh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/drfe-vxdh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/drfe-vxdh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/drfe-vxdh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable"
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
-            "identifier": "https://data.cdc.gov/api/views/dt66-w6m6",
             "description": "Reporting of Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\nWeekly COVID-19 Community Levels (CCLs) have been replaced with levels of COVID-19 hospital admission rates (low, medium, or high) which demonstrate <a href=\"https://www.cdc.gov/mmwr/volumes/72/wr/mm7219e1.htm\">>99% concordance</a> by county during February 2022\u2013March 2023. For more information on the latest COVID-19 status levels in your area and hospital admission rates, visit <a href=\"https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-county\">United States COVID-19 Hospitalizations, Deaths, and Emergency Visits by Geographic Area.</a>\n\nThis archived public use dataset contains historical case and percent positivity data updated weekly for all available counties and jurisdictions. Each week, the dataset was refreshed to capture any historical updates. Please note, percent positivity data may be incomplete for the most recent time period.\n\nThis archived public use dataset contains weekly community transmission levels data for all available counties and jurisdictions since October 20, 2022. The dataset was appended to contain the most recent week's data as originally posted on COVID Data Tracker. Historical corrections are not made to these data if new case or testing information become available. A separate archived file is made available here (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">: Weekly COVID-19 County Level of Community Transmission Historical Changes</a>) if historically updated data are desired.\n\n<b>Related data</b> \nCDC provides the public with two active versions of COVID-19 county-level community transmission level data: this dataset with the levels as originally posted (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly Originally Posted dataset</a>), updated weekly with the most recent week\u2019s data since October 20, 2022, and a historical dataset with the county-level transmission data from January 22, 2020 (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">Weekly Historical Changes dataset</a>).  \n \n<b>Methods for calculating county level of community transmission indicator</b> \nThe County Level of Community Transmission indicator uses two metrics: (1) total new COVID-19 cases per 100,000 persons in the last 7 days and (2) percentage of positive SARS-CoV-2 diagnostic nucleic acid amplification tests (NAAT) in the last 7 days. For each of these metrics, CDC classifies transmission values as low, moderate, substantial, or high (below and\u202f<a href=\"https://www.cdc.gov/mmwr/volumes/70/wr/mm7030e2.htm?s_cid=mm7030e2_w#T1_down\">here</a>). If the values for each of these two metrics differ (e.g., one indicates moderate and the other low), then the higher of the two should be used for decision-making. \n \n<b>CDC core metrics of and thresholds for community transmission levels of SARS-CoV-2</b>\n<b>Total New Case Rate Metric:</b> \"New cases per 100,000 persons in the past 7 days\" is calculated by adding the number of new cases in the county (or other administrative level) in the last 7 days divided by the population in the county (or other administrative level) and multiplying by 100,000. \"New cases per 100,000 persons in the past 7 days\" is considered to have a transmission level of Low (0-9.99); Moderate (10.00-49.99); Substantial (50.00-99.99); and High (greater than or equal to 100.00). \n \n<b>Test Percent Positivity Metric:</b> \"Percentage of positive NAAT in the past 7 days\" is calculated by dividing the number of positive tests in the county (or other administrative level) during the last 7 days by the total number of tests conducted",
-            "title": "Weekly COVID-19 County Level of Community Transmission as Originally Posted - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30760,72 +30666,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dt66-w6m6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dt66-w6m6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dt66-w6m6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "laboratory",
+                "ncird-corvd"
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
+                "name": "CDC"
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
-                "sdoh-environmental",
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
-                "name": "National Center for Health Statistics"
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
@@ -30833,69 +30738,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dtm2-meqi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dtm2-meqi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dtm2-meqi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dtm2-meqi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dtm2-meqi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dtm2-meqi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dtm2-meqi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dtm2-meqi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dtm2-meqi/rows.xml?accessType=DOWNLOAD",
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
-            "landingPage": "https://www.cdc.gov/brfss/index.html",
-            "bureauCode": [
-                "009:20"
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
+                "sdoh-environmental",
+                "united states",
+                "urbanicity"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-19",
-            "references": [
-                "http://www.cdc.gov/brfss"
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-04-03",
+            "programCode": [
+                "009:020"
             ],
-            "keyword": [
-                "behavioral",
-                "brfss",
-                "factor",
-                "risk",
-                "survey"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2018-12-01/2020-12-31",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "Provisional Drug Overdose Deaths by Urban/Rural Classification Scheme for 12 month-ending December 2018-December 2020"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DPH Public Inquiries",
                 "hasEmail": "mailto:PublicInquiriesDPH@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for disease control and prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dttw-5yxu",
-            "description": "2011 to present. BRFSS combined land line and cell phone prevalence data. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
-            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Prevalence Data (2011 to present)",
+            "describedBy": "http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "2011 to present. BRFSS combined land line and cell phone prevalence data. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30903,56 +30812,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dttw-5yxu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dttw-5yxu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dttw-5yxu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf",
+            "identifier": "https://data.cdc.gov/api/views/dttw-5yxu",
+            "issued": "2023-07-18",
+            "keyword": [
+                "behavioral",
+                "brfss",
+                "factor",
+                "risk",
+                "survey"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/index.html",
+            "modified": "2024-09-19",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for disease control and prevention"
+            },
+            "references": [
+                "http://www.cdc.gov/brfss"
+            ],
             "theme": [
                 "Behavioral Risk Factors"
-            ]
+            ],
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Prevalence Data (2011 to present)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/dtz3-sij3",
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
-            "identifier": "https://data.cdc.gov/api/views/dtz3-sij3",
             "description": "Three-dimensional printing (3DP) of manufactured goods has increased in the last 10 yrs.  The increased use of this technology has resulted in questions about the health effects of inhaling emissions generated during printing.  The goal of this study was to determine if inhalation of particulate and toxic chemicals generated during printing with polycarbonate (PC) plastic affected the neuroendocrine system.  Male rats were exposed to 3D-printer emissions (500 \u00b5g/cm3) or filtered air for 1, 4, 8, 15 or 30d for 4d/week (4h/day).  The effects of these exposures on hormone concentrations, and markers of function, injury and/or oxidative stress in the olfactory bulb, hypothalamus and testes were measured after 1, 8 and 30d of exposure.  Thirty days of exposure to 3D-emissions resulted in reductions in  thyroid stimulating hormone, follicle stimulating hormone and prolactin.  These changes were accompanied by increases in markers of cell injury and reductions in active mitochondria in the olfactory bulb, gonadotropin releasing hormone cells and fibers and tyrosine hydroxylase immunolabeled fibers in the arcuate nucleus, and reductions in spermatogonium.  PC plastics contain high concentrations bisphenol A and these results are consistent with the hypothesis that the health effects of inhaling 3D-printer emissions may be due to bisphenol A.",
-            "title": "Inhalation of polycarbonate emissions generated during 3D printing processes affects neuroendocrine function in male rats",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30960,49 +30878,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dtz3-sij3",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/dtz3-sij3",
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
+            "title": "Inhalation of polycarbonate emissions generated during 3D printing processes affects neuroendocrine function in male rats"
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
-                "county",
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
-            "identifier": "https://data.cdc.gov/api/views/duw2-7jbt",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
             "description": "This dataset contains model-based county-level estimates for the PLACES 2022 release. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. This dataset includes estimates for 29 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2020 or 2019 county population estimate data, and American Community Survey 2016\u20132020 or 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, County Data 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31010,69 +30914,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/duw2-7jbt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/duw2-7jbt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/duw2-7jbt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/duw2-7jbt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/duw2-7jbt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/duw2-7jbt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/duw2-7jbt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/duw2-7jbt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/duw2-7jbt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
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
-            "issued": "2021-09-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/duw2-7jbt",
+            "issued": "2023-06-15",
             "keyword": [
                 "behaviors",
                 "brfss",
                 "county",
+                "health",
                 "outcomes",
                 "places",
                 "prevalence",
                 "prevention",
-                "unhealthy"
+                "risk",
+                "status"
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
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "theme": [
+                "500 Cities & Places"
+            ],
+            "title": "PLACES: Local Data for Better Health, County Data 2022 release"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PLACES Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dv4u-3x3q",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
             "description": "This dataset contains model-based county-level estimates for the PLACES project 2020 release. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 27 measures: 5 chronic disease-related unhealthy behaviors, 13 health outcomes, and 9 on use of preventive services. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2018 or 2017 county population data, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, County Data 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31080,67 +30986,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dv4u-3x3q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dv4u-3x3q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dv4u-3x3q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dv4u-3x3q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
+            "identifier": "https://data.cdc.gov/api/views/dv4u-3x3q",
+            "issued": "2021-09-29",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "county",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
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
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "PLACES: Local Data for Better Health, County Data 2020 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dwmy-m9r6",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dwmy-m9r6",
             "description": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Before 2019, listeriosis cases in neonates less than or equal to 60 days of age were counted as one case in a mother-infant pair. Beginning in 2019, maternal and neonatal listeriosis cases are being counted separately. Beginning in 2020, confirmed and probable cases are published separately. Prior years included confirmed cases only.",
-            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31148,40 +31055,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dwmy-m9r6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dwmy-m9r6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dwmy-m9r6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dwmy-m9r6",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "confirmed",
+                "leptospirosis",
+                "listeriosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/dwmy-m9r6",
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
+            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable"
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
+                    "describedBy": "https://data.cdc.gov/api/views/dwqk-w36f/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/dwqk-w36f/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/dwqk-w36f/columns.xml",
+                    "describedByType": "application/xml",
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
@@ -31244,68 +31207,63 @@
                 "wonder",
                 "yellow fever"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC INFO",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/dwqk-w36f",
+            "modified": "2017-01-05",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
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
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "500 Cities Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-City-level-Data-GIS-Friendly-Format-201/dxpw-cm5u",
+            "description": "2017, 2016. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level. There are 7 measures (all teeth lost, dental visits, mammograms, Pap tests, colorectal cancer screening, core preventive services among older adults, and sleep less than 7 hours) in this 2019 release from the 2016 BRFSS that were the same as the 2018 release.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/dwqk-w36f/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/dxpw-cm5u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/dwqk-w36f/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/dxpw-cm5u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dwqk-w36f/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/dwqk-w36f/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/dxpw-cm5u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/dxpw-cm5u",
             "issued": "2017-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://academic.oup.com/aje/article/179/8/1025/109078",
-                "https://academic.oup.com/aje/article/182/2/127/93984",
-                "https://www.cdc.gov/pcd/issues/2017/17_0281.htm",
-                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
-            ],
             "keyword": [
                 "500cities",
                 "behaviors",
@@ -31318,87 +31276,38 @@
                 "tract",
                 "unhealthy"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "500 Cities Public Inquiries",
-                "hasEmail": "mailto:places@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/dxpw-cm5u",
-            "description": "2017, 2016. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level. There are 7 measures (all teeth lost, dental visits, mammograms, Pap tests, colorectal cancer screening, core preventive services among older adults, and sleep less than 7 hours) in this 2019 release from the 2016 BRFSS that were the same as the 2018 release.",
-            "title": "500 Cities: City-level Data (GIS Friendly Format), 2019 release",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "modified": "2023-08-25",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/dxpw-cm5u/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/dxpw-cm5u/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/dxpw-cm5u/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "https://academic.oup.com/aje/article/179/8/1025/109078",
+                "https://academic.oup.com/aje/article/182/2/127/93984",
+                "https://www.cdc.gov/pcd/issues/2017/17_0281.htm",
+                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-City-level-Data-GIS-Friendly-Format-201/dxpw-cm5u",
             "theme": [
                 "500 Cities & Places"
-            ]
+            ],
+            "title": "500 Cities: City-level Data (GIS Friendly Format), 2019 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dy4n-fbwg",
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
-            "identifier": "https://data.cdc.gov/api/views/dy4n-fbwg",
             "description": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31406,70 +31315,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dy4n-fbwg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dy4n-fbwg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/dy4n-fbwg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dy4n-fbwg",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "vancomycin-resistant staphylococcus aureus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/dy4n-fbwg",
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
+            "title": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-maternal-deaths.htm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-03-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-01-01/2024-09-30",
-            "modified": "2025-01-29",
-            "keyword": [
-                "age",
-                "age group",
-                "death rates",
-                "deaths",
-                "hispanic origin",
-                "maternal causes",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/e2d5-ggg7",
             "description": "This data presents national-level provisional maternal mortality rates based on a current flow of mortality and natality data in the National Vital Statistics System. Provisional rates which are an early estimate of the number of maternal deaths per 100,000 live births, are shown as of the date specified and may not include all deaths and births that occurred during a given time period (see Technical Notes).\n\nA maternal death is the death of a woman while pregnant or within 42 days of termination of pregnancy irrespective of the duration and the site of the pregnancy, from any cause related to or aggravated by the pregnancy or its management, but not from accidental or incidental causes. In this data visualization, maternal deaths are those deaths with an underlying cause of death assigned to International Statistical Classification of Diseases, 10th Revision (ICD-10) code numbers A34, O00\u2013O95, and O98\u2013O99.\n\nThe provisional data  include reported 12 month-ending provisional maternal mortality rates overall, by age, and by race and Hispanic origin. Provisional maternal mortality rates presented in this data visualization are for \u201c12-month ending periods,\u201d defined as the number of maternal deaths per 100,000 live births occurring in the 12-month period ending in the month indicated. For example, the 12-month ending period in June 2020 would include deaths and births occurring from July 1, 2019, through June 30, 2020. Evaluation of trends over time should compare estimates from year to year (June 2020 and June 2021), rather than month to month, to avoid overlapping time periods. In the visualization and in the accompanying data file, rates based on death counts less than 20 are suppressed in accordance with current NCHS standards of reliability for rates. Death counts between 1-9 in the data file are suppressed in accordance with National Center for Health Statistics (NCHS) confidentiality standards.\n\nProvisional data presented on this page will be updated on a quarterly basis as additional records are received. Previously released estimates are revised to include data and record updates received since the previous release. As a result, the reliability of estimates for a 12-month period ending with a specific month will improve with each quarterly release and estimates for previous time periods may change as new data and updates are received.",
-            "title": "VSRR Provisional Maternal Death Counts and Rates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31477,69 +31381,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e2d5-ggg7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e2d5-ggg7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e2d5-ggg7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/e2d5-ggg7",
+            "issued": "2023-03-10",
+            "keyword": [
+                "age",
+                "age group",
+                "death rates",
+                "deaths",
+                "hispanic origin",
+                "maternal causes",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-maternal-deaths.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2019-01-01/2024-09-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "VSRR Provisional Maternal Death Counts and Rates"
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
@@ -31547,63 +31454,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e539-uadk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e539-uadk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e539-uadk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/e539-uadk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
```

