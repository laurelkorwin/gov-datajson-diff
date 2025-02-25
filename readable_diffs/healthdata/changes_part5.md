# Change History for healthdata.json (Part 5)

### Changes from 31606f9 to dd2190f (Part 4/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                    "description": "Provides access to metadata of all items in the PMC archive, and the full text of a subset of these items. PMC-OAI is an implementation of the Open Archives Initiative Protocol for Metadata Harvesting.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to metadata of all items in the PMC archive, and the full text of a subset of these items. PMC-OAI is an implementation of the Open Archives Initiative Protocol for Metadata Harvesting.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/oai/",
+                    "mediaType": "text/html",
                     "title": "PMC Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH) Service"
                 },
                 {
@@ -41475,51 +41457,41 @@
                     "title": "Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/wm3j-izuq",
+            "issued": "2021-06-30",
+            "keyword": [
+                "api",
+                "dataset",
+                "literature"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/pmc/",
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
+            "title": "PubMed Central (PMC)"
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
@@ -41542,46 +41514,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
+            "identifier": "https://data.cdc.gov/api/views/c76y-7pzg",
+            "issued": "2023-06-15",
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
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2022 release"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -41604,48 +41581,48 @@
                     "mediaType": "application/xml"
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
                 "Flu Vaccinations"
-            ]
+            ],
+            "title": "Vaccines.gov: Flu vaccinating provider locations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-total-enrollment",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/33be6c15-765c-424a-a2bf-a152d79dbd30/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
             "description": "The CMS Program Statistics - Medicare Total Enrollment tables provide data on characteristics of the Medicare-covered populations.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR ENROLL AB 1. \u00a0Total Medicare Enrollment: \u00a0Total, Original Medicare, and Medicare Advantage and Other Health Plan Enrollment, Yearly Trend\n\tMDCR ENROLL AB 2. \u00a0Total Medicare Enrollment: \u00a0Total, Original Medicare, Medicare Advantage and Other Health Plan Enrollment, and Resident Population, by Area of Residence\n\tMDCR ENROLL AB 3. \u00a0Total Medicare Enrollment: \u00a0Part A and/or Part B Total, Aged, and Disabled Enrollees, Yearly Trend\n\tMDCR ENROLL AB 4. \u00a0Total Medicare Enrollment: Part A and/or Part B Enrollees, by Age Group, Yearly Trend\n\tMDCR ENROLL AB 5. \u00a0Total Medicare Enrollment: \u00a0Part A and/or Part B Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 6. \u00a0Total Medicare Enrollment: \u00a0Part A and/or Part B Enrollees, by Type of Entitlement and Demographic Characteristics\n\tMDCR ENROLL AB 7. \u00a0Total Medicare Enrollment: \u00a0Part A and/or Part B Total, Aged, and Disabled Enrollees, by Area of Residence\n\tMDCR ENROLL AB 8. \u00a0Total Medicare Enrollment: \u00a0Part A and/or Part B Enrollees, by Type of Entitlement and Area of Residence",
-            "title": "CMS Program Statistics - Medicare Total Enrollment",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41702,45 +41679,51 @@
                     "title": "CMS Program Statistics - Medicare Total Enrollment : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/33be6c15-765c-424a-a2bf-a152d79dbd30/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "beneficiary enrollment",
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-total-enrollment",
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
+            "title": "CMS Program Statistics - Medicare Total Enrollment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/en5r-5ds4",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/en5r-5ds4",
             "description": "This dataset provides data at the county level for the contiguous United States. It includes monthly Palmer Drought Severity Index (PDSI) data from 1895-2016 provided by the Cooperative Institute for Climate and Satellites - North Carolina. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about drought on the Tracking Network's website: https://ephtracking.cdc.gov/showDroughtLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
-            "title": "Palmer Drought Severity Index, 1895-2016",
-            "programCode": [
-                "009:20"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41763,41 +41746,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/en5r-5ds4",
+            "issued": "2018-07-26",
+            "keyword": [
+                "drought",
+                "environmental health"
+            ],
+            "landingPage": "https://data.cdc.gov/d/en5r-5ds4",
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
+            "title": "Palmer Drought Severity Index, 1895-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK25501/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2012-08-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "api",
-                "biomedicine",
-                "computational biology",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ia8w-5q76",
             "description": "E-utilities (Entrez Programming Utilities) are a set of eight server-side programs that provide a stable interface into the Entrez query and database system at the National Center for Biotechnology Information (NCBI).",
-            "title": "E-utilities (Entrez Programming Utilities)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41806,141 +41787,136 @@
                     "title": "E-utilities Documentation"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ia8w-5q76",
+            "issued": "2012-08-22",
+            "keyword": [
+                "api",
+                "biomedicine",
+                "computational biology",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK25501/",
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
+            "title": "E-utilities (Entrez Programming Utilities)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ai4k-468n",
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
-            "identifier": "73bc163e-e689-5e09-bd18-95f96234a8c9",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet version v2.10.64 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
-                    "description": "CoreSet version v2.10.64 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet version v2.10.64 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet version v2.10.64 (coreset-impl)"
                 }
             ],
+            "identifier": "73bc163e-e689-5e09-bd18-95f96234a8c9",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/ai4k-468n",
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
+            "title": "CoreSet version v2.10.64 (coreset-impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/aibw-v42k",
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
-            "identifier": "1a05ec18-59b9-5d39-a2aa-1e642ca1e192",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet filters v2.10.64 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
-                    "description": "CoreSet filters v2.10.64 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet filters v2.10.64 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet filters v2.10.64 (coreset-etl-test)"
                 }
             ],
+            "identifier": "1a05ec18-59b9-5d39-a2aa-1e642ca1e192",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/aibw-v42k",
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
+            "title": "CoreSet filters v2.10.64 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-outpatient-facility",
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
-                "outpatient facilities",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/41d96997-415c-42fd-b473-81b7640a7ce2/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Outpatient Facility tables provide use and payment data for all outpatient facilities, including hospitals providing outpatient services, rural health clinics, community mental health centers, federally qualified health centers, outpatient dialysis facilities, comprehensive outpatient rehabilitation facilities, and other outpatient facilities.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR OUTPATIENT 1. \u00a0Medicare Outpatient Facilities: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR OUTPATIENT 2. \u00a0Medicare Outpatient Facilities: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR OUTPATIENT 3. \u00a0Medicare Outpatient Facilities: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR OUTPATIENT 4. \u00a0Medicare Outpatient Facilities: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Type of Outpatient Facility\n\tMDCR OUTPATIENT 5. \u00a0Medicare Outpatient Facilities: \u00a0Utilization for Original Medicare Beneficiaries, by Type of Outpatient Facility and Type of Service\n\tMDCR OUTPATIENT 6.\u00a0 Medicare Outpatient Prospective Payment System Hospitals: Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR OUTPATIENT 7.\u00a0 Medicare Outpatient Prospective Payment System Hospitals: Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR OUTPATIENT 8.\u00a0 Medicare Outpatient Prospective Payment System Hospitals: Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR OUTPATIENT 9.\u00a0 Medicare Outpatient Critical Access Hospitals: Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR OUTPATIENT 10.\u00a0 Medicare Outpatient Critical Access Hospitals: Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR OUTPATIENT 11.\u00a0 Medicare Outpatient Critical Access Hospitals: Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Area of Residence",
-            "title": "CMS Program Statistics - Medicare Outpatient Facility",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41997,50 +41973,54 @@
                     "title": "CMS Program Statistics - Medicare Outpatient Facility : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "Medicare"
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/41d96997-415c-42fd-b473-81b7640a7ce2/data-viewer",
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
             ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-outpatient-facility",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
-            "bureauCode": [
-                "009:20"
             ],
-            "issued": "2024-03-04",
-            "@type": "dcat:Dataset",
-            "temporal": "1999-2018",
-            "modified": "2024-10-24",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-03-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "references": [
-                "https://www.cdc.gov/nchs/nhanes/visualization/"
+                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
             ],
-            "keyword": [
-                "chronic conditions",
-                "dqs",
-                "nhanes"
+            "temporal": "2013-01-01/2021-12-31",
+            "theme": [
+                "Medicare"
+            ],
+            "title": "CMS Program Statistics - Medicare Outpatient Facility"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "NA",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCHS",
                 "hasEmail": "mailto:dqs@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mvup-dmxz",
+            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "description": "These data represent prevalence estimates of select chronic conditions from the National Health and Nutrition Examination Survey (NHANES). This version of the dataset is specific for use by the NCHS DQS.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS NHANES Select Chronic Conditions Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42063,23 +42043,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "identifier": "https://data.cdc.gov/api/views/mvup-dmxz",
+            "issued": "2024-03-04",
+            "keyword": [
+                "chronic conditions",
+                "dqs",
+                "nhanes"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "NA",
+            "modified": "2024-10-24",
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
+            "title": "DQS NHANES Select Chronic Conditions Prevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1993",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, anabolic steroids, and tobacco<br />\namong members of United States households aged 12 and older. Data are<br />\nalso provided on treatment for drug use and on illegal activities<br />\nrelated to drug use. Questions include age at first use, as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco,<br />\nand nonmedical use of psychotherapeutics. Respondents were also asked<br />\nabout problems resulting from their use of drugs, alcohol, and<br />\ntobacco, their perceptions of the risks involved, insurance coverage,<br />\nand personal and family income sources and amounts. Demographic data<br />\ninclude gender, race, ethnicity, educational level, job status, income<br />\nlevel, household composition, and population density.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1993) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1993-nid13577",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1993-nid13577"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1993-nid13577",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -42108,95 +42121,63 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1993",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1993-nid13577",
-            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, anabolic steroids, and tobacco<br />\namong members of United States households aged 12 and older. Data are<br />\nalso provided on treatment for drug use and on illegal activities<br />\nrelated to drug use. Questions include age at first use, as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco,<br />\nand nonmedical use of psychotherapeutics. Respondents were also asked<br />\nabout problems resulting from their use of drugs, alcohol, and<br />\ntobacco, their perceptions of the risks involved, insurance coverage,<br />\nand personal and family income sources and amounts. Demographic data<br />\ninclude gender, race, ethnicity, educational level, job status, income<br />\nlevel, household composition, and population density.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1993)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1993-nid13577",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1993) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1993-nid13577"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1993)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/office-inspector-general-list-excluded-individuals-and-entities",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-05-30",
-            "temporal": "2012-05-25T00:00:00-04:00/2012-05-25T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "administrative",
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
-            "identifier": "924f5959-002c-48cd-a3ed-4e34eaf6e867",
-            "description": "<p>The objective is to ensure that providers who bill Federal health care programs do not submit claims for services furnished, ordered or prescribed by an excluded individual or entity.  The LEIE is updated monthly with all individuals and entities who have been excluded from participation in Federal health care programs.  Providers who bill Medicare, Medicaid, or other Federal health care programs must ensure that they know what individuals or entities are excluded and not bill for their services (e.g., a pharmacy should not bill Medicaid for a drug prescribed by an excluded physician nor for drugs dispensed by an excluded pharmacist).</p>",
-            "title": "Office of Inspector General List of Excluded Individuals and Entities",
+            "dataQuality": true,
+            "describedBy": "http://oig.hhs.gov/exclusions/files/leie_record_layout.pdf",
             "describedByType": "application/pdf",
+            "description": "<p>The objective is to ensure that providers who bill Federal health care programs do not submit claims for services furnished, ordered or prescribed by an excluded individual or entity.  The LEIE is updated monthly with all individuals and entities who have been excluded from participation in Federal health care programs.  Providers who bill Medicare, Medicaid, or other Federal health care programs must ensure that they know what individuals or entities are excluded and not bill for their services (e.g., a pharmacy should not bill Medicaid for a drug prescribed by an excluded physician nor for drugs dispensed by an excluded pharmacist).</p>",
+            "identifier": "924f5959-002c-48cd-a3ed-4e34eaf6e867",
+            "issued": "2012-05-30",
+            "keyword": [
+                "administrative",
+                "department-of-health-human-services"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/office-inspector-general-list-excluded-individuals-and-entities",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:076"
             ],
-            "describedBy": "http://oig.hhs.gov/exclusions/files/leie_record_layout.pdf",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "temporal": "2012-05-25T00:00:00-04:00/2012-05-25T00:00:00-04:00",
+            "title": "Office of Inspector General List of Excluded Individuals and Entities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/akjn-ph78",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-09",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
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
-            "identifier": "9e2d6cdf-a835-4b90-a5de-8a6c47eb471d",
             "description": "The Reference Document link for the downable Blood Disorder Treatment Spreadsheet can be accessed below under the Additional Information table under Related Documents.",
-            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 12/1/2024)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42204,44 +42185,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "9e2d6cdf-a835-4b90-a5de-8a6c47eb471d",
+            "issued": "2025-01-09",
+            "keyword": [
+                "drug products"
+            ],
+            "landingPage": "https://healthdata.gov/d/akjn-ph78",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-08",
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
+            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 12/1/2024)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5una-zw6e",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-05-17",
-            "@type": "dcat:Dataset",
-            "temporal": "August 1, 2011 to June 30, 2022",
-            "modified": "2024-05-17",
-            "keyword": [
-                "community mitigation",
-                "emergency preparedness",
-                "influenza",
-                "pandemic preparedness",
-                "school closure",
-                "state and community interventions"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nicole Zviedrite",
                 "hasEmail": "mailto:nzviedrite@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5una-zw6e",
             "description": "Unplanned public K-12 school district and individual school closures due to influenza and influenza-like illness in the United States from August 1, 2011\u2013June 30, 2022.",
-            "title": "Influenza-related School Closures: USA, 2011-2022",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42264,53 +42242,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, 50 States and D.C.",
+            "identifier": "https://data.cdc.gov/api/views/5una-zw6e",
+            "issued": "2024-05-17",
+            "keyword": [
+                "community mitigation",
+                "emergency preparedness",
+                "influenza",
+                "pandemic preparedness",
+                "school closure",
+                "state and community interventions"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5una-zw6e",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-17",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, 50 States and D.C.",
+            "temporal": "August 1, 2011 to June 30, 2022",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Influenza-related School Closures: USA, 2011-2022"
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
@@ -42333,56 +42304,53 @@
                     "mediaType": "application/xml"
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
+            "title": "PLACES: Local Data for Better Health, ZCTA Data 2023 release"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -42405,49 +42373,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/xkb8-kh2a",
+            "issued": "2018-03-06",
+            "keyword": [
+                "cocaine",
+                "deaths",
+                "drug",
+                "drug overdose",
+                "heroin",
+                "methadone",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "opiate",
+                "opioid",
+                "provisional",
+                "psychostimulants",
+                "state",
+                "united states",
+                "vsrr"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/drug-overdose-data.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2015-01-01/2024-08-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "VSRR Provisional Drug Overdose Death Counts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/monthly-prescription-drug-plan-formulary-and-pharmacy-network-information",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-12-15",
-            "temporal": "2019-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/70a9541f-c350-43c3-a3c6-26fe428807de/Methodology-PUF-2025.pdf"
-            ],
-            "keyword": [
-                "all other provider care types",
-                "drugs",
-                "health care use & payments",
-                "medicare",
-                "medicare prescription drug"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Plan Finder - CM",
                 "hasEmail": "mailto:planfinderqa@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/cb2a224f-4d52-4cae-aa55-8c00c671384f/data-viewer",
-            "description": "The Monthly Prescription Drug Plan Formulary and Pharmacy Network Information files contain formulary and pharmacy network data for Medicare Prescription Drug Plans and Medicare Advantage (MA) Prescription Drug Plans (with the exception of employer and Program of All-Inclusive Care for the Elderly plans).\n\n\u00a0\n\nNotice: CMS has identified an issue that resulted in a 15% coinsurance for plans with Defined Standard benefits to be listed rather than a 25% coinsurance in the Beneficiary Cost File under certain scenarios. This issue affected the October 2023 to November 2024 data. CMS will re-post the corrected data in batches between now and May 2025. The following files have already been corrected and re-posted:\n\n\n\tOctober 2024\n\tNovember 2024\n\n\n\u00a0\n\nThese non-identifiable files are available on a monthly basis and are comprised of the following tables:\n\n\n\tPlan Information - Information such as plan name, contract ID, plan ID, service area, and plan type.\n\tGeographic Locator - MA and Prescription Drug Plans region codes and county codes.\n\tBasic Drugs Formulary - Formulary details for each plan including National Drug Codes (NDCs), cost share tier level, and indicators for step therapy, quantity limits, and prior authorization.\n\tExcluded Drugs Formulary - Enhanced alternative plans may elect to provide a supplemental benefit and cover excluded drugs. File includes formulary details for excluded drugs that are covered by the plan (for enhanced alternative plans only).\n\tBeneficiary Cost - Plan level cost sharing details for preferred, non-preferred, and mail order network pharmacies.\n\tPharmacy Network - National Provider Identifier (NPI) numbers for each network pharmacy including preferred, retail, and mail order indicators.\n\tIndication Based Coverage Formulary File - Includes drugs covered based on FDA-approved indication for each plan.\n\tInsulin Beneficiary Cost File - Plan level cost sharing details for insulin at preferred, non-preferred and mail order network pharmacies.\n\n\n\u00a0\n\nThese are large files and can take time to download.\u00a0\n\u00a0\n\nPlease read the \u201cAgreement for Use\u201d in the Resources section below. This document contains important information regarding timeframes for obtaining data as well as data accuracy and integrity.\n\n\u00a0\n\nThe Quarterly Prescription Drug Plan Formulary, Pharmacy Network, and Pricing Information\u00a0is also available to access for the quarterly level information.\u00a0\n\n\u00a0\n\nPlease note:\u00a0The Part D benefit year information for plans become available in October of the year prior. For example, year 2024 data is available in the October, November and December 2023 monthly files. Year 2024 data continues to be available in the January through September 2024 monthly files, then beginning in October of 2024 year 2025 data becomes available.\n\nEstimated release dates for upcoming 2025 monthly data (files reflect data for the month in which the file is released):\n\n\n\t1/29/25\n\t2/26/25\n\t3/26/25\n\t4/23/25\n\t5/21/25\n\t6/18/25\n\t7/30/25\n\t8/27/25\n\t9/24/25\n\n\nFiles older than contract year 2019 can be purchased.",
-            "title": "Monthly Prescription Drug Plan Formulary and Pharmacy Network Information",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/53da33d6-c110-4834-99ad-483980a07269/PUFRecordLayout-2025.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Monthly Prescription Drug Plan Formulary and Pharmacy Network Information files contain formulary and pharmacy network data for Medicare Prescription Drug Plans and Medicare Advantage (MA) Prescription Drug Plans (with the exception of employer and Program of All-Inclusive Care for the Elderly plans).\n\n\u00a0\n\nNotice: CMS has identified an issue that resulted in a 15% coinsurance for plans with Defined Standard benefits to be listed rather than a 25% coinsurance in the Beneficiary Cost File under certain scenarios. This issue affected the October 2023 to November 2024 data. CMS will re-post the corrected data in batches between now and May 2025. The following files have already been corrected and re-posted:\n\n\n\tOctober 2024\n\tNovember 2024\n\n\n\u00a0\n\nThese non-identifiable files are available on a monthly basis and are comprised of the following tables:\n\n\n\tPlan Information - Information such as plan name, contract ID, plan ID, service area, and plan type.\n\tGeographic Locator - MA and Prescription Drug Plans region codes and county codes.\n\tBasic Drugs Formulary - Formulary details for each plan including National Drug Codes (NDCs), cost share tier level, and indicators for step therapy, quantity limits, and prior authorization.\n\tExcluded Drugs Formulary - Enhanced alternative plans may elect to provide a supplemental benefit and cover excluded drugs. File includes formulary details for excluded drugs that are covered by the plan (for enhanced alternative plans only).\n\tBeneficiary Cost - Plan level cost sharing details for preferred, non-preferred, and mail order network pharmacies.\n\tPharmacy Network - National Provider Identifier (NPI) numbers for each network pharmacy including preferred, retail, and mail order indicators.\n\tIndication Based Coverage Formulary File - Includes drugs covered based on FDA-approved indication for each plan.\n\tInsulin Beneficiary Cost File - Plan level cost sharing details for insulin at preferred, non-preferred and mail order network pharmacies.\n\n\n\u00a0\n\nThese are large files and can take time to download.\u00a0\n\u00a0\n\nPlease read the \u201cAgreement for Use\u201d in the Resources section below. This document contains important information regarding timeframes for obtaining data as well as data accuracy and integrity.\n\n\u00a0\n\nThe Quarterly Prescription Drug Plan Formulary, Pharmacy Network, and Pricing Information\u00a0is also available to access for the quarterly level information.\u00a0\n\n\u00a0\n\nPlease note:\u00a0The Part D benefit year information for plans become available in October of the year prior. For example, year 2024 data is available in the October, November and December 2023 monthly files. Year 2024 data continues to be available in the January through September 2024 monthly files, then beginning in October of 2024 year 2025 data becomes available.\n\nEstimated release dates for upcoming 2025 monthly data (files reflect data for the month in which the file is released):\n\n\n\t1/29/25\n\t2/26/25\n\t3/26/25\n\t4/23/25\n\t5/21/25\n\t6/18/25\n\t7/30/25\n\t8/27/25\n\t9/24/25\n\n\nFiles older than contract year 2019 can be purchased.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42882,45 +42861,49 @@
                     "title": "Monthly Prescription Drug Plan Formulary and Pharmacy Network Information : 2019-01-02"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/53da33d6-c110-4834-99ad-483980a07269/PUFRecordLayout-2025.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/cb2a224f-4d52-4cae-aa55-8c00c671384f/data-viewer",
+            "issued": "2023-12-15",
+            "keyword": [
+                "all other provider care types",
+                "drugs",
+                "health care use & payments",
+                "medicare",
+                "medicare prescription drug"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/monthly-prescription-drug-plan-formulary-and-pharmacy-network-information",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/70a9541f-c350-43c3-a3c6-26fe428807de/Methodology-PUF-2025.pdf"
+            ],
+            "temporal": "2019-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Prescription Drug Plan Formulary and Pharmacy Network Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vp9c-m6nq",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-07-29",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "cause of death",
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
-            "identifier": "https://data.cdc.gov/api/views/vp9c-m6nq",
             "description": "Health, United States is an annual report on trends in health statistics, find more information at http://www.cdc.gov/nchs/hus.htm.",
-            "title": "Selected Trend Table from Health, United States, 2011. Leading causes of death and numbers of deaths, by sex, race, and Hispanic origin: United States, 1980 and 2009",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42943,38 +42926,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vp9c-m6nq",
+            "issued": "2013-07-29",
+            "keyword": [
+                "cause of death",
+                "hus"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vp9c-m6nq",
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
+            "title": "Selected Trend Table from Health, United States, 2011. Leading causes of death and numbers of deaths, by sex, race, and Hispanic origin: United States, 1980 and 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/inspsearch/",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-08-31",
-            "keyword": [
-                "ora"
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
-            "identifier": "7731ca41-583e-45b1-b810-2caf33000e39",
             "description": "FDA is disclosing the final inspection classification for inspections related to currently marketed FDA-regulated products. The disclosure of this information is not intended to interfere with planned enforcement actions, therefore some information may be withheld from posting until such action is taken.",
-            "title": "Inspection Database",
-            "programCode": [
-                "009:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42982,57 +42966,36 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "7731ca41-583e-45b1-b810-2caf33000e39",
+            "issued": "2021-02-25",
+            "keyword": [
+                "ora"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/inspsearch/",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-08-31",
+            "programCode": [
+                "009:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Inspection Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/prams/index.htm",
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
-            "identifier": "https://data.cdc.gov/api/views/ese6-rqpq",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2011/ese6-rqpq",
             "description": "2011.  Centers for Disease Control and Prevention (CDC).  PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments.  PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy.\r\nData will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2011",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43055,88 +43018,107 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2011/ese6-rqpq",
+            "identifier": "https://data.cdc.gov/api/views/ese6-rqpq",
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
+            "landingPage": "http://www.cdc.gov/prams/index.htm",
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
+            "title": "CDC PRAMStat Data for 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/aq28-bxdq",
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
-                "managed care",
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
-            "identifier": "89baf100-259b-4763-b9e2-337972f988c4",
             "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by managed care participation (comprehensive managed care, primary care case management, MLTSS, including PACE, behavioral health organizations, nonmedical prepaid health plans, medical-only prepaid health plans, and other).\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topics Enrollment in CMC, Enrollment in PCCM Programs, and Enrollment in BHO Plans. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Managed Care Information for Medicaid and CHIP Beneficiaries by Month",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/ManagedCare-montly.csv",
-                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by managed care participation (comprehensive managed care, primary care case management, MLTSS, including PACE, behavioral health organizations, nonmedical prepaid health plans, medical-only prepaid health plans, and other).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topics Enrollment in CMC, Enrollment in PCCM Programs, and Enrollment in BHO Plans. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by managed care participation (comprehensive managed care, primary care case management, MLTSS, including PACE, behavioral health organizations, nonmedical prepaid health plans, medical-only prepaid health plans, and other).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topics Enrollment in CMC, Enrollment in PCCM Programs, and Enrollment in BHO Plans. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/ManagedCare-montly.csv",
+                    "mediaType": "text/csv",
                     "title": "Managed Care Information for Medicaid and CHIP Beneficiaries by Month"
                 }
             ],
+            "identifier": "89baf100-259b-4763-b9e2-337972f988c4",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "managed care",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/aq28-bxdq",
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
+            "title": "Managed Care Information for Medicaid and CHIP Beneficiaries by Month"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/aq6q-hrms",
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
-            "identifier": "3edfe68f-b783-4e98-9120-20014dd0fe49",
             "description": "The Rate PUF (Rate-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Rate-PUF contains plan-level data on rates based on an eligible subscriber\u2019s age, tobacco use, and geographic location; and family-tier rates.",
-            "title": "Rate PUF \u2013 PY2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43144,35 +43126,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "3edfe68f-b783-4e98-9120-20014dd0fe49",
+            "issued": "2022-08-10",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2022",
+                "rate"
+            ],
+            "landingPage": "https://healthdata.gov/d/aq6q-hrms",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Rate PUF \u2013 PY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/aq6q-qti2",
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
-            "identifier": "b15e4145-8f0a-4790-810f-ef221ff87230",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210913 to 20210919",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43180,38 +43165,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "b15e4145-8f0a-4790-810f-ef221ff87230",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/aq6q-qti2",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210913 to 20210919"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -43234,40 +43216,41 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://www.cdc.gov/nchs/covid19/rands/reduced-access-to-care.htm",
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
-            "identifier": "https://data.cdc.gov/api/views/th9n-ghnr",
             "description": "The Research and Development Survey (RANDS) is a platform designed for conducting survey question evaluation and statistical research. RANDS is an ongoing series of surveys from probability-sampled commercial survey panels used for methodological research at the National Center for Health Statistics (NCHS). RANDS estimates are generated using an experimental approach that differs from the survey design approaches generally used by NCHS, including possible biases from different response patterns and sampling frames as well as increased variability from lower sample sizes. Use of the RANDS platform allows NCHS to produce more timely data than would be possible using traditional data collection methods. RANDS is not designed to replace NCHS\u2019 higher quality, core data collections. Below are experimental estimates of reduced access to healthcare for three rounds of RANDS during COVID-19. Data collection for the three rounds of RANDS during COVID-19 occurred between June 9, 2020 and July 6, 2020, August 3, 2020 and August 20, 2020, and May 17, 2021 and June 30, 2021. Information needed to interpret these estimates can be found in the Technical Notes. RANDS during COVID-19 included questions about unmet care in the last 2 months during the coronavirus pandemic. Unmet needs for health care are often the result of cost-related barriers. The National Health Interview Survey, conducted by NCHS, is the source for high-quality data to monitor cost-related health care access problems in the United States. For example, in 2018, 7.3% of persons of all ages reported delaying medical care due to cost and 4.8% reported needing medical care but not getting it due to cost in the past year. However, cost is not the only reason someone might delay or not receive needed medical care. As a result of the coronavirus pandemic, people also may not get needed medical care due to cancelled appointments, cutbacks in transportation options, fear of going to the emergency room, or an altruistic desire to not be a burden on the health care system, among other reasons. The Household Pulse Survey (https://www.cdc.gov/nchs/covid19/pulse/reduced-access-to-care.htm), an online survey conducted in response to the COVID-19 pandemic by the Census Bureau in partnership with other federal agencies including NCHS, also reports estimates of reduced access to care during the pandemic (beginning in Phase 1, which started on April 23, 2020). The Household Pulse Survey reports the percentage of adults who delayed medical care in the last 4 weeks or who needed medical care at any time in the last 4 weeks for something other than coronavirus but did not get it because of the pandemic. The experimental estimates on this page are derived from RANDS during COVID-19 and show the percentage of U.S. adults who were unable to receive medical care (including urgent care, surgery, screening tests, ongoing treatment, regular checkups, prescriptions, dental care, vision care, and hearing care) in the last 2 months. Technical Notes: https://www.cdc.gov/nchs/covid19/rands/reduced-access-to-care.htm#limitations",
-            "title": "Reduced Access to Care During COVID-19",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43290,46 +43273,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/th9n-ghnr",
+            "issued": "2020-09-14",
+            "keyword": [
+                "covid-19",
+                "rands"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/rands/reduced-access-to-care.htm",
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
+            "title": "Reduced Access to Care During COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ar7k-98x2",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-16",
-            "keyword": [
-                "2022",
-                "benefits and cost sharing",
-                "exchange puf",
-                "marketplace puf"
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
-            "identifier": "08f39b98-83cf-47d6-be34-12c0f77b1706",
             "description": "The Benefits and Cost Sharing PUF (BenCS-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BenCS-PUF contains plan variant-level data on essential health benefits, coverage limits, and cost sharing for each QHP and SADP.",
-            "title": "Benefits and Cost Sharing PUF - PY2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43337,17 +43319,48 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "08f39b98-83cf-47d6-be34-12c0f77b1706",
+            "issued": "2023-08-09",
+            "keyword": [
+                "2022",
+                "benefits and cost sharing",
+                "exchange puf",
+                "marketplace puf"
+            ],
+            "landingPage": "https://healthdata.gov/d/ar7k-98x2",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Benefits and Cost Sharing PUF - PY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-ii-nys-1977",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>Youth data for the second wave of the National Youth Survey<br />\nare contained in this data collection. The first wave was conducted in<br />\n1976. Youths were interviewed in early 1978 about events<br />\nand behavior that had occurred in 1977. Data were collected on<br />\ndemographic and socioeconomic status of respondents, aspirations,<br />\nsocial isolation, normlessness, labeling, attitudes toward deviance,<br />\nexposure to delinquent peers, commitment to delinquent peers, sex<br />\nroles, interpersonal violence, exposure to substance abuse,<br />\nself-reported delinquency, drug and alcohol use, and victimization.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Youth Survey US:  Wave II (NYS-1977) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-ii-nys-1977-nid13617",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-ii-nys-1977-nid13617"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-ii-nys-1977-nid13617",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "aspirations",
                 "behavior problems",
@@ -43379,64 +43392,29 @@
                 "young adults",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-ii-nys-1977",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-ii-nys-1977-nid13617",
-            "description": "<p>Youth data for the second wave of the National Youth Survey<br />\nare contained in this data collection. The first wave was conducted in<br />\n1976. Youths were interviewed in early 1978 about events<br />\nand behavior that had occurred in 1977. Data were collected on<br />\ndemographic and socioeconomic status of respondents, aspirations,<br />\nsocial isolation, normlessness, labeling, attitudes toward deviance,<br />\nexposure to delinquent peers, commitment to delinquent peers, sex<br />\nroles, interpersonal violence, exposure to substance abuse,<br />\nself-reported delinquency, drug and alcohol use, and victimization.This study has 1 Data Set.</p>",
-            "title": "National Youth Survey US:  Wave II (NYS-1977)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-ii-nys-1977-nid13617",
-                    "description": "National Youth Survey US:  Wave II (NYS-1977) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-ii-nys-1977-nid13617"
-                }
-            ]
+            "title": "National Youth Survey US:  Wave II (NYS-1977)"
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
-            "keyword": [
-                "...",
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
-            "identifier": "https://data.cdc.gov/api/views/waxm-p5qv",
             "description": "2002-2010. BRFSS SMART MMSA Prevalence land line only data. The Selected Metropolitan Area Risk Trends (SMART) project uses the Behavioral Risk Factor Surveillance System (BRFSS) to analyze the data of selected metropolitan statistical areas (MMSAs) with 500 or more respondents. BRFSS data can be used to identify emerging health problems, establish and track health objectives, and develop and evaluate public health policies and programs. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct/data",
-            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) MMSA Prevalence Data (2010 and Prior)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43459,78 +43437,82 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/waxm-p5qv",
+            "issued": "2023-07-18",
+            "keyword": [
+                "...",
+                "behavioral",
+                "brfss",
+                "mmsa",
+                "risk",
+                "smart",
+                "survey"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/",
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
                 "Behavioral Risk Factors"
-            ]
+            ],
+            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) MMSA Prevalence Data (2010 and Prior)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/at9j-skxj",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2014-01-08",
-            "keyword": [
-                "approved drug products with therapuetic equivalence evaluations",
-                "orange book"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Reinwald",
                 "hasEmail": "mailto:Robert.Reinwald@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "5E4326F3-B3EC-40C7-B5B9-1115F3394E94",
             "description": "The Approved Drug Products with Therapeutic Equivalence (Orange Book or OB) is a list of drugs approved under Section 505 of the Federal Food, Drug and Cosmetic Act and provides consumers timely updates on these products. In addition to these products (fo",
-            "title": "Orange Book",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "description": "The Approved Drug Products with Therapeutic Equivalence (Orange Book or OB) is a list of drugs approved under Section 505 of the Federal Food, Drug and Cosmetic Act and provides consumers timely updates on these products. In addition to these products (fo",
                     "downloadURL": "http://www.accessdata.fda.gov/scripts/cder/ob/",
-                    "mediaType": "text/html",
-                    "description": "The Approved Drug Products with Therapeutic Equivalence (Orange Book or OB) is a list of drugs approved under Section 505 of the Federal Food, Drug and Cosmetic Act and provides consumers timely updates on these products. In addition to these products (fo"
+                    "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "5E4326F3-B3EC-40C7-B5B9-1115F3394E94",
+            "issued": "2021-02-25",
+            "keyword": [
+                "approved drug products with therapuetic equivalence evaluations",
+                "orange book"
+            ],
+            "landingPage": "https://healthdata.gov/d/at9j-skxj",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2014-01-08",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Orange Book"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/atef-9yh4",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-10-21",
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
-            "identifier": "61729e5a-7aa8-448c-8903-ba3e0cd0ea3c",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43538,39 +43520,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "61729e5a-7aa8-448c-8903-ba3e0cd0ea3c",
+            "issued": "2024-10-21",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/atef-9yh4",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "State Drug Utilization Data 2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/sgg4-hiwe",
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
-            "identifier": "https://data.cdc.gov/api/views/sgg4-hiwe",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "NAAG Tobacco Settlement Payments Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43578,41 +43561,39 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/sgg4-hiwe",
+            "issued": "2015-01-23",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/sgg4-hiwe",
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
+            "title": "NAAG Tobacco Settlement Payments Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfNHRIC/nhric.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
-            "references": [
-                "http://www.fda.gov/medicaldevices/deviceregulationandguidance/databases/ucm161456.htm"
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
-            "identifier": "72b6e176-fd0a-48eb-b373-38812dd98baa",
             "description": "The National Health Related Items Code (NHRIC) is a system for identification and numbering of marketed device packages that is compatible with other numbering systems such as the National Drug Code (NDC) or Universal Product Code (UPC). Those manufacturers who desire to use the NHRIC number for unique product identification may apply to FDA for a labeler code. This database contains NHRIC data retrieved from records that date back 20 years.",
-            "title": "NHRIC (National Health Related Items Code)",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43620,39 +43601,38 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "72b6e176-fd0a-48eb-b373-38812dd98baa",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfNHRIC/nhric.cfm",
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
+                "http://www.fda.gov/medicaldevices/deviceregulationandguidance/databases/ucm161456.htm"
+            ],
+            "title": "NHRIC (National Health Related Items Code)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rsk5-566a",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
-            "keyword": [
-                "cardiovascular",
-                "cardiovascular disease",
-                "counties",
-                "county",
-                "heart"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Adam Vaughan",
                 "hasEmail": "mailto:avaughan@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rsk5-566a",
             "description": "This dataset documents cardiovascular disease (CVD) death rates, relative and absolute excess death rates, and trends. Specifically, this report presents county (or county equivalent) estimates of CVD death rates in 2000-2020, trends during 2010-2019, and relative and absolute excess death rates in 2020 by age group (ages 35\u201364 years, ages 65 years and older). All estimates were generated using a Bayesian spatiotemporal model and a smoothed over space, time, and 10-year age groups. Rates are age-standardized in 10-year age groups using the 2010 US population. Data source: National Vital Statistics System.",
-            "title": "Cardiovascular Disease Death Rates, Trends, and Excess Death Rates Among US Adults (35+) by County and Age Group \u2013 2010-2020",
-            "programCode": [
-                "009:029"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43675,52 +43655,43 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rsk5-566a",
+            "issued": "2024-06-17",
+            "keyword": [
+                "cardiovascular",
+                "cardiovascular disease",
+                "counties",
+                "county",
+                "heart"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rsk5-566a",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-01",
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
+            "title": "Cardiovascular Disease Death Rates, Trends, and Excess Death Rates Among US Adults (35+) by County and Age Group \u2013 2010-2020"
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
-                "disability",
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
-            "identifier": "https://data.cdc.gov/api/views/kee5-23sr",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2020 population counts, and American Community Survey (ACS) 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. These data can be joined with the Census 2021 ZCTA boundary file in a GIS system to produce maps for 40 measures at the ZCTA level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2024 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43743,21 +43714,63 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-ZCTA-Data-GIS-Friendly-Format-2020-release/kee5-23sr",
+            "identifier": "https://data.cdc.gov/api/views/kee5-23sr",
+            "issued": "2024-08-23",
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
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2024 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2012-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2012 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2012) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2012-nid13601",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2012-nid13601"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2012-nid13601",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -43798,59 +43811,30 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2012-0",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2012-nid13601",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2012 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2012)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2012-nid13601",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2012) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2012-nid13601"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2012)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/aume-h4i3",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-07-28",
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
-            "identifier": "5670e72c-e44e-4282-ab67-4ebebaba3cbd",
             "description": "Metrics from individual Marketplaces during the current reporting period. The report includes data for the states using State-based Marketplaces (SBMs) that use their own eligibility and enrollment platforms<br />\r\n<b>Source:</b> State-based Marketplace (SBM) operational data submitted to CMS. Each monthly reporting period occurs during the first through last day of the reported month. SBMs report relevant Marketplace activity from April 2023 (when unwinding-related renewals were initiated in most SBMs) through the end of a state\u2019s Medicaid unwinding renewal period and processing timeline, which will vary by SBM.  Some SBMs did not receive unwinding-related applications during reporting period months in April or May 2023 due to renewal processing timelines. SBMs that are no longer reporting Marketplace activity due to the completion of a state\u2019s Medicaid unwinding renewal period are marked as NA. Some SBMs may revise data from a prior month and thus this data may not align with that previously reported. For April, Idaho\u2019s reporting period was from February 1, 2023 to April 30, 2023.<br />\t\t\r\n<b>Notes:</b>\r\n<ol>\r\n<li>This table represents consumers whose Medicaid/CHIP coverage was denied or terminated following renewal and 1) whose applications were processed by an SBM through an integrated Medicaid, CHIP, and Marketplace eligibility system or 2) whose applications/information was sent by a state Medicaid or CHIP agency to an SBM through an account transfer process. Consumers who submitted applications to an SBM that can be matched to a Medicaid/CHIP record are also included. See the \"Data Sources and Metrics Definition Overview\" at http://www.medicaid.gov for a full description of the differences between the SBM operating systems and resulting data metrics, measure definitions, and general data limitations. As of the September 2023 report, this table was updated to differentiate between SBMs with an integrated Medicaid, CHIP, and Marketplace eligibility system and those with an account transfer process to better represent the percentage of QHP selections in relation to applicable consumers received and processed by the relevant SBM. State-specific variations are:      \r\n- Maine\u2019s data and Nevada\u2019s April and May 2023 data report all applications with Medicaid/CHIP denials or terminations, not only those part of the annual renewal process. \r\n- Connecticut, Massachusetts, and Washington also report applications with consumers determined ineligible for Medicaid/CHIP due to procedural reasons.\r\n- Minnesota and New York report on eligibility and enrollment for their Basic Health Programs (BHP). Effective April 1, 2024, New York transitioned its BHP to a program operated under a section 1332 waiver, which expands eligibility to individuals with incomes up to 250% of FPL. As of the March 2024 data, New York reports on consumers with expanded eligibility and enrollment under the section 1332 waiver program in the BHP data.\r\n- Idaho\u2019s April data on consumers eligible for a QHP with financial assistance do not depict a direct correlation to consumers with a QHP selection.\r\n- Virginia transitioned from using the HealthCare.gov platform in Plan Year 2023 to an SBM using its own eligibility and enrollment platform in Plan Year 2024. Virginia's data are reported in the HealthCare.gov and HeathCare.gov Transitions Marketplace Medicaid Unwinding Reports through the end of 2024 and is available in SBM reports as of the April 2024 report. Virginia's SBM data report all applications with Medicaid/CHIP denials or terminations, not only those part of the annual renewal process, and as a result are not directly comparable to their data in the HealthCare.gov data reports.\r\n- Only SBMs with an automatic plan assignment process have and report automatic QHP selections. These SBMs make automatic plan assignments into a QHP for a subset of individuals and provide a notification of options regarding active selection of an alternative plan and/or, if appli",
-            "title": "State-based Marketplace (SBM) Medicaid Unwinding Report",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43863,44 +43847,41 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "5670e72c-e44e-4282-ab67-4ebebaba3cbd",
+            "issued": "2023-07-28",
+            "keyword": [
+                "marketplace",
+                "transitions in coverage"
+            ],
+            "landingPage": "https://healthdata.gov/d/aume-h4i3",
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
+            "title": "State-based Marketplace (SBM) Medicaid Unwinding Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-vaccine-adverse-event-reporting-system",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-08-03",
-            "temporal": "1990-01-01T00:00:00-05:00/2012-06-13T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "adverse event",
-                "safety",
-                "side effect",
-                "vaccine",
-                "vaers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "e5532932-ebba-4912-8e59-1e40864911a1",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/vaers.html",
             "description": "<p>The Vaccine Adverse Event Reporting System (VAERS) online database on CDC WONDER provides counts and percentages of adverse event case reports after vaccination, received since January 1990 through last month. Data are available by symptom, vaccine product, manufacturer, onset interval, outcome category, year and month vaccinated, year and month reported, age, sex and state / territory. The Vaccine Adverse Event Reporting System is a cooperative program for vaccine safety of the Centers for Disease Control and Prevention (CDC) and the Food and Drug Administration (FDA). VAERS is a post-marketing safety surveillance program, collecting information about adverse events (possible side effects) that occur after the administration of US licensed vaccines. Data are from the US Department of Health and Human Services (DHHS), Public Health Service (PHS), Food and Drug Administration (FDA)/ Centers for Disease Control (CDC), Vaccine Adverse Event Reporting System (VAERS).</p>",
-            "title": "CDC Wonder Vaccine Adverse Event Reporting System",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43909,21 +43890,54 @@
                     "title": "Text "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/vaers.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "e5532932-ebba-4912-8e59-1e40864911a1",
+            "issued": "2012-08-03",
+            "keyword": [
+                "adverse event",
+                "safety",
+                "side effect",
+                "vaccine",
+                "vaers"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-vaccine-adverse-event-reporting-system",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "1990-01-01T00:00:00-05:00/2012-06-13T00:00:00-04:00",
+            "title": "CDC Wonder Vaccine Adverse Event Reporting System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nnhs/nnas.htm",
+            "accrualPeriodicity": "None",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/data/nnhsd/2004NNHS_DesignCollectionEstimates_072706tags.pdf",
+            "describedByType": "application/pdf",
+            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. The 2004 NNHS included a supplemental survey of nursing assistants employed by nursing homes, the National Nursing Assistant Survey (NNAS), which was sponsored by the Office of the Assistant Secretary for Planning and Evaluation (APSE). Nursing assistants were considered eligible to participate in the survey if they 1) provided assistance with activities of daily living (ADLs); 2) were paid to provide those services; 3) were certified (or in the process of certification) to provide Medicare/Medicaid reimbursable services; 4) worked at least 16 hours per week; and 5) were employees of the nursing home and not contract employees. A sample of up to eight nursing assistants was selected from about half of the nursing home sample at the time of the facility interview. The NNAS was administered after the nursing home visit, using a computer-assisted telephone interview (CATI) system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "2004 National Nursing Assistant Survey - Restricted Dataset"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/sns5-8bg3",
+            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NNAS/2004/",
             "issued": "2024-01-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2004-08-01/2004-12-31",
-            "modified": "2024-03-25",
             "keyword": [
                 "job satisfaction",
                 "nursing assistants",
@@ -43935,114 +43949,87 @@
                 "sdoh-work-place",
                 "turnover"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nnhs/nnas.htm",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-03-25",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/sns5-8bg3",
-            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. The 2004 NNHS included a supplemental survey of nursing assistants employed by nursing homes, the National Nursing Assistant Survey (NNAS), which was sponsored by the Office of the Assistant Secretary for Planning and Evaluation (APSE). Nursing assistants were considered eligible to participate in the survey if they 1) provided assistance with activities of daily living (ADLs); 2) were paid to provide those services; 3) were certified (or in the process of certification) to provide Medicare/Medicaid reimbursable services; 4) worked at least 16 hours per week; and 5) were employees of the nursing home and not contract employees. A sample of up to eight nursing assistants was selected from about half of the nursing home sample at the time of the facility interview. The NNAS was administered after the nursing home visit, using a computer-assisted telephone interview (CATI) system.",
-            "title": "2004 National Nursing Assistant Survey - Restricted Dataset",
-            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NNAS/2004/",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "mediaType": "text/html",
-                    "title": "2004 National Nursing Assistant Survey - Restricted Dataset"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/nnhsd/2004NNHS_DesignCollectionEstimates_072706tags.pdf",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "None",
+            "temporal": "2004-08-01/2004-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2004 National Nursing Assistant Survey - Restricted Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/auzm-qk64",
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
-            "identifier": "ec0abffe-206c-506c-8d53-5df5524758d5",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_measure_compare_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare_download.csv",
-                    "description": "{\"dataset\": \"measure_compare_download\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_compare_download\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare_download.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_compare_download csv file"
                 }
             ],
