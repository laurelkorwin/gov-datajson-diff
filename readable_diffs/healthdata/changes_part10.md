# Change History for healthdata.json (Part 10)

### Changes from 31606f9 to dd2190f (Part 9/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/u6jv-9ijr",
-            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis visualization provides weekly data on the number of deaths by jurisdiction of occurrence and cause of death. Counts of deaths in more recent weeks can be compared with counts from earlier years to determine if the number is higher than expected. Selected causes of death are shown, based on analyses of the most prevalent comorbid conditions reported on death certificates where COVID-19 was listed as a cause of death (see https://www.cdc.gov/nchs/nvss/vsrr/covid_weekly/index.htm#Comorbidities). Cause of death counts are based on the underlying cause of death, and presented for Respiratory diseases, Circulatory diseases, Malignant neoplasms, and Alzheimer disease and dementia. Estimated numbers of deaths due to these other causes of death could represent misclassified COVID-19 deaths, or potentially could be indirectly related to COVID-19 (e.g., deaths from other causes occurring in the context of health care shortages or overburdened health care systems). Deaths with an underlying cause of death of COVID-19 are not included in these estimates of deaths due to other causes. Deaths due to external causes (i.e. injuries) or unknown causes are excluded. For more detail, see the Technical Notes.",
-            "title": "Weekly Counts of Death by Jurisdiction and Select Causes of Death",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Weekly Counts of Death by Jurisdiction and Select Causes of Death"
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
@@ -121538,20 +121509,60 @@
                     "mediaType": "application/xml"
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
+            "title": "PLACES: County Data (GIS Friendly Format), 2023 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "Contains data for FDA Hydrolyzed Vegetable Protein (HVP) Containing Products recalls since February, 2010.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "1281388f-93e7-4c1c-9369-5143ec0fdb8e",
+            "issued": "2021-02-25",
             "keyword": [
                 "health",
                 "hvp",
@@ -121561,65 +121572,32 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "1281388f-93e7-4c1c-9369-5143ec0fdb8e",
-            "description": "Contains data for FDA Hydrolyzed Vegetable Protein (HVP) Containing Products recalls since February, 2010.",
-            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls Widget",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls Widget"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/vxpx-d2pt",
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
-            "identifier": "https://data.cdc.gov/api/views/vxpx-d2pt",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 1 is the first round of a three-round survey. In addition to the probability sample in RANDS during COVID-19 Round 1, the questionnaire was administered to the Dynata non-probability online opt-in sample by NORC at the University of Chicago (NORC) from June 9, 2020 to June 30, 2020. The RANDS during COVID-19 Round 1 Non-Probability Sample does not have a known survey sampling design and cannot be used to produce nationally or sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 1 during COVID-19 non-probability sampled Restricted File",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_1_np_technical_documentation.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 1 is the first round of a three-round survey. In addition to the probability sample in RANDS during COVID-19 Round 1, the questionnaire was administered to the Dynata non-probability online opt-in sample by NORC at the University of Chicago (NORC) from June 9, 2020 to June 30, 2020. The RANDS during COVID-19 Round 1 Non-Probability Sample does not have a known survey sampling design and cannot be used to produce nationally or sub-nationally representative estimates.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121627,40 +121605,47 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_1_np_technical_documentation.pdf",
+            "identifier": "https://data.cdc.gov/api/views/vxpx-d2pt",
+            "issued": "2022-06-15",
+            "keyword": [
+                "anxiety",
+                "covid-19",
+                "depression",
+                "missed healthcare",
+                "research-data-center",
+                "telemedicine"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vxpx-d2pt",
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
+            "title": "NCHS Research and Development Survey (RANDS) Round 1 during COVID-19 non-probability sampled Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/raru-q8p9",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-04-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-10",
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
-            "identifier": "fa6bdb2e-a9ac-4f7c-8d10-5549f8146754",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-03-to-2023-04-09",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121669,44 +121654,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-03-to-2023-04-09"
                 }
             ],
+            "identifier": "fa6bdb2e-a9ac-4f7c-8d10-5549f8146754",
+            "issued": "2023-04-12",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/raru-q8p9",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-04-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-03-to-2023-04-09"
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
@@ -121729,39 +121706,47 @@
                     "mediaType": "application/xml"
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
-            "landingPage": "https://healthdata.gov/d/rbee-8ezs",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2017-12-13",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-22",
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
-            "identifier": "0e112ea8-8e8e-5dee-a7e2-7ed551c3baa4",
             "description": "Provides program names, program features, population enrolled, benefits covered, quality assurance and improvement, performance incentives, provider value-based purchasing, participating plans, regions served and program notes.",
-            "title": "Managed Care Programs by State",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121770,49 +121755,39 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "0e112ea8-8e8e-5dee-a7e2-7ed551c3baa4",
+            "issued": "2017-12-13",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/rbee-8ezs",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2018-08-22",
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
+            "title": "Managed Care Programs by State"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -121835,40 +121810,48 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -121891,41 +121874,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8ihh-n7ic",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8ihh-n7ic",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 6 - Dallas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/mesh/meshhome.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/arcv-nkd5",
             "description": "Medical Subject Headings (MeSH) is a hierarchically-organized terminology for indexing and cataloging of biomedical information. It is used for the indexing of PubMed and other NLM databases. Please see the Terms and Conditions for more information regarding the use and re-use of MeSH. NLM produces Medical Subject Headings XML, ASCII, MARC 21 and RDF formats. \n\nUpdates to the data files are made according to the following schedule:\n\nMeSH XML\nMeSH Descriptor files updated annually\nMeSH Qualifier files updated annually\nMeSH Supplemental Concept Records (SCR) updated daily (Monday - Friday)\n\nMeSH ASCII\nMeSH Descriptor files updated annually\nMeSH Qualifier files updated annually\nMeSH Supplemental Concept Records (SCR) updated daily (Monday - Friday)\n\nMeSH MARC21\nAll files posted monthly\n\nMeSH RDF\nAll files posted daily (Monday - Friday)",
-            "title": "Medical Subject Headings (MeSH)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -121952,67 +121933,70 @@
                     "title": "Download - MeSH - Current Production Year"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nlmpubs.nlm.nih.gov/projects/mesh/",
-                    "description": "Directories 1999-2010\n-All the yearly release files produced by MeSH from 1999 to 2010\n\nDirectories 2011-2016\n-These directories contain the yearly release file of MeSH. These files are distributed in November of the prior MeSH year and do not get updated.\n\nRDF MESH N-TRIPLE DATA folders - for info see https://id.nlm.nih.gov/mesh/",
                     "@type": "dcat:Distribution",
+                    "description": "Directories 1999-2010\n-All the yearly release files produced by MeSH from 1999 to 2010\n\nDirectories 2011-2016\n-These directories contain the yearly release file of MeSH. These files are distributed in November of the prior MeSH year and do not get updated.\n\nRDF MESH N-TRIPLE DATA folders - for info see https://id.nlm.nih.gov/mesh/",
+                    "downloadURL": "https://nlmpubs.nlm.nih.gov/projects/mesh/",
+                    "mediaType": "text/html",
                     "title": "Download - MeSH - Archive of Prior Production Years"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://id.nlm.nih.gov/mesh/swagger/ui#/",
-                    "description": "The SPARQL 1.1 endpoint returns RDF results and graphs.  The lookup API returns simple JSON.",
                     "@type": "dcat:Distribution",
+                    "description": "The SPARQL 1.1 endpoint returns RDF results and graphs.  The lookup API returns simple JSON.",
+                    "downloadURL": "https://id.nlm.nih.gov/mesh/swagger/ui#/",
+                    "mediaType": "text/html",
                     "title": "API - MeSH RDF SPARKL endpoint"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://meshb.nlm.nih.gov/search",
-                    "description": "The browser offers two search methods: FullWord Search and SubString Search.  Each method can be further modified to search by Exact Match, All Fragments, or Any Fragment.  ",
                     "@type": "dcat:Distribution",
+                    "description": "The browser offers two search methods: FullWord Search and SubString Search.  Each method can be further modified to search by Exact Match, All Fragments, or Any Fragment.  ",
+                    "downloadURL": "https://meshb.nlm.nih.gov/search",
+                    "mediaType": "text/html",
                     "title": "Query Interface - MeSH Browser - Current Production Year"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://id.nlm.nih.gov/mesh/",
-                    "description": "Resources supporting the RDF serialization of the Medical Subject Headings (MeSH).",
                     "@type": "dcat:Distribution",
+                    "description": "Resources supporting the RDF serialization of the Medical Subject Headings (MeSH).",
+                    "downloadURL": "https://id.nlm.nih.gov/mesh/",
+                    "mediaType": "text/html",
                     "title": "MeSH RDF Resources"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/arcv-nkd5",
+            "issued": "2020-08-06",
+            "keyword": [
+                "api",
+                "dataset",
+                "health data standards",
+                "terminologies"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/mesh/meshhome.html",
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
+            "title": "Medical Subject Headings (MeSH)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/substance-abuse-treatment-facilities-locator",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-12-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "drug and alcohol abuse treatment facilities",
-                "health care providers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "admin",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Substance Abuse & Mental Health Services Administration, Department of Health & Human Services"
-            },
-            "identifier": "c6c074c3-e676-48f1-be33-a412b846e7bb",
+            "dataQuality": true,
             "description": "<p>The Substance Abuse and Mental Health Services Administration (SAMHSA) provides on-line resource for locating drug and alcohol abuse treatment programs. The Substance Abuse Treatment Facility Locator lists:</p>\n<p>Private and public facilities that are licensed, certified, or otherwise approved for inclusion by their State substance abuse agency</p>\n<p>Treatment facilities administered by the Department of Veterans Affairs, the Indian Health Service and the Department of Defense.</p>\n<p>SAMHSA endeavors to keep the Locator current. All information in the Locator is completely updated each year, based on facility responses to SAMHSA's National Survey of Substance Abuse Treatment Services. The most recent complete update occurred on April 16, 2012 based on data collected as of March 31, 2011 in the National Survey of Substance Abuse Treatment Services. New facilities are added monthly. Updates to facility names, addresses, telephone numbers and services are made weekly, if facilities inform SAMHSA of changes.</p>",
-            "title": "Substance Abuse Treatment Facilities Locator",
-            "programCode": [
-                "009:068"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -122021,37 +122005,37 @@
                     "title": "HTML"
                 }
             ],
+            "identifier": "c6c074c3-e676-48f1-be33-a412b846e7bb",
+            "issued": "2012-12-14",
+            "keyword": [
+                "drug and alcohol abuse treatment facilities",
+                "health care providers"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/substance-abuse-treatment-facilities-locator",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:068"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration, Department of Health & Human Services"
+            },
+            "title": "Substance Abuse Treatment Facilities Locator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/rcra-yvyi",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2016-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
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
-            "identifier": "0ad65fe5-3ad3-5d79-a3f9-7893ded7963a",
             "description": "Active drugs that have been reported by participating drug manufacturers under the Medicaid Drug Rebate Program. All drugs are identified by National Drug Code (NDC), unit type, units per package size, product name, Food and Drug Administration (FDA) approval date, the date the drug entered the market, plus indicators to show whether the drug is an innovator or non-innovator drug; whether it is available by prescription or over-the-counter (OTC); the FDA therapeutic equivalency code; and the Drug Efficacy Study Implementation (DESI) rating and termination date. Each quarter posted represents a snapshot of data in the system at that time and is not updated by subsequent changes.",
-            "title": "Drug Products in the Medicaid Drug Rebate Program",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -122060,82 +122044,85 @@
                     "title": "Drug Products in the Medicaid Drug Rebate Program"
                 }
             ],
+            "identifier": "0ad65fe5-3ad3-5d79-a3f9-7893ded7963a",
+            "issued": "2016-09-22",
+            "keyword": [
+                "drug products",
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/rcra-yvyi",
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
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "Drug Products in the Medicaid Drug Rebate Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/re3e-j6wf",
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
-            "identifier": "78950031-dea0-53d7-9247-d5affba75d96",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure_value v2.10.64 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
-                    "description": "CoreSet measure_value v2.10.64 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure_value v2.10.64 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure_value v2.10.64 (coreset-impl)"
                 }
             ],
+            "identifier": "78950031-dea0-53d7-9247-d5affba75d96",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/re3e-j6wf",
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
+            "title": "CoreSet measure_value v2.10.64 (coreset-impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cygf-tgyd",
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
-            "identifier": "https://data.cdc.gov/api/views/cygf-tgyd",
             "description": "Allergic airway diseases are a growing concern in industrialized nations and can be influenced by fungal exposures. Pathogenic yeast species such as Cryptococcus neoformans are known to exacerbate allergic airway disease. Recent indoor assessments have identified Basidiomycota yeasts, including non-pathogenic species such as Vishniacozyma victoriae (syn. Cryptococcus victoriae), to be prevalent and potentially associated with asthma. However, the pulmonary immune response to repeated V. victoriae exposure was previously unexplored. This study aimed to compare the immunological impact of repeated pulmonary exposure to pathogenic and non-pathogenic Cryptococcus yeasts. Mice were repeatedly exposed to either C. neoformans, V. victoriae, or PBS control, and the immune responses were analyzed by measuring histopathological scores, and quantifications of immune cells in the bronchoalveolar lavage fluid or lung via flow cytometry, and cytokine concentrations in the lung. These findings highlight the importance of in vivo characterizations of exposures to frequently detected fungal organisms.",
-            "title": "Persisting Cryptococcus Yeast Species Vishniacozyma victoriae and Cryptococcus neoformans Elicit Unique Airway Inflammation in Mice Following Repeated Exposure",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -122143,54 +122130,44 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cygf-tgyd",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/cygf-tgyd",
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
+            "title": "Persisting Cryptococcus Yeast Species Vishniacozyma victoriae and Cryptococcus neoformans Elicit Unique Airway Inflammation in Mice Following Repeated Exposure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/provider-service-classifications/restructured-betos-classification-system",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2024-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-22",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/2024%20RBCS%20Final%20Report.pdf"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "medical suppliers & equipment",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
-                "outpatient facilities",
-                "physicians & practitioners"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/e3db6e56-149f-49ce-b374-40aecda2357b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/rbcs-data-dictionary-2024",
             "description": "The Restructured BETOS Classification System (RBCS) dataset\u00a0is a taxonomy that allows researchers to group healthcare service codes for Medicare Part B services (i.e., HCPCS codes) into clinically meaningful categories and subcategories. It is based on the original Berenson-Eggers Type of Service (BETOS) classification created in the 1980s, and includes notable updates such as Part B non-physician services.\u00a0The RBCS will undergo annual updates by a technical expert panel of researchers and clinicians.",
-            "title": "Restructured BETOS Classification System",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e3db6e56-149f-49ce-b374-40aecda2357b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e3db6e56-149f-49ce-b374-40aecda2357b/data",
+                    "mediaType": "text/html",
                     "title": "Restructured BETOS Classification System : 2024-10-04"
                 },
                 {
@@ -122206,51 +122183,52 @@
                     "title": "Restructured BETOS Classification System : 2024-10-04"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/rbcs-data-dictionary-2024",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/e3db6e56-149f-49ce-b374-40aecda2357b/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "hospitals & facilities",
+                "medical suppliers & equipment",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "outpatient facilities",
+                "physicians & practitioners"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/provider-service-classifications/restructured-betos-classification-system",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/2024%20RBCS%20Final%20Report.pdf"
+            ],
+            "temporal": "2024-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Restructured BETOS Classification System"
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
-            "identifier": "https://data.cdc.gov/api/views/r35g-znws",
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Heart-Disease-Mortality-Data-Among-US-Adults-35-by/r35g-znws",
             "description": "2012 to 2014, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "title": "Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -122273,45 +122251,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Heart-Disease-Mortality-Data-Among-US-Adults-35-by/r35g-znws",
+            "identifier": "https://data.cdc.gov/api/views/r35g-znws",
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
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-09-30",
-            "@type": "dcat:Dataset",
-            "temporal": "2018-2023",
-            "modified": "2024-03-29",
-            "references": [
-                "CDC"
-            ],
-            "keyword": [
-                "flu",
-                "flu vaccination",
-                "influenza"
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
-            "identifier": "https://data.cdc.gov/api/views/k87d-gv3u",
             "description": "Weekly Cumulative Doses (in Millions) of Influenza Vaccine Distributed by Flu Season in the United States\n\n\u2022  Archived data are available here:  https://data.cdc.gov/resource/e5zk-7tx5 \n\u2022  Flu vaccine is produced by private manufacturers, so supply depends on manufacturers. Vaccine manufacturers have projected that they will supply the United States with as many as 173.5 million to 183.5 million doses of influenza vaccines for the 2022-2023 season. \n\u2022  Additional information is available:\u202fhttps://www.cdc.gov/flu/prevent/vaccine-supply-distribution.htm.",
-            "title": "Weekly Cumulative Doses (in Millions) of Influenza Vaccine Distributed by Flu Season in the United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -122334,97 +122313,97 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/k87d-gv3u",
+            "issued": "2022-09-30",
+            "keyword": [
+                "flu",
+                "flu vaccination",
+                "influenza"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-03-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "CDC"
+            ],
+            "spatial": "United States",
+            "temporal": "2018-2023",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Doses (in Millions) of Influenza Vaccine Distributed by Flu Season in the United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/rh4q-adeb",
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
-            "identifier": "97ad1e5c-235e-5fcb-b7f0-be14d8d5c804",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_measure_concernLevel",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_concernLevel.csv",
-                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_concernLevel.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_concernLevel csv file"
                 }
             ],
+            "identifier": "97ad1e5c-235e-5fcb-b7f0-be14d8d5c804",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/rh4q-adeb",
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
+            "title": "devAuto_measure_concernLevel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-child-abuse-and-neglect-data-system-ncands-child-file",
             "bureauCode": [
                 "009:70"
             ],
-            "issued": "2013-01-18",
-            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "child abuse",
-                "child maltreatment",
-                "children",
-                "children's health",
-                "child safety",
-                "safety"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hale, Malcolm",
                 "hasEmail": "mailto:malcolm.hale@acf.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Administration for Children and Families"
-            },
-            "identifier": "6820d1cb-0e93-4870-b6e0-4a33d84122c1_6_0",
+            "dataQuality": true,
             "description": "<p>The National Child Abuse and Neglect Data System (NCANDS) Child File data set consists of child-specific data of all reports of maltreatment to State child protective service agencies that received an investigation or assessment response. NCANDS is a Federally-sponsored national data collection effort created for the purpose of tracking the volume and nature of child maltreatment reporting each year within the United States. The Child File is the case-level component of the NCANDS. Child File data are collected annually through the voluntary participation of States. Participating States submit their data after going through a process in which the State's administrative system is mapped to the NCANDS data structure.  Data elements include the demographics of children and their perpetrators, types of maltreatment, investigation or assessment dispositions, risk factors, and services provided as a result of the investigation or assessment.</p>",
-            "title": "National Child Abuse and Neglect Data System (NCANDS) Child File: Link to child file dataset for eligible members of the research community",
-            "programCode": [
-                "009:094"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -122433,18 +122412,52 @@
                     "title": "Link to child file dataset for eligible members of the research community"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "6820d1cb-0e93-4870-b6e0-4a33d84122c1_6_0",
+            "issued": "2013-01-18",
+            "keyword": [
+                "child abuse",
+                "child maltreatment",
+                "children",
+                "children's health",
+                "child safety",
+                "safety"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-child-abuse-and-neglect-data-system-ncands-child-file",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:094"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families"
+            },
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "title": "National Child Abuse and Neglect Data System (NCANDS) Child File: Link to child file dataset for eligible members of the research community"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1988",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, anabolic steroids, and tobacco among members of United States households aged 12 and older. Questions include age at first use, as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco, and nonmedical use of psychotherapeutics. Respondents were also asked about problems resulting from their use of drugs, alcohol, and tobacco, their perceptions of the risks involved, insurance coverage, and personal and family income sources and amounts. Demographic data include gender, race, ethnicity, educational level, job status, income level, household composition, and population density.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1988) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1988-nid13604",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1988-nid13604"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1988-nid13604",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -122470,156 +122483,124 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1988",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1988-nid13604",
-            "description": "<p>This series measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, anabolic steroids, and tobacco among members of United States households aged 12 and older. Questions include age at first use, as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco, and nonmedical use of psychotherapeutics. Respondents were also asked about problems resulting from their use of drugs, alcohol, and tobacco, their perceptions of the risks involved, insurance coverage, and personal and family income sources and amounts. Demographic data include gender, race, ethnicity, educational level, job status, income level, household composition, and population density.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1988)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1988-nid13604",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1988) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1988-nid13604"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1988)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/rnd6-9eip",
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
-            "identifier": "933971be-11d4-50e3-bcb0-38388796ac24",
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
+            "identifier": "933971be-11d4-50e3-bcb0-38388796ac24",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/rnd6-9eip",
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
-            "landingPage": "https://healthdata.gov/d/rpi2-kmqe",
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
-            "identifier": "a4d6c830-21c6-5194-81b3-e69a3606ac78",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_topicArea_measureDisplayGroups",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/topicArea_measureDisplayGroups.csv",
-                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/topicArea_measureDisplayGroups.csv",
+                    "mediaType": "text/csv",
                     "title": "topicArea_measureDisplayGroups csv file"
                 }
             ],
+            "identifier": "a4d6c830-21c6-5194-81b3-e69a3606ac78",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/rpi2-kmqe",
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
+            "title": "prodAuto_topicArea_measureDisplayGroups"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.cdc.gov/Laboratory-Surveillance/Percent-Positivity-of-Respiratory-Syncytial-Virus-/3cxc-4k8q",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-24",
-            "@type": "dcat:Dataset",
-            "temporal": "Data from 2020-04-11 to present",
-            "modified": "2025-01-30",
-            "keyword": [
-                "chronic lower respiratory disease",
-                "respiratory disease",
-                "respiratory syncytial virus",
-                "rsv"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Surveillance and Analytics Team",
                 "hasEmail": "mailto:nrevss@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/3cxc-4k8q",
             "description": "More than 450 public health, clinical, and commercial laboratories located throughout the United States voluntarily participate in surveillance for respiratory syncytial virus (RSV) through CDC's National Respiratory and Enteric Virus Surveillance System (NREVSS) (https://www.cdc.gov/surveillance/nrevss/labs/index.html). The data contain weekly, aggregate counts of RSV tests performed and RSV detections as reported to NREVSS since April 11, 2020. \n\nNREVSS data are reported weekly at the national and 10 HHS regional levels (https://www.hhs.gov/about/agencies/iea/regional-offices/index.html). The presented data are RSV Nucleic Acid Amplification Test (NAAT) results, which include reverse transcription-polymerase chain reaction (RT-PCR) tests. These data exclude antigen, antibody, and at-home test results. Less than 5% of RSV tests reported to NREVSS are from antigen tests. All data are provisional and subject to change. Reporting is less complete for the most recent weeks, but relatively complete (>90%) for the period up to 2 weeks earlier. \n\nPercent positivity is a surveillance metric used to monitor RSV activity over time and by geographic area. Participating laboratories send weekly reports of the total number of RSV tests performed that week, and the number of those tests that were positive. In the table and upon hovering on the map, the total test counts reflect the latest data reported to NREVSS and may differ from data presented by public health jurisdictions. Public health jurisdictions may have additional data not reported to NREVSS and may use a different reporting cadence. The RSV trend graphs display the weekly average percent of tests positive for RSV among all the tests performed. Each point on the regional table displays the average number of RSV tests that were performed, and the average percent of those that were positive during a 3-week period (i.e., the specified week, and the weeks immediately preceding and following it). This is also known as a centered, 3-week moving average. The RSV detections displayed are the 5-week moving average (average of the 4 previous and current weeks) in accordance with the recommendations for assessing RSV trends by detections (https://academic.oup.com/jid/article/216/3/345/3860464). \n\nNREVSS strives to present precise estimates of respiratory viral trends and minimize reporting burden for participating laboratories. However, there are several limitations to this surveillance system. NREVSS is a laboratory-based surveillance system that does not have patient-specific data; multiple tests from a single patient may be included. In addition, NREVSS does not collect demographic or clinical data (i.e., hospitalizations or deaths). Testing practices may vary regionally, and the number of participating laboratories may change from year to year. Laboratories from all 50 states report data weekly, but reporting is voluntary and may not be representative of local RSV activity. The data do not include all test results within a jurisdiction and therefore do not reflect all RSV NAATs administered regionally or nationally. Participating laboratories vary in size, testing capabilities, and areas and populations served. Geographic results from clinical laboratories are based on testing location and laboratories may test samples from across one or more states.  For more information on NREVSS and RSV surveillance please visit: https://www.cdc.gov/surveillance/nrevss.",
-            "title": "Percent Positivity of Respiratory Syncytial Virus Nucleic Acid Amplification Tests by HHS Region, National Respiratory and Enteric Virus Surveillance System",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -122642,48 +122623,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/3cxc-4k8q",
+            "issued": "2023-09-24",
+            "keyword": [
+                "chronic lower respiratory disease",
+                "respiratory disease",
+                "respiratory syncytial virus",
+                "rsv"
+            ],
+            "landingPage": "https://data.cdc.gov/Laboratory-Surveillance/Percent-Positivity-of-Respiratory-Syncytial-Virus-/3cxc-4k8q",
+            "language": [
+                "English"
+            ],
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "Data from 2020-04-11 to present",
             "theme": [
                 "Laboratory Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Percent Positivity of Respiratory Syncytial Virus Nucleic Acid Amplification Tests by HHS Region, National Respiratory and Enteric Virus Surveillance System"
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
-            "modified": "2025-01-29",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -122706,26 +122686,72 @@
                     "mediaType": "application/xml"
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
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19 reported to NCHS by time-period, HHS region, race and Hispanic origin, and age group.\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City, Puerto Rico; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/tpcp-uiv5",
             "issued": "2021-02-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-12-29/2023-07-29",
-            "modified": "2023-09-27",
             "keyword": [
                 "age",
                 "age group",
@@ -122745,59 +122771,46 @@
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
-            "identifier": "https://data.cdc.gov/api/views/tpcp-uiv5",
-            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19 reported to NCHS by time-period, HHS region, race and Hispanic origin, and age group.\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City, Puerto Rico; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
-            "title": "Provisional COVID-19 Deaths by HHS Region, Race, and Age",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2019-12-29/2023-07-29",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 Deaths by HHS Region, Race, and Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2005",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network (DAWN-2005) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2005-nid13596",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2005-nid13596"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2005-nid13596",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol",
                 "demographic characteristics",
@@ -122810,66 +122823,29 @@
                 "substance abuse",
                 "suicide"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2005",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2005-nid13596",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network (DAWN-2005)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2005-nid13596",
-                    "description": "Drug Abuse Warning Network (DAWN-2005) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2005-nid13596"
-                }
-            ]
+            "title": "Drug Abuse Warning Network (DAWN-2005)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -122892,35 +122868,46 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/24ct-nyt8",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Research Branch (RB) National Personal Protective Technology Laboratory (NPPTL)",
                 "hasEmail": "mailto:ODAdmin@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/24ct-nyt8",
             "description": "Filtering facepiece respirators (FFRs) are used extensively by healthcare personnel (HCP) during a pandemic. FFRs are primarily reserved for those personnel who have a greater risk and longer duration of exposure compared with other workers and the general public. Some FFR models contain an exhalation valve, which is a device that closes to allow inhaled breath to be pulled through the filter media and opens to allow exhaled breath to be expelled from the respirator through the exhalation valve as well as the filter media. These FFR models provide the wearer with a level of protection like that of an FFR without an exhalation valve, and they are thought to increase the wearer\u2019s comfort at high work rates and be suitable for longer periods of use. However, respiratory secretions expelled by wearers may exit along with air through the exhalation valve. A concern with FFRs with an exhalation valve is that individuals may spread disease if unfiltered, virus-laden aerosols pass through the valve.\n\nDuring the COVID-19 pandemic, guidance from the Centers for Disease Control and Prevention (CDC) did not recommend using an FFR with an exhalation valve for source control (i.e., to filter respiratory secretions to prevent disease transmission to others) and advised that if only this option isavailable and source control was needed, then the valve should be covered with a surgical mask, procedure mask, or a cloth face covering that does not interfere with the respirator fit. The CDC requested research to provide improved science-based recommendations on the use of exhalation valves.\n\nThis study had three aims: (1) to measure the filtration efficiency provided by FFRs with an exhalation valve under conditions of inward airflow (i.e., in the direction of inhalation) and outward airflow (i.e., in the direction of exhalation); (2) to evaluate how particle penetration in FFRs with an exhalation valve compares to particle penetration in surgical masks, procedure masks, cloth face coverings, and fabric from cotton t-shirts; and (3) to determine the filtration efficiency of three modifications to the exhalation valve in FFRs with the goal of mitigating the emission of unfiltered particles. To accomplish these three aims, thirteen FFR models were each tested in two positions: inward position, which is used by the NIOSH Respirator Approval Program when testing N-type respirators, and outward position, which was used experimentally to channel airflow in the direction of exhalation. For the inward position, three mitigation strategies were used:\n(1)covering the valve on the interior of the FFR with commonly available surgical tape,\n(2)covering the valve on the interior of the FFR with an electrocardiogram (ECG) pad; and\n(3)stretching a surgical mask over the exterior of the FFR.\n\nThe purpose of these three strategies was to measure the varying filtration efficiencies to determine their contribution toward source control. Both positions and all mitigation strategies were tested at three airflow rates: 25, 55, and 85 lpm (liters per minute). In addition to the FFR evaluations, researchers evaluated a selection of surgical masks, procedure masks, cloth face coverings, and fabric from cotton t-shirts using the outward position and flowrates described previously.",
-            "title": "NPPTL Filtering Facepiece Respirators with an Exhalation Valve: Measurements of Filtration Efficiency to Evaluate Their Potential for Source Control",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -122928,86 +122915,81 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/24ct-nyt8",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/24ct-nyt8",
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
+            "title": "NPPTL Filtering Facepiece Respirators with an Exhalation Valve: Measurements of Filtration Efficiency to Evaluate Their Potential for Source Control"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/rs7d-uj9p",
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
-            "identifier": "197a420c-9b82-5108-b9ba-c2bf27da20c6",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard pillar v2.11.16 (cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/pillar.csv",
-                    "description": "Scorecard pillar v2.11.16 (cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard pillar v2.11.16 (cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard pillar v2.11.16 (cmsdev)"
                 }
             ],
