# Change History for healthdata.json (Part 6)

### Changes from 31606f9 to dd2190f (Part 5/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
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
@@ -57840,78 +57867,34 @@
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
-            "identifier": "https://data.cdc.gov/api/views/65mz-jvh5",
-            "description": "Provisional counts of deaths by the month the deaths occurred, by age group, sex, and race/ethnicity, for select underlying causes of death for 2020-2021. Final data are provided for 2019. The dataset also includes monthly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
-            "title": "AH Monthly Provisional Counts of Deaths for Select Causes of Death by Sex, Age, and Race and Hispanic Origin",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.xml?accessType=DOWNLOAD",
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
+            "title": "AH Monthly Provisional Counts of Deaths for Select Causes of Death by Sex, Age, and Race and Hispanic Origin"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135162.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-08-29",
-            "keyword": [
-                "bmis",
-                "cder"
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
-            "identifier": "8d346d8d-33c7-47f8-890d-a4ced16e45dd",
             "description": "This contains information that identifies clinical investigators, contract research organizations, and institutional review boards involved in the conduct of Investigational New Drug (IND) studies with human investigational drugs and therapeutic biologics.",
-            "title": "Bioresearch Monitonoring Information System (BMIS)",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57919,43 +57902,37 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "8d346d8d-33c7-47f8-890d-a4ced16e45dd",
+            "issued": "2021-02-25",
+            "keyword": [
+                "bmis",
+                "cder"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135162.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-08-29",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Bioresearch Monitonoring Information System (BMIS)"
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
@@ -57978,47 +57955,46 @@
                     "mediaType": "application/xml"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -58041,40 +58017,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b36e-ru3r",
+            "issued": "2015-01-08",
+            "keyword": [
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
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue Hemorrhagic Fever"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/dv46-8qnu",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-08-12",
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
-            "identifier": "200c2cba-e58d-4a95-aa60-14b99736808d",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58082,40 +58065,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "200c2cba-e58d-4a95-aa60-14b99736808d",
+            "issued": "2022-08-12",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/dv46-8qnu",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
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
+            "title": "State Drug Utilization Data 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/j6ef-yjai",
             "description": "Identifies the conserved domains present in a protein sequence. CD-Search uses RPS-BLAST (Reverse Position-Specific BLAST) to compare a query sequence against position-specific score matrices that have been prepared from conserved domain alignments present in the Conserved Domain Database (CDD).",
-            "title": "CD Search (Conserved Domain Search Service)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58124,57 +58107,42 @@
                     "title": "Conserved Domain Search Service (CD Search) Homepage and Search"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/j6ef-yjai",
+            "issued": "2021-06-30",
+            "keyword": [
+                "computational biology",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi",
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
+            "title": "CD Search (Conserved Domain Search Service)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "rights": "N/A",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "N/A",
-            "issued": "2024-12-23",
-            "temporal": "N/A",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-29",
-            "references": [
-                "NHSN Hospital Respiratory Data (HRD) Reporting: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html  NHSN Hospital Respiratory Data (HRD) Dashboard: https://wwwdev.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html#anchor_83745   Centers for Medicare and Medicaid Services (CMS) requirements: Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses."
-            ],
-            "keyword": [
-                "admissions",
-                "coronavirus",
-                "covid19",
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
             "conformsTo": "N/A",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DHQP",
                 "hasEmail": "mailto:nhsn@cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/mpgq-jmmr",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
+            "describedBy": "N/A",
             "description": "This dataset represents preliminary weekly hospital respiratory data and metrics aggregated to national and state/territory levels reported to CDC\u2019s National Health Safety Network (NHSN) beginning August 2020. This dataset updates weekly on Wednesdays with preliminary data reported to NHSN for the previous reporting week (Sunday \u2013 Saturday). \n\nData for reporting dates through April 30, 2024 represent data reported during a previous mandated reporting period as specified by the HHS Secretary. Data for reporting dates May 1, 2024 \u2013 October 31, 2024 represent voluntarily reported data in the absence of a mandate. Data for reporting dates beginning November 1, 2024 represent data reported during a current mandated reporting period. All data and metrics capturing information on respiratory syncytial virus (RSV) were voluntarily reported until November 1, 2024. All data included in this dataset represent aggregated counts, and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and new hospital admissions with corresponding metrics indicating reporting coverage for a given reporting week. NHSN monitors national and local trends in healthcare system stress and capacity for all acute care and critical access hospitals in the United States.\n\nFor more information on the reporting mandate per the Centers for Medicare and Medicaid Services (CMS) requirements, visit: <a href=\"https://www.cms.gov/medicare/health-safety-standards/quality-safety-oversight-general-information/policy-memos-states/updates-condition-participation-cop-requirements-hospitals-and-critical-access-hospitals-cahs-report\"> Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses</a>.\n\nFor more information regarding NHSN\u2019s collection of these data, including full reporting guidance, visit: <a href=\"https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html\">NHSN Hospital Respiratory Data</a>. \n\nFor data that is considered final for a given reporting week (Sunday \u2013 Saturday), and reflects that which is used in <a href=\"https://www.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html\">NHSN HRD dashboards</a> for publication each Friday, visit: <a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/ua7e-t2fy/about_data\">https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/ua7e-t2fy/about_data</a>. \n\nCDC coordinates weekly forecasts of hospitalization admissions based on this data set. More information about flu forecasting can be found at <a href=\"https://www.cdc.gov/flu-forecasting/about/index.html\">About Flu Forecasting | FluSight | CDC</a>, and information about COVID-19 forecasting and other modeling analyses for the Respiratory Virus Season are available at <a href=\"https://www.cdc.gov/forecast-outbreak-analytics/our-work/respiratory-virus-season-insights.html\">CFA's Insights for Respiratory Virus Season | CFA | CDC</a>.\n\n<b>Source: CDC National Healthcare Safety Network (NHSN).</b> <ul><li><b>Data source description</b> (updated November 15, 2024): As of October 9, 2024, Hospital Respiratory Data (HRD; formerly Respiratory Pathogen, Hospital Capacity, and Supply data or 'COVID-19 hospital data') are reported to HHS through CDC's National Healthcare Safety Network (NHSN) based on updated requirements from the Centers for Medicare and Medicaid Services (CMS). These data were voluntarily reported to NHSN May 1, 2024 until November 1, 2024, at which time CMS began requiring acute care and critical access hospitals to electronically report information via NHSN about COVID-19, influenza, and RSV, hospital bed census and capacity. Hospital bed capacity and occupancy data for all patients and for patients with COVID-19 or influenza for collection dates prior to May 1, 2024, represent data reported during a previously mandated reporting",
-            "title": "Weekly Hospital Respiratory Data (HRD) Metrics by Jurisdiction, National Healthcare Safety Network (NHSN) (Preliminary)",
-            "isPartOf": "N/A",
-            "primaryITInvestmentUII": "N/A",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58197,47 +58165,62 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
-            "describedBy": "N/A",
+            "identifier": "https://data.cdc.gov/api/views/mpgq-jmmr",
+            "isPartOf": "N/A",
+            "issued": "2024-12-23",
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid19",
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
+            "landingPage": "N/A",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-29",
+            "primaryITInvestmentUII": "N/A",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "NHSN Hospital Respiratory Data (HRD) Reporting: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html  NHSN Hospital Respiratory Data (HRD) Dashboard: https://wwwdev.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html#anchor_83745   Centers for Medicare and Medicaid Services (CMS) requirements: Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses."
+            ],
+            "rights": "N/A",
+            "spatial": "US",
             "systemOfRecords": "N/A",
+            "temporal": "N/A",
             "theme": [
                 "Public Health Surveillance"
             ],
-            "accrualPeriodicity": "Weekly",
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Hospital Respiratory Data (HRD) Metrics by Jurisdiction, National Healthcare Safety Network (NHSN) (Preliminary)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/long-covid.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-06-22",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-06-01/2024-09-16",
-            "modified": "2024-10-04",
-            "keyword": [
-                "covid-19",
-                "post-covid"
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
-            "identifier": "https://data.cdc.gov/api/views/gsea-w83j",
             "description": "As part of an ongoing partnership with the Census Bureau, the National Center for Health Statistics (NCHS) recently added questions to assess the prevalence of post-COVID-19 conditions (long COVID), on the experimental Household Pulse Survey. This 20-minute online survey was designed to complement the ability of the federal statistical system to rapidly respond and provide relevant information about the impact of the coronavirus pandemic in the U.S. Data collection began on April 23, 2020. Beginning in Phase 3.5 (on June 1, 2022), NCHS included questions about the presence of symptoms of COVID that lasted three months or longer. Phase 3.5 will continue with a two-weeks on, two-weeks off collection and dissemination approach. \n\nEstimates on this page are derived from the Household Pulse Survey and show the percentage of adults aged 18 and over who a) as a proportion of the U.S. population, the percentage of adults who EVER experienced post-COVID conditions (long COVID). These adults had COVID and had some symptoms that lasted three months or longer; b) as a proportion of adults who said they ever had COVID, the percentage who EVER experienced post-COVID conditions; c) as a proportion of the U.S. population, the percentage of adults who are CURRENTLY experiencing post-COVID conditions. These adults had COVID, had long-term symptoms, and are still experiencing symptoms; d) as a proportion of adults who said they ever had COVID, the percentage who are CURRENTLY experiencing post-COVID conditions; and e) as a proportion of the U.S. population, the percentage of adults who said they ever had COVID.",
-            "title": "Post-COVID Conditions",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58260,56 +58243,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/gsea-w83j",
+            "issued": "2022-06-22",
+            "keyword": [
+                "covid-19",
+                "post-covid"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/long-covid.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2024-10-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S.",
+            "temporal": "2022-06-01/2024-09-16",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Post-COVID Conditions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-d-spending-by-drug",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2022-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-13",
-            "references": [
-                "https://data.cms.gov/resources/medicare-part-d-spending-by-drug-methodology"
-            ],
-            "keyword": [
-                "drugs",
-                "medical suppliers & equipment",
-                "medicare",
-                "medicare prescription drug"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-part-d-spending-by-drug-data-dictionary",
             "description": "The Medicare Part D by Drug dataset presents information on spending for drugs prescribed to Medicare beneficiaries enrolled in Part D by physicians and other healthcare providers. Drugs prescribed in the Medicare Part D program are drugs patients generally administer themselves.\n\n\u00a0\n\nThe dataset focuses on average spending per dosage unit and change in average spending per dosage unit over time. It\u00a0also includes spending information for manufacturer(s) of the drugs as well as consumer-friendly information of drug uses and clinical indications.\n\n\u00a0\n\nDrug spending metrics for Part D drugs are based on the gross drug cost, which represents total spending for the prescription claim, including Medicare, plan, and beneficiary payments. The Part D spending metrics do not reflect any manufacturers\u2019 rebates or other price concessions as CMS is prohibited from publicly disclosing such information.",
-            "title": "Medicare Part D Spending by Drug",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Part D Spending by Drug : 2022-01-01"
                 },
                 {
@@ -58325,62 +58305,49 @@
                     "title": "Medicare Part D Spending by Drug : 2022-01-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-part-d-spending-by-drug-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "drugs",
+                "medical suppliers & equipment",
+                "medicare",
+                "medicare prescription drug"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-d-spending-by-drug",
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
+                "https://data.cms.gov/resources/medicare-part-d-spending-by-drug-methodology"
+            ],
+            "temporal": "2022-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Part D Spending by Drug"
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
-            "@type": "dcat:Dataset",
-            "temporal": "1988/2020",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -58403,22 +58370,68 @@
                     "mediaType": "application/xml"
                 }
             ],
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Annual (R/P1Y)",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/dataset/aid-families-dependent-children-quality-control-review-panel-decisions-0",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Debbie Nobelman",
+                "hasEmail": "mailto:Debbie.Nobleman@hhs.gov"
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
+            "identifier": "094cdb8f-68b1-4634-aa79-b3ba578488b3",
             "issued": "2012-05-30",
-            "temporal": "1991-08-09T00:00:00-04:00/1996-09-16T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "acf",
                 "administrative",
@@ -58496,81 +58509,35 @@
                 "welfare",
                 "withold"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Debbie Nobelman",
-                "hasEmail": "mailto:Debbie.Nobleman@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/aid-families-dependent-children-quality-control-review-panel-decisions-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:102"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Departmental Appeals Board"
             },
-            "identifier": "094cdb8f-68b1-4634-aa79-b3ba578488b3",
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
-            "landingPage": "https://data.cdc.gov/d/jnru-aqxk",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-05-17",
-            "@type": "dcat:Dataset",
-            "temporal": "August 1, 2020 to June 30, 2022",
-            "modified": "2024-05-17",
-            "references": [
-                "Zviedrite N",
-                "Jahan F",
-                "Moreland S",
-                "Ahmed F",
-                "Uzicanin A. COVID-19\u2013Related School Closures",
-                "United States",
-                "July 27",
-                "2020\u2013June 30",
-                "2022. Emerg Infect Dis. 2024;30(1):58-69. https://doi.org/10.3201/eid3001.231215"
-            ],
-            "keyword": [
-                "community mitigation",
-                "covid-19",
-                "emergency preparedness",
-                "pandemic",
-                "pandemic preparedness",
-                "school closure"
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
-            "identifier": "https://data.cdc.gov/api/views/jnru-aqxk",
             "description": "Unplanned public K-12 school district and individual school closures due to COVID-19 in the United States from August 1, 2020\u2013June 30, 2022.",
-            "title": "COVID-19-related School Closures: USA, 2020-2022",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58593,21 +58560,67 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, 50 States and D.C.",
+            "identifier": "https://data.cdc.gov/api/views/jnru-aqxk",
+            "issued": "2024-05-17",
+            "keyword": [
+                "community mitigation",
+                "covid-19",
+                "emergency preparedness",
+                "pandemic",
+                "pandemic preparedness",
+                "school closure"
+            ],
+            "landingPage": "https://data.cdc.gov/d/jnru-aqxk",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-17",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "Zviedrite N",
+                "Jahan F",
+                "Moreland S",
+                "Ahmed F",
+                "Uzicanin A. COVID-19\u2013Related School Closures",
+                "United States",
+                "July 27",
+                "2020\u2013June 30",
+                "2022. Emerg Infect Dis. 2024;30(1):58-69. https://doi.org/10.3201/eid3001.231215"
+            ],
+            "spatial": "United States, 50 States and D.C.",
+            "temporal": "August 1, 2020 to June 30, 2022",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "COVID-19-related School Closures: USA, 2020-2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2008",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2008) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2008-nid13549",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2008-nid13549"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2008-nid13549",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -58620,58 +58633,29 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2008",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2008-nid13549",
-            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2008)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2008-nid13549",
-                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2008) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2008-nid13549"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2008)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/mesh/meshhome.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-12-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
-            "keyword": [
-                "mesh"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/m5y3-25uc",
             "description": "Listed below are MeSH Topical Qualifiers listed by Name, Abbreviation, and Short Form. Each Qualifier is defined by a Scope Note that provides guidance on how it should be used.",
-            "title": "MeSH Qualifiers with Scope Notes",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58694,46 +58678,38 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/m5y3-25uc",
+            "issued": "2022-12-19",
+            "keyword": [
+                "mesh"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/mesh/meshhome.html",
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
+            "title": "MeSH Qualifiers with Scope Notes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/puin-6ss7",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/puin-6ss7",
             "description": "NNDSS - TABLE 1W.  Meningococcal disease,  All serogroups to Meningococcal disease, Serogroup B - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58756,41 +58732,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/puin-6ss7",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/puin-6ss7",
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
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -58813,68 +58794,74 @@
                     "mediaType": "application/xml"
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
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2011-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://mimic.physionet.org/",
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
                 "fn": "PAI, VINAY MANJUNATH",
                 "hasEmail": "mailto:paiv@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "f4dd62fd-e5cb-4e95-a5b9-a3003f1ab7a6",
+            "dataQuality": true,
             "description": "<p>The objective of this Bioengineering Research Partnership is to focus the resources of a powerful interdisciplinary team from academia (MIT), industry (Philips Medical Systems) and clinical medicine (Beth Israel Deaconess Medical Center) to develop and evaluate advanced ICU patient monitoring systems that will substantially improve the efficiency, accuracy and timeliness of clinical decision making in intensive care.</p>",
-            "title": "Multiparameter Intelligent Monitoring in Intensive Care II (MIMIC-II)",
+            "identifier": "f4dd62fd-e5cb-4e95-a5b9-a3003f1ab7a6",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://mimic.physionet.org/",
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
+            "title": "Multiparameter Intelligent Monitoring in Intensive Care II (MIMIC-II)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dgwc-f5xf",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -58882,43 +58869,37 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dgwc-f5xf",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/dgwc-f5xf",
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
+            "title": "DPM OC, EC and FT-IR data (Quantifying elemental and organic carbon in diesel particulate matter by mid infrared spectrometry)."
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -58941,53 +58922,45 @@
                     "mediaType": "application/xml"
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
+            "title": "DQS NHANES Select Infectious Diseases Prevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-08-07",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2022-03-28",
-            "modified": "2023-07-12",
-            "keyword": [
-                "age",
-                "all causes",
-                "children",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
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
-            "identifier": "https://data.cdc.gov/api/views/3apk-4u4f",
             "description": "Effective June 28, 2023, this dataset will no longer be updated. Similar data are accessible from CDC WONDER (https://wonder.cdc.gov/mcd-icd10-provisional.html).\n\nCumulative deaths involving COVID-19 reported to NCHS by sex and age in years, in the United States.",
-            "title": "Provisional COVID-19 Death Counts by Age in Years, 2020-2023",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59010,46 +58983,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/3apk-4u4f",
+            "issued": "2020-08-07",
+            "keyword": [
+                "age",
+                "all causes",
+                "children",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
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
+            "temporal": "2020-01-01/2022-03-28",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 Death Counts by Age in Years, 2020-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/research/umls/rxnorm/",
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
-                "generic",
-                "health data standards",
-                "semantic",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/t84b-g5db",
             "description": "RxNorm provides normalized names for clinical drugs and links its names to many of the drug vocabularies commonly used in pharmacy management and drug interaction software, including those of First Databank, Micromedex, Gold Standard, and Multum. By providing links between these vocabularies, RxNorm can mediate messages between systems not using the same software and vocabulary.\n\nTechnical documentation at http://www.nlm.nih.gov/research/umls/rxnorm/docs/index.html",
-            "title": "RxNorm",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59076,53 +59054,53 @@
                     "title": "Query Interface (RxNav)"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/t84b-g5db",
+            "issued": "2012-08-22",
+            "keyword": [
+                "api",
+                "dataset",
+                "drugs",
+                "generic",
+                "health data standards",
+                "semantic",
+                "terminologies"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/research/umls/rxnorm/",
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
+            "title": "RxNorm"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revalidation-reassignment-list",
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
-                "provider enrollment",
-                "states & territories",
-                "zip code"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/20f51cff-4137-4f3a-b6b7-bfc9ad57983b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/revalidation-reassignments-list-data-dictionary",
             "description": "The Revalidation Reassignment List dataset provides information on reassignments of providers who are due for revalidation.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Revalidation Reassignment List",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/20f51cff-4137-4f3a-b6b7-bfc9ad57983b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/20f51cff-4137-4f3a-b6b7-bfc9ad57983b/data",
+                    "mediaType": "text/html",
                     "title": "Revalidation Reassignment List : 2025-01-01"
                 },
                 {
@@ -59402,48 +59380,50 @@
                     "title": "Revalidation Reassignment List : 2022-02-28"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/revalidation-reassignments-list-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/20f51cff-4137-4f3a-b6b7-bfc9ad57983b/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment",
+                "states & territories",
+                "zip code"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revalidation-reassignment-list",
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
+            "title": "Revalidation Reassignment List"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/STATESystem",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2019-02-27",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-22",
-            "keyword": [
-                "office on smoking and health",
-                "osh",
-                "qit",
-                "survey questions",
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
-            "identifier": "https://data.cdc.gov/api/views/vdgb-f9s3",
             "description": "1965, 1966, 1970, 1974-2015, 2017. Centers for Disease Control and Prevention (CDC). Office on Smoking and Health (OSH). Survey Questions (Tobacco Use). The QIT is a compilation of more than 7,000 historical tobacco-related survey questions from various state, national and international surveys.",
-            "title": "Question Inventory on Tobacco (QIT)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59466,46 +59446,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vdgb-f9s3",
+            "issued": "2019-02-27",
+            "keyword": [
+                "office on smoking and health",
+                "osh",
+                "qit",
+                "survey questions",
+                "tobacco"
+            ],
+            "landingPage": "http://www.cdc.gov/STATESystem",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-22",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Survey Questions (Tobacco Use)"
-            ]
+            ],
+            "title": "Question Inventory on Tobacco (QIT)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pjtk-n43k",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/pjtk-n43k",
             "description": "NNDSS - TABLE 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease  \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59528,47 +59504,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/pjtk-n43k",
+            "issued": "2020-01-17",
+            "keyword": [
+                "2020",
+                "arboviral diseases",
+                "jamestown canyon virus disease",
+                "la crosse virus disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "powassan virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/pjtk-n43k",
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
+            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-newly-enrolled",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/619a72e4-07cc-414e-95d6-058e3c10557a/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Newly Enrolled tables provide data on characteristics of the newly enrolled Medicare population.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR ENROLL AB 21. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Enrollees, Yearly Trend\n\tMDCR ENROLL AB 22. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total Enrollees by Month of Enrollment, Yearly Trend\n\tMDCR ENROLL AB 23. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 24. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Enrollees, by Area of Residence\n\tMDCR ENROLL AB 25. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Original Medicare Enrollees\n\tMDCR ENROLL AB 26. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Original Medicare Enrollees by Month of Enrollment, Yearly Trend\n\tMDCR ENROLL AB 27. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Original Medicare Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 28. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Original Medicare Enrollees, by Area of Residence\n\tMDCR ENROLL AB 29. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Medicare Advantage and Other Health Plan Enrollees, Yearly Trend\n\tMDCR ENROLL AB 30. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Medicare Advantage and Other Health Plan Enrollees, by Month of Enrollment, Yearly Trend\n\tMDCR ENROLL AB 31. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Medicare Advantage and Other Health Plan Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 32. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Medicare Advantage and Other Health Plan Enrollees, by Area of Residence",
-            "title": "CMS Program Statistics - Medicare Newly Enrolled",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59625,54 +59603,51 @@
                     "title": "CMS Program Statistics - Medicare Newly Enrolled : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/619a72e4-07cc-414e-95d6-058e3c10557a/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-newly-enrolled",
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
+            "title": "CMS Program Statistics - Medicare Newly Enrolled"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hwk8-wu83",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13/2023-10-14",
-            "modified": "2023-10-14",
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
-            "identifier": "https://data.cdc.gov/api/views/hwk8-wu83",
             "description": "This site provides historical data beginning June 14, 2023, for the visualization presented on <a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccinations\">COVID-19 Data Tracker\u2019s \u201cVaccinations in the United States\" </a> site titled \u201cUS COVID-19 Vaccine Doses Delivered by Vaccine Type\u201d\n\n<b>Definition for Distributed: </b>\nCumulative number of COVID-19 updated vaccine doses distributed in the United States.\nCDC is no longer reporting metrics for Johnson & Johnson, and the original Pfizer and Moderna vaccines.\n\nData represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.",
-            "title": "COVID-19 Updated Vaccines Distributed",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59695,81 +59670,93 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/hwk8-wu83",
+            "issued": "2023-06-26",
+            "keyword": [
+                "administration",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "report date",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hwk8-wu83",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1D",
+            "modified": "2023-10-14",
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
+            "temporal": "2020-12-13/2023-10-14",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "COVID-19 Updated Vaccines Distributed"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/e6pu-b7n6",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-16",
-            "@type": "dcat:Dataset",
-            "modified": "2021-12-15",
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
-            "identifier": "0563d88c-8fe5-42a8-9d69-f67fd21c0e91",
             "description": "This table presents the rate of neonatal abstinence syndrome per 1,000 newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019.\r\n\r\nSome states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Data from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Values for Maryland were excluded due to unusuable diagnosis codes in the IP file and the OT file in 2017. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2019.  In addition, states with a high data quality concern on one or more measures are noted in the table with an asterisk (*). \r\n\r\nPlease refer to the DQ Atlas for more information about data quality assessment methods.",
-            "title": "Rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/rate-of-nas-per-thous-in-newborns-2017-to-2019.csv",
-                    "description": "This table presents the rate of neonatal abstinence syndrome per 1,000 newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019.\n\nSome states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Data from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Values for Maryland were excluded due to unusuable diagnosis codes in the IP file and the OT file in 2017. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2019.  In addition, states with a high data quality concern on one or more measures are noted in the table with an asterisk (*). \n\nPlease refer to the DQ Atlas for more information about data quality assessment methods.",
                     "@type": "dcat:Distribution",
+                    "description": "This table presents the rate of neonatal abstinence syndrome per 1,000 newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019.\n\nSome states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Data from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Values for Maryland were excluded due to unusuable diagnosis codes in the IP file and the OT file in 2017. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2019.  In addition, states with a high data quality concern on one or more measures are noted in the table with an asterisk (*). \n\nPlease refer to the DQ Atlas for more information about data quality assessment methods.",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/rate-of-nas-per-thous-in-newborns-2017-to-2019.csv",
+                    "mediaType": "text/csv",
                     "title": "Rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019"
                 }
             ],
+            "identifier": "0563d88c-8fe5-42a8-9d69-f67fd21c0e91",
+            "issued": "2021-12-16",
+            "keyword": [
+                "chip",
+                "medicaid",
+                "neonatal abstinence syndrome"
+            ],
+            "landingPage": "https://healthdata.gov/d/e6pu-b7n6",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2021-12-15",
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
+            "title": "Rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/8ggw-jwph",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -59777,42 +59764,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/8ggw-jwph",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/8ggw-jwph",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "theme": [
-                "National Institute for Occupational Safety and Health"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/e6y3-2bid",
-            "bureauCode": [
-                "009:00"
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
             ],
-            "issued": "2022-08-10",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ],
+            "title": "Examination of the exposome in an animal model: the impact of high fat diet and rat strain on local and systemic immune markers following occupational welding fume exposure"
+        },
+        {
             "@type": "dcat:Dataset",
-            "modified": "2022-08-17",
-            "keyword": [
-                "individual",
-                "individual market medical",
-                "py2022",
-                "qhp",
-                "qhp landscape"
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "009:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Center for Consumer Information and Insurance Oversight",
                 "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Center for Consumer Information and Insurance Oversight"
-            },
-            "identifier": "fb97ce4a-5e5b-4e18-bab8-27299e56d5cf",
             "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2022 Individual Medical",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59820,38 +59801,39 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "fb97ce4a-5e5b-4e18-bab8-27299e56d5cf",
+            "issued": "2022-08-10",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2022",
+                "qhp",
+                "qhp landscape"
+            ],
+            "landingPage": "https://healthdata.gov/d/e6y3-2bid",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2022 Individual Medical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/e6z4-xemc",
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
-                "network",
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
-            "identifier": "0953b9c0-0843-4f41-88e9-cc44aed14407",
             "description": "The Network PUF (Ntwrk-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Ntwrk-PUF contains issuer-level data identifying provider network URLs.",
-            "title": "Network PUF - PY2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59859,90 +59841,85 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "0953b9c0-0843-4f41-88e9-cc44aed14407",
+            "issued": "2022-08-10",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "network",
+                "py2022"
+            ],
+            "landingPage": "https://healthdata.gov/d/e6z4-xemc",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Network PUF - PY2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/e8eg-9rei",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-08-31",
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
-            "identifier": "9f53c963-b4c3-581e-ae56-4067452ea599",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_measureSearchInfo",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measureSearchInfo.csv",
-                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measureSearchInfo.csv",
+                    "mediaType": "text/csv",
                     "title": "measureSearchInfo csv file"
                 }
             ],
