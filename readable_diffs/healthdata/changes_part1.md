# Change History for healthdata.json

### Changes from 631ae89 to 75d151c
**Author:** Automated

**Date:** 2025-02-04 04:12:27+00:00

**Message:** Updated data: Tue Feb  4 04:12:27 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index 6a8f6a0..58badd9 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -14652,7 +14652,7 @@
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
+            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, sex, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14687,7 +14687,7 @@
                 "en-US"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2023-04-14",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -33006,7 +33006,7 @@
             ],
             "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-11-09",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -35594,7 +35594,7 @@
             ],
             "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-01-30",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -52195,6 +52195,71 @@
             ],
             "title": "Skilled Nursing Facility Enrollments"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Monthly",
+            "bureauCode": [
+                "009:20"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "description": "Infant Protection Against RSV by Maternal RSV Vaccination or Receipt of Nirsevimab and Intent for Nirsevimab Receipt, Reported by Females Aged 18-49 Years Who Have an Infant <8 Months During the RSV Season (born since April 1, 2024)\n\nMonthly estimates of infant protection against RSV by maternal RSV vaccination or receipt of nirsevimab, as well as intent for nirsevimab receipt, were calculated using data from the from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM). (https://www.cdc.gov/nis/about/index.html). Data were reported by adult females aged 18-49 years with infants under the age of 8 months during the RSV season (born since April 1, 2024). The NIS\u2013ACM is an ongoing random-digit-dial cellular telephone survey of households with adults 18 years and older. All estimates are based upon parent-reported receipt of nirsevimab.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/vdz4-qrri",
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
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2024-2025",
+            "theme": [
+                "Pregnancy & Vaccination"
+            ],
+            "title": "Infant Protection Against Respiratory Syncytial Virus (RSV) by Maternal RSV Vaccination or Receipt of Nirsevimab, and Intent for Nirsevimab Receipt, United States"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -60483,6 +60548,71 @@
             },
             "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-04-2024-to-11-10-2024"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Weekly",
+            "bureauCode": [
+                "009:20"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "description": "\u2022 Weekly Cumulative RSV Vaccination Coverage and Intent Among Adults 75 Years and Older and 60\u250074 Years with High Risk Conditions Ever Vaccinated with RSV Vaccine by Demographic Characteristics and Jurisdiction \n\n\u2022 Weekly estimates of RSV vaccination coverage and intent among adults 75 years and older and 60\u250074 years with high risk conditions are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html). \n\n\u2022 In June 2023, the Advisory Committee on Immunization Practices (ACIP) voted to recommend that adults aged \u226560 years may receive a single dose of an RSV vaccine, using shared clinical decision-making. In June 2024, the ACIP voted to recommend a single dose of RSV vaccine for all adults 75 years and older and adults 60\u201374 years who are at increased risk for severe RSV disease. The data below captures ever receiving a dose of an RSV vaccine by adults 60 years and older.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/k4cb-dxd7",
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
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2024-2025",
+            "theme": [
+                "Vaccinations"
+            ],
+            "title": "Weekly Cumulative RSV Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 75 and Older and 60-74 Years with High-Risk Conditions Ever Vaccinated, United States"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -66644,7 +66774,7 @@
             ],
             "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-01-30",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -69747,6 +69877,71 @@
             ],
             "title": "featAuto_files_topicSnapshot"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Weekly",
+            "bureauCode": [
+                "009:20"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "description": "Weekly COVID-19 Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \u2022 Weekly estimates of COVID-19 vaccination coverage and intent among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/). \n\nWeekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
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
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2024-2025",
+            "theme": [
+                "Vaccinations"
+            ],
+            "title": "Weekly Cumulative COVID-19 Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -83355,7 +83550,7 @@
             ],
             "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-01-30",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -90832,7 +91027,7 @@
             ],
             "landingPage": "https://learn.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-02-02",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:041"
             ],
@@ -92588,7 +92783,7 @@
             ],
             "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/children-coverage-vaccination.html",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-31",
+            "modified": "2025-02-04",
             "programCode": [
                 "009:020"
             ],
@@ -97325,7 +97520,7 @@
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
+            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, sex, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97361,7 +97556,7 @@
                 "en-US"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2024-10-04",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -98984,7 +99179,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/vt72-wepb",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-04-20",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -126008,7 +126203,7 @@
             ],
             "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-01-30",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -131482,6 +131677,71 @@
             },
             "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-22-to-2024-01-28"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Weekly",
+            "bureauCode": [
+                "009:20"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "description": "\u2022 Weekly Influenza Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \n\n \u2022 Weekly estimates of influenza vaccination coverage and intent for vaccination among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/sw5n-wg2p",
+            "issued": "2024-10-10",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/adult-coverage.html",
+            "language": [
+                "English"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2024-2025",
+            "theme": [
+                "Flu Vaccinations"
+            ],
+            "title": "Weekly Influenza Vaccination Coverage and Intent for Vaccination, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -131838,7 +132098,7 @@
                 "en-US"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2023-04-18",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -135511,7 +135771,7 @@
             ],
             "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-11-15",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -135529,70 +135789,6 @@
             ],
             "title": "Nutrition, Physical Activity, and Obesity - American Community Survey"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "R/P1M",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jasmine Chaitram",