+            "identifier": "197a420c-9b82-5108-b9ba-c2bf27da20c6",
+            "issued": "2023-04-21",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/rs7d-uj9p",
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
+            "title": "Scorecard pillar v2.11.16 (cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/popset",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/c8eu-unh6",
             "description": "The PopSet database is a collection of related DNA sequences derived from population, phylogenetic, mutation and ecosystem studies that have been submitted to GenBank.",
-            "title": "PopSet",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123016,46 +122998,40 @@
                     "title": "Search PopSet - Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/c8eu-unh6",
+            "issued": "2021-08-26",
+            "keyword": [
+                "api",
+                "genetics",
+                "genomics"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/popset",
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
+            "title": "PopSet"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -123078,20 +123054,57 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The primary objective of the National Pregnancy and Health<br />\nSurvey (NPHS) was to produce national annual estimates of the<br />\npercentages and numbers of mothers of live newborns in the United<br />\nStates who used selected licit and illicit drugs in the 12 months<br />\nprior to delivery. A further objective was to describe patterns of<br />\nprenatal substance use among demographic subgroups of<br />\nwomen. Information on demographic and socioeconomic characteristics,<br />\nobstetric history, and drug treatment of women who delivered infants<br />\nat sampled hospitals was obtained through an interviewer-administered<br />\nquestionnaire, while data on substance use before and during pregnancy<br />\nwere collected through a questionnaire completed by the respondent and<br />\nconcealed from the interviewer. Respondents were asked about use of<br />\nthe following substances: alcohol, amphetamines, analgesics, cocaine,<br />\ncrack cocaine, barbiturates, hallucinogens, hashish, heroin,<br />\nmarijuana, methadone, methamphetamine, sedatives, stimulants, tobacco,<br />\nand tranquilizers. Additionally, information was collected on the<br />\nrespondent's pregnancy, prenatal care, delivery, previous pregnancies,<br />\nand background. Additional data were obtained from the mothers' and<br />\ninfants' medical records. Urine specimens collected routinely by the<br />\nhospital on obstetric admissions were tested for selected<br />\ndrugs. Finally, in a subsample of six hospitals, hair specimens were<br />\nrequested from respondents to evaluate the potential of hair as a<br />\nsource of toxicological data in future studies.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Pregnancy and Health Survey: Drug Use Among Women Delivering Live Births (NPHS-1992) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol",
                 "amphetamines",
@@ -123115,41 +123128,47 @@
                 "urinalysis",
                 "women"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992",
-            "description": "<p>The primary objective of the National Pregnancy and Health<br />\nSurvey (NPHS) was to produce national annual estimates of the<br />\npercentages and numbers of mothers of live newborns in the United<br />\nStates who used selected licit and illicit drugs in the 12 months<br />\nprior to delivery. A further objective was to describe patterns of<br />\nprenatal substance use among demographic subgroups of<br />\nwomen. Information on demographic and socioeconomic characteristics,<br />\nobstetric history, and drug treatment of women who delivered infants<br />\nat sampled hospitals was obtained through an interviewer-administered<br />\nquestionnaire, while data on substance use before and during pregnancy<br />\nwere collected through a questionnaire completed by the respondent and<br />\nconcealed from the interviewer. Respondents were asked about use of<br />\nthe following substances: alcohol, amphetamines, analgesics, cocaine,<br />\ncrack cocaine, barbiturates, hallucinogens, hashish, heroin,<br />\nmarijuana, methadone, methamphetamine, sedatives, stimulants, tobacco,<br />\nand tranquilizers. Additionally, information was collected on the<br />\nrespondent's pregnancy, prenatal care, delivery, previous pregnancies,<br />\nand background. Additional data were obtained from the mothers' and<br />\ninfants' medical records. Urine specimens collected routinely by the<br />\nhospital on obstetric admissions were tested for selected<br />\ndrugs. Finally, in a subsample of six hospitals, hair specimens were<br />\nrequested from respondents to evaluate the potential of hair as a<br />\nsource of toxicological data in future studies.This study has 1 Data Set.</p>",
-            "title": "National Pregnancy and Health Survey: Drug Use Among Women Delivering Live Births (NPHS-1992)",
-            "programCode": [
-                "009:030"
+            "title": "National Pregnancy and Health Survey: Drug Use Among Women Delivering Live Births (NPHS-1992)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "001:05"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ajoy Prabhu",
+                "hasEmail": "mailto:aprabhu@od.nih.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This dataset represents all technologies available for licensing from the National Institutes of Health (NIH), the Food and Drug Administration (FDA), and the Center for Disease Control and Prevention (CDC).</p>",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992",
-                    "description": "National Pregnancy and Health Survey: Drug Use Among Women Delivering Live Births (NPHS-1992) \n",
                     "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992"
-                }
-            ]
+                    "downloadURL": "http://www.ott.nih.gov/opportunities",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
                 },
                 {
-            "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/licensing-opportunities-nih-cdc-fda-technologies",
-            "bureauCode": [
-                "001:05"
+                    "@type": "dcat:Distribution",
+                    "accessURL": "http://www.ott.nih.gov/nih-ott-api",
+                    "description": "NIH OTT API - National Institutes of Health Office of Technology Transfer API \n",
+                    "format": "API",
+                    "title": "NIH OTT API"
+                }
             ],
+            "identifier": "caf1a232-013f-4bcf-9258-d7fc10adc73e",
             "issued": "2012-05-30",
-            "temporal": "2014-04-01T00:00:00-04:00/2014-04-01T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "biomedical research",
                 "cdc",
@@ -123165,119 +123184,77 @@
                 "reasearch",
                 "technology"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ajoy Prabhu",
-                "hasEmail": "mailto:aprabhu@od.nih.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "caf1a232-013f-4bcf-9258-d7fc10adc73e",
-            "description": "<p>This dataset represents all technologies available for licensing from the National Institutes of Health (NIH), the Food and Drug Administration (FDA), and the Center for Disease Control and Prevention (CDC).</p>",
-            "title": "Licensing Opportunities for NIH, CDC & FDA Technologies",
+            "landingPage": "https://healthdata.gov/dataset/licensing-opportunities-nih-cdc-fda-technologies",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:046"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ott.nih.gov/opportunities",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
             },
-                {
-                    "format": "API",
-                    "description": "NIH OTT API - National Institutes of Health Office of Technology Transfer API \n",
-                    "accessURL": "http://www.ott.nih.gov/nih-ott-api",
-                    "@type": "dcat:Distribution",
-                    "title": "NIH OTT API"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "temporal": "2014-04-01T00:00:00-04:00/2014-04-01T00:00:00-04:00",
+            "title": "Licensing Opportunities for NIH, CDC & FDA Technologies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ruxz-gvwu",
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
-            "identifier": "50f83c5a-6fa9-4e91-b36c-3d3e225c905f",
             "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). There are three metrics presented: (1) the number of beneficiaries ever enrolled with each benefit package over the year (duplicated count); (2) the number of beneficiaries enrolled with each benefit package as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment with each benefit package. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Some cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.\r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Year",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/BenefitPackage-anul.csv",
-                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). There are three metrics presented: (1) the number of beneficiaries ever enrolled with each benefit package over the year (duplicated count); (2) the number of beneficiaries enrolled with each benefit package as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment with each benefit package. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Some cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). There are three metrics presented: (1) the number of beneficiaries ever enrolled with each benefit package over the year (duplicated count); (2) the number of beneficiaries enrolled with each benefit package as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment with each benefit package. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Some cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/BenefitPackage-anul.csv",
+                    "mediaType": "text/csv",
                     "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Year"
                 }
             ],
+            "identifier": "50f83c5a-6fa9-4e91-b36c-3d3e225c905f",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "program enrollment",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/ruxz-gvwu",
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
+            "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4ynm-6jgm",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "arboviral diseases",
-                "nedss",
-                "netss",
-                "nndss",
-                "st. louis virus disease",
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
-            "identifier": "https://data.cdc.gov/api/views/4ynm-6jgm",
             "description": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile   virus disease - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123300,40 +123277,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4ynm-6jgm",
+            "issued": "2020-01-17",
+            "keyword": [
+                "2020",
+                "arboviral diseases",
+                "nedss",
+                "netss",
+                "nndss",
+                "st. louis virus disease",
+                "west nile virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4ynm-6jgm",
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
+            "title": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/healthywater/surveillance/wastewater-surveillance/wastewater-surveillance.html",
+            "accrualPeriodicity": "Daily",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-04-07",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-22",
-            "keyword": [
-                "covid19",
-                "sars-cov-2",
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
-            "identifier": "https://data.cdc.gov/api/views/2ew6-ywp6",
             "description": "This dataset provides a complete time history of metrics calculated using SARS-CoV-2 concentrations in wastewater.",
-            "title": "NWSS Public SARS-CoV-2 Wastewater Metric Data",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123356,50 +123339,43 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2ew6-ywp6",
+            "issued": "2022-04-07",
+            "keyword": [
+                "covid19",
+                "sars-cov-2",
+                "wastewater"
+            ],
+            "landingPage": "https://www.cdc.gov/healthywater/surveillance/wastewater-surveillance/wastewater-surveillance.html",
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
+            "title": "NWSS Public SARS-CoV-2 Wastewater Metric Data"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -123422,40 +123398,48 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/bridged-race-population-estimates",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-11-05",
-            "temporal": "2002-01-01T00:00:00-05:00/2011-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "population statistics",
-                "race and ethnicity statistics"
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
-            "identifier": "065b5b37-ad82-4921-87db-b676f20aab99",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
             "description": "<p>Population estimates from \"bridging\" the 31 race categories used in Census 2000, as specified in the 1997 Office of Management and Budget (OMB) race and ethnicity data collection standards, to the four race categories specified under the 1977 standards (Asian or Pacific Islander, Black or African American, American Indian or Alaska Native, White).</p>",
-            "title": "Bridged Race Population Estimates",
-            "programCode": [
-                "009:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123464,40 +123448,38 @@
                     "title": "Query Tool "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "065b5b37-ad82-4921-87db-b676f20aab99",
+            "issued": "2012-11-05",
+            "keyword": [
+                "population statistics",
+                "race and ethnicity statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/bridged-race-population-estimates",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2002-01-01T00:00:00-05:00/2011-12-31T00:00:00-05:00",
+            "title": "Bridged Race Population Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/rwqu-teks",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-10-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-24",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "py2025",
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
-            "identifier": "230fcdc8-3a0b-48d5-98d9-36744a87906e",
             "description": "The Transparency in Coverage PUF (TC-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The PUF contains data on issuer and plan-level claims, appeals, and active URL data. The PY2025 PUF contains data from PY2023 for issuers participating in the Exchanges in PY2023.",
-            "title": "Transparency in Coverage PUF - PY2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123505,17 +123487,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "230fcdc8-3a0b-48d5-98d9-36744a87906e",
+            "issued": "2024-10-11",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2025",
+                "transparency in coverage"
+            ],
+            "landingPage": "https://healthdata.gov/d/rwqu-teks",
+            "modified": "2024-10-24",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Transparency in Coverage PUF - PY2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2003-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) measures the<br />\nprevalence and correlates of drug use in the United States. The<br />\nsurveys are designed to provide quarterly, as well as annual,<br />\nestimates. Information is provided on the use of illicit drugs,<br />\nalcohol, and tobacco among members of United States households aged 12<br />\nand older. Questions included age at first use as well as lifetime,<br />\nannual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2003 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, gang involvement,<br />\ndrug use by friends, social support, extracurricular activities,<br />\nexposure to substance abuse prevention and education programs, and<br />\nperceived adult attitudes toward drug use and activities such as<br />\nschool work. Several measures focused on prevention related themes in<br />\nthis section. Also retained were questions on mental health and access<br />\nto care, perceived risk of using drugs, perceived availability of<br />\ndrugs, driving and personal behavior, and cigar smoking. Questions on<br />\nthe tobacco brand used most often were introduced with the 1999 survey<br />\nand retained through the 2003 survey. Background information includes<br />\ngender, race, age, ethnicity, marital status, educational level, job<br />\nstatus, veteran status, and current household composition. A number of additional questions were added in 2003, including questions on prior marijuana and cigarette use, additional questions on drug treatment, adult mental health services, and social environment.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2003) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2003-nid13569",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2003-nid13569"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2003-nid13569",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -123548,61 +123561,29 @@
                 "substance abuse treatment",
                 "tranquilizers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2003-0",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2003-nid13569",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) measures the<br />\nprevalence and correlates of drug use in the United States. The<br />\nsurveys are designed to provide quarterly, as well as annual,<br />\nestimates. Information is provided on the use of illicit drugs,<br />\nalcohol, and tobacco among members of United States households aged 12<br />\nand older. Questions included age at first use as well as lifetime,<br />\nannual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2003 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, gang involvement,<br />\ndrug use by friends, social support, extracurricular activities,<br />\nexposure to substance abuse prevention and education programs, and<br />\nperceived adult attitudes toward drug use and activities such as<br />\nschool work. Several measures focused on prevention related themes in<br />\nthis section. Also retained were questions on mental health and access<br />\nto care, perceived risk of using drugs, perceived availability of<br />\ndrugs, driving and personal behavior, and cigar smoking. Questions on<br />\nthe tobacco brand used most often were introduced with the 1999 survey<br />\nand retained through the 2003 survey. Background information includes<br />\ngender, race, age, ethnicity, marital status, educational level, job<br />\nstatus, veteran status, and current household composition. A number of additional questions were added in 2003, including questions on prior marijuana and cigarette use, additional questions on drug treatment, adult mental health services, and social environment.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2003)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2003-nid13569",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2003) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2003-nid13569"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2003)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mmi4-8ajr",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "flu shot",
-                "immunization",
-                "prams",
-                "pregnant women"
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
-            "identifier": "https://data.cdc.gov/api/views/mmi4-8ajr",
             "description": "For more information about the Pregnancy Risk Assessment Monitoring System please visit http://www.cdc.gov/prams/. See http://www.cdc.gov/mmwr/preview/mmwrhtml/mm6107a1.htm?s_cid=mm6107a1_e for the MMWR article.",
-            "title": "State Specific Influenza Vaccination Coverage Among Women With Live Birth- PRAMS, 2009-10 Influenza Season",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123625,39 +123606,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mmi4-8ajr",
+            "issued": "2013-06-19",
+            "keyword": [
+                "flu shot",
+                "immunization",
+                "prams",
+                "pregnant women"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mmi4-8ajr",
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
                 "Pregnancy & Vaccination"
-            ]
+            ],
+            "title": "State Specific Influenza Vaccination Coverage Among Women With Live Birth- PRAMS, 2009-10 Influenza Season"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ryqa-f6tz",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2020-11-06",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "keyword": [
-                "drug acquisition cost",
-                "nadac"
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
-            "identifier": "e3af839d-8175-5be0-b94e-4a302ed7a035",
             "description": "The tables below display new National Average Drug Acquisition Cost (NADAC) rates, sorted by Drug Product and Date. The drug products listed have not had a NADAC rate in the past.",
-            "title": "First Time NADAC Rates",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123666,42 +123650,39 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "e3af839d-8175-5be0-b94e-4a302ed7a035",
+            "issued": "2020-11-06",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/ryqa-f6tz",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2025-01-07",
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
+            "title": "First Time NADAC Rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/nfn2-3v66",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nfn2-3v66",
             "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Combine Report lists new Entry Combinations.  These are cases where a new, precoordinated Descriptor has been created to replace an existing Descriptor / Qualifier combination.  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
-            "title": "MeSH 2025 Update - Combine Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123724,38 +123705,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nfn2-3v66",
+            "issued": "2023-12-14",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/nfn2-3v66",
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
+            "title": "MeSH 2025 Update - Combine Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hp6w-4ap6",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-06-08",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "youth risk behavior risk surveillance school-based surveillance"
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
-            "identifier": "https://data.cdc.gov/api/views/hp6w-4ap6",
             "description": "The Youth Risk Behavior Surveillance System (YRBSS) monitors six types of health-risk behaviors that contribute to the leading causes of death and disability among youth and adults. This file contains state-level results for 13 tobacco-use variables by sex and grade for 2013.",
-            "title": "YRBS State Tobacco Variables  2013 - v2",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123778,35 +123762,35 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/hp6w-4ap6",
+            "issued": "2015-06-08",
+            "keyword": [
+                "youth risk behavior risk surveillance school-based surveillance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hp6w-4ap6",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-08-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "YRBS State Tobacco Variables  2013 - v2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/rzmt-rapu",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
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
-            "identifier": "13a06cdb-6bbb-4f86-bba7-9d6f3db41090",
             "description": "Medicaid Enterprise System Datatable",
-            "title": "Medicaid Enterprise System Datatable",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123814,42 +123798,35 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "13a06cdb-6bbb-4f86-bba7-9d6f3db41090",
+            "issued": "2025-01-18",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/rzmt-rapu",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Medicaid Enterprise System Datatable"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -123872,43 +123849,46 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Hepatitis (viral, acute, by type) A & B"
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
-            "identifier": "https://data.cdc.gov/api/views/n2zz-25mk",
             "description": "\u2022 Monthly Cumulative Percent of Adults 75 Years and Older Who Received 1+ RSV Vaccination Doses by Jurisdiction, United States. \n\u2022 Respiratory Syncytial Virus (RSV) vaccination coverage for adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group (https://www.cdc.gov/iis/about/).",
-            "title": "Monthly Cumulative Number and Percent of Adults 75 Years and Older Who Received 1+ RSV Vaccination Doses by Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123931,49 +123911,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/n2zz-25mk",
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
+            "title": "Monthly Cumulative Number and Percent of Adults 75 Years and Older Who Received 1+ RSV Vaccination Doses by Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-12-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
-            "modified": "2024-05-24",
-            "references": [
-                "Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
-            ],
-            "keyword": [
-                "flu",
-                "flu vaccination",
-                "influenza"
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
-            "identifier": "https://data.cdc.gov/api/views/g57i-yx3r",
             "description": "Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States \n\n\u2022\tInfluenza vaccination coverage among Medicare fee-for-service beneficiaries aged \u226565 years is assessed using data files from the Medicare Fee-For-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS). \n\n\u2022\tWeekly influenza vaccination coverage estimates were calculated using Kaplan-Meier survival analysis, based on beneficiaries enrolled as of August 1, 2019 and followed through May 31, 2020 for 2019-20 flu season; and enrolled as of August 1, 2020 and followed through May 31, 2021 for 2020-21 flu season; and enrolled as of Aug 1, 2021 and followed through May 28, 2022 for the 2021-22 flu season. \n\n\u2022\tAdditional information about data source is available https://www2.ccwdata.org/web/guest/home/.",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -123996,53 +123975,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/g57i-yx3r",
+            "issued": "2021-12-10",
+            "keyword": [
+                "flu",
+                "flu vaccination",
+                "influenza"
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
+                "Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
+            ],
+            "spatial": "United States",
+            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-premium-reports/cms-program-statistics-medicare-premiums",
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
-                "beneficiary costs",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/22c117c2-c04f-4078-9b7d-782167c8f0bb/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Premium tables provide information on counts of Medicare Part A (Hospital Insurance)\u00a0and Part B (Medical Insurance) total premium, standard base premium, reduced base premium, and penalty beneficiaries. In addition, these tables include premium amounts and penalty amounts. For the Part B premium tables, information on Income Related Monthly Adjustment Amount (IRMAA) beneficiaries, IRMAA amounts, Managed Care Reduction beneficiaries and Managed Care Reduction amounts are also included.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR PREMIUMS 1. Medicare Premiums: \u00a0Medicare Part A Premium Beneficiaries and Amounts, Yearly Trend\n\tMDCR PREMIUMS 2. Medicare Premiums: \u00a0Medicare Part A Premium Beneficiaries and Amounts by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR PREMIUMS 3. Medicare Premiums: \u00a0Medicare Part A Premium Beneficiaries and Amounts, by Area of Residence\n\tMDCR PREMIUMS 4. Medicare Premiums: \u00a0Medicare Part B Premium Beneficiaries and Amounts, Yearly Trend\n\tMDCR PREMIUMS 5. Medicare Premiums: \u00a0Medicare Part B Premium Beneficiaries and Amounts by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR PREMIUMS 6. Medicare Premiums: \u00a0Medicare Part B Premium Beneficiaries and Amounts, by Area of Residence",
-            "title": "CMS Program Statistics - Medicare Premiums",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -124099,26 +124076,62 @@
                     "title": "CMS Program Statistics - Medicare Premiums : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/22c117c2-c04f-4078-9b7d-782167c8f0bb/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "beneficiary costs",
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-premium-reports/cms-program-statistics-medicare-premiums",
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
+            "title": "CMS Program Statistics - Medicare Premiums"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-violent-death-reporting-system-nvdrs",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "nvrds@cdc.gov",
+                "hasEmail": "mailto:nvrds@cdc.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The National Violent Death Reporting System (NVDRS) provides states and communities with a clearer understanding of violent deaths to guide local decisions about efforts to prevent violence and helps them track progress over time.</p>\n<p>To stop violent deaths, we must first understand all the facts. Created in 2002, the NVDRS is a surveillance system that pulls together data on violent deaths in 18 states (see map below), including information about homicides, such as homicides perpetrated by a intimate partner (e.g., boyfriend, girlfriend, wife, husband), child maltreatment (or child abuse) fatalities, suicides, deaths where individuals are killed by law enforcement in the line of duty, unintentional firearm injury deaths, and deaths of undetermined intent.</p>\n<p>These data are supported by WISQARS, an interactive query system that provides data on injury deaths, violent deaths, and nonfatal injuries.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/injury/wisqars/",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "a4b95d02-096c-47a6-9334-9e0088322ece",
             "issued": "2014-04-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "community health",
                 "health care providers",
@@ -124130,78 +124143,43 @@
                 "violent deaths",
                 "ypll"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "nvrds@cdc.gov",
-                "hasEmail": "mailto:nvrds@cdc.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-violent-death-reporting-system-nvdrs",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:100"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "a4b95d02-096c-47a6-9334-9e0088322ece",
-            "description": "<p>The National Violent Death Reporting System (NVDRS) provides states and communities with a clearer understanding of violent deaths to guide local decisions about efforts to prevent violence and helps them track progress over time.</p>\n<p>To stop violent deaths, we must first understand all the facts. Created in 2002, the NVDRS is a surveillance system that pulls together data on violent deaths in 18 states (see map below), including information about homicides, such as homicides perpetrated by a intimate partner (e.g., boyfriend, girlfriend, wife, husband), child maltreatment (or child abuse) fatalities, suicides, deaths where individuals are killed by law enforcement in the line of duty, unintentional firearm injury deaths, and deaths of undetermined intent.</p>\n<p>These data are supported by WISQARS, an interactive query system that provides data on injury deaths, violent deaths, and nonfatal injuries.</p>",
-            "title": "National Violent Death Reporting System (NVDRS)",
-            "programCode": [
-                "009:100"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cdc.gov/injury/wisqars/",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Community",
                 "Health"
-            ]
+            ],
+            "title": "National Violent Death Reporting System (NVDRS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/program-integrity-market-saturation-by-type-of-service/market-saturation-utilization-core-based-statistical-areas",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2023-01-01/2023-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
-            "references": [
-                "https://data.cms.gov/resources/market-saturation-utilization-core-based-statistical-areas-methodology"
-            ],
-            "keyword": [
-                "fraud waste & abuse prevention",
-                "health care use & payments",
-                "medicare",
-                "original medicare",
-                "rural-urban",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/9b0e7798-d945-48fc-9861-d38bb5083a74/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/market-saturation-utilization-core-based-statistical-area-data-dictionary",
             "description": "The Market Saturation and Utilization Core-Based Statistical Areas (CBSA) dataset provides monitoring of market saturation as a means to help prevent potential fraud, waste, and abuse (FWA). CBSAs are geographical delineations that are Census Bureau-defined urban clusters of at least 10,000 people. Market saturation, in the present context, refers to the density of providers of a particular service within a defined geographic area relative to the number of beneficiaries receiving that service in the area. The data can be used to reveal the degree to which use of a service is related to the number of providers servicing a geographic region. There are also a number of secondary research uses for these data, but one objective of making these data public is to assist health care providers in making informed decisions about their service locations and the beneficiary population they serve.\n\nThe interactive dataset can be filtered and analyzed on the site or downloaded in Excel format.",
-            "title": "Market Saturation & Utilization Core-Based Statistical Areas",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9b0e7798-d945-48fc-9861-d38bb5083a74/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9b0e7798-d945-48fc-9861-d38bb5083a74/data",
+                    "mediaType": "text/html",
                     "title": "Market Saturation & Utilization Core-Based Statistical Areas : 2023-12-04"
                 },
                 {
@@ -124217,26 +124195,61 @@
                     "title": "Market Saturation & Utilization Core-Based Statistical Areas : 2023-12-04"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/market-saturation-utilization-core-based-statistical-area-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9b0e7798-d945-48fc-9861-d38bb5083a74/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "fraud waste & abuse prevention",
+                "health care use & payments",
+                "medicare",
+                "original medicare",
+                "rural-urban",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/program-integrity-market-saturation-by-type-of-service/market-saturation-utilization-core-based-statistical-areas",
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
+                "https://data.cms.gov/resources/market-saturation-utilization-core-based-statistical-areas-methodology"
+            ],
+            "temporal": "2023-01-01/2023-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Market Saturation & Utilization Core-Based Statistical Areas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2014",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Behavioral Health Services (I-BHS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2014) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2014-nid13605",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2014-nid13605"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2014-nid13605",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -124249,109 +124262,76 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2014",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2014-nid13605",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Behavioral Health Services (I-BHS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2014)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2014-nid13605",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2014) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2014-nid13605"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2014)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/s3ks-nh9r",
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
-            "identifier": "67ed2b07-ecd9-5506-84a7-b5613ae185c9",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure_value.csv",
-                    "description": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "67ed2b07-ecd9-5506-84a7-b5613ae185c9",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/s3ks-nh9r",
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
+            "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/s3n2-fbxq",
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
-                "mental health condition",
-                "physical health condition"
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
-            "identifier": "7db0e932-5275-4c3c-b4b6-8dc5f1520c3b",
             "description": "This table presents beneficiaries who received a service for a physical health condition among beneficiaries who received a service for a mental health condition, by physical health condition, 2017-2021.\r\n\r\nSome states have serious data quality issues, making the data unusable for identifying this population. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional, Gender, Age, Zip code, Race and ethnicity, Eligibility group code, Enrollment in CMC Plans. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Beneficiaries receiving a physical hlth serv among beneficiaries receiving a mental hlth serv, by physical hlth cond, 2017-2021",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -124360,49 +124340,44 @@
                     "title": "Beneficiaries receiving a physical hlth serv among beneficiaries receiving a mental hlth serv, by physical hlth cond, 2017-2021"
                 }
             ],
+            "identifier": "7db0e932-5275-4c3c-b4b6-8dc5f1520c3b",
+            "issued": "2023-03-28",
+            "keyword": [
+                "behavioral health care",
+                "chip",
+                "integrated care",
+                "medicaid",
+                "mental health condition",
+                "physical health condition"
+            ],
+            "landingPage": "https://healthdata.gov/d/s3n2-fbxq",
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
+            "title": "Beneficiaries receiving a physical hlth serv among beneficiaries receiving a mental hlth serv, by physical hlth cond, 2017-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rh2h-3yt2",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-12-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13/2023-05-12",
-            "modified": "2023-05-12",
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
-            "identifier": "https://data.cdc.gov/api/views/rh2h-3yt2",
             "description": "Overall\u00a0Trends in Number of COVID-19 Vaccinations in the US at\u00a0national\u00a0and jurisdictional levels. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u00a0",