+            "identifier": "9f53c963-b4c3-581e-ae56-4067452ea599",
+            "issued": "2022-08-31",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/e8eg-9rei",
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
+            "title": "prodAuto_measureSearchInfo"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2qxe-cmv4",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/2qxe-cmv4",
             "description": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Please refer to the CDC WONDER publication for weekly updates to the footnote for this condition.",
-            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59965,52 +59942,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2qxe-cmv4",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "hepatitis c",
+                "influenza-associated pediatric mortality",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/2qxe-cmv4",
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
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5i5k-6cmh",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-08-11",
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
-            "identifier": "https://data.cdc.gov/api/views/5i5k-6cmh",
             "description": "This site provides data for select demographic characteristics (age, sex, and age by sex) of people receiving COVID-19 vaccinations in the United States at the national and jurisdictional levels. For national race/ethnicity data, please visit <a href=\"https://data.cdc.gov/Vaccinations/COVID-19-Vaccination-Demographics-in-the-United-St/km4m-vcsb\">COVID-19 Vaccination Demographics in the United States,National</a>. For jurisdictional race/ethnicity data, please visit the relevant health department website if available.\n \nData represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u202f",
-            "title": "COVID-19 Vaccination Age and Sex Trends in the United States, National and Jurisdictional",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60033,58 +60004,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/5i5k-6cmh",
+            "issued": "2022-08-11",
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
+            "landingPage": "https://data.cdc.gov/d/5i5k-6cmh",
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
+            "title": "COVID-19 Vaccination Age and Sex Trends in the United States, National and Jurisdictional"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-09-02",
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
-            "identifier": "https://data.cdc.gov/api/views/4va6-ph5s",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19, influenza, and pneumonia reported to NCHS by jurisdiction of occurrence, place of death, and age group.",
-            "title": "Provisional COVID-19 Deaths by Place of Death and Age",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60107,43 +60074,58 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/4va6-ph5s",
+            "issued": "2020-09-02",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
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
+            "title": "Provisional COVID-19 Deaths by Place of Death and Age"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -60166,51 +60148,44 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
             "theme": [
                 "Foodborne",
                 "Waterborne",
                 "and Related Diseases"
-            ]
+            ],
+            "title": "BEAM Dashboard \u2013 Top 30 Most Common Serotypes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qz3x-mf9n",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-02-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-23",
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
-            "identifier": "https://data.cdc.gov/api/views/qz3x-mf9n",
             "description": "State, territorial, and county executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when individuals in states, territories, and counties were subject to executive orders, administrative orders, resolutions, and proclamations for COVID-19 that require or recommend people stay in their homes.\n\nThese data are derived from the publicly available state, territorial, and county executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly require or recommend individuals stay at home found by the CDC, COVID-19 Community Intervention and At-Risk Task Force, Monitoring and Evaluation Team & CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 15 through May 5, 2020. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. These data do not include mandatory business closures, curfews, or limitations on public or private gatherings. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State, Territorial, and County Stay-At-Home Orders: March 15-May 5 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60233,41 +60208,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qz3x-mf9n",
+            "issued": "2021-02-10",
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
+            "landingPage": "https://data.cdc.gov/d/qz3x-mf9n",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-07-23",
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
+            "title": "U.S. State, Territorial, and County Stay-At-Home Orders: March 15-May 5 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://wwwn.cdc.gov/NHISDataQueryTool/ER_Biannual/index_biannual.html",
+            "accrualPeriodicity": "R/P6M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-07-07",
-            "temporal": "2019/2021",
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
-            "identifier": "https://data.cdc.gov/api/views/trpk-sp8z",
             "description": "Interactive Biannual Early Release Estimates provide health statistics based on data from the 2019-2021 National Health Interview Survey (NHIS) for selected health topics for adults aged 18 years and over. All estimates are unadjusted percentages based on preliminary data files and are released prior to final data editing and final weighting to provide access to the most recent information from the NHIS. Estimates can be grouped by demographic characteristics (such as age, race and Hispanic origin, or sex). Estimates based on 2019-2020 NHIS quarterly data are available in Interactive Quarterly Early Release Estimates. Estimates based on the 1997\u20132018 NHIS can be found in Previous Early Release Reports on Key Health Indicators.",
-            "title": "NHIS Interactive Biannual Early Release Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60290,36 +60272,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/trpk-sp8z",
+            "issued": "2021-07-07",
+            "keyword": [
+                "early release",
+                "key health indicators",
+                "nhis"
+            ],
+            "landingPage": "https://wwwn.cdc.gov/NHISDataQueryTool/ER_Biannual/index_biannual.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P6M",
+            "modified": "2024-12-09",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2019/2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NHIS Interactive Biannual Early Release Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:00"
             ],
-            "landingPage": "https://data.cdc.gov/d/tug7-57z5",
-            "issued": "2024-08-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-29",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Phong Le",
                 "hasEmail": "mailto:pyv8@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/tug7-57z5",
             "description": "This data is what is visualized in the HHS DRIVE dashboard.",
-            "title": "HHS DRIVE",
-            "programCode": [
-                "009:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60342,36 +60329,32 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/tug7-57z5",
+            "issued": "2024-08-29",
+            "landingPage": "https://data.cdc.gov/d/tug7-57z5",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-08-29",
+            "programCode": [
+                "009:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "HHS DRIVE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/vp2h-kf33",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vp2h-kf33",
             "description": "Health Services and Sciences Research Resources (HSRR) provides information about research datasets and instruments/indices employed in Health Services Research, Behavioral and Social Sciences and Public Health.\n\nThis resource was retired on September 14, 2021 and is no longer updated.",
-            "title": "Health Services and Sciences Research Resources (HSRR)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60394,35 +60377,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vp2h-kf33",
+            "issued": "2021-09-14",
+            "keyword": [
+                "health services research",
+                "public health"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/vp2h-kf33",
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
+            "title": "Health Services and Sciences Research Resources (HSRR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3m2r-fh4s",
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
-            "identifier": "https://data.cdc.gov/api/views/3m2r-fh4s",
             "description": ": This dataset contains all vaccine mandate prohibitions that were issued as of ____, by 50 states, 5 territories, and the District of Columbia regardless of whether the law has been superseded by a subsequent law, postponed by subsequent law, or otherwise modified. State and territorial laws are collected from publicly available government websites and cataloged and coded in HHS Protect by one coder with one or more additional coders conducting quality assurance. \nData were collected to determine when certain groups were prohibited from issuing vaccine mandates and to what groups those prohibitions applied. Data can be used to determine when states announced and began prohibiting for different groups from being required to be vaccinated. \nThese data are derived from publicly available state and territorial laws and official policy documents found by the CDC, COVID-19 Mitigation Policy Analysis Unit, and the CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 1, 2020 through _____. These data will be updated as new laws are collected. Any orders not available through publicly accessible websites are not included in this dataset. Recommendations not included in a law are not included in these data. Effective and expiration dates were coded using only the date provided in the law. These data do not necessarily represent the official position of the Centers for Disease Control and Prevention.",
-            "title": "State-Level Restrictions on Vaccine Mandates \u2013 All",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60445,36 +60432,36 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3m2r-fh4s",
+            "issued": "2022-03-23",
+            "landingPage": "https://data.cdc.gov/d/3m2r-fh4s",
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
+            "title": "State-Level Restrictions on Vaccine Mandates \u2013 All"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -60497,21 +60484,45 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cdc.gov/d/g9dy-mhts",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "description": "Explore the Youth and Tobacco Use Infographic which outlines key facts related to tobacco use among youth.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/g9dy-mhts/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/g9dy-mhts",
             "issued": "2016-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
             "keyword": [
                 "cessation",
                 "cigarette",
@@ -60536,64 +60547,34 @@
                 "tobacco use",
                 "youth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/g9dy-mhts",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-07-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/g9dy-mhts",
-            "description": "Explore the Youth and Tobacco Use Infographic which outlines key facts related to tobacco use among youth.",
-            "title": "Youth And Tobacco Use Infographic",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/g9dy-mhts/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "Youth And Tobacco Use Infographic"
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
-                "adult",
-                "gats",
-                "gtss",
-                "osh",
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
-            "identifier": "https://data.cdc.gov/api/views/4xf6-nrwk",
+            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Adu/4xf6-nrwk",
             "description": "2008-2017. Centers for Disease Control and Prevention (CDC).   Office on Smoking and Health (OSH) \u2013 Global Tobacco Surveillance System (GTSS) - Global Adult Tobacco Survey (GATS).    The Global Adult Tobacco Survey (GATS) is the global standard to systematically monitor adult tobacco use and track key tobacco control indicators. GATS is a nationally representative household survey of adults 15 years of age or older, using a standard protocol. It is intended to generate comparable data within and across countries. GATS enhances countries' capacity to design, implement and evaluate tobacco control interventions.",
-            "title": "Global Tobacco Surveillance System (GTSS) - Global Adult Tobacco Survey (GATS)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60616,99 +60597,144 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Adu/4xf6-nrwk",
+            "identifier": "https://data.cdc.gov/api/views/4xf6-nrwk",
+            "issued": "2025-01-31",
+            "keyword": [
+                "adult",
+                "gats",
+                "gtss",
+                "osh",
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
+            "title": "Global Tobacco Surveillance System (GTSS) - Global Adult Tobacco Survey (GATS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/taxonomy",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "biology",
-                "classification",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nmc6-m47x",
             "description": "The Taxonomy Database is a curated classification and nomenclature for all of the organisms in the public sequence databases. This currently represents about 10% of the described species of life on the planet.",
-            "title": "Taxonomy",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Root",
-                    "description": "Search the taxonomy tree using partial taxonomic names, common names, wild cards and phonetically similar names.",
                     "@type": "dcat:Distribution",
+                    "description": "Search the taxonomy tree using partial taxonomic names, common names, wild cards and phonetically similar names.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Root",
+                    "mediaType": "text/html",
                     "title": "Taxonomy Browser - Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/CommonTree/wwwcmt.cgi",
-                    "description": "Generates a taxonomic tree for a selected group of organisms. Users can upload a file of taxonomy IDs or names, or they can enter names or IDs directly.",
                     "@type": "dcat:Distribution",
+                    "description": "Generates a taxonomic tree for a selected group of organisms. Users can upload a file of taxonomy IDs or names, or they can enter names or IDs directly.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/CommonTree/wwwcmt.cgi",
+                    "mediaType": "text/html",
                     "title": "Taxonomy Common Tree"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=STATISTICS&uncultured=hide&unspecified=hide",
-                    "description": "Displays the number of taxonomic nodes in the database for a given rank and date of inclusion.",
                     "@type": "dcat:Distribution",
+                    "description": "Displays the number of taxonomic nodes in the database for a given rank and date of inclusion.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=STATISTICS&uncultured=hide&unspecified=hide",
+                    "mediaType": "text/html",
                     "title": "Taxonomy Statistics - Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/TaxIdentifier/tax_identifier.cgi",
-                    "description": "Displays the current status of a set of taxonomic nodes or IDs.",
                     "@type": "dcat:Distribution",
+                    "description": "Displays the current status of a set of taxonomic nodes or IDs.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/TaxIdentifier/tax_identifier.cgi",
+                    "mediaType": "text/html",
                     "title": "Taxonomy Status Reports"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=cgencodes",
-                    "description": "Currently, genetic codes can be set independently for nucleus, mitochondria, plastids and hydrogenosomes. The current settings for each of these on the taxonomic tree can be viewed with this following code list.",
                     "@type": "dcat:Distribution",
+                    "description": "Currently, genetic codes can be set independently for nucleus, mitochondria, plastids and hydrogenosomes. The current settings for each of these on the taxonomic tree can be viewed with this following code list.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=cgencodes",
+                    "mediaType": "text/html",
                     "title": "Genetic Codes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=extinct",
-                    "description": "Extinct organisms that are represented with sequence data at GenBank",
                     "@type": "dcat:Distribution",
+                    "description": "Extinct organisms that are represented with sequence data at GenBank",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=extinct",
+                    "mediaType": "text/html",
                     "title": "Extinct Organisms"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nmc6-m47x",
+            "issued": "2021-08-26",
+            "keyword": [
+                "biology",
+                "classification",
+                "dataset"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/taxonomy",
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
+            "title": "Taxonomy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "description": "1991-2016. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  Funding Data, Appropriations (1991-2016) and Expenditures (2008-2016).  Appropriations data show public funds allocated to/by a particular state for tobacco prevention and control.  They are not necessarily expended.  Appropriations are from four major funding sources, Federal, state, Robert Wood Johnson Foundation (RWJF), and the American Legacy Foundation (Legacy).  Expenditures are amounts spent by state tobacco control programs on tobacco prevention and control.  Expenditure data are available by CDC Best Practices Program Components (State and Community Interventions, Health Communication Interventions, Cessation Interventions, Surveillance and Evaluation, and Administration and Management). Expenditures from 2008 to 2014 are compared against 2007 CDC Best Practices Recommendations; expenditures from 2015 and forward are compared against 2014 CDC Best Practices Recommendations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/vw7y-v3uk",
             "issued": "2023-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
             "keyword": [
                 "administration and management",
                 "allocation",
@@ -60735,140 +60761,91 @@
                 "surveillance and evaluation",
                 "tobacco"
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
-            "identifier": "https://data.cdc.gov/api/views/vw7y-v3uk",
-            "description": "1991-2016. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  Funding Data, Appropriations (1991-2016) and Expenditures (2008-2016).  Appropriations data show public funds allocated to/by a particular state for tobacco prevention and control.  They are not necessarily expended.  Appropriations are from four major funding sources, Federal, state, Robert Wood Johnson Foundation (RWJF), and the American Legacy Foundation (Legacy).  Expenditures are amounts spent by state tobacco control programs on tobacco prevention and control.  Expenditure data are available by CDC Best Practices Program Components (State and Community Interventions, Health Communication Interventions, Cessation Interventions, Surveillance and Evaluation, and Administration and Management). Expenditures from 2008 to 2014 are compared against 2007 CDC Best Practices Recommendations; expenditures from 2015 and forward are compared against 2014 CDC Best Practices Recommendations.",
-            "title": "University of Illinois at Chicago Health Policy Center - Funding",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-25",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
             "theme": [
                 "Funding"
-            ]
+            ],
+            "title": "University of Illinois at Chicago Health Policy Center - Funding"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ege4-wxz9",
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
-            "identifier": "c21bff91-35f5-5333-9bf5-ffd895d96c6a",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_states_measures",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures.csv",
-                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures.csv",
+                    "mediaType": "text/csv",
                     "title": "states_measures csv file"
                 }
             ],
+            "identifier": "c21bff91-35f5-5333-9bf5-ffd895d96c6a",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/ege4-wxz9",
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
+            "title": "devAuto_states_measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-compliance/cost-report/hospital-provider-cost-report",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2011-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-23",
-            "references": [
-                "https://data.cms.gov/resources/hospital-provider-cost-report-methodology"
-            ],
-            "keyword": [
-                "financials",
-                "health care use & payments",
-                "hospitals & facilities",
-                "inpatient",
-                "medicare",
-                "original medicare",
-                "value-based care"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/44060663-47d8-4ced-a115-b53b4c270acb/data-viewer",
-            "description": "The Hospital Provider Cost Report\u00a0dataset provides select measures from the hospital annual cost report. This data\u00a0includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.",
-            "title": "Hospital Provider Cost Report",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-03/9756088d-5280-4090-80b9-449d31ef25a3/Cost%20Report%20Data%20Dictionary%20Update.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Hospital Provider Cost Report\u00a0dataset provides select measures from the hospital annual cost report. This data\u00a0includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/44060663-47d8-4ced-a115-b53b4c270acb/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/44060663-47d8-4ced-a115-b53b4c270acb/data",
+                    "mediaType": "text/html",
                     "title": "Hospital Provider Cost Report : 2022-12-01"
                 },
                 {
@@ -61016,53 +60993,51 @@
                     "title": "Hospital Provider Cost Report : 2011-12-02"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-03/9756088d-5280-4090-80b9-449d31ef25a3/Cost%20Report%20Data%20Dictionary%20Update.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/44060663-47d8-4ced-a115-b53b4c270acb/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "financials",
+                "health care use & payments",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "original medicare",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/provider-compliance/cost-report/hospital-provider-cost-report",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-23",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/hospital-provider-cost-report-methodology"
+            ],
+            "temporal": "2011-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Hospital Provider Cost Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/y4x9-2nqn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
-                "acute",
-                "by type) a",
-                "by type) b",
-                "hemolytic uremic syndrome post-diarrheal",
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
-            "identifier": "https://data.cdc.gov/api/views/y4x9-2nqn",
             "description": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61085,35 +61060,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y4x9-2nqn",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "acute",
+                "by type) a",
+                "by type) b",
+                "hemolytic uremic syndrome post-diarrheal",
+                "hepatitis (viral",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/y4x9-2nqn",
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
+            "title": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/6wqg-8ykc",
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
-            "identifier": "https://data.cdc.gov/api/views/6wqg-8ykc",
             "description": "In August 2020 there were over 186,000 employees in the oil and gas extraction industry in the United States (United States Department of Labor. Bureau of Labor Statistics, 2020).  Many workers in the upstream oil extraction industry have potential risk of crude oil vapor (COV) inhalation.  There are many current knowledge gaps regarding the health effects from inhalation of complex mixtures found in crude oil vapors.  To aid research in filling these gaps, an automated system that could carefully deliver and control the COV concentration within an animal inhalation exposure chamber was needed.  The objective of this project was to develop an automated computer-controlled system to expose small laboratory animals to precise concentrations of crude oil vapor (COV).",
-            "title": "Automated oil vapor inhalation exposure system",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61121,46 +61108,37 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/6wqg-8ykc",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/6wqg-8ykc",
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
+            "title": "Automated oil vapor inhalation exposure system"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/ri74-jp8e",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-08",
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
-            "identifier": "https://data.cdc.gov/api/views/ri74-jp8e",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 2 is the second round of a three-round survey. In addition to the probability sample of RANDS during COVID-19 Round 2, the questionnaire was administered to the Dynata non-probability online opt-in sample by NORC at the University of Chicago (NORC) from August 3, 2020 to August 20, 2020.  The RANDS during COVID-19 Round 2 Non-Probability Sample does not have a known survey sampling design and cannot be used to produce nationally or sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 2 during COVID-19 non-probability sampled Restricted File",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_2_np_technical_documentation.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 2 is the second round of a three-round survey. In addition to the probability sample of RANDS during COVID-19 Round 2, the questionnaire was administered to the Dynata non-probability online opt-in sample by NORC at the University of Chicago (NORC) from August 3, 2020 to August 20, 2020.  The RANDS during COVID-19 Round 2 Non-Probability Sample does not have a known survey sampling design and cannot be used to produce nationally or sub-nationally representative estimates.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61168,37 +61146,47 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_2_np_technical_documentation.pdf",
+            "identifier": "https://data.cdc.gov/api/views/ri74-jp8e",
+            "issued": "2022-06-08",
+            "keyword": [
+                "anxiety",
+                "covid-19",
+                "depression",
+                "missed healthcare",
+                "research-data-center",
+                "telemedicine"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ri74-jp8e",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "theme": [
-                "NCHS"
-            ]
-        },
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
+            "theme": [
+                "NCHS"
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 2 during COVID-19 non-probability sampled Restricted File"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/healthyyouth/data/yrbs/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-22",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DASH Public Inquiries",
                 "hasEmail": "mailto:nccddashinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/svam-8dhg",
+            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/svam-8dhg",
             "description": "1991-2017. High School Dataset. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors \r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and \r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human \r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors \r\nthe prevalence of obesity and asthma and other priority health behaviors.",
-            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School - Excluding Sexual Identity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61221,47 +61209,35 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/svam-8dhg",
+            "identifier": "https://data.cdc.gov/api/views/svam-8dhg",
+            "issued": "2023-07-19",
+            "landingPage": "https://www.cdc.gov/healthyyouth/data/yrbs/index.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-08-22",
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
+            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School - Excluding Sexual Identity"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -61284,21 +61260,57 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.hrsa.gov/tools/medicare/physician-bonus",
             "bureauCode": [
                 "009:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HRSA Bureau of Health Workforce",
+                "hasEmail": "mailto:data@hrsa.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The HPSAs Eligible for the Medicare Physician Bonus Payment advisor tools allows the user (physician) to determine if an address is eligible for bonus payments. Medicare makes bonus payments to physicians who provide medical care services in geographic areas that are HRSA-designated as primary medical care Health Professional Shortage Areas (HPSAs) and to psychiatrists who provide services in HRSA-designated mental health HPSAs.</p>\n<p>The search results indicate if the address is in a Primary Care HPSA or Mental Health HPSA, along with state, county name, Census Tract, zip code, and a map identifying the address.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://datawarehouse.hrsa.gov/geoHPSAAdvisor/GeographicHPSAAdvisor.aspx",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "5d9629e2-beac-4b50-bcc6-1d929e47fc36",
             "issued": "2012-05-30",
-            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "census tract number",
                 "community health",
@@ -61315,70 +61327,42 @@
                 "poverty",
                 "primary care hpsa"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HRSA Bureau of Health Workforce",
-                "hasEmail": "mailto:data@hrsa.gov"
-            },
+            "landingPage": "https://data.hrsa.gov/tools/medicare/physician-bonus",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:078"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Health Resources and Services Administration"
             },
-            "identifier": "5d9629e2-beac-4b50-bcc6-1d929e47fc36",
-            "description": "<p>The HPSAs Eligible for the Medicare Physician Bonus Payment advisor tools allows the user (physician) to determine if an address is eligible for bonus payments. Medicare makes bonus payments to physicians who provide medical care services in geographic areas that are HRSA-designated as primary medical care Health Professional Shortage Areas (HPSAs) and to psychiatrists who provide services in HRSA-designated mental health HPSAs.</p>\n<p>The search results indicate if the address is in a Primary Care HPSA or Mental Health HPSA, along with state, county name, Census Tract, zip code, and a map identifying the address.</p>",
-            "title": "Find Shortage Areas: HPSAs Eligible for the Medicare Physician Bonus Payment",
-            "programCode": [
-                "009:078"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://datawarehouse.hrsa.gov/geoHPSAAdvisor/GeographicHPSAAdvisor.aspx",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health",
                 "Medicare"
-            ]
+            ],
+            "title": "Find Shortage Areas: HPSAs Eligible for the Medicare Physician Bonus Payment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/xajj-cnsu",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-18",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xajj-cnsu",
             "description": "Hazardous Substances Data Bank (HSDB) was a toxicology database that focused on the toxicology of potentially hazardous chemicals. It provided information on human exposure, industrial hygiene, emergency handling procedures, environmental fate, regulatory requirements, nanomaterials, and related areas. The information in HSDB has been assessed by a Scientific Review Panel.\n\nThis version of HSDB data includes a subset of HSDB for downloading, but is no longer updated. HSDB data has been incorporated into PubChem.",
-            "title": "Hazardous Substances Data Bank (HSDB)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/hsdblease/",
-                    "description": "Download over 5,000 hazardous substance records from HSDB.",
                     "@type": "dcat:Distribution",
+                    "description": "Download over 5,000 hazardous substance records from HSDB.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/hsdblease/",
+                    "mediaType": "text/html",
                     "title": "Download HSDB Data"
                 },
                 {
@@ -61394,49 +61378,39 @@
                     "title": "HSDB Data Element Guide"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xajj-cnsu",
+            "issued": "2020-09-18",
+            "keyword": [
+                "data distribution"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/xajj-cnsu",
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
+            "title": "Hazardous Substances Data Bank (HSDB)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -61459,40 +61433,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/e2d5-ggg7",
+            "issued": "2023-03-10",
+            "keyword": [
+                "age",
+                "age group",
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/d/eikg-657m",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-12",
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
-            "identifier": "648ac749-46d9-45bf-aa68-141c7d4dea45",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-04-2024-to-11-10-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61500,17 +61484,46 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "648ac749-46d9-45bf-aa68-141c7d4dea45",
+            "issued": "2024-11-13",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/eikg-657m",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-12",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-04-2024-to-11-10-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2003",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2003) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2003-nid13575",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2003-nid13575"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2003-nid13575",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -61523,64 +61536,29 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2003",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2003-nid13575",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2003)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2003-nid13575",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2003) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2003-nid13575"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2003)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/e92c-t3mi",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
-            "keyword": [
-                "bars",
-                "fact sheet",
-                "infographic",
-                "restaurants",
-                "secondhand smoke",
-                "smokefree",
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
-            "identifier": "https://data.cdc.gov/api/views/e92c-t3mi",
             "description": "Explore the Going Smokefree Matters \u2013 Bars and Restaurants Infographic which outlines key facts related to the effects of secondhand smoke exposure in bars and restaurants.",
-            "title": "Going Smokefree Matters - Bars and Restaurants Infographic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61588,45 +61566,44 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/e92c-t3mi",
+            "issued": "2016-03-01",
+            "keyword": [
+                "bars",
+                "fact sheet",
+                "infographic",
+                "restaurants",
+                "secondhand smoke",
+                "smokefree",
+                "state system"
+            ],
+            "landingPage": "https://data.cdc.gov/d/e92c-t3mi",
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
+            "title": "Going Smokefree Matters - Bars and Restaurants Infographic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mi28-ze7h",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/mi28-ze7h",
             "description": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61649,38 +61626,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mi28-ze7h",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "animal",
+                "human",
+                "nedss",
+                "netss",
+                "nndss",
+                "rabies",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mi28-ze7h",
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
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ekm7-cmu8",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-28",
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
-            "identifier": "0919b0f0-267b-4418-a585-6d3fb7e60658",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-20-to-2023-02-26",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61689,40 +61674,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-20-to-2023-02-26"
                 }
             ],
+            "identifier": "0919b0f0-267b-4418-a585-6d3fb7e60658",
+            "issued": "2023-03-01",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/ekm7-cmu8",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-02-28",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-20-to-2023-02-26"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/em69-hj4k",
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
-            "identifier": "aa2cf0c7-ff39-484a-9472-764e243ffea9",
             "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2023 Medical SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61730,50 +61711,39 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "aa2cf0c7-ff39-484a-9472-764e243ffea9",
+            "issued": "2023-08-09",
+            "keyword": [
+                "py2023",
+                "qhp",
+                "qhp landscape",
+                "shop",
+                "shop market medical"
+            ],
+            "landingPage": "https://healthdata.gov/d/em69-hj4k",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2023 Medical SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-02-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-30",
-            "keyword": [
-                "age",
-                "age group",
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
-            "identifier": "https://data.cdc.gov/api/views/4ueh-89p9",
             "description": "Deaths by educational attainment, race, sex, and age group for deaths occurring in the United States. Data are final for 2019 and provisional for 2020.  The dataset includes annual counts of death for total deaths and for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
-            "title": "AH Deaths by Educational Attainment, 2019-2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61796,22 +61766,65 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/4ueh-89p9",
+            "issued": "2021-02-24",
+            "keyword": [
+                "age",
+                "age group",
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
+                "sex",
+                "united states",
+                "yearly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-03-30",
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
+            "title": "AH Deaths by Educational Attainment, 2019-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2002",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2002) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2002-nid13566",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2002-nid13566"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2002-nid13566",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -61824,73 +61837,38 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2002",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2002-nid13566",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2002)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2002-nid13566",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2002) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2002-nid13566"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2002)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/number-of-accountable-care-organization-assigned-beneficiaries-by-county",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2016-01-01/2023-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-21",
-            "references": [
-                "https://data.cms.gov/resources/number-of-accountable-care-organization-assigned-beneficiaries-by-county-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/ae8c9418-acc9-4442-b217-33291448f6b8/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/number-of-accountable-care-organization-assigned-beneficiaries-by-county-data-dictionary-2023",
             "description": "The Shared Savings Program Number of Accountable Care Organization Assigned Beneficiaries by County dataset provides aggregate data of total assigned beneficiaries by Shared Savings Program ACO for each county where at least one of their assigned beneficiaries resides. Assigned beneficiary person-year counts are based on certified Shared Savings Program ACO Participant Lists and assignment methodology for that performance year.\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to Shared Savings Program ACO information occur periodically. Each Shared Savings Program ACO has the most up-to-date information about their organization. Consider contacting the Shared Savings Program ACO for the latest information. Contact information is available in the ACO Public Use File (PUF) and the ACO Participants PUF.",
-            "title": "Number of Accountable Care Organization Assigned Beneficiaries by County",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ae8c9418-acc9-4442-b217-33291448f6b8/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ae8c9418-acc9-4442-b217-33291448f6b8/data",
+                    "mediaType": "text/html",
                     "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2023-12-31"
                 },
                 {
@@ -62002,99 +61980,98 @@
                     "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2016-01-15"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/number-of-accountable-care-organization-assigned-beneficiaries-by-county-data-dictionary-2023",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/ae8c9418-acc9-4442-b217-33291448f6b8/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/number-of-accountable-care-organization-assigned-beneficiaries-by-county",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/number-of-accountable-care-organization-assigned-beneficiaries-by-county-methodology"
+            ],
+            "temporal": "2016-01-01/2023-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Accountable Care Organization Assigned Beneficiaries by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/enbs-qir9",
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
-            "identifier": "b087ed0a-861b-5562-aac7-239348af8c82",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard VERSION v0.3.58-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/VERSION.csv",
-                    "description": "Scorecard VERSION v0.3.58-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard VERSION v0.3.58-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/VERSION.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard VERSION v0.3.58-test (local)"
                 }
             ],