-                "hasEmail": "mailto:zoa6@cdc.gov"
-            },
-            "description": "This dataset includes COVID-19 self-test result data voluntarily reported by users of tests through the MakeMyTestCount website (makemytestcount.org). All fields are self-reported by the user with the exception of  fields derived from the self-reported zip code. This dataset will be updated monthly. If there are any questions, please direct them to the data steward, Jasmine Chaitram <zoa6@cdc.gov>. \n\nThis dataset includes the following self-reported data:  \n- Date (by week)\u2013 date of test shown by week starting date  \n- Age group (years) \u2013 age of individual taking the test, categorized into the following: 2-4, 5-11, 12-15, 16-17, 18-29, 30-39, 40-49, 50-64, 65-74, 75+  \n- Race \u2013 race of individual taking the test: American Indian or Alaska Native, Asian, Black, Native Hawaiian or Other Pacific Islander, White, Multiple or Other, missing \n- Ethnicity \u2013 ethnicity of individual taking the test: Hispanic, Non-Hispanic, missing \n- Sex \u2013 sex of individual taking the test: male, female, missing \n- Test result \u2013 positive, negative, inconclusive \n\nThe dataset also includes the following columns to support analyses. These columns are based on the self-reported zip code:  \n- State abbreviation  \n- State name  \n- State FIPS code \n- FEMA region  \n\nPlease note that there are limitations with these data, including: \n\n1. Data are not comprehensive of all self-tests performed. Data represent results voluntarily reported by an individual via the MakeMyTestCount website. These data do not include self-test results that were reported to state and local health departments if they were not also reported through the MakeMyTestCount website. The true denominator (known number of tests completed in the US) cannot be ascertained and reflects a small fraction of the number of self-tests used.    \n\n2. Data are not verified. The quality of specimen, appropriate execution of self-test, result produced, and person tested are unverified; therefore, reported interpretation of results cannot be confirmed. All results and accompanying demographic information are also self-reported and cannot be verified.  \n\n3. Data reports are not complete. Individual submissions vary widely in terms of the data elements collected. Not all data elements are required (only date, age, and zip code), and some results are missing demographic information.  \n\n4. Data are not representative. Based on the limited number of self-reported test results, this dataset is not representative of the use of self-testing by demographic, nor is the dataset inclusive of all self-testing completed within each jurisdiction. This dataset represents a small proportion of overall COVID-19 testing conducted and reported volumes are much lower than testing conducted in point of care and laboratory settings.   \n\n5. Data represent individual test results, not persons tested. Data in this dataset are not linkable and do not allow for analyses around serial testing. Data also cannot be disaggregated to identify multiple reports by the same individual.  \n\nAll analyses should be completed with these limitations in mind.  \n\nFor more information about the challenges and opportunities around self-test data, please refer to the following article: Ritchey MD, Rosenblum HG, Del Guercio K, et al. COVID-19 Self-Test Data: Challenges and Opportunities \u2014 United States, October 31, 2021\u2013June 11, 2022. MMWR Morb Mortal Wkly Rep 2022;71:1005\u20131010. DOI: http://dx.doi.org/10.15585/mmwr.mm7132a1",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2a4-xk9k/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2a4-xk9k/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2a4-xk9k/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2a4-xk9k/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/i2a4-xk9k",
-            "issued": "2023-08-10",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "mmtc",
-                "otc",
-                "self-tests"
-            ],
-            "landingPage": "https://data.cdc.gov/d/i2a4-xk9k",
-            "language": [
-                "en-US"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-14",
-            "programCode": [
-                "009:038"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "US",
-            "temporal": "2022-05-01/2023-11-10",
-            "theme": [
-                "Public Health Surveillance"
-            ],
-            "title": "U.S. COVID-19 MakeMyTestCount Self-Test Data"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -144490,7 +144686,7 @@
                 "en-US"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2023-04-18",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -149730,7 +149926,7 @@
                 "en-US"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2023-09-08",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -150544,7 +150740,7 @@
                 "en-US"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2023-09-08",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -150607,7 +150803,7 @@
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions,",
+            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, sex, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions,",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -150642,7 +150838,7 @@
                 "en-US"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2024-10-04",
+            "modified": "2025-02-03",
             "programCode": [
                 "009:020"
             ],
@@ -154323,69 +154519,6 @@
             ],
             "title": "GEO (Gene Expression Omnibus)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "R/P1M",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jasmine Chaitram",
-                "hasEmail": "mailto:zoa6@cdc.gov"
-            },
-            "description": "This dataset includes COVID-19 self-test result data voluntarily reported by users of tests through manufacturer websites and mobile companion applications. At this time, the dataset does not include data reported through the MakeMyTestCount website. All fields are self-reported by the user voluntarily reporting the test result. This dataset will be updated monthly.\n\nPlease note that there are limitations with these data, including:\n1.\tData are not comprehensive of all self-tests performed. Data represent results voluntarily reported by an individual via manufacturer-provided website or companion mobile applications. Not all self-test manufacturers are currently capturing and sending data to CDC. Similarly, these data do not include self-test results that were reported to state and local health departments if they were not also reported through the manufacturer-provided website or companion mobile applications. The true denominator (number of tests completed) cannot be ascertained, but based on manufacturer production numbers, this dataset reflects a small fraction of the number of self-tests used.   \n\n2.\tData are not verified. The quality of specimen, appropriate execution of self-test, result produced, and person tested are unverified; therefore, reported interpretation of results cannot be confirmed. All results and accompanying demographic information are also self-reported and cannot be verified. \n\n3.\tData reports are not complete. Manufacturer-provided websites and companion mobile applications vary widely in terms of the data elements collected. Not all data elements are required, and many results are missing demographic information. \n\n4.\tData are not representative. Based on the limited number of self-reported test results, this dataset is not representative of the use of self-testing by demographic, nor is the dataset inclusive of all self-testing completed within each jurisdiction. This dataset represents a small proportion of overall COVID-19 testing conducted in each jurisdiction and reported volumes are much lower than testing conducted in point of care and laboratory settings.  \n\n5.\tData represent individual test results, not persons tested. Data in this dataset are not linkable and do not allow for analyses around serial testing. Data also cannot be disaggregated to identify multiple reports by the same individual. \n\nAll analyses should be completed with these limitations in mind.\n\nFor more information about the challenges and opportunities around self-test data, please refer to the following article: Ritchey MD, Rosenblum HG, Del Guercio K, et al. COVID-19 Self-Test Data: Challenges and Opportunities \u2014 United States, October 31, 2021\u2013June 11, 2022. MMWR Morb Mortal Wkly Rep 2022;71:1005\u20131010. DOI: http://dx.doi.org/10.15585/mmwr.mm7132a1",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/275g-9x8h/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/275g-9x8h/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/275g-9x8h/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/275g-9x8h/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/275g-9x8h",
-            "issued": "2023-02-08",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "otc",
-                "self-tests"
-            ],
-            "landingPage": "https://data.cdc.gov/d/275g-9x8h",
-            "language": [
-                "en-US"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-14",
-            "programCode": [
-                "009:038"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "US",
-            "temporal": "2021-10-01/2023-11-10",
-            "theme": [
-                "Public Health Surveillance"
-            ],
-            "title": "U.S. COVID-19 Self-Test Data"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
```

### Changes from 48c0305 to 631ae89
**Author:** Automated

**Date:** 2025-02-03 04:12:14+00:00

**Message:** Updated data: Mon Feb  3 04:12:14 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index ca48fd5..6a8f6a0 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -90832,7 +90832,7 @@
             ],
             "landingPage": "https://learn.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-02-01",
+            "modified": "2025-02-02",
             "programCode": [
                 "009:041"
             ],
```

### Changes from c498318 to 48c0305
**Author:** Automated

**Date:** 2025-02-02 08:11:46+00:00

**Message:** Updated data: Sun Feb  2 08:11:46 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index 0825871..ca48fd5 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -32471,8 +32471,8 @@
                 "coronavirus",
                 "covid-19",
                 "hospital capacity",
-                "hospital occupancy",
                 "hospitalizations",
+                "hospital occupancy",
                 "icu beds",
                 "influenza",
                 "inpatient beds",
@@ -130603,8 +130603,8 @@
                 "sdoh-employment",
                 "sdoh-food-access",
                 "sdoh-food-insecurity",
-                "sdoh-high-school",
                 "sdoh-higher-education",
+                "sdoh-high-school",
                 "sdoh-housing-stability",
                 "sdoh-poverty-income",
                 "sdoh-source-of-health-care",
```

### Changes from 9f6a7dd to c498318
**Author:** Automated

**Date:** 2025-02-02 05:11:38+00:00

**Message:** Updated data: Sun Feb  2 05:11:38 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index b1bdb81..0825871 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -9074,21 +9074,21 @@
             "issued": "2024-06-26",
             "keyword": [
                 "covid",
-                "covid-19",
-                "covid-net",
                 "covid19",
+                "covid-19",
                 "covidnet",
+                "covid-net",
                 "hospitalization rate",
                 "hospitalizations",
                 "rate",
                 "rates by age group",
                 "rates by race and ethnicity",
-                "resp-net",
                 "respiratory disease",
                 "respiratory illness",
                 "respiratory virus response",
                 "respiratory-virus-response",
                 "respnet",
+                "resp-net",
                 "surveillance"
             ],
             "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
@@ -102612,8 +102612,8 @@
                 "coronavirus",
                 "covid-19",
                 "hospital capacity",
-                "hospital occupancy",
                 "hospitalizations",
+                "hospital occupancy",
                 "icu beds",
                 "influenza",
                 "inpatient beds",
@@ -110574,10 +110574,10 @@
             "issued": "2023-09-22",
             "keyword": [
                 "covid",
-                "covid-19",
-                "covid-net",
                 "covid19",
+                "covid-19",
                 "covidnet",
+                "covid-net",
                 "epi curve",
                 "hospitalizations",
                 "icu",
@@ -110585,10 +110585,10 @@
                 "percent icu",
                 "percent in-hospital death",
                 "percent mechanically ventilated",
-                "resp-net",
                 "respiratory illness",
                 "respiratory virus response",
                 "respnet",
+                "resp-net",
                 "surveillance"
             ],
             "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
```

### Changes from ca41c49 to 9f6a7dd
**Author:** Automated

**Date:** 2025-02-02 04:13:05+00:00

**Message:** Updated data: Sun Feb  2 04:13:05 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index 0866a13..b1bdb81 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -1293,68 +1293,6 @@
             },
             "title": "FDA Pet Food Recalls"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC Info",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "description": "VEHSS Composite Prevalence Estimates\n2017, 2019, 2021, 2022. This dataset contains estimates of the prevalence of visual acuity loss and major eye diseases generated using a Bayesian meta-analytic modeling approach that combines information from multiple data sources to produce comprehensive estimates of prevalence by age, race, and gender at the national, state and county levels. These composite prevalence estimates are the primary surveillance measures developed by the Centers for Disease Control and Prevention\u2019s Vision & Eye Health Surveillance System (VEHSS).  \n\nFor more information about these estimates including summary tables and maps, methods, and links to related publications visit https://www.cdc.gov/visionhealth/vehss/estimates/index.html\nTo view this data in the VEHSS interactive data visualization application, visit https://ddt-vehss.cdc.gov/ and search for \u201cVEHSS Composite Prevalence Estimate\u201d.\n\n\nVisual Acuity Loss:\nVisual acuity loss prevalence estimates represent best-corrected visual acuity in the better-seeing eye and are included in rows where Category=\u2019Measured Visual Acuity\u2019.  Rows with Subgroup = \u2018Any vision loss' represents any impairment or blindness of 20/40 or worse; rows with Subgroup = 'US-defined blindness' refers to the subset of vision loss that is 20/200 or worse.\n\n\nAge Related Macular Degeneration:\nThe age-related macular degeneration (AMD) estimates represent AMD as measured with retinal imaging examination, and are included in rows where Category = \u2018Age Related Macular Degeneration\u2019.  The Subgroup \u2018Vision threatening AMD\u2019 includes patients with geographic atrophy, wet-form AMD, or choroidal neovascularization in either eye. The Subgroup \u2018Non-vision threatening AMD\u2019 includes patients with early or intermediate dry-form AMD defined as retinal pigment epithelium abnormalities or drusen \u2265125 \u00b5m in the worse-affected eye, and do not have vision threatening AMD.\n\n\nDiabetic Retinopathy:\nThe diabetic retinopathy (DR) estimates represent DR as measured with retinal imaging examination, and are included in rows where Category=\u2019Diabetic Eye Diseases\u2019.  The Subgroup \u2018Vision threatening DR\u2019 includes patients with severe non-proliferative DR, proliferative DR, and diabetic macular edema. The Subgroup \u2018Non-vision threatening DR\u2019 is defined as patients with mild-moderate non-proliferative DR or unspecified DR, and do not have vision threatening DR.\n\n\nGlaucoma:\nThe glaucoma estimates represent glaucoma as measured with retinal imaging examination and are included in rows where Category=\u2019Glaucoma\u2019. The Subgroup \u2018Vision affecting glaucoma\u2019 includes people with glaucoma and abnormal visual field. The Subgroup \u2018Non-vision affecting glaucoma\u2019 is defined as people with glaucoma without an abnormal visual field.\n\n\nAge Groups:\nThe VEHSS Composite Prevalence Estimates are available by major age groups (All ages, ages 0-17, 18-39, 40-64, 65-84, 85+) and detailed (5-year) age groups, which are indicated by the text \u201cby detailed age groups\u201d in the \u2018Indicator\u2019 field. \n\n\nPrevalence Data Type:\nThese estimates are also available as crude (Data_Value_Type = \u2018Crude Prevalence\u2019) or adjusted data (Data_Value_Type=\u2019Adjusted Prevalence).  Crude Prevalence is the estimate of the actual number and percentage of people living with each condition.  Adjusted Prevalence estimates are adjusted to match the national population by age, race/ethnicity, and gender.  Adjusted prevalence estimates can be used to help identify disparities in prevalence between geographic areas that are not explained by differences in demographic characteristics.\n\n  \nData Sources:\nData sources for VEHSS Composite Prevalence Estimates include the National Health and Nutrition Examination Survey (NHANES), the American Community Survey (ACS), the National Survey of Children\u2019s Health (NSCH), the Behavioral Risk Factor Surveillance System (BRFSS), Medicare Fee-For-Service claims, the Transformed Medicaid Statistical Information System, MarketScan commercial insurance",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/qeru-k2y2/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/qeru-k2y2/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/qeru-k2y2/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/qeru-k2y2/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/qeru-k2y2",
-            "issued": "2024-08-20",
-            "keyword": [
-                "blind",
-                "blindness",
-                "prevalence",
-                "vision",
-                "visual"
-            ],
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/estimates/amd-prevalence.html",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2024-10-18",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "JAMA-Opthalmology forthcoming",
-                "https://jamanetwork.com/journals/jamaophthalmology"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "VEHSS Composite Prevalence Estimates"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -1597,60 +1535,6 @@
             ],
             "title": "Scorecard STATE vCORESET.1.1-test (coreset-local)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC Info",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "description": "The Department of Defense Health Agency\u2019s (DHA) Vision Center of Excellence (VCE) analyzed data from the MHS MART database on behalf of the VEHSS project.  MHS MART is a data management and reporting system used to support decision-making, health care analysis, and operational reporting. MART integrates various sources within MHS to provide a centralized repository for health care data, facilitating access to information that aids in managing health care services, resources, and performance across MHS.\n\nData are based on claims and encounter records in the MHS Management Analysis and Reporting Tool (MART) database. The population includes all active-duty and retired military members and their dependents in the MHS. The sample size is approximately 9.08 million persons.\n\nThese data are also available in the VEHSS Data Explorer, an interactive data visualization tool reporting prevalence information from more than 10 data sources: https://www.cdc.gov/vision-health-data/index.html",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/binw-6h77/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/binw-6h77/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/binw-6h77/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/binw-6h77/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/binw-6h77",