-            "title": "COVID-19 Vaccination Trends in the United States,National and Jurisdictional",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -124425,48 +124400,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/rh2h-3yt2",
+            "issued": "2022-12-01",
+            "keyword": [
+                "administration",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "report date",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rh2h-3yt2",
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
+            "title": "COVID-19 Vaccination Trends in the United States,National and Jurisdictional"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -124489,50 +124465,55 @@
                     "mediaType": "application/xml"
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-22",
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
+            "title": "Vaccination Coverage among Adults (18+ Years)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-discarded-drug-units",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-01-21",
-            "temporal": "2022-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-14",
-            "references": [
-                "https://data.cms.gov/resources/medicare-part-b-discarded-drug-units-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/09fd71b8-eb3e-45af-a01e-f8ab5a190e84/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-part-b-discarded-drug-units-data-dictionary",
             "description": "The Medicare Part B Discarded Drug Units dataset provides spending information on claims for Medicare Part B drugs that were identified as having discarded amounts of a drug. As of January 1, 2017, the Centers for Medicare & Medicaid Services (CMS) requires all physicians, hospitals, and other providers submitting claims for Medicare Part B drugs to report any discarded amount of a single use vial or other single use package drug on its claim for payment. With the passage of the Infrastructure Investment and Jobs Act in November 2021, manufacturers must pay a refund to Medicare for discarded amounts above a specified threshold effective for drugs furnished beginning with January 1, 2023.",
-            "title": "Medicare Part B Discarded Drug Units",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/09fd71b8-eb3e-45af-a01e-f8ab5a190e84/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/09fd71b8-eb3e-45af-a01e-f8ab5a190e84/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Part B Discarded Drug Units : 2022-01-01"
                 },
                 {
@@ -124548,52 +124529,47 @@
                     "title": "Medicare Part B Discarded Drug Units : 2022-01-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-part-b-discarded-drug-units-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/09fd71b8-eb3e-45af-a01e-f8ab5a190e84/data-viewer",
+            "issued": "2022-01-21",
+            "keyword": [
+                "drugs",
+                "medicare",
+                "original medicare"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-discarded-drug-units",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-03-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-part-b-discarded-drug-units-methodology"
+            ],
+            "temporal": "2022-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Part B Discarded Drug Units"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/247v-f7n9",
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
-            "identifier": "https://data.cdc.gov/api/views/247v-f7n9",
             "description": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 The pertussis case definition was modified by CSTE effective January 1, 2020. Criteria were modified increasing sensitivity for case ascertainment such that case counts may increase.",
-            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -124616,84 +124592,93 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/247v-f7n9",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "paralytic",
+                "pertussis",
+                "plague",
+                "poliomyelitis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/247v-f7n9",
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
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/s4kg-z8sq",
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
-            "identifier": "4000fb2c-f5ac-5599-81ed-9443b7135416",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard TAG v0.3.0-1 (etl_test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.0-1/TAG.csv",
-                    "description": "Scorecard TAG v0.3.0-1 (etl_test)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard TAG v0.3.0-1 (etl_test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.0-1/TAG.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard TAG v0.3.0-1 (etl_test)"
                 }
             ],
+            "identifier": "4000fb2c-f5ac-5599-81ed-9443b7135416",
+            "issued": "2023-06-01",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/s4kg-z8sq",
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
+            "title": "Scorecard TAG v0.3.0-1 (etl_test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/s4w6-ihsn",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-03-25",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-21",
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
-            "identifier": "c6f03fab-fe07-4ba3-bc33-212ae0e7cdc8",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-03-14 to 2022-03-20",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -124701,38 +124686,36 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "c6f03fab-fe07-4ba3-bc33-212ae0e7cdc8",
+            "issued": "2022-03-25",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/s4w6-ihsn",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-03-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-03-14 to 2022-03-20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135778.htm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "cder",
-                "establishments",
-                "registration"
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
-            "identifier": "fa27e8ba-4b3c-4a2d-bb29-19eecffa0847",
             "description": "The Drug Establishments Current Registration Site (DECRS) is a database of current information submitted by drug firms to register establishments (facilities) which manufacture, prepare, propagate, compound or process drugs that are commercially distributed in the U.S. or offered for import to the U.S.",
-            "title": "Drug Establishments Current Registration Site",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -124740,77 +124723,70 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "fa27e8ba-4b3c-4a2d-bb29-19eecffa0847",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder",
+                "establishments",
+                "registration"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135778.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P3M"
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Drug Establishments Current Registration Site"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://rdocdb.nimh.nih.gov/",
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
                 "fn": "Farber, Greg",
                 "hasEmail": "mailto:farberg@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "951435a3-1699-43cc-a00b-f138c892058b",
+            "dataQuality": true,
             "description": "<p>RDoCdb supports the Research Domain Criteria Initiative (RDoC), which calls for the development, for research purposes, of new ways of classifying psychopathology based on dimensions of observable behavior and neurobiological measures by providing the research community a data repository for the sharing of research data related to this initiative.</p>",
-            "title": "RDoCdb",
+            "identifier": "951435a3-1699-43cc-a00b-f138c892058b",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://rdocdb.nimh.nih.gov/",
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
+            "title": "RDoCdb"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4qb4-rsd8",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
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
-            "identifier": "https://data.cdc.gov/api/views/4qb4-rsd8",
             "description": "NNDSS - Table II. Rubella to Salmonellosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. \r\n\r\n * Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.\r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.",
-            "title": "NNDSS - Table II. Rubella to Salmonellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -124833,49 +124809,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4qb4-rsd8",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "congenital syndrome",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "salmonellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4qb4-rsd8",
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
+            "title": "NNDSS - Table II. Rubella to Salmonellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/ehr-products-used-meaningful-use-attestation",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/health-care-professional-health-it-developers",
-                "https://www.healthit.gov/data/quickstats/hospital-health-it-developers",
-                "https://www.healthit.gov/data/apps/ehr-vendors-reported-hospitals-demonstrating-meaningful-use",
-                "https://www.healthit.gov/data/apps/ehr-vendors-reported-office-based-providers-demonstrating-meaningful-use"
-            ],
-            "keyword": [
-                "certified",
-                "ehrs",
-                "electronic health records",
-                "health information technology",
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
-            "identifier": "11c83d84-83c1-4310-963f-2134f953943b",
+            "describedBy": "https://www.healthit.gov/data/datasets/ehr-products-used-meaningful-use-attestation",
             "description": "The Medicare Electronic Health Record (EHR) Incentive Program provides incentives to eligible clinicians and hospitals to adopt electronic health records. This dataset combines meaningful use attestations from the Medicare EHR Incentive Program and certified health IT product data from the ONC Certified Health IT Product List (CHPL) to identify the unique vendors, products, and product types of each certified health IT product used to attest to meaningful use. The dataset also includes important provider-specific data, related to the provider&apos;s participation and status in the program, unique provider identifiers, and other characteristics unique to each provider, like geography and provider type.",
-            "title": "EHR Products Used for Meaningful Use Attestation",
-            "programCode": [
-                "009:110"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -124884,36 +124858,45 @@
                     "title": "MU_REPORT.csv"
                 }
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/ehr-products-used-meaningful-use-attestation"
+            "identifier": "11c83d84-83c1-4310-963f-2134f953943b",
+            "issued": "2023-10-03",
+            "keyword": [
+                "certified",
+                "ehrs",
+                "electronic health records",
+                "health information technology",
+                "health it",
+                "interoperability"
+            ],
+            "landingPage": "https://www.healthit.gov/data/datasets/ehr-products-used-meaningful-use-attestation",
+            "modified": "2019-01-01",
+            "programCode": [
+                "009:110"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "references": [
+                "https://www.healthit.gov/data/quickstats/health-care-professional-health-it-developers",
+                "https://www.healthit.gov/data/quickstats/hospital-health-it-developers",
+                "https://www.healthit.gov/data/apps/ehr-vendors-reported-hospitals-demonstrating-meaningful-use",
+                "https://www.healthit.gov/data/apps/ehr-vendors-reported-office-based-providers-demonstrating-meaningful-use"
+            ],
+            "title": "EHR Products Used for Meaningful Use Attestation"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -124936,20 +124919,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8bda-nhxv",
+            "issued": "2021-06-23",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8bda-nhxv",
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
+            "title": "Active Bacterial Core surveillance (ABCs) Neisseria meningitidis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2008",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2008) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2008-nid13576",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2008-nid13576"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2008-nid13576",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -124962,58 +124975,30 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2008",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2008-nid13576",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2008)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2008-nid13576",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2008) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2008-nid13576"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2008)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/s99n-4m79",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-05-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-30",
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
-            "identifier": "46732f54-2971-48e2-b2ae-02d902ca6d33",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-22-to-2023-05-28",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -125022,37 +125007,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-22-to-2023-05-28"
                 }
             ],
+            "identifier": "46732f54-2971-48e2-b2ae-02d902ca6d33",
+            "issued": "2023-05-31",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/s99n-4m79",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-05-30",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-22-to-2023-05-28"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -125075,35 +125058,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9w38-t35p",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9w38-t35p",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 6 - Dallas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/h98p-htn6",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory, Research Pathology and Physiology Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/h98p-htn6",
             "description": "As more women join the skilled-trade workforce, the effects of workplace exposures on pregnancy need to be explored. This study aimed to identify the effects of mild-steel (MS) and stainless-steel (SS) welding fume exposures on first-trimester placental trophoblast cells, using the HTR-8/SVneo cell line. MS is primarily composed of Iron (Fe) and Manganese (Mn), while SS also contains chromium (Cr) and nickel (Ni). We found that all three welding fumes had significant effects on cellular viability, and also caused increases in free radical production, while negatively affecting their invasive capabilities. MS was the only sample to cause an increase in production of the pro-inflammatory cytokines IL-6 and IL-8. Our results show that welding fume exposure is in fact cytotoxic to trophoblasts, and understanding how these occupational exposures could impact maternal and fetal health is necessary. Identifying how the varying combinations of heavy metals and other materials present in MS and SS welding fumes, along",
-            "title": "Effects of Welding Fume Exposure on Human Placental Cells",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -125111,94 +125098,81 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h98p-htn6",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/h98p-htn6",
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
+            "title": "Effects of Welding Fume Exposure on Human Placental Cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/s9cg-pwbt",
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
-            "identifier": "3470acd5-0658-5971-bed7-80019b8a8ee2",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt state v2.10.6 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/state.csv",
-                    "description": "CoreSEt state v2.10.6 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt state v2.10.6 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt state v2.10.6 (coreset-etl-test)"
                 }
             ],
+            "identifier": "3470acd5-0658-5971-bed7-80019b8a8ee2",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/s9cg-pwbt",
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
+            "title": "CoreSEt state v2.10.6 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "keyword": [
-                "administration and management",
-                "best practices",
-                "best practices for comprehensive tobacco control programs",
-                "centers for disease control and prevention",
-                "cessation intervention",
-                "health communication interventions",
-                "office on smoking and health",
-                "osh",
-                "state and community interventions",
-                "surveillance and evaluation",
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
-            "identifier": "https://data.cdc.gov/api/views/vm4m-idi8",
             "description": "2014. Centers for Disease Control and Prevention (CDC). Best Practices for Comprehensive Tobacco Control Programs. Funding. CDC's Best Practices for Comprehensive Tobacco Control Programs is an evidence-based guide to help states plan and establish effective tobacco control programs to prevent and reduce tobacco use.  These data update Best Practices for Comprehensive Tobacco Control Programs\u20142007.  Data are reported at total and per capita funding levels. Data include recommended and minimum total funding levels for state programs, in addition to funding breakdowns by intervention areas such as: State and Community Interventions, Mass-Reach Health Communication Interventions, Cessation Interventions, Surveillance and Evaluation, and Infrastructure, Administration, and Management.",
-            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2014",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -125221,80 +125195,88 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vm4m-idi8",
+            "issued": "2023-07-14",
+            "keyword": [
+                "administration and management",
+                "best practices",
+                "best practices for comprehensive tobacco control programs",
+                "centers for disease control and prevention",
+                "cessation intervention",
+                "health communication interventions",
+                "office on smoking and health",
+                "osh",
+                "state and community interventions",
+                "surveillance and evaluation",
+                "tobacco"
+            ],
+            "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
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
                 "Funding"
-            ]
+            ],
+            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "temporal": "1992-01-01/1996-07-31",
-            "@type": "dcat:Dataset",
-            "modified": "1996-07-31",
-            "references": [
-                "http://www.fda.gov/MedicalDevices/Safety/ReportaProblem/ucm124073.htm"
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
-            "identifier": "290bc7d6-538c-4889-823f-2ec60b6d3b6a",
             "description": "This database allows you to search the CDRH's database information on medical devices which may have malfunctioned or caused a death or serious injury during the years 1992 through 1996.",
-            "title": "MDR (Medical Device Reporting)",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "290bc7d6-538c-4889-823f-2ec60b6d3b6a",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "1996-07-31",
             "programCode": [
                 "009:005"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
-                    "mediaType": "text/html"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/MedicalDevices/Safety/ReportaProblem/ucm124073.htm"
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "temporal": "1992-01-01/1996-07-31",
+            "title": "MDR (Medical Device Reporting)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/saz5-9hgg",
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
-            "identifier": "https://data.cdc.gov/api/views/saz5-9hgg",
             "description": "New weekly allocations of doses are posted every Tuesday.  Beginning the following Thursday, states can begin ordering doses from that week\u2019s new allocation of 1st doses.  Beginning two weeks (Pfizer) or three weeks (Moderna) from the following Sunday, states can begin ordering doses from that week\u2019s new allocation of 2nd doses. After doses are ordered by states, shipments begin the following Monday. The entire order may not arrive in one shipment or on one day, but over the course of the week.\n\nSecond doses are opened up for orders on Sundays, at the appropriate interval two or three weeks later according to the manufacturer\u2019s label, with shipments occurring after jurisdictions place orders. \n\nShipments of an FDA-authorized safe and effective COVID-19 vaccine continue to arrive at sites across America. Vaccinations began on December 14, 2020. \n\nhttps://www.hhs.gov/coronavirus/covid-19-vaccines/index.html\n\nModerna Vaccine Data - https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Distribution-Allocations-by-Juris/b7pe-5nws\n\nJanssen Vaccine Data - https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Distribution-Allocations-by-Juris/w9zu-fywh",
-            "title": "COVID-19 Vaccine Distribution Allocations by Jurisdiction - Pfizer",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -125317,39 +125299,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/saz5-9hgg",
+            "issued": "2021-02-24",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/saz5-9hgg",
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
+            "title": "COVID-19 Vaccine Distribution Allocations by Jurisdiction - Pfizer"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -125372,50 +125355,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8i5t-42wz",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/8i5t-42wz",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 8 - Denver"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-02-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2021-01-30",
-            "modified": "2023-04-03",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "education",
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
-            "identifier": "https://data.cdc.gov/api/views/i6ej-9eac",
             "description": "Provisional counts of deaths in the United States by race and educational attainment. The dataset includes cumulative provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
-            "title": "AH Provisional COVID-19 Deaths by Race and Educational Attainment",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -125438,37 +125411,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/i6ej-9eac",
+            "issued": "2021-02-01",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "education",
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
+            "modified": "2023-04-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2020-01-01/2021-01-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Race and Educational Attainment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/bwwd-cuna",
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
-            "identifier": "https://data.cdc.gov/api/views/bwwd-cuna",
             "description": "Aspergillus versicolor is ubiquitous in the environment and is particularly abundant in damp indoor spaces. Exposure to Aspergillus species, as well as other environmental fungi, has been linked to adverse health outcomes including asthma, allergy, and even local or disseminated infection. However, the pulmonary immunological mechanisms associated with repeated exposure to A. versicolor have remained relatively uncharacterized. Here, A. versicolor was cultured and desiccated on rice, then placed in an acoustical generator system to achieve aerosolization. Mice were challenged with titrated doses of aerosolized conidia to examine deposition, lymphoproliferative properties, and then the immunotoxicological response to repeated inhalation exposures. The necessary dose to induce lymphoproliferation, but not infection-like pathology, was identified. Further, it was determined that the dose was able to initiate localized immune responses. The data presented in this study demonstrate an optimized and reproducible method for delivering A. versicolor conidia to rodents via nose-only inhalation. Additionally, the feasibility of a long-term repeated exposure study was established.  This experimental protocol can be used in future studies to investigate physiological effects of repeated pulmonary exposure to fungal conidia utilizing a practical and relevant mode of delivery. In total, these data constitute an important foundation for subsequent research in the field.",
-            "title": "Optimization of Aspergillus versicolor culture and aerosolization in a murine model of inhalational fungal exposure",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -125476,42 +125463,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bwwd-cuna",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/bwwd-cuna",
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
+            "title": "Optimization of Aspergillus versicolor culture and aerosolization in a murine model of inhalational fungal exposure"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -125534,43 +125515,45 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
             "theme": [
                 "Foodborne",
                 "Waterborne",
                 "and Related Diseases"
-            ]
+            ],
+            "title": "BEAM Dashboard - Serotypes of concern: Burden and Trajectory"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -125593,40 +125576,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/a37y-w96i",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/a37y-w96i",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 8 - Denver"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/scme-3d32",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2014-11-07",
-            "temporal": "2018-01-01T00:00:00+00:00/2019-01-01T00:00:00+00:00",
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
-            "identifier": "8de1b213-73c5-552b-b84e-ac795f34d056",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2018",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -125635,42 +125618,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "8de1b213-73c5-552b-b84e-ac795f34d056",
+            "issued": "2014-11-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/scme-3d32",
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
+            "temporal": "2018-01-01T00:00:00+00:00/2019-01-01T00:00:00+00:00",
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2018"
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
@@ -125693,45 +125675,43 @@
                     "mediaType": "application/xml"
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
                 "Nutrition",
                 "Physical Activity",
                 "and Obesity"
-            ]
+            ],
+            "title": "National Community Based Survey of Supports for Healthy Eating and Active Living  (CBS HEAL)"
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
-            "identifier": "https://data.cdc.gov/api/views/b6ny-6cd5",
             "description": "\u2022 Monthly Cumulative Percent of Persons Who Received \u22651 Influenza Vaccination Doses and Comparison Between 2024-25 and Two Previous Seasons, by Jurisdiction, United States.\n\n\u2022 Influenza (flu) vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly, in aggregate, by age group (https://www.cdc.gov/iis/about/).",
-            "title": "Monthly Cumulative Number and Percent of Who Received \u22651 Influenza Vaccination Doses and Comparison Between 2024-25 and Two Previous Seasons, by Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -125754,25 +125734,58 @@
                     "mediaType": "application/xml"
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
+            "title": "Monthly Cumulative Number and Percent of Who Received \u22651 Influenza Vaccination Doses and Comparison Between 2024-25 and Two Previous Seasons, by Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2010-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2010 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2010) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2010-nid13572",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2010-nid13572"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2010-nid13572",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -125813,70 +125826,30 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2010-0",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2010-nid13572",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2010 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2010)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2010-nid13572",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2010) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2010-nid13572"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2010)"
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
-            "identifier": "https://data.cdc.gov/api/views/pqpp-u99h",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
             "description": "This dataset contains model-based county-level estimates for the PLACES 2021 release. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 4 chronic disease-related health risk behaviors, 13 health outcomes, 3 health status, and 9 on using preventive services. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2019 or 2018 county population estimate data, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, County Data 2021 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -125899,54 +125872,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
+            "identifier": "https://data.cdc.gov/api/views/pqpp-u99h",
+            "issued": "2022-10-11",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "county",
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
+            "title": "PLACES: Local Data for Better Health, County Data 2021 release"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -125969,90 +125939,100 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/sdsu-w7mh",
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
-            "identifier": "ea9b7db3-db71-4663-b4e1-67e11d1d4fcc",
             "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by major eligibility group (children, adult expansion group, adult, aged, persons with disabilities, or COVID newly-eligible).\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern  based on DQ Atlas thresholds for the topic Eligibility Group Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Major Eligibility Group Information for Medicaid and CHIP Beneficiaries by Month",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/MajorEligibilityGroup-montly.csv",
-                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by major eligibility group (children, adult expansion group, adult, aged, persons with disabilities, or COVID newly-eligible).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern  based on DQ Atlas thresholds for the topic Eligibility Group Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by major eligibility group (children, adult expansion group, adult, aged, persons with disabilities, or COVID newly-eligible).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern  based on DQ Atlas thresholds for the topic Eligibility Group Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/MajorEligibilityGroup-montly.csv",
+                    "mediaType": "text/csv",
                     "title": "Major Eligibility Group Information for Medicaid and CHIP Beneficiaries by Month"
                 }
             ],
+            "identifier": "ea9b7db3-db71-4663-b4e1-67e11d1d4fcc",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "major eligibility group",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/sdsu-w7mh",
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
+            "title": "Major Eligibility Group Information for Medicaid and CHIP Beneficiaries by Month"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ii.nlm.nih.gov/MTI/index.shtml",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "history of medicine",
-                "medical informatics",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ivwm-qssp",
             "description": "A system for producing indexing recommendations to assist in the indexing process at NLM.  Currently provides indexing recommendations to more than 100 journals based on the NLM Medical Subject Headings (MeSH) vocabulary.\n\nMTI is the main product of the Indexing Initiative project and has been providing indexing recommendations based on the Medical Subject Headings (MeSH\u00ae) vocabulary since 2002. In 2011, NLM expanded MTI's role by designating it as the first-line indexer (MTIFL) for a few journals; today the MTIFL workflow includes over 350 journals and continues to increase. The close collaboration of the NLM Index Section, Lister Hill National Center for Biomedical Communications, and Office of Computer & Communications Systems continues to expand and refine the ability of MTI to provide assistance to the indexers.",
-            "title": "Medical Text Indexer (MTI)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126061,87 +126041,88 @@
                     "title": "Access NLM Medical Text Indexer (MTI)"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ivwm-qssp",
+            "issued": "2021-06-30",
+            "keyword": [
+                "api",
+                "history of medicine",
+                "medical informatics",
+                "terminologies",
+                "tools & utilities"
+            ],
+            "landingPage": "https://ii.nlm.nih.gov/MTI/index.shtml",
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
+            "title": "Medical Text Indexer (MTI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/se7n-wqxt",
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
-            "identifier": "4256aa88-c7ba-582e-aec6-f6f905c70cb3",
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
+            "identifier": "4256aa88-c7ba-582e-aec6-f6f905c70cb3",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/se7n-wqxt",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -126164,46 +126145,41 @@
                     "mediaType": "application/xml"
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
+            "title": "BRFSS Prevalence and Trends Data: Tobacco Use - Four Level Smoking Data for 1995-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kebt-3t25",
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
-            "identifier": "https://data.cdc.gov/api/views/kebt-3t25",
             "description": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126226,38 +126202,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kebt-3t25",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "paralytic",
+                "pertussis",
+                "plague",
+                "poliomyelitis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kebt-3t25",
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
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/seqp-2d8w",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2017-12-01",
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
-            "identifier": "52ed908b-0cb8-5dd2-846d-99d4af12b369",
             "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. Total Medicaid Enrollees represents an unduplicated count of all beneficiaries in FFS and any type of managed care, including Medicaid-only and Medicare-Medicaid (\"dual\") enrollees.\t\t\t\t\r\n2. Total Medicaid enrollment in Any Type of Managed Care represents an unduplicated count of beneficiaries enrolled in any Medicaid managed care program, including comprehensive MCOs, limited benefit MCOs, and PCCMs.\r\n3. The \u201cMedicaid Enrollment in Comprehensive Managed Care\u201d column represents an unduplicated count of Medicaid beneficiaries enrolled in a managed care plan that provides comprehensive benefits (acute, primary care, specialty, and any other), or PACE program. It excludes beneficiaries who are enrolled in a Financial Alignment Demonstration Medicare-Medicaid Plan as their only form of managed care.\t\t\t\r\n4. The \u201cMedicaid Enrollment in Comprehensive MCOs Under ACA Section VIII Expansion\u201d column is a subset of the total reported in column C and includes individuals who are enrolled in comprehensive MCOs and are low-income adults, with or without dependent children, eligible for Medicaid under ACA Section VIII.\r\n5. n/a\" indicates that a state or territory was either not able to report data or does not operate a managed care program.",
-            "title": "Managed Care Enrollment Summary",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126266,21 +126251,49 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "52ed908b-0cb8-5dd2-846d-99d4af12b369",
+            "issued": "2017-12-01",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/seqp-2d8w",
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
+            "title": "Managed Care Enrollment Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2013",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2013 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2013) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2013-nid13555",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2013-nid13555"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2013-nid13555",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -126321,62 +126334,30 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2013",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2013-nid13555",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2013 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2013)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2013-nid13555",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2013) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2013-nid13555"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2013)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/sfha-xqk6",
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
-            "identifier": "0ad77e97-5a72-46a0-ba74-37a159d100f7",
             "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2022 Individual Dental",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126384,35 +126365,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "0ad77e97-5a72-46a0-ba74-37a159d100f7",
+            "issued": "2022-08-10",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2022",
+                "qhp landscape",
+                "sadp"
+            ],
+            "landingPage": "https://healthdata.gov/d/sfha-xqk6",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2022 Individual Dental"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/sfsy-6enj",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-11-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-28",
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
-            "identifier": "5f23f199-d3cf-44a1-b39c-cd6e34af7a29",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 10-21-2024-to-10-27-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126420,41 +126404,35 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "5f23f199-d3cf-44a1-b39c-cd6e34af7a29",
+            "issued": "2024-11-02",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/sfsy-6enj",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-28",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 10-21-2024-to-10-27-2024"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -126477,54 +126455,53 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-milestones-and-updates",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2025-01-05/2025-01-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/resources/milestones-and-updates-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/4ce4157f-4e02-4188-b43a-2b21b7769b4e/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/milestones-and-updates-data-dictionary",
             "description": "The Innovation Center Milestones and Updates dataset contains a variety of contributions from CMS Innovation Center models, demonstrations, initiatives and programs. These resources include relevant milestones, dates, and changes to the status or parameters of a model, demonstration, or initiative.",
-            "title": "Innovation Center Milestones and Updates",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4ce4157f-4e02-4188-b43a-2b21b7769b4e/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4ce4157f-4e02-4188-b43a-2b21b7769b4e/data",
+                    "mediaType": "text/html",
                     "title": "Innovation Center Milestones and Updates : 2025-01-15"
                 },
                 {
@@ -126540,50 +126517,53 @@
                     "title": "Innovation Center Milestones and Updates : 2025-01-15"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/milestones-and-updates-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/4ce4157f-4e02-4188-b43a-2b21b7769b4e/data-viewer",
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
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-milestones-and-updates",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/milestones-and-updates-methodology"
+            ],
+            "temporal": "2025-01-05/2025-01-11",
             "theme": [
                 "Medicare",
                 "Children's Health Insurance Program"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Innovation Center Milestones and Updates"
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
-            "identifier": "https://data.cdc.gov/api/views/hj2x-85ya",
-            "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation - Preemption. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to summary state preemption of more stringent or differing local laws on smokefree indoor air, youth access and licensure.",
-            "title": "CDC STATE System Tobacco Legislation - Preemption Summary",
-            "programCode": [
-                "009:020"
-            ],
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Preemption-Su/hj2x-85ya",
+            "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation - Preemption. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to summary state preemption of more stringent or differing local laws on smokefree indoor air, youth access and licensure.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126606,82 +126586,89 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Preemption-Su/hj2x-85ya",
+            "identifier": "https://data.cdc.gov/api/views/hj2x-85ya",
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
             "theme": [
                 "Legislation"
-            ]
+            ],
+            "title": "CDC STATE System Tobacco Legislation - Preemption Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/shq4-bbik",
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
-            "identifier": "d1e8f0b9-7dbb-5840-974a-959a45bd100e",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard filters v2.12.1-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/filters.csv",
-                    "description": "Scorecard filters v2.12.1-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard filters v2.12.1-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard filters v2.12.1-test (local)"
                 }
             ],
+            "identifier": "d1e8f0b9-7dbb-5840-974a-959a45bd100e",
+            "issued": "2023-08-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/shq4-bbik",
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
+            "title": "Scorecard filters v2.12.1-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hcxx-dqtx",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Research, Toxicology and Molecular Biology Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hcxx-dqtx",
             "description": "Exposure to certain engineered nanomaterials (ENMs) causes chronic lesions like lung fibrosis and cancer as a result of unresolved inflammation. Elucidating how ENM-induced inflammation is resolved is necessary for better evaluation of the fibrogenic and tumorigenic potentials of ENMs. This study aimed to identify pro-resolving mechanisms by analyzing the inflammatory and fibrogenic responses to multi-walled carbon nanotubes (MWCNTs, Mitsui-7) and fullerenes (fullerene C60, C60F) in B6C3F1 mice. The findings reveal that MWCNTs at a low dose (40 \u00b5g/mouse) and C60F at a high dose (>480 mg/mouse) stimulated acute neutrophilic inflammation, which exhibited rapid initiation and extended resolution. The lesion in MWCNT-exposed mice progressed to fibrotic granulomas by day 28 post-exposure, whereas it remained as alveolar histiocytosis in C60F-exposed mice. The ENMs induced high levels of proinflammatory lipid mediators leukotriene B4 (LTB4) and prostaglandin E2 (PGE2) with peaks at day 1, and high levels of special",