+            "identifier": "b087ed0a-861b-5562-aac7-239348af8c82",
+            "issued": "2023-08-10",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/enbs-qir9",
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
+            "title": "Scorecard VERSION v0.3.58-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/brfss/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-19",
-            "references": [
-                "http://www.cdc.gov/brfss"
-            ],
-            "keyword": [
-                "...",
-                "behavioral",
-                "brfss",
-                "factor",
-                "risk",
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
@@ -62117,45 +62094,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf",
+            "identifier": "https://data.cdc.gov/api/views/dttw-5yxu",
+            "issued": "2023-07-18",
+            "keyword": [
+                "...",
+                "behavioral",
+                "brfss",
+                "factor",
+                "risk",
+                "survey"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/index.html",
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
-            "landingPage": "https://data.cdc.gov/d/u92k-ms37",
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
-            "identifier": "https://data.cdc.gov/api/views/u92k-ms37",
             "description": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62178,38 +62156,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/u92k-ms37",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "vibriosis confirmed",
+                "vibriosis probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/u92k-ms37",
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
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/epau-tsqw",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-02-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-07",
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
-            "identifier": "9951c048-36b7-4c93-aa4f-e34546836e2e",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-29-to-2024-02-04",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62218,37 +62203,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-29-to-2024-02-04"
                 }
             ],
+            "identifier": "9951c048-36b7-4c93-aa4f-e34546836e2e",
+            "issued": "2024-02-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/epau-tsqw",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-02-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-29-to-2024-02-04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/epfe-db87",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-13",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-20",
-            "keyword": [
-                "continuous eligibility",
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
-            "identifier": "cdb769be-0d7b-524b-9d25-2062d36b60ab",
             "description": "States have the option to provide children with 12 months of continuous coverage through Medicaid and CHIP, even if the family experiences a change in income during the year. Continuous eligibility is a valuable tool that helps States ensure that children stay enrolled in the health coverage for which they are eligible and have consistent access to needed health care services.",
-            "title": "Continuous Eligibility for Medicaid and CHIP Coverage",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62257,173 +62241,166 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "cdb769be-0d7b-524b-9d25-2062d36b60ab",
+            "issued": "2016-07-13",
+            "keyword": [
+                "continuous eligibility",
+                "enrollment strategies"
+            ],
+            "landingPage": "https://healthdata.gov/d/epfe-db87",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2018-12-20",
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
+            "title": "Continuous Eligibility for Medicaid and CHIP Coverage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/eqkd-7gq3",
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
-            "identifier": "cc7f1f2d-8942-5b67-a9fe-e48033c972d2",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_measure_compare",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare.csv",
-                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_compare csv file"
                 }
             ],
+            "identifier": "cc7f1f2d-8942-5b67-a9fe-e48033c972d2",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/eqkd-7gq3",
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
+            "title": "prodAuto_measure_compare"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/eqqh-qat3",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-04-06",
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
-            "identifier": "78d44223-b50f-5a31-91d3-ac9b2b609556",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard pillar v2.11.16 (dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/pillar.csv",
-                    "description": "Scorecard pillar v2.11.16 (dev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard pillar v2.11.16 (dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard pillar v2.11.16 (dev)"
                 }
             ],
+            "identifier": "78d44223-b50f-5a31-91d3-ac9b2b609556",
+            "issued": "2023-04-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/eqqh-qat3",
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
+            "title": "Scorecard pillar v2.11.16 (dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://brads.nichd.nih.gov/Home/",
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
                 "fn": "Songco, David",
                 "hasEmail": "mailto:songcod@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "77e6b5dd-989d-415f-b91b-252c6196cc22",
+            "dataQuality": true,
             "description": "<p>BRADS is a repository for data and biospecimens from population health research initiatives and clinical or interventional trials designed and implemented by NICHD\u2019s Division of Intramural Population Health Research (DIPHR). Topics include human reproduction and development, pregnancy, child health and development, and women\u2019s health. The website is maintained by DIPHR.</p>",
-            "title": "Biospecimen Repository Access and Data Sharing (BRADS)",
+            "identifier": "77e6b5dd-989d-415f-b91b-252c6196cc22",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "https://brads.nichd.nih.gov/Home/",
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
+            "title": "Biospecimen Repository Access and Data Sharing (BRADS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2993-4v7d",
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
-            "identifier": "https://data.cdc.gov/api/views/2993-4v7d",
             "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62446,42 +62423,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2993-4v7d",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/2993-4v7d",
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
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/dailymed-webservices",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-05-30",
-            "temporal": "2005-01-01T00:00:00-05:00/2005-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "drug labeling",
-                "pharmaceutical preparations",
-                "treatments",
-                "united states"
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
-            "identifier": "4a86be2e-023b-47a2-bd8a-c112bbcc08e4",
+            "dataQuality": true,
             "description": "<p>The DailyMed RESTful API is a web service for accessing current SPL information. It is implemented using HTTP and can be thought of as a collection of resources, specified as URLs.</p>",