-            "issued": "2024-10-28",
-            "keyword": [
-                "vision"
-            ],
-            "landingPage": "https://data.cdc.gov/d/binw-6h77",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2024-10-30",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "Military Health System (MHS) - Vision and Eye Health Surveillance System (VEHSS)"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -5446,7 +5330,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -6170,83 +6054,6 @@
             ],
             "title": "AH Provisional COVID-19 Deaths Counts by Health Service Area"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DPH Public Inquiries",
-                "hasEmail": "mailto:dphinquiries@cdc.gov"
-            },
-            "describedBy": "https://data.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-CDI-/g4ie-h725",
-            "description": "This dataset is based on indicators described in MMWR \"Indicators for Chronic Disease Surveillance \u2014 United States, 2013\" (https://www.cdc.gov/mmwr/preview/mmwrhtml/rr6401a1.htm) before 2024 CDI refresh. It provided cross-cutting set of 124 indicators that were developed by consensus and that allows states and territories to uniformly define, collect, and report chronic disease data that are important to public health practice and available for states, and territories. In addition to providing access to state-specific indicator data, the CDI web site (www.cdc.gov/cdi) provides current release and additional information and data resources.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4ie-h725/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4ie-h725/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4ie-h725/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4ie-h725/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/g4ie-h725",
-            "issued": "2023-07-19",
-            "keyword": [
-                "alcohol",
-                "arthritis",
-                "asthma",
-                "cancer",
-                "cardiovascular disease",
-                "cdi",
-                "chronic disease indicators",
-                "chronic kidney disease",
-                "chronic obstructive pulmonary disease",
-                "diabetes",
-                "disability",
-                "immunization",
-                "mental health",
-                "nutrition physical activity and weight status",
-                "older adults",
-                "oral health",
-                "overarching conditions",
-                "public health",
-                "reproductive health",
-                "tobacco"
-            ],
-            "landingPage": "https://www.cdc.gov/cdi",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-01-30",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/mmwr/pdf/rr/rr6401.pdf"
-            ],
-            "theme": [
-                "Chronic Disease Indicators"
-            ],
-            "title": "U.S. Chronic Disease Indicators (CDI), 2023 Release"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -7552,7 +7359,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/hmye-mqgq",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-17",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -9267,26 +9074,26 @@
             "issued": "2024-06-26",
             "keyword": [
                 "covid",
-                "covid19",
                 "covid-19",
-                "covidnet",
                 "covid-net",
+                "covid19",
+                "covidnet",
                 "hospitalization rate",
                 "hospitalizations",
                 "rate",
                 "rates by age group",
                 "rates by race and ethnicity",
+                "resp-net",
                 "respiratory disease",
                 "respiratory illness",
                 "respiratory virus response",
                 "respiratory-virus-response",
                 "respnet",
-                "resp-net",
                 "surveillance"
             ],
             "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:038"
             ],
@@ -9571,7 +9378,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/jr58-6ysp",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-17",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:026"
             ],
@@ -11225,71 +11032,6 @@
             ],
             "title": "CDC Social Vulnerability Index (SVI)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "\u2022 Weekly Cumulative RSV Vaccination Coverage and Intent Among Adults 75 Years and Older and 60\u250074 Years with High Risk Conditions Ever Vaccinated with RSV Vaccine by Demographic Characteristics and Jurisdiction \n\n\u2022 Weekly estimates of RSV vaccination coverage and intent among adults 75 years and older and 60\u250074 years with high risk conditions are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html). \n\n\u2022 In June 2023, the Advisory Committee on Immunization Practices (ACIP) voted to recommend that adults aged \u226560 years may receive a single dose of an RSV vaccine, using shared clinical decision-making. In June 2024, the ACIP voted to recommend a single dose of RSV vaccine for all adults 75 years and older and adults 60\u201374 years who are at increased risk for severe RSV disease. The data below captures ever receiving a dose of an RSV vaccine by adults 60 years and older.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/k4cb-dxd7",
-            "issued": "2024-09-26",
-            "keyword": [
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "rsv vaccination",
-                "vsd"
-            ],
-            "landingPage": "https://www.cdc.gov/rsvvaxview/",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States",
-            "temporal": "2024-2025",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Weekly Cumulative RSV Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 75 and Older and 60-74 Years with High-Risk Conditions Ever Vaccinated, United States"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -15777,68 +15519,6 @@
             ],
             "title": "PubMed total records by publication year"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DHDSP Requests",
-                "hasEmail": "mailto:dhdsprequests@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Heart-Disease-Mortality-Data-Among-US-Adults-35-by/i2vk-mgdh",
-            "description": "2013 to 2015, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2vk-mgdh/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2vk-mgdh/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2vk-mgdh/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2vk-mgdh/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/i2vk-mgdh",
-            "issued": "2023-07-18",
-            "keyword": [
-                "cardiovascular disease",
-                "county",
-                "heart disease"
-            ],
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-08-25",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "theme": [
-                "Heart Disease & Stroke Prevention"
-            ],
-            "title": "Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -15886,7 +15566,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -16671,7 +16351,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -16719,72 +16399,6 @@
             ],
             "title": "Biological General Repository for Interaction Datasets (BioGRID)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DHDSP Requests",
-                "hasEmail": "mailto:dhdsprequests@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Health-and-Nutrition-Examination-Survey-N/5svk-8bnq",
-            "description": "1999\u20132000 to 2017\u20132018. The National Health and Nutrition Examination Survey (NHANES) is a program of studies designed to assess the health and nutritional status of adults and children in the United States. The survey is unique in that it combines interviews and physical examinations. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data can be plotted as trends and stratified by age group, sex, and race/ethnicity.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5svk-8bnq/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5svk-8bnq/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5svk-8bnq/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5svk-8bnq/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/5svk-8bnq",
-            "issued": "2023-07-18",
-            "keyword": [
-                "blood pressure",
-                "cardiovascular disease",
-                "cardiovascular health",
-                "cholesterol",
-                "cvd risk factors",
-                "hypertension",
-                "sodium"
-            ],
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2024-04-09",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "theme": [
-                "Heart Disease & Stroke Prevention"
-            ],
-            "title": "National Health and Nutrition Examination Survey (NHANES) - National Cardiovascular Disease Surveillance System"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -17261,7 +16875,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -17788,57 +17402,6 @@
             ],
             "title": "Minimum Data Set Frequency"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "These weekly COVID-19 vaccination coverage estimates are for pregnant persons who are fully vaccinated before and during pregnancy based on data  from the Vaccine Safety Datalink*.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/w6be-99qd/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/w6be-99qd/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/w6be-99qd/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/w6be-99qd/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/w6be-99qd",
-            "issued": "2022-02-01",
-            "landingPage": "https://data.cdc.gov/d/w6be-99qd",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-06-23",
-            "programCode": [
-                "009:026"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Pregnancy & Vaccination"
-            ],
-            "title": "Weekly Data: COVID-19 vaccination among pregnant people ages 18-49 years before and during pregnancy overall, by race/ethnicity, and week ending date - Vaccine Safety Datalink,* United States"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -19743,68 +19306,6 @@
             ],
             "title": "CoreSEt filters v2.10.14 (coreset-dev)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/d/vkwg-yswv",
-            "description": "2013-2018. This dataset is a de-identified summary table of vision and eye health data indicators from BRFSS, stratified by all available combinations of age group, race/ethnicity, gender, risk factor and state. BRFSS is a system of telephone surveys conducted by CDC that collect state data about U.S. residents regarding their health-related risk behaviors, chronic health conditions, and use of preventive services. BRFSS completes more than 400,000 adult interviews each year across 50 states, the District of Columbia, and three U.S. territories. BRFSS data for VEHSS includes one question from the core component related to Visual Function. Data were suppressed following NCHS standards. Data will be updated as it becomes available. Detailed information on VEHSS BRFSS analyses can be found on the VEHSS BRFSS webpage (link). General information about BRFSS can be found on the BRFSS website (https://www.cdc.gov/brfss). The VEHSS BRFSS dataset was last updated in November 2019.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vkwg-yswv/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vkwg-yswv/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vkwg-yswv/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vkwg-yswv/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/vkwg-yswv",
-            "issued": "2024-03-20",
-            "keyword": [
-                "brfss",
-                "contact lenses",
-                "glasses",
-                "visual function"
-            ],
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2024-03-20",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/brfss",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/behavioral-risk-factors-surveillance-system.html"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "Behavioral Risk Factors \u2013 Vision and Eye Health Surveillance"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -21649,7 +21150,7 @@
             ],
             "landingPage": "https://www.cdc.gov/nchs/nhis/shs.htm",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2024-12-05",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -25411,69 +24912,6 @@
             ],
             "title": "Daily County-Level Ozone Concentrations, 2001-2019"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Vax Views",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Monthly Cumulative Influenza Vaccination Coverage, by Race/Ethnicity, Pregnant Persons 18 years to 49 years, United States",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9wzx-rwzv/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9wzx-rwzv/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9wzx-rwzv/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/9wzx-rwzv/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/9wzx-rwzv",