-            "title": "Resolution of Pulmonary Inflammation Induced by Carbon Nanotubes and Fullerenes in Mice: Role of Macrophage Polarization",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126689,47 +126676,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hcxx-dqtx",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/hcxx-dqtx",
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
+            "title": "Resolution of Pulmonary Inflammation Induced by Carbon Nanotubes and Fullerenes in Mice: Role of Macrophage Polarization"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wff4-m3q3",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "age<5 years",
-                "confirmed",
-                "invasive pneumococcal disease",
-                "legionellosis",
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
-            "identifier": "https://data.cdc.gov/api/views/wff4-m3q3",
             "description": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 years, Confirmed to Legionellosis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
-            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, Age<5 years, Confirmed to Legionellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126752,38 +126727,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wff4-m3q3",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "age<5 years",
+                "confirmed",
+                "invasive pneumococcal disease",
+                "legionellosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/wff4-m3q3",
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
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, Age<5 years, Confirmed to Legionellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/iyx3-z4r8",
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
-            "identifier": "https://data.cdc.gov/api/views/iyx3-z4r8",
             "description": "",
-            "title": "Outbreak Data - Restaurant Grading",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126806,42 +126790,39 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/iyx3-z4r8",
+            "issued": "2022-10-17",
+            "keyword": [
+                "restaurant grading"
+            ],
+            "landingPage": "https://data.cdc.gov/d/iyx3-z4r8",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-10-27",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
             "theme": [
                 "Environmental Health & Toxicology"
-            ]
+            ],
+            "title": "Outbreak Data - Restaurant Grading"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4khb-4xch",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-23",
-            "keyword": [
-                "centers for disease control and prevention",
-                "environmental health",
-                "foodborne",
-                "outbreak"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "The National Environmental Assessment Reporting System (NEARS)",
                 "hasEmail": "mailto:nears@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4khb-4xch",
             "description": "Foodborne outbreak investigations often provide data for public health officials to determine how the environment contributed to the outbreak and on how to prevent future outbreaks. State and local health departments are responsible for investigating foodborne illness outbreaks in their jurisdictions and reporting the data to national-level surveillance systems, including information from the environmental assessment. This assessment is designed to describe how the environment contributed to the outbreak and identifies factors that contributed to the outbreak and environmental antecedents to the outbreak. Environmental antecedents, also referred to as root causes, are specific reasons that allow biological or chemical agents to contaminate, survive, or grow in food. From 2017 \u2013 2019, 24 jurisdictions reported 1,430 antecedents from 393 outbreaks to the National Environmental Assessments Reporting System. The most reported antecedents were lack of oversight of employees/enforcement of policies (89.1%), lack of training of employees on specific processes (74.0%), and lack of a food safety culture/attitude towards food safety (57.5%). These findings highlight the critical role that employees play in restaurant food safety and are heavily influenced by restaurant management, who can exercise active managerial control to manage these antecedents. Identifying antecedents during investigations is essential for understanding the outbreak\u2019s root cause and implementing sustainable corrective actions to stop the immediate outbreak and future outbreaks.",
-            "title": "Environmental Antecedents of Foodborne Illness Outbreaks",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126864,44 +126845,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4khb-4xch",
+            "issued": "2024-05-23",
+            "keyword": [
+                "centers for disease control and prevention",
+                "environmental health",
+                "foodborne",
+                "outbreak"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4khb-4xch",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-23",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Center for Environmental Health"
-            ]
+            ],
+            "title": "Environmental Antecedents of Foodborne Illness Outbreaks"
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
-            "identifier": "https://data.cdc.gov/api/views/ysd3-txwj",
             "description": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physical Medical Offices, Adults 18 Years and Older, United States \n\nArchived data are here: https://data.cdc.gov/resource/uxgd-cqqc\n\n- Estimated number of influenza vaccinations among adults 18 years and older is assessed through IQVIA (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, stores, and independent pharmacies) and physician medical offices.",
-            "title": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, by Flu Season and Age Group, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126924,40 +126903,48 @@
                     "mediaType": "application/xml"
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
+            "title": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, by Flu Season and Age Group, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4j6x-nm2a",
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
-            "identifier": "https://data.cdc.gov/api/views/4j6x-nm2a",
             "description": "The U.S. Food and Drug Administration (FDA) requires surgical masks (SMs) and surgical N95 respirators used in healthcare to meet certain fluid resistance and flammability levels. NIOSH\u2019s National Personal Protective Technology Laboratory (NPPTL) investigated the fluid penetration and flammability of respirators and other head/facial personal protective equipment to determine their efficacy in reducing healthcare workers\u2019 risk for occupational exposures to infectious microorganisms and injury due to accidental fires in surgical settings. The results from this study showed that FDA cleared SMs and surgical N95 respirators were resistant to synthetic blood penetration (Rengasamy et al. 2014) and met the flammability levels (Rengasamy et al. 2018) as expected. Seven out of eleven non-FDA cleared NIOSH-approved N95 filtering facepiece respirator models also passed the synthetic blood penetration and flammability tests. NPPTL tested five models of powered air-purifying respirator (PAPR) hoods and all models showed",
-            "title": "Projectile Fluid Penetration and Flammability of Respirators and other Head/Facial Personal Protective Equipment (FPFPPE)",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -126965,60 +126952,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4j6x-nm2a",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/4j6x-nm2a",
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
+            "title": "Projectile Fluid Penetration and Flammability of Respirators and other Head/Facial Personal Protective Equipment (FPFPPE)"
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
-                "https://chronicdata.cdc.gov/d/i54f-wv8z"
-            ],
-            "keyword": [
-                "behavioral",
-                "cigarette",
-                "cigarette use",
-                "current",
-                "frequent",
-                "office on smoking and health",
-                "osh",
-                "prevalence",
-                "risk",
-                "smokeless",
-                "smoker",
-                "smoking",
-                "smoking status",
-                "state system",
-                "surveillance",
-                "survey",
-                "tobacco",
-                "tobacco use",
-                "youth",
-                "yrbss"
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
-            "identifier": "https://data.cdc.gov/api/views/3596-ayf6",
+            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Youth-Risk-Behavioral-Surveillance-System-YRBSS-Da/3596-ayf6",
             "description": "1993, 1995, 1997, 1999, 2001, 2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. YRBSS Data. The YRBS is conducted biennially and collects data on a variety of youth risk behaviors including tobacco use. The YRBS uses a two-stage cluster sample design to produce representative samples of students in high schools (grades 9-12). The YRBS uses SUDAAN to calculate asymmetric confidence intervals based on the logit transformation. The logit transformation constrains confidence interval limits to vary between a lower limit of 0% and an upper limit of 100%. The data for the STATE System were extracted from YRBSS surveys from participating states. Tobacco topics include cigarette and e-cigarette use prevalence, cigarette and e-cigarette use frequency, and smokeless tobacco products.",
-            "title": "Youth Risk Behavioral Surveillance System (YRBSS) Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127041,46 +127004,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Youth-Risk-Behavioral-Surveillance-System-YRBSS-Da/3596-ayf6",
+            "identifier": "https://data.cdc.gov/api/views/3596-ayf6",
+            "issued": "2025-01-31",
+            "keyword": [
+                "behavioral",
+                "cigarette",
+                "cigarette use",
+                "current",
+                "frequent",
+                "office on smoking and health",
+                "osh",
+                "prevalence",
+                "risk",
+                "smokeless",
+                "smoker",
+                "smoking",
+                "smoking status",
+                "state system",
+                "surveillance",
+                "survey",
+                "tobacco",
+                "tobacco use",
+                "youth",
+                "yrbss"
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
+                "https://chronicdata.cdc.gov/d/i54f-wv8z"
+            ],
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "Youth Risk Behavioral Surveillance System (YRBSS) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/phwv-i65c",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/phwv-i65c",
             "description": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chancroid - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Data for Carbapenemase-producing Carbapenem-resistant enterobacteriaceae (CP-CRE) will be displayed in this table after the CDC obtains Office of Management and Budget Paperwork Reduction Act approval to receive data for this condition.",
-            "title": "NNDSS - TABLE 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chancroid",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127103,44 +127080,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/phwv-i65c",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/phwv-i65c",
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
+            "title": "NNDSS - TABLE 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chancroid"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -127163,44 +127141,44 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fhc9-h3em",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "cryptosporidiosis",
-                "dengue virus infection",
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
-            "identifier": "https://data.cdc.gov/api/views/fhc9-h3em",
             "description": "NNDSS - Table II. Cryptosporidiosis to Dengue virus infection - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \t\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 Includes data for dengue and dengue-like illness.",
-            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue virus infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127223,40 +127201,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fhc9-h3em",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "cryptosporidiosis",
+                "dengue virus infection",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fhc9-h3em",
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
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue virus infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://hmddirectory.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "history of medicine",
-                "library services",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6wuu-qryi",
             "description": "The collections described in this Directory database provide research and reference services to scholars interested in the history of the health sciences. Some of the subjects include: dentistry, veterinary medicine, nursing, biomedical sciences, military medicine, and pharmacy. While the Directory is by no means exhaustive, it serves to draw attention to the depth and variety of history of medicine collections available to researchers. In the future, we expect that more institutions will wish to be included.",
-            "title": "Directory of History of Medicine Collections",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127265,47 +127247,40 @@
                     "title": "Search and explore Directory of History of Medicine Collections"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6wuu-qryi",
+            "issued": "2022-02-08",
+            "keyword": [
+                "history of medicine",
+                "library services",
+                "reference"
+            ],
+            "landingPage": "https://hmddirectory.nlm.nih.gov/",
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
+            "title": "Directory of History of Medicine Collections"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-28",
-            "references": [
-                "NIS-Flu"
-            ],
-            "keyword": [
-                "chlidren",
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
-            "identifier": "https://data.cdc.gov/api/views/vfj2-bfuw",
             "description": "Weekly Cumulative Influenza Vaccination Coverage, Children 6 months through 17 years, United States\n\u2022 Influenza vaccination coverage among children is assessed through the National Immunization Survey-Flu (NIS-Flu) annually, providing weekly influenza vaccination coverage estimates for children 6 months\u201317 years based upon parental report. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\no NIS-Flu is a national random-digit-dialed cellular telephone survey of households conducted during the flu season (October-June).\n\u2022 Additional information about NIS-Flu methods and estimates from the 2019-2020 season are available at: https://www.cdc.gov/flu/fluvaxview/coverage-1920estimates.htm.",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage, Children 6 months through 17 years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127328,56 +127303,59 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vfj2-bfuw",
+            "issued": "2022-09-28",
+            "keyword": [
+                "chlidren",
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
+            "modified": "2022-09-28",
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
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-supplier",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-06-05",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/a2d56d3f-3531-4315-9d87-e29986516b41/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-supplier-data-dictionary",
             "description": "The Medicare Durable Medical Equipment, Devices & Supplies by Supplier dataset contains information on usage, payments, submitted charges and beneficiary demographic and health characteristics organized by supplier National Provider Identifier (NPI).",
-            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Supplier",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a2d56d3f-3531-4315-9d87-e29986516b41/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a2d56d3f-3531-4315-9d87-e29986516b41/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Supplier : 2022-12-01"
                 },
                 {
@@ -127489,47 +127467,50 @@
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Supplier : 2014-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-supplier-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a2d56d3f-3531-4315-9d87-e29986516b41/data-viewer",
+            "issued": "2024-06-05",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medical suppliers & equipment",
+                "medicare",
+                "original medicare",
+                "physicians & practitioners"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-supplier",
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
+            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Supplier"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://collections.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "books",
-                "history of medicine",
-                "images",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/886w-u7qx",
             "description": "The National Library of Medicine's (NLM) Digital Collections offers a search-based Web service that provides access to the Dublin Core metadata and full-text OCR of every resource in the repository in XML format. Developers can use the Web service to build applications that query and link to these resources.",
-            "title": "NLM Digital Collections",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127544,108 +127525,109 @@
                     "title": "Search and Browse NLM Digital Collections"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/886w-u7qx",
+            "issued": "2016-08-04",
+            "keyword": [
+                "books",
+                "history of medicine",
+                "images",
+                "library services"
+            ],
+            "landingPage": "http://collections.nlm.nih.gov/",
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
+            "title": "NLM Digital Collections"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://biolincc.nhlbi.nih.gov/home/",
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
                 "fn": "Wagner, Elizabeth",
                 "hasEmail": "mailto:wagnere@nhlbi.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "74fefd6d-b92d-44ad-a64f-6ba8acce77be",
+            "dataQuality": true,
             "description": "<p>The goal of BioLINCC is to facilitate and coordinate the existing activities of the NHLBI Biorepository and the Data Repository and to expand their scope and usability to the scientific community through a single web-based user interface.</p>",
-            "title": "Biologic Specimen and Data Repository Information Coordinating Center (BioLINCC)",
+            "identifier": "74fefd6d-b92d-44ad-a64f-6ba8acce77be",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "https://biolincc.nhlbi.nih.gov/home/",
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
+            "title": "Biologic Specimen and Data Repository Information Coordinating Center (BioLINCC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/4ekx-rduw",
             "bureauCode": [
                 "009:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "description": "An overview of Annual MeSH Processing (AMP) for MeSH/MEDLINE, including downloadable datasets detailing changes to MeSH",
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4ekx-rduw",
             "issued": "2022-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
             "keyword": [
                 "api",
                 "mesh",
                 "mesh 2023 update",
                 "terminologies"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Library of Medicine",
-                "hasEmail": "mailto:custserv@nlm.nih.gov"
-            },
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/4ekx-rduw",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-16",
+            "programCode": [
+                "009:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Library of Medicine"
             },
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4ekx-rduw",
-            "description": "An overview of Annual MeSH Processing (AMP) for MeSH/MEDLINE, including downloadable datasets detailing changes to MeSH",
-            "title": "Annual MeSH Processing (AMP)",
-            "programCode": [
-                "009:041"
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
             "theme": [
                 "Terminology"
-            ]
+            ],
+            "title": "Annual MeSH Processing (AMP)"
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
-                "summary health statistics"
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
-            "identifier": "https://data.cdc.gov/api/views/wxz7-ekz9",
             "description": "Interactive Summary Health Statistics for Children provide annual estimates of selected health topics for children under age 18 years based on final data from the National Health Interview Survey.",
-            "title": "NHIS Child Summary Health Statistics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127668,38 +127650,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wxz7-ekz9",
+            "issued": "2021-11-18",
+            "keyword": [
+                "nhis",
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/d/sqef-kequ",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-11-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
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
-            "identifier": "3944c771-0971-46bf-9a82-12ffc18bdc1b",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-13-to-2023-11-19",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127708,36 +127693,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-13-to-2023-11-19"
                 }
             ],
+            "identifier": "3944c771-0971-46bf-9a82-12ffc18bdc1b",
+            "issued": "2023-11-21",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/sqef-kequ",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-11-20",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-11-13-to-2023-11-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/s5hf-hv94",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-23",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/s5hf-hv94",
             "description": "Carcinogenic Potency Database (CPDB) is a single standardized resource of the results of 45 years of chronic, long-term carcinogenesis bioassays. The experiments vary widely in design, histopathological examination and nomenclature, and in the published authors\u2019 choices of what information to publish in their papers.\n\nData are included from 6153 experiments reported in the general literature and in the in Technical Reports of the National Cancer Institute/National Toxicology Program (NCI/NTP). Information is given in the CPDB on strain, sex, route of compound administration, target organ, histopathology, author\u2019s opinion about carcinogenicity, and reference to the published paper, as well as quantitative data on statistical significance, tumor incidence, dose-response curve shape, length of experiment, duration of dosing, and dose-rate.\n\nThe files on this Web site for the Excel format include (A) documentation of methods, field descriptions, and linking instructions; (B) Excel files; and (C) ancillary files of appendices. NOTE: This dataset is no-longer updated with new content.",
-            "title": "Carcinogenic Potency Database (CPDB)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127752,40 +127736,39 @@
                     "title": "Download Carcinogenic Potency Database (CPDB) Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/s5hf-hv94",
+            "issued": "2020-09-23",
+            "keyword": [
+                "data distribution"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/s5hf-hv94",
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
                 "Literature"
-            ]
+            ],
+            "title": "Carcinogenic Potency Database (CPDB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/sqtc-kb5m",
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
-            "identifier": "56adbcf4-f86b-5ab3-98fe-e713bbf99f12",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 1996",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127793,21 +127776,51 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "56adbcf4-f86b-5ab3-98fe-e713bbf99f12",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/sqtc-kb5m",
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
+            "title": "State Drug Utilization Data 1996"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/child-support-enforcement-handbook",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Child Support Enforcement (OCSE)",
+                "hasEmail": "mailto:OCSEHotline@acf.hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This handbook describes the basic steps to follow to establish paternity, to obtain a support order, and to collect the support due.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.acf.hhs.gov/css/outreach-material/handbook-child-support-enforcement",
+                    "mediaType": "text/html",
+                    "title": "Text"
+                }
+            ],
+            "identifier": "d3cd16fc-fc49-4c29-b28c-6e4daebbe263",
             "issued": "2014-02-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "administrative",
                 "arrears",
@@ -127846,71 +127859,34 @@
                 "title iv-e",
                 "tribal iv-a"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Child Support Enforcement (OCSE)",
-                "hasEmail": "mailto:OCSEHotline@acf.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/child-support-enforcement-handbook",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:084"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Administration for Children and Families, Department of Health & Human Services"
             },
-            "identifier": "d3cd16fc-fc49-4c29-b28c-6e4daebbe263",
-            "description": "<p>This handbook describes the basic steps to follow to establish paternity, to obtain a support order, and to collect the support due.</p>",
-            "title": "Child Support Enforcement Handbook",
-            "programCode": [
-                "009:084"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.acf.hhs.gov/css/outreach-material/handbook-child-support-enforcement",
-                    "mediaType": "text/html",
-                    "title": "Text"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Health",
                 "State"
-            ]
+            ],
+            "title": "Child Support Enforcement Handbook"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vzfn-ifh5",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/vzfn-ifh5",
             "description": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -127933,48 +127909,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vzfn-ifh5",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "ehrlichia ewingii infection",
+                "ehrlichiosis and anaplasmosis",
+                "giardiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined ehrlichiosis/anaplasmosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vzfn-ifh5",
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
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis"
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
@@ -127997,46 +127972,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Women-Infa/735e-byxc",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "Nutrition, Physical Activity, and Obesity - Women, Infant, and Child"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/list-excluded-individuals-and-entities",
             "bureauCode": [
                 "009:92"
             ],
-            "issued": "2013-03-25",
-            "temporal": "1998-01-01T00:00:00-05:00/1998-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "health care providers",
-                "medicaid",
-                "medicare",
-                "pharmacy",
-                "providers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OIG Public Affairs",
                 "hasEmail": "mailto:public.affairs@oig.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Inspector General"
-            },
-            "identifier": "848cbb44-cd74-4265-b2c5-54f5bcacfb55",
+            "dataQuality": true,
             "description": "<p>Our objective is to ensure that providers who bill Federal health care programs do not submit claims for services furnished, ordered or prescribed by an excluded individual or entity.  The LEIE is updated monthly with all individuals and entities who have been excluded from participation in Federal health care programs.  Providers who bill Medicare, Medicaid, or other Federal health care programs must ensure that they know what individuals or entities are excluded and not bill for their services (e.g., a pharmacy should not bill Medicaid for a drug prescribed by an excluded physician nor for drugs dispensed by an excluded pharmacist).</p>",