+            "identifier": "ec0abffe-206c-506c-8d53-5df5524758d5",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/auzm-qk64",
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
+            "title": "featAuto_measure_compare_download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/uk9u-uv8c",
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
-            "identifier": "https://data.cdc.gov/api/views/uk9u-uv8c",
             "description": "Exposure to 4,4\u2019-methylene diphenyl diisocyanate (MDI), the most widely used monomeric diisocyanate, in the occupational setting may lead to the development of occupational asthma (OA). Currently, the underlying molecular mechanism(s) by which MDI induces OA remain an active area of research. Alveolar macrophage dysfunctions play important roles in asthma pathogenesis. Upon exposure to outside stimuli, macrophages are polarized into either classically activated (M1) or alternatively activated (M2) phenotypes. Macrophage polarization is associated with asthma development where M2 macrophage populations are usually pronounced in lungs of asthmatic patients. Recent in vivo studies demonstrated that M2 macrophage associated markers and chemokines were induced by MDI exposure, indicating that MDI may induce M2 macrophage polarization; however, the underling molecular mechanism(s) by which MDI causes induction of M2 associated markers and chemokines is unclear. M2 macrophage polarization can be regulated by activation of several M2 associated transcription factors; however, whether MDI exposure regulates these transcription factors is unknown. We hypothesize that MDI exposure induces M2 macrophage associate markers and chemokines through upregulation of M2 macrophage-associated transcription factors in macrophages. The first aim of this study is to verify whether MDI-exposure can induce M2 macrophage-associated markers and chemokine expression that were observed in previous studies and to identify candidate M2 macrophage-associated transcription factors in response to MDI exposure that may account for the M2 macrophage polarization. After identification of the candidate transcription factor(s) that can be regulated by MDI-exposure, we investigate the roles of the candidate transcription factor in regulation of these candidate M2 macrophage associate markers and chemokines in relation to the exposure to MDI.",
-            "title": "4,4\u2019-Methylene Diphenyl Diisocyanate Exposure Induces Expression of Alternatively Activated Macrophage-Associated Markers and Chemokines Partially Through Kr\u00fcppel-Like Factor 4 Mediated Signaling in Macrophages",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44050,48 +44037,37 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/uk9u-uv8c",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/uk9u-uv8c",
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
+            "title": "4,4\u2019-Methylene Diphenyl Diisocyanate Exposure Induces Expression of Alternatively Activated Macrophage-Associated Markers and Chemokines Partially Through Kr\u00fcppel-Like Factor 4 Mediated Signaling in Macrophages"
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
-            "issued": "2024-09-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-2022",
-            "modified": "2024-10-24",
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
-            "identifier": "https://data.cdc.gov/api/views/k6sd-3kb8",
+            "describedBy": "ftp.cdc.gov - /pub/Health_Statistics/NCHS/Dataset_Documentation/NHAMCS/",
             "description": "These data include counts and rates of emergency department visits from 2016-2022 for selected primary diagnoses and reasons for visit, stratified by selected patient and hospital characteristics.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Estimate of Emergency Department Visits in the United States, 2016-2022",
-            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44114,23 +44090,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "ftp.cdc.gov - /pub/Health_Statistics/NCHS/Dataset_Documentation/NHAMCS/",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annually. Dataset will no longer be updated after the 2022 release in summer 2024.",
-            "theme": [
-                "National Center for Health Statistics"
-            ]
+            "identifier": "https://data.cdc.gov/api/views/k6sd-3kb8",
+            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "issued": "2024-09-03",
+            "keyword": [
+                "diagnosis",
+                "emergency department",
+                "patient characteristics",
+                "reason for visit",
+                "visit characteristics"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-24",
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
+            "temporal": "2016-2022",
+            "theme": [
+                "National Center for Health Statistics"
+            ],
+            "title": "DQS Estimate of Emergency Department Visits in the United States, 2016-2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/us-department-health-and-human-services-office-inspector-general-advisory-opinion-list-0",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OIG Public Affairs",
+                "hasEmail": "mailto:Public.Affairs@OIG.HHS.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This OIG website contains a list of recently issued advisory opinions and a link to archives of previously issued advisory opinions.  In accordance with section 1128D (b) (5) (A) (v) of the Social Security Act and 42 CFR 1008.47 of the Office of Inspector General's (OIG) regulations, advisory opinions issued by the OIG are made available to the general public through this OIG website. One purpose of the advisory opinion process is to provide meaningful advice on the application of the anti-kickback statute and other OIG sanction statutes in specific factual situations. Please note, however, that advisory opinions are binding and may legally be relied upon only by the requestor. Because each opinion will apply legal standards to a set of facts involving certain known persons who provide specific statements about key factual issues, no third parties are bound nor may they legally rely on these advisory opinions.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://oig.hhs.gov/fraud/advisoryopinions.asp",
+                    "mediaType": "text/html",
+                    "title": "Query Tool"
+                }
+            ],
+            "identifier": "6bbd5726-ba60-451a-8cb8-df127b585b26",
             "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "administrative",
                 "advisory",
@@ -44144,66 +44157,34 @@
                 "safe harbor",
                 "safe harbors"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OIG Public Affairs",
-                "hasEmail": "mailto:Public.Affairs@OIG.HHS.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/us-department-health-and-human-services-office-inspector-general-advisory-opinion-list-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:109"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Inspector General, Department of Health & Human Services"
             },
-            "identifier": "6bbd5726-ba60-451a-8cb8-df127b585b26",
-            "description": "<p>This OIG website contains a list of recently issued advisory opinions and a link to archives of previously issued advisory opinions.  In accordance with section 1128D (b) (5) (A) (v) of the Social Security Act and 42 CFR 1008.47 of the Office of Inspector General's (OIG) regulations, advisory opinions issued by the OIG are made available to the general public through this OIG website. One purpose of the advisory opinion process is to provide meaningful advice on the application of the anti-kickback statute and other OIG sanction statutes in specific factual situations. Please note, however, that advisory opinions are binding and may legally be relied upon only by the requestor. Because each opinion will apply legal standards to a set of facts involving certain known persons who provide specific statements about key factual issues, no third parties are bound nor may they legally rely on these advisory opinions.</p>",
-            "title": "U.S. Department of Health and Human Services Office of Inspector General Advisory Opinion List",
-            "programCode": [
-                "009:109"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://oig.hhs.gov/fraud/advisoryopinions.asp",
-                    "mediaType": "text/html",
-                    "title": "Query Tool"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Community"
-            ]
+            ],
+            "title": "U.S. Department of Health and Human Services Office of Inspector General Advisory Opinion List"
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
-            "keyword": [
-                "ghpss",
-                "gtss",
-                "osh",
-                "students",
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
-            "identifier": "https://data.cdc.gov/api/views/x6ag-8y7r",
+            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Hea/x6ag-8y7r",
             "description": "2005-2011. The World Health Organization, CDC, and the Canadian Public Health Association, developed the GHPSS to collect data on tobacco use and cessation counseling among health professional students in all WHO member states. GHPSS is a standardized school-based survey of third-year students pursuing advanced degrees in dentistry, medicine, nursing, or pharmacy. It is conducted in schools during regular class sessions. GHPSS follows an anonymous, self-administered format for data collection. GHPSS uses a core questionnaire on demographics, prevalence of cigarette smoking and other tobacco use, knowledge and attitudes about tobacco use, exposure to secondhand smoke, desire for smoking cessation, and training received regarding patient counseling on smoking cessation techniques. Questionnaires are translated into local languages as needed. GHPSS has a standardized methodology for selecting participating schools and classes and uniform data processing procedures.",
-            "title": "Global Tobacco Surveillance System (GTSS) - Global Health Professions Student Survey (GHPSS)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44226,100 +44207,88 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Hea/x6ag-8y7r",
+            "identifier": "https://data.cdc.gov/api/views/x6ag-8y7r",
+            "issued": "2025-01-31",
+            "keyword": [
+                "ghpss",
+                "gtss",
+                "osh",
+                "students",
+                "tobacco"
+            ],
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
             "theme": [
                 "Global Survey Data"
-            ]
+            ],
+            "title": "Global Tobacco Surveillance System (GTSS) - Global Health Professions Student Survey (GHPSS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/awf7-h3ag",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-11",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-10",
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
-            "identifier": "df89cf2b-2298-5529-8d1b-eb7de7851b6b",
             "description": "I am an update",
-            "title": "Scorecard example_small_source_data_file",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/example_small_source_data_file.csv",
-                    "description": "Scorecard example_small_source_data_file",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard example_small_source_data_file",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/example_small_source_data_file.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard example_small_source_data_file"
                 }
             ],
+            "identifier": "df89cf2b-2298-5529-8d1b-eb7de7851b6b",
+            "issued": "2023-04-11",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/awf7-h3ag",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2023-04-10",
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
+            "title": "Scorecard example_small_source_data_file"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-10-15",
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
-            "identifier": "https://data.cdc.gov/api/views/kucs-wizg",
             "description": "2015, 2014. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census tract-level data in GIS-friendly format can be joined with census tract spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-Boundaries/x7zy-2xmx) in a geographic information system (GIS) to produce maps of 27 measures at the census tract level. Because some questions are only asked every other year in the BRFSS, there are 7 measures in this 2017 release from the 2014 BRFSS that were the same as the 2016 release.",
-            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2017 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44342,51 +44311,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kucs-wizg",
+            "issued": "2018-10-15",
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
+            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2017 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-07-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
-            "keyword": [
-                "age",
-                "age group",
-                "coronavirus",
-                "covid-19",
-                "death rate",
-                "deaths",
-                "hispanic origin",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/jwta-jxbg",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis visualization provides data that can be used to illustrate potential differences in the burden of deaths due to COVID-19 by race and ethnicity.",
-            "title": "Distribution of COVID-19 Deaths and Populations, by Jurisdiction, Age, and Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44409,53 +44381,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/jwta-jxbg",
+            "issued": "2020-07-24",
+            "keyword": [
+                "age",
+                "age group",
+                "coronavirus",
+                "covid-19",
+                "death rate",
+                "deaths",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
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
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Distribution of COVID-19 Deaths and Populations, by Jurisdiction, Age, and Race and Hispanic Origin"
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
-            "modified": "2024-12-23",
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
-            "identifier": "https://data.cdc.gov/api/views/i46a-9kgh",
             "description": "This dataset contains model-based county-level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. Project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2022 county population estimates, and American Community Survey (ACS) 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. These data can be joined with the census 2022 county boundary file in a GIS system to produce maps for 40 measures at the county level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: County Data (GIS Friendly Format), 2024 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44478,35 +44449,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i46a-9kgh",
+            "issued": "2024-08-23",
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
+            "title": "PLACES: County Data (GIS Friendly Format), 2024 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vyry-2yfg",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-05-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Fred Smith",
                 "hasEmail": "mailto:imtech@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vyry-2yfg",
             "description": "CDC is planning a major relaunch of CDC.gov on May 15th, followed by subsequent monthly batches of sites restructuring their CDC.gov content into the fall of 2024.\n \nBecause this restructuring includes merged or changed content, CDC will be updating all URLs to a new standard naming structure. About 70% of these updates will occur during the May 15th launch, but another 30% of our content and URLs will be restructured on a rolling schedule. \n \nThis data set contains the mapping information from old URLs to new URLs. Before May 15th, 2024, this dataset will only include one row of data to preview the fields in the dataset.\u202fAfter May 15th it will contain all content URLs that changed as part of the relaunch of CDC.gov. After launch, we will continue to add additional mappings typically around the 15th of each month for any for sites updated in each monthly batch.",
-            "title": "CDC.gov CleanSlate and Relaunch URL Mappings",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44529,45 +44517,32 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vyry-2yfg",
+            "issued": "2024-05-16",
+            "landingPage": "https://data.cdc.gov/d/vyry-2yfg",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Monthly"
+            "modified": "2024-12-19",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "CDC.gov CleanSlate and Relaunch URL Mappings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-28",
-            "references": [
-                "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm"
-            ],
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
-            "identifier": "https://data.cdc.gov/api/views/jx6g-fdh6",
             "description": "This dataset describes drug poisoning deaths at the U.S. and state level by selected demographic characteristics, and includes age-adjusted death rates for drug poisoning from 1999 to 2015.\r\n\r\nDeaths are classified using the International Classification of Diseases, Tenth Revision (ICD\u201310). Drug-poisoning deaths are defined as having ICD\u201310 underlying cause-of-death codes X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), or Y10\u2013Y14 (undetermined intent).\r\n\r\nEstimates are based on the National Vital Statistics System multiple cause-of-death mortality files (1). Age-adjusted death rates (deaths per 100,000 U.S. standard population for 2000) are calculated using the direct method. Populations used for computing death rates for 2011\u20132015 are postcensal estimates based on the 2010 U.S. census. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\r\n\r\nEstimate does not meet standards of reliability or precision. Death rates are flagged as \u201cUnreliable\u201d in the chart when the rate is calculated with a numerator of 20 or less.\r\n\r\nDeath rates for some states and years may be low due to a high number of unresolved pending cases or misclassification of ICD\u201310 codes for unintentional poisoning as R99, \u201cOther ill-defined and unspecified causes of mortality\u201d (2). For example, this issue is known to affect New Jersey in 2009 and West Virginia in 2005 and 2009 but also may affect other years and other states. Estimates should be interpreted with caution.\r\n\r\nSmoothed county age-adjusted death rates (deaths per 100,000 population) were obtained according to methods described elsewhere (3\u20135). Briefly, two-stage hierarchical models were used to generate empirical Bayes estimates of county age-adjusted death rates due to drug poisoning for each year during 1999\u20132015. These annual county-level estimates \u201cborrow strength\u201d across counties to generate stable estimates of death rates where data are sparse due to small population size (3,5). Estimates are unavailable for Broomfield County, Colo., and Denali County, Alaska, before 2003 (6,7). Additionally, Bedford City, Virginia was added to Bedford County in 2015 and no longer appears in the mortality file in 2015. County boundaries are consistent with the vintage 2005-2007 bridged-race population file geographies (6).",
-            "title": "NCHS - Drug Poisoning Mortality by State: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44590,39 +44565,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/jx6g-fdh6",
+            "issued": "2016-01-07",
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
+            "modified": "2022-03-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm"
+            ],
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
-            "landingPage": "https://healthdata.gov/d/b3gx-7tcv",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-26",
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
-            "identifier": "a86dfb1d-0cf8-45e6-a875-9aed4d430ae7",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-18-to-2023-12-24",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44631,39 +44616,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-18-to-2023-12-24"
                 }
             ],
+            "identifier": "a86dfb1d-0cf8-45e6-a875-9aed4d430ae7",
+            "issued": "2023-12-29",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/b3gx-7tcv",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-12-26",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-18-to-2023-12-24"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://chpl.healthit.gov/#/resources/download",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "keyword": [
-                "certified",
-                "ehr",
-                "electronic health records",
-                "health it"
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
-            "identifier": "udruc2qi-rbx5-4vvp-3rf5-hmf1b7wzvqym",
+            "describedBy": "https://chpl.healthit.gov/#/resources/download",
             "description": "The Certified Health IT Product List (CHPL) is a comprehensive and authoritative listing of all certified Health Information Technology which has been successfully tested and certified by the ONC Health IT Certification program. All products listed on the CHPL have been tested by an ONC-Accredited Testing Laboratory (ONC-ATL) and certified by an ONC-Authorized Certification Body (ONC-ACB) to meet criteria adopted by the Secretary of the Department of Health and Human Services (HHS).",
-            "title": "Certified Health IT Product List (CHPL)",
-            "programCode": [
-                "009:110"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44672,37 +44654,37 @@
                     "title": "chpl-all.xml"
                 }
             ],
-            "describedBy": "https://chpl.healthit.gov/#/resources/download"
+            "identifier": "udruc2qi-rbx5-4vvp-3rf5-hmf1b7wzvqym",
+            "issued": "2023-10-03",
+            "keyword": [
+                "certified",
+                "ehr",
+                "electronic health records",
+                "health it"
+            ],
+            "landingPage": "https://chpl.healthit.gov/#/resources/download",
+            "modified": "2023-10-03",
+            "programCode": [
+                "009:110"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "title": "Certified Health IT Product List (CHPL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://meshb.nlm.nih.gov/MeSHonDemand",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "literature",
-                "terminologies",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/bjsc-pi25",
             "description": "MeSH on Demand identifies MeSH Terms in your text using the NLM Medical Text Indexer (MTI) program. After processing, MeSH on Demand returns a list of MeSH Terms relevant to your text as well as a list of related articles from PubMed.",
-            "title": "MeSH on Demand",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44711,23 +44693,51 @@
                     "title": "Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/bjsc-pi25",
+            "issued": "2021-06-30",
+            "keyword": [
+                "literature",
+                "terminologies",
+                "tools & utilities"
+            ],
+            "landingPage": "https://meshb.nlm.nih.gov/MeSHonDemand",
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
+            "title": "MeSH on Demand"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/state-health-it-privacy-and-consent-laws-and-policies",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-01",
-            "references": [
-                "https://www.healthit.gov/data/apps/state-health-it-privacy-and-consent-laws-and-policies"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/state-health-it-privacy-and-consent-laws-and-policies",
+            "description": "This data was collected by the Office of the National Coordinator for Health IT in coordination with Clinovations and the George Washington University Milken Institute of Public Health. ONC and its partners collected the data through research of state government and health information organization websites. The dataset provides policy and law details for four distinct policies or laws, and, where available, hyperlinks to official state records or websites. These four policies or laws are: 1) State Health Information Exchange (HIE) Consent Policies; 2) State-Sponsored HIE Consent Policies; 3) State Laws Requiring Authorization to Disclose Mental Health Information for Treatment, Payment, and Health Care Operations (TPO); and 4) State Laws that Apply a Minimum Necessary Standard to Treatment Disclosures of Mental Health Information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/state-health-it-privacy-consent-law-policies.csv",
+                    "mediaType": "text/csv",
+                    "title": "state-health-it-privacy-consent-law-policies.csv"
+                }
             ],