-            "title": "DailyMed Webservices",
-            "programCode": [
-                "009:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62490,24 +62471,67 @@
                     "title": "API"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "4a86be2e-023b-47a2-bd8a-c112bbcc08e4",
+            "issued": "2012-05-30",
+            "keyword": [
+                "drug labeling",
+                "pharmaceutical preparations",
+                "treatments",
+                "united states"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/dailymed-webservices",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "temporal": "2005-01-01T00:00:00-05:00/2005-01-01T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "DailyMed Webservices"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Counseling-2010-To-Pre/66cx-b9a4",
+            "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/66cx-b9a4",
+            "issued": "2023-07-18",
             "keyword": [
                 "callers",
                 "cessation",
@@ -62522,58 +62546,61 @@
                 "services",
                 "state system"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-25",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/66cx-b9a4",
-            "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
-            "title": "Quitline \u2013 Services Available \u2013 Counseling - 2010 To Present",
-            "programCode": [
-                "009:020"
+            "references": [
+                "https://chronicdata.cdc.gov/d/h6kq-aiu7"
+            ],
+            "theme": [
+                "Quitline"
+            ],
+            "title": "Quitline \u2013 Services Available \u2013 Counseling - 2010 To Present"
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
+            "description": "Provisional counts of deaths in the United States by educational attainment, race, sex, and age group. The dataset includes cumulative provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.rdf?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.rdf?accessType=DOWNLOAD",
                     "mediaType": "application/rdf+xml"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.json?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.json?accessType=DOWNLOAD",
                     "mediaType": "application/json"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.xml?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.xml?accessType=DOWNLOAD",
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Counseling-2010-To-Pre/66cx-b9a4",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
-            "theme": [
-                "Quitline"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/3ts8-hsrw",
             "issued": "2021-02-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-30",
             "keyword": [
                 "age",
                 "age group",
@@ -62591,60 +62618,59 @@
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
+            "modified": "2023-03-30",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/3ts8-hsrw",
-            "description": "Provisional counts of deaths in the United States by educational attainment, race, sex, and age group. The dataset includes cumulative provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
-            "title": "AH Provisional COVID-19 Deaths by Educational Attainment, Race, Sex, and Age",
-            "programCode": [
-                "009:020"
+            "spatial": "United States",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Educational Attainment, Race, Sex, and Age"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Annual",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:healthus@cdc.gov"
+            },
+            "description": "Data on Medicaid coverage among people under age 65, in the United States, by selected population characteristics. Data from Health, United States. SOURCE: National Center for Health Statistics, National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.rdf?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.rdf?accessType=DOWNLOAD",
                     "mediaType": "application/rdf+xml"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.json?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.json?accessType=DOWNLOAD",
                     "mediaType": "application/json"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.xml?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.xml?accessType=DOWNLOAD",
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
+            "identifier": "https://data.cdc.gov/api/views/hdja-ybdg",
             "issued": "2024-04-11",
-            "temporal": "1997/2019",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-30",
             "keyword": [
                 "adults",
                 "american indian or alaska native",
@@ -62668,82 +62694,35 @@
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
-            "identifier": "https://data.cdc.gov/api/views/hdja-ybdg",
-            "description": "Data on Medicaid coverage among people under age 65, in the United States, by selected population characteristics. Data from Health, United States. SOURCE: National Center for Health Statistics, National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Medicaid coverage among persons under age 65, by selected characteristics: United States",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-30",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.xml?accessType=DOWNLOAD",
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
+            "title": "DQS Medicaid coverage among persons under age 65, by selected characteristics: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-county",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2015-06-01",
-            "keyword": [
-                "county",
-                "health information technology",
-                "health it",
-                "health it data",
-                "indicators",
-                "rec",
-                "regional extension centers"
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
-            "identifier": "x2u52lga-mizz-kkra-dbv4-fg6qmi4a0mfh",
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-county",
             "description": "The ONC Regional Extension Centers (REC) Program provides assistance to health care providers to adopt and meaningfully use certified EHR technology. The program, funded through the American Recovery and Reinvestment Act (ARRA) or The Recovery Act, provides grants to organizations, Regional Extension Centers, that assist providers directly in the organization's region. There are 62 unique RECs across the United States. This data set provides county-level health care professional participation in the REC Program. You can track metrics on the total primary care and non-primary care providers that signed up for REC assistance, gone live with an EHR, and demonstrated meaningful use of certified EHR technology. See ONC's REC data by state to track these metrics at the county level.",
-            "title": "ONC Regional Extension Centers (REC) Key Performance Indicators (KPIs) by County",
-            "programCode": [
-                "009:110"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62752,38 +62731,42 @@
                     "title": "REC_KPI_County.csv"
                 }
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-county"
+            "identifier": "x2u52lga-mizz-kkra-dbv4-fg6qmi4a0mfh",
+            "issued": "2023-10-03",
+            "keyword": [
+                "county",
+                "health information technology",
+                "health it",
+                "health it data",
+                "indicators",
+                "rec",
+                "regional extension centers"
+            ],
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-county",
+            "modified": "2015-06-01",
+            "programCode": [
+                "009:110"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "title": "ONC Regional Extension Centers (REC) Key Performance Indicators (KPIs) by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-daily-air-temperatures-and-heat-index",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-08-03",
-            "temporal": "1979-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "air temperature",
-                "heat index climate state county day month year remotely sensed",
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
-            "identifier": "96b92ba4-d63a-40ac-820b-f955d9f0f0f9",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/nldas.html",
             "description": "<p>The Daily Air Temperature and Heat Index data available on CDC WONDER are county-level daily average air temperatures and heat index measures spanning the years 1979-2010. Temperature data are available in Fahrenheit or Celsius scales. Reported measures are the average temperature, number of observations, and range for the daily maximum and minimum air temperatures, and also percent coverage for the daily maximum heat index. Data are available by place (combined 48 contiguous states, region, division, state, county), time (year, month, day) and specified maximum and minimum air temperature, and heat index value. The data are derived from the North America Land Data Assimilation System (NLDAS) through NLDAS Phase 2, a collaboration project among several groups: the National Oceanic and Atmospheric Administration (NOAA) National Centers for Environmental Prediction (NCEP) Environmental Modeling Center (EMC), the National Aeronautics and Space Administration (NASA) Goddard Space Flight Center (GSFC), Princeton University, the National Weather Service (NWS) Office of Hydrological Development (OHD), the University of Washington, and the NCEP Climate Prediction Center (CPC). In a study funded by the NASA Applied Sciences Program/Public Health Program, scientists at NASA Marshall Space Flight Center/ Universities Space Research Association developed the analysis to produce the data available on CDC WONDER.</p>",
-            "title": "CDC WONDER: Daily Air Temperatures and Heat Index",
-            "programCode": [
-                "010:167"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62792,48 +62775,42 @@
                     "title": "Text "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/nldas.html",
-            "dataQuality": true,
+            "identifier": "96b92ba4-d63a-40ac-820b-f955d9f0f0f9",
+            "issued": "2012-08-03",
+            "keyword": [
+                "air temperature",
+                "heat index climate state county day month year remotely sensed",
+                "other"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-daily-air-temperatures-and-heat-index",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "010:167"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1979-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Daily Air Temperatures and Heat Index"
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
@@ -62856,54 +62833,55 @@
                     "mediaType": "application/xml"
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
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-eligible-beneficiaries",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-05-26",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/54551982-39a8-4744-90f6-c38bb4dd5108/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-reach-eligible-beneficiary-data-dictionary",
             "description": "Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Eligible Beneficiary Public Use File (PUF) data details Medicare Beneficiaries who were used as the reference population for comparison to aligned to the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model, including average risk scores and eligibility months. This data is redacted and does not include identifiable information.",
-            "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/54551982-39a8-4744-90f6-c38bb4dd5108/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/54551982-39a8-4744-90f6-c38bb4dd5108/data",
+                    "mediaType": "text/html",
                     "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01"
                 },
                 {
@@ -62919,44 +62897,50 @@
                     "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/aco-reach-eligible-beneficiary-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/54551982-39a8-4744-90f6-c38bb4dd5108/data-viewer",
+            "issued": "2023-05-26",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-eligible-beneficiaries",
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
+            "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2nf2-f75n",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-12",
-            "keyword": [
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Spiro Tsipianitis",
                 "hasEmail": "mailto:cgw0@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2nf2-f75n",
             "description": "This is a dataset manually created by Spiro Tsipianitis via data.cdc.gov",
-            "title": "dhds_dataset",
-            "programCode": [
-                "009:022"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62979,45 +62963,38 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2nf2-f75n",
+            "issued": "2023-12-12",
+            "keyword": [
+                "united states"
+            ],
+            "landingPage": "https://data.cdc.gov/d/2nf2-f75n",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-12-12",
+            "programCode": [
+                "009:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Web Metrics"
-            ]
+            ],
+            "title": "dhds_dataset"
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
-            "modified": "2025-01-13",
-            "keyword": [
-                "immunization",
-                "influenza",
-                "pregnancy & vaccinations",
-                "td",
-                "tdap",
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
-            "identifier": "https://data.cdc.gov/api/views/h7pm-wmjc",
             "description": "Vaccination Coverage among Pregnant Women\n\n\u2022 Data on influenza and tetanus toxoid, reduced diphtheria toxoid, and acellular pertussis (Tdap) vaccination coverage at the state level from the Pregnancy Risk Assessment Monitoring System (PRAMS) for women who had a recent live birth by age and race/ethnicity.\n\n\u2022 Additional information available at https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html and https://www.cdc.gov/flu/fluvaxview/index.htm",
-            "title": "Vaccination Coverage among Pregnant Women",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63040,44 +63017,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h7pm-wmjc",
+            "issued": "2021-05-13",
+            "keyword": [
+                "immunization",
+                "influenza",
+                "pregnancy & vaccinations",
+                "td",
+                "tdap",
+                "vaccination",
+                "vaccination coverage",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html and https://www.cdc.gov/flu/fluvaxview/index.htm",
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
                 "Pregnancy & Vaccination"
-            ]
+            ],
+            "title": "Vaccination Coverage among Pregnant Women"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -63100,88 +63078,92 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/evma-y6ey",
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
-            "identifier": "8f7c327d-2add-5168-9837-6c55a6826f37",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_states_measures",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures.csv",
-                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures.csv",
+                    "mediaType": "text/csv",
                     "title": "states_measures csv file"
                 }
             ],
+            "identifier": "8f7c327d-2add-5168-9837-6c55a6826f37",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/evma-y6ey",
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
+            "title": "featAuto_states_measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/linkout/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "library services",
-                "literature",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/526z-s65v",
             "description": "LinkOut is a service that allows you to link directly from PubMed and other NCBI databases to a wide range of information and services beyond the NCBI systems. LinkOut aims to facilitate access to relevant online resources in order to extend, clarify, and supplement information found in NCBI databases.\n\nThird parties can link directly from PubMed and other Entrez database records to relevant Web-accessible resources beyond the Entrez system. Includes full-text publications, biological databases, consumer health information and research tools.",
-            "title": "Library LinkOut",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63190,48 +63172,41 @@
                     "title": "Library LinkOut Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/526z-s65v",
+            "issued": "2022-02-08",
+            "keyword": [
+                "library services",
+                "literature",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/linkout/",
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
+            "title": "Library LinkOut"
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
-                "brfss",
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
-            "identifier": "https://data.cdc.gov/api/views/ikwk-8git",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/Behavioral-Risk-Factor-Surveillance-System-BRFSS-N/fwns-azgu",
             "description": "2011\u20132020. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (national, regional, state, and selected sites) and indicator, and they include CVDs (e.g., heart failure) and risk factors (e.g., hypertension). The data can be plotted as trends and stratified by age group, sex, and race/ethnicity.",
-            "title": "Behavioral Risk Factor Surveillance System (BRFSS) -  National Cardiovascular Disease Surveillance Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63254,39 +63229,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/Behavioral-Risk-Factor-Surveillance-System-BRFSS-N/fwns-azgu",
+            "identifier": "https://data.cdc.gov/api/views/ikwk-8git",
+            "issued": "2023-08-11",
+            "keyword": [
+                "brfss",
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
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) -  National Cardiovascular Disease Surveillance Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ewng-ywsi",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-30",
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
-            "identifier": "f9923173-d3c6-4a3f-91e3-48fc7df6f209",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-23-to-2023-10-29",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63295,81 +63280,83 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-23-to-2023-10-29"
                 }
             ],
+            "identifier": "f9923173-d3c6-4a3f-91e3-48fc7df6f209",
+            "issued": "2023-10-31",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/ewng-ywsi",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-10-30",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-23-to-2023-10-29"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ewnm-busu",
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
-            "identifier": "fc93a1e1-dca9-557b-95bf-ba92017c8794",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_measure_backgroundAndMethods",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_backgroundAndMethods.csv",
-                    "description": "{\"dataset\": \"measure_backgroundAndMethods\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_backgroundAndMethods\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_backgroundAndMethods.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_backgroundAndMethods csv file"
                 }
             ],
+            "identifier": "fc93a1e1-dca9-557b-95bf-ba92017c8794",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/ewnm-busu",
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
+            "title": "featAuto_measure_backgroundAndMethods"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/j63e-g9bn",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Physical Effects Research Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/j63e-g9bn",
             "description": "The anterior and posterior superior iliac spine markers are commonly used to define the pelvis, and these markers are predisposed to occlusion during three-dimensional motion capture. The occlusion of these markers leads to the use of various tracking marker configurations on the pelvis, which can create differences in kinematic results. The purpose of this investigation was to examine the agreement of CODA pelvis kinematic results when two different tracking marker configurations were used during ergonomic roofing tasks. Three-dimensional motion data was collected on seven male subjects while mimicking a standing and kneeling roofing task. Hip joint angles were computed using the CODA pelvis with two different tracking marker configurations, the Trochanter Tracking Method (TTM), and the Virtual Pelvis Tracking Method (VPTM).",
-            "title": "Agreement of hip kinematics between two tracking marker configurations used with the 1 CODA pelvis during ergonomic roofing tasks",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63377,38 +63364,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/j63e-g9bn",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/j63e-g9bn",
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
+            "title": "Agreement of hip kinematics between two tracking marker configurations used with the 1 CODA pelvis during ergonomic roofing tasks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ex43-2u8q",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-04-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-19",
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
-            "identifier": "0131a022-958f-45d1-a746-f937bc916c6d",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-10-to-2023-04-16",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63417,36 +63402,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-10-to-2023-04-16"
                 }
             ],
+            "identifier": "0131a022-958f-45d1-a746-f937bc916c6d",
+            "issued": "2023-04-20",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/ex43-2u8q",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-04-19",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-10-to-2023-04-16"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/exyz-4spk",
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
-            "identifier": "beaedcae-1ff6-4c66-b8e2-5ac43751436b",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210816 to 20210822",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63454,33 +63439,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "beaedcae-1ff6-4c66-b8e2-5ac43751436b",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/exyz-4spk",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210816 to 20210822"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mkyn-icix",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Safety Research Analysis and Field Evaluations Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mkyn-icix",
             "description": "It is widely acknowledged that there are costs involved with fatal injury to workers. These costs cross numerous boundaries, and generally address the overall costs to victims and the affected groups, and to society as a whole. This represents a cause for concern to employers, worker groups, policy makers, medical personnel, economists and others interested in workplace safety and health. This broad-reaching burden can include social costs, organizational costs, familial and interpersonal group costs, as well as personal costs such as suffering and loss of companionship. The data in the accompanying tables focus on monetary costs of fatal occupational injury which largely consist of foregone wages, but also include the direct costs of medical care and the indirect costs of household production and certain ancillary measures.\n\nThese data represent a continuation of prior research by the National Institute for Occupational Safety and Health (NIOSH) that attempted to delimit the economic consequences of workplace injury for earlier years. Interested parties should be aware that these data serve as a supplemental update to prior NIOSH publications which described the magnitude and circumstances of occupational injury deaths for earlier years 1,2.\n\nThe current data build on this research, and the findings are compelling. Over the period studied, 2003-2010, the costs from these 42,380 premature deaths exceeded $44 billion, an amount greater than the reportable gross domestic product for some States. These findings inform the national will to reduce this severe toll on our nation\u2019s workers, institutions, communities, and the nation itself. Researchers and concerned parties within the occupational and public health professions, academia, organizations focusing on workplace safety, labor unions and the business community have all proven to be willing and avid users of this data, and have used this research to continue their efforts, in concert with continuing NIOSH research efforts, to reduce the great toll that injury imposes on our workers, workplaces, and Nation.",
-            "title": "Economic Burden of Occupational Fatal Injuries in the United States Based on the Census of Fatal Occupational Injuries, 2003-2010",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63488,35 +63475,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mkyn-icix",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/mkyn-icix",
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
+            "title": "Economic Burden of Occupational Fatal Injuries in the United States Based on the Census of Fatal Occupational Injuries, 2003-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/4u7c-2g4q",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pathology and Physiology Research Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4u7c-2g4q",
             "description": "The toxicity of boron nitride nanotubes (BNNTs) is confounded by the various manufacturing and purification strategies employed targeted to remove 30-60% of the residuals and impurities. Four BNNTs manufactured by the induction thermal plasma process allowed us to assess the influence of these residuals/impurities on the toxicity profile of BNNTs by producing a gradient of BNNT purity levels through sequential gas purification, and water and solvent washing, followed by filtration. Extensive characterization including Infrared, x-ray spectroscopy, thermogravimetric analysis, size, charge, surface area and density allowed characterization of the alteration in physicochemical properties as the material went through sequential purification. The material from each step was screened using acellular and in vitro assays that evaluated general toxicity, mechanisms of toxicity and macrophage function.",
-            "title": "Influence of Impurities from Manufacturing Process on the Toxicity Profile of Boron Nitride Nanotubes",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63524,66 +63511,92 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4u7c-2g4q",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/4u7c-2g4q",
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
+            "title": "Influence of Impurities from Manufacturing Process on the Toxicity Profile of Boron Nitride Nanotubes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ezer-ms4j",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-24",
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
-            "identifier": "e8ec5dc4-7904-52d4-8ce9-73c2fb188514",
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
+            "identifier": "e8ec5dc4-7904-52d4-8ce9-73c2fb188514",
+            "issued": "2023-03-28",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/ezer-ms4j",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2023-03-24",
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
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1997",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, and tobacco among members of United<br />\nStates households aged 12 and older. Questions include age at first<br />\nuse as well as lifetime, annual, and past-month usage for the<br />\nfollowing drug classes: marijuana, cocaine (and crack), hallucinogens,<br />\nheroin, inhalants, alcohol, tobacco, and nonmedical use of<br />\nprescription drugs, including psychotherapeutics. Respondents were<br />\nalso asked about substance abuse treatment history, illegal<br />\nactivities, problems resulting from the use of drugs, personal and<br />\nfamily income sources and amounts, need for treatment for drug or<br />\nalcohol use, criminal record, and needle-sharing. Questions on mental<br />\nhealth and access to care, which were introduced in the 1994-B<br />\nquestionnaire (see NATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1994), were retained in this administration of the survey. In<br />\n1996, the section on risk/availability of drugs was reintroduced, and<br />\nsections on driving behavior and personal behavior were added (see<br />\nNATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1996). The 1997<br />\nquestionnaire continued the risk/availability section along with new<br />\nitems about the use of cigars, people present when respondents used<br />\nmarijuana or cocaine for the first time (if applicable), reasons for<br />\nusing these two drugs the first time, reasons for using these two<br />\ndrugs in the past year, reasons for discontinuing use of these two<br />\ndrugs (for lifetime but not past-year users), and reasons respondents<br />\nnever used these two drugs. In addition, a new series of questions<br />\nasked only of respondents aged 12 to 17 was introduced. These items<br />\ncovered a variety of topics that may be associated with substance use<br />\nand related behaviors, such as exposure to substance abuse prevention<br />\nand education programs, gang involvement, relationship with parents,<br />\nand substance use by friends. Demographic data include gender, race,<br />\nage, ethnicity, marital status, educational level, job status, income<br />\nlevel, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1997) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1997-nid13619",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1997-nid13619"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1997-nid13619",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -63615,64 +63628,29 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1997",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1997-nid13619",
-            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, and tobacco among members of United<br />\nStates households aged 12 and older. Questions include age at first<br />\nuse as well as lifetime, annual, and past-month usage for the<br />\nfollowing drug classes: marijuana, cocaine (and crack), hallucinogens,<br />\nheroin, inhalants, alcohol, tobacco, and nonmedical use of<br />\nprescription drugs, including psychotherapeutics. Respondents were<br />\nalso asked about substance abuse treatment history, illegal<br />\nactivities, problems resulting from the use of drugs, personal and<br />\nfamily income sources and amounts, need for treatment for drug or<br />\nalcohol use, criminal record, and needle-sharing. Questions on mental<br />\nhealth and access to care, which were introduced in the 1994-B<br />\nquestionnaire (see NATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1994), were retained in this administration of the survey. In<br />\n1996, the section on risk/availability of drugs was reintroduced, and<br />\nsections on driving behavior and personal behavior were added (see<br />\nNATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1996). The 1997<br />\nquestionnaire continued the risk/availability section along with new<br />\nitems about the use of cigars, people present when respondents used<br />\nmarijuana or cocaine for the first time (if applicable), reasons for<br />\nusing these two drugs the first time, reasons for using these two<br />\ndrugs in the past year, reasons for discontinuing use of these two<br />\ndrugs (for lifetime but not past-year users), and reasons respondents<br />\nnever used these two drugs. In addition, a new series of questions<br />\nasked only of respondents aged 12 to 17 was introduced. These items<br />\ncovered a variety of topics that may be associated with substance use<br />\nand related behaviors, such as exposure to substance abuse prevention<br />\nand education programs, gang involvement, relationship with parents,<br />\nand substance use by friends. Demographic data include gender, race,<br />\nage, ethnicity, marital status, educational level, job status, income<br />\nlevel, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1997)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1997-nid13619",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1997) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1997-nid13619"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1997)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yvsw-8ht9",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/yvsw-8ht9",
             "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses. With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2012 have been variant influenza viruses.",
-            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63695,45 +63673,45 @@
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
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
-            "bureauCode": [
-                "009:20"
+            "identifier": "https://data.cdc.gov/api/views/yvsw-8ht9",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a virus infections",
+                "wonder"
             ],
-            "issued": "2024-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "references": [
-                "https://www.census.gov/content/dam/Census/programs-surveys/acs/about/ACS_Information_Guide.pdf",
-                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/american-community-survey.html"
+            "landingPage": "https://data.cdc.gov/d/yvsw-8ht9",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
             ],
-            "keyword": [
-                "acs",
-                "contact lenses",
-                "glasses",
-                "visual function"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
+        },
+        {
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
-            "identifier": "https://data.cdc.gov/api/views/thir-stei",
+            "describedBy": "https://chronicdata.cdc.gov/d/thir-stei",
             "description": "2014 - 2022 (excluding 2020). This dataset is a de-identified summary table of vision and eye health data indicators from ACS, stratified by all available combinations of age group, race/ethnicity, gender, and state. ACS is an annual nationwide survey conducted by the U.S. Census Bureau that collects information on demographic, social, economic, and housing characteristics of the U.S. population. Approximate sample size is 3 million annually. ACS data for VEHSS includes one question related to Visual Function. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Data will be updated as it becomes available. Detailed information on VEHSS ACS analyses can be found on the VEHSS ACS webpage (link). Additional information about ACS can be found on the U.S. Census Bureau website (https://www.census.gov/content/dam/Census/programs-surveys/acs/about/ACS_Information_Guide.pdf). The VEHSS ACS dataset was last updated April 2024",
-            "title": "American Community Survey (ACS) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63756,42 +63734,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/d/thir-stei",
+            "identifier": "https://data.cdc.gov/api/views/thir-stei",
+            "issued": "2024-05-01",
+            "keyword": [
+                "acs",
+                "contact lenses",
+                "glasses",
+                "visual function"
+            ],
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2024-05-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://www.census.gov/content/dam/Census/programs-surveys/acs/about/ACS_Information_Guide.pdf",
+                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/american-community-survey.html"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "American Community Survey (ACS) \u2013 Vision and Eye Health Surveillance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ii.nlm.nih.gov/Web_API/index.shtml",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n87j-59eu",
             "description": "The SKR Project was initiated at NLM in order to develop programs to provide usable semantic representation of biomedical free text by building on resources currently available at the library. The SKR project is concerned with reliable and effective management of the information encoded in natural language texts. The project develops programs that provide usable semantic representation of biomedical text by building on resources currently available at the Library, especially the UMLS knowledge sources and the natural language processing tools provided by the SPECIALIST system. This Java-based API to the Semantic Knowledge Representation (SKR) Scheduler facility was created to provide users with the ability to programmatically submit jobs to the Scheduler Batch and Interactive facilities instead of using the Web-based interface.",
-            "title": "Semantic Knowledge Representation API",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63800,55 +63781,51 @@
                     "title": "API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n87j-59eu",
+            "issued": "2012-08-22",
+            "keyword": [
+                "api",
+                "medical informatics",
+                "terminologies",
+                "tools & utilities"
+            ],
+            "landingPage": "https://ii.nlm.nih.gov/Web_API/index.shtml",
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
+            "title": "Semantic Knowledge Representation API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-geographic-comparisons/medicare-geographic-variation-by-national-state-county",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2022-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-31",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-05/a0e72c13-805a-4546-bb18-4e75e84a282f/Geographic%20Variation%20Public%20Use%20File%20Methods%20Paper.pdf"
-            ],
-            "keyword": [
-                "counties",
-                "health care use & payments",
-                "health equity",
-                "medicare",
-                "national",
-                "original medicare",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/6219697b-8f6c-4164-bed4-cd9317c58ebc/data-viewer",
-            "description": "The Medicare Geographic Variation by National, State & County dataset provides information on the geographic differences in the use and quality of health care services for the Original Medicare\u00a0population. This dataset contains demographic, spending, use, and quality indicators at the state level (including the District of Columbia, Puerto Rico, and the Virgin Islands) and the county level.\n\nSpending is standardized to remove geographic differences in payment rates for individual services as a source of variation. In general, total standardized per capita costs are less than actual per capita costs because the extra payments Medicare made to hospitals were removed, such as payments for medical education (both direct and indirect) and payments to hospitals that serve a disproportionate share of low-income patients. Standardization does not adjust for differences in beneficiaries\u2019 health status.",
-            "title": "Medicare Geographic Variation - by National, State & County",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-05/3f6841ec-571e-4e03-8766-5ef355c76857/2014-2022%20Medicare%20Geographic%20Variation%20by%20National%20State%20%20County%20Data%20Dictionary_508.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Medicare Geographic Variation by National, State & County dataset provides information on the geographic differences in the use and quality of health care services for the Original Medicare\u00a0population. This dataset contains demographic, spending, use, and quality indicators at the state level (including the District of Columbia, Puerto Rico, and the Virgin Islands) and the county level.\n\nSpending is standardized to remove geographic differences in payment rates for individual services as a source of variation. In general, total standardized per capita costs are less than actual per capita costs because the extra payments Medicare made to hospitals were removed, such as payments for medical education (both direct and indirect) and payments to hospitals that serve a disproportionate share of low-income patients. Standardization does not adjust for differences in beneficiaries\u2019 health status.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6219697b-8f6c-4164-bed4-cd9317c58ebc/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6219697b-8f6c-4164-bed4-cd9317c58ebc/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Geographic Variation - by National, State & County : 2022-01-15"
                 },
                 {
@@ -63864,45 +63841,51 @@
                     "title": "Medicare Geographic Variation - by National, State & County : 2022-01-15"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-05/3f6841ec-571e-4e03-8766-5ef355c76857/2014-2022%20Medicare%20Geographic%20Variation%20by%20National%20State%20%20County%20Data%20Dictionary_508.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6219697b-8f6c-4164-bed4-cd9317c58ebc/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "counties",
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-geographic-comparisons/medicare-geographic-variation-by-national-state-county",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-07-31",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-05/a0e72c13-805a-4546-bb18-4e75e84a282f/Geographic%20Variation%20Public%20Use%20File%20Methods%20Paper.pdf"
+            ],
+            "temporal": "2022-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Geographic Variation - by National, State & County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/cobalt/cobalt.cgi",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nerf-hjnp",
             "description": "Constraint-Based Multiple Alignment Tool (COBALT) is a protein multiple sequence alignment tool that finds a collection of pairwise constraints derived from conserved domain database, protein motif database, and sequence similarity, using RPS-BLAST, BLASTP, and PHI-BLAST.",
-            "title": "Constraint-Based Multiple Alignment Tool (COBALT)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63911,43 +63894,40 @@
                     "title": "COBALT Homepage and Search"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nerf-hjnp",
+            "issued": "2021-06-30",
+            "keyword": [
+                "protein",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/cobalt/cobalt.cgi",
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
+            "title": "Constraint-Based Multiple Alignment Tool (COBALT)"
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
-                "smokefree indoor air",
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
-            "identifier": "https://data.cdc.gov/api/views/32fd-hyzc",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Ind/32fd-hyzc",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC).  State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation \u2013 Smokefree Indoor Air. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to state legislation on smokefree indoor air in areas such as: Bars, Commercial Day Care Centers, Government Multi-Unit Housing, Government Worksites, Home-Based Day Care Centers, Hotels and Motels, Personal Vehicles, Private Multi-Unit Housing, Private Worksites, Restaurants, Bingo Halls, Casinos, Enclosed Arenas, Grocery Stores, Hospitals, Hospital Campuses, Malls, Mental Health Outpatient and Residential Facilities, Prisons, Public Transportation, Racetrack Casinos, Substance Abuse Outpatient and Residential Facilities.",
-            "title": "CDC STATE System Tobacco Legislation - Smokefree Indoor Air",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63970,42 +63950,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Ind/32fd-hyzc",
+            "identifier": "https://data.cdc.gov/api/views/32fd-hyzc",
+            "issued": "2023-07-18",
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "smokefree indoor air",
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
+            "title": "CDC STATE System Tobacco Legislation - Smokefree Indoor Air"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "references": [
-                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm"
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
-            "identifier": "7138583c-afe2-4e52-843b-a0665c75714d",
+            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm",
             "description": "This searchable database contains establishments (engaged in the manufacture, preparation, propagation, compounding, assembly, or processing of medical devices intended for human use and commercial distribution) and listings of medical devices in commercial distribution by both domestic and foreign manufacturers. Note: This database is updated once a week.",
-            "title": "Establishment Registration & Device Listing",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64013,22 +63996,49 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm",
+            "identifier": "7138583c-afe2-4e52-843b-a0665c75714d",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1W"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm"
+            ],
+            "title": "Establishment Registration & Device Listing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/office-based-health-care-providers-database",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2014-12-01",
-            "references": [
-                "https://www.healthit.gov/data/apps/office-based-physicians-have-demonstrated-meaningful-use-through-medicare-ehr-incentive"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/office-based-health-care-providers-database",
+            "description": "ONC uses the SK&amp;A Office-based Provider Database to calculate the counts of medical doctors, doctors of osteopathy, nurse practitioners, and physician assistants at the state and count level from 2011 through 2013. These counts are grouped as a total, as well as segmented by each provider type and separately as counts of primary care providers.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/SKA_State_County_Data_2011-2013.csv",
+                    "mediaType": "text/csv",
+                    "title": "SKA_State_County_Data_2011-2013.csv"
+                }
             ],
+            "identifier": "oerg8yyb-66a7-cry5-ljpv-0x7h9uz4xq52",
+            "issued": "2023-10-03",
             "keyword": [
                 "health information technology",
                 "health it",
@@ -64039,72 +64049,33 @@
                 "primary care physicians",
                 "providers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/office-based-health-care-providers-database",
+            "modified": "2014-12-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "oerg8yyb-66a7-cry5-ljpv-0x7h9uz4xq52",
-            "description": "ONC uses the SK&amp;A Office-based Provider Database to calculate the counts of medical doctors, doctors of osteopathy, nurse practitioners, and physician assistants at the state and count level from 2011 through 2013. These counts are grouped as a total, as well as segmented by each provider type and separately as counts of primary care providers.",
-            "title": "Office-based Health Care Providers Database",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/SKA_State_County_Data_2011-2013.csv",
-                    "mediaType": "text/csv",
-                    "title": "SKA_State_County_Data_2011-2013.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/apps/office-based-physicians-have-demonstrated-meaningful-use-through-medicare-ehr-incentive"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/office-based-health-care-providers-database"
+            "title": "Office-based Health Care Providers Database"
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
@@ -64127,21 +64098,63 @@
                     "mediaType": "application/xml"
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
-            "landingPage": "https://healthdata.gov/d/f4j7-krxz",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jeff Chamblee",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. Because Medicaid beneficiaries may be enrolled concurrently in more than one type of managed care program (e.g., a Comprehensive MCO and a BHO), users should not sum enrollment across all program types, since the total would count individuals more than once and, in some states, exceed the actual number of Medicaid enrollees.\t\t\t\t\t\t\t\t\r\n2. Comprehensive MCOs cover acute, primary, and specialty medical care services; they may also cover behavioral health, long-term services and supports, and other benefits in some states. Limited benefit managed care programs, including MLTSS only, BHO, Dental, Transportation, and Other cover a narrower set of services.\t\t\t\t\t\t\t\t\r\n3. The indicated territory was not able to supply data for this report. The Northern Mariana Islands reported that they have no Medicaid managed care enrollment, but they did not report total Medicaid enrollees.\r\n4. The \u201cTotal dually eligible individuals\u201d column represents an unduplicated count of all beneficiaries in FFS and any type of managed care, including enrollees receiving full Medicaid benefits or Medicaid cost sharing.\r\n\t\t\t\t\t\r\n\"--\" indicates states that do not operate programs of a given type. 0 signifies that a state operated a program of this type in 2014, but it ended before July 1, 2014, or began after that date.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-by-program-and-population-duals.2022.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "identifier": "8e7be65b-97ba-5ecf-8394-ca8e6f63685a",
             "issued": "2017-12-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
             "keyword": [
                 "bho",
                 "managed care enrollment",
@@ -64154,69 +64167,34 @@
                 "pccm",
                 "pihp"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jeff Chamblee",
-                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/f4j7-krxz",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-16",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "8e7be65b-97ba-5ecf-8394-ca8e6f63685a",
-            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. Because Medicaid beneficiaries may be enrolled concurrently in more than one type of managed care program (e.g., a Comprehensive MCO and a BHO), users should not sum enrollment across all program types, since the total would count individuals more than once and, in some states, exceed the actual number of Medicaid enrollees.\t\t\t\t\t\t\t\t\r\n2. Comprehensive MCOs cover acute, primary, and specialty medical care services; they may also cover behavioral health, long-term services and supports, and other benefits in some states. Limited benefit managed care programs, including MLTSS only, BHO, Dental, Transportation, and Other cover a narrower set of services.\t\t\t\t\t\t\t\t\r\n3. The indicated territory was not able to supply data for this report. The Northern Mariana Islands reported that they have no Medicaid managed care enrollment, but they did not report total Medicaid enrollees.\r\n4. The \u201cTotal dually eligible individuals\u201d column represents an unduplicated count of all beneficiaries in FFS and any type of managed care, including enrollees receiving full Medicaid benefits or Medicaid cost sharing.\r\n\t\t\t\t\t\r\n\"--\" indicates states that do not operate programs of a given type. 0 signifies that a state operated a program of this type in 2014, but it ended before July 1, 2014, or began after that date.",
-            "title": "Managed Care Enrollment by Program and Population (Duals)",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-by-program-and-population-duals.2022.csv",
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
+            "title": "Managed Care Enrollment by Program and Population (Duals)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/sumd-iwm8",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "N/A",
-            "issued": "2024-10-04",
-            "@type": "dcat:Dataset",
-            "temporal": "October 1, 2024 - no specified end date",
-            "modified": "2025-01-17",
-            "keyword": [
-                "deaths",
-                "disease burden",
-                "hospitalizations",
-                "outpatient visits",
-                "respiratory syncytial virus",
-                "rsv"
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
-            "identifier": "https://data.cdc.gov/api/views/sumd-iwm8",
             "description": "This dataset represents preliminary estimates of cumulative U.S. RSV \u2013associated disease burden estimates for the 2024-2025 season, including outpatient visits, hospitalizations, and deaths. Real-time estimates are preliminary and based on continuously collected surveillance data from patients hospitalized with laboratory-confirmed respiratory syncytial virus (RSV) infections. The data  come from the Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET), a surveillance platform that captures data from hospitals that serve about 8% of the U.S. population. Each week CDC estimates a range (i.e., lower estimate and an upper estimate) of RSV-associated disease burden estimates that have occurred since October 1, 2024.  \n\n<b>Note:</b> Data are preliminary and subject to change as more data become available. Rates for recent RSV-associated hospital admissions are subject to reporting delays; as new data are received each week, previous rates are updated accordingly.  \n\n<b>Note:</b> Preliminary burden estimates are not inclusive of data from all RSV-NET sites. Due to model limitations, sites with small sample sizes can impact estimates in unpredictable ways and are excluded for the benefit of model stability. CDC is working to address model limitations and include data from all sites in final burden estimates.  \n\n\n<b>References</b>\n<ol><li>Reed C, Chaves SS, Daily Kirley P, et al. Estimating influenza disease burden from population-based surveillance data in the United States. PLoS One. 2015;10(3):e0118369. https://doi.org/10.1371/journal.pone.0118369\u202f </li><li>Rolfes, MA, Foppa, IM, Garg, S, et al. Annual estimates of the burden of seasonal influenza in the United States: A tool for strengthening influenza surveillance and preparedness. Influenza Other Respi Viruses. 2018; 12: 132\u2013 137. https://doi.org/10.1111/irv.12486</li><li>Tokars  JI, Rolfes  MA, Foppa  IM, Reed  C.  An evaluation and update of methods for estimating the number of influenza cases averted by vaccination in the United States.   Vaccine. 2018;36(48):7331-7337. doi:10.1016/j.vaccine.2018.10.026\u202f</li><li>Collier SA, Deng L, Adam EA, Benedict KM, Beshearse EM, Blackstock AJ, Bruce BB, Derado G, Edens C, Fullerton KE, Gargano JW, Geissler AL, Hall AJ, Havelaar AH, Hill VR, Hoekstra RM, Reddy SC, Scallan E, Stokes EK, Yoder JS, Beach MJ. Estimate of Burden and Direct Healthcare Cost of Infectious Waterborne Disease in the United States. Emerg Infect Dis. 2021 Jan;27(1):140-149. doi: 10.3201/eid2701.190676. PMID: 33350905; PMCID: PMC7774540.</li><li>Reed C, Kim IK, Singleton JA,\u202f et al. Estimated influenza illnesses and hospitalizations averted by vaccination\u2013United States, 2013-14 influenza season. MMWR Morb Mortal Wkly Rep. 2014 Dec 12;63(49):1151-4. https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6349a2.htm\u202f</li><li>Reed C, Angulo FJ, Swerdlow DL, et al. Estimates of the Prevalence of Pandemic (H1N1) 2009, United States, April\u2013July 2009. Emerg Infect Dis. 2009;15(12):2004-2007. https://dx.doi.org/10.3201/eid1512.091413 \u202f</li><li>Devine O, Pham H, Gunnels B, et al. Extrapolating Sentinel Surveillance Information to Estimate National COVID-19 Hospital Admission Rates: A Bayesian Modeling Approach. Influenza and Other Respiratory Viruses. https://onlinelibrary.wiley.com/doi/10.1111/irv.70026. Volume18, Issue10. October 2024.</li><li><a ref=\"https://www.cdc.gov/covid/php/covid-net/index.html\">COVID-NET | COVID-19 | CDC\u202f</a></li><li>https://www.cdc.gov/covid/hcp/clinical-care/systematic-review-process.html\u202f </li><li><a ref=\"https://academic.oup.com/pnasnexus/article/1/3/pgac079/6604394?login=false\">Excess natural-cause deaths in California by cause and setting: March 2020 through February 2021 | PNAS Nexus | Oxford Academic (oup.com)</a></li><li>Kruschke, J. K. 2011. Doing Bayesian data analysis: a tutorial with R and BUGS. Elsevier, Amsterdam, Section 3.3.5.</li></ol>",
-            "title": "Preliminary 2024-2025 U.S. RSV Burden Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64239,40 +64217,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/sumd-iwm8",
+            "issued": "2024-10-04",
+            "keyword": [
+                "deaths",
+                "disease burden",
+                "hospitalizations",
+                "outpatient visits",
+                "respiratory syncytial virus",
+                "rsv"
+            ],
+            "landingPage": "https://data.cdc.gov/d/sumd-iwm8",
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
+            "title": "Preliminary 2024-2025 U.S. RSV Burden Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/sra",
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
                 "fn": "O&#039;Sullivan, Chris",
                 "hasEmail": "mailto:osulliva@ncbi.nlm.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "9b502ae8-4e12-4157-9f4a-bc8de6053870",
+            "dataQuality": true,
             "description": "<p>The Sequence Read Archive (SRA) stores raw sequencing data from the next generation of sequencing platforms including Roche 454 GS System\u00ae, Illumina Genome Analyzer\u00ae, Applied Biosystems SOLiD\u00ae System, Helicos Heliscope\u00ae, Complete Genomics\u00ae, and Pacific Biosciences SMRT\u00ae.</p>",
-            "title": "Sequence Read Archive (SRA)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64281,58 +64266,41 @@
                     "title": "Sequence Read Archive (SRA)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "9b502ae8-4e12-4157-9f4a-bc8de6053870",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/sra",
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
+            "title": "Sequence Read Archive (SRA)"
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
-            "modified": "2024-11-05",
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
-            "identifier": "https://data.cdc.gov/api/views/pg2r-sfcx",
-            "description": "Interactive Summary Health Statistics for Adults provide annual estimates of selected health topics for adults aged 18 years and over based on final data from the National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS NHIS Adult Summary Health Statistics",
-            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "describedBy": "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "Interactive Summary Health Statistics for Adults provide annual estimates of selected health topics for adults aged 18 years and over based on final data from the National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64355,45 +64323,58 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf",
+            "identifier": "https://data.cdc.gov/api/views/pg2r-sfcx",
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
+            "modified": "2024-11-05",
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
+            "title": "DQS NHIS Adult Summary Health Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "http://www.cdc.gov/STATESystem",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "gsps",
-                "gtss",
-                "osh",
-                "school personnel",
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
-            "identifier": "https://data.cdc.gov/api/views/5hns-mwci",
+            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Sch/5hns-mwci",
             "description": "2001-2011. The GSPS was initiated in 2000 to collect information on tobacco use, knowledge and attitudes of school personnel toward tobacco, existence and effectiveness of tobacco control policies in schools, and training and materials available for implementing tobacco prevention and control interventions.",
-            "title": "Global Tobacco Surveillance System (GTSS) - Global School Personnel Survey (GSPS)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64416,47 +64397,42 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Sch/5hns-mwci",
+            "identifier": "https://data.cdc.gov/api/views/5hns-mwci",
+            "issued": "2023-07-18",
+            "keyword": [
+                "gsps",
+                "gtss",
+                "osh",
+                "school personnel",
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
+            "title": "Global Tobacco Surveillance System (GTSS) - Global School Personnel Survey (GSPS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i43m-djm6",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/i43m-djm6",
             "description": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Reporting jurisdictions were informed CDC could receive data for this condition in August 2019. Please note there will be a delay in reporting of case notifications for this condition to CDC.",
-            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64479,40 +64455,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i43m-djm6",
+            "issued": "2020-01-17",
+            "keyword": [
+                "2020",
+                "brucellosis",
+                "campylobacteriosis",
+                "candida auris",
+                "clinical",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i43m-djm6",
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
+            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/f77z-wtsx",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-06-01",
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
-            "identifier": "a9cfe5e9-d7d8-5b87-a7db-b45a7daf84fc",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2014",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64520,36 +64503,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "a9cfe5e9-d7d8-5b87-a7db-b45a7daf84fc",
+            "issued": "2015-06-01",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/f77z-wtsx",
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
+            "title": "State Drug Utilization Data 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rv55-x8ff",
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
-            "identifier": "https://data.cdc.gov/api/views/rv55-x8ff",
             "description": "Information on radiographic evidence of coal workers\u2019 pneumoconiosis (CWP) is presented for a group of 3,194 underground bituminous coal miners and ex-miners examined between 1985 and 1988. Prevalence of CWP was related to estimated cumulative dust exposure, age, and rank of coal. On the basis of these data, miners of medium to low rank coal, who work for 40 years at the current federal dust limit of 2 mg/m3, are predicted to have a 1.4% risk of having progressive massive fibrosis on retirement. Higher prevalences are predicted for less severe categories of CWP. Miners in high rank coal areas appear to be at greater risk than those mining medium and low rank coals. Ex-miners who said that they left mining for health-related reasons had higher levels of abnormality compared to current miners.",
-            "title": "Prevalence of Pneumoconiosis and its Relationship to Dust Exposure in a Cohort of U.S. Bituminous Coal Miners and ex-Miners",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64557,20 +64544,46 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rv55-x8ff",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.cdc.gov/d/rv55-x8ff",
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
+            "title": "Prevalence of Pneumoconiosis and its Relationship to Dust Exposure in a Cohort of U.S. Bituminous Coal Miners and ex-Miners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2001",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2001) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2001-nid13580",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2001-nid13580"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2001-nid13580",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -64583,40 +64596,32 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2001",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2001-nid13580",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2001)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2001-nid13580",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2001) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2001-nid13580"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2001)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/association-university-centers-disabilities-aucd-network-national-information-and-reporting",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Corina Miclea",
+                "hasEmail": "mailto:cmiclea@aucd.org"
+            },
+            "dataQuality": true,
+            "description": "<p>A searchable, web-based tool for accessing data on AUCD training programs, projects, activities, and products.  Includes data on the University Center for Excellence in Developmental Disabilities (UCEDD) and Leadership Education in Neurodevelopmental and related Disabilities (LEND) programs.</p>",
+            "identifier": "165fd4ab-65d6-48e3-a1bb-52216d5f9660",
             "issued": "2014-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "children's health",
                 "fihet",
@@ -64624,70 +64629,42 @@
                 "population statistics",
                 "social determinates of health"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Corina Miclea",
-                "hasEmail": "mailto:cmiclea@aucd.org"
-            },
+            "landingPage": "https://healthdata.gov/dataset/association-university-centers-disabilities-aucd-network-national-information-and-reporting",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:105"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Administration for Children and Families, Department of Health & Human Services"
             },
-            "identifier": "165fd4ab-65d6-48e3-a1bb-52216d5f9660",
-            "description": "<p>A searchable, web-based tool for accessing data on AUCD training programs, projects, activities, and products.  Includes data on the University Center for Excellence in Developmental Disabilities (UCEDD) and Leadership Education in Neurodevelopmental and related Disabilities (LEND) programs.</p>",
-            "title": "The Association of University Centers on Disabilities (AUCD) Network National Information and Reporting System (NIRS)",
-            "programCode": [
-                "009:105"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "The Association of University Centers on Disabilities (AUCD) Network National Information and Reporting System (NIRS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-model-participants",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2025-01-05/2025-01-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "references": [
-                "https://data.cms.gov/resources/model-participants-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/44e93e18-b9b3-4650-9471-2b1b31dc588b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/model-participants-data-dictionary",
             "description": "The Innovation Center Model Participants dataset contains information on current CMS Innovation Center models, demonstrations, initiatives, and programs. This can include the name of the initiative, organization name, location information, address, phase of participation, social media and website URLs, Metropolitan Statistical Area, categories related to health care quality, cost, payment, and delivery, among others. Information on past participants can be found below under resources.",
-            "title": "Innovation Center Model Participants",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/44e93e18-b9b3-4650-9471-2b1b31dc588b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/44e93e18-b9b3-4650-9471-2b1b31dc588b/data",
+                    "mediaType": "text/html",
                     "title": "Innovation Center Model Participants : 2025-01-17"
                 },
                 {
@@ -64703,42 +64680,52 @@
                     "title": "Innovation Center Model Participants : 2025-01-17"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/model-participants-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/44e93e18-b9b3-4650-9471-2b1b31dc588b/data-viewer",
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
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-model-participants",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/model-participants-methodology"
+            ],
+            "temporal": "2025-01-05/2025-01-11",
             "theme": [
                 "Medicare",
                 "Children's Health Insurance Program"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Innovation Center Model Participants"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/338g-fx72",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Protective Technology Branch (PTB), Division of Safety Research (DSR)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/338g-fx72",
             "description": "Top impacts are considered essential tests to evaluate the shock absorption performance of commonly used type I industrial helmets. Currently, there are two major test standards that are widely applied in helmet industry: ANSI/ISEA Z89.1 and EN397.  Since drop impacts are performed using different impactors and at drop heights, results obtained using different test standards are not directly comparable. The purpose of the current study is to evaluate and compare the helmet impact test results obtained using these two frequently used helmet test standards. A representative basic Type I construction helmet model was selected for the study. A total of 19 drop impact tests were performed at different drop heights and with two different impactors (3.6 kg and 5.0 kg). Group (a) contains 10 drop impacts performed using the 3.6 kg  impactor at drop heights from 0.31 m to 1.93 m. Group (b) contains 9 drop impacts performed using the 5.0 kg impactor at drop heights from 0.22 m to 1.32 m. Each of the impact trials was replicated four times. Relationships between the peak impact force and the drop height for these two test groups were analyzed and compared. When the helmets were tested with potential impact energy smaller than critical values, a consistent trend for the relationship of peak impact force as a function of the potential impact energy was obtained. Our results show that our previously proposed quantitative evaluation approach for industrial helmets\u2019 shock absorption performance can be used with either the ANSI/ISEA Z89.1 or EN395 standard to quantify industrial helmets\u2019 shock absorption performance. Furthermore, our results illustrated that the peak impact force would not be a reliable parameter to evaluate the helmets\u2019 safety margin.",
-            "title": "Testing the shock protection performance of Type I construction helmets using impactors of different masses",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64746,38 +64733,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/338g-fx72",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/338g-fx72",
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
+            "title": "Testing the shock protection performance of Type I construction helmets using impactors of different masses"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xml",
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
-            "identifier": "703b0166-e4c2-4c1e-b5d7-46f5f21acb12",
             "description": "This list includes products subject to recall in the United States since June 2009 related to products manufactured by Plainview Milk Products Cooperative.",
-            "title": "Plainview Milk Cooperative Ingredient Recall",
-            "programCode": [
-                "009:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64785,49 +64770,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "703b0166-e4c2-4c1e-b5d7-46f5f21acb12",
+            "issued": "2021-02-25",
+            "keyword": [
+                "recalls"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xml",
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
+            "title": "Plainview Milk Cooperative Ingredient Recall"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/pending-initial-logging-and-tracking-physicians",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/6bd6b1dd-208c-4f9c-88b8-b15fec6db548/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/pending-initial-logging-and-tracking-physician-and-non-physicians-data-dictionary",
             "description": "The Pending Initial Logging and Tracking\u00a0(L & T) Physicians dataset provides a list of pending applications that have not been processed by CMS contractors.",
-            "title": "Pending Initial Logging and Tracking Physicians",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6bd6b1dd-208c-4f9c-88b8-b15fec6db548/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6bd6b1dd-208c-4f9c-88b8-b15fec6db548/data",
+                    "mediaType": "text/html",
                     "title": "Pending Initial Logging and Tracking Physicians : 2025-01-21"
                 },
                 {
@@ -66895,31 +66875,62 @@
                     "title": "Pending Initial Logging and Tracking Physicians : 2023-06-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/pending-initial-logging-and-tracking-physician-and-non-physicians-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6bd6b1dd-208c-4f9c-88b8-b15fec6db548/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/pending-initial-logging-and-tracking-physicians",
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
+            "title": "Pending Initial Logging and Tracking Physicians"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/rdc/index.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-05-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2010-2017",
-            "modified": "2023-03-27",
-            "references": [
-                "https://www.cdc.gov/rdc/b1datatype/dt1229.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Arialdi Minino Domenech",
+                "hasEmail": "mailto:aminino@cdc.gov"
+            },
+            "describedBy": "Information derived from the textual entries in key data fields from death certificates issued by jurisdictions in the U.S.",
+            "description": "The Drug-Involved Mortality (DIM) data are an enhancement to the National Vital Statistics System, Mortality data providing information on substances, as well as prescription (using generic names only \u2013 no trademarks) and illicit drugs mentioned on death certificates of residents of the United States and the District of Columbia. Data files were created by examining the literal text of three fields on the death certificate:  Part I-Cause of Death, Part II \u2013Significant Conditions Contributing to Death and Box 43, a verbatim description of how the injury occurred. The DIM data system does not support individual examination of \u201cliteral text\u201d and the actual variables showing free-form text are not included in these files.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The Drug-Involved Mortality (DIM) data are an enhancement to the National Vital Statistics System, Mortality data providing information on substances, as well as prescription (using generic names only \u2013 no trademarks) and illicit drugs mentioned on death certificates of residents of the United States and the District of Columbia. Data files were created by examining the literal text of three fields on the death certificate:  Part I-Cause of Death, Part II \u2013Significant Conditions Contributing to Death and Box 43, a verbatim description of how the injury occurred. The DIM data system does not support individual examination of \u201cliteral text\u201d and the actual variables showing free-form text are not included in these files.",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "Drug-Involved Mortality (DIM) data available through the Research Data Center (RDC)"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/px5t-5gtx",
+            "isPartOf": "https://www.cdc.gov/nchs/nvss/deaths.htm",
+            "issued": "2022-05-31",
             "keyword": [
                 "deaths",
                 "drug overdose",
@@ -66927,66 +66938,40 @@
                 "injury",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Arialdi Minino Domenech",
-                "hasEmail": "mailto:aminino@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/rdc/index.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-03-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/px5t-5gtx",
-            "description": "The Drug-Involved Mortality (DIM) data are an enhancement to the National Vital Statistics System, Mortality data providing information on substances, as well as prescription (using generic names only \u2013 no trademarks) and illicit drugs mentioned on death certificates of residents of the United States and the District of Columbia. Data files were created by examining the literal text of three fields on the death certificate:  Part I-Cause of Death, Part II \u2013Significant Conditions Contributing to Death and Box 43, a verbatim description of how the injury occurred. The DIM data system does not support individual examination of \u201cliteral text\u201d and the actual variables showing free-form text are not included in these files.",
-            "title": "Drug-Involved Mortality (DIM) data available through the Research Data Center (RDC)",
-            "isPartOf": "https://www.cdc.gov/nchs/nvss/deaths.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "The Drug-Involved Mortality (DIM) data are an enhancement to the National Vital Statistics System, Mortality data providing information on substances, as well as prescription (using generic names only \u2013 no trademarks) and illicit drugs mentioned on death certificates of residents of the United States and the District of Columbia. Data files were created by examining the literal text of three fields on the death certificate:  Part I-Cause of Death, Part II \u2013Significant Conditions Contributing to Death and Box 43, a verbatim description of how the injury occurred. The DIM data system does not support individual examination of \u201cliteral text\u201d and the actual variables showing free-form text are not included in these files.",
-                    "@type": "dcat:Distribution",
-                    "title": "Drug-Involved Mortality (DIM) data available through the Research Data Center (RDC)"
-                }
+            "references": [
+                "https://www.cdc.gov/rdc/b1datatype/dt1229.html"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "Information derived from the textual entries in key data fields from death certificates issued by jurisdictions in the U.S.",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2010-2017",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Drug-Involved Mortality (DIM) data available through the Research Data Center (RDC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/faqw-p9fj",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-13",
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
-            "identifier": "4b1d87f3-f0dc-4e21-98c0-9c9d98724f1c",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-06-to-2023-03-12",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66995,55 +66980,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-06-to-2023-03-12"
                 }
             ],
+            "identifier": "4b1d87f3-f0dc-4e21-98c0-9c9d98724f1c",
+            "issued": "2023-03-28",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/faqw-p9fj",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-03-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-03-06-to-2023-03-12"
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
-            "identifier": "https://data.cdc.gov/api/views/dmzy-x2ad",
             "description": "Data on delay or nonreceipt of needed medical care, nonreceipt of needed prescription drugs, or nonreceipt of needed dental care during the past 12 months due to cost by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health Interview Survey, Family Core, Sample Child, and Sample Adult questionnaires. Data for level of difficulty are from the 2010 Quality of Life, 2011-2017 Functioning and Disability, and 2018 Sample Adult questionnaires. For more information on the National Health Interview Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Delay or nonreceipt of needed medical care, prescription drugs, or dental care during the past 12 months due to cost: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67066,94 +67032,106 @@
                     "mediaType": "application/xml"
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
-            "landingPage": "https://healthdata.gov/d/fats-pywh",
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
-            "identifier": "3380bed6-24ce-568e-982c-99951e1d7db0",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_files_topicSnapshot",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_topicSnapshot.csv",
-                    "description": "{\"dataset\": \"files_topicSnapshot\", \"stage\": \"devAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_topicSnapshot\", \"stage\": \"devAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_topicSnapshot.csv",
+                    "mediaType": "text/csv",
                     "title": "files_topicSnapshot csv file"
                 }
             ],
+            "identifier": "3380bed6-24ce-568e-982c-99951e1d7db0",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/fats-pywh",
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
+            "title": "devAuto_files_topicSnapshot"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xssa-9qw5",
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
-            "identifier": "https://data.cdc.gov/api/views/xssa-9qw5",
             "description": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67176,38 +67154,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xssa-9qw5",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "rubella congenital syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xssa-9qw5",
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
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fc8e-phkt",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-03-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
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
-            "identifier": "b5ce96db-36b4-4f1e-8db8-6fe88322360f",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-26-2024-to-03-03-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67216,44 +67201,38 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-26-2024-to-03-03-2024"
                 }
             ],
+            "identifier": "b5ce96db-36b4-4f1e-8db8-6fe88322360f",
+            "issued": "2024-03-09",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/fc8e-phkt",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-03-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-26-2024-to-03-03-2024"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -67262,59 +67241,62 @@
                     "title": "2004 National Nursing Home Survey - Restricted Facility Dataset"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/nnhsd/2004NNHS_DesignCollectionEstimates_072706tags.pdf",
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "None",
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
+            "title": "2004 National Nursing Home Survey - Restricted Facility Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/genome/viruses/retroviruses/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/37e3-hz3p",
             "description": "Information about retroviruses and specialized tools for the analysis of retroviral proteins and genomes. The tools on this page aid in the identification, study and analysis of retroviral genomes and proteins. For instance, the HIV, human interaction database catalogs and organizes published data in peer-reviewed journals regarding HIV-1 and human protein interactions. Several links external to NCBI are also included  for the purposes of education, research and health-related matters. These include links to the CDC, the Retroviruses textbook and other informative sites.",
-            "title": "Retrovirus Resources",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genome/viruses/retroviruses/hiv-1/interactions/",
-                    "description": "Information about known interactions of HIV-1 proteins with proteins from human hosts. It provides annotated bibliographies of published reports of protein interactions, with links to the corresponding PubMed records and sequence data.",
                     "@type": "dcat:Distribution",
+                    "description": "Information about known interactions of HIV-1 proteins with proteins from human hosts. It provides annotated bibliographies of published reports of protein interactions, with links to the corresponding PubMed records and sequence data.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genome/viruses/retroviruses/hiv-1/interactions/",
+                    "mediaType": "text/html",
                     "title": "HIV-1 Human Interaction Database"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/projects/genotyping/formpage.cgi",
-                    "description": "This tool helps identify the genotype of a viral sequence. A window is slid along the query sequence and each window is compared by BLAST to each of the reference sequences for a particular virus. This approach is especially useful for the analysis of recombinant sequences",
                     "@type": "dcat:Distribution",
+                    "description": "This tool helps identify the genotype of a viral sequence. A window is slid along the query sequence and each window is compared by BLAST to each of the reference sequences for a particular virus. This approach is especially useful for the analysis of recombinant sequences",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/projects/genotyping/formpage.cgi",
+                    "mediaType": "text/html",
                     "title": "Retrovirus genotyping tool"
                 },
                 {
@@ -67348,91 +67330,87 @@
                     "title": "Retrovirus taxonomy browser"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/37e3-hz3p",
+            "issued": "2021-08-26",
+            "keyword": [
+                "dataset",
+                "tools & utilities",
+                "virus"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genome/viruses/retroviruses/",
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
+            "title": "Retrovirus Resources"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fcvk-9npu",
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
-            "identifier": "c57ee71b-bbf2-5406-aef4-3ac15f0554ce",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure v2.10.64 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
-                    "description": "CoreSet measure v2.10.64 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure v2.10.64 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure v2.10.64 (coreset-dev)"
                 }
             ],