-            "title": "List of Excluded Individuals and Entities",
-            "programCode": [
-                "009:109"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128045,44 +128025,40 @@
                     "title": " "
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "848cbb44-cd74-4265-b2c5-54f5bcacfb55",
+            "issued": "2013-03-25",
+            "keyword": [
+                "health care providers",
+                "medicaid",
+                "medicare",
+                "pharmacy",
+                "providers"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/list-excluded-individuals-and-entities",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:109"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Inspector General"
+            },
+            "temporal": "1998-01-01T00:00:00-05:00/1998-01-01T00:00:00-05:00",
+            "title": "List of Excluded Individuals and Entities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qz8t-eu2e",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2015-11-06",
-            "keyword": [
-                "2014",
-                "babesiosis",
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
-            "identifier": "https://data.cdc.gov/api/views/qz8t-eu2e",
             "description": "NNDSS - Table II. Babesiosis to Coccidioidomycosis - 2014.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting year 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Babesiosis to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128105,44 +128081,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qz8t-eu2e",
+            "issued": "2015-01-08",
+            "keyword": [
+                "2014",
+                "babesiosis",
+                "chlamydia trachomatis infection",
+                "coccidioidomycosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qz8t-eu2e",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2015-11-06",
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
+            "title": "NNDSS - Table II. Babesiosis to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nehrs/about.htm",
+            "accrualPeriodicity": "Future funding patterns past 2024 are uncertain however, we expect yearly or biannually is reasonable R/P1Y or R/P2Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm\u201d",
-            "issued": "2023-09-27",
-            "@type": "dcat:Dataset",
-            "temporal": "2012-2015, 2017-2019, 2021",
-            "modified": "2023-09-27",
-            "keyword": [
-                "electronic health records",
-                "nchs",
-                "nehrs",
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
-            "identifier": "https://data.cdc.gov/api/views/myzw-mrfh",
+            "describedBy": "The sampling frame was composed of Master files for all American physicians who met the following criteria: Office-based; Principally engaged in patient care activities; Non-federally employed; Not in specialties of anesthesiology, pathology, or radiology; and Younger than 85 years of age at the time of the survey.",
             "description": "The National Electronic Health Records Survey (NEHRS) is an annual survey of non-federally employed, office-based physicians practicing in the United States (excluding those in the specialties of anesthesiology, radiology, and pathology). NEHRS began in 2008 and was originally designed as an annual mail supplement to the National Ambulatory Medical Care Survey (NAMCS). Since 2012, NEHRS has been administered as a survey independent of NAMCS.\nData from NEHRS can be used to produce state and national estimates of EHR adoption and capabilities, burden associated with EHRs, and progress physicians have made towards meeting the policy goals of the HITECH Act. In more recent years, survey questions have also asked about Promoting Interoperability programs, sponsored by the Centers for Medicare and Medicaid Services (CMS).\n\nRestricted file data dictionaries are available.",
-            "title": "National Electronic Health Records Survey, Restricted data: 2012-2015, 2017-2019, 2021",
-            "isPartOf": "https://www.cdc.gov/nchs/nehrs/questionnaires.htm",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128150,90 +128130,94 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "The sampling frame was composed of Master files for all American physicians who met the following criteria: Office-based; Principally engaged in patient care activities; Non-federally employed; Not in specialties of anesthesiology, pathology, or radiology; and Younger than 85 years of age at the time of the survey.",
+            "identifier": "https://data.cdc.gov/api/views/myzw-mrfh",
+            "isPartOf": "https://www.cdc.gov/nchs/nehrs/questionnaires.htm",
+            "issued": "2023-09-27",
+            "keyword": [
+                "electronic health records",
+                "nchs",
+                "nehrs",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nehrs/about.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Future funding patterns past 2024 are uncertain however, we expect yearly or biannually is reasonable R/P1Y or R/P2Y",
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
+            "temporal": "2012-2015, 2017-2019, 2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Electronic Health Records Survey, Restricted data: 2012-2015, 2017-2019, 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/data_specs/asn/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "data specifications"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/2qab-taci",
             "description": "An International Standards Organization (ISO) data representation format used to achieve interoperability between platforms.",
-            "title": "NCBI ASN.1 Format Summary",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/data_specs/asn/",
-                    "description": "This folder contains most recent public NCBI ASN.1 data specifications.",
                     "@type": "dcat:Distribution",
+                    "description": "This folder contains most recent public NCBI ASN.1 data specifications.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/data_specs/asn/",
+                    "mediaType": "text/html",
                     "title": "NCBI ASN.1 Format Summary (most recent)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/data_specs/ver/",
-                    "description": "This folder contains dated snapshots of public NCBI data specifications (ASN.1, DTD and XML Schema).",
                     "@type": "dcat:Distribution",
+                    "description": "This folder contains dated snapshots of public NCBI data specifications (ASN.1, DTD and XML Schema).",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/data_specs/ver/",
+                    "mediaType": "text/html",
                     "title": "NCBI ASN.1 Format Summary (dated snapshots)"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/2qab-taci",
+            "issued": "2021-06-17",
+            "keyword": [
+                "dataset",
+                "data specifications"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/data_specs/asn/",
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
+            "title": "NCBI ASN.1 Format Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/34p9-h4us",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-30",
-            "keyword": [
-                "haicviz"
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
-            "identifier": "https://data.cdc.gov/api/views/34p9-h4us",
             "description": "<p>The healthcare-associated infection component of CDC\u2019s <a href=\"https://www.cdc.gov/ncezid/dpei/eip/index.html\" target=\"_blank\">EIP</a> engages a <a href=\"https://www.cdc.gov/ncezid/dpei/eip/eip-sites.html\" target=\"_blank\">network</a> of state health departments and their academic medical center partners to help answer critical questions about emerging HAI threats, advanced infection tracking methods, and antibiotic resistance in the United States. Information gathered through this activity will play a key role in shaping future policies and recommendations targeting HAI prevention. </p>",
-            "title": "HAICViz - Candidemia",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128256,38 +128240,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/34p9-h4us",
+            "issued": "2021-06-24",
+            "keyword": [
+                "haicviz"
+            ],
+            "landingPage": "https://data.cdc.gov/d/34p9-h4us",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-03-30",
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
+            "title": "HAICViz - Candidemia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/svyg-vnne",
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
-            "identifier": "a211a52d-278d-4509-87a9-cdc6af256f31",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210920 to 20210926",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128295,44 +128280,36 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "a211a52d-278d-4509-87a9-cdc6af256f31",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/svyg-vnne",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210920 to 20210926"
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DDT Public Inquiries",
                 "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/de4p-4g3k",
+            "describedBy": "https://chronicdata.cdc.gov/d/de4p-4g3k",
             "description": "2016-17 merged. This dataset is a de-identified summary table of vision and eye health data indicators from the National Survye of Chilrens Health (NSCH), stratified by all available combinations of age group, race/ethnicity, gender, risk factor and state. NSCH is a telephone survey conducted by the National Center for Health Statistics at CDC (currently conducted by the U.S. Census Bureau) that examines the physical and emotional health of children 0-17 years of age. Approximate sample size is 95,000 over two rounds of data collection. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Detailed information on VEHSS NSCH analyses can be found on the VEHSS NSCH webpage (cdc.gov/visionhealth/vehss/data/national-surveys/national-survey-of-childrens-health.html). Additional information about NSCH can be found on the NSCH website (http://childhealthdata.org/learn/NSCH). The VEHSS NSCH dataset was last updated in November 2019.",
-            "title": "National Survey of Children\u2019s Health (NSCH) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:029"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128355,46 +128332,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/d/de4p-4g3k",
+            "identifier": "https://data.cdc.gov/api/views/de4p-4g3k",
+            "issued": "2023-09-21",
+            "keyword": [
+                "contact lenses",
+                "glasses",
+                "nsch",
+                "vision impairment",
+                "visual function"
+            ],
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-09-21",
+            "programCode": [
+                "009:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "http://childhealthdata.org/learn/NSCH",
+                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-survey-of-childrens-health.html"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "National Survey of Children\u2019s Health (NSCH) \u2013 Vision and Eye Health Surveillance"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -128417,35 +128394,45 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xup8-ahj8",
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
-            "identifier": "https://data.cdc.gov/api/views/xup8-ahj8",
             "description": "Up-to-date anthropometric information (body dimensions) of the U.S. firefighter population is needed for updating ergonomic and safety specifications for fire apparatus and firefighter protective equipment. Seventy-one measurements relevant to the design of seats, seat belts, cabs, turnout gear, gloves, and head-and-face gear are presented in this webpage. Forty of the 71 measurements were collected with the participants in fitted shorts in both standing and seated postures. Twenty-one of the 71 measurements were collected while the participants were wearing their personal turnout gear, including personal selection of tools stored in their pockets, in both standing and seated postures. Ten of the 71 measurements were hand- and head/face-related dimensions extracted from hand and head/face scans. The data obtained in this study provide the first available U.S. national firefighter anthropometric information which will benefit the design of future fire apparatus and protective equipment to better protect firefi",
-            "title": "Firefighter Body Dimensions for Updating Safety Specifications for Fire Apparatus and Firefighter Protective Equipment",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128453,49 +128440,39 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xup8-ahj8",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/xup8-ahj8",
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
+            "title": "Firefighter Body Dimensions for Updating Safety Specifications for Fire Apparatus and Firefighter Protective Equipment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-current-beneficiary-survey-mcbs/medicare-current-beneficiary-survey-covid-19-supplement",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-02-22",
-            "temporal": "2020-04-01/2021-03-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-29",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-08/COVIDPUF2021W_DUG.pdf"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/1057bdab-3ef8-4057-86a6-88fdc973bd79/data-viewer",
-            "description": "The Medicare Current Beneficiary Survey (MCBS) - COVID-19 Supplement Public Use File (PUF) provide data on Medicare beneficiaries\u2019 experiences with COVID-19 and their access to care during the pandemic.",
-            "title": "Medicare Current Beneficiary Survey - COVID-19 Supplement",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-08/COVIDPUF2021W_Codebook_0.txt",
             "describedByType": "text/plain",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Medicare Current Beneficiary Survey (MCBS) - COVID-19 Supplement Public Use File (PUF) provide data on Medicare beneficiaries\u2019 experiences with COVID-19 and their access to care during the pandemic.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128516,44 +128493,52 @@
                     "title": "Medicare Current Beneficiary Survey - COVID-19 Supplement : 2020-04-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-08/COVIDPUF2021W_Codebook_0.txt",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/1057bdab-3ef8-4057-86a6-88fdc973bd79/data-viewer",
+            "issued": "2023-02-22",
+            "keyword": [
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "medicare prescription drug",
+                "national",
+                "original medicare",
+                "patient experience"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-current-beneficiary-survey-mcbs/medicare-current-beneficiary-survey-covid-19-supplement",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-08-29",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-08/COVIDPUF2021W_DUG.pdf"
+            ],
+            "temporal": "2020-04-01/2021-03-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Current Beneficiary Survey - COVID-19 Supplement"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xml",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "1900-01-01",
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
-            "identifier": "8acf8bd4-3c2b-4697-a2be-3d5006fbfc91",
             "description": "This list includes food subject to recall in the United States since March 2009 related to pistachios distributed by Setton Pistachio of Terra Bella, Inc. The FDA has completed its inspection of Salmonella contamination in pistachios and pistachio products involved in this recall.",
-            "title": "Pistachio Product Recalls",
-            "programCode": [
-                "009:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128561,94 +128546,82 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "8acf8bd4-3c2b-4697-a2be-3d5006fbfc91",
+            "issued": "2021-02-25",
+            "keyword": [
+                "ora"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xml",
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
+            "title": "Pistachio Product Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/sxh4-mmkr",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-15",
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
-            "identifier": "efd0a509-1e9e-583c-90c8-63cac4338c19",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard TAG v0.2.4-1 (etl_test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.2.4-1/TAG.csv",
-                    "description": "Scorecard TAG v0.2.4-1 (etl_test)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard TAG v0.2.4-1 (etl_test)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.2.4-1/TAG.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard TAG v0.2.4-1 (etl_test)"
                 }
             ],
+            "identifier": "efd0a509-1e9e-583c-90c8-63cac4338c19",
+            "issued": "2023-04-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/sxh4-mmkr",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-05-15",
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
+            "title": "Scorecard TAG v0.2.4-1 (etl_test)"
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
-            "identifier": "https://data.cdc.gov/api/views/mb5y-ytti",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
             "description": "This dataset contains model-based census tract level estimates for the PLACES 2021 release in GIS-friendly format. PLACES is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census tract 2015 boundary file in a GIS system to produce maps for 29 measures at the census tract level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. \nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=024cf3f6f59e49fe8c70e0e5410fe3cf",
-            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2021 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128671,49 +128644,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
+            "identifier": "https://data.cdc.gov/api/views/mb5y-ytti",
+            "issued": "2022-10-11",
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
+            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2021 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ekcb-r85s",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-02-26",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/ekcb-r85s",
             "description": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice:  In Table 1n of the 2021 NNDSS weekly tables for week 1 only, data for Haemophilus influenzae in children < 5years categorized as \"non-b serotype\" and \"unknown serotype\" were updated on 02/26/2021 to correct the data associated with these two serotype categories. The original version of the tables incorrectly displayed data for \"non-b serotype\" in the \"unknown serotype\" column and incorrectly displayed data for \"unknown serotype\" in the \"non-b serotype\" column. The data are corrected now.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128736,40 +128710,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ekcb-r85s",
+            "issued": "2021-02-26",
+            "keyword": [
+                "2021",
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
+            "landingPage": "https://data.cdc.gov/d/ekcb-r85s",
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
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/sxwk-mrn8",
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
-            "identifier": "f3144e50-5f27-5e2c-acbb-1962a2aeae55",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2002",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128777,41 +128760,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "f3144e50-5f27-5e2c-acbb-1962a2aeae55",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/sxwk-mrn8",
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
+            "title": "State Drug Utilization Data 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/osiris/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/fqjb-ufn5",
             "description": "A public domain quality assurance software package that facilitates the assessment of multiplex short tandem repeat (STR) DNA profiles based on laboratory-specific protocols.",
-            "title": "OSIRIS",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128820,21 +128802,51 @@
                     "title": "OSIRIS - Download"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/fqjb-ufn5",
+            "issued": "2021-06-30",
+            "keyword": [
+                "genomics",
+                "software",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/osiris/",
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
+            "title": "OSIRIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/warning-letters-1",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>When it is consistent with the public protection responsibilities of the agency and depending on the nature of the violation, it is the Food and Drug Administration's (FDA's) practice to give individuals and firms an opportunity to take voluntary and prompt corrective action before it initiates an enforcement action. Warning Letters are issued to achieve voluntary compliance and to establish prior notice.  The use of Warning Letters and the prior notice policy are based on the expectation that most individuals and firms will voluntarily comply with the law.  See <a href=\"http://www.fda.gov/ICECI/ComplianceManuals/RegulatoryProceduresManual/ucm176870.htm\">http://www.fda.gov/ICECI/ComplianceManuals/RegulatoryProceduresManual/uc...</a> for additional infomation on Warning Letters.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/warningletters/wlSearchExcel.cfm",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "541c2445-224d-4235-9c13-8fac34903aa8",
             "issued": "2012-05-30",
-            "temporal": "1996-11-01T00:00:00-05:00/1996-11-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "administrative",
                 "advertising",
@@ -128847,62 +128859,35 @@
                 "veterinary medicine",
                 "warning letters"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/warning-letters-1",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:002"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "541c2445-224d-4235-9c13-8fac34903aa8",
-            "description": "<p>When it is consistent with the public protection responsibilities of the agency and depending on the nature of the violation, it is the Food and Drug Administration's (FDA's) practice to give individuals and firms an opportunity to take voluntary and prompt corrective action before it initiates an enforcement action. Warning Letters are issued to achieve voluntary compliance and to establish prior notice.  The use of Warning Letters and the prior notice policy are based on the expectation that most individuals and firms will voluntarily comply with the law.  See <a href=\"http://www.fda.gov/ICECI/ComplianceManuals/RegulatoryProceduresManual/ucm176870.htm\">http://www.fda.gov/ICECI/ComplianceManuals/RegulatoryProceduresManual/uc...</a> for additional infomation on Warning Letters.</p>",
-            "title": "Warning Letters",
-            "programCode": [
-                "009:002"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/warningletters/wlSearchExcel.cfm",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1996-11-01T00:00:00-05:00/1996-11-01T00:00:00-05:00",
             "theme": [
                 "Community"
-            ]
+            ],
+            "title": "Warning Letters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/sykp-p4ut",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2018-03-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
-            "keyword": [
-                "quarterly state contact file"
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
-            "identifier": "46a5d780-feef-521a-af7b-25119ec3dc09",
             "description": "Contains each state's policy, rebate and technical contact information for the Medicaid Drug Rebate Program. Updated quarterly.",
-            "title": "Medicaid Drug Rebate Program State Contact Information",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128911,41 +128896,39 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "46a5d780-feef-521a-af7b-25119ec3dc09",
+            "issued": "2018-03-16",
+            "keyword": [
+                "quarterly state contact file"
+            ],
+            "landingPage": "https://healthdata.gov/d/sykp-p4ut",
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
+            "title": "Medicaid Drug Rebate Program State Contact Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/low-income-home-energy-assistance-program-fy-2008-household-data",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-08-10",
-            "temporal": "2008-01-01T00:00:00-05:00/2008-09-30T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "children and family services",
-                "population statistics"
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
-            "identifier": "2c1fbaad-039a-423d-b3a7-9d15476e7a02",
+            "dataQuality": true,
             "description": "<p>State-reported annual data collected on the presence of elderly, disabled, and young children in eligible households receiving Low Income Home Energy Assistance Program (LIHEAP) heating assistance, cooling assistance, crisis assistance or weatherization assistance.</p>",
-            "title": "Low Income Home Energy Assistance Program FY 2008 Household Data",
-            "programCode": [
-                "009:085"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -128954,41 +128937,37 @@
                     "title": "Query Tool "
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "2c1fbaad-039a-423d-b3a7-9d15476e7a02",
+            "issued": "2012-08-10",
+            "keyword": [
+                "children and family services",
+                "population statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/low-income-home-energy-assistance-program-fy-2008-household-data",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:085"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "temporal": "2008-01-01T00:00:00-05:00/2008-09-30T00:00:00-04:00",
+            "title": "Low Income Home Energy Assistance Program FY 2008 Household Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rpjd-ejph",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-10-06",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-19",
-            "keyword": [
-                "122 cities",
-                "2016",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/rpjd-ejph",
             "description": "TABLE III. Deaths in 122 U.S. cities \u2013 2016.  122 Cities Mortality Reporting System \u2014 Each week, the vital statistics offices of 122 cities across the United States report the total number of death certificates processed and the number of those for which pneumonia or influenza was listed as the underlying or contributing cause of death by age group (Under 28 days, 28 days \u20131 year, 1-14 years, 15-24 years, 25-44 years, 45-64 years, 65-74 years, 75-84 years, and \u2265 85 years).\r\n\r\nFOOTNOTE:\r\nU: Unavailable. \u2014: No reported cases.\r\n* Mortality data in this table are voluntarily reported from 122 cities in the United States, most of which have populations of 100,000 or more. A death is reported by the place of its occurrence and by the week that the death certificate was filed. Fetal deaths are not included. \r\n\r\n\u2020 Pneumonia and influenza. \r\n\r\n\u00a7 Total includes unknown ages.",
-            "title": "TABLE III. Deaths in 122 U.S. cities",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129011,36 +128990,40 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/rpjd-ejph",
+            "issued": "2016-10-06",
+            "keyword": [
+                "122 cities",
+                "2016",
+                "death",
+                "influenza",
+                "mortality",
+                "pneumonia"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rpjd-ejph",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2018-01-19",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "TABLE III. Deaths in 122 U.S. cities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5qag-uzp2",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
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
-            "identifier": "https://data.cdc.gov/api/views/5qag-uzp2",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "CDC STATE System Tobacco Legislation Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129048,38 +129031,40 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5qag-uzp2",
+            "issued": "2015-01-21",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5qag-uzp2",
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
                 "Legislation"
-            ]
+            ],
+            "title": "CDC STATE System Tobacco Legislation Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/szsf-s9qi",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-29",
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
-            "identifier": "8865d8e5-85fe-44f2-832d-2d6b984c312b",
             "description": "The Reference Document link for the downable Blood Disorder Treatment Spreadsheet can be accessed below under the Additional Information table under Related Documents.",
-            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 12/1/2023)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129087,48 +129072,42 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "8865d8e5-85fe-44f2-832d-2d6b984c312b",
+            "issued": "2024-01-01",
+            "keyword": [
+                "drug products"
+            ],
+            "landingPage": "https://healthdata.gov/d/szsf-s9qi",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2023-12-29",
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
+            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 12/1/2023)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/quarterly-prescription-drug-plan-formulary-pharmacy-network-and-pricing-information",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-12-15",
-            "temporal": "2019-01-01/2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2023-10/98c7b019-7e9c-4c6d-a77c-f49f6c5b87e6/Methodology-SPUF-2024.pdf"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/a94b1015-1b93-476b-80ec-508b4169c8f5/data-viewer",
-            "description": "The Quarterly Prescription Drug Plan Formulary, Pharmacy Network, and Pricing Information files contain formulary, pharmacy network, and pricing data for Medicare Prescription Drug Plans and Medicare Advantage (MA) Prescription Drug Plans (with the exception of employer and Program of All-Inclusive Care for the Elderly plans).\n\n\u00a0\n\nNotice: CMS has identified an issue that resulted in a 15% coinsurance for plans with Defined Standard benefits to be listed rather than a 25% coinsurance in the Beneficiary Cost File under certain scenarios. This issue affected the 2023 Q4 to 2024 Q3 data. CMS will re-post the corrected data in batches between now and May 2025.\n\n\u00a0\n\nThese non-identifiable files are available on a quarterly basis and are comprised of the following tables:\n\n\n\tPlan Information - Information such as plan name, contract ID, plan ID, service area, and plan type.\n\tGeographic Locator - MA and Prescription Drug Plans region codes and county codes.\n\tBasic Drugs Formulary - Formulary details for each plan including National Drug Codes (NDCs), cost share tier level, and indicators for step therapy, quantity limits, and prior authorization.\n\tExcluded Drugs Formulary - Enhanced alternative plans may elect to provide a supplemental benefit and cover excluded drugs. File includes formulary details for excluded drugs that are covered by the plan (for enhanced alternative plans only).\n\tBeneficiary Cost - Plan level cost sharing details for preferred, non-preferred, and mail order network pharmacies.\n\tPharmacy Network - National Provider Identifier (NPI) numbers for each network pharmacy including preferred, retail, and mail order indicators.\n\tPricing - Plan level average monthly costs for formulary Part D drugs (note: this table is only available in the quarterly files).\n\tPartial Gap Coverage - Plan-RxCUI combinations that are on tiers that offer gap coverage for some drugs on the tier.\n\tIndication Based Coverage Formulary File - Includes drugs covered based on FDA-approved indication for each plan.\n\tInsulin Beneficiary Cost File - Plan level cost sharing details for insulin at preferred, non-preferred and mail order network pharmacies.\n\n\n\u00a0\n\nThese are large files and can take time to download.\u00a0\n\n\u00a0\n\nPlease read the \u201cAgreement for Use\u201d in the Resources section below. This document contains important information regarding timeframes for obtaining data as well as data accuracy and integrity.\n\n\u00a0\n\nThe Monthly Prescription Drug Plan Formulary and Pharmacy Network Information is also available to access for the monthly level information.\n\n\u00a0\n\nPlease note:\u00a0\u00a0The Part D benefit year information for plans become available in October of the year prior. For example, year 2024 data is available in the fourth quarter file of 2023. Year 2024 data continues to be available in the Q1-Q3 2024 \u00a0files, then in the fourth quarter of 2024 year 2025 data becomes available.\u00a0\n\nEstimated release dates for upcoming 2025 quarterly data (files reflect data for the quarter that ended the month before the file was released):\n\n\n\t1/29/25\n\t4/23/25\n\t7/30/25\n\n\nFiles older than contract year 2019 can be purchased.",
-            "title": "Quarterly Prescription Drug Plan Formulary, Pharmacy Network, and Pricing Information",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-01/SPUFRecordLayout-2024.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Quarterly Prescription Drug Plan Formulary, Pharmacy Network, and Pricing Information files contain formulary, pharmacy network, and pricing data for Medicare Prescription Drug Plans and Medicare Advantage (MA) Prescription Drug Plans (with the exception of employer and Program of All-Inclusive Care for the Elderly plans).\n\n\u00a0\n\nNotice: CMS has identified an issue that resulted in a 15% coinsurance for plans with Defined Standard benefits to be listed rather than a 25% coinsurance in the Beneficiary Cost File under certain scenarios. This issue affected the 2023 Q4 to 2024 Q3 data. CMS will re-post the corrected data in batches between now and May 2025.\n\n\u00a0\n\nThese non-identifiable files are available on a quarterly basis and are comprised of the following tables:\n\n\n\tPlan Information - Information such as plan name, contract ID, plan ID, service area, and plan type.\n\tGeographic Locator - MA and Prescription Drug Plans region codes and county codes.\n\tBasic Drugs Formulary - Formulary details for each plan including National Drug Codes (NDCs), cost share tier level, and indicators for step therapy, quantity limits, and prior authorization.\n\tExcluded Drugs Formulary - Enhanced alternative plans may elect to provide a supplemental benefit and cover excluded drugs. File includes formulary details for excluded drugs that are covered by the plan (for enhanced alternative plans only).\n\tBeneficiary Cost - Plan level cost sharing details for preferred, non-preferred, and mail order network pharmacies.\n\tPharmacy Network - National Provider Identifier (NPI) numbers for each network pharmacy including preferred, retail, and mail order indicators.\n\tPricing - Plan level average monthly costs for formulary Part D drugs (note: this table is only available in the quarterly files).\n\tPartial Gap Coverage - Plan-RxCUI combinations that are on tiers that offer gap coverage for some drugs on the tier.\n\tIndication Based Coverage Formulary File - Includes drugs covered based on FDA-approved indication for each plan.\n\tInsulin Beneficiary Cost File - Plan level cost sharing details for insulin at preferred, non-preferred and mail order network pharmacies.\n\n\n\u00a0\n\nThese are large files and can take time to download.\u00a0\n\n\u00a0\n\nPlease read the \u201cAgreement for Use\u201d in the Resources section below. This document contains important information regarding timeframes for obtaining data as well as data accuracy and integrity.\n\n\u00a0\n\nThe Monthly Prescription Drug Plan Formulary and Pharmacy Network Information is also available to access for the monthly level information.\n\n\u00a0\n\nPlease note:\u00a0\u00a0The Part D benefit year information for plans become available in October of the year prior. For example, year 2024 data is available in the fourth quarter file of 2023. Year 2024 data continues to be available in the Q1-Q3 2024 \u00a0files, then in the fourth quarter of 2024 year 2025 data becomes available.\u00a0\n\nEstimated release dates for upcoming 2025 quarterly data (files reflect data for the quarter that ended the month before the file was released):\n\n\n\t1/29/25\n\t4/23/25\n\t7/30/25\n\n\nFiles older than contract year 2019 can be purchased.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129269,62 +129248,50 @@
                     "title": "Quarterly Prescription Drug Plan Formulary, Pharmacy Network, and Pricing Information : 2019-03-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-01/SPUFRecordLayout-2024.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/a94b1015-1b93-476b-80ec-508b4169c8f5/data-viewer",
+            "issued": "2023-12-15",
+            "keyword": [
+                "all other provider care types",
+                "drugs",
+                "health care use & payments",
+                "medicare",
+                "medicare prescription drug"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/quarterly-prescription-drug-plan-formulary-pharmacy-network-and-pricing-information",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2023-10/98c7b019-7e9c-4c6d-a77c-f49f6c5b87e6/Methodology-SPUF-2024.pdf"
+            ],
+            "temporal": "2019-01-01/2024-09-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Quarterly Prescription Drug Plan Formulary, Pharmacy Network, and Pricing Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2020/2021",
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
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "puerto rico",
-                "race",
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
-            "identifier": "https://data.cdc.gov/api/views/q85u-gmyc",
             "description": "Provisional deaths involving coronavirus disease 2019 (COVID-19) reported to NCHS by time-period (week, month, year), HHS region, race and Hispanic origin, and age group (0-24, 25-64, 65+ years) for 2020-2021.\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City, Puerto Rico; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
-            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age Group, 2020-2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129347,41 +129314,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/q85u-gmyc",
+            "issued": "2021-08-26",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hhs region",
+                "hispanic origin",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "puerto rico",
+                "race",
+                "united states",
+                "weekly",
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2020/2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age Group, 2020-2021"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -129404,39 +129387,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/7zky-in8p",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7zky-in8p",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014,  Region 10 - Seattle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/vecscreen/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ci58-3q6g",
             "description": "Quickly identifying segments of a nucleic acid sequence that may be of vector origin.",
-            "title": "VecScreen",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129445,35 +129428,39 @@
                     "title": "VecScreen"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ci58-3q6g",
+            "issued": "2021-07-01",
+            "keyword": [
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/vecscreen/",
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
+            "title": "VecScreen"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hyai-856q",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory, Research Pathology and Physiology Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hyai-856q",
             "description": "Exposure to hand-transmitted vibration (HTV) has been shown to result in cold-induced vasoconstriction and a reduction in blood flow to the hands and fingers of workers. Occupational exposure to HTV can also induce a hypersensitivity of the sympathetic nervous system to various stimuli, which in turn can result in vasoconstriction of the peripheral blood vessels and blanching of the skin because of reductions in peripheral blood flow. The data presented were collected using an established animal model of vibration-induced white finger (Welcome et al. 2008) to determine if changes in blood flow induced by vibration exposure could be used as a biomarker for the development of vibration-induced peripheral vascular disease. Two separate experiments were done. In Experiment 1, changes in blood flow were measured in the ventral tail artery of the rat tail before and after a 4 h exposure to tail vibration (frequency 125 Hz, amplitude 5 g). These data were compared with those of animals that were restrained and had t",
-            "title": "A model for detecting the effects of vibration on peripheral blood flow",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129481,38 +129468,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hyai-856q",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/hyai-856q",
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
+            "title": "A model for detecting the effects of vibration on peripheral blood flow"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/t3mb-6q5x",
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
-            "identifier": "8e1e1e96-629d-4854-9816-b4e32dd8d16c",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210823 to 20210829",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129520,40 +129505,36 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "8e1e1e96-629d-4854-9816-b4e32dd8d16c",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/t3mb-6q5x",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210823 to 20210829"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/wide-ranging-online-data-epidemiologic-research-wonder",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "births",
-                "community health",
-                "deaths",
-                "disease incidence",
-                "epidemiology"
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
-            "identifier": "c1e25290-2a81-4584-9c8e-9c21512c252a",
+            "dataQuality": true,
             "description": "<p>WONDER online databases include county-level Compressed Mortality (death certificates) since 1979; county-level Multiple Cause of Death (death certificates) since 1999; county-level Natality (birth certificates) since 1995; county-level Linked Birth / Death records (linked birth-death certificates) since 1995;  state &amp; large metro-level United States Cancer Statistics mortality (death certificates) since 1999;  state &amp; large metro-level United States Cancer Statistics incidence (cancer registry cases) since 1999; state and metro-level Online Tuberculosis Information System (TB case reports) since 1993;  state-level Sexually Transmitted Disease  Morbidity (case reports) since 1984; state-level Vaccine Adverse Event Reporting system (adverse reaction case reports) since 1990; county-level population estimates since 1970.  The WONDER web server also hosts the Data2010 system with state-level data for compliance with Healthy People 2010 goals since 1998; the National Notifiable Disease Surveillance System weekly provisional case reports since 1996; the 122 Cities Mortality Reporting System weekly death reports since 1996;  the Prevention Guidelines database (book in electronic format) published 1998; the Scientific Data Archives (public use data sets and documentation); and links to other online data sources on the \"Topics\" page.</p>",
-            "title": "CDC WONDER API for Data Query Web Service",
-            "programCode": [
-                "009:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129562,87 +129543,89 @@
                     "title": "API "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "c1e25290-2a81-4584-9c8e-9c21512c252a",
+            "issued": "2012-05-30",
+            "keyword": [
+                "births",
+                "community health",
+                "deaths",
+                "disease incidence",
+                "epidemiology"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/wide-ranging-online-data-epidemiologic-research-wonder",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
             "theme": [
                 "Community",
                 "Health"
-            ]
+            ],
+            "title": "CDC WONDER API for Data Query Web Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/t3my-w6pn",
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
-            "identifier": "45d84210-e8fb-5d7e-9ce0-07c95b40d211",
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
+            "identifier": "45d84210-e8fb-5d7e-9ce0-07c95b40d211",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/t3my-w6pn",
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
-            "landingPage": "https://data.cdc.gov/d/5amh-5sx3",
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
-            "identifier": "https://data.cdc.gov/api/views/5amh-5sx3",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Behavior Risk Factor Surveillance System (BRFSS) Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129650,50 +129633,40 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5amh-5sx3",
+            "issued": "2015-02-05",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5amh-5sx3",
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
+            "title": "Behavior Risk Factor Surveillance System (BRFSS) Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "excess deaths",
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
-            "identifier": "https://data.cdc.gov/api/views/xkkf-xrst",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nEstimates of excess deaths can provide information about the burden of mortality potentially related to COVID-19, beyond the number of deaths that are directly attributed to COVID-19. Excess deaths are typically defined as the difference between observed numbers of deaths and expected numbers. This visualization provides weekly data on excess deaths by jurisdiction of occurrence. Counts of deaths in more recent weeks are compared with historical trends to determine whether the number of deaths is significantly higher than expected.\n\nEstimates of excess deaths can be calculated in a variety of ways, and will vary depending on the methodology and assumptions about how many deaths are expected to occur. Estimates of excess deaths presented in this webpage were calculated using Farrington surveillance algorithms (1). For each jurisdiction, a model is used to generate a set of expected counts, and the upper bound of the 95% Confidence Intervals (95% CI) of these expected counts is used as a threshold to estimate excess deaths. Observed counts are compared to these upper bound estimates to determine whether a significant increase in deaths has occurred. Provisional counts are weighted to account for potential underreporting in the most recent weeks. However, data for the most recent week(s) are still likely to be incomplete. Only about 60% of deaths are reported within 10 days of the date of death, and there is considerable variation by jurisdiction. More detail about the methods, weighting, data, and limitations can be found in the Technical Notes.",
-            "title": "Excess Deaths Associated with COVID-19",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129716,71 +129689,122 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
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
+            "title": "Excess Deaths Associated with COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/t4h5-cn9m",
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
-            "identifier": "a2c8ca85-8fd0-5a5d-8cca-b034c49d713a",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard pillar v2.11.9 (impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/pillar.csv",
-                    "description": "Scorecard pillar v2.11.9 (impl)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard pillar v2.11.9 (impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard pillar v2.11.9 (impl)"
                 }
             ],
+            "identifier": "a2c8ca85-8fd0-5a5d-8cca-b034c49d713a",
+            "issued": "2023-06-29",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/t4h5-cn9m",
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
+            "title": "Scorecard pillar v2.11.9 (impl)"
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
-                "https://chronicdata.cdc.gov/d/3ahs-wye3"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/National-Adult-Tobacco-Survey-NATS-/tbfm-vbpp",
+            "description": "2013-2014. The National Adult Tobacco Survey (NATS) was created to assess the prevalence of tobacco use, as well as the factors promoting and impeding tobacco use among adults. NATS also establishes a comprehensive framework for evaluating both the national and state-specific tobacco control programs.  NATS was designed as a stratified, national, landline, and cell phone survey of non-institutionalized adults aged 18 years and older residing in the 50 states or D.C. It was developed to yield data representative and comparable at both national and state levels. The sample design also aims to provide national estimates for subgroups defined by sex, age, and race/ethnicity.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tbfm-vbpp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tbfm-vbpp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tbfm-vbpp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tbfm-vbpp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/tbfm-vbpp",
+            "issued": "2025-01-31",
             "keyword": [
                 "adult",
                 "age",
@@ -129814,78 +129838,36 @@
                 "tobacco use",
                 "user"
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
-            "identifier": "https://data.cdc.gov/api/views/tbfm-vbpp",
-            "description": "2013-2014. The National Adult Tobacco Survey (NATS) was created to assess the prevalence of tobacco use, as well as the factors promoting and impeding tobacco use among adults. NATS also establishes a comprehensive framework for evaluating both the national and state-specific tobacco control programs.  NATS was designed as a stratified, national, landline, and cell phone survey of non-institutionalized adults aged 18 years and older residing in the 50 states or D.C. It was developed to yield data representative and comparable at both national and state levels. The sample design also aims to provide national estimates for subgroups defined by sex, age, and race/ethnicity.",
-            "title": "National Adult Tobacco Survey (NATS)",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tbfm-vbpp/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tbfm-vbpp/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tbfm-vbpp/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tbfm-vbpp/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
+            "references": [
+                "https://chronicdata.cdc.gov/d/3ahs-wye3"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/National-Adult-Tobacco-Survey-NATS-/tbfm-vbpp",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "National Adult Tobacco Survey (NATS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm142931.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2011-02-10",
-            "keyword": [
-                "cder",
-                "commitments",
-                "postmarket"
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
-            "identifier": "bf085673-ae08-4807-8ca7-aeb36dde83ed",
             "description": "Provides information to the public on postmarket requirements and commitments. The phrase postmarket requirements and commitments refers to studies and clinical trials that sponsors conduct after approval to gather additional information about a product's safety, efficacy, or optimal use. Some of the studies and clinical trials may be required; others may be studies or clinical trials a sponsor has committed to conduct.",
-            "title": "Postmarket Requirements and Commitments",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129893,40 +129875,37 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "bf085673-ae08-4807-8ca7-aeb36dde83ed",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder",
+                "commitments",
+                "postmarket"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm142931.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2011-02-10",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Postmarket Requirements and Commitments"
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
-            "modified": "2022-03-30",
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
-            "identifier": "https://data.cdc.gov/api/views/pbkm-d27e",
             "description": "This dataset describes drug poisoning deaths at the county level by selected demographic characteristics and includes age-adjusted death rates for drug poisoning from 1999 to 2015.\r\n\r\nDeaths are classified using the International Classification of Diseases, Tenth Revision (ICD\u201310). Drug-poisoning deaths are defined as having ICD\u201310 underlying cause-of-death codes X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), or Y10\u2013Y14 (undetermined intent).\r\n\r\nEstimates are based on the National Vital Statistics System multiple cause-of-death mortality files (1). Age-adjusted death rates (deaths per 100,000 U.S. standard population for 2000) are calculated using the direct method. Populations used for computing death rates for 2011\u20132015 are postcensal estimates based on the 2010 U.S. census. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\r\n\r\nEstimate does not meet standards of reliability or precision. Death rates are flagged as \u201cUnreliable\u201d in the chart when the rate is calculated with a numerator of 20 or less.\r\n\r\nDeath rates for some states and years may be low due to a high number of unresolved pending cases or misclassification of ICD\u201310 codes for unintentional poisoning as R99, \u201cOther ill-defined and unspecified causes of mortality\u201d (2). For example, this issue is known to affect New Jersey in 2009 and West Virginia in 2005 and 2009 but also may affect other years and other states. Estimates should be interpreted with caution.\r\n\r\nSmoothed county age-adjusted death rates (deaths per 100,000 population) were obtained according to methods described elsewhere (3\u20135). Briefly, two-stage hierarchical models were used to generate empirical Bayes estimates of county age-adjusted death rates due to drug poisoning for each year during 1999\u20132015. These annual county-level estimates \u201cborrow strength\u201d across counties to generate stable estimates of death rates where data are sparse due to small population size (3,5). Estimates are unavailable for Broomfield County, Colo., and Denali County, Alaska, before 2003 (6,7). Additionally, Bedford City, Virginia was added to Bedford County in 2015 and no longer appears in the mortality file in 2015. County boundaries are consistent with the vintage 2005-2007 bridged-race population file geographies (6).",
-            "title": "NCHS - Drug Poisoning Mortality by County: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -129949,37 +129928,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/pbkm-d27e",
+            "issued": "2016-01-07",
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
+            "title": "NCHS - Drug Poisoning Mortality by County: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/dhcs/prelim-hc-visits/index.htm",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-04-25",
-            "temporal": "2024-01-01/2024-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-13",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/367e-pucc",
             "description": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component, conducted by the National Center for Health Statistics (NCHS), collects annual data on visits to health centers to describe patterns of utilization and provision of ambulatory care delivery in the United States. Data are collected from federally qualified health centers (FQHCs) and FQHC look-alikes from all 50 U.S. states and the District of Columbia and are used to develop nationally representative estimates. \nThe data include preliminary, biannual counts and rates of health center visits from January 2022-June 2024 by medical diagnosis chapters, maternal and reproductive health-related diagnoses, mental health disorders, and respiratory conditions, stratified by selected patient characteristics. Estimates are split into biannual time periods (January to June, and July to December) and are considered preliminary, meaning they may differ from final estimates.",
-            "title": "Preliminary Estimates of Visits to Health Centers in the United States, January 2022-June 2024",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -130002,61 +129989,84 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/367e-pucc",
+            "issued": "2024-04-25",
+            "landingPage": "https://www.cdc.gov/nchs/dhcs/prelim-hc-visits/index.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-12-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S.",
+            "temporal": "2024-01-01/2024-06-30",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Preliminary Estimates of Visits to Health Centers in the United States, January 2022-June 2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/ndi/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-02-22",
-            "temporal": "1979-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "population statistics",
-                "vital statistics  us births and deaths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lilian Ingster",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
-            },
-            "identifier": "a725dbdf-f804-4120-884f-af16b67028f3",
+            "dataQuality": true,
+            "describedBy": "http://www.cdc.gov/nchs/ndi.htm",
             "description": "<p>The National Death Index (NDI) is a centralized database of death record information on file in state vital statistics offices. Working with these state offices, the National Center for Health Statistics (NCHS) established the NDI as a resource to aid epidemiologists and other health and medical investigators with their mortality ascertainment activities.</p>\n<p>Assists investigators in determining whether persons in their studies have died and, if so, provide the names of the states in which those deaths occurred, the dates of death, and the corresponding death certificate numbers. Investigators can then make arrangements with the appropriate state offices to obtain copies of death certificates or specific statistical information such as manner of death or educational level. Cause of death codes may also be obtained using the NDI Plus service.</p>\n<p>Records from 1979 through 2011 are currently available and contain a standard set of identifying information on each death. Death records are added to the NDI file annually, approximately 12 months after the end of a particular calendar year. 2012 should be available summer 2014. Early Release Program for 2013 is now available.</p>\n<p>The NDI service is available to investigators solely for statistical purposes in medical and health research. The service is not accessible to organizations or the general public for legal, administrative, or genealogy purposes.</p>",
-            "title": "National Death Index",
+            "identifier": "a725dbdf-f804-4120-884f-af16b67028f3",
+            "issued": "2015-02-22",
+            "keyword": [
+                "population statistics",
+                "vital statistics  us births and deaths"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/ndi/index.html",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:048"
             ],
-            "describedBy": "http://www.cdc.gov/nchs/ndi.htm",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1979-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
+            "title": "National Death Index"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-grantee",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2015-06-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/regional-extension-centers-rec-priority-primary-care-providers-meaningful-use"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-grantee",
+            "description": "The ONC Regional Extension Centers (REC) Program provides assistance to health care providers to adopt and meaningfully use certified EHR technology. The program, funded through the American Recovery and Reinvestment Act (ARRA) or The Recovery Act, provides grants to organizations, Regional Extension Centers, that assist providers directly in the organization's region. There are 62 unique RECs across the United States. This data set provides federal funding granted to each REC, each REC's program goals, and various metrics on the total providers that have signed up with an REC for assistance, gone live on an EHR, and demonstrated meaningful use of certified EHR technology. This data set is an artifact of ONC's performance measurement and data analysis during the life of ARRA. RECs continue to assist providers to go live and demonstrate meaningful use of EHRs. See ONC's other REC data to track these metrics at the state and county level.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/REC_KPI_Masterfile.csv",
+                    "mediaType": "text/csv",
+                    "title": "REC_KPI_Masterfile.csv"
+                }
             ],
+            "identifier": "ytd2bcc1-rgdn-e58e-os1c-9q7j8rr5qnab",
+            "issued": "2023-10-03",
             "keyword": [
                 "cehrt",
                 "ehr",
@@ -130069,64 +130079,32 @@
                 "rec",
                 "regional extension centers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-grantee",
+            "modified": "2015-06-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "ytd2bcc1-rgdn-e58e-os1c-9q7j8rr5qnab",
-            "description": "The ONC Regional Extension Centers (REC) Program provides assistance to health care providers to adopt and meaningfully use certified EHR technology. The program, funded through the American Recovery and Reinvestment Act (ARRA) or The Recovery Act, provides grants to organizations, Regional Extension Centers, that assist providers directly in the organization's region. There are 62 unique RECs across the United States. This data set provides federal funding granted to each REC, each REC's program goals, and various metrics on the total providers that have signed up with an REC for assistance, gone live on an EHR, and demonstrated meaningful use of certified EHR technology. This data set is an artifact of ONC's performance measurement and data analysis during the life of ARRA. RECs continue to assist providers to go live and demonstrate meaningful use of EHRs. See ONC's other REC data to track these metrics at the state and county level.",
-            "title": "ONC Regional Extension Centers (REC) Key Performance Indicators (KPIs) by Grantee",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/REC_KPI_Masterfile.csv",
-                    "mediaType": "text/csv",
-                    "title": "REC_KPI_Masterfile.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/quickstats/regional-extension-centers-rec-priority-primary-care-providers-meaningful-use"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-grantee"
+            "title": "ONC Regional Extension Centers (REC) Key Performance Indicators (KPIs) by Grantee"
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
@@ -130149,52 +130127,53 @@
                     "mediaType": "application/xml"
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
-            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/accountable-care-organization-skilled-nursing-facility-affiliates",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2017-01-01/2025-12-31",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/5b227bd9-82d4-4145-86fd-809e02ca7f18/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-snf-affiliates-data-dictionary",
             "description": "The Accountable Care Organization Skilled Nursing Facility Affiliates data presents overview information on ACO SNF affiliates in the Medicare Shared Savings Program (Shared Savings Program), including their name, track status, number of years in the program, and contact information of key personnel.\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to ACO information occur periodically. Each ACO has the most up-to-date information about their organization. Consider contacting the ACO for the latest information.",
-            "title": "Accountable Care Organization Skilled Nursing Facility Affiliates",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5b227bd9-82d4-4145-86fd-809e02ca7f18/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5b227bd9-82d4-4145-86fd-809e02ca7f18/data",
+                    "mediaType": "text/html",
                     "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2025-01-15"
                 },
                 {
@@ -130318,51 +130297,49 @@
                     "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2017-01-15"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/aco-snf-affiliates-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/5b227bd9-82d4-4145-86fd-809e02ca7f18/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/accountable-care-organization-skilled-nursing-facility-affiliates",
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
+            "temporal": "2017-01-01/2025-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accountable Care Organization Skilled Nursing Facility Affiliates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/uu9i-eu7y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "hemolytic uremic syndrome post-diarrheal",
-                "hepatitis (viral acute) type a",
-                "hepatitis (viral acute) type b",
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
-            "identifier": "https://data.cdc.gov/api/views/uu9i-eu7y",
             "description": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -130385,20 +130362,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/uu9i-eu7y",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "hemolytic uremic syndrome post-diarrheal",
+                "hepatitis (viral acute) type a",
+                "hepatitis (viral acute) type b",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/uu9i-eu7y",
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
+            "title": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-vi-nys-1983",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>Youth data for the sixth wave of the National Youth Survey<br />\nare contained in this collection. This research project, which was<br />\ndesigned to gain a better understanding of both conventional and<br />\ndeviant types of behavior by youths, involved collecting information<br />\nfrom a representative sample of young people in the United States. The<br />\nfirst wave of this survey was conducted in 1976, the<br />\nsecond wave in 1977, the third wave in 1978,<br />\nthe fourth wave in 1979, and the fifth wave in 1980. For this wave, youths and young adults were interviewed in early<br />\n1984 about events and behavior occurring in calendar year 1983, when<br />\nthey were 17 to 26 years of age. Data are available on the demographic<br />\nand socioeconomic status of respondents, disruptive events for parents,<br />\nneighborhood problems, employment, children, aspirations and current<br />\nsuccesses, normlessness, labeling by parents, perceived disapproval by<br />\nparents, peers, co-workers, and partner, attitudes toward deviance,<br />\nexposure to delinquent peers, self-reported delinquency, drug and<br />\nalcohol use, victimization, pregnancy, depression, use of outpatient<br />\nservices, spouse violence by respondent and partner, and sexual<br />\nactivity.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Youth Survey US: Wave VI (NYS-1983) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-vi-nys-1983-nid13589",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-vi-nys-1983-nid13589"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-vi-nys-1983-nid13589",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "aspirations",
                 "behavior problems",
@@ -130431,69 +130444,32 @@
                 "young adults",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-vi-nys-1983",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-vi-nys-1983-nid13589",
-            "description": "<p>Youth data for the sixth wave of the National Youth Survey<br />\nare contained in this collection. This research project, which was<br />\ndesigned to gain a better understanding of both conventional and<br />\ndeviant types of behavior by youths, involved collecting information<br />\nfrom a representative sample of young people in the United States. The<br />\nfirst wave of this survey was conducted in 1976, the<br />\nsecond wave in 1977, the third wave in 1978,<br />\nthe fourth wave in 1979, and the fifth wave in 1980. For this wave, youths and young adults were interviewed in early<br />\n1984 about events and behavior occurring in calendar year 1983, when<br />\nthey were 17 to 26 years of age. Data are available on the demographic<br />\nand socioeconomic status of respondents, disruptive events for parents,<br />\nneighborhood problems, employment, children, aspirations and current<br />\nsuccesses, normlessness, labeling by parents, perceived disapproval by<br />\nparents, peers, co-workers, and partner, attitudes toward deviance,<br />\nexposure to delinquent peers, self-reported delinquency, drug and<br />\nalcohol use, victimization, pregnancy, depression, use of outpatient<br />\nservices, spouse violence by respondent and partner, and sexual<br />\nactivity.This study has 1 Data Set.</p>",
-            "title": "National Youth Survey US: Wave VI (NYS-1983)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-vi-nys-1983-nid13589",
-                    "description": "National Youth Survey US: Wave VI (NYS-1983) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-vi-nys-1983-nid13589"
-                }
-            ]
+            "title": "National Youth Survey US: Wave VI (NYS-1983)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-hospice",
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
-                "hospice",
-                "hospitals & facilities",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/7f93a63d-f2a2-4d29-b95b-c160185aaf90/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Hospice tables provide use and payment data for hospice.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR HOSPICE 1. \u00a0Medicare Hospices: \u00a0Utilization and Program Payments for Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR HOSPICE 2. \u00a0Medicare Hospices: \u00a0Utilization and Program Payments for Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR HOSPICE 3. \u00a0Medicare Hospices: \u00a0Utilization and Program Payments for Medicare Beneficiaries, by Area of Residence\n\tMDCR HOSPICE 4. \u00a0Medicare Hospices: \u00a0Utilization and Program Payments for Medicare Beneficiaries, by Type of Control and Type of Service Visit\n\tMDCR HOSPICE 5. \u00a0Medicare Hospices: \u00a0Utilization and Program Payments for Medicare Beneficiaries, by Level of Care and Site of Service\n\tMDCR HOSPICE 6. \u00a0Medicare Hospices: \u00a0Utilization and Program Payments for Medicare Beneficiaries, by Number of Service Visits",
-            "title": "CMS Program Statistics - Medicare Hospice",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -130550,54 +130526,53 @@
                     "title": "CMS Program Statistics - Medicare Hospice : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/7f93a63d-f2a2-4d29-b95b-c160185aaf90/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospice",
+                "hospitals & facilities",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-hospice",
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
+            "title": "CMS Program Statistics - Medicare Hospice"
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
-                "brfss",
-                "census tract",
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
-            "identifier": "https://data.cdc.gov/api/views/4ai3-zynv",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
             "description": "This dataset contains model-based census tract-level estimates for the PLACES project 2020 release. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 27 measures: 5 chronic disease-related unhealthy behaviors, 13 health outcomes, and 9 on use of preventive services. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2010 population data, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Census Tract Data 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -130620,99 +130595,95 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
+            "identifier": "https://data.cdc.gov/api/views/4ai3-zynv",
+            "issued": "2021-09-29",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "census tract",
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
+            "title": "PLACES: Local Data for Better Health, Census Tract Data 2020 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2011",
-            "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "alcohol abuse",
-                "drug abuse",
-                "drug treatment",
-                "health care services",
-                "health insurance",
-                "intervention",
-                "mental health",
-                "substance abuse",
-                "substance abuse treatment",
-                "treatment programs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
                 "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Substance Abuse & Mental Health Services Administration"
-            },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2011-nid13594",
             "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and<br />\nhashish, heroin, nonprescription methadone, other opiates and<br />\nsynthetics, PCP, other hallucinogens, methamphetamine, other amphetamines,<br />\nother stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2011)",
-            "programCode": [
-                "009:030"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2011-nid13594",
-                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2011) \n",
                     "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2011) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2011-nid13594",
+                    "mediaType": "text/html",
                     "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2011-nid13594"
                 }
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
-            "bureauCode": [
-                "009:20"
             ],
-            "issued": "2020-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-28",
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2011-nid13594",
+            "issued": "2016-05-23",
             "keyword": [
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "influenza",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "place of death",
-                "pneumonia",
-                "provisional",
-                "puerto rico",
-                "state",
-                "united states",
-                "yearly"
+                "alcohol abuse",
+                "drug abuse",
+                "drug treatment",
+                "health care services",
+                "health insurance",
+                "intervention",
+                "mental health",
+                "substance abuse",
+                "substance abuse treatment",
+                "treatment programs"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2011",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2011)"
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
-            "identifier": "https://data.cdc.gov/api/views/uggs-hy5q",
             "description": "Effective June 28, 2023, this dataset will no longer be updated. Data deaths by place of death are available in this dataset https://data.cdc.gov/NCHS/d/4va6-ph5s.\n\nDeaths involving  COVID-19, pneumonia and influenza reported to NCHS by place of death and state, United States.",
-            "title": "Provisional COVID-19 Deaths by Place of Death and State",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -130735,40 +130706,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/uggs-hy5q",
+            "issued": "2020-05-01",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "influenza",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "place of death",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
+                "state",
+                "united states",
+                "yearly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-06-28",
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
+            "title": "Provisional COVID-19 Deaths by Place of Death and State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/td3v-vb7j",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-10-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-15",
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
-            "identifier": "1bb4e9de-588b-4301-a6a9-523cf621b45b",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 10-07-2024-to-10-13-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -130776,17 +130760,46 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "1bb4e9de-588b-4301-a6a9-523cf621b45b",
+            "issued": "2024-10-23",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/td3v-vb7j",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 10-07-2024-to-10-13-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-us-dawn-ns-1997",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) survey is designed to<br />\ncapture data on emergency department (ED) episodes that are induced by<br />\nor related to the use of an illicit, prescription, or over-the-counter<br />\ndrug. For purposes of this collection, a drug \"episode\" is an ED visit<br />\nthat was induced by or related to the use of an illegal drug or the<br />\nnonmedical use of a legal drug for patients aged six years and<br />\nolder. A drug \"mention\" refers to a substance that was mentioned<br />\nduring a drug-related ED episode. Because up to four drugs can be<br />\nreported for each drug abuse episode, there are more mentions than<br />\nepisodes in the data. Individual persons may also be included more<br />\nthan once in the data. Within each facility participating in DAWN, a<br />\ndesignated reporter, usually a member of the emergency department or<br />\nmedical records staff, was responsible for identifying drug-related<br />\nepisodes and recording and submitting data on each case. An episode<br />\nreport was submitted for each patient visiting a DAWN emergency<br />\ndepartment whose presenting problem(s) was/were related to their own<br />\ndrug use. DAWN produces estimates of drug-related emergency department<br />\nvisits for 50 specific drugs, drug categories, or combinations of<br />\ndrugs, including the following: acetaminophen, alcohol in combination<br />\nwith other drugs, alprazolam, amitriptyline, amphetamines, aspirin,<br />\ncocaine, codeine, diazepam, diphenhydramine, fluoxetine,<br />\nheroin/morphine, inhalants/solvents/aerosols, LSD, lorazepam,<br />\nmarijuana/hashish, methadone, methamphetamine, and PCP/PCP in<br />\ncombination with other drugs. The use of alcohol alone is not<br />\nreported. The route of administration and form of drug used (e.g.,<br />\npowder, tablet, liquid) are included for each drug. Data collected for<br />\nDAWN also include drug use motive and total drug mentions in the<br />\nepisode, as well as race, age, patient disposition, reason for ED<br />\nvisit, and day of the week, quarter, and year of episode.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network US (DAWN-NS-1997) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1997-nid13592",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1997-nid13592"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1997-nid13592",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "demographic characteristics",
                 "drug abuse",
@@ -130799,65 +130812,29 @@
                 "hospitalization",
                 "substance abuse"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-us-dawn-ns-1997",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1997-nid13592",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) survey is designed to<br />\ncapture data on emergency department (ED) episodes that are induced by<br />\nor related to the use of an illicit, prescription, or over-the-counter<br />\ndrug. For purposes of this collection, a drug \"episode\" is an ED visit<br />\nthat was induced by or related to the use of an illegal drug or the<br />\nnonmedical use of a legal drug for patients aged six years and<br />\nolder. A drug \"mention\" refers to a substance that was mentioned<br />\nduring a drug-related ED episode. Because up to four drugs can be<br />\nreported for each drug abuse episode, there are more mentions than<br />\nepisodes in the data. Individual persons may also be included more<br />\nthan once in the data. Within each facility participating in DAWN, a<br />\ndesignated reporter, usually a member of the emergency department or<br />\nmedical records staff, was responsible for identifying drug-related<br />\nepisodes and recording and submitting data on each case. An episode<br />\nreport was submitted for each patient visiting a DAWN emergency<br />\ndepartment whose presenting problem(s) was/were related to their own<br />\ndrug use. DAWN produces estimates of drug-related emergency department<br />\nvisits for 50 specific drugs, drug categories, or combinations of<br />\ndrugs, including the following: acetaminophen, alcohol in combination<br />\nwith other drugs, alprazolam, amitriptyline, amphetamines, aspirin,<br />\ncocaine, codeine, diazepam, diphenhydramine, fluoxetine,<br />\nheroin/morphine, inhalants/solvents/aerosols, LSD, lorazepam,<br />\nmarijuana/hashish, methadone, methamphetamine, and PCP/PCP in<br />\ncombination with other drugs. The use of alcohol alone is not<br />\nreported. The route of administration and form of drug used (e.g.,<br />\npowder, tablet, liquid) are included for each drug. Data collected for<br />\nDAWN also include drug use motive and total drug mentions in the<br />\nepisode, as well as race, age, patient disposition, reason for ED<br />\nvisit, and day of the week, quarter, and year of episode.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network US (DAWN-NS-1997)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1997-nid13592",
-                    "description": "Drug Abuse Warning Network US (DAWN-NS-1997) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-us-dawn-ns-1997-nid13592"
-                }
-            ]
+            "title": "Drug Abuse Warning Network US (DAWN-NS-1997)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -130880,45 +130857,45 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/33kn-dpz2",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "legionellosis",
-                "malaria",
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
-            "identifier": "https://data.cdc.gov/api/views/33kn-dpz2",
             "description": "NNDSS - Table II. Legionellosis to Malaria - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Legionellosis to Malaria",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -130941,21 +130918,72 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/33kn-dpz2",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "legionellosis",
+                "malaria",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/33kn-dpz2",
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
+            "title": "NNDSS - Table II. Legionellosis to Malaria"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/nih-exported-research-portfolio-online-reporting-tools-expenditures-and-results-exporter-0",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NIH RePORT",
+                "hasEmail": "mailto:RePORT@mail.nih.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Research projects funded by the National Institutes of Health (NIH), other DHHS Operating Divisions (ACF, AHRQ, CDC, FDA, HRSA), and the Department of Veterans Affairs.  The ExPORTER files provide weekly and/or yearly snapshots of the data publicly accessible through the NIH Research Portfolio Online Reporting Tools, Expenditures and Results (RePORTER) system at <a href=\"https://reporter.nih.gov\">https://reporter.nih.gov</a>.  The RePORTER database can also be queried using the user interface or the API.  The RePORTER database contains information such as project title, abstract, principal investigator, funded organization, total awarded costs, categorization by area of research (NIH only), and project keywords.  Also available is information on research publications and patents that have cited support from each project.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The data publicly accessible through the NIH Research Portfolio Online Reporting Tools, Expenditures and Results (RePORTER) system can be accessed in 3 ways:\n1. Download the bulk data in CSV format with ExPORTER files\n2. Search using the RePORTER user interface\n3. Retrieve data with the RePORTER API",
+                    "downloadURL": "https://reporter.nih.gov/advanced-search",
+                    "mediaType": "text/html",
+                    "title": "RePORTER"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The data publicly accessible through the NIH Research Portfolio Online Reporting Tools, Expenditures and Results (RePORTER) system can be accessed in 3 ways:\n1. Download the bulk data in CSV format with ExPORTER files\n2. Search using the RePORTER user interface\n3. Retrieve data with the RePORTER API",
+                    "downloadURL": "https://exporter.nih.gov/",
+                    "mediaType": "text/csv",
+                    "title": "RePORTER"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The data publicly accessible through the NIH Research Portfolio Online Reporting Tools, Expenditures and Results (RePORTER) system can be accessed in 3 ways:\n1. Download the bulk data in CSV format with ExPORTER files\n2. Search using the RePORTER user interface\n3. Retrieve data with the RePORTER API",
+                    "downloadURL": "https://api.reporter.nih.gov",
+                    "mediaType": "text/html",
+                    "title": "RePORTER"
+                }
+            ],
+            "identifier": "8f4db285-46c8-445b-9541-9833a9e1d316",
             "issued": "2012-05-30",
-            "temporal": "1985-01-01T00:00:00-05:00/2021-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "acf",
                 "ahrq",
@@ -130983,78 +131011,35 @@
                 "research",
                 "va"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NIH RePORT",
-                "hasEmail": "mailto:RePORT@mail.nih.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
-            },
-            "identifier": "8f4db285-46c8-445b-9541-9833a9e1d316",
-            "description": "<p>Research projects funded by the National Institutes of Health (NIH), other DHHS Operating Divisions (ACF, AHRQ, CDC, FDA, HRSA), and the Department of Veterans Affairs.  The ExPORTER files provide weekly and/or yearly snapshots of the data publicly accessible through the NIH Research Portfolio Online Reporting Tools, Expenditures and Results (RePORTER) system at <a href=\"https://reporter.nih.gov\">https://reporter.nih.gov</a>.  The RePORTER database can also be queried using the user interface or the API.  The RePORTER database contains information such as project title, abstract, principal investigator, funded organization, total awarded costs, categorization by area of research (NIH only), and project keywords.  Also available is information on research publications and patents that have cited support from each project.</p>",
-            "title": "NIH Research Portfolio Online Reporting Tools: Expenditures and Results (RePORTER)",
+            "landingPage": "https://healthdata.gov/dataset/nih-exported-research-portfolio-online-reporting-tools-expenditures-and-results-exporter-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:046"
             ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://reporter.nih.gov/advanced-search",
-                    "description": "The data publicly accessible through the NIH Research Portfolio Online Reporting Tools, Expenditures and Results (RePORTER) system can be accessed in 3 ways:\n1. Download the bulk data in CSV format with ExPORTER files\n2. Search using the RePORTER user interface\n3. Retrieve data with the RePORTER API",
-                    "@type": "dcat:Distribution",
-                    "title": "RePORTER"
-                },
-                {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://exporter.nih.gov/",
-                    "description": "The data publicly accessible through the NIH Research Portfolio Online Reporting Tools, Expenditures and Results (RePORTER) system can be accessed in 3 ways:\n1. Download the bulk data in CSV format with ExPORTER files\n2. Search using the RePORTER user interface\n3. Retrieve data with the RePORTER API",
-                    "@type": "dcat:Distribution",
-                    "title": "RePORTER"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
             },
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://api.reporter.nih.gov",
-                    "description": "The data publicly accessible through the NIH Research Portfolio Online Reporting Tools, Expenditures and Results (RePORTER) system can be accessed in 3 ways:\n1. Download the bulk data in CSV format with ExPORTER files\n2. Search using the RePORTER user interface\n3. Retrieve data with the RePORTER API",
-                    "@type": "dcat:Distribution",
-                    "title": "RePORTER"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "accrualPeriodicity": "R/P1W",
+            "temporal": "1985-01-01T00:00:00-05:00/2021-12-31T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "NIH Research Portfolio Online Reporting Tools: Expenditures and Results (RePORTER)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/teis-u4xt",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-03",
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
-            "identifier": "83216270-4c25-4d9a-a670-4d5da10ed78c",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-25-to-2023-12-31",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131063,44 +131048,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-25-to-2023-12-31"
                 }
             ],
+            "identifier": "83216270-4c25-4d9a-a670-4d5da10ed78c",
+            "issued": "2024-01-08",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/teis-u4xt",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-01-03",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-12-25-to-2023-12-31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4t6w-ibvk",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "botulism",
-                "foodborne",
-                "infant",
-                "nedss",
-                "netss",
-                "nndss",
-                "other (wound and unspecified)",
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
-            "identifier": "https://data.cdc.gov/api/views/4t6w-ibvk",
             "description": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified) - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1E. Botulism, Foodborne to Botulism, Other",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131123,48 +131099,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4t6w-ibvk",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "botulism",