-            "issued": "2021-03-10",
-            "keyword": [
-                "flu",
-                "influenza",
-                "pregnant persons",
-                "vaccine coverage"
-            ],
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2022-04-01",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "Vaccine Safety Datalink"
-            ],
-            "theme": [
-                "Pregnancy & Vaccination"
-            ],
-            "title": "Monthly Cumulative Influenza Vaccination Coverage, by Race/Ethnicity, Pregnant Persons 18 years to 49 years, United States"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -25566,73 +25004,6 @@
             ],
             "title": "Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County \u2013 2019-2021"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Monthly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "\u2022 National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on the Updated 2023-24 COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics. \n\n\u2022 The data start in October 2023.  \n\n\u2022 The archived data can be found here:",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/uc4z-hbsd/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/uc4z-hbsd/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/uc4z-hbsd/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/uc4z-hbsd/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/uc4z-hbsd",
-            "issued": "2024-01-16",
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
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adults.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-08-09",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2023-24",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -26253,69 +25624,6 @@
             ],
             "title": "NCHS - Nonmarital Birth Rates, by Age Group for All Women Age 15-44: United States, 1970-2013"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Weekly RSV Vaccination Coverage of Adults 60 Years and Older by Jurisdiction \n\n\u2022 RSV vaccination coverage among adults 60 years and older is assessed through the National Immunization Survey-Adult COVID Module, providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n \u2022 The CDC recommended the RSV vaccine for adults 60 years and older in July 2023. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5vw4-awn6/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5vw4-awn6/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5vw4-awn6/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/5vw4-awn6/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/5vw4-awn6",
-            "issued": "2023-12-11",
-            "keyword": [
-                "nis-acm",
-                "older adults",
-                "rsv",
-                "vaccination"
-            ],
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-09-11",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2023-2024",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Differences in Weekly Cumulative Percentage of Adults 60 Years and Older Vaccinated with Respiratory Syncytial Virus (RSV) Vaccine by Selected Demographics"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -26761,7 +26069,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -30155,63 +29463,6 @@
             ],
             "title": "Mapping Injury, Overdose, and Violence - State"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Assessment Branch, Immunization Services Division, NCIRD, CDC",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "These archived cumulative COVID-19 vaccination coverage estimates are for persons who were pregnant anytime from December 20, 2020, to January 20, 2022, and received at least 1 dose of COVID-19 vaccine during pregnancy based on data from the Vaccine Safety Datalink*. As of January 20, 2022, after moving to reporting weekly estimates, the figures on https://covid.cdc.gov/covid-data-tracker/#vaccinations-pregnant-women no longer present cumulative estimates, and these   archived data are no longer updated.\n\nFor these cumulative data, on December 15, 2021, an error was identified where pregnant people who had received an additional or booster dose of a COVID-19 vaccine were not included in the coverage estimates. After correcting the error, coverage estimates for the week of December 11, 2021, increased overall and by race/ethnicity. The persons that were inadvertently excluded have been counted in the December 11, 2021, estimates. Prior weeks\u2019 estimates have not been updated.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4ht3-nbmd/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4ht3-nbmd/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4ht3-nbmd/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4ht3-nbmd/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/4ht3-nbmd",
-            "issued": "2021-11-24",
-            "keyword": [
-                "covid-19 vaccine",
-                "covid tracker",
-                "pregnancy",
-                "vsd"
-            ],
-            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccinations-pregnant-women",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2022-04-22",
-            "programCode": [
-                "009:026"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Archived Cumulative Data: Percent of pregnant people aged 18-49 years receiving at least one dose of a COVID-19 vaccine during pregnancy overall, by race/ethnicity, and date reported to CDC-Vaccine Safety Datalink*, United States | December 20, 2020 \u2013 Jan"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -30455,7 +29706,7 @@
             "issued": "2023-06-29",
             "landingPage": "https://data.cdc.gov/d/bc4h-zh8r",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-07-26",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:028"
             ],
@@ -32779,7 +32030,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -33220,8 +32471,8 @@
                 "coronavirus",
                 "covid-19",
                 "hospital capacity",
-                "hospitalizations",
                 "hospital occupancy",
+                "hospitalizations",
                 "icu beds",
                 "influenza",
                 "inpatient beds",
@@ -33234,7 +32485,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -35541,7 +34792,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -36292,52 +35543,6 @@
             ],
             "title": "Weekly United States COVID-19 Hospitalization Metrics by County \u2013 ARCHIVED"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Tuberculosis Epidemiologic Studies Consortium",
-                "hasEmail": "mailto:tbesc3@cdc.gov"
-            },
-            "description": "This was a head-to-head comparison of three FDA-approved tests for TB infection (Tuberculin Skin Test, QuantiFERON-TB Gold In-Tube, and T-SPOT.TB) in populations at high risk of latent TB infection and/or progression to TB disease.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/5hpj-p74g/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/5hpj-p74g",
-            "issued": "2024-03-20",
-            "keyword": [
-                "interferon gamma release assay (igra)",
-                "quantiferon (qft)",
-                "t-spot.tb (tspot)",
-                "tuberculin skin test (tst)",
-                "tuberculosis"
-            ],
-            "landingPage": "https://data.cdc.gov/d/5hpj-p74g",
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-11-26",
-            "programCode": [
-                "009:027"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "National Center for HIV",
-                "Viral Hepatitis",
-                "STD",
-                "and TB Prevention"
-            ],
-            "title": "Tuberculosis Epidemiologic Studies Consortium (TBESC)-II Part A: Comparison of the Tuberculin Skin Test and Interferon-Gamma Release Assays in Diagnosing Infection with Mycobacterium tuberculosis and Prediction of Progression to Tuberculosis Disease"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -36837,7 +36042,7 @@
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "description": "Weekly COVID-19 Vaccination Coverage, Pregnant Persons 18-49 Years Old\n\n\u2022 COVID-19 vaccination coverage among pregnant persons is assessed through the Vaccine \n   Safety Datalink* \n\n\u2022 Data on updated 2023-24 COVID-19 vaccinations among pregnant persons was available starting September 23, 2023, and includes doses received starting September 14, 2023.",
+            "description": "Weekly COVID-19 Vaccination Coverage, Pregnant Women 18-49 Years Old\n\n\u2022 COVID-19 vaccination coverage among pregnant women is assessed through the Vaccine Safety Datalink* \n\n\u2022 Data on updated 2023-24 COVID-19 vaccinations among pregnant women was available starting September 23, 2023, and includes doses received starting September 14, 2023.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36873,7 +36078,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2024-08-28",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -36886,7 +36091,7 @@
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "title": "Weekly COVID-19 Vaccination Coverage among Pregnant Persons by Race and Ethnicity"
+            "title": "Weekly COVID-19 Vaccination Coverage among Pregnant Women by Race and Ethnicity"
         },
         {
             "@type": "dcat:Dataset",
@@ -37091,7 +36296,7 @@
             ],
             "landingPage": "https://www.cdc.gov/rsv/php/surveillance/rsv-net.html",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:038"
             ],
@@ -38131,7 +37336,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -39184,7 +38389,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -41226,7 +40431,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -45530,7 +44735,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -46823,7 +46028,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/xnjn-rdmd",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-17",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -47235,7 +46440,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -47537,70 +46742,6 @@
             },
             "title": "Drug Abuse Warning Network (DAWN-2011)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/National-Health-Interview-Survey-NHIS-Vision-and-E/2t2r-sf6s",
-            "description": "2014-15 merged, 2016-17 merged. This dataset is a de-identified summary table of vision and eye health data indicators from NHIS, stratified by all available combinations of age group, race/ethnicity, gender, and risk factor. NHIS is an annual household survey conducted by the National Center for Health Statistics at CDC that monitors trends in illness, disabilities, and progress towards national health objectives. Approximate sample size is 35,000 households and 87,500 persons annually. NHIS data for VEHSS includes questions related to Visual Function. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Data will be updated as it becomes available. Detailed information on VEHSS NHIS analyses can be found on the VEHSS NHIS webpage (link). Additional information about NHIS can be found on the NHIS website (http://www.cdc.gov/nchs/nhis/about_nhis.htm). The VEHSS NHIS dataset was last updated in November 2019.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/2t2r-sf6s/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/2t2r-sf6s/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/2t2r-sf6s/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/2t2r-sf6s/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/2t2r-sf6s",
-            "issued": "2023-09-21",
-            "keyword": [
-                "blind",
-                "contact lenses",
-                "glasses",
-                "nhis",
-                "vision correction",
-                "visual function"
-            ],
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2023-09-21",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "http://www.cdc.gov/nchs/nhis/about_nhis.htm",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-health-interview-survey.html"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "National Health Interview Survey (NHIS) \u2013 Vision and Eye Health Surveillance"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -47769,69 +46910,6 @@
             ],
             "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DHDSP Requests",
-                "hasEmail": "mailto:dhdsprequests@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Center-for-Medicare-Medicaid-Services-CMS-Medicare/iw6q-r3ja",
-            "description": "2016\u20132021. CMS compiles claims data for Medicare and Medicaid patients across a variety of categories and years. This includes Inpatient and Outpatient claims, Master Beneficiary Summary Files, and many other files. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (national and state) and indicator. The data can be plotted as trends and stratified by sex and race/ethnicity.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/iw6q-r3ja/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/iw6q-r3ja/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/iw6q-r3ja/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/iw6q-r3ja/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/iw6q-r3ja",
-            "issued": "2023-08-11",
-            "keyword": [
-                "cardiovascular disease",
-                "claims data",
-                "heart disease",
-                "stroke"
-            ],
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2024-04-09",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "theme": [
-                "Heart Disease & Stroke Prevention"
-            ],
-            "title": "Center for Medicare & Medicaid Services (CMS) , Medicare Claims data"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -48457,6 +47535,74 @@
             ],
             "title": "DQS Death rates for heart disease, by sex, race, Hispanic origin, and age: United States from CDC WONDER"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Weekly",