+            "identifier": "yw73pryi-h3or-9rhg-jpgp-dofus7swvmx1",
+            "issued": "2023-10-03",
             "keyword": [
                 "authorization",
                 "consent",
@@ -44754,67 +44764,32 @@
                 "tpo",
                 "treatment"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/state-health-it-privacy-and-consent-laws-and-policies",
+            "modified": "2017-07-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "yw73pryi-h3or-9rhg-jpgp-dofus7swvmx1",
-            "description": "This data was collected by the Office of the National Coordinator for Health IT in coordination with Clinovations and the George Washington University Milken Institute of Public Health. ONC and its partners collected the data through research of state government and health information organization websites. The dataset provides policy and law details for four distinct policies or laws, and, where available, hyperlinks to official state records or websites. These four policies or laws are: 1) State Health Information Exchange (HIE) Consent Policies; 2) State-Sponsored HIE Consent Policies; 3) State Laws Requiring Authorization to Disclose Mental Health Information for Treatment, Payment, and Health Care Operations (TPO); and 4) State Laws that Apply a Minimum Necessary Standard to Treatment Disclosures of Mental Health Information.",
-            "title": "State Health IT Privacy and Consent Laws and Policies",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/state-health-it-privacy-consent-law-policies.csv",
-                    "mediaType": "text/csv",
-                    "title": "state-health-it-privacy-consent-law-policies.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/apps/state-health-it-privacy-and-consent-laws-and-policies"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/state-health-it-privacy-and-consent-laws-and-policies"
+            "title": "State Health IT Privacy and Consent Laws and Policies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hm3s-vk7u",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-09",
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
                 "fn": "T.J. Pierce",
                 "hasEmail": "mailto:pwc2@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hm3s-vk7u",
             "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when individuals in states and territories were subject to executive orders, administrative orders, resolutions, and proclamations for COVID-19 that require or recommend people stay in their homes. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level.\n\nThese data are derived from the publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly require or recommend individuals stay at home found by the CDC, COVID-19 Community Intervention and At-Risk Task Force, Monitoring and Evaluation Team & CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 15, 2020 through May 31, 2021. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. These data do not include mandatory business closures, curfews, or limitations on public or private gatherings. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Stay-At-Home Orders: March 15, 2020 \u2013 May 31, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44837,40 +44812,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hm3s-vk7u",
+            "issued": "2021-12-10",
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
+            "landingPage": "https://data.cdc.gov/d/hm3s-vk7u",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-09-09",
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
+            "title": "U.S. State and Territorial Stay-At-Home Orders: March 15, 2020 \u2013 May 31, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/b58n-utnf",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-07-16",
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
-            "identifier": "a1f3598e-fc71-51aa-8560-78e7e1a61b09",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2018",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44878,39 +44861,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "a1f3598e-fc71-51aa-8560-78e7e1a61b09",
+            "issued": "2018-07-16",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/b58n-utnf",
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
+            "title": "State Drug Utilization Data 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/b77k-8tjv",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-23",
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
-            "identifier": "136e08d6-1a95-4c6d-9072-ff1e518e9736",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-16-2024-to-12-22-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44918,40 +44902,35 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "136e08d6-1a95-4c6d-9072-ff1e518e9736",
+            "issued": "2024-12-25",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/b77k-8tjv",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-23",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-16-2024-to-12-22-2024"
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
-            "modified": "2022-03-29",
-            "keyword": [
-                "county",
-                "deaths",
-                "drug poisoning",
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
-            "identifier": "https://data.cdc.gov/api/views/p56q-jrxg",
             "description": "This dataset contains model-based county estimates for drug-poisoning mortality. \r\n\r\nDeaths are classified using the International Classification of Diseases, Tenth Revision (ICD\u201310). Drug-poisoning deaths are defined as having ICD\u201310 underlying cause-of-death codes X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), or Y10\u2013Y14 (undetermined intent).\r\n\r\nEstimates are based on the National Vital Statistics System multiple cause-of-death mortality files (1). Age-adjusted death rates (deaths per 100,000 U.S. standard population for 2000) are calculated using the direct method. Populations used for computing death rates for 2011\u20132016 are postcensal estimates based on the 2010 U.S. census. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\r\n\r\nDeath rates for some states and years may be low due to a high number of unresolved pending cases or misclassification of ICD\u201310 codes for unintentional poisoning as R99, \u201cOther ill-defined and unspecified causes of mortality\u201d (2). For example, this issue is known to affect New Jersey in 2009 and West Virginia in 2005 and 2009 but also may affect other years and other states. Drug poisoning death rates may be underestimated in those instances.\r\n\r\nSmoothed county age-adjusted death rates (deaths per 100,000 population) were obtained according to methods described elsewhere (3\u20135). Briefly, two-stage hierarchical models were used to generate empirical Bayes estimates of county age-adjusted death rates due to drug poisoning for each year. These annual county-level estimates \u201cborrow strength\u201d across counties to generate stable estimates of death rates where data are sparse due to small population size (3,5). Estimates for 1999-2015 have been updated, and may differ slightly from previously published estimates. Differences are expected to be minimal, and may result from different county boundaries used in this release (see below) and from the inclusion of an additional year of data. Previously published estimates can be found here for comparison.(6) Estimates are unavailable for Broomfield County, Colorado, and Denali County, Alaska, before 2003 (7,8). Additionally, Clifton Forge County, Virginia only appears on the mortality files prior to 2003, while Bedford City, Virginia was added to Bedford County in 2015 and no longer appears in the mortality file in 2015. These counties were therefore merged with adjacent counties where necessary to create a consistent set of geographic units across the time period. County boundaries are largely consistent with the vintage 2005-2007 bridged-race population file geographies, with the modifications noted previously (7,8).\r\n\r\nREFERENCES\r\n1. National Center for Health Statistics. National Vital Statistics System: Mortality data. Available from: http://www.cdc.gov/nchs/deaths.htm.\r\n\r\n2. CDC. CDC Wonder: Underlying cause of death 1999\u20132016. Available from: http://wonder.cdc.gov/wonder/help/ucd.html.\r\n\r\n3. Rossen LM, Khan D, Warner M. Trends and geographic patterns in drug-poisoning death rates in the U.S., 1999\u20132009. Am J Prev Med 45(6):e19\u201325. 2013.\r\n\r\n4. Rossen LM, Khan D, Warner M. Hot spots in mortality from drug poisoning in the United States, 2007\u20132009. Health Place 26:14\u201320. 2014.\r\n\r\n5. Rossen LM, Khan D, Hamilton B, Warner M. Spatiotemporal variation in selected health outcomes from the National Vital Statistics System. Presented at: 2015 National Conference on Health Statistics, August 25, 2015, Bethesda, MD. Available from: http://www.cdc.gov/nchs/ppt/nchs2015/Rossen_Tuesday_WhiteOak_BB3.pdf.\r\n\r\n6. Rossen LM, Bastian B, Warner M, and Khan D. NCHS \u2013 Drug Poisoning Mortality by County: United States, 1999-2015. Available from: https://data.cdc.gov/NCHS/NCHS-Drug-Poisoning-Mortality-by-County-United-Sta/pbkm-d27e.\r\n\r\n7. National Center for Health Statistics. County geog",
-            "title": "NCHS - Drug Poisoning Mortality by County: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44974,69 +44953,77 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/p56q-jrxg",
+            "issued": "2017-12-06",
+            "keyword": [
+                "county",
+                "deaths",
+                "drug poisoning",
+                "mortality",
+                "nchs",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-29",
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
+            "title": "NCHS - Drug Poisoning Mortality by County: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/hhs-enterprise-data-inventory",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Data @ HHS",
+                "hasEmail": "mailto:HealthData@HHS.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Enterprise Data Inventory (EDI) is the comprehensive inventory listing of agency data resources including public, restricted public, and non-public datasets.</p>",
+            "identifier": "c5acee93-1748-4fcf-8fcb-5c35f0336526_5_0",
             "issued": "2015-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "catalog",
                 "edi",
                 "enterprise data inventory",
                 "other"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Health Data @ HHS",
-                "hasEmail": "mailto:HealthData@HHS.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/hhs-enterprise-data-inventory",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:023"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "c5acee93-1748-4fcf-8fcb-5c35f0336526_5_0",
-            "description": "<p>The Enterprise Data Inventory (EDI) is the comprehensive inventory listing of agency data resources including public, restricted public, and non-public datasets.</p>",
-            "title": "HHS Enterprise Data Inventory: 2016-11 HHS EDI JSON",
-            "programCode": [
-                "009:023"
-            ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "title": "HHS Enterprise Data Inventory: 2016-11 HHS EDI JSON"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/k2fe-zny8",
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
-            "identifier": "https://data.cdc.gov/api/views/k2fe-zny8",
             "description": "Nanomaterials represent a new class of materials with numerous industrial applications. Considering the projected increase in the production and use of nanomaterials, a corresponding increase in occupational exposure to nanomaterials and their resulting adverse health effects may be anticipated among workers. There is substantial evidence in the literature, based on cell culture and animal studies, supporting the potential toxicity and detrimental health effects associated with exposure to nanomaterials. Intervention and/or prevention of adverse health effects associated with occupational exposure to toxic nanomaterials is a concern for health providers and regulatory and non-regulatory government agencies as the use of nanomaterials expand. A key element in the intervention and/or prevention of the adverse health effects associated with occupational exposure to toxic nanomaterials is a clear understanding of the molecular mechanisms underlying the pulmonary toxicity induced by nanomaterials.\n\nDue to its physicochemical and mechanical properties, multi-walled carbon nanotubes (MWCNT) have found many industrial applications. There is potential for human exposure to MWCNT or products that contain MWCNT both during the production and use of the materials that contain MWCNT. The objectives of the current study were to investigate MWCNT-induced lung toxicity and the molecular mechanisms underlying that toxicity. A rat inhalation exposure model was employed to determine the lung toxicity induced by MWCNT. Global gene expression profiles in the lung and blood were conducted to determine the molecular mechanisms underlying MWCNT-induced lung toxicity.",
-            "title": "Pulmonary toxicity and gene expression changes in response to whole-body inhalation exposure to multi-walled carbon nanotubes in rats-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45044,38 +45031,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/k2fe-zny8",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/k2fe-zny8",
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
+            "title": "Pulmonary toxicity and gene expression changes in response to whole-body inhalation exposure to multi-walled carbon nanotubes in rats-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/b8df-88d9",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-09-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-18",
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
-            "identifier": "e2893fe7-8869-45c9-bb4c-9eb20dc2bd33",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-11-to-2023-09-17",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45084,19 +45069,47 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-11-to-2023-09-17"
                 }
             ],
+            "identifier": "e2893fe7-8869-45c9-bb4c-9eb20dc2bd33",
+            "issued": "2023-09-20",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/b8df-88d9",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-09-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-11-to-2023-09-17"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/medicare-appeals-council-decisions",
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
+            "identifier": "22ed0b95-e0da-4838-88bf-4e37c931b3f3",
             "issued": "2012-05-30",
-            "temporal": "2003-06-11T00:00:00-04:00/2003-06-11T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "administrative",
                 "adopt",
@@ -45176,74 +45189,37 @@
                 "supplier",
                 "surgery"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/medicare-appeals-council-decisions",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:078"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "22ed0b95-e0da-4838-88bf-4e37c931b3f3",
-            "description": "<p>Decisions of the Departmental Appeals Board's Medicare Appeals Council involving claims for entitlement to Medicare and individual claims for Medicare coverage and payment filed by beneficiaries or health care providers/suppliers.</p>",
-            "title": "Medicare Appeals Council Decisions",
-            "programCode": [
-                "009:078"
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
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-04-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2005/2018",
-            "modified": "2023-08-29",
-            "keyword": [
-                "accidental falls",
-                "age",
-                "disasters",
-                "emergency service",
-                "health us",
-                "hospital",
-                "hospitals",
-                "sex",
-                "wounds and injuries"
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
-            "identifier": "https://data.cdc.gov/api/views/w4cs-jspc",
             "description": "<strong>On December 20 2021, all estimates and standard errors for 2017\u20132018 were revised in this table to correct programming errors.</strong>\n\nData on initial injury-related visits to hospital emergency departments, by sex, age, and intent and mechanism of injury. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. Due to a change in national medical data coding standards in 2015, from the International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM) to the ICD-10-CM, the definition for injuries and injury subcategories changed for the 2017 reporting period and beyond. Results from 2017 and subsequent years should not be compared with previous reporting periods. Any observed changes in trends across this transition period should not be considered. Data for 2016 are not included. Additional information regarding injury definitions and categorization of injuries by mechanism and intent of injury is available at: https://www.cdc.gov/nchs/injury/injury_tools.htm. Note that the data file available here has more recent years of data than what is shown in the PDF or Excel version.\n\nSOURCE: NCHS, National Hospital Ambulatory Medical Care Survey. For more information on the National Hospital Ambulatory Medical Care Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus17_appendix.pdf.",
-            "title": "Initial injury-related visits to hospital emergency departments, by sex, age, and intent and mechanism of injury: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45266,23 +45242,68 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/w4cs-jspc",
+            "issued": "2022-04-28",
+            "keyword": [
+                "accidental falls",
+                "age",
+                "disasters",
+                "emergency service",
+                "health us",
+                "hospital",
+                "hospitals",
+                "sex",
+                "wounds and injuries"
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2005/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Initial injury-related visits to hospital emergency departments, by sex, age, and intent and mechanism of injury: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.hrsa.gov",
             "bureauCode": [
                 "009:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "data.hrsa.gov",
+                "hasEmail": "mailto:data@hrsa.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://data.hrsa.gov/data/about",
+            "description": "<p>DATA.HRSA.GOV is the go-to source for data, dashboards, maps, reports, locators, APIs and downloadable data files on HRSA's public health programs, including:</p>\n<ul>\n<li>HRSA-funded Health Center grants, grantees, sites, and related primary care programs</li>\n<li>Health Professional Shortage Areas (HPSA) and Medically Underserved Areas/Populations (MUA/P)</li>\n<li>Ryan White HIV/AIDS services, grantees, and providers</li>\n<li>Maternal and Child Health grants (Title V, Home Visiting, Healthy Start)</li>\n<li>National Health Service Corps (NHSC), Nurse Corps, and other workforce loan repayment/scholarship programs</li>\n<li>Grants for workforce training programs in medicine, nursing, dentistry, and public health</li>\n<li>Grants for rural health programs</li>\n<li>Organ donation</li>\n</ul>\n<p>DATA.HRSA.GOV allows you to search by topic area, by geography, and by tool.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "HRSA Health Centers care for you, even if you have no health insurance \u2013 you pay what you can afford based on your income. Health centers provide services that include checkups when you are well, treatment when you are sick, complete care when you are pregnant, and immunizations and checkups for your children. Some health centers also provide mental health, substance abuse, oral health, and/or vision services. Contact the health center organization directly to confirm the availability of specific services and to make an appointment. \n",
+                    "downloadURL": "https://findahealthcenter.hrsa.gov",
+                    "mediaType": "application/unknown",
+                    "title": "Find a Health Center"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://data.hrsa.gov/data/services/registration",
+                    "description": "data.hrsa.gov API, web services, and map services registration link \n",
+                    "format": "API",
+                    "title": "data.hrsa.gov API, web services, and map services"
+                }
+            ],
+            "identifier": "518e9015-b51d-40d1-9fe5-dd1befdb8d8c",
             "issued": "2012-08-03",
-            "temporal": "1999-01-01T00:00:00-05:00/1999-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "340b",
                 "340(b)",
@@ -45352,74 +45373,38 @@
                 "workforce",
                 "xml"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "data.hrsa.gov",
-                "hasEmail": "mailto:data@hrsa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Health Resources and Services Administration"
-            },
-            "identifier": "518e9015-b51d-40d1-9fe5-dd1befdb8d8c",
-            "description": "<p>DATA.HRSA.GOV is the go-to source for data, dashboards, maps, reports, locators, APIs and downloadable data files on HRSA's public health programs, including:</p>\n<ul>\n<li>HRSA-funded Health Center grants, grantees, sites, and related primary care programs</li>\n<li>Health Professional Shortage Areas (HPSA) and Medically Underserved Areas/Populations (MUA/P)</li>\n<li>Ryan White HIV/AIDS services, grantees, and providers</li>\n<li>Maternal and Child Health grants (Title V, Home Visiting, Healthy Start)</li>\n<li>National Health Service Corps (NHSC), Nurse Corps, and other workforce loan repayment/scholarship programs</li>\n<li>Grants for workforce training programs in medicine, nursing, dentistry, and public health</li>\n<li>Grants for rural health programs</li>\n<li>Organ donation</li>\n</ul>\n<p>DATA.HRSA.GOV allows you to search by topic area, by geography, and by tool.</p>",
-            "title": "data.hrsa.gov (HRSA Data Warehouse)",
+            "landingPage": "https://data.hrsa.gov",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:110"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/unknown",
-                    "downloadURL": "https://findahealthcenter.hrsa.gov",
-                    "description": "HRSA Health Centers care for you, even if you have no health insurance \u2013 you pay what you can afford based on your income. Health centers provide services that include checkups when you are well, treatment when you are sick, complete care when you are pregnant, and immunizations and checkups for your children. Some health centers also provide mental health, substance abuse, oral health, and/or vision services. Contact the health center organization directly to confirm the availability of specific services and to make an appointment. \n",
-                    "@type": "dcat:Distribution",
-                    "title": "Find a Health Center"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Health Resources and Services Administration"
             },
-                {
-                    "format": "API",
-                    "description": "data.hrsa.gov API, web services, and map services registration link \n",
-                    "accessURL": "https://data.hrsa.gov/data/services/registration",
-                    "@type": "dcat:Distribution",
-                    "title": "data.hrsa.gov API, web services, and map services"
-                }
-            ],
-            "describedBy": "https://data.hrsa.gov/data/about",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1999-01-01T00:00:00-05:00/1999-01-01T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health",
                 "National",
                 "State"
-            ]
+            ],
+            "title": "data.hrsa.gov (HRSA Data Warehouse)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ba35-nkej",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-14",
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
-            "identifier": "819b3417-0f93-488d-974a-4f80c87eb48f",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211004 to 20211010",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45427,42 +45412,36 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "819b3417-0f93-488d-974a-4f80c87eb48f",
+            "issued": "2021-10-17",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/ba35-nkej",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2021-10-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211004 to 20211010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bag9-usym",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-09-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-27",
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
-            "identifier": "d30cfc7c-4b32-4df1-b2bf-e0a850befd77",
             "description": "<p>This historic dataset with total enrollment in separate CHIP programs by month and state was created to fulfill reporting requirements under section 1902(tt)(1) of the Social Security Act, which was added by section 5131(b) of subtitle D of title V of division FF of the Consolidated Appropriations Act, 2023 (P.L. 117-328) (CAA, 2023). For each month from April 1, 2023, through June 30, 2024, states were required to submit to CMS (on a timely basis), and CMS was required to make public, certain monthly data, including the total number of beneficiaries who were enrolled in a separate CHIP program. Accordingly, this historic dataset contains separate CHIP enrollment by month and state between April 2023 and June 2024.</p>\r\n<p>CMS will continue to publicly report separate CHIP enrollment by month and state (beyond the historic CAA/Unwinding period) in a new dataset, which is available at <a href=\"https://data.medicaid.gov/dataset/4723da0d-4d04-46ce-8163-e4b58c8fe728\">[link]</a>. Please note that the methods used to count separate CHIP enrollees differ slightly between the two datasets; as a result, data users should exercise caution if comparing separate CHIP enrollment across the two datasets.</p>\r\n<p><b>Sources:</b> T-MSIS Analytic Files (TAF) and state-submitted enrollment totals. The data notes indicate when a state\u2019s monthly total was a state-submitted value, rather than from T-MSIS.<br /><br />TAF data were pulled as follows:<br />April 2023 enrollment - TAF as of August 2023<br />May 2023 enrollment - TAF as of August 2023<br />June 2023 enrollment - TAF as of September 2023<br />July 2023 enrollment - TAF as of October 2023<br />August 2023 enrollment - TAF as of November 2023<br />September 2023 enrollment - TAF as of December 2023<br />October 2023 enrollment - TAF as of January 2024<br />November 2023 enrollment - TAF as of February 2024<br />December 2023 enrollment - TAF as of March 2024<br />January 2024 enrollment - TAF as of April 2024<br />February 2024 enrollment - TAF as of May 2024<br />March 2024 enrollment - TAF as of June 2024<br />April 2024 enrollment \u2013 TAF as of July 2024<br/>May 2024 enrollment \u2013 TAF as of August 2024<br/>June 2024 enrollment \u2013 TAF as of September 2024</p>\t\r\n<p>TAF are produced one month after the T-MSIS submission month. For example, TAF as of August 2023 is based on July T-MSIS submissions.</p>\r\n<p><b>Notes:</b> The separate CHIP enrollment in this report is not inclusive of enrollees covered by Medicaid expansion CHIP. Enrollment includes individuals enrolled in separate CHIP at any point during the month but excludes those enrolled in both Medicaid and separate CHIP during the month. See the Data Sources and Metrics Definitions Overview document for a full description of the data sources, metric definitions, and general data limitations.<br /><br />Alaska, District of Columbia, Hawaii, New Hampshire, New Mexico, North Carolina, North Dakota, Ohio, South Carolina, Vermont, and Wyoming do not have separate CHIP Programs. Maryland has a separate CHIP program that began in July 2023; April 2023 - June 2023 data for Maryland represents retroactive coverage. <br /><br />This document includes separate CHIP data submitted to CMS by states via T-MSIS or a separate collection form. These data include reporting metrics consistent with section 1902(tt)(1) of the Social Security Act.<br /><br />CHIP: Children's Health Insurance Program</p>\t\r\n<p><b>Data notes:</b> \r\n(a) State-submitted value; data not from T-MSIS<br />(b1) May 2023 enrollment pulled from TAF as of September 2023<br />(b2) Data was restated using TAF as of October 2023<br />(b3) Data was restated using TAF as of April 2024<br />(b4) Data was restated using TAF as of July 2024<br />(b5) Data was restated using TAF as of August 2024<br />(c) Enrollment counts include postpartum women with coverage funded via a Health Services Initiative</p>",