+            "identifier": "c57ee71b-bbf2-5406-aef4-3ac15f0554ce",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/fcvk-9npu",
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
+            "title": "CoreSet measure v2.10.64 (coreset-dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DASH Public Inquiries",
                 "hasEmail": "mailto:nccddashinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/q6p7-56au",
+            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/q6p7-56au",
             "description": "2015-2017. High School Dataset \u2013 Including Sexual Orientation. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors\r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and\r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human\r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors\r\nthe prevalence of obesity and asthma and other priority health behaviors.  This dataset contains national, state, and local data from 2015 that includes two aspects of sexual orientation \u2013 sexual identity and sex of sexual contacts.  Additional information about the YRBSS can be found at www.cdc.gov/yrbss.",
-            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School \u2013  Including Sexual Orientation",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67455,42 +67433,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/q6p7-56au",
+            "identifier": "https://data.cdc.gov/api/views/q6p7-56au",
+            "issued": "2023-07-14",
+            "keyword": [
+                "high school",
+                "risk behavior",
+                "sexual contacts",
+                "sexual identity",
+                "sexual orientation",
+                "survey",
+                "youth online",
+                "yrbs"
+            ],
+            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School \u2013  Including Sexual Orientation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/372p-dx3h",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-07-25",
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
-            "identifier": "https://data.cdc.gov/api/views/372p-dx3h",
             "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2011-2014. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.",
-            "title": "Daily Census Tract-Level Ozone Concentrations, 2011-2014",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67513,47 +67494,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/372p-dx3h",
+            "issued": "2018-07-25",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "ozone"
+            ],
+            "landingPage": "https://data.cdc.gov/d/372p-dx3h",
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
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2011-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/y4ut-ybj7",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "confirmed",
-                "hepatitis b",
-                "hepatitis c acute",
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
-            "identifier": "https://data.cdc.gov/api/views/y4ut-ybj7",
             "description": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 For acute Hepatitis C, only confirmed cases were verified.",