+            "bureauCode": [
+                "009:20"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "description": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Women 18-49 years\n\n\u2022 These monthly flu vaccination coverage estimates for pregnant women are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD), a collaboration between CDC\u2019s Immunization Safety Office and nine integrated health care organizations.\u00a7 This system has been used annually to estimate vaccination coverage among pregnant women. COVID-19 vaccination coverage for pregnant women is available here.\n\n\u2022 Figure 3A. Monthly Cumulative Influenza Vaccination Coverage*, by Flu Season and Race/Ethnicity, Pregnant Women 18-49 years, United States, Data Source: Vaccine Safety Datalink\n\n\u2022 Figure 3B. Cumulative Influenza Vaccination Coverage*, by Month, Flu Season, and Race/Ethnicity, Pregnant Women 18-49 years, United States, Data Source: Vaccine Safety Datalink\n\n\u2022 For any month\u2019s coverage estimate, the denominator is the number of women with a pregnancy during the current flu season (defined as August through March) beginning before or during the specified month. The numerator is the subset of the denominator who have received flu vaccination prior to, during, or after pregnancy. The denominator increases as more women are identified as pregnant or having been pregnant during the flu season. Cumulative vaccination coverage for one month may be lower than cumulative coverage for a previous month due to addition to the denominator of women who are less likely to have received vaccination.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkr7-scx6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkr7-scx6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkr7-scx6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkr7-scx6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/nkr7-scx6",
+            "issued": "2025-01-31",
+            "keyword": [
+                "children",
+                "flu",
+                "influenza",
+                "nis",
+                "nis-flu",
+                "vaccine coverage"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "language": [
+                "English"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-31",
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
+            "spatial": "United States",
+            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
+            "theme": [
+                "Vaccinations"
+            ],
+            "title": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Women 18-49 years"
+        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -50465,57 +49611,6 @@
             ],
             "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Month"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Estimates are for pregnant persons who are up-to-date with COVID-19 vaccines, overall and by race and ethnicity based on data from the Vaccine Safety Datalink*.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/hv7b-3sw8",
-            "issued": "2023-06-22",
-            "landingPage": "https://data.cdc.gov/d/hv7b-3sw8",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-08-02",
-            "programCode": [
-                "009:026"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Pregnancy & Vaccination"
-            ],
-            "title": "Data: COVID-19 vaccination among pregnant people aged 18-49 years overall, by race and ethnicity, and date reported to CDC - Vaccine Safety Datalink,* United States"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -50768,7 +49863,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -50829,7 +49924,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -51927,67 +51022,6 @@
             ],
             "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age, 2015-2021"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "James Singleton",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/udsf-9v7b/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/udsf-9v7b/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/udsf-9v7b/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/udsf-9v7b/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/udsf-9v7b",
-            "issued": "2022-07-06",
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
-            "landingPage": "https://data.cdc.gov/d/udsf-9v7b",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2024-01-24",
-            "programCode": [
-                "009:026"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)-Archived"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
@@ -61174,58 +60208,6 @@
             ],
             "title": "NCHS Research and Development Survey (RANDS) Round 2 during COVID-19 non-probability sampled Restricted File"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DASH Public Inquiries",
-                "hasEmail": "mailto:nccddashinfo@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/svam-8dhg",
-            "description": "1991-2017. High School Dataset. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors \r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and \r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human \r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors \r\nthe prevalence of obesity and asthma and other priority health behaviors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/svam-8dhg",
-            "issued": "2023-07-19",
-            "landingPage": "https://www.cdc.gov/healthyyouth/data/yrbs/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-08-22",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Youth Risk Behaviors"
-            ],
-            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School - Excluding Sexual Identity"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -63194,71 +62176,6 @@
             ],
             "title": "Library LinkOut"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DHDSP Requests",
-                "hasEmail": "mailto:dhdsprequests@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/dataset/Behavioral-Risk-Factor-Surveillance-System-BRFSS-N/fwns-azgu",
-            "description": "2011\u20132020. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (national, regional, state, and selected sites) and indicator, and they include CVDs (e.g., heart failure) and risk factors (e.g., hypertension). The data can be plotted as trends and stratified by age group, sex, and race/ethnicity.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ikwk-8git/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ikwk-8git/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ikwk-8git/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ikwk-8git/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/ikwk-8git",
-            "issued": "2023-08-11",
-            "keyword": [
-                "brfss",
-                "cardiovascular disease",
-                "coronary heart disease",
-                "hypertension",
-                "risk factors",
-                "stroke"
-            ],
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2024-04-09",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "theme": [
-                "Heart Disease & Stroke Prevention"
-            ],
-            "title": "Behavioral Risk Factor Surveillance System (BRFSS) -  National Cardiovascular Disease Surveillance Data"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -63699,68 +62616,6 @@
             ],
             "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/d/thir-stei",
-            "description": "2014 - 2022 (excluding 2020). This dataset is a de-identified summary table of vision and eye health data indicators from ACS, stratified by all available combinations of age group, race/ethnicity, gender, and state. ACS is an annual nationwide survey conducted by the U.S. Census Bureau that collects information on demographic, social, economic, and housing characteristics of the U.S. population. Approximate sample size is 3 million annually. ACS data for VEHSS includes one question related to Visual Function. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Data will be updated as it becomes available. Detailed information on VEHSS ACS analyses can be found on the VEHSS ACS webpage (link). Additional information about ACS can be found on the U.S. Census Bureau website (https://www.census.gov/content/dam/Census/programs-surveys/acs/about/ACS_Information_Guide.pdf). The VEHSS ACS dataset was last updated April 2024",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/thir-stei",
-            "issued": "2024-05-01",
-            "keyword": [
-                "acs",
-                "contact lenses",
-                "glasses",
-                "visual function"
-            ],
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2024-05-01",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.census.gov/content/dam/Census/programs-surveys/acs/about/ACS_Information_Guide.pdf",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/american-community-survey.html"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "American Community Survey (ACS) \u2013 Vision and Eye Health Surveillance"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -64229,7 +63084,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/sumd-iwm8",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-17",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -67398,68 +66253,6 @@
             ],
             "title": "CoreSet measure v2.10.64 (coreset-dev)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DASH Public Inquiries",
-                "hasEmail": "mailto:nccddashinfo@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/q6p7-56au",
-            "description": "2015-2017. High School Dataset \u2013 Including Sexual Orientation. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors\r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and\r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human\r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors\r\nthe prevalence of obesity and asthma and other priority health behaviors.  This dataset contains national, state, and local data from 2015 that includes two aspects of sexual orientation \u2013 sexual identity and sex of sexual contacts.  Additional information about the YRBSS can be found at www.cdc.gov/yrbss.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/q6p7-56au/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/q6p7-56au",
-            "issued": "2023-07-14",
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
-            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-08-25",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Youth Risk Behaviors"
-            ],
-            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School \u2013  Including Sexual Orientation"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -68581,7 +67374,7 @@
             "issued": "2024-05-03",
             "landingPage": "https://www.cdc.gov/resp-net/dashboard/index.html",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:038"
             ],
@@ -69251,7 +68044,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/x9gk-5huc",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-01-27",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -71643,7 +70436,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -72826,7 +71619,7 @@
             "issued": "2024-06-26",
             "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:038"
             ],
@@ -73519,7 +72312,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/ahrf-yqdt",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-17",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -73758,7 +72551,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -78172,7 +76965,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/rdmq-nq56",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:037"
             ],
@@ -79109,7 +77902,7 @@
             "issued": "2024-02-07",
             "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2024-09-17",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -79486,74 +78279,6 @@
             ],
             "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DPH Public Inquiries",
-                "hasEmail": "mailto:PublicInquiriesDPH@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Healthy-Aging/Alzheimer-s-Disease-and-Healthy-Aging-Data/hfr9-rurv",
-            "description": "2015-2022. This data set contains data from BRFSS.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hfr9-rurv/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/hfr9-rurv",
-            "issued": "2024-04-29",
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
-            "landingPage": "https://www.cdc.gov/aging/index.html",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2024-04-29",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/aging/index.html"
-            ],
-            "theme": [
-                "Healthy Aging"
-            ],
-            "title": "Alzheimer's Disease and Healthy Aging Data"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -79672,7 +78397,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -80264,65 +78989,6 @@
             ],
             "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DASH Public Inquiries",
-                "hasEmail": "mailto:nccddashinfo@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/k5bc-k3g8",
-            "description": "1991-2017. Middle School Dataset. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors \r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and \r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human \r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors \r\nthe prevalence of obesity and asthma and other priority health behaviors.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5bc-k3g8/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/k5bc-k3g8",
-            "issued": "2023-07-19",
-            "keyword": [
-                "middle school",
-                "risk behavior",
-                "survey",
-                "youth online",
-                "yrbs"
-            ],
-            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2023-08-25",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Youth Risk Behaviors"
-            ],
-            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): Middle School"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -80613,7 +79279,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/seuz-s2cv",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:037"
             ],
@@ -84099,69 +82765,6 @@
             ],
             "title": "devAuto_briefType"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Weekly RSV Vaccination Coverage of Adults 60 Years and Older by Demographic Characteristics \n\n\u2022 RSV vaccination coverage among adults 60 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 The CDC recommended the RSV vaccine for adults 60 years and older in July 2023.  (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/mx2d-yjrk/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/mx2d-yjrk",
-            "issued": "2023-11-07",
-            "keyword": [
-                "nis-acm",
-                "older adults",
-                "rsv",
-                "vaccination"
-            ],
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-08-28",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2023-2024",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine by Demographic Characteristics"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -84621,7 +83224,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/4bc2-bbpq",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:026"
             ],
@@ -86242,7 +84845,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -88677,7 +87280,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -89159,68 +87762,6 @@
             ],
             "title": "Telemedicine Use in the Last 4 Weeks"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Weekly COVID-19 Vaccination Coverage of Adults 18 Years and Older by Demographic Characteristics \n\n\u2022 COVID-19 vaccination coverage among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n \n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm35-qkiu/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/hm35-qkiu",