-            "title": "Separate CHIP Enrollment by Month and State \u2013 Historic CAA/Unwinding Period",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45475,45 +45454,45 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "d30cfc7c-4b32-4df1-b2bf-e0a850befd77",
+            "issued": "2023-09-29",
+            "keyword": [
+                "applications",
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
+                "medicaid",
+                "program enrollment"
+            ],
+            "landingPage": "https://healthdata.gov/d/bag9-usym",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1M",
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
+            "title": "Separate CHIP Enrollment by Month and State \u2013 Historic CAA/Unwinding Period"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/rsvvaxview/",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-29",
-            "keyword": [
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
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
-            "identifier": "https://data.cdc.gov/api/views/ndai-i7s4",
             "description": "\u2022 Weekly Cumulative RSV Vaccination Coverage and Intent Among Adults 75 Years and Older and 60\u250074 Years with High Risk Conditions Ever Vaccinated with RSV Vaccine by Demographic Characteristics and Jurisdiction \n\u2022 Weekly estimates of RSV vaccination coverage and intent among adults 75 years and older and 60\u250074 years with high risk conditions are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/)\n\u2022 In June 2023, the Advisory Committee on Immunization Practices (ACIP) voted to recommend that adults aged \u226560 years may receive a single dose of an RSV vaccine, using shared clinical decision-making. In June 2024, the ACIP voted to recommend a single dose of RSV vaccine for all adults 75 years and older and adults 60\u201374 years who are at increased risk for severe RSV disease. The data below captures ever receiving a dose of an RSV vaccine by adults 60 years and older.\u202f",
-            "title": "Weekly Differences in Cumulative RSV Vaccination Coverage Among Adults 75 and Older and 60\u201374 Years with High-Risk Conditions Ever Vaccinated with RSV Vaccine, Overall, by Selected Demographics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45536,98 +45515,82 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/ndai-i7s4",
+            "issued": "2024-09-26",
+            "keyword": [
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
+                "rsv vaccination",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/rsvvaxview/",
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
+            "title": "Weekly Differences in Cumulative RSV Vaccination Coverage Among Adults 75 and Older and 60\u201374 Years with High-Risk Conditions Ever Vaccinated with RSV Vaccine, Overall, by Selected Demographics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://dip.doe-mbi.ucla.edu/dip/Main.cgi",
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
                 "fn": "BRAZHNIK, PAUL\u00a0",
                 "hasEmail": "mailto:brazhnikp@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "f064cdba-fa8d-4818-9c85-296ef4d514bb",
+            "dataQuality": true,
             "description": "<p>The DIP database catalogs experimentally determined interactions between proteins. It combines information from a variety of sources to create a single, consistent set of protein-protein interactions. The data stored within the DIP database are curated both manually by expert curators and also automatically using computational approaches that utilize the the knowledge about the protein-protein interaction networks extracted from the most reliable, core subset of the DIP data.</p>",
-            "title": "Database of Interacting Proteins (DIP)",
+            "identifier": "f064cdba-fa8d-4818-9c85-296ef4d514bb",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://dip.doe-mbi.ucla.edu/dip/Main.cgi",
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
+            "title": "Database of Interacting Proteins (DIP)"
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
-            "identifier": "https://data.cdc.gov/api/views/xvu4-xjdb",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2010/xvu4-xjdb",
             "description": "2010. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45650,53 +45613,69 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2010/xvu4-xjdb",
+            "identifier": "https://data.cdc.gov/api/views/xvu4-xjdb",
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
+            "title": "CDC PRAMStat Data for 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-innovation-advisors",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2015-01-01/2015-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-19",
-            "references": [
-                "https://data.cms.gov/resources/innovation-advisors-methodology"
-            ],
-            "keyword": [
-                "medicaid",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/6d6fe0be-25d8-473b-84f6-b3b9ef3e4469/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/innovation-advisors-data-dictionary",
             "description": "The CMS Innovation Center Innovation Advisors dataset provides information on individuals chosen by CMS as participants in the Innovation Advisors Program. The data\u00a0includes the name of the initiative, as well as participants names, geographic location including city and state, and geographic reach of the practice.\u00a0",
-            "title": "Innovation Center Innovation Advisors",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6d6fe0be-25d8-473b-84f6-b3b9ef3e4469/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6d6fe0be-25d8-473b-84f6-b3b9ef3e4469/data",
+                    "mediaType": "text/html",
                     "title": "Innovation Center Innovation Advisors : 2015-01-16"
                 },
                 {
@@ -45712,61 +45691,51 @@
                     "title": "Innovation Center Innovation Advisors : 2015-01-16"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/innovation-advisors-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6d6fe0be-25d8-473b-84f6-b3b9ef3e4469/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicaid",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-innovation-advisors",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-01-19",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/innovation-advisors-methodology"
+            ],
+            "temporal": "2015-01-01/2015-12-31",
             "theme": [
                 "Medicare",
                 "Medicaid"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Innovation Center Innovation Advisors"
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
-            "temporal": "1984-01-01/2019-12-31",
-            "modified": "2023-08-29",
-            "keyword": [
-                "african americans",
-                "age",
-                "alaskan natives",
-                "american natives",
-                "asian continental ancestry group",
-                "continental population groups",
-                "divorce",
-                "european continental ancestry group",
-                "health insurance",
-                "health us",
-                "hispanic americans",
-                "marital status",
-                "medicaid",
-                "oceanic ancestry group",
-                "poverty",
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
-            "identifier": "https://data.cdc.gov/api/views/km5s-4339",
             "description": "Data on Medicaid coverage among persons under age 65 by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health Interview Survey, health insurance supplements (1984, 1989, 1994-1996). Starting with 1997, data are from the family core and the sample adult questionnaires. Data for level of difficulty are from the 2010 Quality of Life, 2011-2017 Functioning and Disability, and 2018 Sample Adult questionnaires. For more information on the National Health Interview Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Medicaid coverage among persons under age 65, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45789,47 +45758,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/km5s-4339",
+            "issued": "2022-04-28",
+            "keyword": [
+                "african americans",
+                "age",
+                "alaskan natives",
+                "american natives",
+                "asian continental ancestry group",
+                "continental population groups",
+                "divorce",
+                "european continental ancestry group",
+                "health insurance",
+                "health us",
+                "hispanic americans",
+                "marital status",
+                "medicaid",
+                "oceanic ancestry group",
+                "poverty",
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "1984-01-01/2019-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Medicaid coverage among persons under age 65, by selected characteristics: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rtjs-ain8",
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
-                "vancomycin-intermediate staphylococcus aureus",
-                "vancomycin-resistant staphylococcus aureus",
-                "varicella morbidity",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC INFO",
                 "hasEmail": "mailto:cdcinfo.cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rtjs-ain8",
             "description": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45852,20 +45829,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rtjs-ain8",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "vancomycin-intermediate staphylococcus aureus",
+                "vancomycin-resistant staphylococcus aureus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rtjs-ain8",
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
+            "title": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2002-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) measures the<br />\nprevalence and correlates of drug use in the United States. The<br />\nsurveys are designed to provide quarterly, as well as annual,<br />\nestimates. Information is provided on the use of illicit drugs,<br />\nalcohol, and tobacco among members of United States households aged 12<br />\nand older. Questions include age at first use as well as lifetime,<br />\nannual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey includes questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents are<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2002 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, gang involvement,<br />\ndrug use by friends, social support, extracurricular activities,<br />\nexposure to substance abuse prevention and education programs, and<br />\nperceived adult attitudes toward drug use and activities such as<br />\nschool work. Several measures focused on prevention related themes in<br />\nthis section. Also retained were questions on mental health and access<br />\nto care, perceived risk of using drugs, perceived availability of<br />\ndrugs, driving and personal behavior, and cigar smoking. Questions on<br />\nthe tobacco brand used most often were introduced with the 1999 survey<br />\nand have been retained through the 2002 survey. Demographic data<br />\ninclude gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2002) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2002-nid13623",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2002-nid13623"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2002-nid13623",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -45898,67 +45911,29 @@
                 "substance abuse treatment",
                 "tranquilizers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2002-0",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2002-nid13623",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) measures the<br />\nprevalence and correlates of drug use in the United States. The<br />\nsurveys are designed to provide quarterly, as well as annual,<br />\nestimates. Information is provided on the use of illicit drugs,<br />\nalcohol, and tobacco among members of United States households aged 12<br />\nand older. Questions include age at first use as well as lifetime,<br />\nannual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey includes questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents are<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2002 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, gang involvement,<br />\ndrug use by friends, social support, extracurricular activities,<br />\nexposure to substance abuse prevention and education programs, and<br />\nperceived adult attitudes toward drug use and activities such as<br />\nschool work. Several measures focused on prevention related themes in<br />\nthis section. Also retained were questions on mental health and access<br />\nto care, perceived risk of using drugs, perceived availability of<br />\ndrugs, driving and personal behavior, and cigar smoking. Questions on<br />\nthe tobacco brand used most often were introduced with the 1999 survey<br />\nand have been retained through the 2002 survey. Demographic data<br />\ninclude gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2002)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2002-nid13623",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2002) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2002-nid13623"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2002)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/42jj-z7fa",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-30",
-            "keyword": [
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
                 "fn": "T.J. Pierce",
                 "hasEmail": "mailto:pwc2@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/42jj-z7fa",
             "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when members of the public in states and territories were subject to state and territorial executive orders, administrative orders, resolutions, and proclamations for COVID-19 that require them to wear masks in public. \u201cMembers of the public\u201d are defined as individuals operating in a personal capacity. \u201cIn public\u201d is defined to mean either (1) anywhere outside the home or (2) both in retail businesses and in restaurants/food establishments. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level. \n\nThese data are derived from publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly require individuals to wear masks in public found by the CDC, COVID-19 Community Intervention & Critical Populations Task Force, Monitoring & Evaluation Team, Mitigation Policy Analysis Unit, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program, and Max Gakh, Assistant Professor, School of Public Health, University of Nevada, Las Vegas from April 10, 2020 through July 20, 2021.  These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. Effective and expiration dates were coded using only the dates provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not include data on counties that have opted out of their state mask mandate pursuant to state law. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Public Mask Mandates From April 10, 2020 through July 20, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45981,23 +45956,72 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/42jj-z7fa",
+            "issued": "2021-12-10",
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
+            "landingPage": "https://data.cdc.gov/d/42jj-z7fa",
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
+            "title": "U.S. State and Territorial Public Mask Mandates From April 10, 2020 through July 20, 2021 by County by Day"
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
-                "https://chronicdata.cdc.gov/d/i6st-vu2f"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Youth-Tobacco-Survey-YTS-Data/4juz-x2tp",
+            "description": "1999-2017.  Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  YTS Data.  The YTS was developed to provide states with comprehensive data on both middle school and high school students regarding tobacco use, exposure to environmental tobacco smoke, smoking cessation, school curriculum, minors' ability to purchase or otherwise obtain tobacco products, knowledge and attitudes about tobacco, and familiarity with pro-tobacco and anti-tobacco media messages.  The YTS uses a two-stage cluster sample design to produce representative samples of students in middle schools (grades 6\u20138) and high schools (grades 9\u201312).  The data for the STATE System were extracted from Youth Tobacco Surveys from participating states.  Tobacco topics included are cigarette smoking prevalence, cigarette smoking frequency, smokeless tobacco products prevalence and quit attempts.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4juz-x2tp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4juz-x2tp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4juz-x2tp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4juz-x2tp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4juz-x2tp",
+            "issued": "2025-01-31",
             "keyword": [
                 "cessation",
                 "cigarette",
@@ -46022,76 +46046,37 @@
                 "tobacco use",
                 "youth"
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
-            "identifier": "https://data.cdc.gov/api/views/4juz-x2tp",
-            "description": "1999-2017.  Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  YTS Data.  The YTS was developed to provide states with comprehensive data on both middle school and high school students regarding tobacco use, exposure to environmental tobacco smoke, smoking cessation, school curriculum, minors' ability to purchase or otherwise obtain tobacco products, knowledge and attitudes about tobacco, and familiarity with pro-tobacco and anti-tobacco media messages.  The YTS uses a two-stage cluster sample design to produce representative samples of students in middle schools (grades 6\u20138) and high schools (grades 9\u201312).  The data for the STATE System were extracted from Youth Tobacco Surveys from participating states.  Tobacco topics included are cigarette smoking prevalence, cigarette smoking frequency, smokeless tobacco products prevalence and quit attempts.",
-            "title": "Youth Tobacco Survey (YTS) Data",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4juz-x2tp/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4juz-x2tp/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4juz-x2tp/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4juz-x2tp/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
+            "references": [
+                "https://chronicdata.cdc.gov/d/i6st-vu2f"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Youth-Tobacco-Survey-YTS-Data/4juz-x2tp",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "Youth Tobacco Survey (YTS) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bdcr-kmyg",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-11-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-06",
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
-            "identifier": "4d2b3013-7162-4ee7-8af3-849e41f0a7da",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-30-to-2023-11-05",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46100,21 +46085,46 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-30-to-2023-11-05"
                 }
             ],
+            "identifier": "4d2b3013-7162-4ee7-8af3-849e41f0a7da",
+            "issued": "2023-11-08",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/bdcr-kmyg",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-11-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-30-to-2023-11-05"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/federal-health-it-strategic-plan-2015-2020-goals",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2015-09-01",
-            "references": [
-                "https://www.healthit.gov/sites/default/files/9-5-federalhealthitstratplanfinal_0.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/federal-health-it-strategic-plan-2015-2020-goals",
+            "description": "The Federal Health IT Strategic Plan 2015-2020 explains how the federal government intends to apply the effective use of information and technology to help the nation achieve high-quality care, lower costs, a healthy population, and engaged individuals. The work described in this Plan aims to modernize the U.S. health IT infrastructure so that individuals, their providers, and communities can use it to help achieve health and wellness goals. The Plan goals, objectives, and strategies outline how this work will be organized and tracked over the term of this Plan. Access the full list of goals, objectives, and strategies below.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/federal-health-it-strategic-plan-2015-2020-goals.csv",
+                    "mediaType": "text/csv",
+                    "title": "federal-health-it-strategic-plan-2015-2020-goals.csv"
+                }
             ],
+            "identifier": "5oubhewj-dyyu-xdf1-4uip-petoebzik6ii",
+            "issued": "2023-10-03",
             "keyword": [
                 "adoption",
                 "certified health information technology",
@@ -46128,61 +46138,33 @@
                 "quality care",
                 "strategy"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/federal-health-it-strategic-plan-2015-2020-goals",
+            "modified": "2015-09-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "5oubhewj-dyyu-xdf1-4uip-petoebzik6ii",
-            "description": "The Federal Health IT Strategic Plan 2015-2020 explains how the federal government intends to apply the effective use of information and technology to help the nation achieve high-quality care, lower costs, a healthy population, and engaged individuals. The work described in this Plan aims to modernize the U.S. health IT infrastructure so that individuals, their providers, and communities can use it to help achieve health and wellness goals. The Plan goals, objectives, and strategies outline how this work will be organized and tracked over the term of this Plan. Access the full list of goals, objectives, and strategies below.",
-            "title": "Federal Health IT Strategic Plan: 2015-2020 Goals",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/federal-health-it-strategic-plan-2015-2020-goals.csv",
-                    "mediaType": "text/csv",
-                    "title": "federal-health-it-strategic-plan-2015-2020-goals.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/sites/default/files/9-5-federalhealthitstratplanfinal_0.pdf"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/federal-health-it-strategic-plan-2015-2020-goals"
+            "title": "Federal Health IT Strategic Plan: 2015-2020 Goals"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bemt-5git",
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
-                "plan attributes",
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
-            "identifier": "8a1786d6-e3cc-43be-bcfa-10e98f514ba4",
             "description": "The Plan Attributes PUF (Plan-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Plan-PUF contains plan variant-level data on maximum out of pocket payments, deductibles, health savings account (HSA) eligibility, and other plan attributes.",
-            "title": "Plan Attributes PUF - PY2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46190,51 +46172,46 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "8a1786d6-e3cc-43be-bcfa-10e98f514ba4",
+            "issued": "2023-08-09",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "plan attributes",
+                "py2023"
+            ],
+            "landingPage": "https://healthdata.gov/d/bemt-5git",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Plan Attributes PUF - PY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/program-integrity-market-saturation-by-type-of-service/market-saturation-utilization-state-county",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2023-01-01/2023-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
-            "references": [
-                "https://data.cms.gov/resources/market-saturation-utilization-state-county-methodology"
-            ],
-            "keyword": [
-                "counties",
-                "fraud waste & abuse prevention",
-                "health care use & payments",
-                "medicare",
-                "national",
-                "original medicare",
-                "states & territories"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Market Saturation - CPI",
                 "hasEmail": "mailto:MarketSaturation@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/8900b9c5-50b7-43de-9bdd-0d7113a8355e/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/market-saturation-utilization-state-county-data-dictionary",
             "description": "The Market Saturation and Utilization State-County dataset provides monitoring of market saturation as a means to help prevent potential fraud, waste, and abuse (FWA). Market saturation, in the present context, refers to the density of providers of a particular service within a defined geographic area relative to the number of beneficiaries receiving that service in the area. The data can be used to reveal the degree to which use of a service is related to the number of providers servicing a geographic region. There are also a number of secondary research uses for these data, but one objective of making these data public is to assist health care providers in making informed decisions about their service locations and the beneficiary population they serve.\n\nThe interactive dataset can be filtered and analyzed on the site or downloaded in Excel format.",
-            "title": "Market Saturation & Utilization State-County",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8900b9c5-50b7-43de-9bdd-0d7113a8355e/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8900b9c5-50b7-43de-9bdd-0d7113a8355e/data",
+                    "mediaType": "text/html",
                     "title": "Market Saturation & Utilization State-County : 2023-12-04"
                 },
                 {
@@ -46250,49 +46227,52 @@
                     "title": "Market Saturation & Utilization State-County : 2023-12-04"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/market-saturation-utilization-state-county-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/8900b9c5-50b7-43de-9bdd-0d7113a8355e/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "counties",
+                "fraud waste & abuse prevention",
+                "health care use & payments",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/program-integrity-market-saturation-by-type-of-service/market-saturation-utilization-state-county",
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
+                "https://data.cms.gov/resources/market-saturation-utilization-state-county-methodology"
+            ],
+            "temporal": "2023-01-01/2023-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Market Saturation & Utilization State-County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bev8-iywz",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-03-12",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-17",
-            "keyword": [
-                "chip",
-                "eligibility levels",
-                "federal poverty level",
-                "fpl",
-                "magi",
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
-            "identifier": "d7e4cccb-1c56-5b5d-acce-5e7744c6d3b4",
             "description": "The following table provides eligibility levels in each state for key coverage groups that use Modified Adjusted Gross Income (MAGI), as of April 1, 2018. The data represent the principal, but not all, MAGI coverage groups in Medicaid, the Children\u2019s Health Insurance Program (CHIP), and the Basic Health Program (BHP). All income standards are expressed as a percentage of the federal poverty level (FPL). The MAGI-based rules generally include adjusting an individual\u2019s income by an amount equivalent to a 5% FPL disregard. Other eligibility criteria also apply, such as citizenship, immigration status, and state residency.\r\n\r\nFor more information, see: \r\nhttps://www.medicaid.gov/medicaid/program-information/medicaid-and-chip-eligibility-levels/index.html",
-            "title": "Medicaid and CHIP Eligibility Levels",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46301,22 +46281,52 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "d7e4cccb-1c56-5b5d-acce-5e7744c6d3b4",
+            "issued": "2018-03-12",
+            "keyword": [
+                "chip",
+                "eligibility levels",
+                "federal poverty level",
+                "fpl",
+                "magi",
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/bev8-iywz",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2018-11-17",
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
+            "title": "Medicaid and CHIP Eligibility Levels"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225434.htm",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "Contains data for FDA shell egg recalls.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "dc522ec9-a996-440b-b94e-972136ab80c0",
             "issued": "2021-02-25",
-            "temporal": "2010-01-01/2010-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "community health",
                 "food",
@@ -46326,109 +46336,77 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225434.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "dc522ec9-a996-440b-b94e-972136ab80c0",
-            "description": "Contains data for FDA shell egg recalls.",
-            "title": "FDA Shell Egg Recalls",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xls",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "temporal": "2010-01-01/2010-12-31",
+            "title": "FDA Shell Egg Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bfdt-c7p4",
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
-            "identifier": "ec9aaf6f-f7e4-560d-8db1-a297ace39b5f",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard FILTERS v0.3.58-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/FILTERS.csv",
-                    "description": "Scorecard FILTERS v0.3.58-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard FILTERS v0.3.58-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/FILTERS.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard FILTERS v0.3.58-test (local)"
                 }
             ],
+            "identifier": "ec9aaf6f-f7e4-560d-8db1-a297ace39b5f",
+            "issued": "2023-08-10",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/bfdt-c7p4",
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
+            "title": "Scorecard FILTERS v0.3.58-test (local)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -46451,51 +46429,45 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1H. Cholera to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-07-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
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
-                "puerto rico",
-                "race",
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
-            "identifier": "https://data.cdc.gov/api/views/qfhf-uhaa",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis visualization provides weekly data on the number of deaths from all causes by jurisdiction of occurrence and race and Hispanic origin. Numbers of deaths are also shown for all causes excluding COVID-19, and for COVID-19. Counts of deaths in more recent weeks can be compared with counts from earlier years to determine if the number is higher than expected.",
-            "title": "Weekly Counts of Deaths by Jurisdiction, and Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46518,22 +46490,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/qfhf-uhaa",
+            "issued": "2020-07-22",
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
+                "puerto rico",
+                "race",
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
+            "title": "Weekly Counts of Deaths by Jurisdiction, and Race and Hispanic Origin"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/child-support-enforcement-annual-data-report-form-34a-and-instructions",
             "bureauCode": [
                 "001:05"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HHS/ACF/OCSE Data Questions",
+                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Federally approved OCSE Form 34A and instructions for child support professionals.</p>",
+            "identifier": "4f03d9be-5b22-49bb-ae18-61ad0f6c7d57",
             "issued": "2014-02-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "administrative",
                 "case management",
@@ -46571,65 +46576,35 @@
                 "tribal plan",
                 "verification of employment"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HHS/ACF/OCSE Data Questions",
-                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/child-support-enforcement-annual-data-report-form-34a-and-instructions",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:084"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Administration for Children and Families, Department of Health & Human Services"
             },
-            "identifier": "4f03d9be-5b22-49bb-ae18-61ad0f6c7d57",
-            "description": "<p>Federally approved OCSE Form 34A and instructions for child support professionals.</p>",
-            "title": "OFFICE OF CHILD SUPPORT ENFORCEMENT",
-            "programCode": [
-                "009:084"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "National",
                 "State"
-            ]
+            ],
+            "title": "OFFICE OF CHILD SUPPORT ENFORCEMENT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/brfss/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2017-04-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-14",
-            "references": [
-                "https://www.cdc.gov/brfss/"
-            ],
-            "keyword": [
-                "behavioral",
-                "brfss",
-                "factor",
-                "questions",
-                "risk",
-                "surveillance",
-                "survey",
-                "system"
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
-            "identifier": "https://data.cdc.gov/api/views/iuq5-y9ct",
+            "describedBy": "https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
             "description": "1984-2023.  Centers for Disease Control and Prevention (CDC). BRFSS Survey Data.  The BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death.\nDetailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss).",
-            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Historical Questions",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46652,21 +46627,73 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "theme": [
-                "Behavioral Risk Factors"
-            ]
-        },
+            "identifier": "https://data.cdc.gov/api/views/iuq5-y9ct",
+            "issued": "2017-04-12",
+            "keyword": [
+                "behavioral",
+                "brfss",
+                "factor",
+                "questions",
+                "risk",
+                "surveillance",
+                "survey",
+                "system"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-14",
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
+            "theme": [
+                "Behavioral Risk Factors"
+            ],
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Historical Questions"
+        },
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
+            "description": "Provisional counts of deaths by the month the deaths occurred, by age group and race/ethnicity, for select underlying causes of death for 2020-2021. Final data is provided for 2019. The dataset also includes monthly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r5pw-bk5t/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r5pw-bk5t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r5pw-bk5t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r5pw-bk5t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/r5pw-bk5t",
             "issued": "2021-02-11",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
             "keyword": [
                 "age",
                 "age group",
@@ -46696,81 +46723,35 @@
                 "septicemia",
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
-            "identifier": "https://data.cdc.gov/api/views/r5pw-bk5t",
-            "description": "Provisional counts of deaths by the month the deaths occurred, by age group and race/ethnicity, for select underlying causes of death for 2020-2021. Final data is provided for 2019. The dataset also includes monthly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
-            "title": "AH Monthly Provisional Counts of Deaths for Select Causes of Death by Age, and Race and Hispanic Origin",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/r5pw-bk5t/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/r5pw-bk5t/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/r5pw-bk5t/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/r5pw-bk5t/rows.xml?accessType=DOWNLOAD",
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
+            "title": "AH Monthly Provisional Counts of Deaths for Select Causes of Death by Age, and Race and Hispanic Origin"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bj6z-7dpu",
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
-            "identifier": "d3ea6f2d-a517-4f9b-a2fb-1ffcaebc3107",
             "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2024 Individual Dental",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46778,39 +46759,39 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "d3ea6f2d-a517-4f9b-a2fb-1ffcaebc3107",
+            "issued": "2024-08-06",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2024",
+                "qhp landscape",
+                "sadp"
+            ],
+            "landingPage": "https://healthdata.gov/d/bj6z-7dpu",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2024 Individual Dental"
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
-            "modified": "2025-01-17",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -46833,83 +46814,80 @@
                     "mediaType": "application/xml"
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
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
             "accessLevel": "public",
-            "landingPage": "http://www.iedb.org/",
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
                 "fn": "Deckhut, Alison",
                 "hasEmail": "mailto:augustine@niaid.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "7c8fdef9-811d-4672-817a-8576c5a4376f",
+            "dataQuality": true,
             "description": "<p>This repository contains antibody/B cell and T cell epitope information and epitope prediction and analysis tools for use by the research community worldwide. Immune epitopes are defined as molecular structures recognized by specific antigen receptors of the immune system, namely antibodies, B cell receptors, and T cell receptors. Immune epitopes from infectious diseases, excluding HIV, and immune-mediated diseases and the accompanying biological information are included.</p>",
-            "title": "Immune Epitope Database and Analysis Resource (IEDB)",
+            "identifier": "7c8fdef9-811d-4672-817a-8576c5a4376f",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.iedb.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
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
+            "title": "Immune Epitope Database and Analysis Resource (IEDB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-geographic-comparisons/medicare-geographic-variation-by-hospital-referral-region",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-12-20",
-            "temporal": "2013-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2023-02/d30ee401-edd4-4d41-a631-69d95356dc2d/Geographic%20Variation%20Public%20Use%20File%20Methods%20Paper.pdf"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "hospital referral regions",
-                "medicare",
-                "national",
-                "original medicare"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/6d7b229d-5bfb-4666-a2d2-38cea44a112c/data-viewer",
-            "description": "The Medicare Geographic Variation by Hospital Referral Region dataset provides information for researchers and policymakers to evaluate the geographic differences in the use and quality of health care services for the Original Medicare population. The dataset includes demographic, spending, use, and quality indicators at the hospital referral region (HRR) level.\n\n\u00a0\n\nPlease note that CMS has decided to discontinue updates to the Fee-for-Service (FFS) Geographic Variation Public Use File by Hospital Referral Region, so the dataset is retired. Data in the FFS Geographic Variation Public Use File by Hospital Referral Region has been divided into two files: 2007-2013 data and 2014-2021 data. This was done to account for changes to the Geographic Variation methodology beginning with data year 2014. The 2007-2013 data is located under data year 2013, and the 2014-2021 data is located under data year 2021.",
-            "title": "Medicare Geographic Variation - by Hospital Referral Region",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-12/2014-2021%20Medicare%20FFS%20Geographic%20Variation%20HRR%20Data%20Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Medicare Geographic Variation by Hospital Referral Region dataset provides information for researchers and policymakers to evaluate the geographic differences in the use and quality of health care services for the Original Medicare population. The dataset includes demographic, spending, use, and quality indicators at the hospital referral region (HRR) level.\n\n\u00a0\n\nPlease note that CMS has decided to discontinue updates to the Fee-for-Service (FFS) Geographic Variation Public Use File by Hospital Referral Region, so the dataset is retired. Data in the FFS Geographic Variation Public Use File by Hospital Referral Region has been divided into two files: 2007-2013 data and 2014-2021 data. This was done to account for changes to the Geographic Variation methodology beginning with data year 2014. The 2007-2013 data is located under data year 2013, and the 2014-2021 data is located under data year 2021.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46924,93 +46902,97 @@
                     "title": "Medicare Geographic Variation - by Hospital Referral Region : 2013-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-12/2014-2021%20Medicare%20FFS%20Geographic%20Variation%20HRR%20Data%20Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6d7b229d-5bfb-4666-a2d2-38cea44a112c/data-viewer",
+            "issued": "2024-12-20",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospital referral regions",
+                "medicare",
+                "national",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-geographic-comparisons/medicare-geographic-variation-by-hospital-referral-region",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-12-19",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2023-02/d30ee401-edd4-4d41-a631-69d95356dc2d/Geographic%20Variation%20Public%20Use%20File%20Methods%20Paper.pdf"
+            ],
+            "temporal": "2013-01-01/2021-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Geographic Variation - by Hospital Referral Region"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bkf8-77qr",
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
-            "identifier": "e1f19f91-424b-5769-81a4-5878fb5fefd9",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure v2.11.9 (impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure.csv",
-                    "description": "Scorecard measure v2.11.9 (impl)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure v2.11.9 (impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure v2.11.9 (impl)"
                 }
             ],
+            "identifier": "e1f19f91-424b-5769-81a4-5878fb5fefd9",
+            "issued": "2023-06-29",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/bkf8-77qr",
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
+            "title": "Scorecard measure v2.11.9 (impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/assisted-reproductive-technology-art-surveillance",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-05-30",
-            "temporal": "1995-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "infertility",
-                "quality measurement",
-                "reproductive health"
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
-            "identifier": "329645f5-726d-4a73-9b18-044642e6532f",
+            "dataQuality": true,
             "description": "<p>In 1992, Congress enacted the Fertility Clinic Success Rate and Certification Act (FCSRCA). The act requires CDC to collect  data from clinics and submit an annual report to Congress on Assisted Reproductive Technology (ART) success rates. In 1996, CDC initiated the ART Surveillance System to collect cycle specific and clinic specific data from all medical clinics practicing ART in the United States and its territories.  The data collected include patient's diagnosis, type of ART,  clinical information pertaining to the ART procedure, and information on pregnancy outcomes.</p>",
-            "title": "Assisted Reproductive Technology (ART) Surveillance",
-            "programCode": [
-                "009:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47019,47 +47001,41 @@
                     "title": "Query Tool "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "329645f5-726d-4a73-9b18-044642e6532f",
+            "issued": "2012-05-30",
+            "keyword": [
+                "infertility",
+                "quality measurement",
+                "reproductive health"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/assisted-reproductive-technology-art-surveillance",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1995-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Assisted Reproductive Technology (ART) Surveillance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fqve-8wzt",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-29",
-            "keyword": [
-                "2014",
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
-            "identifier": "https://data.cdc.gov/api/views/fqve-8wzt",
             "description": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. \r\n\r\n* Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\r\n\ufffd\ufffd\ufffd Illnesses with similar clinical presentation that result from Spotted fever group rickettsia infections are reported as Spotted fever rickettsiosis. Rocky Mountain spotted fever (RMSF) caused by Rickettsia rickettsii, is the most common and well-known spotted fever.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47082,40 +47058,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fqve-8wzt",
+            "issued": "2015-01-08",
+            "keyword": [
+                "2014",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "rmsf",
+                "spotted fever rickettsiosis",
+                "syphilis primary and secondary",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fqve-8wzt",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-04-29",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -47138,87 +47120,87 @@
                     "mediaType": "application/xml"
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
+            "title": "Selected Trend Table from Health, United States, 2011. Health conditions among children under 18 years of age, by selected characteristics: United States, average annual, selected years 1997 - 1999 through 2008 - 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bmpj-55us",
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
-            "identifier": "c6957298-4fec-5d1d-9cf0-5fcd3024bf15",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard version v2.12.1-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/version.csv",
-                    "description": "Scorecard version v2.12.1-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard version v2.12.1-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/version.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard version v2.12.1-test (local)"
                 }
             ],
+            "identifier": "c6957298-4fec-5d1d-9cf0-5fcd3024bf15",
+            "issued": "2023-08-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/bmpj-55us",
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
+            "title": "Scorecard version v2.12.1-test (local)"
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
-            "modified": "2025-01-29",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -47241,48 +47223,45 @@
                     "mediaType": "application/xml"
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
+            "title": "Vaccination Concerns, Issues, and Motivators | RespVaxView | Data | Centers for Disease Control and Prevention (cdc.gov)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -47305,45 +47284,44 @@
                     "mediaType": "application/xml"
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-12",
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
+            "title": "Vaccination Coverage among Health Care Personnel"
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
@@ -47366,58 +47344,106 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/NOHSS-Adult-Indicators-2010-And-Prior-BRFSS/aemk-wcbf",
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
+            "title": "NOHSS Adult Indicators - 2010 And Prior BRFSS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://pediatricmri.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Rumsey, Judy",
+                "hasEmail": "mailto:jrumsey@mail.nih.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The NIH Study of Normal Brain Development is a longitudinal study using anatomical MRI, diffusion tensor imaging (DTI), and MR spectroscopy (MRS) to map pediatric brain development.</p>",
+            "identifier": "8abea208-9ff7-4ff6-a1fa-a85b0afe6287",
             "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "brain",
                 "brain development",
                 "diffusion tensor imaging",
                 "mri"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Rumsey, Judy",
-                "hasEmail": "mailto:jrumsey@mail.nih.gov"
-            },
+            "landingPage": "http://pediatricmri.nih.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Institutes of Health (NIH)"
             },
-            "identifier": "8abea208-9ff7-4ff6-a1fa-a85b0afe6287",
-            "description": "<p>The NIH Study of Normal Brain Development is a longitudinal study using anatomical MRI, diffusion tensor imaging (DTI), and MR spectroscopy (MRS) to map pediatric brain development.</p>",
-            "title": "Pediatric MRI",
-            "programCode": [
-                "009:046"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Pediatric MRI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:healthus@cdc.gov"
+            },
+            "description": "NOTE: On October 19, 2021, estimates for 2016\u20132018 by health insurance status were revised to correct errors. Changes are highlighted and tagged at https://www.cdc.gov/nchs/data/hus/2019/012-508.pdf\n\nData on health conditions among children under age 18, by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time.\n\nSOURCE: NCHS, National Health Interview Survey, Family Core and Sample Child questionnaires.  For more information on the National Health Interview Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2m93-xvra/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2m93-xvra/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2m93-xvra/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2m93-xvra/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/2m93-xvra",
             "issued": "2021-06-07",
-            "@type": "dcat:Dataset",
-            "temporal": "1997/2019",
-            "modified": "2023-08-29",
             "keyword": [
                 "african americans",
                 "age",
@@ -47448,59 +47474,46 @@
                 "sex",
                 "skin"
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
-            "identifier": "https://data.cdc.gov/api/views/2m93-xvra",
-            "description": "NOTE: On October 19, 2021, estimates for 2016\u20132018 by health insurance status were revised to correct errors. Changes are highlighted and tagged at https://www.cdc.gov/nchs/data/hus/2019/012-508.pdf\n\nData on health conditions among children under age 18, by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time.\n\nSOURCE: NCHS, National Health Interview Survey, Family Core and Sample Child questionnaires.  For more information on the National Health Interview Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Health conditions among children under age 18, by selected characteristics: United States",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-08-29",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/2m93-xvra/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/2m93-xvra/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/2m93-xvra/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/2m93-xvra/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1997/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Health conditions among children under age 18, by selected characteristics: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2011",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug-related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 22 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network (DAWN-2011) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2011-nid13586",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2011-nid13586"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2011-nid13586",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "demographic characteristics",
@@ -47513,67 +47526,30 @@
                 "substance abuse",
                 "suicide"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2011",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2011-nid13586",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug-related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 22 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network (DAWN-2011)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2011-nid13586",
-                    "description": "Drug Abuse Warning Network (DAWN-2011) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2011-nid13586"
-                }
-            ]
+            "title": "Drug Abuse Warning Network (DAWN-2011)"
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DDT Public Inquiries",
                 "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2t2r-sf6s",
+            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/National-Health-Interview-Survey-NHIS-Vision-and-E/2t2r-sf6s",
             "description": "2014-15 merged, 2016-17 merged. This dataset is a de-identified summary table of vision and eye health data indicators from NHIS, stratified by all available combinations of age group, race/ethnicity, gender, and risk factor. NHIS is an annual household survey conducted by the National Center for Health Statistics at CDC that monitors trends in illness, disabilities, and progress towards national health objectives. Approximate sample size is 35,000 households and 87,500 persons annually. NHIS data for VEHSS includes questions related to Visual Function. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Data will be updated as it becomes available. Detailed information on VEHSS NHIS analyses can be found on the VEHSS NHIS webpage (link). Additional information about NHIS can be found on the NHIS website (http://www.cdc.gov/nchs/nhis/about_nhis.htm). The VEHSS NHIS dataset was last updated in November 2019.",
-            "title": "National Health Interview Survey (NHIS) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47596,52 +47572,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/National-Health-Interview-Survey-NHIS-Vision-and-E/2t2r-sf6s",
+            "identifier": "https://data.cdc.gov/api/views/2t2r-sf6s",
+            "issued": "2023-09-21",
+            "keyword": [
+                "blind",
+                "contact lenses",
+                "glasses",
+                "nhis",
+                "vision correction",
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
+                "http://www.cdc.gov/nchs/nhis/about_nhis.htm",
+                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-health-interview-survey.html"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "National Health Interview Survey (NHIS) \u2013 Vision and Eye Health Surveillance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/medicare-demonstrations",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2024-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-12",
-            "references": [
-                "https://data.cms.gov/resources/medicare-demonstrations-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/0764d86c-d19c-4b73-9e57-eba3cc1f7849/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-demonstrations-data-dictionary",
             "description": "The Medicare Demonstrations dataset provides information on demonstrations conducted in the CMS Innovation Center. It includes the demonstration project name, type, description, year, and website for the demonstration page.",
-            "title": "Medicare Demonstrations",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0764d86c-d19c-4b73-9e57-eba3cc1f7849/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0764d86c-d19c-4b73-9e57-eba3cc1f7849/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Demonstrations : 2024-04-12"
                 },
                 {
@@ -47657,45 +47637,49 @@
                     "title": "Medicare Demonstrations : 2024-04-12"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-demonstrations-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/0764d86c-d19c-4b73-9e57-eba3cc1f7849/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/medicare-demonstrations",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-04-12",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-demonstrations-methodology"
+            ],
+            "temporal": "2024-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Demonstrations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/animaldrugsatfda/index.cfm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
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
-            "identifier": "ee7073db-55c0-46b0-b831-1c659fe7137d",
             "description": "On November 16, 1988, the President of the United States signed into law the Generic Animal Drug and Patent Restoration Act (GADPTRA). Among its major provisions, the Act extends eligibility for submission of Abbreviated New Animal Drug Applications (ANADAs) to all animal drug products approved for safety and effectiveness under the Federal Food, Drug, and Cosmetic Act. The Act also requires that each sponsor of an approved animal drug product submit to the FDA certain information regarding patents held for the animal drug or its method of use. The Act requires that this information, as well as a list of all animal drug products approved for safety and effectiveness, be made available to the public. This list must be updated monthly under the provisions of the Act. This publication, which is known as the \ufffdGreen Book\ufffd, was first published in January of 1989. Updates have been added monthly since then. The list is published in its entirety each January.",
-            "title": "Approved Animal Drug Products (Green Book)",
-            "programCode": [
-                "009:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47703,46 +47687,36 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "ee7073db-55c0-46b0-b831-1c659fe7137d",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cvm",
+                "labeling"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/animaldrugsatfda/index.cfm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:004"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Approved Animal Drug Products (Green Book)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/u7wx-dav2",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/u7wx-dav2",
             "description": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html\r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47765,46 +47739,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/u7wx-dav2",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/u7wx-dav2",
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
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-08-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-09",
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "keyword": [
-                "cardiovascular disease",
-                "claims data",
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
-            "identifier": "https://data.cdc.gov/api/views/iw6q-r3ja",
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Center-for-Medicare-Medicaid-Services-CMS-Medicare/iw6q-r3ja",
             "description": "2016\u20132021. CMS compiles claims data for Medicare and Medicaid patients across a variety of categories and years. This includes Inpatient and Outpatient claims, Master Beneficiary Summary Files, and many other files. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (national and state) and indicator. The data can be plotted as trends and stratified by sex and race/ethnicity.",
-            "title": "Center for Medicare & Medicaid Services (CMS) , Medicare Claims data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47827,21 +47804,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Center-for-Medicare-Medicaid-Services-CMS-Medicare/iw6q-r3ja",
+            "identifier": "https://data.cdc.gov/api/views/iw6q-r3ja",
+            "issued": "2023-08-11",
+            "keyword": [
+                "cardiovascular disease",
+                "claims data",
+                "heart disease",
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
                 "Heart Disease & Stroke Prevention"
-            ]
+            ],
+            "title": "Center for Medicare & Medicaid Services (CMS) , Medicare Claims data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/Widgets/",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "The FDA Peanut-Containing Product Recall widget allows you to browse the Food and Drug Administration (FDA) database of peanut butter and peanut-containing products subject to recall. This database makes it easier for you to determine whether any of the products you have at home are subject to recent recalls, and will be updated as new information becomes available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/Widgets/",
+                    "mediaType": "application/vnd.pmi.widget"
+                }
+            ],
+            "identifier": "ece9c52a-ba02-4615-b441-fa0d2f8b9722",
             "issued": "2025-01-30",
-            "@type": "dcat:Dataset",
-            "modified": "2012-05-30",
             "keyword": [
                 "brownie",
                 "cake and pie",
@@ -47862,106 +47873,77 @@
                 "salmonella",
                 "snack bars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.cdc.gov/Widgets/",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2012-05-30",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "ece9c52a-ba02-4615-b441-fa0d2f8b9722",
-            "description": "The FDA Peanut-Containing Product Recall widget allows you to browse the Food and Drug Administration (FDA) database of peanut butter and peanut-containing products subject to recall. This database makes it easier for you to determine whether any of the products you have at home are subject to recent recalls, and will be updated as new information becomes available.",
-            "title": "FDA Peanut-Containing Product Recall",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cdc.gov/Widgets/",
-                    "mediaType": "application/vnd.pmi.widget"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Peanut-Containing Product Recall"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bver-eziq",
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
-            "identifier": "58af1996-6af7-5b7c-82a8-6d69c5652420",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure.csv",
-                    "description": "CoreSEt measure v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "58af1996-6af7-5b7c-82a8-6d69c5652420",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/bver-eziq",
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
+            "title": "CoreSEt measure v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bvst-ezb8",
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
-                "py2025",
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
-            "identifier": "46925516-0fb4-4e60-b00d-b0d7f7ddc372",
             "description": "The Service Area PUF (SA-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The SA-PUF contains issuer-level data on geographic service areas including state, county, and zip code.",
-            "title": "Service Area PUF \u2013 PY2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47969,38 +47951,37 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "46925516-0fb4-4e60-b00d-b0d7f7ddc372",
+            "issued": "2024-12-10",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2025",
+                "service area"
+            ],
+            "landingPage": "https://healthdata.gov/d/bvst-ezb8",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Service Area PUF \u2013 PY2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/v76h-zdce",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/v76h-zdce",
             "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2001-2005. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level Ozone Concentrations, 2001-2005",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48023,46 +48004,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/v76h-zdce",
+            "issued": "2020-06-01",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "ozone"
+            ],
+            "landingPage": "https://data.cdc.gov/d/v76h-zdce",
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
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2001-2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ekd3-qu3w",
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
-            "identifier": "https://data.cdc.gov/api/views/ekd3-qu3w",
             "description": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Illnesses with similar clinical presentation that result from Spotted fever group rickettsia infections are reported as Spotted fever rickettsioses. Rocky Mountain spotted fever (RMSF) caused by Rickettsia rickettsii, is the most common and well-known spotted fever.",