-            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67576,46 +67551,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y4ut-ybj7",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "confirmed",
+                "hepatitis b",
+                "hepatitis c acute",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
+                "probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/y4ut-ybj7",
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
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider-and-service",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-05-08",
-            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-06",
-            "keyword": [
-                "100 diagnosis-related groups  drg",
-                "cms",
-                "health care providers",
-                "hospital referral region  hrr",
-                "inpatient",
-                "ipps",
-                "medicare",
-                "state"
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
-            "identifier": "bed9c757-f144-49eb-95ef-f8e01224a1ee",
+            "dataQuality": true,
             "description": "<p>A provider level summary of Inpatient Prospective Payment System (IPPS) discharges, average charges and average Medicare payments for the Top 100 Diagnosis-Related Groups (DRG)</p>",
-            "title": "Inpatient Prospective Payment System (IPPS) Provider Summary for the Top 100 Diagnosis-Related Groups (DRG)",
-            "programCode": [
-                "009:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67630,43 +67607,46 @@
                     "title": "CSV "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "bed9c757-f144-49eb-95ef-f8e01224a1ee",
+            "issued": "2013-05-08",
+            "keyword": [
+                "100 diagnosis-related groups  drg",
+                "cms",
+                "health care providers",
+                "hospital referral region  hrr",
+                "inpatient",
+                "ipps",
+                "medicare",
+                "state"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-provider-and-service",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-09-06",
+            "programCode": [
+                "009:078"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
             "theme": [
                 "Community"
-            ]
+            ],
+            "title": "Inpatient Prospective Payment System (IPPS) Provider Summary for the Top 100 Diagnosis-Related Groups (DRG)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "temporal": "2002-11-01/2013-11-01",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-01",
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
-            "identifier": "5291f6b2-f62a-4498-a640-0639d94ec3c6",
             "description": "This database contains a list of classified medical device recalls since November 1, 2002",
-            "title": "Recalls of Medical Devices",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67674,18 +67654,51 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "5291f6b2-f62a-4498-a640-0639d94ec3c6",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
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
+                "http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm329946.htm"
+            ],
+            "temporal": "2002-11-01/2013-11-01",
+            "title": "Recalls of Medical Devices"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-online-tuberculosis-information-system-otis-0",
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
+            "description": "<p>The Online Tuberculosis Information System (OTIS) on CDC WONDER contains information on verified tuberculosis (TB) cases reported to the Centers for Disease Control and Prevention (CDC) by state health departments, the District of Columbia and Puerto Rico since 1993.  These data were extracted from the CDC national TB surveillance system.  OTIS reports case counts, incidence rates, population counts, percentage of cases that completed therapy within 1 year of diagnosis, and percentage of cases tested for drug susceptibility.  Data for 22 variables are included in the data set, including:  age groups, race / ethnicity, sex, vital status, year reported, state, metropolitan area, several patient risk factors, directly observed therapy, disease verification criteria and multi-drug resistant TB.   Each year these data are updated with an additional year of cases plus revisions to cases reported in previous years.   OTIS is produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/tb.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "e68f8a49-eae3-41b8-8b03-0f02d0167fcf",
             "issued": "2012-05-30",
-            "temporal": "1993-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "age",
                 "alcohol use",
@@ -67714,66 +67727,34 @@
                 "vital status",
                 "year"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-online-tuberculosis-information-system-otis-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "e68f8a49-eae3-41b8-8b03-0f02d0167fcf",
-            "description": "<p>The Online Tuberculosis Information System (OTIS) on CDC WONDER contains information on verified tuberculosis (TB) cases reported to the Centers for Disease Control and Prevention (CDC) by state health departments, the District of Columbia and Puerto Rico since 1993.  These data were extracted from the CDC national TB surveillance system.  OTIS reports case counts, incidence rates, population counts, percentage of cases that completed therapy within 1 year of diagnosis, and percentage of cases tested for drug susceptibility.  Data for 22 variables are included in the data set, including:  age groups, race / ethnicity, sex, vital status, year reported, state, metropolitan area, several patient risk factors, directly observed therapy, disease verification criteria and multi-drug resistant TB.   Each year these data are updated with an additional year of cases plus revisions to cases reported in previous years.   OTIS is produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
-            "title": "CDC WONDER: Online Tuberculosis Information System (OTIS)",
-            "programCode": [
-                "009:053"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/tb.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/tb.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1993-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Online Tuberculosis Information System (OTIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/85gd-bw4a",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/85gd-bw4a",
             "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Update (All Fields) Report lists each individual modification made to a Descriptor or Supplementary Concept Record (SCR).  More than one field on a term can be modified during YEP, resulting in a term having multiple entries on the list.  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
-            "title": "MeSH 2025 Update - Update All Fields Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67796,50 +67777,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/85gd-bw4a",
+            "issued": "2023-12-14",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/85gd-bw4a",
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
+            "title": "MeSH 2025 Update - Update All Fields Report"
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
-                "adults",
-                "brfss",
-                "dnpao",
-                "fruit",
-                "nutrition",
-                "obesity",
-                "overweight",
-                "physical activity",
-                "vegetables",
-                "walking"
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
-            "identifier": "https://data.cdc.gov/api/views/hn4x-zwk7",
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Behavioral/hn4x-zwk7",
             "description": "This dataset includes data on adult's diet, physical activity, and weight status from Behavioral Risk Factor Surveillance System. This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding.",
-            "title": "Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67862,49 +67835,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Behavioral/hn4x-zwk7",
+            "identifier": "https://data.cdc.gov/api/views/hn4x-zwk7",
+            "issued": "2025-01-30",
+            "keyword": [
+                "adults",
+                "brfss",
+                "dnpao",
+                "fruit",
+                "nutrition",
+                "obesity",
+                "overweight",
+                "physical activity",
+                "vegetables",
+                "walking"
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
+            "title": "Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System"
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
-            "modified": "2024-05-13",
-            "references": [
-                "https://chronicdata.cdc.gov/d/sgg4-hiwe"
-            ],
-            "keyword": [
-                "office on smoking and health",
-                "osh",
-                "policy",
-                "state system",
-                "tobacco",
-                "tobacco settlement payments"
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
-            "identifier": "https://data.cdc.gov/api/views/ffbi-is3j",
+            "describedBy": "https://chronicdata.cdc.gov/Policy/NAAG-Tobacco-Settlement-Payments/ffbi-is3j",
             "description": "1999-2024. National Association of Attorneys General (NAAG). Policy\u2014Tobacco Settlement Payments. The National Association of Attorneys General (NAAG) provides Tobacco Settlement Revenue data for 46 states participating in the Master Settlement Agreement (MSA) with the four largest tobacco companies in the United States.  Data are reported on an annual basis.  Four states (Florida, Minnesota, Mississippi, and Texas) provide the STATE System their Tobacco Settlement Revenue data independently.",
-            "title": "NAAG Tobacco Settlement Payments",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67927,42 +67904,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Policy/NAAG-Tobacco-Settlement-Payments/ffbi-is3j",
+            "identifier": "https://data.cdc.gov/api/views/ffbi-is3j",
+            "issued": "2023-07-14",
+            "keyword": [
+                "office on smoking and health",
+                "osh",
+                "policy",
+                "state system",
+                "tobacco",
+                "tobacco settlement payments"
+            ],
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2024-05-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "https://chronicdata.cdc.gov/d/sgg4-hiwe"
+            ],
             "theme": [
                 "Policy"
-            ]
+            ],
+            "title": "NAAG Tobacco Settlement Payments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fiep-96bi",
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
-                "py2024",
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
-            "identifier": "5c232812-fc30-4dd7-8af7-015ce0073eb8",
             "description": "The Transparency in Coverage PUF (TC-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The PUF contains data on issuer and plan-level claims, appeals, and active URL data. The PY2024 PUF contains data from PY2022 for issuers participating in the Exchanges in PY2022.",
-            "title": "Transparency in Coverage PUF - PY2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67970,51 +67952,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "5c232812-fc30-4dd7-8af7-015ce0073eb8",
+            "issued": "2024-10-11",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2024",
+                "transparency in coverage"
+            ],
+            "landingPage": "https://healthdata.gov/d/fiep-96bi",
+            "modified": "2024-10-24",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Transparency in Coverage PUF - PY2024"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -68037,86 +68006,97 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://repository.niddk.nih.gov/home/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-18",
-            "keyword": [
-                "national-institutes-of-health-nih"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rodriguez, Rebecca",
                 "hasEmail": "mailto:niddk-crsupport@niddk.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "ad6250c9-72ec-4581-9883-45012df72b4e",
+            "dataQuality": true,
             "description": "<p>The NIDDK Central Repository stores biosamples, genetic and other data collected in designated NIDDK-funded clinical studies. The purpose of the NIDDK Central Repository is to expand the usefulness of these studies by allowing a wider research community to access data and materials beyond the end of the study.</p>",
-            "title": "NIDDK Central Repository",
+            "identifier": "ad6250c9-72ec-4581-9883-45012df72b4e",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "https://repository.niddk.nih.gov/home/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-08-18",
             "programCode": [
                 "009:110"
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
+            "title": "NIDDK Central Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/medicare-value-based-payment-modifier-program/value-modifier",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2016-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-06",
-            "references": [
-                "https://data.cms.gov/resources/2018-value-modifier-performance-year-2016-methodology"
-            ],
-            "keyword": [
-                "medicare",
-                "original medicare",
-                "payment models",
-                "value-based care"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/c3e8e9c3-5193-47fb-a5bb-d3ddb00e7197/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/value-modifier-data-dictionary",
             "description": "The Medicare Value-Based Payment Modifier (Value Modifier) data contains the performance results of de-identified practices that were subject to the Value Modifier, such as the practices' quality and cost tiers along with any applicable Value Modifier payment adjustment. The Value Modifier provided\u00a0for differential payment under the Medicare Physician Fee Schedule based on the quality of care furnished to Medicare beneficiaries compared to the cost of care during a performance period. Calendar Year 2015 was the first payment adjustment period under the Value Modifier based on performance in 2013. Calendar Year 2018 was the final payment adjustment period under the Value Modifier based on performance in 2016.\u00a0\n\n\u00a0\n\nThe Merit-based Incentive Payment System (MIPS) under the Quality Payment Program has replaced the Value Modifier program. The Centers for Medicare & Medicaid Services (CMS) encourages everyone to learn more about the Quality Payment Program.\u00a0",
-            "title": "Value Modifier",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c3e8e9c3-5193-47fb-a5bb-d3ddb00e7197/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c3e8e9c3-5193-47fb-a5bb-d3ddb00e7197/data",
+                    "mediaType": "text/html",
                     "title": "Value Modifier : 2016-12-31"
                 },
                 {
@@ -68168,54 +68148,48 @@
                     "title": "Value Modifier : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/value-modifier-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c3e8e9c3-5193-47fb-a5bb-d3ddb00e7197/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/medicare-value-based-payment-modifier-program/value-modifier",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2021-01-06",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/2018-value-modifier-performance-year-2016-methodology"
+            ],
+            "temporal": "2013-01-01/2016-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Value Modifier"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/65xe-6neq",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
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
-            "identifier": "https://data.cdc.gov/api/views/65xe-6neq",
             "description": "NNDSS - Table II. Hepatitis (viral, acute) - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Hepatitis (viral, acute)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68238,39 +68212,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/65xe-6neq",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
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
+            "landingPage": "https://data.cdc.gov/d/65xe-6neq",
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
+            "title": "NNDSS - Table II. Hepatitis (viral, acute)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/population-groups.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-14",
-            "@type": "dcat:Dataset",
-            "temporal": "2002-01-01/2018-12-31",
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
-            "identifier": "https://data.cdc.gov/api/views/3q3z-9ucr",
             "description": "[1] The Progress by Population Group analysis is a component of the Healthy People 2020 (HP2020) Final Review. The analysis included subsets of the 1,111 measurable HP2020 objectives that have data available for any of six broad population characteristics: sex, race and ethnicity, educational attainment, family income, disability status, and geographic location. Progress toward meeting HP2020 targets is presented for up to 24 population groups within these characteristics, based on objective data aggregated across HP2020 topic areas. The Progress by Population Group data are also available at the individual objective level in the downloadable data set. \n[2] The final value was generally based on data available on the HP2020 website as of January 2020. For objectives that are continuing into HP2030, more recent data will be included on the HP2030 website as it becomes available: https://health.gov/healthypeople.\n[3] For more information on the HP2020 methodology for measuring progress toward target attainment and the elimination of health disparities, see: Healthy People Statistical Notes, no 27; available from: https://www.cdc.gov/nchs/data/statnt/statnt27.pdf.\n[4] Status for objectives included in the HP2020 Progress by Population Group analysis was determined using the baseline, final, and target value. The progress status categories used in HP2020 were:\n\na. Target met or exceeded\u2014One of the following applies: (i) At baseline, the target was not met or exceeded, and the most recent value was equal to or exceeded the target (the percentage of targeted change achieved was equal to or greater than 100%); (ii) The baseline and most recent values were equal to or exceeded the target (the percentage of targeted change achieved was not assessed). \n\nb. Improved\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved 10% or more of the targeted change.\n\nc. Little or no detectable change\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was not statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved less than 10% of the targeted change; (iii) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was not statistically significant; (iv) Movement was away from the baseline and target, standard errors were not available, and the objective had moved less than 10% relative to the baseline; (v) No change was observed between the baseline and the final data point.\n\nd. Got worse\u2014One of the following applies: (i) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was statistically significant; (ii) Movement was away from the baseline and target, standard errors were not available, and the objective had moved 10% or more relative to the baseline.\n\nNOTE: Measurable objectives had baseline data.\nSOURCE: National Center for Health Statistics, Healthy People 2020 Progress by Population Group database.",
-            "title": "Healthy People 2020 Final Progress by Population Group Chart and Table",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68293,46 +68277,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/3q3z-9ucr",
+            "issued": "2021-09-14",
+            "keyword": [
+                "healthy people 2020"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/population-groups.htm",
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
+            "temporal": "2002-01-01/2018-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Healthy People 2020 Final Progress by Population Group Chart and Table"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/yviw-z6j5",
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
-                "covid-19",
-                "surveillance"
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
-            "identifier": "https://data.cdc.gov/api/views/yviw-z6j5",
             "description": "<b>Note:</b> \nThe cumulative case count for some counties (with small population) is higher than expected due to the inclusion of non-permanent residents in COVID-19 case counts. \n\nReporting of Aggregate Case and Death Count data was discontinued on May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\n<b>Aggregate Data Collection Process\nSince the beginning of the COVID-19 pandemic, data were reported through a robust process with the following steps:</b><ul><li>Aggregate county-level counts were obtained indirectly, via automated overnight web collection, or directly, via a data submission process.</li><li>If more than one official county data source existed, CDC used a comprehensive data selection process comparing each official county data source to retrieve the highest case and death counts, unless otherwise specified by the state.</li><li>A CDC data team reviewed counts for congruency prior to integration. CDC routinely compiled these data and post the finalized information on COVID Data Tracker.</li><li>Cases and deaths are based on date of report and not on the date of symptom onset. CDC calculates rates in this data by using population estimates provided by the US Census Bureau Population Estimates Program (2019 Vintage).</li><li>COVID-19 aggregate case and death data were organized in a time series that includes cumulative number of cases and deaths as reported by a jurisdiction on a given date.  New case and death counts were calculated as the week-to-week change in reported cumulative cases and deaths (i.e., newly reported cases and deaths = cumulative number of cases/deaths reported this week minus the cumulative total reported the week before.</li></ul>\n\nThis process was collaborative, with CDC and jurisdictions working together to ensure the accuracy of COVID-19 case and death numbers. County counts provided the most up-to-date numbers on cases and deaths by report date. Throughout data collection, CDC retrospectively updated counts to correct known data quality issues. CDC also worked with jurisdictions after the end of the public health emergency declaration to finalize county data. \n<ul><li><b>Source:</b> The weekly archived dataset is based on county-level aggregate count data</li><li><b>Confirmed/Probable Cases/Death breakdown:</b> Cumulative cases and deaths for each county are included.  Total reported cases include probable and confirmed cases.</li><li><b>Time Series Frequency:</b> The weekly archived dataset contains weekly time series data (i.e., one record per week per county)</li></ul>\n \n<b>Important note:</b> The counts reflected during a given time period in this dataset may not match the counts reflected for the same time period in the daily archived dataset noted above. Discrepancies may exist due to differences between county and state COVID-19 case surveillance and reconciliation efforts.\n\nThe surveillance case definition for COVID-19, a nationally notifiable disease, was first described in a <a href=\"https://ndc.services.cdc.gov/case-definitions/coronavirus-disease-2019-covid-19/\">position statement</a> from the Council for State and Territorial Epidemiologists, which was later <a href=\"https://ndc.services.cdc.gov/case-definitions/coronavirus-disease-2019-covid-19/\">revised</a>. However, there is some variation in how jurisdictions implement these case classifications. More information on how CDC collects COVID-19 case surveillance data can be found at <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\">FAQ: COVID-19 Data and Surveillance</a>.\n\n<b>Confirmed and Probable Counts</b>\nIn this dataset, counts by jurisdiction are not displayed by confirmed or probable status. Instead, counts of confirmed and probable cases and deaths are included in the Total Cases and Total Deaths columns, when available. Not all jurisdictions report",
-            "title": "Weekly United States COVID-19 Cases and Deaths by County - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68355,40 +68337,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/yviw-z6j5",
+            "issued": "2023-06-06",
+            "keyword": [
+                "covid",
+                "covid-19",
+                "surveillance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/yviw-z6j5",
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
+            "title": "Weekly United States COVID-19 Cases and Deaths by County - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fjmx-xmbz",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-17",
-            "keyword": [
-                "py2022",
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
-            "identifier": "385f17c1-f03d-4927-947d-854cfcd07c00",
             "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2022 Medical SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68396,80 +68377,81 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "385f17c1-f03d-4927-947d-854cfcd07c00",
+            "issued": "2022-08-10",
+            "keyword": [
+                "py2022",
+                "qhp",
+                "qhp landscape instructions",
+                "shop",
+                "shop market medical"
+            ],
+            "landingPage": "https://healthdata.gov/d/fjmx-xmbz",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2022 Medical SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ahrq.gov/data/innovations/3p-rd.html",
             "bureauCode": [
                 "009:00"
             ],
-            "rights": "Restricted-Use Files also available",
-            "issued": "2023-09-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-15",
-            "keyword": [
-                "physician",
-                "physician practice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "3P-RD help desk",
                 "hasEmail": "mailto:3P-RD@ahrq.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Agency for Healthcare Research and Quality"
-            },
-            "identifier": "https://healthdata.gov/api/views/fk2u-ctai",
             "description": "The Physician and Physician Practice Research Database (3P-RD) captures characteristics of physicians and physician practices in 13 states. The database describes the supply of physician services available across selected states for data year 2019-2020.",
-            "title": "Physician and Physician Practice Research Database (3P-RD)",
-            "programCode": [
-                "009:074"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ahrq.gov/data/innovations/3p-rd.html",
-                    "description": "The Physician and Physician Practice Research Database (3P-RD) captures characteristics of physicians and physician practices in 13 states. The database describes the supply of physician services available across selected states for data year 2019-2020. AHRQ created 3P-RD as a resource to address existing data gaps in physician health services information at the state and market levels. \n\n3P-RD consists of both public use and restricted use data files. The public use file (PUF) version of 3P-RD is currently available for download. The Restricted Use File (RUF) version of 3P-RD will be available for each state. Once the data are released, a data use agreement (DUA) will be required for access to the data files.",
                     "@type": "dcat:Distribution",
+                    "description": "The Physician and Physician Practice Research Database (3P-RD) captures characteristics of physicians and physician practices in 13 states. The database describes the supply of physician services available across selected states for data year 2019-2020. AHRQ created 3P-RD as a resource to address existing data gaps in physician health services information at the state and market levels. \n\n3P-RD consists of both public use and restricted use data files. The public use file (PUF) version of 3P-RD is currently available for download. The Restricted Use File (RUF) version of 3P-RD will be available for each state. Once the data are released, a data use agreement (DUA) will be required for access to the data files.",
+                    "downloadURL": "https://www.ahrq.gov/data/innovations/3p-rd.html",
+                    "mediaType": "text/html",
                     "title": "Physician and Physician Practice Research Database (3P-RD)"
                 }
             ],
+            "identifier": "https://healthdata.gov/api/views/fk2u-ctai",
+            "issued": "2023-09-15",
+            "keyword": [
+                "physician",
+                "physician practice"
+            ],
+            "landingPage": "https://www.ahrq.gov/data/innovations/3p-rd.html",
+            "modified": "2023-09-15",
+            "programCode": [
+                "009:074"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality"
+            },
+            "rights": "Restricted-Use Files also available",
             "spatial": "13 states (AR, AZ, CA, CO, FL, MA, MD, MN, MO, MT, NY, TX, WA)",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "Physician and Physician Practice Research Database (3P-RD)"
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
-            "identifier": "https://data.cdc.gov/api/views/akkj-j5ru",
             "description": "National Immunization Survey-Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent by week for the national-level view, and by month for the jurisdiction-level view.",
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Trends in Vaccination Status and Intent",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68492,44 +68474,41 @@
                     "mediaType": "application/xml"
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
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Trends in Vaccination Status and Intent"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fkfr-fp4z",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-11-27",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "keyword": [
-                "child enrollment",
-                "chip",
-                "eligibility determinations",
-                "enrollment",
-                "medicaid",
-                "program enrollment",
-                "renewals"
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
-            "identifier": "5abea2e0-3f8e-4b49-a50d-d63d5fd9103c",
             "description": "All states (including the District of Columbia) provide data to the Centers for Medicare & Medicaid Services (CMS) on a range of Medicaid and Children\u2019s Health Insurance Program (CHIP) eligibility and enrollment metrics. These data reflect state-reported information on Medicaid and CHIP eligibility renewals initiated and scheduled for completion during the reporting period. In addition to reporting the outcomes of renewals at the end of each reporting period, states also provide an update on renewals that were reported pending as of the end of a reporting period. For more information on these data, see Sections II and III of the <a href=\"https://www.medicaid.gov/resources-for-states/downloads/eligibility-processing-data-specs-august-2024.pdf\">Eligibility Processing Data Report specifications</a>. <br/>\r\n<b>Notes:</b><br/> Georgia reported data for individuals who continue to be eligible following a change in circumstances and were granted a new 12-month eligibility period during the reporting period, along with data on individuals due for renewal in the month.<br/>\r\nNorth Carolina reports renewal outcomes for only initiated renewals scheduled for completion in the report month, and as such, the data do not reflect renewals that should have been completed in the reporting period that the state was unable to initiate by the end of the report month.",
-            "title": "State Medicaid and CHIP Eligibility Processing Data",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68537,36 +68516,45 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "5abea2e0-3f8e-4b49-a50d-d63d5fd9103c",
+            "issued": "2024-11-27",
+            "keyword": [
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
+                "medicaid",
+                "program enrollment",
+                "renewals"
+            ],
+            "landingPage": "https://healthdata.gov/d/fkfr-fp4z",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "State Medicaid and CHIP Eligibility Processing Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/resp-net/dashboard/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-05-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RESP-NET",
                 "hasEmail": "mailto:CovidRSV-Net@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/kvib-3txy",
             "description": "The Respiratory Virus Hospitalization Surveillance Network (RESP-NET) is a network that conducts, active, population-based surveillance for laboratory confirmed hospitalizations associated with Influenza, COVID-19, and RSV. The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. Hospitalization rates show how many people in the surveillance area are hospitalized with influenza, COVID-19, and RSV compared to the total number of people residing in that area. \n\nData will be updated weekly. Data are preliminary and subject to change as more data become available.",
-            "title": "Rates of Laboratory-Confirmed RSV, COVID-19, and Flu Hospitalizations from the RESP-NET Surveillance Systems",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68589,41 +68577,36 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "RESP-NET Sites",
+            "identifier": "https://data.cdc.gov/api/views/kvib-3txy",
+            "issued": "2024-05-03",
+            "landingPage": "https://www.cdc.gov/resp-net/dashboard/index.html",
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
+            "spatial": "RESP-NET Sites",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Rates of Laboratory-Confirmed RSV, COVID-19, and Flu Hospitalizations from the RESP-NET Surveillance Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://jats.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "data standards",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/77jt-4tze",
             "description": "Journal Article Tag Suite (JATS) is an application of NISO Z39.96.2019, which defines a set of XML elements and attributes for describing the textual and graphical content of journal articles and describes three article models.",
-            "title": "Journal Article Tag Suite (JATS)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68632,49 +68615,42 @@
                     "title": "Journal Article Tag Suite (JATS) Homepage"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/77jt-4tze",
+            "issued": "2022-02-08",
+            "keyword": [
+                "data standards",
+                "tools & utilities"
+            ],
+            "landingPage": "https://jats.nlm.nih.gov/",
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
+            "title": "Journal Article Tag Suite (JATS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-home-health-agency",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "references": [
-                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "home health",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/b8135181-4274-4a11-a6cd-992090297ef5/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The Medicare Home Health Agency tables provide use and payment data for home health agencies. The tables include use and expenditure data from home health Part A (Hospital Insurance) and Part B (Medical Insurance) claims.\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR HHA 1. \u00a0Medicare Home Health Agencies: \u00a0Utilization and\u00a0Program Payments for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR HHA 2. \u00a0Medicare Home Health Agencies: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR HHA 3. \u00a0Medicare Home Health Agencies: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR HHA 4. \u00a0Medicare Home Health Agencies: \u00a0Persons with Utilization and Total Service Visits for Original Medicare Beneficiaries, Type of Agency and Type of Service Visit\n\tMDCR HHA 5. \u00a0Medicare Home Health Agencies: \u00a0Persons with Utilization and Total Service Visits for Original Medicare Beneficiaries, by Type of Control and Type of Service Visit\n\tMDCR HHA 6. \u00a0Medicare Home Health Agencies: \u00a0Persons with Utilization, Total Service Visits, and Program Payments for Original Medicare Beneficiaries, by Number of Service Visits and Number of Episodes",
-            "title": "CMS Program Statistics - Medicare Home Health Agency",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68731,27 +68707,77 @@
                     "title": "CMS Program Statistics - Medicare Home Health Agency : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/b8135181-4274-4a11-a6cd-992090297ef5/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "home health",
+                "hospitals & facilities",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-home-health-agency",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-06-12",
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
+            "title": "CMS Program Statistics - Medicare Home Health Agency"
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
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional counts of deaths by the week the deaths occurred, by state of occurrence, and by select underlying causes of death for 2020-2023.  The dataset also includes weekly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.\n\nNOTE: death counts are presented with a one week lag.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/muzy-jte6",
             "issued": "2020-04-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-04/2023-07-22",
-            "modified": "2023-09-27",
             "keyword": [
                 "all causes",
                 "alzheimer disease",
@@ -68779,77 +68805,36 @@
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
-            "identifier": "https://data.cdc.gov/api/views/muzy-jte6",
-            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional counts of deaths by the week the deaths occurred, by state of occurrence, and by select underlying causes of death for 2020-2023.  The dataset also includes weekly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.\n\nNOTE: death counts are presented with a one week lag.",
-            "title": "Weekly Provisional Counts of Deaths by State and Select Causes, 2020-2023",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2020-01-04/2023-07-22",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Weekly Provisional Counts of Deaths by State and Select Causes, 2020-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fmc9-nsxa",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-09-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-12",
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
-            "identifier": "b3c30bd4-f3f9-496f-97ec-c5f9d8083ad0",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-04-to-2023-09-10",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68858,64 +68843,92 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-04-to-2023-09-10"
                 }
             ],
+            "identifier": "b3c30bd4-f3f9-496f-97ec-c5f9d8083ad0",
+            "issued": "2023-09-13",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/fmc9-nsxa",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-09-12",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-04-to-2023-09-10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fmd4-iw4i",
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
-            "identifier": "9285d2b8-866e-5760-ac92-c2628ac59e2e",
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
+            "identifier": "9285d2b8-866e-5760-ac92-c2628ac59e2e",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/fmd4-iw4i",
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
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2009",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug-related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 22 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network (DAWN-2009) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2009-nid13608",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2009-nid13608"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2009-nid13608",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "demographic characteristics",
@@ -68928,91 +68941,63 @@
                 "substance abuse",
                 "suicide"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2009",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2009-nid13608",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug-related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 22 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network (DAWN-2009)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2009-nid13608",
-                    "description": "Drug Abuse Warning Network (DAWN-2009) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2009-nid13608"
-                }
-            ]
+            "title": "Drug Abuse Warning Network (DAWN-2009)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.metabolomicsworkbench.org/",
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
                 "fn": "MARUVADA, PADMA\u00a0",
                 "hasEmail": "mailto:maruvadp@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "37d41112-7b13-4f93-9c6c-f6e0b12f979f",
+            "dataQuality": true,
             "description": "<p>The Metabolomics Program's Data Repository and Coordinating Center (DRCC), housed at the San Diego Supercomputer Center (SDSC), University of California, San Diego, has developed the Metabolomics Workbench. MetWB will serve as a national and international repository for metabolomics data and metadata and will provide analysis tools and access to metabolite standards, protocols, tutorials, training, and more.</p>",
-            "title": "Metabolomics Workbench (MetWB)",
+            "identifier": "37d41112-7b13-4f93-9c6c-f6e0b12f979f",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.metabolomicsworkbench.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:110"
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
+            "title": "Metabolomics Workbench (MetWB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/drugshortages/default.cfm",
+            "accrualPeriodicity": "R/P1W",
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
-            "identifier": "520f8f0d-b519-4ad9-8597-14d517f00987",
             "description": "Information provided to FDA by manufacturers about current drugs in shortage, resolved shortages, and discontinuations of specific drug products.",
-            "title": "Current and Resolved Drug Shortages and Discontinuations Reported to FDA",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69020,46 +69005,35 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "520f8f0d-b519-4ad9-8597-14d517f00987",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/drugshortages/default.cfm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1W"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Current and Resolved Drug Shortages and Discontinuations Reported to FDA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g6fu-zp23",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/g6fu-zp23",
             "description": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69082,47 +69056,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g6fu-zp23",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
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
+            "landingPage": "https://data.cdc.gov/d/g6fu-zp23",
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
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/keia-pvvn",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
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
-            "identifier": "https://data.cdc.gov/api/views/keia-pvvn",
             "description": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. \r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.   Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n \r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Please refer to the MMWR publication for weekly updates to the footnote for this condition.",
-            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69145,42 +69120,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/keia-pvvn",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
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
+            "landingPage": "https://data.cdc.gov/d/keia-pvvn",
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
+            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -69203,41 +69183,43 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cdc.gov/d/x9gk-5huc",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
-            "keyword": [
-                "2022",
-                "nndss",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NNDSS Team",
                 "hasEmail": "mailto:NNDSSWeb@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/x9gk-5huc",
             "description": "NNDSS - In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\n\nNotes:\n\n\u2022 These are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/infectious-disease/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data.\n\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page https://www.cdc.gov/nndss/infectious-disease/notice-to-data-users.html.\n\n\u2022 The list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2024 and 2025 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u2022 Please refer to the Stacks publication for weekly updates to the footnote for influenza-associated pediatric mortality.\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS Weekly Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69260,47 +69242,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x9gk-5huc",
+            "issued": "2022-01-18",
+            "keyword": [
+                "2022",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/x9gk-5huc",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-27",
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
+            "title": "NNDSS Weekly Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/52cr-rw4k",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "2014",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "salmonellosis",
-                "shiga toxin-producing e. coli",
-                "shigellosis",
-                "stec",
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
-            "identifier": "https://data.cdc.gov/api/views/52cr-rw4k",
             "description": "NNDSS - Table II. Salmonellosis to Shigellosis - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd\ufffd Includes E. coli O157:H7; Shiga toxin positive, serogroup non-O157; and Shiga toxin positive, not serogrouped.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Salmonellosis to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69323,40 +69298,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/52cr-rw4k",
+            "issued": "2015-01-08",
+            "keyword": [
+                "2014",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonellosis",
+                "shiga toxin-producing e. coli",
+                "shigellosis",
+                "stec",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/52cr-rw4k",
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
+            "title": "NNDSS - Table II. Salmonellosis to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://imagic.nlm.nih.gov/imagic/code/map",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "health data standards",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/7bij-avxu",
             "description": "I-MAGIC (Interactive Map-Assisted Generation of ICD Codes)  is an interactive tool to demonstrate how the SNOMED CT to ICD-10-CM map can be used to generate ICD-10-CM codes from clinical problems coded in SNOMED CT.",
-            "title": "I-MAGIC",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69365,91 +69347,86 @@
                     "title": " I-MAGIC Homepage and Search"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/7bij-avxu",
+            "issued": "2021-06-30",
+            "keyword": [
+                "health data standards",
+                "terminologies",
+                "tools & utilities"
+            ],
+            "landingPage": "https://imagic.nlm.nih.gov/imagic/code/map",
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
                 "Terminology"
-            ]
+            ],
+            "title": "I-MAGIC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fruh-rw7y",
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
-            "identifier": "abb567c0-42bd-5851-870e-8dad158d97e2",
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
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "abb567c0-42bd-5851-870e-8dad158d97e2",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/fruh-rw7y",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-            "landingPage": "https://data.cdc.gov/d/n835-hpyp",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
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
-            "identifier": "https://data.cdc.gov/api/views/n835-hpyp",
             "description": "NNDSS - Table II. Chlamydia to Coccidioidomycosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP:  Nationally notifiable but not published.  Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.",
-            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69472,35 +69449,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n835-hpyp",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
+                "chlamydia trachomatis infection",
+                "coccidioidomycosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n835-hpyp",
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
+            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/d29v-yfc2",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -69508,45 +69495,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/d29v-yfc2",
+            "issued": "2024-12-06",
+            "landingPage": "https://data.cdc.gov/d/d29v-yfc2",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-06",
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
+            "title": "Shoulder-Assist Exoskeleton Effects on Balance and Muscle Activity During a Block-laying Task on a Simulated Mast Climber"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -69569,41 +69546,45 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis"
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
-            "keyword": [
-                "osh",
-                "sam",
-                "sammec",
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
-            "identifier": "https://data.cdc.gov/api/views/4yyu-3s69",
             "description": "2005-2009. SAMMEC - Smoking-Attributable Mortality, Morbidity, and Economic Costs. Smoking-attributable mortality (SAM) is the number of deaths caused by cigarette smoking based on diseases for which the U.S. Surgeon General has determined that cigarette smoking is a causal factor.",
-            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Mortality (SAM)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69626,53 +69607,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/4yyu-3s69",
+            "issued": "2025-01-31",
+            "keyword": [
+                "osh",
+                "sam",
+                "sammec",
+                "tobacco"
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
             "theme": [
                 "Health Consequences and Costs"
-            ]
+            ],
+            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Mortality (SAM)"
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
-            "identifier": "https://data.cdc.gov/api/views/k25u-mg9b",
             "description": "2016, 2015. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census tract-level data in GIS-friendly format can be joined with census tract spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-Boundaries/x7zy-2xmx) in a geographic information system (GIS) to produce maps of 27 measures at the census tract level. There are 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, cholesterol screening) in this 2018 release from the 2015 BRFSS that were the same as the 2017 release.",
-            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2018 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69695,35 +69664,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/k25u-mg9b",
+            "issued": "2023-07-18",
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
+            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2018 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/c2hx-eeis",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -69731,42 +69718,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/c2hx-eeis",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/c2hx-eeis",
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
+            "title": "NIOSH Anthropometric Data and ISO Digital Headforms"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
+            "accrualPeriodicity": "Annually",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-04-10",
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
-            "identifier": "https://data.cdc.gov/api/views/fvm6-ic5r",
             "description": "The BEAM (Bacteria, Enterics, Amoeba, and Mycotics) Dashboard is an interactive tool to access and visualize data from the System for Enteric Disease Response, Investigation, and Coordination (SEDRIC). The BEAM Dashboard provides timely data on pathogen trends and serotype details to inform work to prevent illnesses from food and animal contact.",
-            "title": "BEAM Dashboard - Serotypes of concern: Illnesses and Outbreaks",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69789,57 +69770,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/fvm6-ic5r",
+            "issued": "2023-04-10",
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
+            "title": "BEAM Dashboard - Serotypes of concern: Illnesses and Outbreaks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-compliance/cost-report/home-health-agency-cost-report",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-12-15",
-            "temporal": "2020-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-25",
-            "references": [
-                "https://data.cms.gov/resources/home-health-agency-cost-report-methodology"
-            ],
-            "keyword": [
-                "financials",
-                "home health",
-                "hospitals & facilities",
-                "medicare",
-                "original medicare",
-                "value-based care"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/4999da74-1d8d-4a6f-934e-2d7ea470cc63/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/home-health-agency-cost-report-data-dictionary",
             "description": "The Home Health Agency Provider Cost Report dataset provides select measures from the home health agency annual cost report. This data includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.",
-            "title": "Home Health Agency Cost Report",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4999da74-1d8d-4a6f-934e-2d7ea470cc63/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4999da74-1d8d-4a6f-934e-2d7ea470cc63/data",
+                    "mediaType": "text/html",
                     "title": "Home Health Agency Cost Report : 2022-12-01"
                 },
                 {
@@ -69879,97 +69857,96 @@
                     "title": "Home Health Agency Cost Report : 2020-12-02"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/home-health-agency-cost-report-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/4999da74-1d8d-4a6f-934e-2d7ea470cc63/data-viewer",
+            "issued": "2023-12-15",
+            "keyword": [
+                "financials",
+                "home health",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/provider-compliance/cost-report/home-health-agency-cost-report",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-25",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/home-health-agency-cost-report-methodology"
+            ],
+            "temporal": "2020-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Home Health Agency Cost Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fx7n-f9pk",
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
-            "identifier": "d6a1edcf-eec9-5eef-82e2-a4d68cc940c4",
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
+            "identifier": "d6a1edcf-eec9-5eef-82e2-a4d68cc940c4",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/fx7n-f9pk",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -69992,39 +69969,45 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1AA.  Poliovirus infection, nonparalytic to Psittacosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/e8fc-yrqd",
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
-            "identifier": "https://data.cdc.gov/api/views/e8fc-yrqd",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 1 - Boston",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70047,53 +70030,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/e8fc-yrqd",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/e8fc-yrqd",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 1 - Boston"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-09-15",
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
-            "identifier": "https://data.cdc.gov/api/views/w4jm-mysj",
             "description": "Deaths involving coronavirus disease 2019 (COVID-19) by month of death, region, age, place of death, and race and Hispanic origin: May-August 2020.",
-            "title": "AH Monthly COVID-19 Deaths, by Census Region, Age, Place, and Race and Hispanic Origin, 2020 Provisional",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70116,46 +70086,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/w4jm-mysj",
+            "issued": "2020-09-15",
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
+            "title": "AH Monthly COVID-19 Deaths, by Census Region, Age, Place, and Race and Hispanic Origin, 2020 Provisional"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/54ys-qyzm",
+            "accrualPeriodicity": "None - this dataset is archived as of May 2023",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-03-17",
-            "@type": "dcat:Dataset",
-            "temporal": "October 3, 2021 - April 22, 2023",
-            "modified": "2023-06-01",
-            "keyword": [
-                "covid-19 bivalent boosters",
-                "covid-19 booster doses",
-                "covid-19 breakthrough",
-                "covid-19 cases",
-                "covid-19 deaths",
-                "covid-19 vaccination"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vaccine Breakthrough/Surveillance and Analytics Team",
                 "hasEmail": "mailto:vbtsurveillance@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/54ys-qyzm",
             "description": "Data for CDC\u2019s COVID Data Tracker site on Rates of COVID-19 Cases and Deaths by Updated (Bivalent) Booster Status.\nClick 'More' for important dataset description and footnotes\n\nWebpage: https://covid.cdc.gov/covid-data-tracker/#rates-by-vaccine-status\n\nDataset and data visualization details:\n\n\nThese data were posted and archived on May 30, 2023 and reflect cases among persons with a positive specimen collection date through April 22, 2023, and deaths among persons with a positive specimen collection date through April 1, 2023. These data will no longer be updated after May 2023.\n\nVaccination status: A person vaccinated with at least a primary series had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after verifiably completing the primary series of an FDA-authorized or approved COVID-19 vaccine. An unvaccinated person had SARS-CoV-2 RNA or antigen detected on a respiratory specimen and has not been verified to have received COVID-19 vaccine. Excluded were partially vaccinated people who received at least one FDA-authorized vaccine dose but did not complete a primary series \u226514 days before collection of a specimen where SARS-CoV-2 RNA or antigen was detected. A person vaccinated with a primary series and a monovalent booster dose had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after verifiably receiving a primary series of an FDA-authorized or approved vaccine and at least one additional dose of any monovalent FDA-authorized or approved COVID-19 vaccine on or after August 13, 2021. (Note: this definition does not distinguish between vaccine recipients who are immunocompromised and are receiving an additional dose versus those who are not immunocompromised and receiving a booster dose.) A person vaccinated with a primary series and an updated (bivalent) booster dose had SARS-CoV-2 RNA or antigen detected in a respiratory specimen collected \u226514 days after verifiably receiving a primary series of an FDA-authorized or approved vaccine and an additional dose of any bivalent FDA-authorized or approved vaccine COVID-19 vaccine on or after September 1, 2022. (Note: Doses with bivalent doses reported as first or second doses are classified as vaccinated with a bivalent booster dose.) People with primary series or a monovalent booster dose were combined in the \u201cvaccinated without an updated booster\u201d category. \n\nDeaths: A COVID-19\u2013associated death occurred in a person with a documented COVID-19 diagnosis who died; health department staff reviewed to make a determination using vital records, public health investigation, or other data sources. Per the interim guidance of the Council of State and Territorial Epidemiologists (CSTE), this should include persons whose death certificate lists COVID-19 disease or SARS-CoV-2 as the underlying cause of death or as a significant condition contributing to death. Rates of COVID-19 deaths by vaccination status are primarily reported based on when the patient was tested for COVID-19. In select jurisdictions, deaths are included that are not laboratory confirmed and are reported based on alternative dates (i.e., onset date for most; or date of death or report date, where onset date is unavailable). Deaths usually occur up to 30 days after COVID-19 diagnosis.\n\nParticipating jurisdictions: Currently, these 24 health departments that regularly link their case surveillance to immunization information system data are included in these incidence rate estimates: Alabama, Arizona, Colorado, District of Columbia, Georgia, Idaho, Indiana, Kansas, Kentucky, Louisiana, Massachusetts, Michigan, Minnesota, Nebraska, New Jersey, New Mexico, New York, New York City (NY), North Carolina, Rhode Island, Tennessee, Texas, Utah, and West Virginia; 23 jurisdictions also report deaths among vaccinated and unvaccinated people. These jurisdictions represent 48% of the total U.S. population and all ten of the Health and Human Services Regions. This list will be",
-            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Updated (Bivalent) Booster Status",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70178,46 +70157,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Select US Jurisdictions",
+            "identifier": "https://data.cdc.gov/api/views/54ys-qyzm",
+            "issued": "2023-03-17",
+            "keyword": [
+                "covid-19 bivalent boosters",
+                "covid-19 booster doses",
+                "covid-19 breakthrough",
+                "covid-19 cases",
+                "covid-19 deaths",
+                "covid-19 vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/54ys-qyzm",
+            "language": [
+                "English"
+            ],
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "None - this dataset is archived as of May 2023",
+            "modified": "2023-06-01",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "Select US Jurisdictions",
+            "temporal": "October 3, 2021 - April 22, 2023",
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Updated (Bivalent) Booster Status"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/fztk-4izv",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2014-09-22",
-            "keyword": [
-                "drug name",
-                "feasibility",
-                "proprietary",
-                "safety"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Quinn",
                 "hasEmail": "mailto:john.quinn@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "78e2c44a-948a-4f20-a810-6f1e60cee0d1",
             "description": "POCA is a software that produces a data set used internally to assess the  safety, and feasibility of proposed proprietary drug names.  FDA product name safety evaluators have access to an internal version of the POCA system behind the FDA firewall.   Source code to develop external non-FDA instances of POCA are available at http://www.fda.gov/Drugs/ResourcesForYou/Industry/ucm400127.htm",
-            "title": "POCA -Phonetic Orthographic Computer Algorithm",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70225,45 +70206,40 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "78e2c44a-948a-4f20-a810-6f1e60cee0d1",
+            "issued": "2021-02-25",
+            "keyword": [
+                "drug name",
+                "feasibility",
+                "proprietary",
+                "safety"
+            ],
+            "landingPage": "https://healthdata.gov/d/fztk-4izv",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2014-09-22",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "POCA -Phonetic Orthographic Computer Algorithm"
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
-            "@type": "dcat:Dataset",
-            "temporal": "2015/2017",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/NCHS-TMSIS-MATCH-STATUS.pdf"
-            ],
-            "keyword": [
-                "linked medicaid data",
-                "nhcs",
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
-            "identifier": "https://data.cdc.gov/api/views/ay69-birh",
-            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with Medicaid and Children\u2019s Health Insurance Program (CHIP) claims data collected by the Centers for Medicare & Medicaid Services (CMS) Transformed Medicaid Statistical Information System (T-MSIS). Linkage of NHCS patient data with T-MSIS enrollment and claims data creates a new data resource that can support research studies focused on a wide range of patient health outcomes and the association of means-tested government insurance programs with health and health outcomes.",
-            "title": "National Hospital Care Survey (NHCS) linked to Centers for Medicare & Medicaid (CMS) Medicaid Data",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 22) here: https://www.cdc.gov/nchs/data/datalinkage/2016-nhcs-cms-medicaid-linkage-methodology.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the National Hospital Care Survey (NHCS) by augmenting it with Medicaid and Children\u2019s Health Insurance Program (CHIP) claims data collected by the Centers for Medicare & Medicaid Services (CMS) Transformed Medicaid Statistical Information System (T-MSIS). Linkage of NHCS patient data with T-MSIS enrollment and claims data creates a new data resource that can support research studies focused on a wide range of patient health outcomes and the association of means-tested government insurance programs with health and health outcomes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70271,21 +70247,58 @@
                     "mediaType": "text/html"
                 }
             ],
-            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 22) here: https://www.cdc.gov/nchs/data/datalinkage/2016-nhcs-cms-medicaid-linkage-methodology.pdf",
+            "identifier": "https://data.cdc.gov/api/views/ay69-birh",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-12-20",
+            "keyword": [
+                "linked medicaid data",
+                "nhcs",
+                "research-data-center",
+                "t-msis"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-medicaid.htm",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/NCHS-TMSIS-MATCH-STATUS.pdf"
+            ],
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
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1998",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npsychotherapeutics. Respondents were also asked about personal and<br />\nfamily income sources and amounts, substance abuse treatment history,<br />\nillegal activities, problems resulting from the use of drugs, need for<br />\ntreatment for drug or alcohol use, criminal record, and<br />\nneedle-sharing. Questions on mental health and access to care, which<br />\nwere introduced in the 1994-B questionnaire (see NATIONAL HOUSEHOLD<br />\nSURVEY ON DRUG ABUSE, 1994), were retained in this<br />\nadministration of the survey. Also retained was the section on<br />\nrisk/availability of drugs that was reintroduced in 1996, and sections<br />\non driving behavior and personal behavior were added (see NATIONAL<br />\nHOUSEHOLD SURVEY ON DRUG ABUSE, 1996). The 1997<br />\nquestionnaire (NATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1997) introduced new items that the 1998 NHSDA continued on cigar<br />\nsmoking, people who were present when respondents used marijuana or<br />\ncocaine for the first time (if applicable), reasons for using these<br />\ntwo drugs the first time, reasons for using these two drugs in the<br />\npast year, reasons for discontinuing use of these two drugs (for<br />\nlifetime but not past-year users), and reasons respondents never used<br />\nthese two drugs. Both the 1997 and 1998 NHSDAs had a series of<br />\nquestions that were asked only of respondents aged 12 to 17. These<br />\nitems covered a variety of topics that may be associated with<br />\nsubstance use and related behaviors, such as exposure to substance<br />\nabuse prevention and education programs, gang involvement,<br />\nrelationship with parents, and substance use by friends. Demographic<br />\ndata include gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, income level, veteran status, and current household<br />\ncomposition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1998) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1998-nid13630",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1998-nid13630"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1998-nid13630",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "alcohol abuse",
@@ -70317,61 +70330,30 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1998",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1998-nid13630",
-            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npsychotherapeutics. Respondents were also asked about personal and<br />\nfamily income sources and amounts, substance abuse treatment history,<br />\nillegal activities, problems resulting from the use of drugs, need for<br />\ntreatment for drug or alcohol use, criminal record, and<br />\nneedle-sharing. Questions on mental health and access to care, which<br />\nwere introduced in the 1994-B questionnaire (see NATIONAL HOUSEHOLD<br />\nSURVEY ON DRUG ABUSE, 1994), were retained in this<br />\nadministration of the survey. Also retained was the section on<br />\nrisk/availability of drugs that was reintroduced in 1996, and sections<br />\non driving behavior and personal behavior were added (see NATIONAL<br />\nHOUSEHOLD SURVEY ON DRUG ABUSE, 1996). The 1997<br />\nquestionnaire (NATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1997) introduced new items that the 1998 NHSDA continued on cigar<br />\nsmoking, people who were present when respondents used marijuana or<br />\ncocaine for the first time (if applicable), reasons for using these<br />\ntwo drugs the first time, reasons for using these two drugs in the<br />\npast year, reasons for discontinuing use of these two drugs (for<br />\nlifetime but not past-year users), and reasons respondents never used<br />\nthese two drugs. Both the 1997 and 1998 NHSDAs had a series of<br />\nquestions that were asked only of respondents aged 12 to 17. These<br />\nitems covered a variety of topics that may be associated with<br />\nsubstance use and related behaviors, such as exposure to substance<br />\nabuse prevention and education programs, gang involvement,<br />\nrelationship with parents, and substance use by friends. Demographic<br />\ndata include gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, income level, veteran status, and current household<br />\ncomposition.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1998)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1998-nid13630",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1998) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1998-nid13630"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1998)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-11-28",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/khic-yj26",
             "description": "The BEAM (Bacteria, Enterics, Amoeba, and Mycotics) Dashboard is an interactive tool to access and visualize data from the System for Enteric Disease Response, Investigation, and Coordination (SEDRIC). The BEAM Dashboard provides timely data on pathogen trends and serotype details to inform work to prevent illnesses from food and animal contact.",
-            "title": "BEAM Dashboard - Isolates by HHS Region",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70394,55 +70376,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/khic-yj26",
+            "issued": "2022-11-28",
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
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Foodborne",
                 "Waterborne",
                 "and Related Diseases"
-            ]
+            ],
+            "title": "BEAM Dashboard - Isolates by HHS Region"
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
-            "identifier": "https://data.cdc.gov/api/views/equ4-92qe",
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Service-Utilization-2010-To-Present/equ4-92qe",
             "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
-            "title": "Quitline \u2013 Service Utilization - 2010 To Present",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70465,93 +70436,99 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Service-Utilization-2010-To-Present/equ4-92qe",
+            "identifier": "https://data.cdc.gov/api/views/equ4-92qe",
+            "issued": "2023-07-14",
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
+            "title": "Quitline \u2013 Service Utilization - 2010 To Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/g2vc-5pzi",
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
-            "identifier": "2eb2dbeb-08d4-56a3-b081-2c87d0353027",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard version v2.11.9 (prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/version.csv",
-                    "description": "Scorecard version v2.11.9 (prod)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard version v2.11.9 (prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/version.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard version v2.11.9 (prod)"
                 }
             ],
+            "identifier": "2eb2dbeb-08d4-56a3-b081-2c87d0353027",
+            "issued": "2023-07-22",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/g2vc-5pzi",
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
+            "title": "Scorecard version v2.11.9 (prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/students-trained-through-onc-workforce-programs",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2014-06-01",
-            "references": [
-                "http://www.healthit.gov/facas/sites/faca/files/Workforce%20Evaluation%20Briefing%20for%20FACA%20Committee%2009%2010.pdf",
-                "https://www.healthit.gov/data/quickstats/hitech-workforce-development-programs"
-            ],
-            "keyword": [
-                "grantees",
-                "health information",
-                "health it",
-                "health it professionals",
-                "onc community college consortia"
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
-            "identifier": "4zpu3gv4-vo8i-wwb6-6wfi-gd6i7vzqsqo3",
+            "describedBy": "https://www.healthit.gov/data/datasets/students-trained-through-onc-workforce-programs",
             "description": "The Office of the National Coordinator for Health Information Technology (ONC) created the Community College Consortia to Educate Health IT Professionals in Health Care Program and University-based Training Program to increase the workforce of skilled health IT specialists that can help transition health care providers to electronic health records (EHRs). The Community College Consortia Program includes 82 member community colleges representing all 50 states, and the University-based Training Program includes 9 member universities in 9 states. The member community colleges and universities received funding to rapidly create health IT academic programs, or expand existing health IT training programs that can be completed in six months or less. This data provides the number of students trained through both programs, segmented by rural and urban areas for each U.S. state. The data is through September, 2013: the duration of the program. This data is an artifact of ONC's performance measurement for the Recovery and HITECH Acts",
-            "title": "Students Trained through ONC Workforce Programs",
-            "programCode": [
-                "009:110"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70560,17 +70537,53 @@
                     "title": "workforce-programs-trained.csv"
                 }
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/students-trained-through-onc-workforce-programs"
+            "identifier": "4zpu3gv4-vo8i-wwb6-6wfi-gd6i7vzqsqo3",
+            "issued": "2023-10-03",
+            "keyword": [
+                "grantees",
+                "health information",
+                "health it",
+                "health it professionals",
+                "onc community college consortia"
+            ],
+            "landingPage": "https://www.healthit.gov/data/datasets/students-trained-through-onc-workforce-programs",
+            "modified": "2014-06-01",
+            "programCode": [
+                "009:110"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "references": [
+                "http://www.healthit.gov/facas/sites/faca/files/Workforce%20Evaluation%20Briefing%20for%20FACA%20Committee%2009%2010.pdf",
+                "https://www.healthit.gov/data/quickstats/hitech-workforce-development-programs"
+            ],
+            "title": "Students Trained through ONC Workforce Programs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1993",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1993) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1993-nid13571",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1993-nid13571"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1993-nid13571",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -70583,69 +70596,30 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1993",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1993-nid13571",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1993)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1993-nid13571",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1993) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1993-nid13571"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1993)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-10-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2022-10-15",
-            "modified": "2023-04-05",
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
-            "identifier": "https://data.cdc.gov/api/views/ite7-j2w7",
             "description": "Provisional count of deaths involving COVID-19 by United States county of occurrence, by week of death.",
-            "title": "AH COVID-19 Death Counts by County and Week, 2020-present",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70668,37 +70642,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/ite7-j2w7",
+            "issued": "2022-10-18",
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
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-04-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2020-01-01/2022-10-15",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH COVID-19 Death Counts by County and Week, 2020-present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wa6b-urfv",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wa6b-urfv",
             "description": "A new high-flow, compact aerosol concentrator, using rapid, turbulent mixing to grow aerosol particles into droplets for dry spot sample collection, has been designed and tested. The \u201cTCAC (Turbulent-mixing, Condensation Aerosol Concentrator)\u201d is composed of a saturator for generating hot vapor, a mixing section where the hot vapor mixes with the cold aerosol flow, a growth tube where condensational droplet growth primarily occurs, and a converging nozzle that focuses the droplets into a beam. The prototype concentrator utilizes an aerosol sample flow rate of 4 L min-1. The TCAC was optimized by varying the operating conditions, such as relative humidity of the aerosol flow, mixing flow ratio, vapor temperature, and impaction characteristics. The results showed that particles with a diameter \u2265 25 nm can be grown to a droplet diameter > 1400 nm with near 100 % efficiency. Complete activation and growth were observed at relative humidity \u2265 25 % of the aerosol sample flow. A consistent spot sample with a diameter of D90 = 1.4 mm (the diameter of a circle containing 90 % of the deposited particles) was obtained regardless of the aerosol particle diameter (dp = 20 \u2013 1900 nm). For fiber counting applications using phase contrast microscopy, the TCAC can reduce the sampling time, or counting uncertainty, by two to three orders of magnitude, compared to the 25-mm-filter collection. The study shows that the proposed mixing-flow scheme enables a compact spot sample collector suitable for handheld or portable applications, while still allowing for high flow rates.",
-            "title": "Compact, High-flow, Water-based, Turbulent-mixing, Condensation Aerosol Concentrator for Collection of Spot Samples",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70706,170 +70693,196 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wa6b-urfv",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/wa6b-urfv",
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
+            "title": "Compact, High-flow, Water-based, Turbulent-mixing, Condensation Aerosol Concentrator for Collection of Spot Samples"
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
-                "name": "Centers for Disease Control and Prevention"
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
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Future funding patterns past 2024 are uncertain however, we expect yearly or biannually is reasonable R/P1Y or R/P2Y",
+            "modified": "2024-02-20",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/d/g4wx-we5n",
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
-            "identifier": "d4063f55-6da8-587b-8279-8ff627b2318b",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_tafVersion",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/tafVersion.csv",
-                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/tafVersion.csv",
+                    "mediaType": "text/csv",
                     "title": "tafVersion csv file"
                 }
             ],