-            "issued": "2023-11-07",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination",
-                "nis-acm"
-            ],
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-08-28",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2023-2024",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -90206,68 +88747,6 @@
             },
             "title": "ONC Health Information Technology for Economic and Clinical Health (HITECH) Grantee Crosswalk"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "\u2022 COVID-19 vaccination coverage and intent among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pakc-hru3/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/pakc-hru3",
-            "issued": "2023-11-03",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination",
-                "nis-acm"
-            ],
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-08-28",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2023-2024",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 18 Years and Older Vaccinated with Updated 2023-24 COVID-19 Vaccine"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -92353,7 +90832,7 @@
             ],
             "landingPage": "https://learn.nlm.nih.gov/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-01-31",
+            "modified": "2025-02-01",
             "programCode": [
                 "009:041"
             ],
@@ -93230,7 +91709,7 @@
             "issued": "2024-11-08",
             "landingPage": "https://data.cdc.gov/d/f3zz-zga5",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:038"
             ],
@@ -94109,7 +92588,7 @@
             ],
             "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/children-coverage-vaccination.html",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2024-08-28",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -95244,7 +93723,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -95353,7 +93832,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/53g5-jf7x",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:026"
             ],
@@ -97554,73 +96033,6 @@
             ],
             "title": "CoreSet pillar v2.10.64 (coreset-impl)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/National-Health-and-Nutrition-Examination-Survey-N/tdbk-8ubw",
-            "description": "1999-2008; 2005-2008. This dataset is a de-identified summary table of vision and eye health data indicators from NHANES, stratified by all available combinations of age group, race/ethnicity, gender, and risk factor. NHANES is a program of studies conducted by the National Center for Health Statistics at CDC designed to assess the health and nutritional status of adults and children in the U.S, and combines interviews and physical examinations. NHANES stopped collecting vision and eye health data in 2008. Approximate sample size is 5,000 persons per year. NHANES data for VEHSS includes questions and examinations related to Visual Function, Vision Exam Measures, Eye Health Conditions, Service Utilization, and Examination Measures. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Detailed information on VEHSS NHANES analyses can be found on the VEHSS NHANES webpage (https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-health-and-nutrition-examination-survey.html). Additional information about NHANES can be found on the NHANES website (https://www.cdc.gov/nchs/nhanes/index.htm). The VEHSS NHANES dataset was last updated in June 2018.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdbk-8ubw/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdbk-8ubw/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdbk-8ubw/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/tdbk-8ubw/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/tdbk-8ubw",
-            "issued": "2023-09-21",
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
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2023-09-21",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/index.htm",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-health-and-nutrition-examination-survey.html"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "National Health and Nutrition Examination Survey (NHANES) \u2013 Vision and Eye Health Surveillance"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -99443,75 +97855,6 @@
             ],
             "title": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DNPAO Public Inquiries",
-                "hasEmail": "mailto:dnpaoinfo@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/CDC-Nutrition-Physical-Activity-and-Obesity-Legisl/nxst-x9p4",
-            "description": "This dataset contains policy data for 50 US states and DC from 2001 to 2017. Data include information related to state legislation and regulations on nutrition, physical activity, and obesity in settings such as early care and education centers, restaurants, schools, work places, and others. To identify individual bills, use the identifier ProvisionID.  A bill or citation may appear more than once because it could apply to multiple health or policy topics, settings, or states. As of Q 2 2016, data include only enacted legislation.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/nxst-x9p4/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/nxst-x9p4/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/nxst-x9p4/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/nxst-x9p4/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/nxst-x9p4",
-            "issued": "2023-07-18",
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
-            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-08-25",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "http://www.cdc.gov/nccdphp/DNPAO"
-            ],
-            "theme": [
-                "Nutrition",
-                "Physical Activity",
-                "and Obesity"
-            ],
-            "title": "CDC Nutrition, Physical Activity, and Obesity - Legislation"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -104269,8 +102612,8 @@
                 "coronavirus",
                 "covid-19",
                 "hospital capacity",
-                "hospitalizations",
                 "hospital occupancy",
+                "hospitalizations",
                 "icu beds",
                 "influenza",
                 "inpatient beds",
@@ -104283,7 +102626,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -109043,7 +107386,7 @@
             "issued": "2024-02-16",
             "landingPage": "https://data.cdc.gov/d/9xt5-u42s",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2024-12-23",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -109623,7 +107966,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -112231,10 +110574,10 @@
             "issued": "2023-09-22",
             "keyword": [
                 "covid",
-                "covid19",
                 "covid-19",
-                "covidnet",
                 "covid-net",
+                "covid19",
+                "covidnet",
                 "epi curve",
                 "hospitalizations",
                 "icu",
@@ -112242,15 +110585,15 @@
                 "percent icu",
                 "percent in-hospital death",
                 "percent mechanically ventilated",
+                "resp-net",
                 "respiratory illness",
                 "respiratory virus response",
                 "respnet",
-                "resp-net",
                 "surveillance"
             ],
             "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:038"
             ],
@@ -114150,72 +112493,6 @@
             ],
             "title": "Tests for antibodies to trachoma PGP3 antigen"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Private-Medicaid-Claims-MAX-Vision-and-Eye-Health-/bwx3-gx66",
-            "description": "2016-2019. This dataset is a de-identified summary table of prevalence rates for vision and eye health data indicators from the Medicaid Analytic eXtract (MAX) data. Medicaid MAX are a set of de-identified person-level data files with information on Medicaid eligibility, service utilization, diagnoses, and payments. The MAX data contain a convenience sample of claims processed by Medicaid and Children\u2019s Health Insurance Program (CHIP) fee for service and managed care plans.  Not all states are included in MAX in all years, and as of November 2019, 2014 data is the latest available.  Prevalence estimates are stratified by all available combinations of age group, gender, and state.  Detailed information on VEHSS Medicare analyses can be found on the VEHSS Medicaid MAX webpage (cdc.gov/visionhealth/vehss/data/claims/medicaid.html). Information on available Medicare claims data can be found on the ResDac website (www.resdac.org). The VEHSS Medicaid MAX dataset was last updated May 2023.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/bwx3-gx66",
-            "issued": "2023-09-21",
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
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2023-09-21",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://wwwdev.cdc.gov/visionhealth/vehss/data/claims/medicaid.html",
-                "https://www.medicaid.gov/medicaid/index.html"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "Medicaid Claims (MAX) - Vision and Eye Health Surveillance"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -114941,69 +113218,6 @@
             ],
             "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine.\n\n \u2022 RSV vaccination coverage among adults ages 60 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n \u2022 The CDC recommended the RSV vaccine for adults ages 60 years and older in July 2023. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/gzbv-dn9g",
-            "issued": "2023-11-07",
-            "keyword": [
-                "nis-acm",
-                "older adults",
-                "rsv",
-                "vaccination"
-            ],
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-08-28",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2023-2024",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -116704,7 +114918,7 @@
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "description": "Weekly RSV Vaccination Coverage, Pregnant Persons 18-49 Years Old\n\n\u2022 RSV vaccination coverage among pregnant persons is assessed through the Vaccine Safety Datalink*\n\n\u2022 Data on RSV vaccinations among pregnant persons was available starting September 22, 2023, and includes doses received starting September 24, 2023.",
+            "description": "Weekly RSV Vaccination Coverage, Pregnant Women 18-49 Years Old\n\n\u2022 RSV vaccination coverage among pregnant women is assessed through the Vaccine Safety Datalink*\n\n\u2022 Data on RSV vaccinations among pregnant women was available starting September 22, 2023, and includes doses received starting September 24, 2023.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -116739,7 +114953,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2024-04-17",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -116752,7 +114966,7 @@
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant Persons by Race and Ethnicity"
+            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant Women by Race and Ethnicity"
         },
         {
             "@type": "dcat:Dataset",
@@ -117473,71 +115687,6 @@
             ],
             "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Shell-Commercial-Medical-Insurance-MSCANCC-Vision-/a35h-9yn4",
-            "description": "2016. This dataset is a de-identified summary table of prevalence rates for vision and eye health data indicators from the 2016 MarketScan\u00ae Commercial Claims and Encounters Data (CCAE) is produced by Truven Health Analytics, a division of IBM Watson Health.  The CCEA data contain a convenience sample of insurance claims information from person with employer-sponsored insurance and their dependents, including 43.6 million person years of data. Prevalence estimates are stratified by all available combinations of age group, gender, and state.  Detailed information on VEHSS MarketScan analyses can be found on the VEHSS MarketScan webpage (cdc.gov/visionhealth/vehss/data/claims/marketscan.html). Information on available Medicare claims data can be found on the IBM MarketScan website (https://marketscan.truvenhealth.com). The VEHSS MarketScan summary dataset was last updated November 2019.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/a35h-9yn4",
-            "issued": "2024-12-20",
-            "keyword": [
-                "claims",
-                "diagnosed prevalence",
-                "eye exams",
-                "marketscan",
-                "medical diagnoses",
-                "service utilization",
-                "truven"
-            ],
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2024-12-20",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://wwwdev.cdc.gov/visionhealth/vehss/data/claims/marketscan.html",
-                "https://marketscan.truvenhealth.com/marketscanportal/"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "Commercial Medical Insurance (MSCANCC) - Vision and Eye Health Surveillance"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -118080,71 +116229,6 @@
             ],
             "title": "Hospital Change of Ownership"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Weekly COVID-19 Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \u2022 Weekly estimates of COVID-19 vaccination coverage and intent among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/). \n\nWeekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/ksfb-ug5d",
-            "issued": "2024-09-26",
-            "keyword": [
-                "covid-19 vaccination",
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "vsd"
-            ],
-            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/adult-vaccination-coverage.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2024-2025",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Weekly Cumulative COVID-19 Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -119540,7 +117624,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/5c6r-xi2t",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:037"
             ],
@@ -122216,68 +120300,6 @@
             ],
             "title": "Restructured BETOS Classification System"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DHDSP Requests",