-            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48085,38 +48061,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ekd3-qu3w",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "rmsf",
+                "spotted fever rickettsiosis",
+                "syphilis primary and secondary",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ekd3-qu3w",
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
+            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bw9e-y3qb",
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
-            "identifier": "85272998-7ec9-4bd9-87ef-8c75156436ac",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210830 to 20210905",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48124,18 +48109,46 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "85272998-7ec9-4bd9-87ef-8c75156436ac",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/bw9e-y3qb",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210830 to 20210905"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2014",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2014 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nThis study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2014) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2014-nid13618",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2014-nid13618"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2014-nid13618",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -48176,68 +48189,29 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2014",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2014-nid13618",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2014 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nThis study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2014)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2014-nid13618",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2014) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2014-nid13618"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2014)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rg4j-6mcc",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "2014",
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
-            "identifier": "https://data.cdc.gov/api/views/rg4j-6mcc",
             "description": "NNDSS - Table II. Hepatitis (viral, acute) - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Hepatitis (viral, acute)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48260,51 +48234,58 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rg4j-6mcc",
+            "issued": "2015-01-08",
+            "keyword": [
+                "2014",
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
+            "landingPage": "https://data.cdc.gov/d/rg4j-6mcc",
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
+            "title": "NNDSS - Table II. Hepatitis (viral, acute)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/quality-payment-program-experience",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2017-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-04/2022%20QPP%20Experience%20Report%20Public%20Use%20Files%20Methodology.pdf"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "medicare",
-                "original medicare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Quality Payment Program - CCSQ",
                 "hasEmail": "mailto:qpp@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/7adb8b1b-b85c-4ed3-b314-064776e50180/data-viewer",
-            "description": "The Quality Payment Program (QPP) Experience dataset provides participation and performance information in the Merit-based Incentive Payment System (MIPS) during each performance year. They cover eligibility and participation, performance categories, and final score and payment adjustments. The dataset provides additional details at the TIN/NPI level on what was published in the previous performance year. You can sort the data by variables like clinician type, practice size, scores, and payment adjustments.",
-            "title": "Quality Payment Program Experience",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-04/2022%20QPP%20Experience%20Report%20Public%20Use%20Files%20Data%20Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Quality Payment Program (QPP) Experience dataset provides participation and performance information in the Merit-based Incentive Payment System (MIPS) during each performance year. They cover eligibility and participation, performance categories, and final score and payment adjustments. The dataset provides additional details at the TIN/NPI level on what was published in the previous performance year. You can sort the data by variables like clinician type, practice size, scores, and payment adjustments.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7adb8b1b-b85c-4ed3-b314-064776e50180/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7adb8b1b-b85c-4ed3-b314-064776e50180/data",
+                    "mediaType": "text/html",
                     "title": "Quality Payment Program Experience : 2022-01-01"
                 },
                 {
@@ -48380,56 +48361,48 @@
                     "title": "Quality Payment Program Experience : 2017-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-04/2022%20QPP%20Experience%20Report%20Public%20Use%20Files%20Data%20Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/7adb8b1b-b85c-4ed3-b314-064776e50180/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "medicare",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/quality-payment-program-experience",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-08",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-04/2022%20QPP%20Experience%20Report%20Public%20Use%20Files%20Methodology.pdf"
+            ],
+            "temporal": "2017-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Quality Payment Program Experience"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-04-08",
-            "temporal": "1950/2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "keyword": [
-                "american indian or alaska native",
-                "asian",
-                "black or african american",
-                "death rates",
-                "health us",
-                "heart disease",
-                "hispanic or latino",
-                "men",
-                "mortality",
-                "native hawaiian or other pacific islander",
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
-            "identifier": "https://data.cdc.gov/api/views/4892-xxjy",
             "description": "Data on death rates for diseases of heart in the United States, by age, sex, race, and Hispanic origin. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Mortality File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Death rates for heart disease, by sex, race, Hispanic origin, and age: United States from CDC WONDER",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48452,21 +48425,61 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4892-xxjy",
+            "issued": "2024-04-08",
+            "keyword": [
+                "american indian or alaska native",
+                "asian",
+                "black or african american",
+                "death rates",
+                "health us",
+                "heart disease",
+                "hispanic or latino",
+                "men",
+                "mortality",
+                "native hawaiian or other pacific islander",
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
+            "temporal": "1950/2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Death rates for heart disease, by sex, race, Hispanic origin, and age: United States from CDC WONDER"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2006-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) primarily<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions included age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2006 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Background information<br />\nincludes gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2006) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2006-nid13554",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2006-nid13554"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2006-nid13554",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -48507,66 +48520,30 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2006-0",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2006-nid13554",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) primarily<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions included age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2006 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Background information<br />\nincludes gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2006)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2006-nid13554",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2006) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2006-nid13554"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2006)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/2015-edition-market-readiness-hospitals-and-clinicians-data",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-04-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/2015-edition-market-readiness-hospitals-and-clinicians"
-            ],
-            "keyword": [
-                "certified",
-                "ehrs",
-                "electronic health records",
-                "health information technology",
-                "health it",
-                "market"
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
-            "identifier": "j7aeu9v0-eudg-eqb6-3cik-gyv36mrqd7e7",
+            "describedBy": "https://www.healthit.gov/data/datasets/2015-edition-market-readiness-hospitals-and-clinicians-data",
             "description": "This dataset provides the proportion of developers, by market share, that have certified 2015 edition health IT modules. Market share approximations are determined through an analysis of the certified health IT products reported by participants in the Medicare EHR Incentive Program from 2011 to 2016. Approximations use the most recently reported data for each unique clinician and hospital participant. It is important to understand how to interpret these approximations. Some clinicians and hospitals report certified software from more than one unique developer. The market share percentages in this dataset, therefore, include some double counting (the percentages will, if summed together, add up above 100 percent.) The approximations convey the percent of hospitals and clinicians who use a developer's technology, and are not to be interpreted in aggregate as the percent of all hospitals and clinicians who have access to 2015 edition certified technology.",
-            "title": "2015 Edition Market Readiness for Hospitals and Clinicians Data",
-            "programCode": [
-                "009:110"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48575,35 +48552,43 @@
                     "title": "2015-edition-market-readiness-hospitals-clinicians-data.csv"
                 }
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/2015-edition-market-readiness-hospitals-and-clinicians-data"
+            "identifier": "j7aeu9v0-eudg-eqb6-3cik-gyv36mrqd7e7",
+            "issued": "2023-10-03",
+            "keyword": [
+                "certified",
+                "ehrs",
+                "electronic health records",
+                "health information technology",
+                "health it",
+                "market"
+            ],
+            "landingPage": "https://www.healthit.gov/data/datasets/2015-edition-market-readiness-hospitals-and-clinicians-data",
+            "modified": "2019-04-01",
+            "programCode": [
+                "009:110"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "references": [
+                "https://www.healthit.gov/data/quickstats/2015-edition-market-readiness-hospitals-and-clinicians"
+            ],
+            "title": "2015 Edition Market Readiness for Hospitals and Clinicians Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/bzbt-2kdz",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-02-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-26",
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
-            "identifier": "be496f61-3e23-47aa-b442-2334a1fbe40a",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-19-2024-to-02-25-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48612,47 +48597,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-19-2024-to-02-25-2024"
                 }
             ],
+            "identifier": "be496f61-3e23-47aa-b442-2334a1fbe40a",
+            "issued": "2024-02-28",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/bzbt-2kdz",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-02-26",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-19-2024-to-02-25-2024"
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
-                "http://www.cdc.gov/nchs/data/databriefs/db162.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf"
-            ],
-            "keyword": [
-                "age",
-                "births",
-                "nchs",
-                "nonmarital",
-                "percent distribution"
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
-            "identifier": "https://data.cdc.gov/api/views/hzd8-r9mj",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes percent distribution of births to unmarried women by age group in the United States since 1970.\n\nMethods for collecting information on marital status changed over the reporting period and have been documented in:\n\n\u2022 Ventura SJ, Bachrach CA. Nonmarital childbearing in the United States, 1940\u201399. National vital statistics reports; vol 48 no 16. Hyattsville, Maryland: National Center for Health Statistics. 2000. Available from: http://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf.\n\u2022 National Center for Health Statistics. User guide to the 2013 natality public use file. Hyattsville, Maryland: National Center for Health Statistics. 2014. Available from: http://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm.",
-            "title": "NCHS - Percent Distribution of Births to Unmarried Women by Age Group: United States",
-            "isPartOf": "NCHS - Percent Distribution of Births to Unmarried Women by Age Group: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48675,55 +48649,62 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/hzd8-r9mj",
+            "isPartOf": "NCHS - Percent Distribution of Births to Unmarried Women by Age Group: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "age",
+                "births",
+                "nchs",
+                "nonmarital",
+                "percent distribution"
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
+                "http://www.cdc.gov/nchs/data/databriefs/db162.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf"
+            ],
+            "rights": "public",
+            "spatial": "United States",
+            "temporal": "1970/2015",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Percent Distribution of Births to Unmarried Women by Age Group: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicaid-spending-by-drug",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2022-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-13",
-            "references": [
-                "https://data.cms.gov/resources/medicaid-spending-by-drug-methodology"
-            ],
-            "keyword": [
-                "all other provider care types",
-                "drugs",
-                "medicaid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS Drug Spending - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/be64fce3-e835-4589-b46b-024198e524a6/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicaid-spending-by-drug-data-dictionary",
             "description": "The Medicaid by Drug dataset presents information on spending for covered outpatient drugs prescribed to beneficiaries enrolled in Medicaid by physicians and other healthcare professionals.\u00a0\n\n\u00a0\n\nThe dataset focuses on average spending per dosage unit and change in average spending per dosage unit over time. Units refer to the drug unit in the lowest dispensable amount. It also includes spending information for manufacturer(s) of the drugs as well as consumer-friendly information of drug uses and clinical indications.\n\n\u00a0\n\nDrug spending metrics for Medicaid represent the total amount reimbursed by both Medicaid and non-Medicaid entities to pharmacies for the drug. Medicaid drug spending contains both the Federal and State reimbursement and is inclusive of any applicable dispensing fees. In addition, this total is not reduced or affected by Medicaid rebates paid to the states.",
-            "title": "Medicaid Spending by Drug",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/be64fce3-e835-4589-b46b-024198e524a6/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/be64fce3-e835-4589-b46b-024198e524a6/data",
+                    "mediaType": "text/html",
                     "title": "Medicaid Spending by Drug : 2022-01-01"
                 },
                 {
@@ -48739,56 +48720,48 @@
                     "title": "Medicaid Spending by Drug : 2022-01-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicaid-spending-by-drug-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/be64fce3-e835-4589-b46b-024198e524a6/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "all other provider care types",
+                "drugs",
+                "medicaid"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicaid-spending-by-drug",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicaid-spending-by-drug-methodology"
+            ],
+            "temporal": "2022-01-01/2022-12-31",
             "theme": [
                 "Medicaid"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicaid Spending by Drug"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-01",
-            "temporal": "1950/2021",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "keyword": [
-                "american indian or alaska native",
-                "asian",
-                "black or african american",
-                "death rates",
-                "health us",
-                "hispanic or latino",
-                "men",
-                "mental health",
-                "native hawaiian or other pacific islander",
-                "suicide",
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
-            "identifier": "https://data.cdc.gov/api/views/p7se-k3ix",
             "description": "Data on death rates for suicide in the United States, by age, sex, race, and Hispanic origin. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Mortality File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Death rates for suicide, by sex, race, Hispanic origin, and age: United States from CDC WONDER",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48811,44 +48784,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/p7se-k3ix",
+            "issued": "2024-03-01",
+            "keyword": [
+                "american indian or alaska native",
+                "asian",
+                "black or african american",
+                "death rates",
+                "health us",
+                "hispanic or latino",
+                "men",
+                "mental health",
+                "native hawaiian or other pacific islander",
+                "suicide",
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
+            "temporal": "1950/2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Death rates for suicide, by sex, race, Hispanic origin, and age: United States from CDC WONDER"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "http://www.cdc.gov/STATESystem",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "global",
-                "gtss",
-                "gyts",
-                "osh",
-                "tobacco",
-                "youth"
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
-            "identifier": "https://data.cdc.gov/api/views/57qw-ifet",
+            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-You/57qw-ifet",
             "description": "1999-2018. The GYTS is a school-based survey that collects data on students aged 13\u201315 years using a standardized methodology for constructing the sample frame, selecting schools and classes, and processing data. The GYTS surveillance system is intended to enhance the capacity of countries to design, implement, and evaluate tobacco control and prevention programs. Funding for the GYTS has been provided by the Canadian Public Health Association, National Cancer Institute, United Nations Children Emergency Fund, and the World Health Organization\u2014Tobacco Free Initiative.",
-            "title": "Global Tobacco Surveillance System (GTSS) - Global Youth Tobacco Survey (GYTS)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48871,95 +48851,90 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-You/57qw-ifet",
+            "identifier": "https://data.cdc.gov/api/views/57qw-ifet",
+            "issued": "2025-01-31",
+            "keyword": [
+                "global",
+                "gtss",
+                "gyts",
+                "osh",
+                "tobacco",
+                "youth"
+            ],
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
             "theme": [
                 "Global Survey Data"
-            ]
+            ],
+            "title": "Global Tobacco Surveillance System (GTSS) - Global Youth Tobacco Survey (GYTS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/c2aj-88y2",
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
-            "identifier": "792f9cf5-a4c9-5d41-a267-14ff9962456b",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt version v2.10.16 (coreset-dev0)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/version.csv",
-                    "description": "CoreSEt version v2.10.16 (coreset-dev0)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt version v2.10.16 (coreset-dev0)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt version v2.10.16 (coreset-dev0)"
                 }
             ],
+            "identifier": "792f9cf5-a4c9-5d41-a267-14ff9962456b",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/c2aj-88y2",
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
+            "title": "CoreSEt version v2.10.16 (coreset-dev0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-21",
-            "temporal": "1989/2015",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-01",
-            "keyword": [
-                "american indian or alaska native",
-                "asian or pacific islander",
-                "black or african american",
-                "child and adolescent",
-                "deaths",
-                "health us",
-                "hispanic or latino",
-                "infant mortality",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pjb2-jvdr",
             "description": "This topic is no longer available in the NCHS Data Query System (DQS). Search, visualize, and download other estimates from over 120 health topics with DQS, available from: https://www.cdc.gov/nchs/dataquery/index.htm.\nData on on average annual infant mortality rates in the United States and U.S. dependent areas, by race and Hispanic origin of mother, state, and territory. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Linked Birth/Infant Death Data Set.",
-            "title": "DQS Infant mortality rates, by race and Hispanic origin of mother, state, and territory: United States and U.S. dependent areas (Archived)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48982,69 +48957,107 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/pjb2-jvdr",
+            "issued": "2024-02-21",
+            "keyword": [
+                "american indian or alaska native",
+                "asian or pacific islander",
+                "black or african american",
+                "child and adolescent",
+                "deaths",
+                "health us",
+                "hispanic or latino",
+                "infant mortality",
+                "state",
+                "white"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-11-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "1989/2015",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Infant mortality rates, by race and Hispanic origin of mother, state, and territory: United States and U.S. dependent areas (Archived)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/c3dm-3fy7",
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
-            "identifier": "cf603cd1-db1f-533f-acad-d03954787bab",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_measureSearchInfo",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measureSearchInfo.csv",
-                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measureSearchInfo.csv",
+                    "mediaType": "text/csv",
                     "title": "measureSearchInfo csv file"
                 }
             ],
+            "identifier": "cf603cd1-db1f-533f-acad-d03954787bab",
+            "issued": "2022-08-31",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/c3dm-3fy7",
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
+            "title": "devAuto_measureSearchInfo"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2006",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2006) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2006-nid13546",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2006-nid13546"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2006-nid13546",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -49057,58 +49070,30 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2006",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2006-nid13546",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2006)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2006-nid13546",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2006) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2006-nid13546"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2006)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/c48b-9hs6",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-03-16",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-14",
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
-            "identifier": "aab40af5-2e31-478c-be9b-9475f919e9c7",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-03-07 to 2022-03-13",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49116,38 +49101,36 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "aab40af5-2e31-478c-be9b-9475f919e9c7",
+            "issued": "2022-03-16",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/c48b-9hs6",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-03-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-03-07 to 2022-03-13"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.acf.hhs.gov/programs/ana/",
             "bureauCode": [
                 "009:70"
             ],
-            "issued": "2012-08-10",
-            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "administrative",
-                "social and economic  development"
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
-            "identifier": "73c33ee9-43a3-407a-8df9-186a43671599",
+            "dataQuality": true,
             "description": "<p>The 2010 Congressional Report provides results for 70 ANA projects that ended in 2010. The report includes a brief summary of each project visited and an analysis of how ANA funding has impacted Native American communities.</p>",
-            "title": "Administration for Native Americans (ANA) Projects Report",
-            "programCode": [
-                "009:095"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49156,36 +49139,37 @@
                     "title": "HTML"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "73c33ee9-43a3-407a-8df9-186a43671599",
+            "issued": "2012-08-10",
+            "keyword": [
+                "administrative",
+                "social and economic  development"
+            ],
+            "landingPage": "http://www.acf.hhs.gov/programs/ana/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:095"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families"
+            },
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "title": "Administration for Native Americans (ANA) Projects Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-06-04",
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
-            "identifier": "a0710f78-0585-45c8-9320-7d252b291390",
             "description": "This application provides information for active, inactive, and pre-registered firms. Query options are by FEI, Applicant Name, Establishment Name, Other Names, Establishment Type, Establishment Status, City, State, Zip Code, Country and Reporting Official First Name or Last Name.",
-            "title": "Blood Establishment Registration Database",
-            "programCode": [
-                "009:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49193,105 +49177,84 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "a0710f78-0585-45c8-9320-7d252b291390",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cber"
+            ],
+            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-06-04",
+            "programCode": [
+                "009:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Blood Establishment Registration Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/c5te-qbma",
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
-            "identifier": "53426d8c-82b5-5dec-b44b-0f935b4603e5",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_files_stateSnapshot",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_stateSnapshot.csv",
-                    "description": "{\"dataset\": \"files_stateSnapshot\", \"stage\": \"devAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_stateSnapshot\", \"stage\": \"devAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_stateSnapshot.csv",
+                    "mediaType": "text/csv",
                     "title": "files_stateSnapshot csv file"
                 }
             ],
+            "identifier": "53426d8c-82b5-5dec-b44b-0f935b4603e5",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/c5te-qbma",
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
+            "title": "devAuto_files_stateSnapshot"
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
-            "identifier": "https://data.cdc.gov/api/views/u76f-m89e",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2003/u76f-m89e",
             "description": "2003. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2003",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49314,40 +49277,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2003/u76f-m89e",
+            "identifier": "https://data.cdc.gov/api/views/u76f-m89e",
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
+            "title": "CDC PRAMStat Data for 2003"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -49370,53 +49353,81 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y8pa-p62q",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/y8pa-p62q",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 7 - Kansas City"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/geo/",
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
                 "fn": "Barret, Tanya",
                 "hasEmail": "mailto:barrett@ncbi.nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "03c4f32c-8437-4eb5-af9f-bfb70ffaec73",
+            "dataQuality": true,
             "description": "<p>Gene Expression Omnibus is a public functional genomics data repository supporting MIAME-compliant submissions of array- and sequence-based data. Tools are provided to help users query and download experiments and curated gene expression profiles.</p>",
-            "title": "Gene Expression Omnibus (GEO)",
+            "identifier": "03c4f32c-8437-4eb5-af9f-bfb70ffaec73",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/geo/",
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
+            "title": "Gene Expression Omnibus (GEO)"
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
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "486663d1-b2cd-4ccc-b221-6f9a155675e9",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "food",
                 "health",
@@ -49426,72 +49437,31 @@
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
-            "identifier": "486663d1-b2cd-4ccc-b221-6f9a155675e9",
-            "description": "Contains data for FDA peanut product recalls since January 2009.",
-            "title": "FDA Peanut Product Recalls Widget",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Peanut Product Recalls Widget"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2017-12-04",
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
-            "identifier": "https://data.cdc.gov/api/views/dxpw-cm5u",
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-City-level-Data-GIS-Friendly-Format-201/dxpw-cm5u",
             "description": "2017, 2016. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level. There are 7 measures (all teeth lost, dental visits, mammograms, Pap tests, colorectal cancer screening, core preventive services among older adults, and sleep less than 7 hours) in this 2019 release from the 2016 BRFSS that were the same as the 2018 release.",
-            "title": "500 Cities: City-level Data (GIS Friendly Format), 2019 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49514,41 +49484,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-City-level-Data-GIS-Friendly-Format-201/dxpw-cm5u",
+            "identifier": "https://data.cdc.gov/api/views/dxpw-cm5u",
+            "issued": "2017-12-04",
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
+            "title": "500 Cities: City-level Data (GIS Friendly Format), 2019 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/c7xe-en73",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2014-11-07",
-            "temporal": "2016-01-01T00:00:00+00:00/2017-01-01T00:00:00+00:00",
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
-            "identifier": "7656fc17-f1b4-566b-9a2d-c4a4f2ac7ae1",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2016",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49557,42 +49540,42 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "7656fc17-f1b4-566b-9a2d-c4a4f2ac7ae1",
+            "issued": "2014-11-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/c7xe-en73",
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
+            "temporal": "2016-01-01T00:00:00+00:00/2017-01-01T00:00:00+00:00",
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/rands/telemedicine.htm",
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
-            "identifier": "https://data.cdc.gov/api/views/8xy9-ubqz",
             "description": "The Research and Development Survey (RANDS) is a platform designed for conducting survey question evaluation and statistical research. RANDS is an ongoing series of surveys from probability-sampled commercial survey panels used for methodological research at the National Center for Health Statistics (NCHS). RANDS estimates are generated using an experimental approach that differs from the survey design approaches generally used by NCHS, including possible biases from different response patterns and sampling frames as well as increased variability from lower sample sizes. Use of the RANDS platform allows NCHS to produce more timely data than would be possible using traditional data collection methods. RANDS is not designed to replace NCHS\u2019 higher quality, core data collections. Below are experimental estimates of telemedicine access and use for three rounds of RANDS during COVID-19. Data collection for the three rounds of RANDS during COVID-19 occurred between June 9, 2020 and July 6, 2020, August 3, 2020 and August 20, 2020, and May 17, 2021 and June 30, 2021. Information needed to interpret these estimates can be found in the Technical Notes. RANDS during COVID-19 included questions about whether providers offered telemedicine (including video and telephone appointments) in the last 2 months\u2014both during and before the pandemic\u2014and about the use of telemedicine in the last 2 months during the pandemic. As a result of the coronavirus pandemic, many local and state governments discouraged people from leaving their homes for nonessential reasons. Although health care is considered an essential activity, telemedicine offers an opportunity for care without the potential or perceived risks of leaving the home. The National Health Interview Survey, conducted by NCHS, added telemedicine questions to its sample adult questionnaire in July 2020.  The Household Pulse Survey (https://www.cdc.gov/nchs/covid19/pulse/telemedicine-use.htm), an online survey conducted in response to the COVID-19 pandemic by the Census Bureau in partnership with other federal agencies including NCHS, also reports estimates of telemedicine use during the pandemic (beginning in Phase 3.1, which started on April 14, 2021). The Household Pulse Survey reports telemedicine use in the last 4 weeks among adults and among households with at least one child under age 18 years. The experimental estimates on this page are derived from RANDS during COVID-19 and show the percentage of U.S. adults who have a usual place of care and a provider that offered telemedicine in the past 2 months, who used telemedicine in the past 2 months, or who have a usual place of care and a provider that offered telemedicine prior to the coronavirus pandemic. Technical Notes: https://www.cdc.gov/nchs/covid19/rands/telemedicine.htm#limitations",
-            "title": "Access and Use of Telemedicine During COVID-19",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49615,92 +49598,91 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/8xy9-ubqz",
+            "issued": "2020-09-14",
+            "keyword": [
+                "covid-19",
+                "rands"
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
+            "title": "Access and Use of Telemedicine During COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/c8di-4x22",
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
-            "identifier": "3f3dd079-167e-58ac-ac1b-dbbed02ae596",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard state v2.11.16 (dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/state.csv",
-                    "description": "Scorecard state v2.11.16 (dev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard state v2.11.16 (dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/state.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard state v2.11.16 (dev)"
                 }
             ],
+            "identifier": "3f3dd079-167e-58ac-ac1b-dbbed02ae596",
+            "issued": "2023-03-28",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/c8di-4x22",
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
+            "title": "Scorecard state v2.11.16 (dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://chpl.healthit.gov/#/resources/chpl_api",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "references": [
-                "https://chpl.healthit.gov/"
-            ],
-            "keyword": [
-                "na"
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
-            "identifier": "hl1o4xum-glh3-5j9f-ral7-kkm8hprfl53q",
+            "describedBy": "https://chpl.healthit.gov/#/resources/chpl_api",
             "description": "The Certified Health IT Product List (CHPL) is a comprehensive and authoritative listing of all certified Health Information Technology which has been successfully tested and certified by the ONC Health IT Certification program. All products listed on the CHPL have been tested by an ONC-Accredited Testing Laboratory (ONC-ATL) and certified by an ONC-Authorized Certification Body (ONC-ACB) to meet criteria adopted by the Secretary of the Department of Health and Human Services (HHS). This is a fully queryable REST API with JSON and XML output.",
-            "title": "Certified Health IT Product List (CHPL) Open API",
-            "programCode": [
-                "009:110"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49709,36 +49691,37 @@
                     "title": "CHPL Open API"
                 }
             ],