+                "foodborne",
+                "infant",
+                "nedss",
+                "netss",
+                "nndss",
+                "other (wound and unspecified)",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4t6w-ibvk",
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
+            "title": "NNDSS - TABLE 1E. Botulism, Foodborne to Botulism, Other"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/medicaid-restricted.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-12-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2014/2019",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/NCHS-CMS-TMSIS-linked-data-list-of-variables.pdf"
-            ],
-            "keyword": [
-                "linked medicaid files",
-                "nchs surveys",
-                "research-data-center",
-                "t-msis"
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
-            "identifier": "https://data.cdc.gov/api/views/5cg4-4qqe",
-            "description": "NCHS has linked various surveys with Medicaid enrollment and claims records collected from the Centers for Medicare & Medicaid Services (CMS) Transformed Medicaid Statistical Information System (T-MSIS). Linkage of the NCHS survey participants with the CMS T-MSIS data creates a new data resource that can support research studies focused on a wide range of patient health outcomes and the association of means-tested government insurance programs on health and health outcomes.",
-            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) Medicaid Enrollment and Claims Files",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/NCHS-TMSIS-MATCH-STATUS.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "NCHS has linked various surveys with Medicaid enrollment and claims records collected from the Centers for Medicare & Medicaid Services (CMS) Transformed Medicaid Statistical Information System (T-MSIS). Linkage of the NCHS survey participants with the CMS T-MSIS data creates a new data resource that can support research studies focused on a wide range of patient health outcomes and the association of means-tested government insurance programs on health and health outcomes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131172,44 +131148,49 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/NCHS-TMSIS-MATCH-STATUS.pdf",
+            "identifier": "https://data.cdc.gov/api/views/5cg4-4qqe",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-12-20",
+            "keyword": [
+                "linked medicaid files",
+                "nchs surveys",
+                "research-data-center",
+                "t-msis"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/medicaid-restricted.htm",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/NCHS-CMS-TMSIS-linked-data-list-of-variables.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "2014/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) Medicaid Enrollment and Claims Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/office-head-start-ohs-program-fact-sheet",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-12-18",
-            "temporal": "2004-01-01T00:00:00-05:00/2004-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "administration-for-children-and-families-department-of-health-human-services",
-                "administrative",
-                "children's health",
-                "population statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jesse Escobar",
                 "hasEmail": "mailto:jesse.escobar@acf.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Administration for Children and Families, Department of Health & Human Services"