-                "hasEmail": "mailto:dhdsprequests@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Heart-Disease-Mortality-Data-Among-US-Adults-35-by/r35g-znws",
-            "description": "2012 to 2014, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/r35g-znws/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/r35g-znws/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/r35g-znws/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/r35g-znws/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/r35g-znws",
-            "issued": "2023-07-18",
-            "keyword": [
-                "cardiovascular disease",
-                "county",
-                "heart disease"
-            ],
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-08-25",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "theme": [
-                "Heart Disease & Stroke Prevention"
-            ],
-            "title": "Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -122700,7 +120722,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -123925,7 +121947,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -125748,7 +123770,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -126918,7 +124940,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -128297,69 +126319,6 @@
             },
             "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210920 to 20210926"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/d/de4p-4g3k",
-            "description": "2016-17 merged. This dataset is a de-identified summary table of vision and eye health data indicators from the National Survye of Chilrens Health (NSCH), stratified by all available combinations of age group, race/ethnicity, gender, risk factor and state. NSCH is a telephone survey conducted by the National Center for Health Statistics at CDC (currently conducted by the U.S. Census Bureau) that examines the physical and emotional health of children 0-17 years of age. Approximate sample size is 95,000 over two rounds of data collection. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Detailed information on VEHSS NSCH analyses can be found on the VEHSS NSCH webpage (cdc.gov/visionhealth/vehss/data/national-surveys/national-survey-of-childrens-health.html). Additional information about NSCH can be found on the NSCH website (http://childhealthdata.org/learn/NSCH). The VEHSS NSCH dataset was last updated in November 2019.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/de4p-4g3k/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/de4p-4g3k/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/de4p-4g3k/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/de4p-4g3k/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/de4p-4g3k",
-            "issued": "2023-09-21",
-            "keyword": [
-                "contact lenses",
-                "glasses",
-                "nsch",
-                "vision impairment",
-                "visual function"
-            ],
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2023-09-21",
-            "programCode": [
-                "009:029"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "http://childhealthdata.org/learn/NSCH",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/national-survey-of-childrens-health.html"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "National Survey of Children\u2019s Health (NSCH) \u2013 Vision and Eye Health Surveillance"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -132644,8 +130603,8 @@
                 "sdoh-employment",
                 "sdoh-food-access",
                 "sdoh-food-insecurity",
-                "sdoh-higher-education",
                 "sdoh-high-school",
+                "sdoh-higher-education",
                 "sdoh-housing-stability",
                 "sdoh-poverty-income",
                 "sdoh-source-of-health-care",
@@ -132655,7 +130614,7 @@
             ],
             "landingPage": "https://www.cdc.gov/nchs/nhis/shs.htm",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2024-08-12",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -133485,70 +131444,6 @@
             ],
             "title": "NNDSS - TABLE 1HH. Syphilis, Congenital to Syphilis, Primary and Secondary"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DHDSP Requests",
-                "hasEmail": "mailto:dhdsprequests@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Health-Interview-Survey-NHIS-National-Car/fwns-azgu",
-            "description": "2019\u20132020. The National Health Interview Survey (NHIS) has monitored the health of the nation since 1957. NHIS data on a broad range of health topics are collected through personal household interviews. Indicators for this dataset has been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (region) and indicator, and they include CVDs (e.g., heart failure) and risk factors (e.g., hypertension). The data can be plotted as trends and stratified by age group, sex, and race/ethnicity.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fwns-azgu/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fwns-azgu/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fwns-azgu/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fwns-azgu/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/fwns-azgu",
-            "issued": "2023-07-18",
-            "keyword": [
-                "cardiovascular disease",
-                "coronary heart disease",
-                "hypertension",
-                "risk factors",
-                "stroke"
-            ],
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2024-04-09",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "theme": [
-                "Heart Disease & Stroke Prevention"
-            ],
-            "title": "National Health Interview Survey (NHIS) - National Cardiovascular Disease Surveillance Data"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -133633,7 +131528,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -133648,69 +131543,6 @@
             ],
             "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to date with COVID-19 Vaccines and Comparison Between 2023-24 and 2024-25 by Jurisdiction"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DHDSP Requests",
-                "hasEmail": "mailto:dhdsprequests@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Stroke-Mortality-Data-Among-US-Adults-35-by-State-/kpwh-eddm",
-            "description": "2013 to 2015, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kpwh-eddm/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kpwh-eddm/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kpwh-eddm/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kpwh-eddm/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/kpwh-eddm",
-            "issued": "2023-07-18",
-            "keyword": [
-                "cardiovascular disease",
-                "cerebrovascular disease",
-                "county",
-                "stroke"
-            ],
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-08-25",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "theme": [
-                "Heart Disease & Stroke Prevention"
-            ],
-            "title": "Stroke Mortality Data Among US Adults (35+) by State/Territory and County"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -138216,7 +136048,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/vutn-jzwm",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:026"
             ],
@@ -138832,7 +136664,7 @@
             ],
             "landingPage": "https://www.cdc.gov/rsv/php/surveillance/rsv-net.html",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:038"
             ],
@@ -139148,7 +136980,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -139787,70 +137619,6 @@
             ],
             "title": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Behavioral-Risk-Factors-Vision-Eye-Health/pttf-ck53",
-            "description": "2005-2016. This dataset includes data from the retired BRFSS Vision Module. From 2005-2011 the BRFSS employed a ten question vision module regarding vision impairment, access and utilization of eye care, and self-reported eye diseases. In 2013 and subsequently, one question in the core of BRFSS asks about vision: \u201cAre you blind or do you have serious difficulty seeing, even when wearing glasses?\u201d The latest data for this core question can be found in the Vision and Eye Health Surveillance System (VEHSS). VEHSS is intended to provide population estimates of vision loss function, eye diseases, health disparities, as well as barriers and facilitators to access to vision and eye care. This information can be used for designing, implementing, and evaluating vision and eye health prevention programs. To access the latest BRFSS data, (2013-2017) view the Behavioral Risk Factors \u2013 Vision and Eye Health Surveillance dataset (https://chronicdata.cdc.gov/Vision-Eye-Health/Behavioral-Risk-Factors-Vision-and-Eye-Health-Surv/vkwg-yswv).",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pttf-ck53/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pttf-ck53/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pttf-ck53/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pttf-ck53/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/pttf-ck53",
-            "issued": "2023-09-21",
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
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-09-21",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "BRFSS Vision Module Data \u2013 Vision & Eye Health"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -140152,7 +137920,7 @@
             ],
             "landingPage": "https://data.cdc.gov/d/7xva-uux8",
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-24",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:026"
             ],
@@ -140634,71 +138402,6 @@
             ],
             "title": "State Drug Utilization Data 2004"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "\u2022 Weekly Influenza Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \n\n \u2022 Weekly estimates of influenza vaccination coverage and intent for vaccination among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html).",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/sw5n-wg2p/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/sw5n-wg2p",
-            "issued": "2024-10-10",
-            "keyword": [
-                "flu vaccination",
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "vsd"
-            ],
-            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/adult-coverage.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2024-2025",
-            "theme": [
-                "Flu Vaccinations"
-            ],
-            "title": "Weekly Influenza Vaccination Coverage and Intent for Vaccination, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -142619,67 +140322,6 @@
             ],
             "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Vision-Service-Plan-VSP-Vision-and-Eye-Health-Surv/4r3g-hv9c",
-            "description": "2016. This dataset is a de-identified summary table of vision and eye health data indicators from VSP, stratified by all available combinations of age group, race/ethnicity, gender, and state. VSP claims for VEHSS provides a convenience sample of vision insurance members representing approximately more than 1 in 4 of the U.S. population. VSP uses a web-based claims submissions system to collect and process claims. The denominator of the rates represents persons with VSP benefits as reported by employers, and is subject to some uncertainty.  VSP data for VEHSS include Service Utilization and Eye Health Condition indicators.  Certain ophthalmic conditions and procedures are covered by health insurance and are not covered by managed vision insurance, claims based eye disease prevalence may therefore be expected to undercount true prevalence.  Person level claims and person counts are not publically available.  Reported rates were suppressed for de-identification to ensure protection of patient privacy. Detailed information on VEHSS VSP analyses can be found on the VEHSS VSP webpage (link). Information on VSP data can be found on the VSP website (www.vsp.com). The VEHSS VSP dataset was last updated in June 2018.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4r3g-hv9c/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4r3g-hv9c/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4r3g-hv9c/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/4r3g-hv9c/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/4r3g-hv9c",
-            "issued": "2023-09-21",
-            "keyword": [
-                "claims",
-                "medical diagnoses",
-                "vsp"
-            ],
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2023-09-21",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.vsp.com",
-                "https://www.cdc.gov/visionhealth/vehss/data/claims/vsp.html"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "Vision Service Plan (VSP) \u2013 Vision and Eye Health Surveillance"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -142730,7 +140372,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -143066,68 +140708,6 @@
             ],
             "title": "Study of Womens Health Across the Nation (SWAN) Biospecimen Repository"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Weekly COVID-19 Vaccination Coverage of Adults 18 Years and Older by Jurisdiction \n\n\u2022 COVID-19 vaccination coverage among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module, providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html) \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/kevv-m5vs",
-            "issued": "2023-12-11",
-            "keyword": [
-                "adults",
-                "covid-19 vaccination",
-                "nis-acm"
-            ],
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-08-28",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2023-2024",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Weekly Differences in Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine by Selected Demographics"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -143526,70 +141106,6 @@
             ],
             "title": "OMIM (Online Mendelian Inheritance in Man)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DDT Public Inquiries",