-            "describedBy": "https://chpl.healthit.gov/#/resources/chpl_api"
+            "identifier": "hl1o4xum-glh3-5j9f-ral7-kkm8hprfl53q",
+            "issued": "2023-10-03",
+            "keyword": [
+                "na"
+            ],
+            "landingPage": "https://chpl.healthit.gov/#/resources/chpl_api",
+            "modified": "2023-10-03",
+            "programCode": [
+                "009:110"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "references": [
+                "https://chpl.healthit.gov/"
+            ],
+            "title": "Certified Health IT Product List (CHPL) Open API"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -49761,52 +49744,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xsu4-4sk9",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xsu4-4sk9",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014,  Region 9 - San Francisco"
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
-            "temporal": "1988/2019",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-29",
-            "keyword": [
-                "adult",
-                "african americans",
-                "age",
-                "asian continental ancestry group",
-                "chronic conditions",
-                "continental population groups",
-                "european continental ancestry group",
-                "health risk factors",
-                "health us",
-                "hispanic americans",
-                "obesity",
-                "overweight",
-                "poverty",
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
-            "identifier": "https://data.cdc.gov/api/views/3nzu-udr9",
             "description": "Data on normal weight, overweight, and obesity among adults aged 20 and over by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health and Nutrition Examination Survey. For more information on the National Health and Nutrition Examination Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Normal weight, overweight, and obesity among adults aged 20 and over, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49829,41 +49800,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3nzu-udr9",
+            "issued": "2022-04-28",
+            "keyword": [
+                "adult",
+                "african americans",
+                "age",
+                "asian continental ancestry group",
+                "chronic conditions",
+                "continental population groups",
+                "european continental ancestry group",
+                "health risk factors",
+                "health us",
+                "hispanic americans",
+                "obesity",
+                "overweight",
+                "poverty",
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "1988/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Normal weight, overweight, and obesity among adults aged 20 and over, by selected characteristics: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-births-0",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-08-03",
-            "temporal": "1995-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "natality births population health state county infant race hispanic age sex year birth weight gestat",
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
-            "identifier": "fb7cc429-69d2-4424-b287-68855af600ff",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/natality.html",
             "description": "<p>The Births (Natality) online databases in CDC WONDER report birth rates, fertility rates and counts of live births occurring within the United States to U.S. residents and non-residents. Counts can be obtained by state, county, child's gender and weight, mother's race, mother's age, mother's education, gestation period, prenatal care, birth plurality, and mother's medical and tobacco use risk factors. The data are derived from birth certificates. Data are available since 1995. The data are produced by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Births",
-            "programCode": [
-                "009:015"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49872,99 +49856,88 @@
                     "title": "Text "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/natality.html",
-            "dataQuality": true,
+            "identifier": "fb7cc429-69d2-4424-b287-68855af600ff",
+            "issued": "2012-08-03",
+            "keyword": [
+                "natality births population health state county infant race hispanic age sex year birth weight gestat",
+                "population statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-births-0",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:015"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1995-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
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
-            "landingPage": "https://healthdata.gov/d/c9tb-dwqg",
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
-            "identifier": "e9c931e7-55b5-570c-bdee-aa0b5fe87e1f",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard filters v2.11.18 (etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/filters.csv",
-                    "description": "Scorecard filters v2.11.18 (etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard filters v2.11.18 (etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard filters v2.11.18 (etl-test)"
                 }
             ],
+            "identifier": "e9c931e7-55b5-570c-bdee-aa0b5fe87e1f",
+            "issued": "2023-04-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/c9tb-dwqg",
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
+            "title": "Scorecard filters v2.11.18 (etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-26",
-            "temporal": "2005/2018",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
-            "keyword": [
-                "accidental falls",
-                "accidents",
-                "children and adolescents",
-                "emergency department visits",
-                "health care use",
-                "health us",
-                "injury",
-                "men",
-                "older persons",
-                "traffic",
-                "women",
-                "wounds and injuries"
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
-            "identifier": "https://data.cdc.gov/api/views/qdzf-zqgy",
             "description": "Data on initial injury-related visits to hospital emergency departments in the United States, by sex, age, and intent and mechanism of injury. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Hospital Ambulatory Medical Care Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Initial injury-related visits to hospital emergency departments, by sex, age, and intent and mechanism of injury: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49987,48 +49960,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qdzf-zqgy",
+            "issued": "2024-02-26",
+            "keyword": [
+                "accidental falls",
+                "accidents",
+                "children and adolescents",
+                "emergency department visits",
+                "health care use",
+                "health us",
+                "injury",
+                "men",
+                "older persons",
+                "traffic",
+                "women",
+                "wounds and injuries"
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2005/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Initial injury-related visits to hospital emergency departments, by sex, age, and intent and mechanism of injury: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vxsn-2csw",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "hepatitis",
-                "hepatitis (viral acute)",
-                "hepatitis (viral acute) type a",
-                "hepatitis (viral acute) type b",
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
-            "identifier": "https://data.cdc.gov/api/views/vxsn-2csw",
             "description": "NNDSS - Table II. Hepatitis (viral, acute) A & B - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Hepatitis (viral, acute) A & B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50051,51 +50026,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vxsn-2csw",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "hepatitis",
+                "hepatitis (viral acute)",
+                "hepatitis (viral acute) type a",
+                "hepatitis (viral acute) type b",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vxsn-2csw",
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
+            "title": "NNDSS - Table II. Hepatitis (viral, acute) A & B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-04",
-            "temporal": "1999/2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "keyword": [
-                "american indian or alaska native",
-                "asian",
-                "black or african american",
-                "cancer",
-                "death rates",
-                "health us",
-                "hispanic or latino",
-                "men",
-                "mortality",
-                "native hawaiian or other pacific islander",
-                "neoplasms",
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
-            "identifier": "https://data.cdc.gov/api/views/4giy-47wy",
             "description": "Data on death rates for neoplasms in the United States, by age, sex, race, and Hispanic origin. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Mortality File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Death rates for malignant neoplasms, by sex, race, Hispanic origin, and age: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50118,46 +50090,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4giy-47wy",
+            "issued": "2024-09-04",
+            "keyword": [
+                "american indian or alaska native",
+                "asian",
+                "black or african american",
+                "cancer",
+                "death rates",
+                "health us",
+                "hispanic or latino",
+                "men",
+                "mortality",
+                "native hawaiian or other pacific islander",
+                "neoplasms",
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
+            "temporal": "1999/2022",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Death rates for malignant neoplasms, by sex, race, Hispanic origin, and age: United States"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -50180,90 +50157,87 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Invasive Pneumococcal Diseases, Age <5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.acf.hhs.gov/ofa/data/tanf-final-rule-pages-17769-17818",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-06-18",
-            "temporal": "1996-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-29",
-            "keyword": [
-                "children's health",
-                "temporary assistance to needy families  cash assistance  welfare policy"
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
-            "identifier": "20287f1e-d621-41ee-928f-284caeb0b786",
+            "dataQuality": false,
             "description": "<p>Single source providing information on Temporary Assistance for Needy Families (TANF) program rules among States and across years (currently 1996-2010), including longitudinal tables with state TANF polices for selected years.</p>",
-            "title": "TANF Rules Data Base",
-            "programCode": [
-                "009:102"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.acf.hhs.gov/ofa/data/tanf-final-rule-pages-17769-17818",
-                    "description": "[Federal Register: April 12, 1999 (Volume 64, Number 69)]\n[Rules and Regulations]\n[Page 17769-17818]\nFrom the Federal Register Online via GPO Access [wais.access.gpo.gov]\n[DOCID:fr12ap99-24]\n\n[[pp. 17769-17818]] Temporary Assistance for Needy Families Program (TANF)\n",
                     "@type": "dcat:Distribution",
+                    "description": "[Federal Register: April 12, 1999 (Volume 64, Number 69)]\n[Rules and Regulations]\n[Page 17769-17818]\nFrom the Federal Register Online via GPO Access [wais.access.gpo.gov]\n[DOCID:fr12ap99-24]\n\n[[pp. 17769-17818]] Temporary Assistance for Needy Families Program (TANF)\n",
+                    "downloadURL": "https://www.acf.hhs.gov/ofa/data/tanf-final-rule-pages-17769-17818",
+                    "mediaType": "text/html",
                     "title": "TANF Final Rule \u2013 Pages 17769 - 17818"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "20287f1e-d621-41ee-928f-284caeb0b786",
+            "issued": "2013-06-18",
+            "keyword": [
+                "children's health",
+                "temporary assistance to needy families  cash assistance  welfare policy"
+            ],
+            "landingPage": "https://www.acf.hhs.gov/ofa/data/tanf-final-rule-pages-17769-17818",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2024-10-29",
+            "programCode": [
+                "009:102"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "temporal": "1996-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
+            "title": "TANF Rules Data Base"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gxj9-t96f",
+            "accrualPeriodicity": "Archived",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-11-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13/2022-08-10",
-            "modified": "2022-10-20",
-            "references": [
-                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
-            ],
-            "keyword": [
-                "administration",
-                "cases",
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
-            "identifier": "https://data.cdc.gov/api/views/gxj9-t96f",
             "description": "</p><p style=\"margin:0in;vertical-align:baseline;\"><strong><em><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>After October 13, 2022, this dataset will no longer be updated as the related CDC COVID Data Tracker site was retired on October 13, 2022.</span></em></strong><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span></p>This dataset contains historical trends in vaccinations and cases by age group, at the US national level. Data is stratified by at least one dose and fully vaccinated. Data also represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.",
-            "title": "Archive: COVID-19 Vaccination and Case Trends by Age Group, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50286,40 +50260,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/gxj9-t96f",
+            "issued": "2021-11-17",
+            "keyword": [
+                "administration",
+                "cases",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "report date",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/gxj9-t96f",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Archived",
+            "modified": "2022-10-20",
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
+            "temporal": "2020-12-13/2022-08-10",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Archive: COVID-19 Vaccination and Case Trends by Age Group, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/cdnr-9f3u",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-05-02",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-01",
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
-            "identifier": "e56d9a47-fe57-42c0-b37d-4ab244fd08b1",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-24-to-2023-04-30",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50328,36 +50313,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-24-to-2023-04-30"
                 }
             ],
+            "identifier": "e56d9a47-fe57-42c0-b37d-4ab244fd08b1",
+            "issued": "2023-05-02",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/cdnr-9f3u",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-05-01",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-24-to-2023-04-30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/cefh-9ep2",
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
-            "identifier": "cfbf62b6-ab10-46d1-9284-b08475964470",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-23-to-2023-01-29",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50366,20 +50351,46 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-23-to-2023-01-29"
                 }
             ],
+            "identifier": "cfbf62b6-ab10-46d1-9284-b08475964470",
+            "issued": "2023-02-09",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/cefh-9ep2",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-23-to-2023-01-29"
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
@@ -50390,106 +50401,82 @@
                 "telemedicine",
                 "vaccination"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/66km-38zv",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-24",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
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
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-            "landingPage": "https://healthdata.gov/d/cgyd-rri7",
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
-            "identifier": "e7d5089e-647c-4aa7-8c7b-f98dd8ea3852",
             "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Month",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/BenefitPackage-montly.csv",
-                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/BenefitPackage-montly.csv",
+                    "mediaType": "text/csv",
                     "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Month"
                 }
             ],
+            "identifier": "e7d5089e-647c-4aa7-8c7b-f98dd8ea3852",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "program enrollment",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/cgyd-rri7",
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
+            "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Month"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hv7b-3sw8",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hv7b-3sw8",
             "description": "Estimates are for pregnant persons who are up-to-date with COVID-19 vaccines, overall and by race and ethnicity based on data from the Vaccine Safety Datalink*.",
-            "title": "Data: COVID-19 vaccination among pregnant people aged 18-49 years overall, by race and ethnicity, and date reported to CDC - Vaccine Safety Datalink,* United States",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50512,40 +50499,35 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hv7b-3sw8",
+            "issued": "2023-06-22",
+            "landingPage": "https://data.cdc.gov/d/hv7b-3sw8",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-02",
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
+            "title": "Data: COVID-19 vaccination among pregnant people aged 18-49 years overall, by race and ethnicity, and date reported to CDC - Vaccine Safety Datalink,* United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/hmd/indexcat/index.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "dataset",
-                "history of medicine",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/axmu-a5jw",
             "description": "IndexCat provides access to the digitized version of the printed Index-Catalogue of the Library of the Surgeon General's Office; eTK for medieval Latin texts; and eVK2 for medieval English texts; along with links to other selected NLM resources.",
-            "title": "IndexCat",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50560,39 +50542,40 @@
                     "title": "Download IndexCat Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/axmu-a5jw",
+            "issued": "2016-08-04",
+            "keyword": [
+                "dataset",
+                "history of medicine",
+                "library services"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/hmd/indexcat/index.html",
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
                 "Images"
-            ]
+            ],
+            "title": "IndexCat"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -50615,41 +50598,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/95m5-agj4",
+            "issued": "2021-06-23",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "landingPage": "https://data.cdc.gov/d/95m5-agj4",
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
+            "title": "Active Bacterial Core surveillance (ABCs) Group B Streptococcus"
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
-            "identifier": "https://data.cdc.gov/api/views/vugp-mqip",
             "description": "Monthly Cumulative Percent of Persons Who Received 1+ updated 2023-24 COVID-19 Vaccination Doses by Age Group and Jurisdiction\n\n\u2022 Estimated Number of COVID-19 vaccinations among children 6 months\u201317 years and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group.\n\n \u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19. (https://www.cdc.gov/coronavirus/2019-ncov/vaccines/stay-up-to-date.html)\n\u2003",
-            "title": "Monthly Cumulative Number and Percent of Persons Who Received 1+ updated 2023-24 COVID-19 Vaccination Doses by Age Group and Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50672,44 +50654,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "identifier": "https://data.cdc.gov/api/views/vugp-mqip",
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
-            "landingPage": "http://www.fda.gov/ICECI/EnforcementActions/WarningLetters/2013/default.htm",
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
-            "identifier": "8ab03039-617f-469d-bf37-b4f844372945",
             "description": "An index of FDA warning letters issued to companies operating in the United States.",
-            "title": "Warning Letters",
-            "programCode": [
-                "009:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50717,41 +50701,37 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "8ab03039-617f-469d-bf37-b4f844372945",
+            "issued": "2021-02-25",
+            "keyword": [
+                "ora",
+                "regulations"
+            ],
+            "landingPage": "http://www.fda.gov/ICECI/EnforcementActions/WarningLetters/2013/default.htm",
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
+            "title": "Warning Letters"
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
-            "temporal": "2023-24 & 2024-25",
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
-            "identifier": "https://data.cdc.gov/api/views/pvk6-8bzd",
             "description": "\u2022 Weekly COVID-19 Vaccination Coverage, Pregnant Women 18-49 Years Old by Race and Ethnicity \n\n\u2022 Weekly COVID-19 vaccination coverage estimates for pregnant women ages 18\u201349 years are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD) ((https://www.cdc.gov/vaccine-safety-systems/vsd/), a collaboration between CDC\u2019s Immunization Safety Office and multiple integrated health care organizations.",
-            "title": "Weekly COVID-19 Vaccination Coverage Among Pregnant Women 18-49 Years, by Race and Ethnicity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50774,45 +50754,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/pvk6-8bzd",
+            "issued": "2024-10-02",
+            "keyword": [
+                "covid-19 vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
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
+            "temporal": "2023-24 & 2024-25",
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly COVID-19 Vaccination Coverage Among Pregnant Women 18-49 Years, by Race and Ethnicity"
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
-            "identifier": "https://data.cdc.gov/api/views/ker6-gs6z",
             "description": "\u2022 Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months-17 Years Who are Up to date with the COVID-19 Vaccines by Season. \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey\u2013Child COVID Module (NIS\u2013CCM). The NIS\u2013CCM was discontinued at the end of 2023 and questions regarding COVID-19 vaccination status and intent were added to the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html).",
-            "title": "Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months -17 Years Who are Up to date with the COVID-19 Vaccines by Season, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50835,27 +50818,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/ker6-gs6z",
+            "issued": "2025-01-29",
+            "keyword": [
+                "covid-19 vaccination",
+                "nis-ccm"
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
+            "title": "Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months -17 Years Who are Up to date with the COVID-19 Vaccines by Season, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:births@cdc.gov"
+            },
+            "describedBy": "All registered infant deaths linked with corresponding birth certificates occurring to residents of the United States",
+            "description": "This dataset includes all infant deaths that were linked to their corresponding birth certificate and includes all items released in the public-use file. Additional information in this file includes state and county of residence and exact dates of birth and death (which includes day of month, month, and year).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This dataset includes all infant deaths that were linked to their corresponding birth certificate and includes all items released in the public-use file. Additional information in this file includes state and county of residence and exact dates of birth and death (which includes day of month, month, and year).",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "NCHS - All-County Linked Births/Infant Deaths File with Exact Dates of Birth and Death"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/wis9-vyx6",
+            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "issued": "2022-12-22",
-            "@type": "dcat:Dataset",
-            "temporal": "2016/2020",
-            "modified": "2023-04-14",
             "keyword": [
                 "births",
                 "county",
@@ -50866,69 +50879,37 @@
                 "research-data-center",
                 "united states"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:births@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-14",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/wis9-vyx6",
-            "description": "This dataset includes all infant deaths that were linked to their corresponding birth certificate and includes all items released in the public-use file. Additional information in this file includes state and county of residence and exact dates of birth and death (which includes day of month, month, and year).",
-            "title": "NCHS - All-County Linked Births/Infant Deaths File with Exact Dates of Birth and Death",
-            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "This dataset includes all infant deaths that were linked to their corresponding birth certificate and includes all items released in the public-use file. Additional information in this file includes state and county of residence and exact dates of birth and death (which includes day of month, month, and year).",
-                    "@type": "dcat:Distribution",
-                    "title": "NCHS - All-County Linked Births/Infant Deaths File with Exact Dates of Birth and Death"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "50 states and District of Columbia, all counties with a population of 100,000 or greater",
-            "describedBy": "All registered infant deaths linked with corresponding birth certificates occurring to residents of the United States",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2016/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - All-County Linked Births/Infant Deaths File with Exact Dates of Birth and Death"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/cmfu-57yz",
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
-            "identifier": "fade0e37-50d8-418b-92a0-46828980a384",
             "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2025 Individual Dental",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50936,32 +50917,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "fade0e37-50d8-418b-92a0-46828980a384",
+            "issued": "2024-12-10",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2025",
+                "qhp landscape",
+                "sadp"
+            ],
+            "landingPage": "https://healthdata.gov/d/cmfu-57yz",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2025 Individual Dental"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kw6u-z8u2",
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
-            "identifier": "https://data.cdc.gov/api/views/kw6u-z8u2",
             "description": "This dataset contains all state and territorial vaccine mandates that were issued from July 26, 2021 to ____, regardless of whether the law has been superseded by a subsequent law, postponed by subsequent law, or otherwise modified. State and territorial laws are collected from publicly available government websites and cataloged and coded using HHS Protect by one coder with one or more additional coders conducting quality assurance. \nData were collected to determine when certain groups were subject to vaccine mandates. Data can be used to determine when states announced and required different groups to be vaccinated. \nThese data are derived from publicly available state and territorial laws and official policy documents found by CDC\u2019s COVID-19 Mitigation Policy Analysis Unit, and CDC\u2019s Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from July 26, 2021 through _____. These data will be updated as new laws are collected. Any orders not available through publicly accessible websites are not included in this dataset. Recommendations not included in a law are not included in these data. Effective and expiration dates were coded using only the date provided in the law. These data do not necessarily represent the official position of the Centers for Disease Control and Prevention.",
-            "title": "State-Level Vaccine Mandates - All",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50984,20 +50971,60 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kw6u-z8u2",
+            "issued": "2022-03-23",
+            "landingPage": "https://data.cdc.gov/d/kw6u-z8u2",
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
+            "title": "State-Level Vaccine Mandates - All"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ephtracking.cdc.gov/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Craig Kassinger",
+                "hasEmail": "mailto:cak8@cdc.gov"
+            },
+            "description": "The Environmental Protection Agency (EPA) provides air pollution data about ozone and particulate matter (PM2.5) to CDC for the Tracking Network. The EPA maintains a database called the Air Quality System (AQS) which contains data from approximately 4,000 monitoring stations around the country, mainly in urban areas. Data from the AQS is considered the \"gold standard\" for determining outdoor air pollution. However, AQS data are limited because the monitoring stations are usually in urban areas or cities and because they only take air samples for some air pollutants every three days or during times of the year when air pollution is very high. CDC and EPA have worked together to develop a statistical model (Downscaler) to make modeled predictions available for environmental public health tracking purposes in areas of the country that do not have monitors and to fill in the time gaps when monitors may not be recording data. This data does not include \"Percent of population in counties exceeding NAAQS (vs. population in counties that either meet the standard or do not monitor PM2.5)\". Please visit the Tracking homepage for this information.View additional information for indicator definitions and documentation by selecting Content Area \"Air Quality\" and the respective indicator at the following website: http://ephtracking.cdc.gov/showIndicatorsData.action",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/cjae-szjv",
             "issued": "2015-08-13",
-            "@type": "dcat:Dataset",
-            "modified": "2018-06-05",
             "keyword": [
                 "air pollution",
                 "air quality",
@@ -51029,130 +51056,83 @@
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/cjae-szjv",
-            "description": "The Environmental Protection Agency (EPA) provides air pollution data about ozone and particulate matter (PM2.5) to CDC for the Tracking Network. The EPA maintains a database called the Air Quality System (AQS) which contains data from approximately 4,000 monitoring stations around the country, mainly in urban areas. Data from the AQS is considered the \"gold standard\" for determining outdoor air pollution. However, AQS data are limited because the monitoring stations are usually in urban areas or cities and because they only take air samples for some air pollutants every three days or during times of the year when air pollution is very high. CDC and EPA have worked together to develop a statistical model (Downscaler) to make modeled predictions available for environmental public health tracking purposes in areas of the country that do not have monitors and to fill in the time gaps when monitors may not be recording data. This data does not include \"Percent of population in counties exceeding NAAQS (vs. population in counties that either meet the standard or do not monitor PM2.5)\". Please visit the Tracking homepage for this information.View additional information for indicator definitions and documentation by selecting Content Area \"Air Quality\" and the respective indicator at the following website: http://ephtracking.cdc.gov/showIndicatorsData.action",
-            "title": "Air Quality Measures on the National Environmental Health Tracking Network",
+            "landingPage": "http://ephtracking.cdc.gov/",
+            "language": [
+                "English"
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-            "landingPage": "https://healthdata.gov/d/cqip-xq88",
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
-            "identifier": "ce40c2ae-06e3-593f-b055-41d39df5edcb",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard state v2.11.9 (prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/state.csv",
-                    "description": "Scorecard state v2.11.9 (prod)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard state v2.11.9 (prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/state.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard state v2.11.9 (prod)"
                 }
             ],
+            "identifier": "ce40c2ae-06e3-593f-b055-41d39df5edcb",
+            "issued": "2023-07-22",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/cqip-xq88",
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
+            "title": "Scorecard state v2.11.9 (prod)"
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
-            "modified": "2023-07-25",
-            "references": [
-                "https://www.hcup-us.ahrq.gov/reports/trendtables/HCUPSummaryTrendTables_Methods.xlsx"
-            ],
-            "keyword": [
-                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
-                "hcup",
-                "healthcare cost and utilization"
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
-            "identifier": "https://healthdata.gov/api/views/cqqt-nv72",
+            "describedBy": "https://www.hcup-us.ahrq.gov/reports/trendtables/summarytrendtables.jsp",
             "description": "The HCUP Summary Trend Tables include monthly information on hospital utilization derived from the HCUP State Inpatient Databases (SID) and HCUP State Emergency Department Databases (SEDD). Information on emergency department (ED) utilization is dependent on availability of HCUP data; not all HCUP Partners participate in the SEDD.\n\nThe HCUP Summary Trend Tables include downloadable Microsoft\u00ae Excel tables with information on the following topics:\n\n<li>Overview of monthly trends in inpatient and emergency department utilization\n<li>All inpatient encounter types\n<li>Inpatient stays by priority conditions\n-COVID-19\n-Influenza\n-Other acute or viral respiratory infection\n<li>Inpatient encounter type\n-Normal newborns\n-Deliveries\n-Non-elective inpatient stays, admitted through the ED\n-Non-elective inpatient stays, not admitted through the ED\n-Elective inpatient stays\n<li>Inpatient service line\n-Maternal and neonatal conditions\n-Mental health and substance use disorders\n-Injuries\n-Surgeries\n-Other medical conditions\n<li>Emergency department treat-and-release visits\n<li>Emergency department treat-and-release visits by priority conditions\n-COVID-19\n-Influenza\n-Other acute or viral respiratory infection\n<li>Description of the data source, methodology, and clinical criteria",
-            "title": "Healthcare Cost and Utilization Project (HCUP) Summary Trends Tables",
-            "programCode": [
-                "009:074"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51161,47 +51141,39 @@
                     "title": "Healthcare Cost and Utilization Project (HCUP) Summary Trends Tables"
                 }
             ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/reports/trendtables/summarytrendtables.jsp"
+            "identifier": "https://healthdata.gov/api/views/cqqt-nv72",
+            "issued": "2022-06-07",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "hcup",
+                "healthcare cost and utilization"
+            ],
+            "landingPage": "https://www.hcup-us.ahrq.gov",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:074"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "references": [
+                "https://www.hcup-us.ahrq.gov/reports/trendtables/HCUPSummaryTrendTables_Methods.xlsx"
+            ],
+            "title": "Healthcare Cost and Utilization Project (HCUP) Summary Trends Tables"
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
-                "county",
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
-            "identifier": "https://data.cdc.gov/api/views/xyst-f73f",
             "description": "This dataset contains model-based county-level estimates for the PLACES 2022 release in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. Project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2020 or 2019 county population estimates, and American Community Survey (ACS) 2016\u20132020 or 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. These data can be joined with the census 2020 county boundary file in a GIS system to produce maps for 29 measures at the county level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: County Data (GIS Friendly Format), 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51224,46 +51196,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xyst-f73f",
+            "issued": "2023-06-15",
+            "keyword": [
+                "behaviors",
+                "county",
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
+            "title": "PLACES: County Data (GIS Friendly Format), 2022 release"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -51286,54 +51262,56 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospice-all-owners",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/e983965e-1603-4cb8-82b5-c40090e380d1/data-viewer",
-            "description": "The \u00a0Hospice All Owners dataset provides ownership information on all hospices currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
-            "title": "Hospice All Owners",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospice_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The \u00a0Hospice All Owners dataset provides ownership information on all hospices currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e983965e-1603-4cb8-82b5-c40090e380d1/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e983965e-1603-4cb8-82b5-c40090e380d1/data",
+                    "mediaType": "text/html",
                     "title": "Hospice All Owners : 2025-01-01"
                 },
                 {
@@ -51433,47 +51411,50 @@
                     "title": "Hospice All Owners : 2023-04-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospice_All_Owners_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/e983965e-1603-4cb8-82b5-c40090e380d1/data-viewer",
+            "issued": "2023-04-20",
+            "keyword": [
+                "hospice",
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospice-all-owners",
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
+            "title": "Hospice All Owners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/CCDS/CcdsBrowse.cgi",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nmdi-yqxg",
             "description": "The Consensus CDS (CCDS) project is a collaborative effort to identify a core set of human and mouse protein coding regions that are consistently annotated and of high quality. The long term goal is to support convergence towards a standard set of gene annotations.",
-            "title": "Consensus CDS (CCDS)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51488,41 +51469,41 @@
                     "title": "Download CCDS Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nmdi-yqxg",
+            "issued": "2021-06-17",
+            "keyword": [
+                "dataset",
+                "genetics",
+                "genomics",
+                "protein"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/CCDS/CcdsBrowse.cgi",
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
+            "title": "Consensus CDS (CCDS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/nq6q-szvs",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2014-04-01",
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
-            "identifier": "https://data.cdc.gov/api/views/nq6q-szvs",
             "description": "Changes in the rates of TBI-related deaths vary depending on age.  For persons 44 years of age and younger, TBI-related deaths decreased between the periods of 2001-2002 and 2009-2010.  Rates for age groups 45-64 years of age remained stable for this same ten-year period.  For persons 65 years and older, rates of TBI-related deaths increased during this time period, from 41.2 to 45.2 deaths per 100,000.Go to http://www.cdc.gov/traumaticbraininjury/data/index.html to view more TBI data & statistics.Source: http://www.cdc.gov/traumaticbraininjury/data/rates_deaths_byage.html",
-            "title": "Rates of TBI-related Deaths by Age Group - United States, 2001 - 2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51545,97 +51526,87 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/nq6q-szvs",
+            "issued": "2014-04-01",
+            "keyword": [
+                "brain injury",
+                "head trauma",
+                "tbi",
+                "traumatic brain injury"
+            ],
+            "landingPage": "https://data.cdc.gov/d/nq6q-szvs",
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
+            "title": "Rates of TBI-related Deaths by Age Group - United States, 2001 - 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/cssi-nbpn",
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
-            "identifier": "6f27ead3-bc9e-529a-a2b1-2cf5efea881e",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard pillar v2.12.1-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/pillar.csv",
-                    "description": "Scorecard pillar v2.12.1-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard pillar v2.12.1-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard pillar v2.12.1-test (local)"
                 }
             ],
+            "identifier": "6f27ead3-bc9e-529a-a2b1-2cf5efea881e",
+            "issued": "2023-08-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/cssi-nbpn",
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
+            "title": "Scorecard pillar v2.12.1-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.findhivcare.hrsa.gov/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-05-30",
-            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "references": [
-                "https://hab.hrsa.gov/stateprofiles/State-Overview.aspx"
-            ],
-            "keyword": [
-                "health care providers",
-                "health center",
-                "hiv aids",
-                "locator",
-                "low income",
-                "map",
-                "medical",
-                "ryan white",
-                "service",
-                "treatment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HRSA Data Warehouse",
                 "hasEmail": "mailto:datawarehouse@hrsa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Health Resources and Services Administration, Department of Health & Human Services"
-            },
-            "identifier": "d5636ec5-83f1-40fc-bd15-973fdc17359b",
             "description": "<p>The Find Ryan White HIV/AIDS Medical Care Providers tool is a locator that helps people living with HIV/AIDS access medical care and related services. Users can search for Ryan White-funded medical care providers near a specific complete address, city and state, state and county, or ZIP code.</p>\n<p>Search results are sorted by distance away and include the Ryan White HIV/AIDS facility name, address, approximate distance from the search point, telephone number, website address, and a link for driving directions.</p>\n<p>HRSA's Ryan White program funds an array of grants at the state and local levels in areas where most needed. These grants provide medical and support services to more than a half million people who otherwise would be unable to afford care.</p>",
-            "title": "Find Ryan White HIV/AIDS Medical Care Providers",
-            "programCode": [
-                "009:016"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51644,45 +51615,51 @@
                     "title": "Query Tool "
                 }
             ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "theme": [
-                "Health"
-            ]
+            "identifier": "d5636ec5-83f1-40fc-bd15-973fdc17359b",
+            "issued": "2012-05-30",
+            "keyword": [
+                "health care providers",
+                "health center",
+                "hiv aids",
+                "locator",
+                "low income",
+                "map",
+                "medical",
+                "ryan white",
+                "service",
+                "treatment"
+            ],
+            "landingPage": "https://www.findhivcare.hrsa.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:016"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Health Resources and Services Administration, Department of Health & Human Services"
+            },
+            "references": [
+                "https://hab.hrsa.gov/stateprofiles/State-Overview.aspx"
+            ],
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "theme": [
+                "Health"
+            ],
+            "title": "Find Ryan White HIV/AIDS Medical Care Providers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qz67-9a9h",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/qz67-9a9h",
             "description": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51705,23 +51682,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qz67-9a9h",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-congenital",
+                "wonder",
+                "yellow fever",
+                "zika virus disease"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qz67-9a9h",
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
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-county",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2014-06-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/physician-e-rx-through-ehr"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-county",
+            "description": "Electronic prescribing (eRx) is a key component of the meaningful use of health IT to improve health care quality and lower costs. This dataset includes county-level electronic prescribing (eRx) and health information exchange activity by community pharmacies and office-based health care providers active through the Surescripts Network. Surescripts is a health information network, and ONC procured electronic prescribing activity data conducted within its network from December 2008 through April 2014. The Surescripts network is used by the majority of all U.S. community pharmacies to rout prescriptions, excluding closed systems such as Kaiser Permanente. These include chain, franchise, and independently owned pharmacies. Data for annual percentages of new and renewal prescriptions routed through the Surescripts network exclude controlled substances. You may view more information about Surescripts, contact the company, and access more network data through the company's official site.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/Surescripts_County_04-2014.csv",
+                    "mediaType": "text/csv",
+                    "title": "Surescripts_County_04-2014.csv"
+                }
             ],
+            "identifier": "y6vgv2n0-vxxe-pk39-wsqz-9l5plgpjljzr",
+            "issued": "2023-10-03",
             "keyword": [
                 "county",
                 "doctors",
@@ -51732,105 +51742,78 @@
                 "health it",
                 "physicians"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-county",
+            "modified": "2014-06-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "y6vgv2n0-vxxe-pk39-wsqz-9l5plgpjljzr",
-            "description": "Electronic prescribing (eRx) is a key component of the meaningful use of health IT to improve health care quality and lower costs. This dataset includes county-level electronic prescribing (eRx) and health information exchange activity by community pharmacies and office-based health care providers active through the Surescripts Network. Surescripts is a health information network, and ONC procured electronic prescribing activity data conducted within its network from December 2008 through April 2014. The Surescripts network is used by the majority of all U.S. community pharmacies to rout prescriptions, excluding closed systems such as Kaiser Permanente. These include chain, franchise, and independently owned pharmacies. Data for annual percentages of new and renewal prescriptions routed through the Surescripts network exclude controlled substances. You may view more information about Surescripts, contact the company, and access more network data through the company's official site.",
-            "title": "Electronic Prescribing Adoption and Use by County",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/Surescripts_County_04-2014.csv",
-                    "mediaType": "text/csv",
-                    "title": "Surescripts_County_04-2014.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/quickstats/physician-e-rx-through-ehr"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-county"
+            "title": "Electronic Prescribing Adoption and Use by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/cxha-65ek",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-01",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-31",
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
-            "identifier": "b5cdefdb-4031-575a-8bb4-8607fabf6cb3",
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
+            "identifier": "b5cdefdb-4031-575a-8bb4-8607fabf6cb3",
+            "issued": "2023-06-01",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/cxha-65ek",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-05-31",
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
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/rysd-8s3y",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-09-14",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rysd-8s3y",
             "description": "Health Services Research Projects in Progress (HSRProj) was a database of health services research and public health projects in progress, related to research in quality, cost, and access to health care. It included behavioral health research and public health research, with over 38,000 projects and information back to the 1990s.\n\nThis resource was retired on September 14, 2021 and is no longer updated.",
-            "title": "Health Services Research Projects in Progress (HSRProj)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51853,53 +51836,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rysd-8s3y",
+            "issued": "2021-09-14",
+            "keyword": [
+                "health services research",
+                "public health"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/rysd-8s3y",
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
+            "title": "Health Services Research Projects in Progress (HSRProj)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-15",
-            "temporal": "2015/2021",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xy7w-35q7",
             "description": "Provisional deaths involving coronavirus disease 2019 (COVID-19) and deaths from all causes reported to NCHS by week the death occurred, HHS region of occurrence, race and Hispanic origin, and age group (0-24, 25-64, 65+ years), from 2015-2021.\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
-            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age, 2015-2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51922,46 +51892,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xy7w-35q7",
+            "issued": "2021-09-15",
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
+            "modified": "2022-04-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2015/2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age, 2015-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/udsf-9v7b",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-07-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-24",
-            "keyword": [
-                "covid19",
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
                 "fn": "James Singleton",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/udsf-9v7b",
             "description": "National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics.",
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)-Archived",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51984,47 +51961,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/udsf-9v7b",
+            "issued": "2022-07-06",
+            "keyword": [
+                "covid19",
+                "covid-19 vaccination",
+                "immunization",
+                "nis-acm",
+                "vaccination",
+                "vaccination coverage",
+                "vaccine confidence",
+                "vaxviews"
+            ],
+            "landingPage": "https://data.cdc.gov/d/udsf-9v7b",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-01-24",
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
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)-Archived"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/esrd-restricted.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-16",
-            "@type": "dcat:Dataset",
-            "temporal": "1974/2018",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/Variable-List.pdf"
-            ],
-            "keyword": [
-                "linked usrds esrd files",
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
-            "identifier": "https://data.cdc.gov/api/views/jmgj-74h4",
-            "description": "NCHS has linked data from various surveys with End Stage Renal Disease (ESRD) data obtained from the United States Renal Data System (USRDS). Linkage of the data from NCHS survey participants with the USRDS ESRD data provides the opportunity to study changes in health status and health care utilization among patients diagnosed with ESRD.",
-            "title": "NCHS Survey Data Linked to United States Renal Data System (USRDS) End-Stage Renal Disease Files",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/MatchRate-Tables.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "NCHS has linked data from various surveys with End Stage Renal Disease (ESRD) data obtained from the United States Renal Data System (USRDS). Linkage of the data from NCHS survey participants with the USRDS ESRD data provides the opportunity to study changes in health status and health care utilization among patients diagnosed with ESRD.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52032,46 +52009,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/MatchRate-Tables.pdf",
+            "identifier": "https://data.cdc.gov/api/views/jmgj-74h4",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-16",
+            "keyword": [
+                "linked usrds esrd files",
+                "nchs surveys",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/esrd-restricted.htm",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/Variable-List.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "1974/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Survey Data Linked to United States Renal Data System (USRDS) End-Stage Renal Disease Files"
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
@@ -52094,47 +52073,47 @@
                     "mediaType": "application/xml"
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
+            "title": "2022 Final Assisted Reproductive Technology (ART) Success Rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-provider-enrollment/medicare-provider-type-reports/cms-program-statistics-medicare-providers",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-06",
-            "references": [
-                "https://data.cms.gov/resources/medicare-provider-type-methodology"
-            ],
-            "keyword": [
-                "medicare",
-                "national",
-                "original medicare",
-                "provider enrollment",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/5ad4e138-a8b4-49e1-a2f4-34f52b3a665a/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-provider-type-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Providers summary tables provide data on institutional (i.e., hospitals, skilled nursing facilities, home health agencies, hospices, etc.) and non-institutional (i.e., physicians, nonphysicians, specialists, and suppliers) providers.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR PROVIDERS 1. \u00a0Medicare Providers: Number of Medicare Certified Institutional Providers, Yearly Trend\n\tMDCR PROVIDERS 2. \u00a0Medicare Providers: \u00a0Number of Medicare Certified Inpatient Hospital and Skilled Nursing Facility Beds and Beds Per 1,000 Enrollees, Yearly Trend\n\tMDCR PROVIDERS 3. \u00a0Medicare Providers: \u00a0Number of Medicare Certified Facilities, by Type of Control, Yearly Trend\n\tMDCR PROVIDERS 4. \u00a0Medicare Providers: \u00a0Number of Skilled Nursing Facilities and Medicare Certified Hospitals, and Number of Beds, by State, Territories, Possessions and Other Areas\n\tMDCR PROVIDERS 5. \u00a0Medicare Providers: \u00a0Number of Medicare Certified Providers, by Type of Provider, by State, Territories, Possessions, and Other Areas\n\tMDCR PROVIDERS 6. \u00a0Medicare Providers: \u00a0Number of Medicare Non-Institutional Providers by Specialty, Yearly Trend\n\tMDCR PROVIDERS 7. \u00a0Medicare Providers: \u00a0Number of Medicare Non-Institutional Providers, by State, Territories, Possessions, and Other Areas, Yearly Trend",
-            "title": "CMS Program Statistics - Medicare Providers",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52191,58 +52170,58 @@
                     "title": "CMS Program Statistics - Medicare Providers : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-provider-type-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/5ad4e138-a8b4-49e1-a2f4-34f52b3a665a/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "national",
+                "original medicare",
+                "provider enrollment",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-provider-enrollment/medicare-provider-type-reports/cms-program-statistics-medicare-providers",
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
+                "https://data.cms.gov/resources/medicare-provider-type-methodology"
+            ],
+            "temporal": "2013-01-01/2021-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS Program Statistics - Medicare Providers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/accountable-care-organization-participants",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/9767cb68-8ea9-4f0b-8179-9431abc89f11/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/accountable-care-organization-participants-data-dictionary",
             "description": "The Accountable Care Organization Participants data presents overview information on ACO participants in the Medicare Shared Savings Program (Shared Savings Program), including their name, track status, number of years in the program, and contact information of key personnel.\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to ACO information occur periodically. Each ACO has the most up-to-date information about their organization. Consider contacting the ACO for the latest information.",
-            "title": "Accountable Care Organization Participants",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9767cb68-8ea9-4f0b-8179-9431abc89f11/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9767cb68-8ea9-4f0b-8179-9431abc89f11/data",
+                    "mediaType": "text/html",
                     "title": "Accountable Care Organization Participants : 2025-01-15"
                 },
                 {
@@ -52402,51 +52381,49 @@
                     "title": "Accountable Care Organization Participants : 2014-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/accountable-care-organization-participants-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9767cb68-8ea9-4f0b-8179-9431abc89f11/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/accountable-care-organization-participants",
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
+            "title": "Accountable Care Organization Participants"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -52469,57 +52446,46 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/service-locator-family-planning-title-x",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2014-04-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "birth control",
-                "cervical cancer",
-                "community health",
-                "contraceptives",
-                "family planning",
-                "health care providers",
-                "health services",
-                "locator",
-                "pregnancy",
-                "primary care",
-                "providers",
-                "safety",
-                "sexual assault",
-                "sexually transmitted infections",
-                "stds",
-                "stis",
-                "testing",
-                "treatment",
-                "treatments",
-                "wellness"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Population Affairs",
                 "hasEmail": "mailto:opa@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Health & Human Services"
-            },
-            "identifier": "20f6d943-1707-457d-876b-ef65bcd7f476",
+            "dataQuality": true,
             "description": "<p>This locator tool will help you find Title X family planning centers that provide high quality and cost-effective family planning and related preventive health services for low-income women and men.</p>\n<p>Family planning centers offer a broad range of FDA-approved contraceptive methods and related counseling; as well as breast and cervical cancer screening; pregnancy testing and counseling; screening and treatment for sexually transmitted infections (STIs); HIV testing; and other patient education and referrals.</p>\n<p>4,400 family planning centers serve about 5 million clients each year. Services are provided through state, county, and local health departments; community health centers; Planned Parenthood centers; and hospital-based, school-based, faith-based, other private nonprofits.</p>\n<p>Title X staff are specially trained to meet the contraceptive needs of individuals with limited English proficiency, teenagers, and those confronting complex medical and personal issues such as substance abuse, disability, homelessness or interpersonal and domestic violence.</p>",
-            "title": "Service Locator - Family Planning Title X",
-            "programCode": [
-                "009:019"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52546,40 +52512,59 @@
                     "title": "API "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "20f6d943-1707-457d-876b-ef65bcd7f476",
+            "issued": "2014-04-08",
+            "keyword": [
+                "birth control",
+                "cervical cancer",
+                "community health",
+                "contraceptives",
+                "family planning",
+                "health care providers",
+                "health services",
+                "locator",
+                "pregnancy",
+                "primary care",
+                "providers",
+                "safety",
+                "sexual assault",
+                "sexually transmitted infections",
+                "stds",
+                "stis",
+                "testing",
+                "treatment",
+                "treatments",
+                "wellness"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/service-locator-family-planning-title-x",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:019"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
             "theme": [
                 "Community",
                 "Health"
-            ]
+            ],
+            "title": "Service Locator - Family Planning Title X"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/d2f3-87v3",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2015-04-07",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
-            "keyword": [
-                "drug manufacturer contacts"
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
-            "identifier": "9fcb14ec-d5f0-536e-9938-3f0024531e5b",
             "description": "Drug Manufacturer Contact Information contains Optional Effective Date, Termination Date (if applicable), and Legal, Invoice and Technical Contact information for each drug company participating in the Medicaid Drug Rebate Program. For more information see: https://www.medicaid.gov/medicaid/prescription-drugs/medicaid-drug-rebate-program/index.html",
-            "title": "Drug Manufacturer Contacts",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52587,39 +52572,39 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "9fcb14ec-d5f0-536e-9938-3f0024531e5b",
+            "issued": "2015-04-07",
+            "keyword": [
+                "drug manufacturer contacts"
+            ],
+            "landingPage": "https://healthdata.gov/d/d2f3-87v3",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-11-08",
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
+            "title": "Drug Manufacturer Contacts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/d3b6-wcft",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-01-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-22",
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
-            "identifier": "bbdcd2d0-13ac-4c1f-8670-914acb43b81e",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-15-to-2024-01-21",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52628,81 +52613,83 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-15-to-2024-01-21"
                 }
             ],
+            "identifier": "bbdcd2d0-13ac-4c1f-8670-914acb43b81e",
+            "issued": "2024-01-24",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/d3b6-wcft",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-01-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-15-to-2024-01-21"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/d3br-cfmg",
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
-            "identifier": "edbb579b-1056-5cb6-99b9-16f4dafbd27e",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_fileType_measureDisplayGroups",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/fileType_measureDisplayGroups.csv",
-                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/fileType_measureDisplayGroups.csv",
+                    "mediaType": "text/csv",
                     "title": "fileType_measureDisplayGroups csv file"
                 }
             ],
+            "identifier": "edbb579b-1056-5cb6-99b9-16f4dafbd27e",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/d3br-cfmg",
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
+            "title": "implAuto_fileType_measureDisplayGroups"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -52725,37 +52712,33 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/9ikp-t8tw",
+            "issued": "2024-11-21",
+            "landingPage": "https://data.cdc.gov/d/9ikp-t8tw",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-23",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "CDT_INDIVIDUAL_BY_WEEK_LOCAL"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/d52h-r2s7",
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
-            "identifier": "ec0d4b04-55bc-56d1-bff5-280f68915442",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 1993",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52763,55 +52746,50 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "ec0d4b04-55bc-56d1-bff5-280f68915442",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/d52h-r2s7",
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
+            "title": "State Drug Utilization Data 1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-enrollments",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/5f2c306f-3b1c-42cd-b037-187b2ce22126/data-viewer",
-            "description": "The Skilled Nursing Facility (SNF) Enrollments dataset provides enrollment information of all SNF 's currently enrolled in Medicare. This data includes information on the SNF's legal business name, doing business as name, organization type and address.\n\n\u00a0\n\nOn November 17, 2023, CMS published in the Federal Register a final rule titled, \u201cMedicare and Medicaid Programs; Disclosures of Ownership and Additional Disclosable Parties Information for Skilled Nursing Facilities and Nursing Facilities; Medicare Providers\u2019 and Suppliers\u2019 Disclosure of Private Equity Companies and Real Estate Investment Trusts\u201d (88 FR 80141). This final rule implements parts of section 1124(c) of the Act which requires SNFs to disclose detailed information about their ownership and management as well as additional data regarding: (1) other parties with which the SNF is associated; and (2) the ownership structures of these other parties.\u00a0 Refer to Medicare Enrollment for Providers & Suppliers for more information on the Skilled Nursing Facility disclosure requirements. \n\nSection 6101(b) of the Affordable Care Act states that no later than 1 year after final regulations promulgated under section 1124(c) of the Act are published in the\u00a0Federal Register, the Secretary shall make the information reported available to the public.\n\n\u00a0On November 21, 2024 CMS updated this dataset to include this reported information.",
-            "title": "Skilled Nursing Facility Enrollments",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/SNF_Enrollments_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Skilled Nursing Facility (SNF) Enrollments dataset provides enrollment information of all SNF 's currently enrolled in Medicare. This data includes information on the SNF's legal business name, doing business as name, organization type and address.\n\n\u00a0\n\nOn November 17, 2023, CMS published in the Federal Register a final rule titled, \u201cMedicare and Medicaid Programs; Disclosures of Ownership and Additional Disclosable Parties Information for Skilled Nursing Facilities and Nursing Facilities; Medicare Providers\u2019 and Suppliers\u2019 Disclosure of Private Equity Companies and Real Estate Investment Trusts\u201d (88 FR 80141). This final rule implements parts of section 1124(c) of the Act which requires SNFs to disclose detailed information about their ownership and management as well as additional data regarding: (1) other parties with which the SNF is associated; and (2) the ownership structures of these other parties.\u00a0 Refer to Medicare Enrollment for Providers & Suppliers for more information on the Skilled Nursing Facility disclosure requirements. \n\nSection 6101(b) of the Affordable Care Act states that no later than 1 year after final regulations promulgated under section 1124(c) of the Act are published in the\u00a0Federal Register, the Secretary shall make the information reported available to the public.\n\n\u00a0On November 21, 2024 CMS updated this dataset to include this reported information.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5f2c306f-3b1c-42cd-b037-187b2ce22126/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5f2c306f-3b1c-42cd-b037-187b2ce22126/data",
+                    "mediaType": "text/html",
                     "title": "Skilled Nursing Facility Enrollments : 2025-01-01"
                 },
                 {
@@ -53151,59 +53129,51 @@
                     "title": "Skilled Nursing Facility Enrollments : 2022-09-20"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/SNF_Enrollments_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/5f2c306f-3b1c-42cd-b037-187b2ce22126/data-viewer",
+            "issued": "2022-09-27",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment",
+                "skilled nursing"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-enrollments",
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
+            "title": "Skilled Nursing Facility Enrollments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-19",
-            "temporal": "2000/2021",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-30",
-            "keyword": [
-                "bureau of labor statistics",
-                "health care employment",
-                "health care practitioners",
-                "health care practitioners and technical occupations",
-                "health care support occupations",
-                "health care wages",
-                "health us",
-                "hourly wages",
-                "industry",
-                "mean hourly wages",
-                "occupational employment and wage statistics",
-                "sdoh-occupation-type",
-                "sdoh-source-of-health-care",
-                "sdoh-wages",
-                "us department of labor"
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
-            "identifier": "https://data.cdc.gov/api/views/q9cb-be9u",
             "description": "Data on health care employment and wages in the United States, by selected occupations. Data are from Health, United States. Source: U.S. Department of Labor, Bureau of Labor Statistics, Occupational Employment and Wage Statistics.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Health care employment and wages, by selected occupations: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53226,56 +53196,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/q9cb-be9u",
+            "issued": "2024-09-19",
+            "keyword": [
+                "bureau of labor statistics",
+                "health care employment",
+                "health care practitioners",
+                "health care practitioners and technical occupations",
+                "health care support occupations",
+                "health care wages",
+                "health us",
+                "hourly wages",
+                "industry",
+                "mean hourly wages",
+                "occupational employment and wage statistics",
+                "sdoh-occupation-type",
+                "sdoh-source-of-health-care",
+                "sdoh-wages",
+                "us department of labor"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-09-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2000/2021",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Health care employment and wages, by selected occupations: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-27",
-            "keyword": [
-                "african americans",
-                "alaskan natives",
-                "american natives",
-                "asian continental ancestry group",
-                "continental population groups",
-                "death",
-                "european continental ancestry group",
-                "fetal death",
-                "health us",
-                "hispanic americans",
-                "infant",
-                "infant death",
-                "live birth",
-                "mortality",
-                "mothers",
-                "oceanic ancestry group",
-                "pregnancy",
-                "pregnancy complications"
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
-            "identifier": "https://data.cdc.gov/api/views/nfuu-hu6j",
             "description": "Data on infant, neonatal, postneonatal, fetal, and perinatal mortality rates by selected characteristics of the mother. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Vital Statistics System, public-use Linked Birth/Infant Death Data Set, public-use Fetal Death File, and public-use Birth File. For more information on the National Vital Statistics System, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Infant, neonatal, postneonatal, fetal, and perinatal mortality rates, by detailed race and Hispanic origin of mother: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53298,38 +53265,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/nfuu-hu6j",
+            "issued": "2021-05-14",
+            "keyword": [
+                "african americans",
+                "alaskan natives",
+                "american natives",
+                "asian continental ancestry group",
+                "continental population groups",
+                "death",
+                "european continental ancestry group",
+                "fetal death",
+                "health us",
+                "hispanic americans",
+                "infant",
+                "infant death",
+                "live birth",
+                "mortality",
+                "mothers",
+                "oceanic ancestry group",
+                "pregnancy",
+                "pregnancy complications"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-27",
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
+            "title": "Infant, neonatal, postneonatal, fetal, and perinatal mortality rates, by detailed race and Hispanic origin of mother: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/Medsun/searchReportText.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-13",
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
-            "identifier": "068aa9da-ef7e-419a-9de2-2a690dbec65b",
             "description": "The Medical Product Safety Network (MedSun) is an adverse event reporting program launched in 2002. The primary goal for MedSun is to work collaboratively with the clinical community to identify, understand, and solve problems with the use of medical devices.",
-            "title": "MedSun Reports",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53337,81 +53321,78 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "068aa9da-ef7e-419a-9de2-2a690dbec65b",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/Medsun/searchReportText.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-13",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "MedSun Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/health-it-catalog",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HealthITcatalog",
+                "hasEmail": "mailto:HealthITcatalog@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This is a consolidated list of Health IT initiatives and websites across HHS.</p>",
+            "identifier": "0fb05840-02fe-4199-8f2b-efaac0e5d868",
             "issued": "2013-11-08",
-            "temporal": "2013-07-01T00:00:00-04:00/2013-07-01T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "health care cost",
                 "health care providers",
                 "office-of-the-national-coordinator-for-health-information-technology-department-of-health-human-services",
                 "other"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HealthITcatalog",
-                "hasEmail": "mailto:HealthITcatalog@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/health-it-catalog",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology, Department of Health & Human Services"
             },
-            "identifier": "0fb05840-02fe-4199-8f2b-efaac0e5d868",
-            "description": "<p>This is a consolidated list of Health IT initiatives and websites across HHS.</p>",
-            "title": "Health IT Catalog",
-            "programCode": [
-                "009:110"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "temporal": "2013-07-01T00:00:00-04:00/2013-07-01T00:00:00-04:00",
+            "title": "Health IT Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/fiscal-intermediary-shared-system-attending-and-rendering",
+            "accrualPeriodicity": "R/P3.5D",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2023-05-21/2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2020-08/Fiscal%20Intermediary%20Standard%20System%20%28FISS%29.pdf"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/75e8dcb2-78eb-4a7d-a377-9108441966db/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/fiscal-intermediary-shared-system-attending-and-rendering-data-dictionary",
             "description": "The Fiscal Intermediary Shared System (FISS) Attending and Rendering dataset provides a list of those attending and rendering physicians for the FISS. FISS edits require that the Line Item Rendering Physician information be transmitted when providers submit a combined claim. Claims that include both facility and professional components, need to report the rendering physician or other practitioner at the line level if it differs from the rendering physician/practitioner reported at the claim level.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Fiscal Intermediary Shared System Attending and Rendering",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/75e8dcb2-78eb-4a7d-a377-9108441966db/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/75e8dcb2-78eb-4a7d-a377-9108441966db/data",
+                    "mediaType": "text/html",
                     "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21"
                 },
                 {
@@ -55467,52 +55448,47 @@
                     "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/fiscal-intermediary-shared-system-attending-and-rendering-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/75e8dcb2-78eb-4a7d-a377-9108441966db/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/fiscal-intermediary-shared-system-attending-and-rendering",
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
+                "https://data.cms.gov/sites/default/files/2020-08/Fiscal%20Intermediary%20Standard%20System%20%28FISS%29.pdf"
+            ],
+            "temporal": "2023-05-21/2025-01-18",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Fiscal Intermediary Shared System Attending and Rendering"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rwap-xbst",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
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
-            "identifier": "https://data.cdc.gov/api/views/rwap-xbst",
             "description": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
-            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55535,41 +55511,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rwap-xbst",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/rwap-xbst",
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
+            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/2015-plan-selections-zip-code-health-insurance-marketplace",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-04-10",
-            "temporal": "2014-11-15T00:00:00-05:00/2015-02-22T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "administrative",
-                "marketplace enrollment  zip code  plan selections",
-                "population statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Munira Gunja",
                 "hasEmail": "mailto:munira.gunja@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Assistant Secretary for Planning & Evaluation, Department of Health & Human Services"
-            },
-            "identifier": "de6f60a0-e3d0-4b25-9601-701ff82d7e0e",
+            "dataQuality": true,
+            "describedBy": "http://aspe.hhs.gov/health/reports/2015/MarketPlaceEnrollment/EnrollmentByZip/rpt_EnrollmentByZip_Apr2015.cfm",
             "description": "<p>The dataset here provides the total number of Qualified Health Plan selections by ZIP Code for 37 states for the second Health Insurance Marketplace open enrollment period (November 15, 2014 \u2013 February 15, 2015, including additional special enrollment period activity reported through February 22, 2015).</p>",
-            "title": "2015 Plan Selections by ZIP Code in the Health Insurance Marketplace",
-            "programCode": [
-                "009:072"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55578,41 +55561,39 @@
                     "title": "CSV"
                 }
             ],
-            "describedBy": "http://aspe.hhs.gov/health/reports/2015/MarketPlaceEnrollment/EnrollmentByZip/rpt_EnrollmentByZip_Apr2015.cfm",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "de6f60a0-e3d0-4b25-9601-701ff82d7e0e",
+            "issued": "2015-04-10",
+            "keyword": [
+                "administrative",
+                "marketplace enrollment  zip code  plan selections",
+                "population statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/2015-plan-selections-zip-code-health-insurance-marketplace",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Assistant Secretary for Planning & Evaluation, Department of Health & Human Services"
+            },
+            "temporal": "2014-11-15T00:00:00-05:00/2015-02-22T00:00:00-05:00",
+            "title": "2015 Plan Selections by ZIP Code in the Health Insurance Marketplace"
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
-            "temporal": "1950-01-01/2000-12-31",
-            "modified": "2022-03-23",
-            "keyword": [
-                "cause of death",
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
-            "identifier": "https://data.cdc.gov/api/views/mc4y-cbbv",
             "description": "This dataset contains information on the number of deaths and age-adjusted death rates for the five leading causes of death in 1900, 1950, and 2000.\n\nAge-adjusted death rates (deaths per 100,000) after 1998 are calculated based on the 2000 U.S. standard population. Populations used for computing death rates for 2011\u20132017 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years between 2000 and 2010 are revised using updated intercensal population estimates and may differ from rates previously published. Data on age-adjusted death rates prior to 1999 are taken from historical data (see References below).\n\nSOURCES\n\nCDC/NCHS, National Vital Statistics System, historical data, 1900-1998 (see https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm); CDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\n\nREFERENCES\n\n1. National Center for Health Statistics, Data Warehouse. Comparability of cause-of-death between ICD revisions. 2008. Available from: http://www.cdc.gov/nchs/nvss/mortality/comparability_icd.htm.\n\n2. National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.\n\n3. Kochanek KD, Murphy SL, Xu JQ, Arias E. Deaths: Final data for 2017. National Vital Statistics Reports; vol 68 no 9. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_09-508.pdf.\n\n4. Arias E, Xu JQ. United States life tables, 2017. National Vital Statistics Reports; vol 68 no 7. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_07-508.pdf.\n\n5. National Center for Health Statistics. Historical Data, 1900-1998. 2009. Available from: https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm.",
-            "title": "NCHS - Top Five Leading Causes of Death: United States, 1990, 1950, 2000",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55635,47 +55616,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/mc4y-cbbv",
+            "issued": "2015-07-14",
+            "keyword": [
+                "cause of death",
+                "mortality",
+                "nchs",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-trends/index.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2022-03-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "1950-01-01/2000-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NCHS - Top Five Leading Causes of Death: United States, 1990, 1950, 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/d9iu-q3ng",
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
-            "identifier": "e68d9ef0-549c-4fec-a91b-781eb865c60e",
             "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2024 Medical SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55683,22 +55664,50 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "e68d9ef0-549c-4fec-a91b-781eb865c60e",
+            "issued": "2024-08-06",
+            "keyword": [
+                "py2024",
+                "qhp",
+                "qhp landscape",
+                "shop",
+                "shop market medical"
+            ],
+            "landingPage": "https://healthdata.gov/d/d9iu-q3ng",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2024 Medical SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/DataPage.aspx?Component=LimitedAccess&Cycle=1959-1994",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2018-03-01",
-            "@type": "dcat:Dataset",
-            "temporal": "1971/1994",
-            "modified": "2023-04-17",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/index.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "The NHANES samples were selected using complex, stratified, multistage probability cluster sampling designs.",
+            "description": "The <b> National Health and Nutrition Examination Survey</b> (NHANES) is designed to assess the health and nutritional status of adults and children in the United States. The survey is unique in that it combines interviews with standardized physical examinations and laboratory tests. <br>\nNHANES was conducted on a periodic basis from 1971 to 1994, including NHANES I (1971-1975), NHANES II (1976-1980), NHANES III (1988-1994), and a Hispanic Health and Nutrition Examination Survey (HHANES, 1982-1984). In 1999, NHANES became continuous and has been collecting data annually ever since. <br>\nAll of the NHANES programs utilized a stratified, multistage probability cluster design to provide a nationally representative sample of the U.S. civilian, noninstitutionalized population. The NHANES interview includes demographic, socioeconomic, dietary, and health-related questions. The examination component conducted in a mobile examination center consists of medical, dental, and physiological measurements, as well as the collection of biospecimens, such as blood and urine for laboratory testing.\n\nThis set of restricted data contains indirect identifying and/or sensitive information collected in <b>NHANES prior to 1999. </b>Please refer to the links below for additional data available from NHANES:\n<ul><li><a href=\"https://wwwn.cdc.gov/nchs/nhanes/Default.aspx\">NHANES Public Use Data at: https://wwwn.cdc.gov/nchs/nhanes/Default.aspx</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/9ixb-fwvy\">NHANES Restricted Data: 1999 - present at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/9ixb-fwvy</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu\">NHANES Genetic Restricted Data at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs\">NHANES National Youth Fitness Survey (NNYFS) Restricted Data at: https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs</a></li> </ul>\nPlease refer to the <a href=\"https://www.cdc.gov/nchs/nhanes/index.htm\">NHANES - National Health and Nutrition Examination Survey Homepage at: https://www.cdc.gov/nchs/nhanes/index.htm</a> for further details on the NHANES design, implementation, and data analysis.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: Prior to 1999"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ic32-yq9m",
+            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/default.aspx",
+            "issued": "2018-03-01",
             "keyword": [
                 "health statistics",
                 "nchs",
@@ -55708,68 +55717,39 @@
                 "surveillance",
                 "survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/DataPage.aspx?Component=LimitedAccess&Cycle=1959-1994",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-17",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/ic32-yq9m",
-            "description": "The <b> National Health and Nutrition Examination Survey</b> (NHANES) is designed to assess the health and nutritional status of adults and children in the United States. The survey is unique in that it combines interviews with standardized physical examinations and laboratory tests. <br>\nNHANES was conducted on a periodic basis from 1971 to 1994, including NHANES I (1971-1975), NHANES II (1976-1980), NHANES III (1988-1994), and a Hispanic Health and Nutrition Examination Survey (HHANES, 1982-1984). In 1999, NHANES became continuous and has been collecting data annually ever since. <br>\nAll of the NHANES programs utilized a stratified, multistage probability cluster design to provide a nationally representative sample of the U.S. civilian, noninstitutionalized population. The NHANES interview includes demographic, socioeconomic, dietary, and health-related questions. The examination component conducted in a mobile examination center consists of medical, dental, and physiological measurements, as well as the collection of biospecimens, such as blood and urine for laboratory testing.\n\nThis set of restricted data contains indirect identifying and/or sensitive information collected in <b>NHANES prior to 1999. </b>Please refer to the links below for additional data available from NHANES:\n<ul><li><a href=\"https://wwwn.cdc.gov/nchs/nhanes/Default.aspx\">NHANES Public Use Data at: https://wwwn.cdc.gov/nchs/nhanes/Default.aspx</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/9ixb-fwvy\">NHANES Restricted Data: 1999 - present at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/9ixb-fwvy</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu\">NHANES Genetic Restricted Data at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs\">NHANES National Youth Fitness Survey (NNYFS) Restricted Data at: https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs</a></li> </ul>\nPlease refer to the <a href=\"https://www.cdc.gov/nchs/nhanes/index.htm\">NHANES - National Health and Nutrition Examination Survey Homepage at: https://www.cdc.gov/nchs/nhanes/index.htm</a> for further details on the NHANES design, implementation, and data analysis.",
-            "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: Prior to 1999",
-            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/default.aspx",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "mediaType": "text/html",
-                    "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: Prior to 1999"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/nhanes/index.htm"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "describedBy": "The NHANES samples were selected using complex, stratified, multistage probability cluster sampling designs.",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "1971/1994",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: Prior to 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ssz5-s49e",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-24",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
-            "keyword": [
-                "haicviz",
-                "healthcare associated infections",
-                "mrsa",
-                "mssa",
-                "staphylococcus aureus"
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
-            "identifier": "https://data.cdc.gov/api/views/ssz5-s49e",
             "description": "<p>The healthcare-associated infection component of CDC\u2019s <a href=\"https://www.cdc.gov/ncezid/dpei/eip/index.html\" target=\"_blank\">EIP</a> engages a <a href=\"https://www.cdc.gov/ncezid/dpei/eip/eip-sites.html\" target=\"_blank\">network</a> of state health departments and their academic medical center partners to help answer critical questions about emerging HAI threats, advanced infection tracking methods, and antibiotic resistance in the United States. Information gathered through this activity will play a key role in shaping future policies and recommendations targeting HAI prevention. Click <a href=\"https://www.cdc.gov/hai/eip/saureus.html\" target=\"_blank\">here</a> to learn more about Invasive Staphylococcus aureus infections</p>\n\n<h3>Interpretation</h3>\n<ul><li>Data presented in HAICViz may differ from other HAIC publications since different datasets or methods may be used.</li><li>Small numbers for some topics or filters may make year to year changes difficult to interpret.</li><li>Since each infection may have unique characteristics, the information available to display differs by individual organism.</li></ul>\n\n<h3>More Details</h3>\n<ul><li><a href=\"https://www.cdc.gov/hai/eip/saureus.html#Methods\" target=\"_blank\">Methodology</a>: Find details about surveillance population, case determination, surveillance evaluation, and more.</li><li>Reports and Findings: Access <a href=\"https://www.cdc.gov/hai/eip/saureus.html#anchor_1611155585754\" target=\"_blank\">reports</a> or lists of <a href=\"https://www.cdc.gov/hai/eip/saureus.html#anchor_1611155777037\" target=\"_blank\">publications</a> using HAIC Invasive Staphylococcus aureus data</li></ul>",
-            "title": "HAICViz - iSA",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55792,38 +55772,43 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ssz5-s49e",
+            "issued": "2021-06-24",
+            "keyword": [
+                "haicviz",
+                "healthcare associated infections",
+                "mrsa",
+                "mssa",
+                "staphylococcus aureus"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ssz5-s49e",
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
+            "title": "HAICViz - iSA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/damp-z9iv",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-11-12",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-10",
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
-            "identifier": "92b5948f-b32b-404c-ad28-ea83de8a324e",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211101 to 20211107",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55831,88 +55816,83 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "92b5948f-b32b-404c-ad28-ea83de8a324e",
+            "issued": "2021-11-12",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/damp-z9iv",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2021-11-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211101 to 20211107"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pubchem.ncbi.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "chemistry physical",
-                "community health",
-                "dataset",
-                "organic chemicals"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/t2ny-ab25",
             "description": "PubChem contains the chemical structures of small organic molecules and information on their biological activities. PubChem includes substance information, compound structures, and bioactivity data in three primary databases, PCSubstance, PCCompound, and PCBioAssay, respectively. PubChem is integrated with Entrez, NCBI's primary search engine, and also provides compound neighboring, sub/superstructure, similarity structure, bioactivity data, and other searching features. Technical documentation at \thttp://pubchem.ncbi.nlm.nih.gov/help.html#faq",
-            "title": "PubChem",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/power-user-gateway",
-                    "description": "The PubChem Power User Gateway (PUG) provides access to PubChem services via programmatic interfaces (REST, SOAP, . The basic design principle is straightforward. There is a single CGI (pug.cgi, referred to hereafter as simply PUG) that is the central gateway to multiple PubChem functions. PUG takes no URL arguments; all communication with PUG is through XML.",
                     "@type": "dcat:Distribution",
+                    "description": "The PubChem Power User Gateway (PUG) provides access to PubChem services via programmatic interfaces (REST, SOAP, . The basic design principle is straightforward. There is a single CGI (pug.cgi, referred to hereafter as simply PUG) that is the central gateway to multiple PubChem functions. PUG takes no URL arguments; all communication with PUG is through XML.",
+                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/power-user-gateway",
+                    "mediaType": "text/html",
                     "title": "API - PubChem Power User Gateway (PUG)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pubchem.ncbi.nlm.nih.gov/standardize/standardize.cgi",
-                    "description": "Standardization in PubChem is the validation and determination of a unique chemical structure that is used to create a PubChem Compound from one or more submitted Substance records. Standardization is part of the PubChem Upload pipeline for submitted records with valid chemical structures. It allows PubChem to display one Compound page for aspirin (for example) that includes information from many submitted aspirin Substance records.",
                     "@type": "dcat:Distribution",
+                    "description": "Standardization in PubChem is the validation and determination of a unique chemical structure that is used to create a PubChem Compound from one or more submitted Substance records. Standardization is part of the PubChem Upload pipeline for submitted records with valid chemical structures. It allows PubChem to display one Compound page for aspirin (for example) that includes information from many submitted aspirin Substance records.",
+                    "downloadURL": "https://pubchem.ncbi.nlm.nih.gov/standardize/standardize.cgi",
+                    "mediaType": "text/html",
                     "title": "PubChem Standardization Service"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pubchem.ncbi.nlm.nih.gov/search/search.cgi",
-                    "description": "PubChem Structure Search provides various chemical search types and options.",
                     "@type": "dcat:Distribution",
+                    "description": "PubChem Structure Search provides various chemical search types and options.",
+                    "downloadURL": "https://pubchem.ncbi.nlm.nih.gov/search/search.cgi",
+                    "mediaType": "text/html",
                     "title": "PubChem Structure Search - Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://pubchem.ncbi.nlm.nih.gov/upload/#welcome",
-                    "description": "The PubChem Upload tool enables you to submit data to the PubChem Substance and PubChem BioAssay databases, or update your existing data, including chemical structures, experimental biological activity results, annotations, siRNA data and more. Once your submission is reviewed and published in PubChem, your data will be available for Open Access to the public around the world.",
                     "@type": "dcat:Distribution",
+                    "description": "The PubChem Upload tool enables you to submit data to the PubChem Substance and PubChem BioAssay databases, or update your existing data, including chemical structures, experimental biological activity results, annotations, siRNA data and more. Once your submission is reviewed and published in PubChem, your data will be available for Open Access to the public around the world.",
+                    "downloadURL": "https://pubchem.ncbi.nlm.nih.gov/upload/#welcome",
+                    "mediaType": "text/html",
                     "title": "PubChem Upload"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pcsubstance",
-                    "description": "The PubChem Substance Database contains descriptions of samples, from a variety of sources, and links to biological screening results that are available in PubChem BioAssay. If the chemical contents of a sample are known, the description includes links to PubChem Compound.",
                     "@type": "dcat:Distribution",
+                    "description": "The PubChem Substance Database contains descriptions of samples, from a variety of sources, and links to biological screening results that are available in PubChem BioAssay. If the chemical contents of a sample are known, the description includes links to PubChem Compound.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pcsubstance",
+                    "mediaType": "text/html",
                     "title": "PubChem Substance"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pccompound",
-                    "description": "The PubChem Compound Database contains validated chemical depiction information provided to describe substances in PubChem Substance. Structures stored within PubChem Compounds are pre-clustered and cross-referenced by identity and similarity groups.",
                     "@type": "dcat:Distribution",
+                    "description": "The PubChem Compound Database contains validated chemical depiction information provided to describe substances in PubChem Substance. Structures stored within PubChem Compounds are pre-clustered and cross-referenced by identity and similarity groups.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pccompound",
+                    "mediaType": "text/html",
                     "title": "PubChem Compound"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pcassay",
-                    "description": "The PubChem BioAssay Database contains bioactivity screens of chemical substances described in PubChem Substance. It provides searchable descriptions of each bioassay, including descriptions of the conditions and readouts specific to that screening procedure.",
                     "@type": "dcat:Distribution",
+                    "description": "The PubChem BioAssay Database contains bioactivity screens of chemical substances described in PubChem Substance. It provides searchable descriptions of each bioassay, including descriptions of the conditions and readouts specific to that screening procedure.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pcassay",
+                    "mediaType": "text/html",
                     "title": "PubChem BioAssay"
                 },
                 {
@@ -55922,99 +55902,97 @@
                     "title": "Downloading PubChem Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/t2ny-ab25",
+            "issued": "2012-05-30",
+            "keyword": [
+                "api",
+                "chemistry physical",
+                "community health",
+                "dataset",
+                "organic chemicals"
+            ],
+            "landingPage": "https://pubchem.ncbi.nlm.nih.gov/",
             "license": "http://opendatacommons.org/licenses/odbl/1.0/",
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
+            "title": "PubChem"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/dbdd-hhrf",
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
-            "identifier": "0833a46e-3155-5b38-a029-2d05abe6721c",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure v2.11.18 (etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/measure.csv",
-                    "description": "Scorecard measure v2.11.18 (etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure v2.11.18 (etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure v2.11.18 (etl-test)"
                 }
             ],
+            "identifier": "0833a46e-3155-5b38-a029-2d05abe6721c",
+            "issued": "2023-04-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/dbdd-hhrf",
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
+            "title": "Scorecard measure v2.11.18 (etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/strong-start-for-mothers-and-newborns-initiative/strong-start-awardees",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2017-01-01/2017-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-12",
-            "references": [
-                "https://data.cms.gov/resources/strong-start-awardees-methodology"
-            ],
-            "keyword": [
-                "children's health insurance program",
-                "health care use & payments",
-                "medicaid",
-                "payment models",
-                "service delivery models",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/9d4218d7-bb48-4278-964b-01755f0d8a85/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/strong-start-awardees-data-dictionary",
             "description": "The Strong Start Awardees dataset provides information on the financial awards made to participants in the Strong Start for Mothers and Newborns Initiative. This initiative tested three evidence-based maternity care service approaches with the goal of improving health outcomes of pregnant women and newborns. The data can include the participant name, participant location, locations of practices participating under the participants\u2019 umbrella practice, descriptive text for the type(s) of enhanced prenatal care provided, and the amount of funding awarded to the participant as a result of their participation in year 1 of the initiative.",
-            "title": "Strong Start Awardees",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9d4218d7-bb48-4278-964b-01755f0d8a85/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9d4218d7-bb48-4278-964b-01755f0d8a85/data",
+                    "mediaType": "text/html",
                     "title": "Strong Start Awardees : 2017-09-25"
                 },
                 {
@@ -56030,103 +56008,106 @@
                     "title": "Strong Start Awardees : 2017-09-25"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/strong-start-awardees-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9d4218d7-bb48-4278-964b-01755f0d8a85/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "children's health insurance program",
+                "health care use & payments",
+                "medicaid",
+                "payment models",
+                "service delivery models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/strong-start-for-mothers-and-newborns-initiative/strong-start-awardees",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-05-12",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/strong-start-awardees-methodology"
+            ],
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "Medicaid",
                 "Children's Health Insurance Program"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Strong Start Awardees"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://api.ncbi.nlm.nih.gov/variation/v0/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "data specifications",
-                "genetics",
-                "genomics",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jy6x-w83b",
             "description": "This genetic variation services interconvert and transform short genetic variants between HGVS expressions,  VCF format, and the new SPDI (Sequence Position Deletion Insertion) format, based on alignment datasets used by ClinVar and dbSNP.  NOTE: This service is still in beta testing mode",
-            "title": "SPDI Variation Service",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://api.ncbi.nlm.nih.gov/variation/v0/",
-                    "description": "dbSNP provides bulk download in VCF and JSON at https://ftp.ncbi.nih.gov/snp/latest_release/ for users with a large number of RefSNPs (>100K) to process.  NOTE: This service is still in beta testing mode. Please limit your request rate to 1 request/second.  ",
                     "@type": "dcat:Distribution",
+                    "description": "dbSNP provides bulk download in VCF and JSON at https://ftp.ncbi.nih.gov/snp/latest_release/ for users with a large number of RefSNPs (>100K) to process.  NOTE: This service is still in beta testing mode. Please limit your request rate to 1 request/second.  ",
+                    "downloadURL": "https://api.ncbi.nlm.nih.gov/variation/v0/",
+                    "mediaType": "text/html",
                     "title": "API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jy6x-w83b",
+            "issued": "2021-06-30",
+            "keyword": [
+                "api",
+                "data specifications",
+                "genetics",
+                "genomics",
+                "molecular biology",
+                "tools & utilities"
+            ],
+            "landingPage": "https://api.ncbi.nlm.nih.gov/variation/v0/",
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
+            "title": "SPDI Variation Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-spending-by-drug",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2022-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-13",
-            "references": [
-                "https://data.cms.gov/resources/medicare-part-b-spending-by-drug-methodology"
-            ],
-            "keyword": [
-                "drugs",
-                "medicare",
-                "original medicare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS Drug Spending - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-part-b-spending-by-drug-data-dictionary",
             "description": "The Medicare Part B by Drug dataset presents information on spending for drugs administered in doctors\u2019 offices and other outpatient settings by physicians and other healthcare providers to Medicare Part B enrollees.\u00a0\n\nThe dataset focuses on average spending per dosage unit and change in average spending per dosage unit over time. It\u00a0also includes consumer-friendly descriptions of the drug uses, clinical indications, and manufacturer(s).\n\nDrug spending metrics for Part B drugs represent the full value of the product, including the Medicare payment and beneficiary liability. All Part B drug spending metrics are calculated at the HCPCS level.",
-            "title": "Medicare Part B Spending by Drug",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Part B Spending by Drug : 2022-01-01"
                 },
                 {
@@ -56142,51 +56123,48 @@
                     "title": "Medicare Part B Spending by Drug : 2022-01-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-part-b-spending-by-drug-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "drugs",
+                "medicare",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-spending-by-drug",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-part-b-spending-by-drug-methodology"
+            ],
+            "temporal": "2022-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Part B Spending by Drug"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -56209,61 +56187,47 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-10-21",
-            "temporal": "2020-01-01/2020-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "keyword": [
-                "age",
-                "age group",
-                "causes of death",
-                "chronic liver disease",
-                "chronic lower respiratory disease",
-                "cirrhosis",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "diabetes",
-                "hypertensive disease",
-                "kidney disease",
-                "major cardiovascular diseases",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "obesity",
-                "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/qdcb-uzft",
             "description": "Provisional death counts of diabetes, coronavirus disease 2019 (COVID-19) and other select causes of death, by month, sex, and age.",
-            "title": "AH Provisional Diabetes Death Counts for 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56286,40 +56250,60 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qdcb-uzft",
+            "issued": "2020-10-21",
+            "keyword": [
+                "age",
+                "age group",
+                "causes of death",
+                "chronic liver disease",
+                "chronic lower respiratory disease",
+                "cirrhosis",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "diabetes",
+                "hypertensive disease",
+                "kidney disease",
+                "major cardiovascular diseases",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "obesity",
+                "provisional",
+                "sex",
+                "united states"
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
+            "temporal": "2020-01-01/2020-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional Diabetes Death Counts for 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://meps.ahrq.gov",
             "bureauCode": [
                 "009:33"
             ],
-            "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
-                "health care cost"
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
-            "identifier": "0855a432-ecad-4c56-8734-76bac1184345",
+            "describedBy": "https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp",
             "description": "The Medical Expenditure Panel Survey (MEPS) Household Component (HC) collects data from a sample of families and individuals in selected communities across the United States, drawn from a nationally representative subsample of households that participated in the prior year's National Health Interview Survey (conducted by the National Center for Health Statistics). During the household interviews, MEPS collects detailed information for each person in the household on the following: demographic characteristics, health conditions, health status, use of medical services, charges and source of payments, access to care, satisfaction with care, health insurance coverage, income, and employment. The panel design of the survey, which features several rounds of interviewing, makes it possible to determine how changes in respondents' health status, income, employment, eligibility for public and private insurance coverage, use of services, and payment for care are related. Public Use Files for Household data are available on the MEPS website.",
-            "title": "Medical Expenditure Panel Survey (MEPS) Household Component Public Use Files",
-            "programCode": [
-                "009:072"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56328,37 +56312,35 @@
                     "title": "Data, Codebook, and Documentation "
                 }
             ],
-            "describedBy": "https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp"
+            "identifier": "0855a432-ecad-4c56-8734-76bac1184345",
+            "issued": "2021-02-13",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "health care cost"
+            ],
+            "landingPage": "https://meps.ahrq.gov",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:072"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "title": "Medical Expenditure Panel Survey (MEPS) Household Component Public Use Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/healthit/snomedct/index.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/aq5x-f2xa",
             "description": "SNOMED CT is one of a suite of designated standards for use in U.S. Federal Government systems for the electronic exchange of clinical health information and is also a required standard in interoperability specifications of the U.S. Healthcare Information Technology Standards Panel.",
-            "title": "SNOMED CT",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56367,20 +56349,52 @@
                     "title": "Download SNOMED CT Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/aq5x-f2xa",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "health data standards",
+                "terminologies"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/healthit/snomedct/index.html",
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
+            "title": "SNOMED CT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datatools.ahrq.gov/meps-hc",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:33"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "MEPS Project Director",
+                "hasEmail": "mailto:mepsprojectdirector@ahrq.hhs.gov"
+            },
+            "describedBy": "https://datatools.ahrq.gov/meps-hc",
+            "description": "The Medical Expenditure Panel Survey (MEPS) Household Component collects data on all members of sample households from selected communities across the United States. With the MEPS-HC Data Tools, users can explore trends and cross-sectional bar charts for nationally representative estimates of household medical utilization and expenditures, demographic and socioeconomic characteristics, health insurance coverage, accessibility and quality of care, treated medical conditions, and prescribed medicine purchases.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datatools.ahrq.gov/meps-hc",
+                    "mediaType": "text/html",
+                    "title": "Query Tool"
+                }
+            ],
+            "identifier": "https://healthdata.gov/api/views/de7f-8ncr",
             "issued": "2022-06-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "agency for healthcare research and quality",
                 "agency-for-healthcare-research-and-quality-department-of-health-human-services",
@@ -56392,69 +56406,32 @@
                 "medical expenditure",
                 "meps"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "MEPS Project Director",
-                "hasEmail": "mailto:mepsprojectdirector@ahrq.hhs.gov"
-            },
+            "landingPage": "https://datatools.ahrq.gov/meps-hc",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:073"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
             },
-            "identifier": "https://healthdata.gov/api/views/de7f-8ncr",
-            "description": "The Medical Expenditure Panel Survey (MEPS) Household Component collects data on all members of sample households from selected communities across the United States. With the MEPS-HC Data Tools, users can explore trends and cross-sectional bar charts for nationally representative estimates of household medical utilization and expenditures, demographic and socioeconomic characteristics, health insurance coverage, accessibility and quality of care, treated medical conditions, and prescribed medicine purchases.",
-            "title": "Medical Expenditure Panel Survey (MEPS) Household Component Data Tools",
-            "programCode": [
-                "009:073"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://datatools.ahrq.gov/meps-hc",
-                    "mediaType": "text/html",
-                    "title": "Query Tool"
-                }
-            ],
-            "describedBy": "https://datatools.ahrq.gov/meps-hc",
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "National"
-            ]
+            ],
+            "title": "Medical Expenditure Panel Survey (MEPS) Household Component Data Tools"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jr4g-zdpg",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/jr4g-zdpg",
             "description": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56477,38 +56454,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jr4g-zdpg",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "other serogroups",