-            },
-            "identifier": "5a79e346-f10e-4820-a303-7b86f1ce5322",
+            "dataQuality": true,
             "description": "<p>Office of Head Start (OHS) Program Fact Sheet provides information on demographics, state allocations, program statistics, and program enrollment history.</p>",
-            "title": "Office of Head Start (OHS) Program Fact Sheet",
-            "programCode": [
-                "009:092"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131218,39 +131199,39 @@
                     "title": "HTML"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "5a79e346-f10e-4820-a303-7b86f1ce5322",
+            "issued": "2013-12-18",
+            "keyword": [
+                "administration-for-children-and-families-department-of-health-human-services",
+                "administrative",
+                "children's health",
+                "population statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/office-head-start-ohs-program-fact-sheet",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:092"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "temporal": "2004-01-01T00:00:00-05:00/2004-01-01T00:00:00-05:00",
+            "title": "Office of Head Start (OHS) Program Fact Sheet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://metamap.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2012-08-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "medical informatics",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xnpy-mnxp",
             "description": "MetaMap is a highly configurable application developed by the Lister Hill National Center for Biomedical Communications at the National Library of Medicine (NLM) to map biomedical text to the UMLS Metathesaurus or, equivalently, to identify Metathesaurus concepts referred to in English text. MetaMap employs a knowledge-intensive approach, natural-language processing (NLP), and computational-linguistic techniques, and is used worldwide in industry and academia. At NLM, MetaMap is one of the foundations of NLM's Medical Text Indexer (MTI), which is applied to both semiautomatic and fully automatic indexing of biomedical literature.  Technical documentation at http://metamap.nlm.nih.gov/#Downloads",
-            "title": "MetaMap",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131259,53 +131240,51 @@
                     "title": "API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xnpy-mnxp",
+            "issued": "2012-08-22",
+            "keyword": [
+                "api",
+                "medical informatics",
+                "terminologies",
+                "tools & utilities"
+            ],
+            "landingPage": "https://metamap.nlm.nih.gov/",
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
+            "title": "MetaMap"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/rural-health-clinic-all-owners",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/ab03c9bc-0c22-4ca4-b032-21dd3408210d/data-viewer",
-            "description": "The Rural Health Clinic (RHC) All Owners dataset provides ownership information on all \u00a0RHCs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
-            "title": "Rural Health Clinic All Owners",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-09/RHC_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Rural Health Clinic (RHC) All Owners dataset provides ownership information on all \u00a0RHCs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ab03c9bc-0c22-4ca4-b032-21dd3408210d/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ab03c9bc-0c22-4ca4-b032-21dd3408210d/data",
+                    "mediaType": "text/html",
                     "title": "Rural Health Clinic All Owners : 2025-01-01"
                 },
                 {
@@ -131381,52 +131360,51 @@
                     "title": "Rural Health Clinic All Owners : 2023-10-29"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-09/RHC_All_Owners_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/ab03c9bc-0c22-4ca4-b032-21dd3408210d/data-viewer",
+            "issued": "2023-12-08",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "outpatient facilities",
+                "provider enrollment",
+                "rural health clinics"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/rural-health-clinic-all-owners",
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
+            "title": "Rural Health Clinic All Owners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-sexually-transmitted-disease-std-morbidity-0",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-08-01",
-            "temporal": "1984-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "age",
-                "case",
-                "epidemiology",
-                "incidence",
-                "morbidity",
-                "sex race ethnicity year state puerto rico virgin islands guam",
-                "sexually transmitted disease",
-                "std"
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
-            "identifier": "9731c732-b001-4413-81ce-a4345df220c6",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/std.html",
             "description": "<p>The Sexually Transmitted Disease (STD) Morbidity online databases on CDC WONDER contain case reports reported from the 50 United States and D.C., Puerto Rico, Virgin Islands and Guam. The online databases report the number of cases and disease incidence rates by year, state, disease, age, gender of patient, type of STD, and area of report, since 1984. Data are updated annually. Data are produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
-            "title": "CDC WONDER: Sexually Transmitted Disease (STD) morbidity",
-            "programCode": [
-                "009:027"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131435,41 +131413,46 @@
                     "title": "Text "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/std.html",
-            "dataQuality": true,
+            "identifier": "9731c732-b001-4413-81ce-a4345df220c6",
+            "issued": "2012-08-01",
+            "keyword": [
+                "age",
+                "case",
+                "epidemiology",
+                "incidence",
+                "morbidity",
+                "sex race ethnicity year state puerto rico virgin islands guam",
+                "sexually transmitted disease",
+                "std"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-sexually-transmitted-disease-std-morbidity-0",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:027"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1984-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Sexually Transmitted Disease (STD) morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g4ag-jrdn",
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
-            "identifier": "https://data.cdc.gov/api/views/g4ag-jrdn",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 2 - New York",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131492,53 +131475,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g4ag-jrdn",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/g4ag-jrdn",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 2 - New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-referring-provider",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/f8603e5b-9c47-4c52-9b47-a4ef92dfada4/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-referring-provider-data-dictionary",
             "description": "The Medicare Durable Medical Equipment, Devices & Supplies by Referring Provider dataset contains information on usage, payments, submitted charges and beneficiary demographic and health characteristics organized by National Provider Identifier (NPI).",
-            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f8603e5b-9c47-4c52-9b47-a4ef92dfada4/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f8603e5b-9c47-4c52-9b47-a4ef92dfada4/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider : 2022-12-30"
                 },
                 {
@@ -131650,45 +131628,51 @@
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider : 2014-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-referring-provider-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/f8603e5b-9c47-4c52-9b47-a4ef92dfada4/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medical suppliers & equipment",
+                "medicare",
+                "original medicare",
+                "physicians & practitioners"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-referring-provider",
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
+            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/places/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "keyword": [
-                "500 cities",
-                "places"
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
-            "identifier": "https://data.cdc.gov/api/views/m35w-spkz",
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities-Places/PLACES-and-500-Cities-Data-Dictionary/m35w-spkz",
             "description": "This dataset provides a data dictionary for PLACES and 500 Cities releases.  For each measure, the data dictionary provides the measure ID, measure full and short name, measure category ID and name, year of BRFSS data used to generate the estimate by release year, and frequency BRFSS collects data about the measure.",
-            "title": "PLACES and 500 Cities: Data Dictionary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131711,42 +131695,39 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities-Places/PLACES-and-500-Cities-Data-Dictionary/m35w-spkz",
+            "identifier": "https://data.cdc.gov/api/views/m35w-spkz",
+            "issued": "2024-08-26",
+            "keyword": [
+                "500 cities",
+                "places"
+            ],
+            "landingPage": "https://www.cdc.gov/places/index.html",
             "license": "https://www.usa.gov/government-works",
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
+            "title": "PLACES and 500 Cities: Data Dictionary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/u4vw-xsmf",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-04-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
-            "keyword": [
-                "covid-19 vaccination",
-                "covid tracker",
-                "disability",
-                "hps"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/u4vw-xsmf",
             "description": "Household Pulse Survey (HPS): HPS is a rapid-response survey of adults ages \u226518 years led by the U.S. Census Bureau, in partnership with seven other federal statistical agencies, to measure household experiences during the COVID-19 pandemic. Detailed information on probability sampling using the U.S. Census Bureau\u2019s Master Address File, questionnaires, response rates, and bias assessment is available on the Census Bureau website (https://www.census.gov/data/experimental-data-products/household-pulse-survey.html).\n\nData from adults ages \u226518 years and older are collected by a 20-minute online survey from randomly sampled households stratified by state and the top 15 metropolitan statistical areas (MSAs). Data are weighted to represent total persons ages 18 and older living within households and to mitigate possible bias that can result from non-responses and incomplete survey frame. Data from adults ages \u226518 years and older are collected by 20-minute online survey from randomly sampled households stratified by state and the top 15 metropolitan statistical areas (MSAs). For more information on this survey, see https://www.census.gov/programs-surveys/household-pulse-survey.html.\n\nData are weighted to represent total persons ages 18 and older living within households and to mitigate possible bias that can result from non-responses and incomplete survey frame. Responses in the Household Pulse Survey (https://www.census.gov/programs-surveys/household-pulse-survey.html) are self-reported. Estimates of vaccination coverage may differ from vaccine administration data reported at COVID-19 Vaccinations in the United States (https://covid.cdc.gov/covid-data-tracker/#vaccinations).",
-            "title": "Household Pulse Survey (HPS): COVID-19 Vaccination among People with Disabilities",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131769,20 +131750,50 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/u4vw-xsmf",
+            "issued": "2023-04-04",
+            "keyword": [
+                "covid-19 vaccination",
+                "covid tracker",
+                "disability",
+                "hps"
+            ],
+            "landingPage": "https://data.cdc.gov/d/u4vw-xsmf",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-27",
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
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225433.htm",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "Contains data for FDA recalls from 2009 through the present.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/DataSets/Recalls/RecallsDataSet.xml",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "d4959928-1229-4fff-a32e-704245f42cb6",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "animal health",
                 "biologics",
@@ -131796,66 +131807,31 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225433.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "d4959928-1229-4fff-a32e-704245f42cb6",
-            "description": "Contains data for FDA recalls from 2009 through the present.",
-            "title": "All FDA Recalls",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fda.gov/DataSets/Recalls/RecallsDataSet.xml",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "All FDA Recalls"
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
-                "Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
-            ],
-            "keyword": [
-                "children",
-                "flu",
-                "flu shot",
-                "influenza",
-                "nis",
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
-            "identifier": "https://data.cdc.gov/api/views/2den-c3u2",
             "description": "Cumulative Influenza Vaccination Coverage Differences by Race/Ethnicity, Children 6 months through 17 years, United States Vaccinations \n\n\u2022 Influenza vaccination coverage among children is assessed through the National Immunization Survey-Flu (NIS-Flu) annually, providing weekly influenza vaccination coverage estimates for children 6 months\u201317 years based upon parental report. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)  \n\no NIS-Flu is a national random-digit-dialed cellular telephone survey of households conducted during the flu season (October-June).  \n\n\u2022 Final estimates for prior seasons and other flu vaccination data are available at CDC\u2019s FluVaxView:  https://www.cdc.gov/flu/fluvaxview/index.htm.",
-            "title": "Cumulative Influenza Vaccination Coverage Differences by Race/Ethnicity, Children 6 months through 17 years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131878,47 +131854,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/2den-c3u2",
+            "issued": "2023-12-01",
+            "keyword": [
+                "children",
+                "flu",
+                "flu shot",
+                "influenza",
+                "nis",
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
+                "Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
+            ],
+            "spatial": "United States",
+            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Cumulative Influenza Vaccination Coverage Differences by Race/Ethnicity, Children 6 months through 17 years, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/gap/",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/iq5v-eu5s",
             "description": "Database of Genotype and Phenotype (dbGaP) was developed to archive and distribute the data and results from studies that have investigated the interaction of genotype and phenotype in Humans.",
-            "title": "Database of Genotype and Phenotype (dbGaP)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131933,47 +131913,44 @@
                     "title": "Download dbGap Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/iq5v-eu5s",
+            "issued": "2021-06-17",
+            "keyword": [
+                "dataset",
+                "genetics",
+                "genomics",
+                "software",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/gap/",
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
+            "title": "Database of Genotype and Phenotype (dbGaP)"
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
-            ],
-            "keyword": [
-                "linked hud files",
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
-            "identifier": "https://data.cdc.gov/api/views/xcz7-jei9",
-            "description": "NCHS has linked 1999-2018 National Health Interview Survey (NHIS) and 1999-2018 National Health and Nutrition Examination Survey (NHANES) to administrative data through 2019 for the Department of Housing and Urban Development\u2019s (HUD) largest housing assistance programs: the Housing Choice Voucher program, public housing, and privately owned, subsidized multifamily housing. Linkage of NCHS survey participants with HUD administrative records provides the opportunity to examine relationships between housing and health.",
-            "title": "NCHS Survey Data Linked to the Department of Housing and Urban Development (HUD) Housing Assistance Program Files",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/NCHS-HUD-Match-Rate-Tables-final.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "NCHS has linked 1999-2018 National Health Interview Survey (NHIS) and 1999-2018 National Health and Nutrition Examination Survey (NHANES) to administrative data through 2019 for the Department of Housing and Urban Development\u2019s (HUD) largest housing assistance programs: the Housing Choice Voucher program, public housing, and privately owned, subsidized multifamily housing. Linkage of NCHS survey participants with HUD administrative records provides the opportunity to examine relationships between housing and health.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -131981,46 +131958,47 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/NCHS-HUD-Match-Rate-Tables-final.pdf",
+            "identifier": "https://data.cdc.gov/api/views/xcz7-jei9",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-16",
+            "keyword": [
+                "linked hud files",
+                "nchs surveys",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/hud-restricted.htm",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/weight-file.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
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
-            "landingPage": "https://data.cdc.gov/d/mk6z-83q2",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "age <5",
-                "invasive pneumococcal disease",
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
-            "identifier": "https://data.cdc.gov/api/views/mk6z-83q2",
             "description": "NNDSS - Table II. Invasive pneumococcal disease, age <5 - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 Includes drug resistant and susceptible cases of invasive pneumococcal disease.",
-            "title": "NNDSS - Table II. Invasive pneumococcal disease, age <5",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132043,98 +132021,93 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mk6z-83q2",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "age <5",
+                "invasive pneumococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mk6z-83q2",
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
+            "title": "NNDSS - Table II. Invasive pneumococcal disease, age <5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/thds-yxwf",
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
-            "identifier": "58e99d2d-ea9f-5a30-a509-43c0c350072f",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_map",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/map.csv",
-                    "description": "{\"dataset\": \"map\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"map\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/map.csv",
+                    "mediaType": "text/csv",
                     "title": "map csv file"
                 }
             ],
+            "identifier": "58e99d2d-ea9f-5a30-a509-43c0c350072f",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/thds-yxwf",
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
+            "title": "implAuto_map"
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
@@ -132157,43 +132130,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
+            "identifier": "https://data.cdc.gov/api/views/duw2-7jbt",
+            "issued": "2023-06-15",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "county",
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
+            "title": "PLACES: Local Data for Better Health, County Data 2022 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "temporal": "1976-01-01/2013-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
-            "references": [
-                "http://www.fda.gov/MedicalDevices/ProductsandMedicalProcedures/DeviceApprovalsandClearances/510kClearances/ucm089428.htm"
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
-            "identifier": "142e5da1-24f6-4215-83e5-18a7cd813889",
             "description": "Medical device manufacturers are required to submit a premarket notification or 510(k) if they intend to introduce a device into commercial distribution for the first time or reintroduce a device that will be significantly changed or modified to the extent that its safety or effectiveness could be affected. This database of releasable 510(k)s can be searched by 510(k) number, applicant, device name or FDA product code. Summaries of safety and effectiveness information is available via the web interface for more recent records.",
-            "title": "Premarket Notifications (510(k)s)",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132201,33 +132182,39 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "142e5da1-24f6-4215-83e5-18a7cd813889",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1M"
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/MedicalDevices/ProductsandMedicalProcedures/DeviceApprovalsandClearances/510kClearances/ucm089428.htm"
+            ],
+            "temporal": "1976-01-01/2013-12-31",
+            "title": "Premarket Notifications (510(k)s)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/c294-dri5",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -132235,39 +132222,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/c294-dri5",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/c294-dri5",
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
+            "title": "Trends in Worker Hearing Loss by Industry Sector, 1981-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/28km-nz6e",
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
-            "identifier": "https://data.cdc.gov/api/views/28km-nz6e",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 4 - Atlanta",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132290,35 +132273,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/28km-nz6e",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/28km-nz6e",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 4 - Atlanta"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/2m7c-st88",
-            "issued": "2024-11-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC Prevention Research Centers Contact",
                 "hasEmail": "mailto:prcprogram@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2m7c-st88",
             "description": "The P2P Resource Center is a one-stop, easy-to-navigate website that features tools and resources produced by CDC-funded PRC research projects. Community organizations and public health practitioners can tailor these resources to identify, replicate, and use key aspects of successful public health programs and inspire others to expand the uptake and use of evidence-based interventions. It also includes information on previous or current research from the PRC Network.",
-            "title": "Pathway to Practice (P2P) Resource Center",
-            "programCode": [
-                "009:029"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132341,43 +132328,32 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/2m7c-st88",
+            "issued": "2024-11-19",
+            "landingPage": "https://data.cdc.gov/d/2m7c-st88",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-19",
+            "programCode": [
+                "009:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "Pathway to Practice (P2P) Resource Center"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/29js-qshz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/29js-qshz",
             "description": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Includes data for dengue and dengue-like illness.",
-            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132400,20 +132376,71 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/29js-qshz",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/29js-qshz",
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
+            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue"
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
+            "description": "Provisional counts of deaths by the month the deaths occurred, by age group and HHS region, for select underlying causes of death for 2019-2020. The dataset also includes monthly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/ezfr-g6hf",
             "issued": "2020-09-04",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
             "keyword": [
                 "age",
                 "age group",
@@ -132442,89 +132469,36 @@
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
-            "identifier": "https://data.cdc.gov/api/views/ezfr-g6hf",
-            "description": "Provisional counts of deaths by the month the deaths occurred, by age group and HHS region, for select underlying causes of death for 2019-2020. The dataset also includes monthly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
-            "title": "AH Monthly Provisional Counts of Deaths by Age Group and HHS region for Select Causes of Death, 2019-2021",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Monthly Provisional Counts of Deaths by Age Group and HHS region for Select Causes of Death, 2019-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/namcs-linkage.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2024-10-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2021/2022",
-            "modified": "2024-10-23",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/NAMCS-HC-Codebook-Mortality-Variables.pdf"
-            ],
-            "keyword": [
-                "linked ndi data",
-                "namcs",
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
-            "identifier": "https://data.cdc.gov/api/views/h5rx-ppfj",
-            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the 2021 National Ambulatory Medical Care Survey (NAMCS) by augmenting it with mortality data from the National Death Index (NDI). Linkage of NAMCS data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality.",
-            "title": "National Ambulatory Medical Care Survey (NAMCS) Linked to National Death Index (NDI) Data",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 9) here: https://www.cdc.gov/nchs/data/datalinkage/NAMCS-HC-NDI-Methodology-Analytic-Considerations.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the 2021 National Ambulatory Medical Care Survey (NAMCS) by augmenting it with mortality data from the National Death Index (NDI). Linkage of NAMCS data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132532,46 +132506,49 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 9) here: https://www.cdc.gov/nchs/data/datalinkage/NAMCS-HC-NDI-Methodology-Analytic-Considerations.pdf",
+            "identifier": "https://data.cdc.gov/api/views/h5rx-ppfj",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2024-10-23",
+            "keyword": [
+                "linked ndi data",
+                "namcs",
+                "research-data-center",
+                "sdoh-access-to-health-care",
+                "sdoh-source-of-health-care",
+                "sdoh-use-of-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/namcs-linkage.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data/datalinkage/NAMCS-HC-Codebook-Mortality-Variables.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "temporal": "2021/2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey (NAMCS) Linked to National Death Index (NDI) Data"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -132594,57 +132571,48 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality"
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
-            "issued": "2024-02-27",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2023",
-            "modified": "2024-08-12",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/48ev-2ygq",
-            "description": "List of footnotes, notes, and source information for NHIS Child Summary Statistics. Each row of this dataset contains the accompanying text for a footnote found in the NHIS Child Summary Statistics Dataset.",
-            "title": "DQS NHIS Children Summary Statistics Footnotes",
-            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "describedBy": "https://www.cdc.gov/nchs/data/nhis/SHS_Tech_Notes.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "List of footnotes, notes, and source information for NHIS Child Summary Statistics. Each row of this dataset contains the accompanying text for a footnote found in the NHIS Child Summary Statistics Dataset.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132667,50 +132635,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/nhis/SHS_Tech_Notes.pdf",
+            "identifier": "https://data.cdc.gov/api/views/48ev-2ygq",
+            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "issued": "2024-02-27",
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
+            "modified": "2024-08-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
+            "title": "DQS NHIS Children Summary Statistics Footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-28",
-            "references": [
-                "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/"
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
-            "identifier": "https://data.cdc.gov/api/views/44rk-q6r2",
             "description": "This dataset describes drug poisoning deaths at the U.S. and state level by selected demographic characteristics, and includes age-adjusted death rates for drug poisoning. \n\nDeaths are classified using the International Classification of Diseases, Tenth Revision (ICD\u201310). Drug-poisoning deaths are defined as having ICD\u201310 underlying cause-of-death codes X40\u2013X44 (unintentional), X60\u2013X64 (suicide), X85 (homicide), or Y10\u2013Y14 (undetermined intent).\n\nEstimates are based on the National Vital Statistics System multiple cause-of-death mortality files (1). Age-adjusted death rates (deaths per 100,000 U.S. standard population for 2000) are calculated using the direct method. Populations used for computing death rates for 2011\u20132017 are postcensal estimates based on the 2010 U.S. census. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\n\nDeath rates for some states and years may be low due to a high number of unresolved pending cases or misclassification of ICD\u201310 codes for unintentional poisoning as R99, \u201cOther ill-defined and unspecified causes of mortality\u201d (2). For example, this issue is known to affect New Jersey in 2009 and West Virginia in 2005 and 2009 but also may affect other years and other states. Drug poisoning death rates may be underestimated in those instances.\n\nREFERENCES\n1. National Center for Health Statistics. National Vital Statistics System: Mortality data. Available from: http://www.cdc.gov/nchs/deaths.htm.\n\n2. CDC. CDC Wonder: Underlying cause of death 1999\u20132016. Available from: http://wonder.cdc.gov/wonder/help/ucd.html.",
-            "title": "NCHS - Drug Poisoning Mortality by State: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132733,51 +132708,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/44rk-q6r2",
+            "issued": "2019-04-26",
+            "keyword": [
+                "deaths",
+                "drug poisoning",
+                "mortality",
+                "national",
+                "nchs",
+                "state",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm",
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
+                "https://www.cdc.gov/nchs/data-visualization/drug-poisoning-mortality/"
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
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-28",
-            "keyword": [
-                "age",
-                "age group",
-                "cancer",
-                "deaths",
-                "hispanic origin",
-                "monthly",
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
-            "identifier": "https://data.cdc.gov/api/views/2na8-fe6s",
             "description": "Provisional death counts of malignant neoplasms (cancer) by month and year, and other selected demographics, for 2020-2021. Data are based on death certificates for U.S. residents.",
-            "title": "AH Provisional Cancer Death Counts by Month and Year, 2020-2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132800,42 +132773,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2na8-fe6s",
+            "issued": "2021-06-15",
+            "keyword": [
+                "age",
+                "age group",
+                "cancer",
+                "deaths",
+                "hispanic origin",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "sex",
+                "united states"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
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
+            "title": "AH Provisional Cancer Death Counts by Month and Year, 2020-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/office-refugee-resettlement-orr-overseas-refugee-arrival-data-fy-2010",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-12-13",
-            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "administration-for-children-and-families-department-of-health-human-services",
-                "administrative",
-                "population statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Schmalz",
                 "hasEmail": "mailto:jennifer.schmalz@acf.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Administration for Children and Families, Department of Health & Human Services"
-            },
-            "identifier": "a36cb33e-2ef6-413b-9bfb-573dec1f618d",
+            "dataQuality": true,
             "description": "<p>Office of Refugee Resettlement (ORR) Overseas Refugee Arrival Data FY 2010 sorted by country of origin and state of initial resettlement in the United States</p>",
-            "title": "Office of Refugee Resettlement (ORR) Overseas Refugee Arrival Data FY 2010",
-            "programCode": [
-                "009:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132844,42 +132826,38 @@
                     "title": "HTML "
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "a36cb33e-2ef6-413b-9bfb-573dec1f618d",
+            "issued": "2013-12-13",
+            "keyword": [
+                "administration-for-children-and-families-department-of-health-human-services",
+                "administrative",
+                "population statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/office-refugee-resettlement-orr-overseas-refugee-arrival-data-fy-2010",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "title": "Office of Refugee Resettlement (ORR) Overseas Refugee Arrival Data FY 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n24i-76tn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "all ages",
-                "invasive pneumococcal disease",
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
-            "identifier": "https://data.cdc.gov/api/views/n24i-76tn",
             "description": "NNDSS - Table II. Invasive pneumococcal disease, all ages - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum.\r\n \r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 Includes drug resistant and susceptible cases of invasive pneumococcal disease.",
-            "title": "NNDSS - Table II. Invasive pneumococcal disease, all ages",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -132902,44 +132880,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n24i-76tn",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "all ages",
+                "invasive pneumococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n24i-76tn",
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
+            "title": "NNDSS - Table II. Invasive pneumococcal disease, all ages"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -132962,38 +132940,44 @@
                     "mediaType": "application/xml"
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
+            "title": "Vaccination Coverage among Nursing Home Residents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/tppf-bjgq",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-10-23",
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
-            "identifier": "ac74549c-a621-4f6b-a42d-1a05bc0eb5a3",
             "description": "Dataset.",
-            "title": "2022 Managed Care Programs By State",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133001,21 +132985,46 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "ac74549c-a621-4f6b-a42d-1a05bc0eb5a3",
+            "issued": "2024-10-23",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/tppf-bjgq",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "2022 Managed Care Programs By State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-state",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2014-06-01",
-            "references": [
-                "https://www.healthit.gov/data/data-briefs/e-prescribing-trends-united-states",
-                "https://www.healthit.gov/data/quickstats/electronic-health-record-adoption-and-electronic-prescribing"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-state",
+            "description": "Electronic prescribing (eRx) is a key component of the meaningful use of health IT to improve health care quality and lower costs. This dataset includes national and state eRx and health information exchange activity by community pharmacies and office-based health care providers active through the Surescripts Network. Surescripts is a health information network, and ONC procured electronic prescribing activity data conducted within its network from December 2008 through April 2014. The Surescripts network is used by the majority of all U.S. community pharmacies to rout prescriptions, excluding closed systems such as Kaiser Permanente. These include chain, franchise, and independently owned pharmacies. Data for annual percentages of new and renewal prescriptions routed through the Surescripts network exclude controlled substances. You may view more information about Surescripts, contact the company, and access more network data through the company's official site.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/Surescripts_04-2014_State.csv",
+                    "mediaType": "text/csv",
+                    "title": "Surescripts_04-2014_State.csv"
+                }
             ],
+            "identifier": "0lydsyj1-d79k-3mnz-kwfn-imuzpx5q4tyn",
+            "issued": "2023-10-03",
             "keyword": [
                 "doctors",
                 "ehr",
@@ -133026,55 +133035,33 @@
                 "physicians",
                 "state"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-state",
+            "modified": "2014-06-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "0lydsyj1-d79k-3mnz-kwfn-imuzpx5q4tyn",
-            "description": "Electronic prescribing (eRx) is a key component of the meaningful use of health IT to improve health care quality and lower costs. This dataset includes national and state eRx and health information exchange activity by community pharmacies and office-based health care providers active through the Surescripts Network. Surescripts is a health information network, and ONC procured electronic prescribing activity data conducted within its network from December 2008 through April 2014. The Surescripts network is used by the majority of all U.S. community pharmacies to rout prescriptions, excluding closed systems such as Kaiser Permanente. These include chain, franchise, and independently owned pharmacies. Data for annual percentages of new and renewal prescriptions routed through the Surescripts network exclude controlled substances. You may view more information about Surescripts, contact the company, and access more network data through the company's official site.",
-            "title": "Electronic Prescribing Adoption and Use by State",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/Surescripts_04-2014_State.csv",
-                    "mediaType": "text/csv",
-                    "title": "Surescripts_04-2014_State.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/data-briefs/e-prescribing-trends-united-states",
+                "https://www.healthit.gov/data/quickstats/electronic-health-record-adoption-and-electronic-prescribing"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-state"
+            "title": "Electronic Prescribing Adoption and Use by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5bep-4fv6",
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
-            "identifier": "https://data.cdc.gov/api/views/5bep-4fv6",
             "description": "Healthcare workers concurrently may be at a higher risk of developing respiratory infections and allergic disease, such as asthma, than the general public. Increased incidence of allergic diseases is thought to be caused, in part, due to occupational exposure to chemicals that induce or augment Th2 immune responses. However, whether exposure to these chemical antimicrobials can influence immune responses to respiratory pathogens is unknown. Here, we use a BALB/c murine model to test if the Th2-promoting antimicrobial chemical triclosan influences immune responses to influenza A virus. Mice were dermally exposed to 2% triclosan for 7 days prior to infection with a sub-lethal dose of mouse adapted PR8 A(H1N1) virus (50 pfu); triclosan exposure continued until 10 days post infection (dpi). Infected mice exposed to triclosan did not show an increase in morbidity or mortality, and viral titers were unchanged. Assessment of T cell responses at 10 dpi showed a decrease in the number of total and activated (CD44hi) CD4+ and CD8+ T cells at the site of infection (BAL and lung) in triclosan exposed mice compared to controls. Influenza-specific CD4+ and CD8+ T cells were assessed using MHCI and MHCII tetramers, with reduced populations, although not reaching statistical significance at these sites following triclosan exposure. Reductions in the Th1 transcription factor T-bet were seen in both activated and tetramer+ CD4+ and CD8+ T cells in the lungs of triclosan exposed infected mice, indicating reduced Th1 polarization and providing a potential mechanism for numerical reduction in T cells. Overall, these results indicate that the immune environment induced by triclosan exposure has the potential to influence the developing immune response to a respiratory viral infection and may have implications for healthcare workers who may be at an increased risk for developing infectious diseases.",
-            "title": "Effects of antimicrobial chemical exposures on influenza vaccination and antiviral immunity",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133082,35 +133069,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5bep-4fv6",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/5bep-4fv6",
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
+            "title": "Effects of antimicrobial chemical exposures on influenza vaccination and antiviral immunity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4m2e-y29d",
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
-            "identifier": "https://data.cdc.gov/api/views/4m2e-y29d",
             "description": "Occupational exposure to 4,4\u2019-methylene diphenyl diisocyanate (MDI), the most widely used monomeric diisocyanate, is one of the leading causes of occupational asthma (OA). Pathophysiological mechanism(s) by which how MDI causes OA is still warranted to be elucidated. Alveolar macrophages are the most abundant immune cell type in the lung, and these cells serve as one of the first immune responders against inhaled pathogens, particles, stimuli, and chemical allergens such as dNCOs. Upon encountering outside stimuli, alveolar macrophages react by phagocytosis as well as producing and secreting different mediators such as cytokines, chemokines, and others, into the alveoli microenvironment to orchestrate the initiation of inflammatory/immune responses. Dysfunction of alveolar macrophages, including elevated production and secretion of pro-inflammatory cytokines and other immune mediators, has been shown to play an important role in asthma pathogenesis. In the clinical setting, the levels of many immune mediators produced by macrophages have been found elevated in the asthmatic airway. However, both the levels of these asthma-associated, macrophage-secreted inflammatory/immune mediators in MDI-OA patients\u2019 airways and how expression of these mediators change in response to MDI exposure in alveolar macrophages are largely undetermined. Previously, we demonstrated a microRNA (miR)-206-3p and miR-381-3p mediated PPP3CA/Calcineurin signaling induced inducible nitric oxide synthase (iNOS) transcription in macrophages and bronchoalveolar lavage cells (BALCs) after acute MDI exposure; however, whether this mechanism participates in regulation of other asthma-associated mediators secreted by macrophages/BALCs after MDI exposure is currently unknown. The first aim of this study was to identify candidate asthma-associated, macrophage-secreted mediators that can be regulated after MDI exposure. After identified the candidate mediators can be regulated by MDI-exposure, we investigated the roles of miR-mediated calcineurin signaling in regulation of these candidate mediators\u2019 expressions in relation to the exposure to MDI.",
-            "title": "MicroRNA-Mediated Calcineurin Signaling Activation Induces CCL2, CCL3, CCL5, IL8 and Chemotactic Activities in 4,4\u2019-Methylene Diphenyl Diisocyanate Exposed Macrophages",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133118,66 +133105,92 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4m2e-y29d",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/4m2e-y29d",
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
+            "title": "MicroRNA-Mediated Calcineurin Signaling Activation Induces CCL2, CCL3, CCL5, IL8 and Chemotactic Activities in 4,4\u2019-Methylene Diphenyl Diisocyanate Exposed Macrophages"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/trni-48be",
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
-            "identifier": "b6cbcfc5-f4d3-5cf2-b374-5be14f16d8ba",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt pillar v2.10.14 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/pillar.csv",
-                    "description": "CoreSEt pillar v2.10.14 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt pillar v2.10.14 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt pillar v2.10.14 (coreset-dev)"
                 }
             ],
+            "identifier": "b6cbcfc5-f4d3-5cf2-b374-5be14f16d8ba",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/trni-48be",
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
+            "title": "CoreSEt pillar v2.10.14 (coreset-dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2008",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network (DAWN-2008) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2008-nid13624",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2008-nid13624"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2008-nid13624",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "demographic characteristics",
@@ -133190,72 +133203,38 @@
                 "substance abuse",
                 "suicide"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2008",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2008-nid13624",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network (DAWN-2008)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2008-nid13624",
-                    "description": "Drug Abuse Warning Network (DAWN-2008) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2008-nid13624"
-                }
-            ]
+            "title": "Drug Abuse Warning Network (DAWN-2008)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/9552739e-3d05-4c1b-8eff-ecabf391e2e5/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-part-d-prescribers-by-provider-and-drug-data-dictionary",
             "description": "The Medicare Part D Prescribers by Provider and Drug dataset provides information on prescription drugs prescribed to Medicare beneficiaries enrolled in Part D by physicians and other health care providers. This dataset contains the total number of prescription fills that were dispensed and the total drug cost paid organized by prescribing National Provider Identifier (NPI), drug brand name (if applicable) and drug generic name.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Medicare Part D Prescribers - by Provider and Drug",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9552739e-3d05-4c1b-8eff-ecabf391e2e5/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9552739e-3d05-4c1b-8eff-ecabf391e2e5/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Part D Prescribers - by Provider and Drug : 2022-12-30"
                 },
                 {
@@ -133379,44 +133358,49 @@
                     "title": "Medicare Part D Prescribers - by Provider and Drug : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-part-d-prescribers-by-provider-and-drug-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9552739e-3d05-4c1b-8eff-ecabf391e2e5/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "drugs",
+                "health equity",
+                "medicare",
+                "medicare prescription drug",
+                "physicians & practitioners"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-provider-and-drug",
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
+            "title": "Medicare Part D Prescribers - by Provider and Drug"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ts8w-jk9x",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-10-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-21",
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
-            "identifier": "90a99487-4084-4074-9220-3af12943caab",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 10-14-2024-to-10-20-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133424,41 +133408,35 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "90a99487-4084-4074-9220-3af12943caab",
+            "issued": "2024-10-23",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/ts8w-jk9x",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 10-14-2024-to-10-20-2024"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -133481,47 +133459,45 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary"
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
-                "cardiovascular disease",
-                "coronary heart disease",
-                "hypertension",
-                "risk factors",
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
-            "identifier": "https://data.cdc.gov/api/views/fwns-azgu",
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Health-Interview-Survey-NHIS-National-Car/fwns-azgu",
             "description": "2019\u20132020. The National Health Interview Survey (NHIS) has monitored the health of the nation since 1957. NHIS data on a broad range of health topics are collected through personal household interviews. Indicators for this dataset has been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (region) and indicator, and they include CVDs (e.g., heart failure) and risk factors (e.g., hypertension). The data can be plotted as trends and stratified by age group, sex, and race/ethnicity.",
-            "title": "National Health Interview Survey (NHIS) - National Cardiovascular Disease Surveillance Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133544,39 +133520,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Health-Interview-Survey-NHIS-National-Car/fwns-azgu",
+            "identifier": "https://data.cdc.gov/api/views/fwns-azgu",
+            "issued": "2023-07-18",
+            "keyword": [
+                "cardiovascular disease",
+                "coronary heart disease",
+                "hypertension",
+                "risk factors",
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
+            "title": "National Health Interview Survey (NHIS) - National Cardiovascular Disease Surveillance Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/tsq7-dnqw",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-29",
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
-            "identifier": "cc8fd7b9-87a4-4d32-ae81-aa37e84f81db",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-22-to-2024-01-28",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133585,38 +133570,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-22-to-2024-01-28"
                 }
             ],
+            "identifier": "cc8fd7b9-87a4-4d32-ae81-aa37e84f81db",
+            "issued": "2024-01-31",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/tsq7-dnqw",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-01-29",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-22-to-2024-01-28"
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
-            "identifier": "https://data.cdc.gov/api/views/n97r-u9uh",
             "description": "\u2022 Weekly Cumulative Percentage of Children 6 Months\u201317 Years Who Are Up to Date with COVID-19 Vaccines and Comparison Between 2023\u201324 and 2024\u201325 by Jurisdiction.\n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey\u2013Child COVID Module (NIS\u2013CCM). The NIS\u2013CCM was discontinued at the end of 2023 and questions regarding COVID-19 vaccination status and intent were added to the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html).",
-            "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to date with COVID-19 Vaccines and Comparison Between 2023-24 and 2024-25 by Jurisdiction",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133639,51 +133622,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/n97r-u9uh",
+            "issued": "2024-10-23",
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
+            "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to date with COVID-19 Vaccines and Comparison Between 2023-24 and 2024-25 by Jurisdiction"
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
-            "identifier": "https://data.cdc.gov/api/views/kpwh-eddm",
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Stroke-Mortality-Data-Among-US-Adults-35-by-State-/kpwh-eddm",
             "description": "2013 to 2015, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "title": "Stroke Mortality Data Among US Adults (35+) by State/Territory and County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133706,36 +133683,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Stroke-Mortality-Data-Among-US-Adults-35-by-State-/kpwh-eddm",
+            "identifier": "https://data.cdc.gov/api/views/kpwh-eddm",
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
-            "landingPage": "https://data.cdc.gov/d/jj3m-siz7",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Physical Effects Research Branch (PERB), National Institute for Occupational Safety and Health (NIOSH) Health Effects Laboratory Division (HELD),",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/jj3m-siz7",
             "description": "Di-n-butyl phthalate is a known endocrine disruptor and has been found in increased levels in women of childbearing age. To investigate mechanisms of phthalate toxicity in normal human cells and to provide information concerning inter-individual variation and gene-environment interactions.",
-            "title": "Gene Expression Profiles of Di-n-butyl Phthalate in Normal Human Mammary Epithelial Cells",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133743,79 +133730,68 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jj3m-siz7",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.cdc.gov/d/jj3m-siz7",
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
+            "title": "Gene Expression Profiles of Di-n-butyl Phthalate in Normal Human Mammary Epithelial Cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fludb.org/brc/home.do?decorator=influenza",
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
-            "identifier": "92714708-8d4d-414c-8aba-75a6f46414ac",
+            "dataQuality": true,
             "description": "<p>The Influenza Research Database (IRD) serves as a public repository and analysis platform for flu sequence, experiment, surveillance and related data.</p>",
-            "title": "Influenza Research Database (IRD)",
+            "identifier": "92714708-8d4d-414c-8aba-75a6f46414ac",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.fludb.org/brc/home.do?decorator=influenza",
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
+            "title": "Influenza Research Database (IRD)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -133838,42 +133814,47 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Guanarito virus to Viral hemorrhagic fevers, Lassa virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/tu8w-mv7i",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "2025",
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
-            "identifier": "ebbf57d1-2e47-4289-9799-d251e79b2ff6",
             "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2025 Dental SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133881,36 +133862,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "ebbf57d1-2e47-4289-9799-d251e79b2ff6",
+            "issued": "2024-12-10",
+            "keyword": [
+                "2025",
+                "qhp landscape",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "landingPage": "https://healthdata.gov/d/tu8w-mv7i",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2025 Dental SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/orffinder/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/anuf-cjsp",
             "description": "A graphical analysis tool that finds all open reading frames in a user's sequence or in a sequence already in the database.",
-            "title": "Open Reading Frame Finder (ORF Finder)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133919,38 +133902,40 @@
                     "title": "Open Reading Frame Finder (ORF Finder) - Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/anuf-cjsp",
+            "issued": "2021-06-30",
+            "keyword": [
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/orffinder/",
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
+            "title": "Open Reading Frame Finder (ORF Finder)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/tvjb-6gpg",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-21",
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
-            "identifier": "6de859d5-5ea7-42df-b5aa-1fc22c4b35a1",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-13-to-2023-03-19",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -133959,37 +133944,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-13-to-2023-03-19"
                 }
             ],
+            "identifier": "6de859d5-5ea7-42df-b5aa-1fc22c4b35a1",
+            "issued": "2023-03-28",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/tvjb-6gpg",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-03-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-13-to-2023-03-19"
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
-                "nutrition"
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
-            "identifier": "https://data.cdc.gov/api/views/8wmh-yzz9",
             "description": "These data represent mean intake, on a given day, estimates of nutrients from foods and beverages from the National Health and Nutrition Examination Survey (NHANES).",
-            "title": "NHANES Select Mean Dietary Intake Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134012,49 +133996,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/8wmh-yzz9",
+            "issued": "2023-03-02",
+            "keyword": [
+                "nutrition"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-04-18",
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
+            "title": "NHANES Select Mean Dietary Intake Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/sd5c-m3g5",
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
-            "identifier": "https://data.cdc.gov/api/views/sd5c-m3g5",
             "description": "NNDSS - Table II. West Nile virus disease - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. \r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Updated weekly from the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance).  Data for Jamestown Canyon virus, La Crosse virus, Chikungunya virus, Eastern equine encephalitis virus, Powassan virus, St. Louis virus, and Western equine encephalitis virus diseases are available in Table I. \r\n\u00b6 Not reportable in all states. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.",
-            "title": "NNDSS - Table II. West Nile virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134077,86 +134055,90 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/sd5c-m3g5",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "west nile virus",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/sd5c-m3g5",
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
+            "title": "NNDSS - Table II. West Nile virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/twxi-9wu2",
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
-            "identifier": "6982e042-595d-54a8-ab18-7e1b4f69f9ca",
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
+            "identifier": "6982e042-595d-54a8-ab18-7e1b4f69f9ca",
+            "issued": "2023-06-01",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/twxi-9wu2",
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
+            "title": "Scorecard TAG v0.2.4-1 (dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://mor.nlm.nih.gov/RxNav/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/yqm5-asqn",
             "description": "An application for navigating RxNorm drugs. This applications displays relations among drug entities in RxNorm and provides additional information about RxNorm drugs, including drug classes, pill images and drug-drug interactions. RxNav is supported by several drug APIs.",
-            "title": "RxNav",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134165,38 +134147,41 @@
                     "title": "RxNav"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/yqm5-asqn",
+            "issued": "2022-03-01",
+            "keyword": [
+                "drugs",
+                "supplements",
+                "tools & utilities"
+            ],
+            "landingPage": "https://mor.nlm.nih.gov/RxNav/",
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
+            "title": "RxNav"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ty9a-9953",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-04-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-04",
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
-            "identifier": "b66d54f8-c740-42e2-adf1-8fc58d0d49e4",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-27-to-2023-04-02",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134205,79 +134190,81 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-27-to-2023-04-02"
                 }
             ],
+            "identifier": "b66d54f8-c740-42e2-adf1-8fc58d0d49e4",
+            "issued": "2023-04-05",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/ty9a-9953",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-04-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-27-to-2023-04-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/tyrw-zsmq",
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
-            "identifier": "cb4bb49c-2cae-510d-8220-caa48fe4f99e",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure v2.10.16 (coreset-dev0)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/measure.csv",
-                    "description": "CoreSEt measure v2.10.16 (coreset-dev0)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure v2.10.16 (coreset-dev0)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure v2.10.16 (coreset-dev0)"
                 }
             ],
+            "identifier": "cb4bb49c-2cae-510d-8220-caa48fe4f99e",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/tyrw-zsmq",
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
+            "title": "CoreSEt measure v2.10.16 (coreset-dev0)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/a2mg-p2ni",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -134285,46 +134272,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/a2mg-p2ni",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/a2mg-p2ni",
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
+            "title": "Prevalence of Hearing Loss in the United States by Industry, 2000-2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5nfe-wsjn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/5nfe-wsjn",
             "description": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers'. NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134347,43 +134323,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5nfe-wsjn",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "machupo virus",
+                "marburg virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "sabia virus",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5nfe-wsjn",
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
+            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-28",
-            "references": [
-                "CDC"
-            ],
-            "keyword": [
-                "flu",
-                "flu vaccination",
-                "influenza"
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
-            "identifier": "https://data.cdc.gov/api/views/e5zk-7tx5",
             "description": "Weekly Cumulative Influenza Vaccine Doses Distributed in the United States, 2016-2021\n\n\u2022 Flu vaccine is produced by private manufacturers. For the 2020-2021 season, manufacturers have projected they will provide as many as 194 to 198 million doses of influenza vaccine for the U.S. market.\n\u2022 Additional information is available: https://www.cdc.gov/flu/prevent/vaccine-supply-distribution.htm.",
-            "title": "Weekly Cumulative Influenza Vaccine Doses Distributed in the United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134406,42 +134385,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/e5zk-7tx5",
+            "issued": "2022-09-28",
+            "keyword": [
+                "flu",
+                "flu vaccination",
+                "influenza"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-09-28",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "CDC"
+            ],
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Influenza Vaccine Doses Distributed in the United States"
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
-            "@type": "dcat:Dataset",
-            "temporal": "1899-2017",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -134464,48 +134448,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
+            "identifier": "https://data.cdc.gov/api/views/66i6-hisz",
+            "issued": "2019-05-23",
+            "keyword": [
+                "botulism"
+            ],
+            "landingPage": "https://data.cdc.gov/d/66i6-hisz",
+            "language": [
+                "English"
+            ],
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Annual",
+            "modified": "2019-05-23",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "USA",
+            "temporal": "1899-2017",
             "theme": [
                 "Foodborne",
                 "Waterborne",
                 "and Related Diseases"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Botulism"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/u2nu-8ww6",
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
-            "identifier": "905e5046-5351-44e4-b65b-204bf684805c",
             "description": "This table presents three populations of beneficiaries who could benefit from different levels of integrated care, 2017-2021: (1) beneficiaries who received services for a behavioral health (BH) condition; (2) beneficiaries who received services for a behavioral health condition who also received services for at least one of a number of select physical health (PH) conditions (a subset of population 1); and (3) beneficiaries prescribed medications for substance use disorders who do not have a medical claim for a behavioral health condition (a subset of population 1).\r\n\r\nSome states have serious data quality issues, making the data unusable for identifying this population. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional, Gender, Age, Zip code, Race and ethnicity, Eligibility group code, Enrollment in CMC Plans. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.",
-            "title": "Beneficiaries who could benefit from integrated care, 2017-2021",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134514,56 +134496,42 @@
                     "title": "Beneficiaries who could benefit from integrated care, 2017-2021"
                 }
             ],
+            "identifier": "905e5046-5351-44e4-b65b-204bf684805c",
+            "issued": "2023-03-28",
+            "keyword": [
+                "behavioral health care",
+                "chip",
+                "integrated care",
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/u2nu-8ww6",
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
+            "title": "Beneficiaries who could benefit from integrated care, 2017-2021"
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
-                "children",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "hhs region",
-                "hispanic origin",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "puerto rico",
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
-            "identifier": "https://data.cdc.gov/api/views/9xc7-3a4q",
             "description": "Deaths involving coronavirus disease 2019 (COVID-19) reported to NCHS by time-period, HHS region, race and Hispanic origin, and age groups (<65, 65-74. 75-84, 85+, and 65+).\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
-            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, Age 65plus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134586,41 +134554,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/9xc7-3a4q",
+            "issued": "2022-09-09",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "children",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hhs region",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "puerto rico",
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cdc.gov/d/4r49-eadb",
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
-            "identifier": "https://data.cdc.gov/api/views/4r49-eadb",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 6 - Dallas",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134643,88 +134626,88 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4r49-eadb",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/4r49-eadb",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 6 - Dallas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/u3vx-mcbv",
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
-            "identifier": "d55ac067-44dd-5ea0-ab04-d06b5985b540",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_files_allDownloadsSSBtn",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/files_allDownloadsSSBtn.csv",
-                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/files_allDownloadsSSBtn.csv",
+                    "mediaType": "text/csv",
                     "title": "files_allDownloadsSSBtn csv file"
                 }
             ],
+            "identifier": "d55ac067-44dd-5ea0-ab04-d06b5985b540",
+            "issued": "2022-06-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/u3vx-mcbv",
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
+            "title": "devAuto_files_allDownloadsSSBtn"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/u3zz-5xrq",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2019-07-22",
-            "@type": "dcat:Dataset",
-            "modified": "2019-09-26",
-            "keyword": [
-                "core sets",
-                "performance rates",
-                "quality measures"
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
-            "identifier": "229d6279-e614-5353-9226-f6a6f37d06c3",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2018 reporting.\r\n\r\nSource: Mathematica analysis of MACPro and Form CMS-416 reports for the FFY 2018 reporting cycle. For more information, see the Children's Health Care Quality Measures and Adult Health Care Quality Measures webpages.",
-            "title": "2018 Child and Adult Health Care Quality Measures",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134733,42 +134716,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "229d6279-e614-5353-9226-f6a6f37d06c3",
+            "issued": "2019-07-22",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/u3zz-5xrq",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2019-09-26",
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
+            "title": "2018 Child and Adult Health Care Quality Measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/u4aj-azap",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "exchange puf",
-                "machine readable",
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
-            "identifier": "e839d4df-6c9c-435d-a48d-fd790b2897a6",
             "description": "The Machine Readable PUF (MR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The MR-PUF contains issuer-level URL locations for machine-readable network provider and formulary information.",
-            "title": "Machine Readable PUF - PY2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134776,39 +134758,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "e839d4df-6c9c-435d-a48d-fd790b2897a6",
+            "issued": "2024-12-13",
+            "keyword": [
+                "exchange puf",
+                "machine readable",
+                "marketplace puf",
+                "py2025"
+            ],
+            "landingPage": "https://healthdata.gov/d/u4aj-azap",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Machine Readable PUF - PY2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMAUDE/search.CFM",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "temporal": "1991-01-01/2013-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2013-10-31",
-            "references": [
-                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/PostmarketRequirements/ReportingAdverseEvents/ucm127891.htm"
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
-            "identifier": "1327f116-da9f-40b9-babd-c893ab2ceacd",
             "description": "MAUDE data represents reports of adverse events involving medical devices. The data consists of all voluntary reports since June, 1993, user facility reports since 1991, distributor reports since 1993, and manufacturer reports since August, 1996.",
-            "title": "MAUDE (Manufacturer and User Facility Device Experience)",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134816,43 +134796,40 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "1327f116-da9f-40b9-babd-c893ab2ceacd",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMAUDE/search.CFM",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-10-31",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/PostmarketRequirements/ReportingAdverseEvents/ucm127891.htm"
+            ],
+            "temporal": "1991-01-01/2013-10-31",
+            "title": "MAUDE (Manufacturer and User Facility Device Experience)"
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
-            "temporal": "1960-01-01/2015-12-31",
-            "modified": "2022-03-28",
-            "keyword": [
-                "birth rate",
-                "nchs",
-                "teen births",
-                "united states",
-                "u.s. teen birth rate",
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
-            "identifier": "https://data.cdc.gov/api/views/rg8a-czmp",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset assembles all final birth data for females aged 15\u201319, 15\u201317, and 18\u201319 for the United States.",
-            "title": "NCHS - Birth Rates for Women Aged 15-17, 17-18, and 15-19: United States, 1960-2015",
-            "isPartOf": "NCHS - Birth Rates for Women Aged 15-17, 17-18, and 15-19: United States, 1960-2015",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -134875,32 +134852,62 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/rg8a-czmp",
+            "isPartOf": "NCHS - Birth Rates for Women Aged 15-17, 17-18, and 15-19: United States, 1960-2015",
+            "issued": "2015-12-02",
+            "keyword": [
+                "birth rate",
+                "nchs",
+                "teen births",
+                "united states",
+                "u.s. teen birth rate",
+                "women"
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1960-01-01/2015-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Birth Rates for Women Aged 15-17, 17-18, and 15-19: United States, 1960-2015"
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
@@ -134911,77 +134918,50 @@
                 "sdoh-use-of-health-care",
                 "short-stay-hospitals"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:nhcs@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhds/index.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
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
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Database will not be updated again.",
+            "temporal": "1965\u20142010",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Discharge Survey (NHDS) Restricted Data, 1965-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/deficit-reduction-act-hospital-acquired-condition-measures",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2015-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-29",
-            "references": [
-                "https://data.cms.gov/resources/deficit-reduction-act-dra-hospital-acquired-condition-hac-measures-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/01edb62e-5c45-4f43-8c91-16cba21cbb74/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/deficit-reduction-act-dra-hospital-acquired-condition-hac-measures-data-dictionary",
             "description": "The Publicly Reported Deficit Reduction Act (DRA) Hospital-Acquired Condition (HAC) Measures data provides information on hospital-level measures rates for four of the HACs included in the DRA HAC payment provision \u2013 foreign object retained after surgery, blood incompatibility, air embolism, and falls and trauma \u2013 for Medicare fee-for-service discharges. The Publicly Reported DRA HAC Measures are reported only for informational and quality improvement purposes; the results of the measure calculations do not affect payment and are not a part of the HAC Reduction Program.",
-            "title": "Deficit Reduction Act Hospital-Acquired Condition Measures",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/01edb62e-5c45-4f43-8c91-16cba21cbb74/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/01edb62e-5c45-4f43-8c91-16cba21cbb74/data",
+                    "mediaType": "text/html",
                     "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2024-01-01"
                 },
                 {
@@ -135105,101 +135085,98 @@
                     "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2015-08-16"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/deficit-reduction-act-dra-hospital-acquired-condition-hac-measures-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/01edb62e-5c45-4f43-8c91-16cba21cbb74/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "medicare",
+                "original medicare",
+                "safety of care"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/deficit-reduction-act-hospital-acquired-condition-measures",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-08-29",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/deficit-reduction-act-dra-hospital-acquired-condition-hac-measures-methodology"
+            ],
+            "temporal": "2015-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Deficit Reduction Act Hospital-Acquired Condition Measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nsfg/index.htm",
+            "accrualPeriodicity": "Irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2020-10-20",
-            "@type": "dcat:Dataset",
-            "temporal": "1973/2019",
-            "modified": "2023-12-12",
-            "references": [
-                "https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-MainText-508.pdf; https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-App7a-RestrictedUseRDCvars-FemResp-Preg-508.pdf; https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-App7b-RestrictedUseRDCvars-Male-508.pdf;  https://www.cdc.gov/nchs/nsfg/nsfg_special_supplementary_data.htm"
-            ],
-            "keyword": [
-                "pregnancy; births; infertility; marriage; contraception; health; cohabitation; survey; research-data-center"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:nsfg@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/3daf-8gde",
+            "describedBy": "Nationally representative sample of women and men in the household population (civilian, non-institutionalized) ages 15-49",
             "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.  Restricted-use files include contextual data, restricted-use analytic variables, paradata, and interviewer observation data.  Geographic information can be used to link NSFG to external data files.  Estimates cannot be made for specific geographic areas.  Contents of restricted-use files varies over time.",
-            "title": "Restricted Use National Survey of Family Growth (NSFG)",
-            "isPartOf": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.  Restricted-use files include contextual data, restricted-use analytic variables, paradata, and interviewer observation data.  Geographic information can be used to link NSFG to external data files.  Estimates cannot be made for specific geographic areas.  Contents of restricted-use files varies over time.",
                     "@type": "dcat:Distribution",
+                    "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.  Restricted-use files include contextual data, restricted-use analytic variables, paradata, and interviewer observation data.  Geographic information can be used to link NSFG to external data files.  Estimates cannot be made for specific geographic areas.  Contents of restricted-use files varies over time.",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
                     "title": "Restricted Use National Survey of Family Growth (NSFG)"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Nationally representative sample of women and men in the household population (civilian, non-institutionalized) ages 15-49",
+            "identifier": "https://data.cdc.gov/api/views/3daf-8gde",
+            "isPartOf": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
+            "issued": "2020-10-20",
+            "keyword": [
+                "pregnancy; births; infertility; marriage; contraception; health; cohabitation; survey; research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nsfg/index.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Irregular",
+            "modified": "2023-12-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-MainText-508.pdf; https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-App7a-RestrictedUseRDCvars-FemResp-Preg-508.pdf; https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-App7b-RestrictedUseRDCvars-Male-508.pdf;  https://www.cdc.gov/nchs/nsfg/nsfg_special_supplementary_data.htm"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "1973/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Restricted Use National Survey of Family Growth (NSFG)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/h4pd-hu6x",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
-                "arboviral diseases",
-                "nedss",
-                "netss",
-                "nndss",
-                "st. louis virus disease",
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
-            "identifier": "https://data.cdc.gov/api/views/h4pd-hu6x",
             "description": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
```