+            "identifier": "d4063f55-6da8-587b-8279-8ff627b2318b",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/g4wx-we5n",
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
+            "title": "devAuto_tafVersion"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/g58t-eidy",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "keyword": [
-                "acute care",
-                "chip",
-                "dqatlas",
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
-            "identifier": "d55e5ef5-9a2e-4d6c-884e-65a40a70756b",
             "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of acute care services, including emergency department (ED) visits, inpatient stays, intensive care unit (ICU) stays, and ICU stays that include ventilator use, provided to Medicaid and CHIP beneficiaries, by state. Users can filter to acute care services for any reason, or acute care services for COVID-19. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating acute care services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Acute Care Services Provided to the Medicaid and CHIP Population",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Acute-Care-Services-Provided-to-the-MedicaidCHIP-Population.csv",
-                    "description": "Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Acute-Care-Services-Provided-to-the-MedicaidCHIP-Population.csv",
+                    "mediaType": "text/csv",
                     "title": "Acute Care Services Provided to the Medicaid and CHIP Population"
                 }
             ],
+            "identifier": "d55e5ef5-9a2e-4d6c-884e-65a40a70756b",
+            "issued": "2023-03-28",
+            "keyword": [
+                "acute care",
+                "chip",
+                "dqatlas",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/g58t-eidy",
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
+            "title": "Acute Care Services Provided to the Medicaid and CHIP Population"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2009",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2009) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2009-nid13631",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2009-nid13631"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2009-nid13631",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -70882,117 +70895,78 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2009",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2009-nid13631",
-            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2009)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2009-nid13631",
-                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2009) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2009-nid13631"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2009)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/g5mg-5c44",
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
-            "identifier": "315310e1-367d-51cd-ac6d-ecf42f828960",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_files_topicSnapshot",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_topicSnapshot.csv",
-                    "description": "{\"dataset\": \"files_topicSnapshot\", \"stage\": \"featAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_topicSnapshot\", \"stage\": \"featAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_topicSnapshot.csv",
+                    "mediaType": "text/csv",
                     "title": "files_topicSnapshot csv file"
                 }
             ],
+            "identifier": "315310e1-367d-51cd-ac6d-ecf42f828960",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/g5mg-5c44",
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
+            "title": "featAuto_files_topicSnapshot"
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
@@ -71015,46 +70989,49 @@
                     "mediaType": "application/xml"
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
+            "title": "PLACES: ZCTA Data (GIS Friendly Format), 2020 release"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -71077,47 +71054,46 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cdc.gov/d/nra9-vzzn",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-22/2022-10-18",
-            "modified": "2025-01-13",
-            "references": [
-                "https://data.cdc.gov/Public-Health-Surveillance/United-States-County-Level-of-Community-Transmissi/8396-v7yb"
-            ],
-            "keyword": [
-                "cases",
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
-            "identifier": "https://data.cdc.gov/api/views/nra9-vzzn",
             "description": "On October 20, 2022, CDC began retrieving aggregate case and death data from jurisdictional and state partners weekly instead of daily. This dataset contains archived historical community transmission and related data elements by county. Although these data will continue to be publicly available, this dataset has not been updated since October 20, 2022. An archived dataset containing weekly historical community transmission data by county can also be found here: <a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">Weekly COVID-19 County Level of Community Transmission Historical Changes | Data | Centers for Disease Control and Prevention (cdc.gov)</a>. \n\n<b>Related data</b>\nCDC has been providing the public with two versions of COVID-19 county-level community transmission level data: this historical dataset with the daily county-level transmission data from January 22, 2020, and a dataset with the daily values as originally posted on the COVID Data Tracker. Similar to this dataset, the <a href=\"https://data.cdc.gov/Public-Health-Surveillance/United-States-COVID-19-County-Level-of-Community-T/nra9-vzzn\">original dataset</a> with daily data as posted is archived on 10/20/2022. It will continue to be publicly available but will no longer be updated. A new dataset containing community transmission data by county as originally posted is now published weekly and can be found at: <a href=\"https://data.cdc.gov/dataset/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly COVID-19 County Level of Community Transmission as Originally Posted | Data | Centers for Disease Control and Prevention (cdc.gov)</a>.\n\nThis public use dataset has 7 data elements reflecting historical data for community transmission levels for all available counties and jurisdictions. It contains historical data for the county level of community transmission and includes updated data submitted by states and jurisdictions. Each day, the dataset was updated to include the most recent days\u2019 data and incorporate any historical changes made by jurisdictions. This dataset includes data since January 22, 2020. Transmission level is set to low, moderate, substantial, or high using the calculation rules below.\n\n<b>Methods for calculating county level of community transmission indicator</b>\nThe County Level of Community Transmission indicator uses two metrics: (1) total new COVID-19 cases per 100,000 persons in the last 7 days and (2) percentage of positive SARS-CoV-2 diagnostic nucleic acid amplification tests (NAAT) in the last 7 days. For each of these metrics, CDC classifies transmission values as low, moderate, substantial, or high (below and <a href=\"https://www.cdc.gov/mmwr/volumes/70/wr/mm7030e2.htm?s_cid=mm7030e2_w#T1_down\">here</a>). If the values for each of these two metrics differ (e.g., one indicates moderate and the other low), then the higher of the two should be used for decision-making.\n\n<b>CDC core metrics of and thresholds for community transmission levels of SARS-CoV-2</b>\n\n<b>Total New Case Rate Metric:</b> \"New cases per 100,000 persons in the past 7 days\" is calculated by adding the number of new cases in the county (or other administrative level) in the last 7 days divided by the population in the county (or other administrative level) and multiplying by 100,000. \"New cases per 100,000 persons in the past 7 days\" is considered to have transmission level of Low (0-9.99); Moderate (10.00-49.99); Substantial (50.00-99.99); and High (greater than or equal to 100.00).\n\n<b>Test Percent Positivity Metric:</b> \"Percentage of positive NAAT in the past 7 days\" is calculated by dividing the number of positive tests in the county (or other administrative level) during the last 7 days by the total number of tests resulted over the last 7 days. \"Percentage of positive NAAT in the past 7 days\" is considered to have transmission level of Low (less than 5.00); Moderate (5.00-7.99); Substa",
-            "title": "United States COVID-19 County Level of Community Transmission Historical Changes - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71140,58 +71116,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/nra9-vzzn",
+            "issued": "2022-01-06",
+            "keyword": [
+                "cases",
+                "community transmission",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "laboratory"
+            ],
+            "landingPage": "https://data.cdc.gov/d/nra9-vzzn",
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
+                "https://data.cdc.gov/Public-Health-Surveillance/United-States-County-Level-of-Community-Transmissi/8396-v7yb"
+            ],
+            "spatial": "US",
+            "temporal": "2020-01-22/2022-10-18",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "United States COVID-19 County Level of Community Transmission Historical Changes - ARCHIVED"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -71214,47 +71181,57 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -71277,40 +71254,45 @@
                     "mediaType": "application/xml"
                 }
             ],
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
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/msaviewer/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6iwu-fbds",
             "description": "An interactive Web application that enables users to visualize multiple alignments created by database search results or other software applications. The MSA Viewer allows users to upload an alignment and set a master sequence and to explore the data using features such as zooming and changing of coloration.",
-            "title": "Multiple Sequence Alignment (MSA) Viewer",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71319,78 +71301,106 @@
                     "title": "Multiple Sequence Alignment (MSA) Viewer"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/tools/msaviewer/embedding-api/",
-                    "description": "The NCBI Multiple Sequence (MSA) Alignment Viewer is a general purpose tool for viewing multiple alignments of biological sequences. It can be embedded in a wide variety of web pages and with a large number of options.",
                     "@type": "dcat:Distribution",
+                    "description": "The NCBI Multiple Sequence (MSA) Alignment Viewer is a general purpose tool for viewing multiple alignments of biological sequences. It can be embedded in a wide variety of web pages and with a large number of options.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/tools/msaviewer/embedding-api/",
+                    "mediaType": "text/html",
                     "title": "Multiple Sequence Alignment Viewer Embedding API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6iwu-fbds",
+            "issued": "2021-06-30",
+            "keyword": [
+                "api",
+                "protein",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/msaviewer/",
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
+            "title": "Multiple Sequence Alignment (MSA) Viewer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/g995-q4wt",
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
-            "identifier": "622fd82e-d2cb-5204-9a97-ba4df56ffcc6",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_files_allDownloadsSSBtn",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/files_allDownloadsSSBtn.csv",
-                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_allDownloadsSSBtn\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/files_allDownloadsSSBtn.csv",
+                    "mediaType": "text/csv",
                     "title": "files_allDownloadsSSBtn csv file"
                 }
             ],