+                "unknown serogroup",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/jr4g-zdpg",
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
+            "title": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/dfe6-ej4t",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-10-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-10-18",
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
-            "identifier": "e38a7952-47df-4d57-b75f-e2775fb854f1",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211011 to 20211017",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56516,43 +56501,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "e38a7952-47df-4d57-b75f-e2775fb854f1",
+            "issued": "2021-10-19",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/dfe6-ej4t",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2021-10-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211011 to 20211017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rsk8-spa7",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rsk8-spa7",
             "description": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56575,41 +56552,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rsk8-spa7",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-congenital",
+                "wonder",
+                "yellow fever",
+                "zika virus disease"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rsk8-spa7",
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
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital"
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
-                "household",
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
-            "identifier": "https://healthdata.gov/api/views/dfw3-qjdi",
+            "describedBy": "https://datatools.ahrq.gov/meps-hc#varexpLabel",
             "description": "The Medical Expenditure Panel Survey (MEPS) Household Component collects data on all members of sample households from selected communities across the United States. The MEPS-HC Variable Explorer Tool provides a quick and easy way to search across MEPS Public Use Files for variables and files needed for users' research projects.",
-            "title": "Medical Expenditure Panel Survey (MEPS) Household Component Variable Explorer",
-            "programCode": [
-                "009:072"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56618,88 +56600,83 @@
                     "title": "Query Tool"
                 }
             ],