-                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/d/e28h-tx85",
-            "description": "2014-2019. This dataset is a de-identified summary table of vision and eye health data indicators from Medicare claims, stratified by all available combinations of age group, race/ethnicity, gender, and state. Medicare claims for VEHSS includes beneficiaries who were fully enrolled in Medicare Part B Fee-for-Service (FFS) for the duration of the year. Medicare claims provide a convenience sample that includes approximately 30 million individuals annually, which represents nearly 89% of the US population aged 65 and older and 3.3% of the US population younger than 65, including persons disabled due to blindness. Medicare data for VEHSS include Service Utilization and Medical Diagnoses indicators. Data were suppressed for de-identification to ensure protection of patient privacy. Data will be updated as it becomes available. Detailed information on VEHSS Medicare analyses can be found on the VEHSS Medicare webpage (cdc.gov/visionhealth/vehss/data/claims/medicare.html). Information on available Medicare claims data can be found on the ResDac website (www.resdac.org). The VEHSS Medicare dataset was last updated May 2023.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/e28h-tx85",
-            "issued": "2021-06-15",
-            "keyword": [
-                "claims",
-                "eye exams",
-                "medical diagnoses",
-                "medicare",
-                "service utilization",
-                "treated prevalence"
-            ],
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2023-09-21",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.resdac.org",
-                "https://www.cdc.gov/visionhealth/vehss/data/claims/medicare.html"
-            ],
-            "theme": [
-                "Vision & Eye Health"
-            ],
-            "title": "Medicare Claims \u2013 Vision and Eye Health Surveillance"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -145897,71 +143413,6 @@
             "temporal": "2002-01-01T00:00:00-05:00/2006-01-01T00:00:00-05:00",
             "title": "Head Start Impact Study"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Monthly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VaxView Team",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Infant Protection Against RSV by Maternal RSV Vaccination or Receipt of Nirsevimab and Intent for Nirsevimab Receipt, Reported by Females Aged 18-49 Years Who Have an Infant <8 Months During the RSV Season (born since April 1, 2024)\n\nMonthly estimates of infant protection against RSV by maternal RSV vaccination or receipt of nirsevimab, as well as intent for nirsevimab receipt, were calculated using data from the from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM). (https://www.cdc.gov/nis/about/index.html). Data were reported by adult females aged 18-49 years with infants under the age of 8 months during the RSV season (born since April 1, 2024). The NIS\u2013ACM is an ongoing random-digit-dial cellular telephone survey of households with adults 18 years and older. All estimates are based upon parent-reported receipt of nirsevimab.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/vdz4-qrri",
-            "issued": "2024-09-26",
-            "keyword": [
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "nis-flu",
-                "rsv vaccination",
-                "vsd"
-            ],
-            "landingPage": "https://www.cdc.gov/rsvvaxview/",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "spatial": "United States- National, Region, State",
-            "temporal": "2024-2025",
-            "theme": [
-                "Pregnancy & Vaccination"
-            ],
-            "title": "Infant Protection Against Respiratory Syncytial Virus (RSV) by Maternal RSV Vaccination or Receipt of Nirsevimab, and Intent for Nirsevimab Receipt, United States"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -146158,7 +143609,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
@@ -148411,51 +145862,6 @@
             },
             "title": "National Household Survey on Drug Abuse (NHSDA-1999)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Tuberculosis Epidemiologic Studies Consortium",
-                "hasEmail": "mailto:tbesc3@cdc.gov"
-            },
-            "description": "This study focused on describing and quantifying the steps in the tuberculosis (TB) prevention cascade of care within health department clinics. This included better understanding the proportions of patients with latent TB infection who are identified, offered treatment, accept treatment, and complete treatment.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/epap-ayij/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/epap-ayij",
-            "issued": "2024-10-16",
-            "keyword": [
-                "care cascade",
-                "cascade of care",
-                "latent tuberculosis infection (ltbi)",
-                "tuberculosis (tb)"
-            ],
-            "landingPage": "https://data.cdc.gov/d/epap-ayij",
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-10-16",
-            "programCode": [
-                "009:027"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "National Center for HIV",
-                "Viral Hepatitis",
-                "STD",
-                "and TB Prevention"
-            ],
-            "title": "Tuberculosis Epidemiologic Studies Consortium (TBESC)-II Part B: Strengthening Public Health Surveillance for Latent Tuberculosis Infection"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -149105,74 +146511,6 @@
             ],
             "title": "CoreSEt pillar v2.10.22 (coreset-impl)"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "Weekly",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Vax Views",
-                "hasEmail": "mailto:VaxView@cdc.gov"
-            },
-            "description": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years\n\t\n\u2022  These monthly flu vaccination coverage estimates for pregnant persons are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD), a collaboration between CDC\u2019s Immunization Safety Office and nine integrated health care organizations.\u00a7 This system has been used annually to estimate vaccination coverage among pregnant persons. COVID-19 vaccination coverage for pregnant persons is available here. \n\n\u2022\tFigure 3A. Monthly Cumulative Influenza Vaccination Coverage*, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years, United States, Data Source: Vaccine Safety Datalink \n\n\u2022\tFigure 3B. Cumulative Influenza Vaccination Coverage*, by Month, Flu Season, and Race/Ethnicity, Pregnant Persons 18-49 years, United States, Data Source: Vaccine Safety Datalink \n\n\u2022\tFor any month\u2019s coverage estimate, the denominator is the number of persons with a pregnancy during the current flu season (defined as August through March) beginning before or during the specified month. The numerator is the subset of the denominator who have received flu vaccination prior to, during, or after pregnancy. The denominator increases as more persons are identified as pregnant or having been pregnant during the flu season. Cumulative vaccination coverage for one month may be lower than cumulative coverage for a previous month due to addition to the denominator of persons who are less likely to have received vaccination.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/fz77-au2z",
-            "issued": "2022-09-30",
-            "keyword": [
-                "children",
-                "flu",
-                "influenza",
-                "nis",
-                "nis-flu",
-                "vaccine coverage"
-            ],
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
-            "language": [
-                "English"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "modified": "2024-05-03",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "Vaccine Safety Datalink"
-            ],
-            "spatial": "United States",
-            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
-            "theme": [
-                "Vaccinations"
-            ],
-            "title": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -150009,69 +147347,6 @@
             ],
             "title": "Evidence-Based Practices Resource Center"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DHDSP Requests",
-                "hasEmail": "mailto:dhdsprequests@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Stroke-Mortality-Data-Among-US-Adults-35-by-State-/dhsy-4sea",
-            "description": "2012 to 2014, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dhsy-4sea/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dhsy-4sea/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dhsy-4sea/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/dhsy-4sea/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/dhsy-4sea",
-            "issued": "2023-07-18",
-            "keyword": [
-                "cardiovascular disease",
-                "cerebrovascular disease",
-                "county",
-                "stroke"
-            ],
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2023-08-25",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "theme": [
-                "Heart Disease & Stroke Prevention"
-            ],
-            "title": "Stroke Mortality Data Among US Adults (35+) by State/Territory and County"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -153586,70 +150861,6 @@
             ],
             "title": "NCBI C++ Toolkit Book"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "non-public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DHDSP Requests",
-                "hasEmail": "mailto:dhdsprequests@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Vital-Statistics-System-NVSS-National-Car/kztq-p2jf",
-            "description": "2000\u20132020. NVSS is a secure, web-based data management system that collects and disseminates the Nation's official vital statistics. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (national and state) and indicator; NVSS mortality data include CVDs (e.g., heart failure). The data can be viewed by temporal trends and stratified by age group, sex, and race/ethnicity.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kztq-p2jf/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kztq-p2jf/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kztq-p2jf/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kztq-p2jf/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/kztq-p2jf",
-            "issued": "2023-07-18",
-            "keyword": [
-                "cardiovascular disease",
-                "coronary heart disease",
-                "diseases of the heart",
-                "mortality",
-                "stroke"
-            ],
-            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "modified": "2024-04-09",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "references": [
-                "https://www.cdc.gov/dhdsp/index.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
-                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
-            ],
-            "theme": [
-                "Health"
-            ],
-            "title": "National Vital Statistics System (NVSS) - National Cardiovascular Disease Surveillance Data"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -157302,66 +154513,6 @@
             ],
             "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable"
         },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:20"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DASH Publc Inquiries",
-                "hasEmail": "mailto:nccdDashInfo@cdc.gov"
-            },
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Global-School-based-Student-Health-Survey-GSH/pxpe-pgrg",
-            "description": "2003-2015. Global School dataset.  The Global School-based Student Health Survey (GSHS) was developed by the World Health Organization (WHO) in collaboration with the United Nations' UNICEF, UNESCO, and UNAIDS; and with technical assistance from CDC.  The GSHS is a school-based survey conducted primarily among students aged 13-17 years in countries around the world.  It uses core questionnaire modules that address the leading causes of morbidity and mortality among children and adults worldwide: 1) Alcohol use, 2) dietary behaviors, 3) drug use, 4) hygiene, 5) mental health, 6) physical activity, 7) protective factors, 8) sexual behaviors that contribute to HIV infection, other sexually-transmitted infections, and unintended pregnancy, 9) tobacco use, and 10) violence and unintentional injury.  This dataset contains global data from 2003 \u2013 2015.  Additional information about the GSHS can be found at https://www.cdc.gov/gshs/index.htm.",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "identifier": "https://data.cdc.gov/api/views/pxpe-pgrg",
-            "issued": "2023-07-18",
-            "keyword": [
-                "global",
-                "gshs",
-                "risk behavior",
-                "student health",
-                "survey",
-                "youth online"
-            ],
-            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "modified": "2023-08-25",
-            "programCode": [
-                "009:020"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "theme": [
-                "Youth Risk Behaviors"
-            ],
-            "title": "DASH - Global School-based Student Health Survey (GSHS)"
-        },
         {
             "@type": "dcat:Dataset",
             "accessLevel": "public",
@@ -157652,7 +154803,7 @@
                 "English"
             ],
             "license": "https://www.usa.gov/government-works",
-            "modified": "2025-01-29",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
```

### Changes from dd2190f to ca41c49
**Author:** Automated

**Date:** 2025-02-01 19:16:20+00:00

**Message:** Updated data: Sat Feb  1 19:16:20 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index 4c48019..0866a13 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -136426,8 +136426,8 @@
             "identifier": "87105064-444b-4e33-b5f7-f686ffe9c414",
             "issued": "2013-07-31",
             "keyword": [
-                "indian-health-service",
-                "health care providers"
+                "health care providers",
+                "indian-health-service"
             ],
             "landingPage": "https://healthdata.gov/dataset/ihs-facility-locator",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
```