+            "identifier": "622fd82e-d2cb-5204-9a97-ba4df56ffcc6",
+            "issued": "2022-06-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/g995-q4wt",
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
+            "title": "featAuto_files_allDownloadsSSBtn"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/state-health-it-policy-levers-activities-catalog",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2015-12-01",
-            "references": [
-                "https://www.healthit.gov/data/apps/state-health-it-policy-levers-compendium"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/state-health-it-policy-levers-activities-catalog",
+            "description": "The Health IT State Policy Levers Compendium was developed by the Office of National Coordinator for Health Information Technology (ONC) in coordination with states. It is intended to support state efforts to advance interoperability and can also be used in service of delivery system reform. The Compendium includes a directory of health IT policy levers and nearly 300 examples of how states have used them. The 'Activities Catalog' includes the over 300 documented examples of health IT policy levers in use by states. The catalog data includes the states using the policy lever to promote health IT and advance interoperability, the state's documented activities, and official information source for these activities.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/policy-levers-activities-catalog.csv",
+                    "mediaType": "text/csv",
+                    "title": "policy-levers-activities-catalog.csv"
+                }
             ],
+            "identifier": "exxucmj0-ey0t-ofmw-ehjp-yknmz432m3og",
+            "issued": "2023-10-03",
             "keyword": [
                 "ehr",
                 "health information exchange",
@@ -71400,66 +71410,32 @@
                 "state health it policies",
                 "state hie"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/state-health-it-policy-levers-activities-catalog",
+            "modified": "2015-12-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "exxucmj0-ey0t-ofmw-ehjp-yknmz432m3og",
-            "description": "The Health IT State Policy Levers Compendium was developed by the Office of National Coordinator for Health Information Technology (ONC) in coordination with states. It is intended to support state efforts to advance interoperability and can also be used in service of delivery system reform. The Compendium includes a directory of health IT policy levers and nearly 300 examples of how states have used them. The 'Activities Catalog' includes the over 300 documented examples of health IT policy levers in use by states. The catalog data includes the states using the policy lever to promote health IT and advance interoperability, the state's documented activities, and official information source for these activities.",
-            "title": "State Health IT Policy Levers Activities Catalog",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/policy-levers-activities-catalog.csv",
-                    "mediaType": "text/csv",
-                    "title": "policy-levers-activities-catalog.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/apps/state-health-it-policy-levers-compendium"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/state-health-it-policy-levers-activities-catalog"
+            "title": "State Health IT Policy Levers Activities Catalog"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -71482,21 +71458,58 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Chapare virus to Ebola virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-vaccine-adverse-event-reporting-system-vaers",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/vaers.html",
+            "description": "<p>The Vaccine Adverse Event Reporting System (VAERS) online database on CDC WONDER provides counts and percentages of adverse event case reports after vaccination, by symptom, vaccine product, manufacturer, onset interval, outcome category, year and month vaccinated, year and month reported, age, sex and state / territory. The Vaccine Adverse Event Reporting System is a cooperative program for vaccine safety of the Centers for Disease Control and Prevention (CDC) and the Food and Drug Administration (FDA). VAERS is a post-marketing safety surveillance program, collecting information about adverse events (possible side effects) that occur after the administration of US licensed vaccines.  Data are from the US Department of Health and Human Services (DHHS), Public Health Service (PHS), Food and Drug Administration (FDA)/ Centers for Disease Control (CDC), Vaccine Adverse Event Reporting System (VAERS).</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/vaers.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "2761a3aa-c892-4e95-bece-7902cff70133",
             "issued": "2012-05-30",
-            "temporal": "1990-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "adverse event",
                 "aefi",
@@ -71520,60 +71533,34 @@
                 "vaers",
                 "year"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-vaccine-adverse-event-reporting-system-vaers",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:011"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "2761a3aa-c892-4e95-bece-7902cff70133",
-            "description": "<p>The Vaccine Adverse Event Reporting System (VAERS) online database on CDC WONDER provides counts and percentages of adverse event case reports after vaccination, by symptom, vaccine product, manufacturer, onset interval, outcome category, year and month vaccinated, year and month reported, age, sex and state / territory. The Vaccine Adverse Event Reporting System is a cooperative program for vaccine safety of the Centers for Disease Control and Prevention (CDC) and the Food and Drug Administration (FDA). VAERS is a post-marketing safety surveillance program, collecting information about adverse events (possible side effects) that occur after the administration of US licensed vaccines.  Data are from the US Department of Health and Human Services (DHHS), Public Health Service (PHS), Food and Drug Administration (FDA)/ Centers for Disease Control (CDC), Vaccine Adverse Event Reporting System (VAERS).</p>",
-            "title": "CDC WONDER: Vaccine Adverse Event Reporting System (VAERS)",
-            "programCode": [
-                "009:011"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/vaers.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/vaers.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1990-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Vaccine Adverse Event Reporting System (VAERS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/qzjj-q36s",
-            "issued": "2022-03-30",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kayla Janos",
                 "hasEmail": "mailto:qrw4@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/qzjj-q36s",
             "description": "not for public use",
-            "title": "testing_cte_aspost",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71596,37 +71583,33 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/qzjj-q36s",
+            "issued": "2022-03-30",
+            "landingPage": "https://data.cdc.gov/d/qzjj-q36s",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2022-03-30",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "testing_cte_aspost"
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
-            "identifier": "https://data.cdc.gov/api/views/skkh-jsrk",
             "description": "\u2022 Weekly Cumulative Percentage of Children 6 Months\u201317 Years Who Are Up to Date with COVID-19 Vaccines by Selected Demographics and by Season.\n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey\u2013Child COVID Module (NIS\u2013CCM). The NIS\u2013CCM was discontinued at the end of 2023 and questions regarding COVID-19 vaccination status and intent were added to the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html).\n\n\u2022 Please note, weekly estimates for children 6 months to 4 years and 5 to 11 years from January-June 2024 have been updated due to a mistake in age group coding.",
-            "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to date with COVID-19 Vaccines by Selected Demographics and by Season, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71649,25 +71632,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/skkh-jsrk",
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
+            "title": "Weekly Cumulative Percentage of Children Ages 6 Months -17 Years Who Are Up to date with COVID-19 Vaccines by Selected Demographics and by Season, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/valuing-invaluable-2011-update-growing-contributions-and-costs-family-caregiving",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Claudia Williams",
+                "hasEmail": "mailto:Claudia_H_Williams@ostp.eop.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This report estimates the economic value of family caregiving at $450 billion in 2009 based on 42.1 million caregivers age 18 or older providing an average of 18.4 hours of care per week to care recipients age 18 or older, at an average value of $11.16 per hour.</p>\n<p><strong><em>This data is not collected by a government agency.  The findings and conclusions in this report are those of the author and do not necessarily represent the views of the Department of Health &amp; Human Services.</em></strong></p>",
+            "identifier": "f5545353-28ba-4e82-a0ca-164560d9eb2a",
             "issued": "2014-07-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "caregiver",
                 "caregiving",
@@ -71677,62 +71682,33 @@
                 "healthcare",
                 "seniors"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Claudia Williams",
-                "hasEmail": "mailto:Claudia_H_Williams@ostp.eop.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/valuing-invaluable-2011-update-growing-contributions-and-costs-family-caregiving",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "f5545353-28ba-4e82-a0ca-164560d9eb2a",
-            "description": "<p>This report estimates the economic value of family caregiving at $450 billion in 2009 based on 42.1 million caregivers age 18 or older providing an average of 18.4 hours of care per week to care recipients age 18 or older, at an average value of $11.16 per hour.</p>\n<p><strong><em>This data is not collected by a government agency.  The findings and conclusions in this report are those of the author and do not necessarily represent the views of the Department of Health &amp; Human Services.</em></strong></p>",
-            "title": "Long-Term Care Calculator: Compare Costs, Types of Service in Your Area",
-            "programCode": [
-                "009:015"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Long-Term Care Calculator: Compare Costs, Types of Service in Your Area"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5wdd-3g8t",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/5wdd-3g8t",
             "description": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNotes:\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022\tNotices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\nFootnotes:\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71755,35 +71731,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5wdd-3g8t",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "anthrax",
+                "arboviral diseases",
+                "chikungunya virus disease",
+                "eastern equine encephalitis virus disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5wdd-3g8t",
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
+            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dqgu-gg5d",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -71791,45 +71778,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dqgu-gg5d",
+            "issued": "2022-11-30",
+            "landingPage": "https://data.cdc.gov/d/dqgu-gg5d",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-31",
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
+            "title": "v-safe COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2vtj-68zm",
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
-            "identifier": "https://data.cdc.gov/api/views/2vtj-68zm",
             "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 In previous years, cases were reported as Salmonellosis. Beginning in January 2019, cases began to be reported as Salmonella Paratyphi infection.\n\u00b6 In previous years, cases were reported as typhoid fever. Beginning in January 2019, cases began to be reported as Salmonella Typhi infection.\n** In previous years, cases were reported as Salmonellosis (excluding paratyphoid fever and typhoid fever). Beginning in January 2019, cases began to be reported as Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection).",
-            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71852,41 +71829,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2vtj-68zm",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonella paratyphi infection",
+                "salmonella typhi infection",
+                "salmonellosis (excluding salmonella typhi infection and salmonella paratyphi infection)",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/2vtj-68zm",
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
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qjju-smys",
             "bureauCode": [
                 "009:032"
             ],
-            "issued": "2018-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-27",
-            "keyword": [
-                "air pollution",
-                "asthma",
-                "environmental health",
-                "particulate matter"
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
-            "identifier": "https://data.cdc.gov/api/views/qjju-smys",
             "description": "This dataset provides modeled predictions of particulate matter (PM2.5) levels from the EPA's Downscaler model. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Data are at the county levels for 2001-2014. The dataset includes the maximum, median, mean, and population-weighted mean concentration. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
-            "title": "Daily County-Level PM2.5 Concentrations, 2001-2014",
-            "programCode": [
-                "009:20"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71909,41 +71890,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qjju-smys",
+            "issued": "2018-06-15",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "particulate matter"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qjju-smys",
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
+            "title": "Daily County-Level PM2.5 Concentrations, 2001-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/gdw9-dep3",
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
-                "network",
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
-            "identifier": "2226672d-d505-49ae-9853-1049b53722df",
             "description": "The Network PUF (Ntwrk-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Ntwrk-PUF contains issuer-level data identifying provider network URLs.",
-            "title": "Network PUF - PY2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71951,17 +71933,48 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "2226672d-d505-49ae-9853-1049b53722df",
+            "issued": "2024-08-06",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "network",
+                "py2024"
+            ],
+            "landingPage": "https://healthdata.gov/d/gdw9-dep3",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Network PUF - PY2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ge4b-j6f6",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. Because Medicaid beneficiaries may be enrolled concurrently in more than one type of managed care program (e.g., a Comprehensive MCO and a BHO), users should not sum enrollment across all program types, since the total would count individuals more than once and, in some states, exceed the actual number of Medicaid enrollees.\r\n\r\n2. Comprehensive MCOs cover acute, primary, and specialty medical care services; they may also cover behavioral health, long-term services and supports, and other benefits in some states. Limited benefit managed care programs, including PCCM, MLTSS only, BHO, Dental, Transportation, and Other cover a narrower set of services.\r\n\r\n3.  The \u201cTotal Medicaid Enrollees\u201d column represents an unduplicated count of all beneficiaries in FFS and any type of managed care, including Medicaid-only and dually eligible individuals receiving full Medicaid benefits or Medicaid cost sharing.\r\n\r\n\"--\" indicates states that do not operate programs of a given type. 0 signifies that a state operated a program of this type in 2014, but it ended before July 1, 2014, or began after that date.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-by-program-and-population-all-2022-tab2.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "identifier": "e2ce0d2f-07c5-5213-947a-31e19bc649f6",
             "issued": "2017-12-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
             "keyword": [
                 "bho",
                 "managed care enrollment",
@@ -71974,71 +71987,33 @@
                 "pccm",
                 "pihp"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Medicaid.gov",
-                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/ge4b-j6f6",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-16",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "e2ce0d2f-07c5-5213-947a-31e19bc649f6",
-            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. Because Medicaid beneficiaries may be enrolled concurrently in more than one type of managed care program (e.g., a Comprehensive MCO and a BHO), users should not sum enrollment across all program types, since the total would count individuals more than once and, in some states, exceed the actual number of Medicaid enrollees.\r\n\r\n2. Comprehensive MCOs cover acute, primary, and specialty medical care services; they may also cover behavioral health, long-term services and supports, and other benefits in some states. Limited benefit managed care programs, including PCCM, MLTSS only, BHO, Dental, Transportation, and Other cover a narrower set of services.\r\n\r\n3.  The \u201cTotal Medicaid Enrollees\u201d column represents an unduplicated count of all beneficiaries in FFS and any type of managed care, including Medicaid-only and dually eligible individuals receiving full Medicaid benefits or Medicaid cost sharing.\r\n\r\n\"--\" indicates states that do not operate programs of a given type. 0 signifies that a state operated a program of this type in 2014, but it ended before July 1, 2014, or began after that date.",
-            "title": "Managed Care Enrollment by Program and Population (All)",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-by-program-and-population-all-2022-tab2.csv",
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
+            "title": "Managed Care Enrollment by Program and Population (All)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/62d6-pm5i",
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
-            "identifier": "https://data.cdc.gov/api/views/62d6-pm5i",
             "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when members of the public in states and territories were subject to state and territorial executive orders, administrative orders, resolutions, and proclamations for COVID-19 that require them to wear masks in public. \u201cMembers of the public\u201d are defined as individuals operating in a personal capacity. \u201cIn public\u201d is defined to mean either (1) anywhere outside the home or (2) both in retail businesses and in restaurants/food establishments. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level. \n\nThese data are derived from publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly require individuals to wear masks in public found by the CDC, COVID-19 Community Intervention & Critical Populations Task Force, Monitoring & Evaluation Team, Mitigation Policy Analysis Unit, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program, and Max Gakh, Assistant Professor, School of Public Health, University of Nevada, Las Vegas from April 10, 2020 through August 15, 2021.  These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. Effective and expiration dates were coded using only the dates provided; no distinction was made based on the specific time of the day the order became effective or expired. These data do not include data on counties that have opted out of their state mask mandate pursuant to state law. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
-            "title": "U.S. State and Territorial Public Mask Mandates From April 10, 2020 through August 15, 2021 by County by Day",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72061,38 +72036,47 @@
                     "mediaType": "application/xml"
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
+            "title": "U.S. State and Territorial Public Mask Mandates From April 10, 2020 through August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/geqt-uwhp",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-30",
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
-            "identifier": "f7420ebf-7bd1-44de-b2a4-07c6ec9c28ac",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-23-2024-to-12-29-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72100,38 +72084,35 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "f7420ebf-7bd1-44de-b2a4-07c6ec9c28ac",
+            "issued": "2025-01-01",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/geqt-uwhp",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-30",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-23-2024-to-12-29-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://catalog.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "books",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/f3sh-4v4q",
             "description": "A MARC-based catalog, the LocatorPlus Catalog provides access to NLM bibliographic data for journals, books, audiovisuals, computer software, electronic resources and other materials.",
-            "title": "LocatorPlus",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72140,27 +72121,59 @@
                     "title": "Query Interface"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://support.nlm.nih.gov/knowledgebase/article/KA-04188/en-us",
-                    "description": "Retrieving NLM bibliographic records from the LocatorPlus Catalog via Z39.50",
                     "@type": "dcat:Distribution",
+                    "description": "Retrieving NLM bibliographic records from the LocatorPlus Catalog via Z39.50",
+                    "downloadURL": "https://support.nlm.nih.gov/knowledgebase/article/KA-04188/en-us",
+                    "mediaType": "text/html",
                     "title": "Alma - Z39.50 Protocol"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/f3sh-4v4q",
+            "issued": "2021-06-30",
+            "keyword": [
+                "api",
+                "books",
+                "library services",
+                "literature"
+            ],
+            "landingPage": "https://catalog.nlm.nih.gov/",
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
+            "title": "LocatorPlus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2009",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2009) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2009-nid13614",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2009-nid13614"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2009-nid13614",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -72173,56 +72186,30 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2009",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2009-nid13614",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2009)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2009-nid13614",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2009) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2009-nid13614"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2009)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/lack-socialconnection.htm",
+            "accrualPeriodicity": "monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-21",
-            "temporal": "2024-02-05/2024-09-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-04",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mnaa-qctp",
             "description": "In 2020, the National Center for Health Statistics (NCHS) partnered with the Census Bureau on an experimental data system called the Household Pulse Survey. This survey was designed to complement the ability of the federal statistical system to rapidly respond and provide relevant information about how emergent issues are impacting American households. Beginning in Phase 4.0 (on January 9, 2024), questions on social support, loneliness, and social isolation were added to the survey. These questions have been included on other nationally representative surveys. Briefly, the question on social support was included on the National Health Interview Survey (NHIS) from July 2020-December 2021 and was added to the 2024 NHIS. The question on loneliness was added to the 2024 NHIS. The questions on social isolation are adapted from the Berkman-Syme Social Network Index and were included on an earlier cycle of the National Health and Nutrition Examination Survey. For more information, please visit: https://www.cdc.gov/nchs/covid19/pulse/lack-socialconnection.htm",
-            "title": "Lack of Social Connection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72245,49 +72232,41 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/mnaa-qctp",
+            "issued": "2024-02-21",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/lack-socialconnection.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "monthly",
+            "modified": "2024-10-04",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "U.S.",
+            "temporal": "2024-02-05/2024-09-16",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Lack of Social Connection"
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
-            "identifier": "https://data.cdc.gov/api/views/ui6g-vumy",
+            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Se/ui6g-vumy",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Services and Profiles dataset provides an overview of clinic services, the clinic\u2019s contact information, location, the medical director\u2019s name, and summary statistics.",
-            "title": "2021 Final Assisted Reproductive Technology (ART) Services and Profiles",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72310,46 +72289,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Se/ui6g-vumy",
+            "identifier": "https://data.cdc.gov/api/views/ui6g-vumy",
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
+            "title": "2021 Final Assisted Reproductive Technology (ART) Services and Profiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vuhn-dxkt",
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
-            "identifier": "https://data.cdc.gov/api/views/vuhn-dxkt",
             "description": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72372,42 +72349,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vuhn-dxkt",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "nonparalytic",
+                "poliovirus infection",
+                "psittacosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vuhn-dxkt",
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
+            "title": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -72430,166 +72411,156 @@
                     "mediaType": "application/xml"
                 }
             ],
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Annually",
+            "modified": "2023-05-02",
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
+            "title": "autism prevalence studies"
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
-                "name": "Centers for Disease Control and Prevention"
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
+                "name": "Centers for Disease Control and Prevention"
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/ahcd/namcs_hc.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "Public access",
-            "issued": "2024-07-24",
-            "@type": "dcat:Dataset",
-            "temporal": "2022",
-            "modified": "2024-07-24",
-            "keyword": [
-                "ambulatory-care",
-                "health center",
-                "health center component",
-                "health center encounter",
-                "namcs"
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
-            "identifier": "https://data.cdc.gov/api/views/wj2j-rzx9",
-            "description": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component, conducted by the National Center for Health Statistics (NCHS), collects annual data on visits to health centers to describe patterns of utilization and provision of ambulatory care delivery in the United States. Health centers are local clinics that are community-based and provide comprehensive health care services to populations that are often vulnerable and underserved. Health centers are either federally qualified health centers (FQHCs), which receive federal funding from the Health Resources and Services Administration (HRSA), or FQHC look-alikes, which meet HRSA requirements but do not receive HRSA funding.",
-            "title": "National Ambulatory Medical Care Survey, Health Center Component, 2022, Public-use file",
+            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS_HC/2022/2022-NAMCS-HCC-PUF-Codebook-508.pdf, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS_HC/2022/2022-NAMCS-HCC-PUF-Tech-Doc-508.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component, conducted by the National Center for Health Statistics (NCHS), collects annual data on visits to health centers to describe patterns of utilization and provision of ambulatory care delivery in the United States. Health centers are local clinics that are community-based and provide comprehensive health care services to populations that are often vulnerable and underserved. Health centers are either federally qualified health centers (FQHCs), which receive federal funding from the Health Resources and Services Administration (HRSA), or FQHC look-alikes, which meet HRSA requirements but do not receive HRSA funding.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/ahcd/namcs_hc.htm",
-                    "description": "R, SAS, and STATA data files are readily available.",
                     "@type": "dcat:Distribution",
+                    "description": "R, SAS, and STATA data files are readily available.",
+                    "downloadURL": "https://www.cdc.gov/nchs/ahcd/namcs_hc.htm",
+                    "mediaType": "text/html",
                     "title": "2022 NAMCS Health Center Component"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS_HC/2022/2022-NAMCS-HCC-PUF-Codebook-508.pdf, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS_HC/2022/2022-NAMCS-HCC-PUF-Tech-Doc-508.pdf",
+            "identifier": "https://data.cdc.gov/api/views/wj2j-rzx9",
+            "issued": "2024-07-24",
+            "keyword": [
+                "ambulatory-care",
+                "health center",
+                "health center component",
+                "health center encounter",
+                "namcs"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/namcs_hc.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-07-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "Public access",
+            "spatial": "United States",
+            "temporal": "2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey, Health Center Component, 2022, Public-use file"
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
-            "identifier": "https://data.cdc.gov/api/views/tid6-xphm",
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Quitline-Names-and-Phone-Numbers/tid6-xphm",
             "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
-            "title": "Quitline \u2013 Quitline Names and Phone Numbers",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72612,50 +72583,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Quitline-Names-and-Phone-Numbers/tid6-xphm",
+            "identifier": "https://data.cdc.gov/api/views/tid6-xphm",
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
+            "title": "Quitline \u2013 Quitline Names and Phone Numbers"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -72678,48 +72652,51 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/index_2020.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-09-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2020-12-31",
-            "modified": "2022-09-01",
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
-            "identifier": "https://data.cdc.gov/api/views/ss2j-8ajj",
             "description": "The dataset presents life expectancy at birth estimates based on annual complete period life tables for each of the 50 states and the District of Columbia (D.C.)\nin 2020 for the total, male and female populations.",
-            "title": "U.S. State Life Expectancy by Sex, 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72742,43 +72719,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/ss2j-8ajj",
+            "issued": "2022-09-01",
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
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/state-life-expectancy/index_2020.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2022-09-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
+            "temporal": "2020-01-01/2020-12-31",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "U.S. State Life Expectancy by Sex, 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/gk4r-hamn",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-09",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-16",
-            "keyword": [
-                "business rules",
-                "exchange puf",
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
-            "identifier": "ab6b8ea6-fdd8-4eb6-9fe6-7a93aca92b46",
             "description": "The Business Rules PUF (BR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BR-PUF contains plan-level data on rating business rules, such as maximum age for a dependent and allowed dependent relationships.",
-            "title": "Business Rules PUF - PY2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72786,32 +72768,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "ab6b8ea6-fdd8-4eb6-9fe6-7a93aca92b46",
+            "issued": "2023-08-09",
+            "keyword": [
+                "business rules",
+                "exchange puf",
+                "marketplace puf",
+                "py2023"
+            ],
+            "landingPage": "https://healthdata.gov/d/gk4r-hamn",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Business Rules PUF - PY2023"
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
-            "modified": "2025-01-24",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RESP-NET",
                 "hasEmail": "mailto:CovidRSV-Net@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
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
@@ -72834,48 +72822,37 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "COVID-NET Sites",
+            "identifier": "https://data.cdc.gov/api/views/6jg4-xsqq",
+            "issued": "2024-06-26",
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
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2023-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-10",
-            "references": [
-                "https://chronicdata.cdc.gov/d/5qag-uzp2"
             ],
-            "keyword": [
-                "legislation",
-                "osh",
-                "policy",
-                "state system",
-                "tax",
-                "tobacco"
+            "title": "Weekly Rates of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OSHData Support",
                 "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/2dwv-vfam",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Tax/2dwv-vfam",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation-Tax. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include state taxes on combustible (cigarettes, cigars, little cigars, pipe tobacco, and roll-your-own tobacco) tobacco products, non-combustible (snus, moist snuff, dry snuff, chewing tobacco) tobacco products, and tax stamps.",
-            "title": "CDC STATE System Tobacco Legislation - Tax",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72898,47 +72875,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Tax/2dwv-vfam",
+            "identifier": "https://data.cdc.gov/api/views/2dwv-vfam",
+            "issued": "2023-07-14",
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "state system",
+                "tax",
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
+            "title": "CDC STATE System Tobacco Legislation - Tax"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vqyf-z2g3",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/vqyf-z2g3",
             "description": "NNDSS - TABLE 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNotes:\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\nFootnotes:\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.",
-            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72961,90 +72937,93 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vqyf-z2g3",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "arboviral diseases",
+                "jamestown canyon virus disease",
+                "la crosse virus disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "powassan virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vqyf-z2g3",
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
+            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/gngx-pf4v",
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
-            "identifier": "4b7403de-2d4b-5b0e-a3c3-af9e6a0152d7",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard MEASURE_VALUE vCORESET.1.1-test (coreset-local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/MEASURE_VALUE.csv",
-                    "description": "Scorecard MEASURE_VALUE vCORESET.1.1-test (coreset-local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard MEASURE_VALUE vCORESET.1.1-test (coreset-local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/MEASURE_VALUE.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard MEASURE_VALUE vCORESET.1.1-test (coreset-local)"
                 }
             ],
+            "identifier": "4b7403de-2d4b-5b0e-a3c3-af9e6a0152d7",
+            "issued": "2024-05-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/gngx-pf4v",
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
+            "title": "Scorecard MEASURE_VALUE vCORESET.1.1-test (coreset-local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hrdz-jaxc",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-03-01/2023-11-24",
-            "modified": "2025-01-13",
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
-            "identifier": "https://data.cdc.gov/api/views/hrdz-jaxc",
             "description": "<b>Note:</b>\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis table summarizes COVID-19 case and death data submitted to CDC as case reports for the line-level dataset. Case and death counts are stratified according to sex, age, and race and ethnicity at regional and national levels. Data for US territories are included in case and death counts, but not population counts. Weekly cumulative counts with five or fewer cases or deaths are not reported to protect confidentiality of patients. Records with unknown or missing sex, age, or race and ethnicity and of multiple, non-Hispanic race and ethnicity are included in case and death totals. COVID-19 case and death data are provisional and are subject to change. Visualization of COVID-19 case and death rate trends by demographic variables may be viewed on COVID Data Tracker (<a href=\"https://covid.cdc.gov/covid-data-tracker/#demographicsovertime\">https://covid.cdc.gov/covid-data-tracker/#demographicsovertime</a>).",
-            "title": "COVID-19 Weekly Cases and Deaths by Age, Race/Ethnicity, and Sex - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73067,48 +73046,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/hrdz-jaxc",
+            "issued": "2023-06-15",
+            "keyword": [
+                "case",
+                "community transmission",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "laboratory"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hrdz-jaxc",
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
+            "temporal": "2020-03-01/2023-11-24",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "COVID-19 Weekly Cases and Deaths by Age, Race/Ethnicity, and Sex - ARCHIVED"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -73131,47 +73108,47 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -73194,20 +73171,56 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2000",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2000) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2000-nid13622",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2000-nid13622"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2000-nid13622",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -73220,66 +73233,29 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2000",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2000-nid13622",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2000)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2000-nid13622",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2000) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2000-nid13622"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2000)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n3wf-wtep",
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
-                "shiga toxin-producing e. coli",
-                "shigellosis",
-                "stec",
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
-            "identifier": "https://data.cdc.gov/api/views/n3wf-wtep",
```