-            "describedBy": "https://datatools.ahrq.gov/meps-hc#varexpLabel"
+            "identifier": "https://healthdata.gov/api/views/dfw3-qjdi",
+            "issued": "2022-06-03",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "household",
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
+            "title": "Medical Expenditure Panel Survey (MEPS) Household Component Variable Explorer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/dg8p-t4kf",
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
-            "identifier": "7a7c087d-83f5-5056-94c9-6d479b7b7b49",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard state v2.12.1-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/state.csv",
-                    "description": "Scorecard state v2.12.1-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard state v2.12.1-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/state.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard state v2.12.1-test (local)"
                 }
             ],
+            "identifier": "7a7c087d-83f5-5056-94c9-6d479b7b7b49",
+            "issued": "2023-08-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/dg8p-t4kf",
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
+            "title": "Scorecard state v2.12.1-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/exs3-hbne",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-01-25",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "age-adjusted",
-                "age group",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "mortality",
-                "race and ethnicity",
-                "sex"
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
-            "identifier": "https://data.cdc.gov/api/views/exs3-hbne",
             "description": "Monthly COVID-19 death rates per 100,000 population stratified by age group, race/ethnicity, sex, and region, with race/ethnicity by age group and age group by race/ethnicity double stratification",
-            "title": "Monthly COVID-19 Death Rates per 100,000 Population by Age Group, Race and Ethnicity, Sex, and Region with Double Stratification",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56722,21 +56699,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/exs3-hbne",
+            "issued": "2024-01-25",
+            "keyword": [
+                "age-adjusted",
+                "age group",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "race and ethnicity",
+                "sex"
+            ],
+            "landingPage": "https://data.cdc.gov/d/exs3-hbne",
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
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Monthly COVID-19 Death Rates per 100,000 Population by Age Group, Race and Ethnicity, Sex, and Region with Double Stratification"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1992",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1992) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1992-nid13534",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1992-nid13534"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1992-nid13534",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -56749,64 +56762,29 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1992",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1992-nid13534",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1992)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1992-nid13534",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1992) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1992-nid13534"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1992)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/cdi/overview.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
-            "keyword": [
-                "alcohol",
-                "arthritis",
-                "asthma",
-                "cancer",
-                "copd",
-                "diabetes",
-                "tobacco"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC Info",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hksd-2xuw",
             "description": "CDC's Division of Population Health provides a cross-cutting set of 115 indicators developed by consensus among CDC, the Council of State and Territorial Epidemiologists, and the National Association of Chronic Disease Directors.  These indicators allow states and territories to uniformly define, collect, and report chronic disease data that are important to public health practice in their area. In addition to providing access to state-specific indicator data, the CDI web site serves as a gateway to additional information and data resources.",
-            "title": "U.S. Chronic Disease Indicators",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56829,25 +56807,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hksd-2xuw",
+            "issued": "2023-11-13",
+            "keyword": [
+                "alcohol",
+                "arthritis",
+                "asthma",
+                "cancer",
+                "copd",
+                "diabetes",
+                "tobacco"
+            ],
+            "landingPage": "https://www.cdc.gov/cdi/overview.html",
             "license": "http://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2024-10-16",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Chronic Disease Indicators"
-            ]
+            ],
+            "title": "U.S. Chronic Disease Indicators"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/nnyfsdata.aspx?Component=LimitedAccess",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2022-10-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2012/2012",
-            "modified": "2023-04-17",
-            "references": [
-                "https://www.cdc.gov/nchs/nnyfs/index.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "NNYFS was conducted concurrently with NHANES in 2012, the second year of the NHANES 2011\u20132012 cycle, with survey participants selected from an independent sample of dwelling units within the segments selected for that year of NHANES. The sample design has consisted of stratified, clustered four-stage probability sampling.",
+            "description": "The <b>National Health and Nutrition Examination Survey\u2019s</b> (NHANES) <b>National Youth Fitness Survey</b> (NNYFS) was conducted in 2012 to collect nationally representative data on physical activity and fitness levels for U.S. children and adolescents aged 3-15 years, through household interviews and fitness tests conducted in mobile examination centers. <br>\nThe NNYFS interview includes demographic, socioeconomic, dietary, and health-related questions. The fitness tests included standardized measurements of core, upper, and lower body muscle strength, and gross motor skills, as well as a measurement of cardiovascular fitness by walking and running on a treadmill. A total of 1,640 children and adolescents aged 3-15 were interviewed and 1,576 were examined. <br>\nThis set of restricted data files contains indirect identifying and/or sensitive information collected in NNYFS. For NNYFS public use files, please visit <a href=\"https://wwwn.cdc.gov/nchs/nhanes/search/nnyfs12.aspx\">NNYFS 2012 at: https://wwwn.cdc.gov/nchs/nhanes/search/nnyfs12.aspx.</a>\nFor more information on the survey design, implementation, and data analysis, see the <a href=\"https://www.cdc.gov/nchs/nnyfs/analytic_guidelines.htm\"> NNYFS Analytic Guidelines at: https://www.cdc.gov/nchs/nnyfs/analytic_guidelines.htm.</a> \nFor more information on NHANES, visit the <a href=\"https://www.cdc.gov/nchs/nhanes/index.htm\"> NHANES - National Health and Nutrition Examination Survey Homepage at: https://www.cdc.gov/nchs/nhanes/index.htm.</a>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "NHANES National Youth Fitness Survey (NNYFS) Restricted Data"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5u84-m4rs",
+            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/search/nnyfs12.aspx",
+            "issued": "2022-10-01",
             "keyword": [
                 "fitness",
                 "health statistics",
@@ -56860,124 +56869,88 @@
                 "surveillance",
                 "survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/nnyfsdata.aspx?Component=LimitedAccess",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-17",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/5u84-m4rs",
-            "description": "The <b>National Health and Nutrition Examination Survey\u2019s</b> (NHANES) <b>National Youth Fitness Survey</b> (NNYFS) was conducted in 2012 to collect nationally representative data on physical activity and fitness levels for U.S. children and adolescents aged 3-15 years, through household interviews and fitness tests conducted in mobile examination centers. <br>\nThe NNYFS interview includes demographic, socioeconomic, dietary, and health-related questions. The fitness tests included standardized measurements of core, upper, and lower body muscle strength, and gross motor skills, as well as a measurement of cardiovascular fitness by walking and running on a treadmill. A total of 1,640 children and adolescents aged 3-15 were interviewed and 1,576 were examined. <br>\nThis set of restricted data files contains indirect identifying and/or sensitive information collected in NNYFS. For NNYFS public use files, please visit <a href=\"https://wwwn.cdc.gov/nchs/nhanes/search/nnyfs12.aspx\">NNYFS 2012 at: https://wwwn.cdc.gov/nchs/nhanes/search/nnyfs12.aspx.</a>\nFor more information on the survey design, implementation, and data analysis, see the <a href=\"https://www.cdc.gov/nchs/nnyfs/analytic_guidelines.htm\"> NNYFS Analytic Guidelines at: https://www.cdc.gov/nchs/nnyfs/analytic_guidelines.htm.</a> \nFor more information on NHANES, visit the <a href=\"https://www.cdc.gov/nchs/nhanes/index.htm\"> NHANES - National Health and Nutrition Examination Survey Homepage at: https://www.cdc.gov/nchs/nhanes/index.htm.</a>",
-            "title": "NHANES National Youth Fitness Survey (NNYFS) Restricted Data",
-            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/search/nnyfs12.aspx",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "mediaType": "text/html",
-                    "title": "NHANES National Youth Fitness Survey (NNYFS) Restricted Data"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/nnyfs/index.htm"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "describedBy": "NNYFS was conducted concurrently with NHANES in 2012, the second year of the NHANES 2011\u20132012 cycle, with survey participants selected from an independent sample of dwelling units within the segments selected for that year of NHANES. The sample design has consisted of stratified, clustered four-stage probability sampling.",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2012/2012",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NHANES National Youth Fitness Survey (NNYFS) Restricted Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/diu3-pej8",
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
-            "identifier": "9001e41d-13c2-589d-b62f-1712298c8c35",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_measure_compare",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare.csv",
-                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_compare csv file"
                 }
             ],
+            "identifier": "9001e41d-13c2-589d-b62f-1712298c8c35",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/diu3-pej8",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
-            "theme": [
-                "Uncategorized"
-            ]
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
+            "theme": [
+                "Uncategorized"
+            ],
+            "title": "implAuto_measure_compare"
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
-            "identifier": "https://data.cdc.gov/api/views/nw2y-v4gm",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
             "description": "This dataset contains model-based census tract-level estimates for the PLACES 2022 release. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Census Tract Data 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57000,36 +56973,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
+            "identifier": "https://data.cdc.gov/api/views/nw2y-v4gm",
+            "issued": "2023-06-15",
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
+            "title": "PLACES: Local Data for Better Health, Census Tract Data 2022 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b5mu-3rk7",
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
-            "identifier": "https://data.cdc.gov/api/views/b5mu-3rk7",
             "description": "Triclosan is an antimicrobial chemical incorporated into products that are applied to the skin of healthcare workers. Exposure to triclosan has previously been shown to be immunomodulatory and associated with allergic disease. Additionally, we have shown that exposure to triclosan dermally activates the NLRP3 inflammasome and disrupts the skin barrier integrity in mice. The skin is the largest organ in the body and plays an important role as a physical barrier and regulator of the immune system. Alterations in the barrier and immune regulatory functions of the skin have been demonstrated to increase the risk of sensitization and development of allergic disease. In this study, the impact of triclosan exposure on the skin barrier and keratinocyte function was investigated using a model of reconstructed human epidermis. The apical surface of reconstructed human epidermis was exposed to triclosan once for 6, 24, or 48 hours or daily for 5 consecutive days.",
-            "title": "Exposure to the antimicrobial chemical triclosan disrupts keratinocyte function and skin integrity in a model of reconstructed human epidermis",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57037,20 +57024,46 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b5mu-3rk7",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/b5mu-3rk7",
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
+            "title": "Exposure to the antimicrobial chemical triclosan disrupts keratinocyte function and skin integrity in a model of reconstructed human epidermis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/fda-peanut-containing-product-recall-0",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The FDA Peanut-Containing Product Recall widget allows you to browse the Food and Drug Administration (FDA) database of peanut butter and peanut-containing products subject to recall. This database makes it easier for you to determine whether any of the products you have at home are subject to recent recalls, and will be updated as new information becomes available.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/Widgets/#peanutrecall",
+                    "mediaType": "text/html",
+                    "title": "Widget "
+                }
+            ],
+            "identifier": "178c1eb8-c2cc-4301-a3e1-b6ff1609b1a6",
             "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "brownie",
                 "cake and pie",
@@ -57072,69 +57085,33 @@
                 "salmonella",
                 "snack bars"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/fda-peanut-containing-product-recall-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration, Department of Health & Human Services"
             },
-            "identifier": "178c1eb8-c2cc-4301-a3e1-b6ff1609b1a6",
-            "description": "<p>The FDA Peanut-Containing Product Recall widget allows you to browse the Food and Drug Administration (FDA) database of peanut butter and peanut-containing products subject to recall. This database makes it easier for you to determine whether any of the products you have at home are subject to recent recalls, and will be updated as new information becomes available.</p>",
-            "title": "FDA Peanut-Containing Product Recall",
-            "programCode": [
-                "009:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cdc.gov/Widgets/#peanutrecall",
-                    "mediaType": "text/html",
-                    "title": "Widget "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "National"
-            ]
+            ],
+            "title": "FDA Peanut-Containing Product Recall"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -57157,41 +57134,45 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -57214,20 +57195,52 @@
                     "mediaType": "application/xml"
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
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2006-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1996",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, and tobacco among members of United<br />\nStates households aged 12 and older. Questions include age at first<br />\nuse as well as lifetime, annual, and past-month usage for the<br />\nfollowing drug classes: marijuana, cocaine (and crack), hallucinogens,<br />\nheroin, inhalants, alcohol, tobacco, and nonmedical use of<br />\nprescription drugs, including psychotherapeutics. Respondents were<br />\nalso asked about substance abuse treatment history, illegal<br />\nactivities, problems resulting from the use of drugs, personal and<br />\nfamily income sources and amounts, need for treatment for drug or<br />\nalcohol use, criminal record, and needle-sharing. Questions on mental<br />\nhealth and access to care, which were introduced in the 1994-B<br />\nquestionnaire (see NATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1994), were retained in this administration of the survey. In<br />\n1996, the section on risk/availability of drugs was reintroduced, and<br />\nsections on driving behavior and personal behavior were<br />\nadded. Demographic data include gender, race, age, ethnicity, marital<br />\nstatus, educational level, job status, income level, veteran status,<br />\nand current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1996) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1996-nid13564",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1996-nid13564"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1996-nid13564",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -57258,59 +57271,29 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1996",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1996-nid13564",
-            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, and tobacco among members of United<br />\nStates households aged 12 and older. Questions include age at first<br />\nuse as well as lifetime, annual, and past-month usage for the<br />\nfollowing drug classes: marijuana, cocaine (and crack), hallucinogens,<br />\nheroin, inhalants, alcohol, tobacco, and nonmedical use of<br />\nprescription drugs, including psychotherapeutics. Respondents were<br />\nalso asked about substance abuse treatment history, illegal<br />\nactivities, problems resulting from the use of drugs, personal and<br />\nfamily income sources and amounts, need for treatment for drug or<br />\nalcohol use, criminal record, and needle-sharing. Questions on mental<br />\nhealth and access to care, which were introduced in the 1994-B<br />\nquestionnaire (see NATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1994), were retained in this administration of the survey. In<br />\n1996, the section on risk/availability of drugs was reintroduced, and<br />\nsections on driving behavior and personal behavior were<br />\nadded. Demographic data include gender, race, age, ethnicity, marital<br />\nstatus, educational level, job status, income level, veteran status,<br />\nand current household composition.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1996)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1996-nid13564",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1996) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1996-nid13564"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1996)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/nichsr/hedges/search.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "health services research",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/q6im-bymd",
             "description": "Health Service Research (HSR) PubMed Queries contains preformulated specialized PubMed searches on healthcare quality and costs.",
-            "title": "Health Service Research (HSR) PubMed Queries",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57319,43 +57302,40 @@
                     "title": "Health Service Research (HSR) PubMed Queries Homepage and Search"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/q6im-bymd",
+            "issued": "2022-02-08",
+            "keyword": [
+                "health services research",
+                "reference"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/nichsr/hedges/search.html",
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
+            "title": "Health Service Research (HSR) PubMed Queries"
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
-                "licensure",
-                "osh",
-                "policy",
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
-            "identifier": "https://data.cdc.gov/api/views/ne52-uraz",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Licensure/ne52-uraz",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  E-Cigarette Legislation\u2014Licensure. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies.  Data are reported on a quarterly basis. Data include information related to requirements, restrictions and penalties associated with holding a retail license to sell e-cigarettes over-the-counter and through vending machines.",
-            "title": "CDC STATE System E-Cigarette Legislation - Licensure",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57378,53 +57358,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Licensure/ne52-uraz",
+            "identifier": "https://data.cdc.gov/api/views/ne52-uraz",
+            "issued": "2023-07-18",
+            "keyword": [
+                "e-cigarette",
+                "legislation",
+                "licensure",
+                "osh",
+                "policy",
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
+            "title": "CDC STATE System E-Cigarette Legislation - Licensure"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -57447,46 +57418,56 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
@@ -57495,26 +57476,58 @@
                     "title": "National Post-acute and Long-term Care Study: Adult Day Service Provider Restricted Dataset"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/npals/2020-NPALS-ADSC-Questionnaire-Center.pdf",
+            "identifier": "https://data.cdc.gov/api/views/xqjn-3jef",
+            "issued": "2022-06-16",
+            "keyword": [
+                "adult day services centers",
+                "covid-19",
+                "long-term care",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/npals/index.html",
+            "language": [
+                "en-US"
+            ],
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Irregular",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/application-process/submission.html",
+            "spatial": "United States",
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
-            "landingPage": "https://healthdata.gov/d/dngx-euui",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jeff Chamblee",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. The information in this table was provided by state officials. In some cases, program or plan names in this table differ from those used in publicly available sources. Questions regarding state-specific information in this table should be directed to State/territorial Medicaid officials.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-by-program-and-plan2022.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "identifier": "0bef7b8a-c663-5b14-9a46-0b5c2b86b0fe",
             "issued": "2017-12-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
             "keyword": [
                 "bho",
                 "comprehensive mco",
@@ -57528,123 +57541,79 @@
                 "pccm",
                 "pihp"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jeff Chamblee",
-                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/dngx-euui",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-16",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "0bef7b8a-c663-5b14-9a46-0b5c2b86b0fe",
-            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. The information in this table was provided by state officials. In some cases, program or plan names in this table differ from those used in publicly available sources. Questions regarding state-specific information in this table should be directed to State/territorial Medicaid officials.",
-            "title": "Managed Care Enrollment by Program and Plan",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-by-program-and-plan2022.csv",
-                    "mediaType": "text/csv",
-                    "title": "CSV"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
             "theme": [
                 "Enrollment"
-            ]
+            ],
+            "title": "Managed Care Enrollment by Program and Plan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/dnzj-fmps",
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
-            "identifier": "49948457-e2d0-55a4-be39-82f0de8d72e1",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure_value v2.10.14 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/measure_value.csv",
-                    "description": "CoreSEt measure_value v2.10.14 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure_value v2.10.14 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure_value v2.10.14 (coreset-dev)"
                 }
             ],
+            "identifier": "49948457-e2d0-55a4-be39-82f0de8d72e1",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/dnzj-fmps",
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
+            "title": "CoreSEt measure_value v2.10.14 (coreset-dev)"
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
-            "identifier": "https://data.cdc.gov/api/views/rja3-32tc",
             "description": "This is the complete dataset for the 500 Cities project 2018 release. This dataset includes 2016, 2015 model-based small area estimates for 27 measures of chronic disease related to unhealthy behaviors (5), health outcomes (13), and use of preventive services (9). Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. It represents a first-of-its kind effort to release information on a large scale for cities and for small areas within those cities. It includes estimates for the 500 largest US cities and approximately 28,000 census tracts within these cities. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these measures include Behavioral Risk Factor Surveillance System (BRFSS) data (2016, 2015), Census Bureau 2010 census population data, and American Community Survey (ACS) 2012-2016, 2011-2015 estimates. Because some questions are only asked every other year in the BRFSS, there are 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, cholesterol screening) from the 2015 BRFSS that are the same in the 2018 release as the previous 2017 release. More information about the methodology can be found at www.cdc.gov/500cities.",
-            "title": "500 Cities: Local Data for Better Health, 2018 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57667,38 +57636,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rja3-32tc",
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
+            "title": "500 Cities: Local Data for Better Health, 2018 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/dpeb-iic2",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-10-07",
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
-            "identifier": "f45f35c5-7aa4-4500-b196-ae7833717add",
             "description": "Clotting Factor (CF) designation allows for a minimum rebate percentage of 17.1 percent of Average Manufacturer Price (AMP) for single source and innovator multiple source drugs.",
-            "title": "Clotting Factor Drug Report",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57706,36 +57691,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "f45f35c5-7aa4-4500-b196-ae7833717add",
+            "issued": "2022-10-07",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/dpeb-iic2",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2025-01-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Clotting Factor Drug Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/dqff-mbxx",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-06",
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
-            "identifier": "c1561c13-1ed6-430f-8d88-7d8cbea6d083",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-30-2024-to-01-05-2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57744,36 +57728,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-30-2024-to-01-05-2025"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "c1561c13-1ed6-430f-8d88-7d8cbea6d083",
+            "issued": "2025-01-08",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/dqff-mbxx",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-30-2024-to-01-05-2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ksf9-pem2",
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
-            "identifier": "https://data.cdc.gov/api/views/ksf9-pem2",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 1 - Boston",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57796,20 +57779,64 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ksf9-pem2",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ksf9-pem2",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 1 - Boston"
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
```

