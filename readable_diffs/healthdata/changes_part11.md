# Change History for healthdata.json (Part 11)

### Changes from 31606f9 to dd2190f (Part 10/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "title": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135222,53 +135199,58 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h4pd-hu6x",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "arboviral diseases",
+                "nedss",
+                "netss",
+                "nndss",
+                "st. louis virus disease",
+                "west nile virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/h4pd-hu6x",
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
+            "title": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/6ia3-k3g2",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "data distribution",
-                "dataset",
-                "health services research"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6ia3-k3g2",
             "description": "The Health Services Research Projects in Progress (HSRProj) was a dataset of ongoing health services research and public health projects containing descriptions of research in progress funded by federal and private grants and contracts.\n\nThis project was retired September 14, 2021.",
-            "title": "Health Services Research Projects in Progress (HSRProj)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/HSRProject/",
-                    "description": "Download previous HSRProj datasets of health service research and public health projects in XML format.",
                     "@type": "dcat:Distribution",
+                    "description": "Download previous HSRProj datasets of health service research and public health projects in XML format.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/HSRProject/",
+                    "mediaType": "text/html",
                     "title": "Download - HSRProj"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nlm.nih.gov/nichsr/hsrprojset_xml_element_descriptions.html#HSRProjRecordSet",
-                    "description": "Sample XML data is contained within the HTML document.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample XML data is contained within the HTML document.",
+                    "downloadURL": "https://www.nlm.nih.gov/nichsr/hsrprojset_xml_element_descriptions.html#HSRProjRecordSet",
+                    "mediaType": "text/html",
                     "title": "Documentation - XML Element Descriptions, Attributes, and Sample Data"
                 },
                 {
@@ -135278,71 +135260,72 @@
                     "title": "About the Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6ia3-k3g2",
+            "issued": "2020-09-22",
+            "keyword": [
+                "data distribution",
+                "dataset",
+                "health services research"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/6ia3-k3g2",
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
-            "landingPage": "https://healthdata.gov/dataset/hivaids-testing-sites-and-locator-services",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The HIV Testing Sites &amp; Care Services Locator is a first-of-its-kind, location-based search tool that allows you to search for testing services, housing providers, health centers and other service providers near your current location.</p>",
+            "identifier": "54f56a12-8a8d-4c32-bebe-521e0362a451",
             "issued": "2013-04-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "department-of-health-human-services",
                 "health care providers",
                 "treatments"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/hivaids-testing-sites-and-locator-services",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "54f56a12-8a8d-4c32-bebe-521e0362a451",
-            "description": "<p>The HIV Testing Sites &amp; Care Services Locator is a first-of-its-kind, location-based search tool that allows you to search for testing services, housing providers, health centers and other service providers near your current location.</p>",
-            "title": "HIV/AIDS testing sites and locator services",
-            "programCode": [
-                "009:027"
-            ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "title": "HIV/AIDS testing sites and locator services"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -135365,21 +135348,51 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2011",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2011) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2011-nid13540",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2011-nid13540"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2011-nid13540",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -135392,40 +135405,40 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2011",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2011-nid13540",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2011)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2011-nid13540",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2011) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2011-nid13540"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2011)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-i-nys-1976",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This dataset contains parent and youth data for the National<br />\nYouth Survey. Youths and one of their parents or legal guardians were<br />\ninterviewed in early 1977 about events and behavior occurring during<br />\ncalendar year 1976. Included is information on the demographics and<br />\nsocioeconomic status of respondents, disruptive events in the home,<br />\nneighborhood problems, parental aspirations for youth, labeling,<br />\nintegration of family and peer contexts, attitudes toward deviance in<br />\nadults and juveniles, parental discipline, community involvement, and<br />\ndrug use.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Youth Survey US:  Wave I (NYS-1976) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-i-nys-1976-nid13552",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-i-nys-1976-nid13552"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-i-nys-1976-nid13552",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "aspirations",
                 "behavior problems",
@@ -135456,66 +135469,29 @@
                 "victimization",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-i-nys-1976",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-i-nys-1976-nid13552",
-            "description": "<p>This dataset contains parent and youth data for the National<br />\nYouth Survey. Youths and one of their parents or legal guardians were<br />\ninterviewed in early 1977 about events and behavior occurring during<br />\ncalendar year 1976. Included is information on the demographics and<br />\nsocioeconomic status of respondents, disruptive events in the home,<br />\nneighborhood problems, parental aspirations for youth, labeling,<br />\nintegration of family and peer contexts, attitudes toward deviance in<br />\nadults and juveniles, parental discipline, community involvement, and<br />\ndrug use.This study has 1 Data Set.</p>",
-            "title": "National Youth Survey US:  Wave I (NYS-1976)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-i-nys-1976-nid13552",
-                    "description": "National Youth Survey US:  Wave I (NYS-1976) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-i-nys-1976-nid13552"
-                }
-            ]
+            "title": "National Youth Survey US:  Wave I (NYS-1976)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -135538,39 +135514,46 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1O.  Hansen's disease to Hantavirus pulmonary syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/vqff-ff7g",
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
-            "identifier": "https://data.cdc.gov/api/views/vqff-ff7g",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 4 - Atlanta",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135593,41 +135576,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vqff-ff7g",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/vqff-ff7g",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 4 - Atlanta"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ucjd-qcux",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-10-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-25",
-            "keyword": [
-                "exchange puf",
-                "marketplace puf",
-                "py2023",
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
-            "identifier": "d722880d-4526-4f54-a87d-e25bdf7891d2",
             "description": "The Transparency in Coverage PUF (TC-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The PUF contains data on issuer and plan-level claims, appeals, and active URL data. The PY2023 PUF contains data from PY2021 for issuers participating in the Exchange in PY2021.",
-            "title": "Transparency in Coverage PUF - PY2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135635,36 +135617,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "d722880d-4526-4f54-a87d-e25bdf7891d2",
+            "issued": "2022-10-14",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2023",
+                "transparency in coverage"
+            ],
+            "landingPage": "https://healthdata.gov/d/ucjd-qcux",
+            "modified": "2022-10-25",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Transparency in Coverage PUF - PY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/DrugSafety/PostmarketDrugSafetyInformationforPatientsandProviders/ucm111350.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-12",
-            "keyword": [
-                "cder",
-                "rems"
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
-            "identifier": "6c697267-fe17-4c66-8c6d-da38ab9b723b",
             "description": "The Food and Drug Administration Amendments Act of 2007 gave FDA the authority to require a Risk Evaluation and Mitigation Strategy (REMS) from manufacturers to ensure that the benefits of a drug or biological product outweigh its risks.",
-            "title": "Approved Risk Evaluation and Mitigation Strategies",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135672,35 +135655,36 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "6c697267-fe17-4c66-8c6d-da38ab9b723b",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder",
+                "rems"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/DrugSafety/PostmarketDrugSafetyInformationforPatientsandProviders/ucm111350.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-12",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Approved Risk Evaluation and Mitigation Strategies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ucv6-xg6i",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
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
-            "identifier": "71b2ad7d-b821-4025-aff6-6784a51fa0ea",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-09-2024-to-12-15-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135708,35 +135692,35 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "71b2ad7d-b821-4025-aff6-6784a51fa0ea",
+            "issued": "2024-12-18",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/ucv6-xg6i",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-09-2024-to-12-15-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma_pas.cfm",
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
-            "identifier": "910c9a83-0447-4c05-b418-c2f49dd83b1b",
             "description": "The CDRH Post-Approval Studies Program encompasses design, tracking, oversight, and review responsibilities for studies mandated as a condition of approval of a premarket approval (PMA) application, protocol development product (PDP) application, or humanitarian device exemption (HDE) application. The program helps ensure that well-designed post-approval studies (PAS) are conducted effectively and efficiently and in the least burdensome manner.",
-            "title": "Post-Approval Studies",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135744,44 +135728,37 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "910c9a83-0447-4c05-b418-c2f49dd83b1b",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma_pas.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Post-Approval Studies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-ndi.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2014/2017",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/NHCS-Codebook-Mortality-Variables.pdf"
-            ],
-            "keyword": [
-                "linked ndi data",
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
-            "identifier": "https://data.cdc.gov/api/views/tuza-3b7w",
-            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from National Hospital Care Survey (NHCS) by augmenting it with mortality data from the National Death Index (NDI). Linkage of NHCS data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality.",
-            "title": "National Hospital Care Survey (NHCS) Linked to National Death Index (NDI) Data",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 6) here: https://www.cdc.gov/nchs/data/datalinkage/NHCS16-NDI16-17-Methodology-Analytic-Consider.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from National Hospital Care Survey (NHCS) by augmenting it with mortality data from the National Death Index (NDI). Linkage of NHCS data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135789,52 +135766,47 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 6) here: https://www.cdc.gov/nchs/data/datalinkage/NHCS16-NDI16-17-Methodology-Analytic-Consider.pdf",
+            "identifier": "https://data.cdc.gov/api/views/tuza-3b7w",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-23",
+            "keyword": [
+                "linked ndi data",
+                "nhcs",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-ndi.htm",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/NHCS-Codebook-Mortality-Variables.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "2014/2017",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Care Survey (NHCS) Linked to National Death Index (NDI) Data"
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
-            "identifier": "https://data.cdc.gov/api/views/kmvs-jkvx",
             "description": "This dataset contains model-based county-level estimates for the PLACES 2021 release in GIS-friendly format. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. Project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2019 or 2018 county population estimates, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census 2015 county boundary file in a GIS system to produce maps for 29 measures at the county level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=024cf3f6f59e49fe8c70e0e5410fe3cf",
-            "title": "PLACES: County Data (GIS Friendly Format), 2021 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -135857,20 +135829,61 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kmvs-jkvx",
+            "issued": "2022-10-11",
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
+            "title": "PLACES: County Data (GIS Friendly Format), 2021 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-sexual-violence-resource-center-nsvrc",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NSVRC",
+                "hasEmail": "mailto:resources@nsvrc.org"
+            },
+            "dataQuality": true,
+            "description": "<p>The National Sexual Violence Resource Center (NSVRC) is a national information and resource hub relating to all aspects of sexual violence.</p>\n<p>NSVRC staff collect and disseminate a wide range of resources on sexual violence including statistics, research, position statements, statutes, training curricula, prevention initiatives and program information. With these resources, NSVRC assists coalitions, advocates and others interested in understanding and eliminating sexual violence. NSVRC has an active and diverse Advisory Council that assists and advises staff and ensures a broad national perspective. NSVRC also enjoys a strong partnership with state, territory and tribal anti-sexual assault coalitions and allied organizations.</p>\n<p>NSVRC is funded through a cooperative agreement from the Centers for Disease Control and Prevention (CDC) Division of Violence Prevention.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nsvrc.org/",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "identifier": "c9b629ba-3935-4acb-b65c-b35bc3e87def",
             "issued": "2014-04-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "abuse",
                 "curricula",
@@ -135884,42 +135897,41 @@
                 "violence",
                 "women"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NSVRC",
-                "hasEmail": "mailto:resources@nsvrc.org"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-sexual-violence-resource-center-nsvrc",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:096"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "c9b629ba-3935-4acb-b65c-b35bc3e87def",
-            "description": "<p>The National Sexual Violence Resource Center (NSVRC) is a national information and resource hub relating to all aspects of sexual violence.</p>\n<p>NSVRC staff collect and disseminate a wide range of resources on sexual violence including statistics, research, position statements, statutes, training curricula, prevention initiatives and program information. With these resources, NSVRC assists coalitions, advocates and others interested in understanding and eliminating sexual violence. NSVRC has an active and diverse Advisory Council that assists and advises staff and ensures a broad national perspective. NSVRC also enjoys a strong partnership with state, territory and tribal anti-sexual assault coalitions and allied organizations.</p>\n<p>NSVRC is funded through a cooperative agreement from the Centers for Disease Control and Prevention (CDC) Division of Violence Prevention.</p>",
-            "title": "National Sexual Violence Resource Center (NSVRC)",
-            "programCode": [
-                "009:096"
-            ],
-            "distribution": [
+            "title": "National Sexual Violence Resource Center (NSVRC)"
+        },
         {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nsvrc.org/",
-                    "mediaType": "text/html",
-                    "title": "Text "
-                }
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:00"
             ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
             },
+            "dataQuality": true,
+            "description": "<p>A Web service that allows patient portals and electronic health record (EHR) systems to use existing code sets to link to relevant, authoritative health information from MedlinePlus.gov. Matches ICD-9-CM or SNOMED CT codes to related MedlinePlus consumer health information, LOINC codes to information on lab tests, and also matches NDC, RXCUI or text strings to patient medication information.</p>",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/medlineplus-connect-electronic-health-record-ehr-systems-web-service",
-            "bureauCode": [
-                "009:00"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nlm.nih.gov/medlineplus/connect/service.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool"
+                }
             ],
+            "identifier": "94200b58-3941-43fb-b316-ec5648ff0034",
             "issued": "2012-05-30",
-            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "biomedical research",
                 "connect",
@@ -135945,63 +135957,34 @@
                 "snomed ct",
                 "wellness"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/medlineplus-connect-electronic-health-record-ehr-systems-web-service",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Institutes of Health (NIH)"
             },
-            "identifier": "94200b58-3941-43fb-b316-ec5648ff0034",
-            "description": "<p>A Web service that allows patient portals and electronic health record (EHR) systems to use existing code sets to link to relevant, authoritative health information from MedlinePlus.gov. Matches ICD-9-CM or SNOMED CT codes to related MedlinePlus consumer health information, LOINC codes to information on lab tests, and also matches NDC, RXCUI or text strings to patient medication information.</p>",
-            "title": "MedlinePlus Connect for Electronic Health Record (EHR) Systems - Web Service",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nlm.nih.gov/medlineplus/connect/service.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "MedlinePlus Connect for Electronic Health Record (EHR) Systems - Web Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/pvxp-wfpg",
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
-            "identifier": "https://data.cdc.gov/api/views/pvxp-wfpg",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 3 - Philadelphia",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136024,48 +136007,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/pvxp-wfpg",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/pvxp-wfpg",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 3 - Philadelphia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/edtz-vibe",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "2014",
-                "anaplasma phagocytophilum",
-                "ehrlichia chaffeensis",
-                "ehrlichiosis/anaplasmosis",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "undetermined",
-                "week",
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
-            "identifier": "https://data.cdc.gov/api/views/edtz-vibe",
             "description": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136088,85 +136062,95 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/edtz-vibe",
+            "issued": "2015-01-08",
+            "keyword": [
+                "2014",
+                "anaplasma phagocytophilum",
+                "ehrlichia chaffeensis",
+                "ehrlichiosis/anaplasmosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined",
+                "week",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/edtz-vibe",
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
+            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/uhcs-g759",
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
-            "identifier": "253c29a7-f6dd-5d91-8c1f-142e1a436a66",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet pillar v2.10.64 (coreset-cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
-                    "description": "CoreSet pillar v2.10.64 (coreset-cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet pillar v2.10.64 (coreset-cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet pillar v2.10.64 (coreset-cmsdev)"
                 }
             ],
+            "identifier": "253c29a7-f6dd-5d91-8c1f-142e1a436a66",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/uhcs-g759",
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
+            "title": "CoreSet pillar v2.10.64 (coreset-cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/aids-info",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-08-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "epidemiology",
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
-            "identifier": "3011ab57-28d8-4baf-8894-7b4b8b80eb06",
+            "dataQuality": true,
             "description": "<p>Aids Info</p>",
-            "title": "AIDS Info",
-            "programCode": [
-                "009:027"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136175,42 +136159,39 @@
                     "title": "API "
                 }
             ],
+            "identifier": "3011ab57-28d8-4baf-8894-7b4b8b80eb06",
+            "issued": "2012-08-22",
+            "keyword": [
+                "epidemiology",
+                "national-institutes-of-health-nih-department-of-health-human-services"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/aids-info",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:027"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
+            },
+            "title": "AIDS Info"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/npals/index.html",
+            "accrualPeriodicity": "Irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/application-process/submission.html.",
-            "issued": "2022-06-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2021-07-21",
-            "modified": "2025-01-13",
-            "keyword": [
-                "covid-19",
-                "long-term care",
-                "research-data-center",
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
-            "identifier": "https://data.cdc.gov/api/views/nbs2-kemu",
-            "description": "The National Post-acute and Long-term Care Study (NPALS) is a biennial study of major post-acute and long-term care providers and their services users. Seven provider settings are included. NPALS collects survey data on the residential care community and adult day services sectors, and uses administrative data (available from CMS) for home health, nursing home, hospice, inpatient rehabilitation, and long-term care hospital sectors.\nThe goals of the study are to: estimate the supply of paid, regulated post-acute and long-term care services providers; estimate key policy-relevant characteristics and practices of these providers; estimate the number of post-acute and long-term care services users; estimate key policy-relevant characteristics of these users; produce national and state estimates where feasible; compare across provider sectors; and monitor trends over time.",
-            "title": "National Post-acute and Long-term Care Study: Residential Care Community Restricted Dataset",
+            "describedBy": "https://www.cdc.gov/nchs/data/npals/2020-NPALS-RCC-Questionnaire-Community.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The National Post-acute and Long-term Care Study (NPALS) is a biennial study of major post-acute and long-term care providers and their services users. Seven provider settings are included. NPALS collects survey data on the residential care community and adult day services sectors, and uses administrative data (available from CMS) for home health, nursing home, hospice, inpatient rehabilitation, and long-term care hospital sectors.\nThe goals of the study are to: estimate the supply of paid, regulated post-acute and long-term care services providers; estimate key policy-relevant characteristics and practices of these providers; estimate the number of post-acute and long-term care services users; estimate key policy-relevant characteristics of these users; produce national and state estimates where feasible; compare across provider sectors; and monitor trends over time.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136219,51 +136200,47 @@
                     "title": "National Post-acute and Long-term Care Study: Residential Care Community Restricted Dataset"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/npals/2020-NPALS-RCC-Questionnaire-Community.pdf",
+            "identifier": "https://data.cdc.gov/api/views/nbs2-kemu",
+            "issued": "2022-06-16",
+            "keyword": [
+                "covid-19",
+                "long-term care",
+                "research-data-center",
+                "residential care communities"
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
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/application-process/submission.html.",
+            "spatial": "United States",
+            "temporal": "2020-01-01/2021-07-21",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Post-acute and Long-term Care Study: Residential Care Community Restricted Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/23gt-ssfe",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-18",
-            "keyword": [
-                "2014",
-                "invasive pneumococcal disease",
-                "legionellosis",
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
-            "identifier": "https://data.cdc.gov/api/views/23gt-ssfe",
             "description": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd\ufffd Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as < 5 years. Since 2010, case notifications for this condition were consolidated under one event code for Invasive pneumococcal disease.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136286,95 +136263,92 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/23gt-ssfe",
+            "issued": "2019-01-18",
+            "keyword": [
+                "2014",
+                "invasive pneumococcal disease",
+                "legionellosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/23gt-ssfe",
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
+            "title": "NNDSS - Table II. Invasive Pneumococcal to Legionellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ui9d-wyxf",
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
-            "identifier": "90196fbe-8c6f-5260-9c9d-02b1b455cf0f",
             "description": "This is a dataset created for use by the Scorecard website, and is not intended for use outside that application.",
-            "title": "Scorecard pillar",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/pillar.csv",
-                    "description": "Scorecard pillar",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard pillar",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard pillar"
                 }
             ],
+            "identifier": "90196fbe-8c6f-5260-9c9d-02b1b455cf0f",
+            "issued": "2023-03-28",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/ui9d-wyxf",
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
+            "title": "Scorecard pillar"
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
-                "city",
-                "outcomes",
-                "place",
-                "places",
-                "prevalence",
-                "prevention",
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
-            "identifier": "https://data.cdc.gov/api/views/q8xq-ygsk",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
             "description": "This dataset contains model-based place (incorporated and census designated places) level estimates for the PLACES project 2020 release. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 27 measures: 5 chronic disease-related unhealthy behaviors, 13 health outcomes, and 9 on use of preventive services. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates  include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2010 population data, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Place Data 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136397,41 +136371,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
+            "identifier": "https://data.cdc.gov/api/views/q8xq-ygsk",
+            "issued": "2021-09-29",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "city",
+                "outcomes",
+                "place",
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
+            "title": "PLACES: Local Data for Better Health, Place Data 2020 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/ihs-facility-locator",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-07-31",
-            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
-            "keyword": [
-                "indian-health-service",
-                "health care providers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Data",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Indian Health Service"
-            },
-            "identifier": "87105064-444b-4e33-b5f7-f686ffe9c414",
+            "dataQuality": true,
             "description": "<p>This map can be used to find an Indian Health Service, Tribal or Urban Indian Health Program facility. This map can be used to:&#13;<br />\nZoom in to a general location to see if there is a facility in that region.&#13;<br />\nEnter your current location in the form to see the facilities available.&#13;<br />\nFind a specific facility by selecting the \"Facility Information\" tab and typing in the name of the facility that you are trying to find.&#13;</p>",
-            "title": "IHS Facility Locator",
-            "programCode": [
-                "009:024"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136440,40 +136423,38 @@
                     "title": "XLS "
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "87105064-444b-4e33-b5f7-f686ffe9c414",
+            "issued": "2013-07-31",
+            "keyword": [
+                "indian-health-service",
+                "health care providers"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/ihs-facility-locator",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2025-01-28",
+            "programCode": [
+                "009:024"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Indian Health Service"
+            },
+            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
+            "title": "IHS Facility Locator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/uj9c-xffk",
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
-            "identifier": "8ada60fc-9bf0-4034-912e-de57e0624ecb",
             "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2022 Medical SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136481,42 +136462,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "8ada60fc-9bf0-4034-912e-de57e0624ecb",
+            "issued": "2022-08-10",
+            "keyword": [
+                "py2022",
+                "qhp",
+                "qhp landscape",
+                "shop",
+                "shop market medical"
+            ],
+            "landingPage": "https://healthdata.gov/d/uj9c-xffk",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2022 Medical SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/usyq-s7ip",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
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
-            "identifier": "https://data.cdc.gov/api/views/usyq-s7ip",
             "description": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136539,39 +136516,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/usyq-s7ip",
+            "issued": "2019-04-23",
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
+            "landingPage": "https://data.cdc.gov/d/usyq-s7ip",
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
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/food-safety-information-rss-feed",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-08-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "food products",
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
-            "identifier": "58aa7a22-f890-4cf9-9f34-f953d4a96871",
+            "dataQuality": true,
             "description": "<p>This is an RSS Feed of Food Safety information that\u2019s produced in real-time by the CDC. This RSS feed is the integration of two other XML feeds, one from the USDA's Food Safety Inspection Service (FSIS) - <a href=\"http://www.fsis.usda.gov/RSS/usdarss.xml\">http://www.fsis.usda.gov/RSS/usdarss.xml</a> - and one from the FDA's Food Safety Recalls - <a href=\"http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/FoodSafety/rss.xml\">http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/FoodSafety/...</a>. Most users will prefer the CDC feed linked above, but developers may prefer the individual XML feeds.</p>",
-            "title": "Food Safety Information RSS feed",
-            "programCode": [
-                "005:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136580,79 +136564,82 @@
                     "title": "XML "
                 }
             ],
+            "identifier": "58aa7a22-f890-4cf9-9f34-f953d4a96871",
+            "issued": "2012-08-28",
+            "keyword": [
+                "food products",
+                "safety"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/food-safety-information-rss-feed",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "modified": "2023-07-25",
+            "programCode": [
+                "005:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "title": "Food Safety Information RSS feed"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/ujp5-dggr",
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
-            "identifier": "f84a8b57-39db-538b-9603-8e049bab7d8f",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard PILLAR v0.3.58-test (local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/PILLAR.csv",
-                    "description": "Scorecard PILLAR v0.3.58-test (local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard PILLAR v0.3.58-test (local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/PILLAR.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard PILLAR v0.3.58-test (local)"
                 }
             ],
+            "identifier": "f84a8b57-39db-538b-9603-8e049bab7d8f",
+            "issued": "2023-08-10",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/ujp5-dggr",
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
+            "title": "Scorecard PILLAR v0.3.58-test (local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/nmdn-2xuz",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-03-30",
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
-            "identifier": "https://data.cdc.gov/api/views/nmdn-2xuz",
             "description": "This dataset contains vaccine mandate prohibitions that were issued by 50 states, 5 territories, and the District of Columbia currently in effect. State and territorial laws are collected from publicly available government websites and cataloged and coded in HHS Protect by one coder with one or more additional coders conducting quality assurance.\nData were collected to determine when certain groups were prohibited from issuing vaccine mandates and to what groups those prohibitions applied. Data can be used to determine the status of state-issued vaccine requirement prohibitions for certain groups as of the date of last update. \nThese data are derived from publicly available state and territorial laws and official policy documents found by the CDC, Mitigation Policy Analysis Unit, and the CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 1, 2020 through _____. These data will be updated as new laws are collected. Any orders not available through publicly accessible websites are not included in this dataset. Recommendations not included in a law are not included in these data. Effective and expiration dates were coded using only the date provided in the law. These data do not necessarily represent the official position of the Centers for Disease Control and Prevention.",
-            "title": "State-Level Restrictions on Vaccine Mandate \u2013 Currently in Effect",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136675,41 +136662,35 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/nmdn-2xuz",
+            "issued": "2022-03-30",
+            "landingPage": "https://data.cdc.gov/d/nmdn-2xuz",
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
+            "title": "State-Level Restrictions on Vaccine Mandate \u2013 Currently in Effect"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -136732,41 +136713,42 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/d/ukvu-csc3",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-10-12",
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
-            "identifier": "1d3ffff8-2cf5-4cc9-a820-5879e957caa2",
             "description": "The Reference Document link for the downable Blood Disorder Treatment Spreadsheet can be accessed below under the Additional Information table under Related Documents.",
-            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 6/1/2022)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136774,39 +136756,42 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "1d3ffff8-2cf5-4cc9-a820-5879e957caa2",
+            "issued": "2022-10-12",
+            "keyword": [
+                "drug products"
+            ],
+            "landingPage": "https://healthdata.gov/d/ukvu-csc3",
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
+            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 6/1/2022)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/umgm-k5i9",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-16",
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
-            "identifier": "4b8b2176-9584-4edf-bc8e-48887cd6b0a1",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-09-to-2023-10-15",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136815,49 +136800,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-09-to-2023-10-15"
                 }
             ],
+            "identifier": "4b8b2176-9584-4edf-bc8e-48887cd6b0a1",
+            "issued": "2023-10-18",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/umgm-k5i9",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-10-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-09-to-2023-10-15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-04-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2020-12-31",
-            "modified": "2023-04-03",
-            "keyword": [
-                "age",
-                "age group",
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
-            "identifier": "https://data.cdc.gov/api/views/xmrr-rw5u",
             "description": "Provisional counts of deaths involving coronavirus disease 2019 (COVID-19) by United States county of residence and age group, from January 1, 2020 through December 31, 2020.",
-            "title": "AH Provisional COVID-19 Deaths by County and Age for 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136880,118 +136852,133 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/xmrr-rw5u",
+            "issued": "2021-04-28",
+            "keyword": [
+                "age",
+                "age group",
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
+            "modified": "2023-04-03",
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
+            "title": "AH Provisional COVID-19 Deaths by County and Age for 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/umvi-rd22",
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
-            "identifier": "afea55ca-bf11-525a-93ea-891339cc44f7",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_topicArea_measureDisplayGroups",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/topicArea_measureDisplayGroups.csv",
-                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/topicArea_measureDisplayGroups.csv",
+                    "mediaType": "text/csv",
                     "title": "topicArea_measureDisplayGroups csv file"
                 }
             ],
+            "identifier": "afea55ca-bf11-525a-93ea-891339cc44f7",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/umvi-rd22",
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
+            "title": "featAuto_topicArea_measureDisplayGroups"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.xenbase.org/common/",
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
                 "fn": "COULOMBE, JAMES N",
                 "hasEmail": "mailto:coulombej@mail.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "e4cf43f9-56f8-4b88-8159-66043a9585fa",
+            "dataQuality": true,
             "description": "<p>Xenbase is a Xenopus laevis and Xenopus tropicalis biology and genomics resource.</p>",
-            "title": "Xenbase",
+            "identifier": "e4cf43f9-56f8-4b88-8159-66043a9585fa",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.xenbase.org/common/",
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
+            "title": "Xenbase"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/b68w-a53h",
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
-            "identifier": "https://data.cdc.gov/api/views/b68w-a53h",
             "description": "We describe design and characterization of an aerosol NanoSpotTM collector, designed for collection of airborne particles on a microscopy substrate for direct electron microscopy, optical microscopy, and laser spectroscopy analysis. The collector implements a water-based, laminar-flow, condensation growth technique, followed by impaction onto an optical/electron microscopy substrate or a transmission electron microscopy grid for direct analysis. The compact design employs three parallel growth tubes allowing a sampling flow rate of 1.2 L min-1. Each of the three growth tubes consists of three-temperature regions, for controlling the water vapor saturation profile and exit dew point. Following the droplet growth, the three streams merge into one flow and a converging nozzle enhances focusing of the grown droplets into a tight beam, prior to their final impaction on the warm surface of the collection substrate. A miniscule sample deposition area is attained for effective coupling with microscopic and spectroscopic analysis. Experiments were conducted for the acquisition of the size-dependent collection efficiency, the uniformity of the spot deposit, the surface density distribution of the collected particles, and the aerosol concentration effect on the triple-tube NanoSpotTM Collector. Particles as small as 7 nm could be activated and collected on the electron microscopy stub. A spot deposit of approximately 0.7-mm diameter is formed for particles over a broad particle diameter range. The collected particle samples were analyzed using electron microscopy and Raman spectroscopy for the acquisition of the particle spatial distribution, the spot sample uniformity, and the analyte concentration. Finally, the NanoSpotTM collector\u2019s analytical measurement sensitivity for laser Raman analysis and the counting statistics for fiber count measurement using optical microscopy were calculated and were compared with those of the conventional aerosol sampling methods.",
-            "title": "NanoSpotTM Collector for Aerosol Sample Collection for Direct Microscopy and Spectroscopy Analysis-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -136999,45 +136986,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/b68w-a53h",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/b68w-a53h",
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
+            "title": "NanoSpotTM Collector for Aerosol Sample Collection for Direct Microscopy and Spectroscopy Analysis-Dataset"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -137060,47 +137037,45 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -137123,35 +137098,47 @@
                     "mediaType": "application/xml"
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2021-09-13",
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
+            "title": "U.S. State and Territorial Orders Closing and Reopening Restaurants Issued from March 11, 2020 through August 15, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xfk2-6xmb",
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
-            "identifier": "https://data.cdc.gov/api/views/xfk2-6xmb",
             "description": "Per- and polyfluoroalkyl substances (PFAS) are a large group of synthetic man-made surfactants of over 12,000 compounds that are incorporated into numerous products for their chemical and physical properties.  Numerous PFAS have been associated with adverse health effects.  Although there is a high potential for dermal exposure, these studies are lacking.  The present study evaluated the systemic and immunotoxicity of sub-chronic 28- or 10-day dermal exposure, respectively, to of PFHpS (0.3125-2.5% or 7.82-62.5 mg/kg/dose) or PFOS (0.5% or 12.5 mg/kg/dose) in a murine model.",
-            "title": "Systemic and immunotoxicity induced by topical application of perfluoroheptane sulfonic acid (PFHpS) or perfluorooctane sulfonic acid (PFOS) in a murine model",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137159,81 +137146,81 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xfk2-6xmb",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/xfk2-6xmb",
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
+            "title": "Systemic and immunotoxicity induced by topical application of perfluoroheptane sulfonic acid (PFHpS) or perfluorooctane sulfonic acid (PFOS) in a murine model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/uqfv-i6nk",
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
-            "identifier": "75fe7241-d60e-525f-bf3e-e94acfda708b",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure v2.11.16 (dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/measure.csv",
-                    "description": "Scorecard measure v2.11.16 (dev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure v2.11.16 (dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure v2.11.16 (dev)"
                 }
             ],
+            "identifier": "75fe7241-d60e-525f-bf3e-e94acfda708b",
+            "issued": "2023-03-28",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/uqfv-i6nk",
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
+            "title": "Scorecard measure v2.11.16 (dev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xd2k-siai",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-18",
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
-            "identifier": "https://data.cdc.gov/api/views/xd2k-siai",
             "description": "In the lung, carcinogenesis is a multi-stage process that includes initiation by a genotoxic agent, promotion that expands the population of cells with damaged DNA to form a tumor, and progression from benign to malignant neoplasms. We have previously shown that Mitsui-7, a long and rigid multi-walled carbon nanotube (MWCNT), promotes pulmonary carcinogenesis in a mouse model. To investigate the potential exposure threshold and dose-response for tumor promotion by this MWCNT, 3-methylcholanthrene (MC) initiated (10 \u03bcg/g, i.p., once) or vehicle (corn oil) treated B6C3F1 mice were exposed by inhalation to filtered air or MWCNT (5 mg/m3) for 5 hours/day for 0, 2, 5, or 10 days and were followed for 17 months  post-exposure for evidence of lung tumors.",
-            "title": "Potent Lung Tumor Promotion by Inhaled MWCNT",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137241,44 +137228,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xd2k-siai",
+            "issued": "2024-11-18",
+            "landingPage": "https://data.cdc.gov/d/xd2k-siai",
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
+            "title": "Potent Lung Tumor Promotion by Inhaled MWCNT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/q2dj-esu7",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/q2dj-esu7",
             "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses. With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2012 have been variant influenza viruses.",
-            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137301,20 +137279,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/q2dj-esu7",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a virus infections",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/q2dj-esu7",
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
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2004",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the  Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2004) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2004-nid13545",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2004-nid13545"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2004-nid13545",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -137327,59 +137340,29 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2004",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2004-nid13545",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the  Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2004)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2004-nid13545",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2004) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2004-nid13545"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2004)"
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
@@ -137387,87 +137370,86 @@
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
+            "title": "University of Illinois at Chicago Health Policy Center - Funding Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/urf3-qwh7",
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
-                "telehealth",
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
-            "identifier": "651fa253-4dd4-4867-8725-2b5ae1dd5ce9",
             "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of\u00a0services provided via telehealth, including live audio video, remote patient monitoring, store and forward, and other telehealth, to Medicaid and CHIP beneficiaries, by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating telehealth services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Telehealth Services Provided to the Medicaid and CHIP Population",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Telehealth-Services-Provided-to-the-MedicaidCHIP-Population.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of\u00a0services provided via telehealth, including live audio video, remote patient monitoring, store and forward, and other telehealth, to Medicaid and CHIP beneficiaries, by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating telehealth services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of\u00a0services provided via telehealth, including live audio video, remote patient monitoring, store and forward, and other telehealth, to Medicaid and CHIP beneficiaries, by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating telehealth services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Telehealth-Services-Provided-to-the-MedicaidCHIP-Population.csv",
+                    "mediaType": "text/csv",
                     "title": "Telehealth Services Provided to the Medicaid and CHIP Population"
                 }
             ],
+            "identifier": "651fa253-4dd4-4867-8725-2b5ae1dd5ce9",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "service use",
+                "telehealth",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/urf3-qwh7",
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
+            "title": "Telehealth Services Provided to the Medicaid and CHIP Population"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/igaz-icki",
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
-            "identifier": "https://data.cdc.gov/api/views/igaz-icki",
             "description": "This dataset includes deidentified data on patients receiving artesunate through the National Artesunate for Severe Malaria Program from April- December 2019. \n\nThis dataset contains the data from the case report form only.\nPlease see the links below for the other datasets and see the attached document 'Guide to NSAMP Datasets':\nData on Artesunate Dosing- https://data.cdc.gov/dataset/National-Artesunate-for-Severe-Malaria-Program-Art/qan4-gt4k\nData on Follow-On Antimalarial Dosing- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Fol/g3k9-gyw7\nData on Microscopy (Parasitemia values)- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Mic/v2k9-ctv4\n\nAll data can be easily linked using the ParticipantID field, a unique ID number assigned to each participant.",
-            "title": "National Artesunate for Severe Malaria Program Case Report Data- April to December 2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137490,22 +137472,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/igaz-icki",
+            "issued": "2020-04-10",
+            "keyword": [
+                "artesunate",
+                "division of parasitic diseases and malaria",
+                "malaria"
+            ],
+            "landingPage": "https://data.cdc.gov/d/igaz-icki",
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
+            "title": "National Artesunate for Severe Malaria Program Case Report Data- April to December 2019"
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
@@ -137514,65 +137527,37 @@
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
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "1989/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - All-County Natality File with Exact Date of Birth"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/uryh-z79n",
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
-            "identifier": "b672964d-7038-405c-9338-303f9a4d6c28",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-30-to-2023-02-05",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137581,93 +137566,84 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-30-to-2023-02-05"
                 }
             ],
+            "identifier": "b672964d-7038-405c-9338-303f9a4d6c28",
+            "issued": "2023-02-09",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/uryh-z79n",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-02-07",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-30-to-2023-02-05"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/us3r-u9zr",
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
-            "identifier": "44cf9d94-81fa-5190-8541-de8f16fc43d5",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_measure_concernLevel",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_concernLevel.csv",
-                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_concernLevel.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_concernLevel csv file"
                 }
             ],
+            "identifier": "44cf9d94-81fa-5190-8541-de8f16fc43d5",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/us3r-u9zr",
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
+            "title": "implAuto_measure_concernLevel"
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
@@ -137690,46 +137666,50 @@
                     "mediaType": "application/xml"
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
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-11-15",
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
+            "title": "Nutrition, Physical Activity, and Obesity - American Community Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i2a4-xk9k",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-08-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-05-01/2023-11-10",
-            "modified": "2025-01-14",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "mmtc",
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
-            "identifier": "https://data.cdc.gov/api/views/i2a4-xk9k",
             "description": "This dataset includes COVID-19 self-test result data voluntarily reported by users of tests through the MakeMyTestCount website (makemytestcount.org). All fields are self-reported by the user with the exception of  fields derived from the self-reported zip code. This dataset will be updated monthly. If there are any questions, please direct them to the data steward, Jasmine Chaitram <zoa6@cdc.gov>. \n\nThis dataset includes the following self-reported data:  \n- Date (by week)\u2013 date of test shown by week starting date  \n- Age group (years) \u2013 age of individual taking the test, categorized into the following: 2-4, 5-11, 12-15, 16-17, 18-29, 30-39, 40-49, 50-64, 65-74, 75+  \n- Race \u2013 race of individual taking the test: American Indian or Alaska Native, Asian, Black, Native Hawaiian or Other Pacific Islander, White, Multiple or Other, missing \n- Ethnicity \u2013 ethnicity of individual taking the test: Hispanic, Non-Hispanic, missing \n- Sex \u2013 sex of individual taking the test: male, female, missing \n- Test result \u2013 positive, negative, inconclusive \n\nThe dataset also includes the following columns to support analyses. These columns are based on the self-reported zip code:  \n- State abbreviation  \n- State name  \n- State FIPS code \n- FEMA region  \n\nPlease note that there are limitations with these data, including: \n\n1. Data are not comprehensive of all self-tests performed. Data represent results voluntarily reported by an individual via the MakeMyTestCount website. These data do not include self-test results that were reported to state and local health departments if they were not also reported through the MakeMyTestCount website. The true denominator (known number of tests completed in the US) cannot be ascertained and reflects a small fraction of the number of self-tests used.    \n\n2. Data are not verified. The quality of specimen, appropriate execution of self-test, result produced, and person tested are unverified; therefore, reported interpretation of results cannot be confirmed. All results and accompanying demographic information are also self-reported and cannot be verified.  \n\n3. Data reports are not complete. Individual submissions vary widely in terms of the data elements collected. Not all data elements are required (only date, age, and zip code), and some results are missing demographic information.  \n\n4. Data are not representative. Based on the limited number of self-reported test results, this dataset is not representative of the use of self-testing by demographic, nor is the dataset inclusive of all self-testing completed within each jurisdiction. This dataset represents a small proportion of overall COVID-19 testing conducted and reported volumes are much lower than testing conducted in point of care and laboratory settings.   \n\n5. Data represent individual test results, not persons tested. Data in this dataset are not linkable and do not allow for analyses around serial testing. Data also cannot be disaggregated to identify multiple reports by the same individual.  \n\nAll analyses should be completed with these limitations in mind.  \n\nFor more information about the challenges and opportunities around self-test data, please refer to the following article: Ritchey MD, Rosenblum HG, Del Guercio K, et al. COVID-19 Self-Test Data: Challenges and Opportunities \u2014 United States, October 31, 2021\u2013June 11, 2022. MMWR Morb Mortal Wkly Rep 2022;71:1005\u20131010. DOI: http://dx.doi.org/10.15585/mmwr.mm7132a1",
-            "title": "U.S. COVID-19 MakeMyTestCount Self-Test Data",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137752,40 +137732,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/i2a4-xk9k",
+            "issued": "2023-08-10",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "mmtc",
+                "otc",
+                "self-tests"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i2a4-xk9k",
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
+            "temporal": "2022-05-01/2023-11-10",
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. COVID-19 MakeMyTestCount Self-Test Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5biu-jjj3",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vsafe@cdc.gov",
                 "hasEmail": "mailto:vsafe@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/5biu-jjj3",
             "description": "Users of the v-safe data are required to adhere to the following standards for the analysis and reporting of research data. All research results must be presented and/or published in a manner that protects the confidentiality of participants. v-safe data will not be presented and/or published in any way in which an individual can be identified. \n\nTherefore, users will:\n<ol>\n<li>Not attempt to link or permit others to link the data with individually identified records in another database.</li>\n<li>Not attempt to learn the identity of any participant in the data and will not deliberately combine these data with other CDC or non-CDC data for the purpose of matching records to identify individuals. If you should inadvertently discover the identity of any participant, you will ensure the identity of any participant is kept confidential, and will not be used in any publications and/or presentations.</li>\n<li>Not imply or state, either in written or oral form, that interpretations based on analysis of the data reflect official CDC policies or positions.</li>\n<li>Understand that sub-national analyses are not appropriate for this national sample and will not be conducted. </li>\n<li>Understand that v-safe is a voluntary self-enrollment program requiring smartphone access; therefore, information from v-safe might not be representative or generalizable to the US population.</li></ol>\nBy clicking on the weblink below to download and use these v-safe data, you signify your agreement to comply with the above-stated terms.\n\nv-safe is an active surveillance program to monitor the safety of COVID-19 vaccines during the period when the vaccines are authorized for use under Food and Drug Administration (FDA) Emergency Use Authorization (EUA) and after vaccine licensure.\n\nThese data include MedDRA coded text responses collected through v-safe from 12/13/2020 to 06/30/2023. Please review the v-safe data user agreement before analyzing any v-safe data.",
-            "title": "v-safe COVID-19 MedDRA coded text responses",
-            "programCode": [
-                "009:037"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137793,39 +137780,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5biu-jjj3",
+            "issued": "2023-07-26",
+            "landingPage": "https://data.cdc.gov/d/5biu-jjj3",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-31",
+            "programCode": [
+                "009:037"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "v-safe COVID-19 MedDRA coded text responses"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i6st-vu2f",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-02-20",
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
-            "identifier": "https://data.cdc.gov/api/views/i6st-vu2f",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Youth Tobacco Survey (YTS) Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137833,39 +137816,39 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i6st-vu2f",
+            "issued": "2015-02-20",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i6st-vu2f",
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
+            "title": "Youth Tobacco Survey (YTS) Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/hmd/digicolls/cummings/index.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n3zq-zwvr",
             "description": "An online edition of XML-encoded speeches, articles, and Congressional Appropriations testimonies by former NLM director Martin M. Cummings, based on the collection of his papers in HMD\u2019s Modern Manuscripts collection.",
-            "title": "Martin M. Cummings and the NLM",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137874,43 +137857,40 @@
                     "title": "Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n3zq-zwvr",
+            "issued": "2021-06-30",
+            "keyword": [
+                "history of medicine",
+                "reference"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/hmd/digicolls/cummings/index.html",
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
+            "title": "Martin M. Cummings and the NLM"
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
-                "smokefree indoor air",
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
-            "identifier": "https://data.cdc.gov/api/views/wan8-w4er",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Smokefree/wan8-w4er",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC).  State Tobacco Activities Tracking and Evaluation (STATE) System.  E-Cigarette Legislation\u2014Smokefree Indoor Air. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to state legislation on smokefree indoor air in areas such as: Bars, Commercial Day Care Centers, Government Multi-Unit Housing, Government Worksites, Home-Based Day Care Centers, Hotels and Motels, Personal Vehicles, Private Multi-Unit Housing, Private Worksites, Restaurants, Bingo Halls, Casinos, Enclosed Arenas, Grocery Stores, Hospitals, Hospital Campuses, Malls, Mental Health Outpatient and Residential Facilities, Prisons, Public Transportation, Racetrack Casinos, Substance Abuse Outpatient and Residential Facilities.",
-            "title": "CDC STATE System E-Cigarette Legislation - Smokefree Indoor Air",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137933,39 +137913,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Smokefree/wan8-w4er",
+            "identifier": "https://data.cdc.gov/api/views/wan8-w4er",
+            "issued": "2023-07-18",
+            "keyword": [
+                "e-cigarette",
+                "legislation",
+                "osh",
+                "policy",
+                "smokefree indoor air",
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
+            "title": "CDC STATE System E-Cigarette Legislation - Smokefree Indoor Air"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/uu5w-8un5",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-07-11",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-10",
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
-            "identifier": "89360ee9-e669-40e2-bed5-979596c43e0b",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-03-to-2023-07-09",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -137974,37 +137959,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-03-to-2023-07-09"
                 }
             ],
+            "identifier": "89360ee9-e669-40e2-bed5-979596c43e0b",
+            "issued": "2023-07-11",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/uu5w-8un5",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-07-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-03-to-2023-07-09"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/5s4c-fa96",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "data distribution",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/5s4c-fa96",
             "description": "The Meeting Abstracts database contains selected abstracts from meetings and conferences in the subject areas of: AIDS, Health Services Research, and Space Life Sciences, published between 1990 \u2013 2010. The abstracts are organized into three collections, each available in XML file format. This dataset is no-longer updated.",
-            "title": "NLM Meeting Abstracts (NO LONGER UPDATED)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138031,35 +138014,39 @@
                     "title": "About the Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/5s4c-fa96",
+            "issued": "2020-09-22",
+            "keyword": [
+                "data distribution",
+                "dataset"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/5s4c-fa96",
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
+            "title": "NLM Meeting Abstracts (NO LONGER UPDATED)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/dtz3-sij3",
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
-            "identifier": "https://data.cdc.gov/api/views/dtz3-sij3",
             "description": "Three-dimensional printing (3DP) of manufactured goods has increased in the last 10 yrs.  The increased use of this technology has resulted in questions about the health effects of inhaling emissions generated during printing.  The goal of this study was to determine if inhalation of particulate and toxic chemicals generated during printing with polycarbonate (PC) plastic affected the neuroendocrine system.  Male rats were exposed to 3D-printer emissions (500 \u00b5g/cm3) or filtered air for 1, 4, 8, 15 or 30d for 4d/week (4h/day).  The effects of these exposures on hormone concentrations, and markers of function, injury and/or oxidative stress in the olfactory bulb, hypothalamus and testes were measured after 1, 8 and 30d of exposure.  Thirty days of exposure to 3D-emissions resulted in reductions in  thyroid stimulating hormone, follicle stimulating hormone and prolactin.  These changes were accompanied by increases in markers of cell injury and reductions in active mitochondria in the olfactory bulb, gonadotropin releasing hormone cells and fibers and tyrosine hydroxylase immunolabeled fibers in the arcuate nucleus, and reductions in spermatogonium.  PC plastics contain high concentrations bisphenol A and these results are consistent with the hypothesis that the health effects of inhaling 3D-printer emissions may be due to bisphenol A.",
-            "title": "Inhalation of polycarbonate emissions generated during 3D printing processes affects neuroendocrine function in male rats",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138067,21 +138054,60 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/dtz3-sij3",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/dtz3-sij3",
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
+            "title": "Inhalation of polycarbonate emissions generated during 3D printing processes affects neuroendocrine function in male rats"
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
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis dataset shows health conditions and contributing causes mentioned in conjunction with deaths involving coronavirus disease 2019 (COVID-19) by age group and jurisdiction of occurrence.\n\n2022 and 2023 data are provisional. Estimates for 2020 and 2021 are based on final data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/hk9y-quqm",
             "issued": "2020-05-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2020/2023",
-            "modified": "2023-09-27",
             "keyword": [
                 "adult respiratory distress syndrome",
                 "age",
@@ -138121,63 +138147,60 @@
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
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/hk9y-quqm",
-            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis dataset shows health conditions and contributing causes mentioned in conjunction with deaths involving coronavirus disease 2019 (COVID-19) by age group and jurisdiction of occurrence.\n\n2022 and 2023 data are provisional. Estimates for 2020 and 2021 are based on final data.",
-            "title": "Conditions Contributing to COVID-19 Deaths, by State and Age, Provisional 2020-2023",
-            "programCode": [
-                "009:020"
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2020/2023",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "Conditions Contributing to COVID-19 Deaths, by State and Age, Provisional 2020-2023"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Syndromic Surveillance Program (NSSP)",
+                "hasEmail": "mailto:nssp@cdc.gov"
+            },
+            "description": "2023 Respiratory Virus Response - NSSP Emergency Department Visits - COVID-19, Flu, RSV, Combined\n<br>\nFor additional information, please see:  <a href=\"https://www.cdc.gov/ncird/surveillance/respiratory-illnesses/index.html#companion-guide\"><b>Companion Guide: NSSP Emergency Department Data on Respiratory Illness</b></a>\n<br>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/vutn-jzwm/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.rdf?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/vutn-jzwm/rows.rdf?accessType=DOWNLOAD",
                     "mediaType": "application/rdf+xml"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.json?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/vutn-jzwm/rows.json?accessType=DOWNLOAD",
                     "mediaType": "application/json"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.xml?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/vutn-jzwm/rows.xml?accessType=DOWNLOAD",
                     "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/vutn-jzwm",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/vutn-jzwm",
             "issued": "2024-11-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-12-31/2024-02-17",
-            "modified": "2025-01-24",
-            "references": [
-                "https://www.cdc.gov/ncird/surveillance/respiratory-illnesses/index.html#companion-guide"
-            ],
             "keyword": [
                 "covid19",
                 "ed",
@@ -138191,131 +138214,84 @@
                 "rsv",
                 "rvr"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Syndromic Surveillance Program (NSSP)",
-                "hasEmail": "mailto:nssp@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/vutn-jzwm",
-            "description": "2023 Respiratory Virus Response - NSSP Emergency Department Visits - COVID-19, Flu, RSV, Combined\n<br>\nFor additional information, please see:  <a href=\"https://www.cdc.gov/ncird/surveillance/respiratory-illnesses/index.html#companion-guide\"><b>Companion Guide: NSSP Emergency Department Data on Respiratory Illness</b></a>\n<br>",
-            "title": "2023 Respiratory Virus Response - NSSP Emergency Department Visits - COVID-19, Flu, RSV, Combined",
+            "landingPage": "https://data.cdc.gov/d/vutn-jzwm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-24",
             "programCode": [
                 "009:026"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vutn-jzwm/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vutn-jzwm/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vutn-jzwm/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/vutn-jzwm/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
+            "references": [
+                "https://www.cdc.gov/ncird/surveillance/respiratory-illnesses/index.html#companion-guide"
             ],
             "spatial": "US",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "temporal": "2022-12-31/2024-02-17",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "2023 Respiratory Virus Response - NSSP Emergency Department Visits - COVID-19, Flu, RSV, Combined"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/uygm-ff83",
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
-            "identifier": "f3e3687a-2d5d-5391-8640-8ffe448c8191",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure_value v2.10.64 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
-                    "description": "CoreSet measure_value v2.10.64 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure_value v2.10.64 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure_value v2.10.64 (coreset-prod)"
                 }
             ],
+            "identifier": "f3e3687a-2d5d-5391-8640-8ffe448c8191",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/uygm-ff83",
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
+            "title": "CoreSet measure_value v2.10.64 (coreset-prod)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -138338,38 +138314,47 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/uzsd-re6n",
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
-            "identifier": "fa14a08c-6549-4c1d-a910-6a5c5df7314c",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210809 to 20210815",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138377,18 +138362,44 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "fa14a08c-6549-4c1d-a910-6a5c5df7314c",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/uzsd-re6n",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210809 to 20210815"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/uzvb-34qu",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "description": "This data set includes annual counts and percentages of Medicaid enrollees who are eligible for benefits based on disability, overall; by reason for qualification of disability benefits; and by four subpopulation topics: age group, dual eligibility status, race and ethnicity, and managed care participation. \r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands who were enrolled for at least one day in the calendar year, except where otherwise noted. Enrollees in Guam, American Samoa, and the Northern Mariana Islands are not included. The Children\u2019s Health Insurance Program (CHIP) does not confer eligibility based on disability, so Medicaid expansion CHIP (M-CHIP) and separate CHIP (S-CHIP) enrollees are not included. Results shown for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown for the dual eligibility, race and ethnicity, and managed care participation subpopulation topics are restricted to working-age adults (ages 19 to 64) with comprehensive Medicaid benefits. Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Medicaid enrollees who qualify for benefits based on disability in 2020.\" Enrollees are assigned to a disability category based on their latest reported eligibility group code and age in the calendar year. Enrollees are assigned to an age group subpopulation using age as of December 31st of the calendar year. Enrollees are assigned to a dual eligibility status subpopulation based on the dual eligibility code that applies to the majority of their enrolled-months during the year (Dual Eligibility Code). Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to a managed care participation subpopulation based on the managed care plan type code that applies to the majority of their enrolled-months during the year (Enrollment in CMC Plans). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/disability-2020-2022-01162025.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "identifier": "b12e390f-1721-47c0-bb38-b0b1805e0446",
             "issued": "2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
             "keyword": [
                 "demographics",
                 "disability",
@@ -138396,60 +138407,30 @@
                 "medicaid",
                 "t-msis analytic files"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Medicaid.gov",
-                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/uzvb-34qu",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "b12e390f-1721-47c0-bb38-b0b1805e0446",
-            "description": "This data set includes annual counts and percentages of Medicaid enrollees who are eligible for benefits based on disability, overall; by reason for qualification of disability benefits; and by four subpopulation topics: age group, dual eligibility status, race and ethnicity, and managed care participation. \r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands who were enrolled for at least one day in the calendar year, except where otherwise noted. Enrollees in Guam, American Samoa, and the Northern Mariana Islands are not included. The Children\u2019s Health Insurance Program (CHIP) does not confer eligibility based on disability, so Medicaid expansion CHIP (M-CHIP) and separate CHIP (S-CHIP) enrollees are not included. Results shown for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown for the dual eligibility, race and ethnicity, and managed care participation subpopulation topics are restricted to working-age adults (ages 19 to 64) with comprehensive Medicaid benefits. Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Medicaid enrollees who qualify for benefits based on disability in 2020.\" Enrollees are assigned to a disability category based on their latest reported eligibility group code and age in the calendar year. Enrollees are assigned to an age group subpopulation using age as of December 31st of the calendar year. Enrollees are assigned to a dual eligibility status subpopulation based on the dual eligibility code that applies to the majority of their enrolled-months during the year (Dual Eligibility Code). Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to a managed care participation subpopulation based on the managed care plan type code that applies to the majority of their enrolled-months during the year (Enrollment in CMC Plans). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
-            "title": "Medicaid enrollees who qualify for benefits based on disability",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://download.medicaid.gov/data/disability-2020-2022-01162025.csv",
-                    "mediaType": "text/csv"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "title": "Medicaid enrollees who qualify for benefits based on disability"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2024-11-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "genomics",
-                "protein",
-                "sars-cov-2",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/dbuy-v859",
             "description": "NCBI Virus is an integrative, value-added resource designed to support retrieval, display and analysis of a curated collection of virus sequences and large sequence datasets. Its goal is to increase the usability of viral sequence data archived in GenBank and other NCBI repositories.\n\nThis resource includes resources previously included in HIV-1, Human Protein Interaction Database, Influenza Virus Resource, and Virus Variation.",
-            "title": "NCBI Virus",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138458,38 +138439,41 @@
                     "title": "NCBI Virus Homepage and Search"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/dbuy-v859",
+            "issued": "2024-11-05",
+            "keyword": [
+                "genomics",
+                "protein",
+                "sars-cov-2",
+                "virus"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/",
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
+            "title": "NCBI Virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/698n-pqtv",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-09-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
-            "keyword": [
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/698n-pqtv",
             "description": "Partners in Information Access for the Public Health Workforce (PHPartners) is a web portal and current awareness service of information for the public health workforce. Alerts the communities to meetings, webinars, new web-born reports (analyses, statistics), datasets, and general news. Currently contains over 4,000 items.\n\nThis resource was retired on September 14, 2021 and is no longer updated.",
-            "title": "Partners in Information Access for the Public Health Workforce (PHPartners) (retired September 14, 2021)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138512,57 +138496,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/698n-pqtv",
+            "issued": "2021-09-14",
+            "keyword": [
+                "public health"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/698n-pqtv",
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
                 "Other"
-            ]
+            ],
+            "title": "Partners in Information Access for the Public Health Workforce (PHPartners) (retired September 14, 2021)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -138585,58 +138553,58 @@
                     "mediaType": "application/xml"
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
+            "title": "DQS NHIS Children Summary Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "public",
-            "issued": "2018-02-07",
-            "@type": "dcat:Dataset",
-            "temporal": "2003/2018",
-            "modified": "2022-04-08",
-            "references": [
-                "http://www.cdc.gov/nchs/nvss/dvs_data_release.htm",
-                "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
-                "https://www.cdc.gov/nchs/nvss/bridged_race.htm",
-                "http://onlinelibrary.wiley.com/doi/10.1111/rssa.12266/abstract",
-                "http://www.sciencedirect.com/science/article/pii/S1877584516300442",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
-                "http://www.cdc.gov/nchs/data/nvss/bridged_race/County_Geography_Changes.pdf"
-            ],
-            "keyword": [
-                "county teen birth trends",
-                "county trends on teen births",
-                "nchs",
-                "teen births",
-                "united states",
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
-            "identifier": "https://data.cdc.gov/api/views/3h58-x6cd",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This data set contains estimated teen birth rates for age group 15\u201319 (expressed per 1,000 females aged 15\u201319) by county and year.\n\nDEFINITIONS\n\nEstimated teen birth rate: Model-based estimates of teen birth rates for age group 15\u201319 (expressed per 1,000 females aged 15\u201319) for a specific county and year. Estimated county teen birth rates were obtained using the methods described elsewhere (1,2,3,4). These annual county-level teen birth estimates \u201cborrow strength\u201d across counties and years to generate accurate estimates where data are sparse due to small population size (1,2,3,4). The inferential method uses information\u2014including the estimated teen birth rates from neighboring counties across years and the associated explanatory variables\u2014to provide a stable estimate of the county teen birth rate.\nMedian teen birth rate: The middle value of the estimated teen birth rates for the age group 15\u201319 for counties in a state.\nBayesian credible intervals: A range of values within which there is a 95% probability that the actual teen birth rate will fall, based on the observed teen births data and the model.\n\nNOTES\n\nData on the number of live births for women aged 15\u201319 years were extracted from the National Center for Health Statistics\u2019 (NCHS) National Vital Statistics System birth data files for 2003\u20132015 (5).\n\nPopulation estimates were extracted from the files containing intercensal and postcensal bridged-race population estimates provided by NCHS. For each year, the July population estimates were used, with the exception of the year of the decennial census, 2010, for which the April estimates were used.\n\nHierarchical Bayesian space\u2013time models were used to generate hierarchical Bayesian estimates of county teen birth rates for each year during 2003\u20132015 (1,2,3,4).\n\nThe Bayesian analogue of the frequentist confidence interval is defined as the Bayesian credible interval. A 100*(1-\u03b1)% Bayesian credible interval for an unknown parameter vector \u03b8 and observed data vector y is a subset C of parameter space \u0424 such that\n1-\u03b1\u2264P({C\u2502y})=\u222bp{\u03b8 \u2502y}d\u03b8,\nwhere integration is performed over the set  and is replaced by summation for discrete components of \u03b8.  The probability that \u03b8 lies in C given the observed data y is at least (1- \u03b1) (6).\n\nCounty borders in Alaska changed, and new counties were formed and others were merged, during 2003\u20132015. These changes were reflected in the population files but not in the natality files. For this reason, two counties in Alaska were collapsed so that the birth and population counts were comparable. Additionally, Kalawao County, a remote island county in Hawaii, recorded no births, and census estimates indicated a denominator of 0 (i.e., no females between the ages of 15 and 19 years residing in the county from 2003 through 2015). For this reason, Kalawao County was removed from the analysis. Also , Bedford City, Virginia, was added to Bedford County in 2015 and no longer appears in the mortality file in 2015. For consistency, Bedford City was merged with Bedford County, Virginia, for the entire 2003\u20132015 period. Final analysis was conducted on 3,137 counties for each year from 2003 through 2015. County boundaries are consistent with the vintage 2005\u20132007 bridged-race population file geographies (7).",
-            "title": "NCHS - Teen Birth Rates for Age Group 15-19 in the United States by County",
-            "isPartOf": "NCHS - Teen Birth Rates for Age Group 15-19 in the United States by County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138659,45 +138627,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/3h58-x6cd",
+            "isPartOf": "NCHS - Teen Birth Rates for Age Group 15-19 in the United States by County",
+            "issued": "2018-02-07",
+            "keyword": [
+                "county teen birth trends",
+                "county trends on teen births",
+                "nchs",
+                "teen births",
+                "united states",
+                "u.s. teen birth rate"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-08",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "http://www.cdc.gov/nchs/nvss/dvs_data_release.htm",
+                "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+                "https://www.cdc.gov/nchs/nvss/bridged_race.htm",
+                "http://onlinelibrary.wiley.com/doi/10.1111/rssa.12266/abstract",
+                "http://www.sciencedirect.com/science/article/pii/S1877584516300442",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "http://www.cdc.gov/nchs/data/nvss/bridged_race/County_Geography_Changes.pdf"
+            ],
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "2003/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Teen Birth Rates for Age Group 15-19 in the United States by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-coverage-race.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-29",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2024-04-12",
-            "keyword": [
-                "flu vaccination",
-                "nis-ccm"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:vaxview@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/nsxk-tvbw",
             "description": "\u2022 Influenza vaccination coverage and parental intent among children 6 months to 17 years is assessed through the National Immunization Survey-Child COVID Module providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n\u2022 For the 2023-2024 flu season, the CDC recommends a flu shot for most people 6 months and older.",
-            "title": "Weekly Influenza Vaccination Status and Intent for Vaccination, Overall, by Selected Demographics, and Jurisdiction, Children 6 Months - 17 Years, 2023-24, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138720,51 +138703,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/nsxk-tvbw",
+            "issued": "2023-11-29",
+            "keyword": [
+                "flu vaccination",
+                "nis-ccm"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-coverage-race.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-04-12",
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
                 "Child Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Influenza Vaccination Status and Intent for Vaccination, Overall, by Selected Demographics, and Jurisdiction, Children 6 Months - 17 Years, 2023-24, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://vsac.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
-                "clinical quality measures",
-                "cqm",
-                "dataset",
-                "health data standards",
-                "icd",
-                "rxnorm",
-                "snomed",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qbke-6ijm",
             "description": "The VSAC is a repository and authoring tool for public value sets created by external programs. Value sets are lists of codes and corresponding terms, from NLM-hosted standard clinical vocabularies (such as SNOMED CT\u00ae, RxNorm, LOINC\u00ae and others), that define clinical concepts to support effective and interoperable health information exchange. The VSAC does not create value set content. The VSAC also provides downloadable access to all official versions of value sets specified by the Centers for Medicare & Medicaid Services (CMS) electronic Clinical Quality Measures (eCQMs). For information on CMS eCQMs, visit the eCQI Resource Center. The VSAC is provided by the National Library of Medicine (NLM), in collaboration with the Office of the National Coordinator for Health Information Technology (ONC) and CMS.",
-            "title": "Value Set Authority Center",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138785,39 +138761,47 @@
                     "title": "Download VSAC Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qbke-6ijm",
+            "issued": "2016-08-04",
+            "keyword": [
+                "api",
+                "clinical quality measures",
+                "cqm",
+                "dataset",
+                "health data standards",
+                "icd",
+                "rxnorm",
+                "snomed",
+                "terminologies"
+            ],
+            "landingPage": "https://vsac.nlm.nih.gov/",
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
+            "title": "Value Set Authority Center"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/rsv/php/surveillance/rsv-net.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-23",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "rsv",
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
-            "identifier": "https://data.cdc.gov/api/views/pbq2-7wr2",
             "description": "The Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET) is a network that conducts active, population-based surveillance for laboratory-confirmed RSV-associated hospitalizations in children younger than 18 years of age and adults. RSV-NET, along with the Coronavirus Disease 2019 (COVID-19) Hospitalization Surveillance Network (COVID-NET) an the Influenza Hospitalization Surveillance network (FluSuv-NET), comprise the Respiratory Virus Hospitalization Surveillance Network (RESP-NET). The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. Because the surveillance areas and age groups included in surveillance have changed over time, trends should be interpreted with caution. RSV-NET is CDC\u2019s source for important data on rates of hospitalizations associated with RSV. Hospitalization rates show how many people in the surveillance area are hospitalized with RSV, compared to the total number of people residing in that area.\n\nData are preliminary and subject to change as more data become available. Data will be updated weekly.",
-            "title": "Monthly Rates of Laboratory-Confirmed RSV Hospitalizations from the RSV-NET Surveillance System",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138840,44 +138824,41 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "RSV-NET Sites",
+            "identifier": "https://data.cdc.gov/api/views/pbq2-7wr2",
+            "issued": "2024-07-23",
+            "keyword": [
+                "rsv",
+                "surveillance"
+            ],
+            "landingPage": "https://www.cdc.gov/rsv/php/surveillance/rsv-net.html",
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
+            "spatial": "RSV-NET Sites",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Monthly Rates of Laboratory-Confirmed RSV Hospitalizations from the RSV-NET Surveillance System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/v4vn-2zy9",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "individual",
-                "individual market medical",
-                "py2025",
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
-            "identifier": "735facd9-1df8-400e-b650-da881c728a2b",
             "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape PY2025 Individual Medical",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -138885,45 +138866,38 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "735facd9-1df8-400e-b650-da881c728a2b",
+            "issued": "2024-12-10",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2025",
+                "qhp",
+                "qhp landscape"
+            ],
+            "landingPage": "https://healthdata.gov/d/v4vn-2zy9",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape PY2025 Individual Medical"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -138946,86 +138920,95 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/v69g-79w7",
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
-            "identifier": "1de5f854-a0ce-50ca-ae19-06312d2e8950",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSEt measure_value v2.10.23 (coreset-prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.23/20241029/measure_value.csv",
-                    "description": "CoreSEt measure_value v2.10.23 (coreset-prod)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSEt measure_value v2.10.23 (coreset-prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.23/20241029/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSEt measure_value v2.10.23 (coreset-prod)"
                 }
             ],
+            "identifier": "1de5f854-a0ce-50ca-ae19-06312d2e8950",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/v69g-79w7",
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
+            "title": "CoreSEt measure_value v2.10.23 (coreset-prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/v6z3-irev",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2019-07-22",
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
-            "identifier": "daba7980-e219-5996-9bec-90358fd156f1",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2019",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139033,46 +139016,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "daba7980-e219-5996-9bec-90358fd156f1",
+            "issued": "2019-07-22",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/v6z3-irev",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-10-21",
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
+            "title": "State Drug Utilization Data 2019"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -139095,43 +139072,46 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024, 2024-25",
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
-            "identifier": "https://data.cdc.gov/api/views/ewpg-rz7g",
             "description": "- Weekly Cumulative Estimated Number of COVID-19 Vaccinations Administered in Pharmacies and Physical Medical Offices, Adults 18 Years and Older, United States \n\n- Estimated number of COVID-19 vaccinations among adults 18 years and older is assessed through IQVIA (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, stores, and independent pharmacies) and physician medical offices.",
-            "title": "Weekly Cumulative Estimated Number of COVID-19 Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, by Season and Age Group, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139154,54 +139134,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/ewpg-rz7g",
+            "issued": "2025-01-28",
+            "keyword": [
+                "covid-19 vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "vsd"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/data-reporting",
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
+            "temporal": "2023-2024, 2024-25",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Estimated Number of COVID-19 Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, by Season and Age Group, United States"
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
                 "fn": "500 Cities Public Inquiries",
                 "hasEmail": "mailto:places@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fbbf-hgkc",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
             "description": "This dataset contains model-based ZIP Code tabulation Areas (ZCTA) level estimates for the PLACES project 2020 release. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 27 measures: 5 chronic disease-related unhealthy behaviors, 13 health outcomes, and 9 on use of preventive services. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2010 population data, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, ZCTA Data 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139224,90 +139198,98 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
+            "identifier": "https://data.cdc.gov/api/views/fbbf-hgkc",
+            "issued": "2021-09-29",
+            "keyword": [
+                "behaviors",
+                "brfss",
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
+            "title": "PLACES: Local Data for Better Health, ZCTA Data 2020 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/v9s5-mfrb",
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
-            "identifier": "bd43096f-1e66-5037-9100-4eb2aa907367",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_states",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states.csv",
-                    "description": "{\"dataset\": \"states\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states.csv",
+                    "mediaType": "text/csv",
                     "title": "states csv file"
                 }
             ],
+            "identifier": "bd43096f-1e66-5037-9100-4eb2aa907367",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/v9s5-mfrb",
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
+            "title": "prodAuto_states"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/va8w-6mua",
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
-                "py2024",
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
-            "identifier": "2638f347-5311-4655-8d2b-1466848adeae",
             "description": "The Rate PUF (Rate-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Rate-PUF contains plan-level data on rates based on an eligible subscriber\u2019s age, tobacco use, and geographic location; and family-tier rates.",
-            "title": "Rate PUF - PY2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139315,63 +139297,94 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "2638f347-5311-4655-8d2b-1466848adeae",
+            "issued": "2024-08-06",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2024",
+                "rate"
+            ],
+            "landingPage": "https://healthdata.gov/d/va8w-6mua",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Rate PUF - PY2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vaib-d9kh",
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
-            "identifier": "7dd7d8bd-d353-5836-b7bd-33d034afbd50",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard VERSION vCORESET.1.1-test (coreset-local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/VERSION.csv",
-                    "description": "Scorecard VERSION vCORESET.1.1-test (coreset-local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard VERSION vCORESET.1.1-test (coreset-local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/VERSION.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard VERSION vCORESET.1.1-test (coreset-local)"
                 }
             ],
+            "identifier": "7dd7d8bd-d353-5836-b7bd-33d034afbd50",
+            "issued": "2024-05-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/vaib-d9kh",
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
+            "title": "Scorecard VERSION vCORESET.1.1-test (coreset-local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee-list",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee-list",
+            "description": "The Health Information Technology for Economic and Clinical Health (HITECH) Act was passed as part of the American Recovery and Reinvestment Act (ARRA) to invest in the U.S. health IT infrastructure. The Office of the National Coordinator for Health IT (ONC) received over $2 billion of these HITECH funds, which was granted to health and community organizations across the U.S. This data set provides the full list of ONC's HITECH Act grantees. The data encompasses the five ONC HITECH Act programs: the Beacon Communities Program, the Health IT Regional Extension Centers Program, the Health IT Workforce Programs, the State Health Information Exchange Program, and the Strategic Health IT Advanced Research Projects (SHARP) Program. This data set includes geographic, federal funding, and grantee organization data. The data can be linked to other open data sets on the Health IT Dashboard and other sources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/ONC_HITECH_Grantee_List.csv",
+                    "mediaType": "text/csv",
+                    "title": "ONC_HITECH_Grantee_List.csv"
+                }
+            ],
+            "identifier": "9yl9iufr-tyrn-xj4n-iqou-cf3r98e02fw8",
             "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2015-06-01",
             "keyword": [
                 "arra",
                 "ehr",
@@ -139383,58 +139396,30 @@
                 "regional extension centers",
                 "state health information exchange cooperative agreement"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee-list",
+            "modified": "2015-06-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "9yl9iufr-tyrn-xj4n-iqou-cf3r98e02fw8",
-            "description": "The Health Information Technology for Economic and Clinical Health (HITECH) Act was passed as part of the American Recovery and Reinvestment Act (ARRA) to invest in the U.S. health IT infrastructure. The Office of the National Coordinator for Health IT (ONC) received over $2 billion of these HITECH funds, which was granted to health and community organizations across the U.S. This data set provides the full list of ONC's HITECH Act grantees. The data encompasses the five ONC HITECH Act programs: the Beacon Communities Program, the Health IT Regional Extension Centers Program, the Health IT Workforce Programs, the State Health Information Exchange Program, and the Strategic Health IT Advanced Research Projects (SHARP) Program. This data set includes geographic, federal funding, and grantee organization data. The data can be linked to other open data sets on the Health IT Dashboard and other sources.",
-            "title": "ONC Health Information Technology for Economic and Clinical Health (HITECH) Grantee List",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/ONC_HITECH_Grantee_List.csv",
-                    "mediaType": "text/csv",
-                    "title": "ONC_HITECH_Grantee_List.csv"
-                }
-            ],
-            "describedBy": "https://www.healthit.gov/data/datasets/onc-health-information-technology-economic-and-clinical-health-hitech-grantee-list"
+            "title": "ONC Health Information Technology for Economic and Clinical Health (HITECH) Grantee List"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vbu7-4nqs",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-11-03",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-02",
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
-            "identifier": "71e4f2a9-689d-4328-b90a-7f464dc9859c",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211025 to 20211031",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139442,37 +139427,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "71e4f2a9-689d-4328-b90a-7f464dc9859c",
+            "issued": "2021-11-03",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/vbu7-4nqs",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2021-11-02",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211025 to 20211031"
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
-                "mesh",
-                "mesh 2023 update"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vwzh-6q7y",
             "description": "Publication Types (Publication Characteristics) are Descriptors that indicate what an indexed item is, (i.e., its genre, rather than what it is about - for example, Historical Article). They may include Publication Components, such as Charts; Publication Formats, such as Editorial; and Study Characteristics, such as Clinical Trial.\n\nThey function as metadata, rather than being about the content. These records are searchable in PubMed as Publication Type [PT], and the terms in MEDLINE records are labeled as \"PT\" or <PublicationType> rather than \"MH\" or <MeSHHeading>. They are listed in category V of the MeSH Tree Structures.",
-            "title": "MeSH 2023 Publication Types",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139495,47 +139478,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vwzh-6q7y",
+            "issued": "2022-12-19",
+            "keyword": [
+                "mesh",
+                "mesh 2023 update"
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
+            "title": "MeSH 2023 Publication Types"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/scxv-4u4u",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "animal",
-                "congenital syndrome",
-                "mmwr",
-                "nedss",
-                "netss",
-                "nndss",
-                "rabies",
-                "rubella",
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
-            "identifier": "https://data.cdc.gov/api/views/scxv-4u4u",
             "description": "NNDSS - Table II. Rabies, animal to Rubella, congenital syndrome - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Rabies, animal to Rubella, congenital syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139558,53 +139533,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/scxv-4u4u",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "animal",
+                "congenital syndrome",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "rabies",
+                "rubella",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/scxv-4u4u",
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
+            "title": "NNDSS - Table II. Rabies, animal to Rubella, congenital syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-supplier-and-service",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/1746a83e-bb65-4300-8e02-21edbab77c6b/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-supplier-and-service-data-dictionary",
             "description": "The Medicare Durable Medical Equipment, Devices & Supplies by Supplier and Service dataset contains information on usage, payments and submitted charges organized by supplier National Provider Identifier (NPI), Healthcare Common Procedure Coding System (HCPCS) code, and supplier rental indicator.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Supplier and Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1746a83e-bb65-4300-8e02-21edbab77c6b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1746a83e-bb65-4300-8e02-21edbab77c6b/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Supplier and Service : 2022-05-28"
                 },
                 {
@@ -139716,51 +139694,50 @@
                     "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Supplier and Service : 2014-12-30"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-supplier-and-service-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/1746a83e-bb65-4300-8e02-21edbab77c6b/data-viewer",
+            "issued": "2024-06-05",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medical suppliers & equipment",
+                "medicare",
+                "original medicare",
+                "physicians & practitioners"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-supplier-and-service",
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
+            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Supplier and Service"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -139783,47 +139760,46 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup"
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DDT Public Inquiries",
                 "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/pttf-ck53",
+            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Behavioral-Risk-Factors-Vision-Eye-Health/pttf-ck53",
             "description": "2005-2016. This dataset includes data from the retired BRFSS Vision Module. From 2005-2011 the BRFSS employed a ten question vision module regarding vision impairment, access and utilization of eye care, and self-reported eye diseases. In 2013 and subsequently, one question in the core of BRFSS asks about vision: \u201cAre you blind or do you have serious difficulty seeing, even when wearing glasses?\u201d The latest data for this core question can be found in the Vision and Eye Health Surveillance System (VEHSS). VEHSS is intended to provide population estimates of vision loss function, eye diseases, health disparities, as well as barriers and facilitators to access to vision and eye care. This information can be used for designing, implementing, and evaluating vision and eye health prevention programs. To access the latest BRFSS data, (2013-2017) view the Behavioral Risk Factors \u2013 Vision and Eye Health Surveillance dataset (https://chronicdata.cdc.gov/Vision-Eye-Health/Behavioral-Risk-Factors-Vision-and-Eye-Health-Surv/vkwg-yswv).",
-            "title": "BRFSS Vision Module Data \u2013 Vision & Eye Health",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139846,44 +139822,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Behavioral-Risk-Factors-Vision-Eye-Health/pttf-ck53",
+            "identifier": "https://data.cdc.gov/api/views/pttf-ck53",
+            "issued": "2023-09-21",
+            "keyword": [
+                "diabetes",
+                "eye diseases",
+                "heart diseases",
+                "hypertension",
+                "physical activity",
+                "smoking",
+                "state",
+                "stroke",
+                "vhi",
+                "vision impairment"
+            ],
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-09-21",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "BRFSS Vision Module Data \u2013 Vision & Eye Health"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/statesystem/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2017-08-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "keyword": [
-                "centers for disease control and prevention",
-                "department of health and human services",
-                "healthy people 2020",
-                "leading health indicator",
-                "office on smoking and health",
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
-            "identifier": "https://data.cdc.gov/api/views/hhew-mxbt",
+            "describedBy": "https://chronicdata.cdc.gov/Healthy-People-2020/Healthy-People-2020-Tobacco-Use-Objectives/hhew-mxbt",
             "description": "U.S. Department of Health and Human Services (HHS). Centers for Disease Control and Prevention (CDC). Healthy People 2020 Tobacco Use Objectives. Healthy People 2020. Healthy People 2020 provides a framework for action to reduce tobacco use to the point that it is no longer a public health problem for the Nation. This dataset includes information related to the Healthy People 2020 Tobacco Use objectives, operational definitions, baselines, and targets. Baseline years may vary by objective. Targets represented correspond to the year 2020.",
-            "title": "Healthy People 2020 Tobacco Use Objectives",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139906,44 +139886,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Healthy-People-2020/Healthy-People-2020-Tobacco-Use-Objectives/hhew-mxbt",
+            "identifier": "https://data.cdc.gov/api/views/hhew-mxbt",
+            "issued": "2017-08-23",
+            "keyword": [
+                "centers for disease control and prevention",
+                "department of health and human services",
+                "healthy people 2020",
+                "leading health indicator",
+                "office on smoking and health",
+                "osh"
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
             "theme": [
                 "Healthy People 2020"
-            ]
+            ],
+            "title": "Healthy People 2020 Tobacco Use Objectives"
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
-            "modified": "2024-09-17",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/visualization/"
-            ],
-            "keyword": [
-                "diet",
-                "dqs",
-                "nhanes"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:dqs@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/59vz-u8kg",
+            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "description": "These data represent prevalence estimates of select oral health topics from the National Health and Nutrition Examination Survey (NHANES).\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS NHANES Select Oral Health Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -139966,38 +139947,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "identifier": "https://data.cdc.gov/api/views/59vz-u8kg",
+            "issued": "2024-02-06",
+            "keyword": [
+                "diet",
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
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS NHANES Select Oral Health Prevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/r9ns-zmra",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division Exposure Assessment Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/r9ns-zmra",
             "description": "The occupational exposure risk to peracetic acid (PAA), a common disinfectant and sterilant use in industrial settings like healthcare facilities and meat processing plants, is typically assessed through collection and analysis of atmospheric workplace samples. In this study, a new personal sampling technique was developed for determining the atmospheric concentration of PAA in the workplace. Samples of humidified air containing peracetic acid (concentration range: 25-2000 ppb) were collected on 350-mg XAD-7 solid sorbent tubes to adsorb the analyte. Peracetic acid was desorbed using anhydrous acetonitrile, after which it was treated with excess cyclohexene to generate the corresponding epoxide via the Prilezhaev reaction. The epoxide product was analyzed and quantified using gas chromatography-mass spectrometry, indirectly determining the amount of peracetic acid in the original air sample. The specificity for peracetic acid over other contaminants was assessed through a series of hydrogen peroxide (HP) and acetic acid (AA) spiking experiments, in which selectivity for PAA was demonstrated at several different concentrations of both HP and AA. The limit-of-detection (LOD) and the limit-of-quantitation (LOQ) for this method was determined to be 60 ppb and 198 ppb, respectively. Unlike many other methods, the sorbent tube negates the need for solvent in the sampling apparatus, adding to its ease of use. These features as well as inexpensive materials and the use of small, wearable vacuum pumps could allow for implementation of easier personal sampling in the workplace.",
-            "title": "Feasibility of a Selective Epoxidation Technique for Use in Quantification of Peracetic Acid in Air Samples Collected on Sorbent Tubes-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140005,38 +139992,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/r9ns-zmra",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/r9ns-zmra",
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
+            "title": "Feasibility of a Selective Epoxidation Technique for Use in Quantification of Peracetic Acid in Air Samples Collected on Sorbent Tubes-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vexp-ryu3",
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
-            "identifier": "6264a6d4-5082-4b67-9e8b-014646430e22",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-12-to-2023-06-18",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140045,100 +140030,84 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-12-to-2023-06-18"
                 }
             ],
+            "identifier": "6264a6d4-5082-4b67-9e8b-014646430e22",
+            "issued": "2023-06-27",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/vexp-ryu3",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-06-12-to-2023-06-18"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vfdk-z8av",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-06",
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
-            "identifier": "a3adef5c-97e9-52e0-8c4b-b2dcb8e8eca9",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_files_stateSnapshot",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_stateSnapshot.csv",
-                    "description": "{\"dataset\": \"files_stateSnapshot\", \"stage\": \"prodAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"files_stateSnapshot\", \"stage\": \"prodAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_stateSnapshot.csv",
+                    "mediaType": "text/csv",
                     "title": "files_stateSnapshot csv file"
                 }
             ],
+            "identifier": "a3adef5c-97e9-52e0-8c4b-b2dcb8e8eca9",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/vfdk-z8av",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2022-10-06",
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
+            "title": "prodAuto_files_stateSnapshot"
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
-            "modified": "2025-01-24",
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
-                "respiratory-virus-response",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -140161,42 +140130,56 @@
                     "mediaType": "application/xml"
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
+                "respiratory-virus-response",
+                "rsv",
+                "rvr",
+                "virus"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7xva-uux8",
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
-            "landingPage": "https://healthdata.gov/d/vfze-g45j",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2021-09-28",
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
-            "identifier": "fbbe1734-b448-4e5a-bc94-3f8688534741",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2020 reporting.\r\n\r\nSource: Mathematica analysis of MACPro and Form CMS-416 reports for the FFY 2020 reporting cycle. Dataset revised September 2021. For more information, see the Children's Health Care Quality Measures and Adult Health Care Quality Measures webpages.",
-            "title": "2020 Child and Adult Health Care Quality Measures Quality",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140205,39 +140188,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "fbbe1734-b448-4e5a-bc94-3f8688534741",
+            "issued": "2021-10-08",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/vfze-g45j",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2021-09-28",
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
+            "title": "2020 Child and Adult Health Care Quality Measures Quality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vg5g-85ys",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-04",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-02",
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
-            "identifier": "a8366086-07bb-4e1e-b019-744984e6764d",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-25-to-2023-10-01",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140246,33 +140231,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-25-to-2023-10-01"
                 }
             ],
+            "identifier": "a8366086-07bb-4e1e-b019-744984e6764d",
+            "issued": "2023-10-04",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/vg5g-85ys",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-10-02",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-09-25-to-2023-10-01"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kgid-f54m",
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
-            "identifier": "https://data.cdc.gov/api/views/kgid-f54m",
             "description": "The objective of this study was to evaluate the effect of a back-support exoskeleton (Laevo V2.5) on the trunk and hip angles, low back muscle activity, and heart rate during in-bed patient handling tasks. Eight participants (5 males and 3 females) performed four different in-bed patient handling tasks, including sitting to lying, repositioning toward the caregiver, turning toward the caregiver, and turning away from the caregiver.",
-            "title": "Evaluation of A Passive Back-Support Exoskeleton during In-Bed Patient Handling Tasks",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140280,39 +140267,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kgid-f54m",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/kgid-f54m",
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
+            "title": "Evaluation of A Passive Back-Support Exoskeleton during In-Bed Patient Handling Tasks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ebbj-sh54",
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
-            "identifier": "https://data.cdc.gov/api/views/ebbj-sh54",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012. 2012 Source: Fatality Analysis Reporting System (FARS)Note: Blank cells indicate data are suppressed. 2014 Source: Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, All States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140335,22 +140318,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ebbj-sh54",
+            "issued": "2016-09-26",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ebbj-sh54",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, All States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/vr4m-kmk6",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. Some rounds also include non-probability panels.  The eighth round of RANDS (RANDS 8) was administered by NORC at the University of Chicago using the AmeriSpeak Panel. Samples also were purchased by NORC from the Lucid and Community Marketing Insights (CMI) non-probability panels. Data were collected from June 8, 2023 to July 24, 2023. RANDS 8 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on disability, gender identity, aspects of life, emotional well-being, and the reason behind perceived acts of discrimination. The AmeriSpeak part of RANDS 8 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/vr4m-kmk6",
             "issued": "2024-06-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2023",
-            "modified": "2024-06-26",
             "keyword": [
                 "anxiety",
                 "covid-19",
@@ -140372,62 +140381,36 @@
                 "social isolation and loneliness",
                 "vaccination"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/vr4m-kmk6",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-06-26",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/vr4m-kmk6",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. Some rounds also include non-probability panels.  The eighth round of RANDS (RANDS 8) was administered by NORC at the University of Chicago using the AmeriSpeak Panel. Samples also were purchased by NORC from the Lucid and Community Marketing Insights (CMI) non-probability panels. Data were collected from June 8, 2023 to July 24, 2023. RANDS 8 contained the embedded probe questions and experiments as in previous rounds of RANDS. It included questions on disability, gender identity, aspects of life, emotional well-being, and the reason behind perceived acts of discrimination. The AmeriSpeak part of RANDS 8 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 8 Restricted File",
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
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "50 states and District of Columbia",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2023",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 8 Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/spsk-9jj6",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-08-08",
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
-            "identifier": "https://data.cdc.gov/api/views/spsk-9jj6",
             "description": "This dataset provides data at the county level for the contiguous United States. It includes weekly United States Drought Monitor (USDM) data from 2000-2016 provided by the Cooperative Institute for Climate and Satellites - North Carolina. Please refer to the metadata attachment for more information.\r\n\r\nThese data are used by the CDC's National Environmental Public Health Tracking Network to generate drought measures. Learn more about drought on the Tracking Network's website: https://ephtracking.cdc.gov/showDroughtLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
-            "title": "United States Drought Monitor, 2000-2016",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140450,38 +140433,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/spsk-9jj6",
+            "issued": "2018-08-08",
+            "keyword": [
+                "drought",
+                "environmental health"
+            ],
+            "landingPage": "https://data.cdc.gov/d/spsk-9jj6",
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
+            "title": "United States Drought Monitor, 2000-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vgvk-c9nt",
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
-            "identifier": "43507fce-50ab-4ff4-8050-7d0b9665c2be",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-16-to-2023-01-22",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140490,36 +140475,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-16-to-2023-01-22"
                 }
             ],
+            "identifier": "43507fce-50ab-4ff4-8050-7d0b9665c2be",
+            "issued": "2023-02-09",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/vgvk-c9nt",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-16-to-2023-01-22"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vgwy-3264",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-05-16",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-15",
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
-            "identifier": "a6001b78-982f-4238-ba22-a022db235c1e",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-08-to-2023-05-14",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140528,44 +140513,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-08-to-2023-05-14"
                 }
             ],
+            "identifier": "a6001b78-982f-4238-ba22-a022db235c1e",
+            "issued": "2023-05-16",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/vgwy-3264",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-05-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-08-to-2023-05-14"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/eez9-q5m5",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/eez9-q5m5",
             "description": "NNDSS - Table 1B. Arboviral diseases, neuroinvasive and non-neuroinvasive, Jamestown Canyon virus disease to Powassan virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon to Powassan",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140588,40 +140564,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/eez9-q5m5",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/eez9-q5m5",
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
+            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon to Powassan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vhte-a3ix",
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
-            "identifier": "4d88c014-8989-5a88-bd21-17c1beed0dd3",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2004",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140629,45 +140612,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "4d88c014-8989-5a88-bd21-17c1beed0dd3",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/vhte-a3ix",
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
+            "title": "State Drug Utilization Data 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/adult-coverage.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-10",
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
-            "identifier": "https://data.cdc.gov/api/views/sw5n-wg2p",
             "description": "\u2022 Weekly Influenza Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \n\n \u2022 Weekly estimates of influenza vaccination coverage and intent for vaccination among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html).",
-            "title": "Weekly Influenza Vaccination Coverage and Intent for Vaccination, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140690,72 +140669,105 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
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
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Influenza Vaccination Coverage and Intent for Vaccination, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vjdu-bnzk",
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
-            "identifier": "7df7c585-cbc3-5e87-aadc-b690718fbe41",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet filters v2.10.64 (coreset-impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
-                    "description": "CoreSet filters v2.10.64 (coreset-impl)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet filters v2.10.64 (coreset-impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet filters v2.10.64 (coreset-impl)"
                 }
             ],
+            "identifier": "7df7c585-cbc3-5e87-aadc-b690718fbe41",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/vjdu-bnzk",
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
+            "title": "CoreSet filters v2.10.64 (coreset-impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.hrsa.gov/tools/shortage-area/by-address",
             "bureauCode": [
                 "009:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HRSA Data Warehouse",
+                "hasEmail": "mailto:data@hrsa.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Find Shortage Areas: Health Professional Shortage Area (HPSA) and Medically Underserved Area/Population (MUA/P) by Address tool helps you determine if a specific address is located in a designated shortage area.  Shortage areas are designated by HRSA as specific geographic areas or sites that have the greatest need for health care.  Shortage areas are categorized by specific needs (Primary Care HPSA, Mental Health HPSA, Dental Care HPSA, or MUA/P).</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://datawarehouse.hrsa.gov/GeoAdvisor/ShortageDesignationAdvisor.aspx",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "479be80d-2fac-415b-90c5-77a15ae1cab7",
             "issued": "2012-05-30",
-            "temporal": "2009-01-01T00:00:00-05:00/2009-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "census tract number",
                 "comprehensive health center",
@@ -140779,66 +140791,35 @@
                 "primary care hpsa",
                 "shortage"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HRSA Data Warehouse",
-                "hasEmail": "mailto:data@hrsa.gov"
-            },
+            "landingPage": "https://data.hrsa.gov/tools/shortage-area/by-address",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Health Resources and Services Administration"
             },
-            "identifier": "479be80d-2fac-415b-90c5-77a15ae1cab7",
-            "description": "<p>The Find Shortage Areas: Health Professional Shortage Area (HPSA) and Medically Underserved Area/Population (MUA/P) by Address tool helps you determine if a specific address is located in a designated shortage area.  Shortage areas are designated by HRSA as specific geographic areas or sites that have the greatest need for health care.  Shortage areas are categorized by specific needs (Primary Care HPSA, Mental Health HPSA, Dental Care HPSA, or MUA/P).</p>",
-            "title": "Find Shortage Areas: HPSA & MUA/P by Address",
-            "programCode": [
-                "009:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://datawarehouse.hrsa.gov/GeoAdvisor/ShortageDesignationAdvisor.aspx",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2009-01-01T00:00:00-05:00/2009-01-01T00:00:00-05:00",
             "theme": [
                 "Health",
                 "Medicare"
-            ]
+            ],
+            "title": "Find Shortage Areas: HPSA & MUA/P by Address"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/7vzs-mg28",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/7vzs-mg28",
             "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Replace Report lists Descriptors and Supplementary Concept Records (SCRs) where an existing MeSH term has been replaced by another term.  Note that replacement terms are not necessarily new to the vocabulary; terms are sometimes consolidated under or moved to other existing terms.  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
-            "title": "MeSH 2025 Update - Replace Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -140861,123 +140842,122 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/7vzs-mg28",
+            "issued": "2023-12-14",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/7vzs-mg28",
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
+            "title": "MeSH 2025 Update - Replace Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://zfin.org/",
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
-            "identifier": "94570c43-8e2f-4bf0-a5b4-6f03cd74eb3e",
+            "dataQuality": true,
             "description": "<p>ZFIN serves as the zebrafish model organism database. It aims to: a) be the community database resource for the laboratory use of zebrafish, b) develop and support integrated zebrafish genetic, genomic and developmental information, c) maintain the definitive reference data sets of zebrafish research information, d) to link this information extensively to corresponding data in other model organism and human databases, e) facilitate the use of zebrafish as a model for human biology, and f) serve the needs of the research community.</p>",
-            "title": "The Zebrafish Model Organism Database (ZFIN)",
+            "identifier": "94570c43-8e2f-4bf0-a5b4-6f03cd74eb3e",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://zfin.org/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
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
+            "title": "The Zebrafish Model Organism Database (ZFIN)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vkqw-3twk",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2014-02-04",
-            "keyword": [
-                "cdrh",
-                "gudid",
-                "udi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rajan, Velayudhan",
                 "hasEmail": "mailto:Velayudhan.Rajan@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "C37E5FDF-6717-4AB3-8585-1808C7BF3B3B",
             "description": "The Global Unique Device Identification Database (GUDID) contains key device identification information submitted to the FDA about medical devices that have Unique Device Identifiers (UDI). Unique device identification is a system being established by the",
-            "title": "GUDID Download",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "description": "The Global Unique Device Identification Database (GUDID) contains key device identification information submitted to the FDA about medical devices that have Unique Device Identifiers (UDI). Unique device identification is a system being established by the",
                     "downloadURL": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/GlobalUDIDatabaseGUDID/default.htm",
-                    "mediaType": "text/html",
-                    "description": "The Global Unique Device Identification Database (GUDID) contains key device identification information submitted to the FDA about medical devices that have Unique Device Identifiers (UDI). Unique device identification is a system being established by the"
+                    "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "C37E5FDF-6717-4AB3-8585-1808C7BF3B3B",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh",
+                "gudid",
+                "udi"
+            ],
+            "landingPage": "https://healthdata.gov/d/vkqw-3twk",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2014-02-04",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "GUDID Download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/opioid-treatment-program-providers",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2023-05-21/2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "references": [
-                "https://data.cms.gov/resources/opioid-treatment-program-providers-methodology"
-            ],
-            "keyword": [
-                "drugs",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/f1a8c197-b53d-4c24-9770-aea5d5a97dfb/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/opioid-treatment-program-providers-data-dictionary",
             "description": "The Opioid Treatment Program (OTP) Providers dataset provides information on Providers who have enrolled in Medicare under the Opioid Treatment Program. It contains provider's name, National Provider Identifier (NPI), address, phone number and the effective enrollment date.",
-            "title": "Opioid Treatment Program Providers",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f1a8c197-b53d-4c24-9770-aea5d5a97dfb/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f1a8c197-b53d-4c24-9770-aea5d5a97dfb/data",
+                    "mediaType": "text/html",
                     "title": "Opioid Treatment Program Providers : 2025-01-21"
                 },
                 {
@@ -141989,26 +141969,60 @@
                     "title": "Opioid Treatment Program Providers : 2023-05-30"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/opioid-treatment-program-providers-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/f1a8c197-b53d-4c24-9770-aea5d5a97dfb/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "drugs",
+                "medicare",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/opioid-treatment-program-providers",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/opioid-treatment-program-providers-methodology"
+            ],
+            "temporal": "2023-05-21/2025-01-18",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Opioid Treatment Program Providers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ahrq.gov/professionals/systems/monahrq/index.html",
             "bureauCode": [
                 "009:33"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "MONAHRQ user support",
+                "hasEmail": "mailto:monahrq@ahrq.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.ahrq.gov/professionals/systems/monahrq/software/index.html",
+            "description": "<p>MONAHRQ\u00ae is a desktop software tool that enables organizations\u2014such as state and local data organizations, regional reporting collaborations, hospitals and hospital systems, nursing homes and nursing home organizations, and health plans\u2014to quickly and easily generate a health care reporting website.</p>\n<p>Effective September 27, 2017, technical support and software updates will no longer be available. Version 7, build 5, will be the final update. Existing software and supporting materials will remain available on this site. In addition, the open source project will remain active with software and materials available through GitHub: <a href=\"https://github.com/AHRQ/MONAHRQ-Open-Source\">https://github.com/AHRQ/MONAHRQ-Open-Source</a></p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://monahrq.ahrq.gov/download.shtml",
+                    "mediaType": "text/html",
+                    "title": "Widget "
+                }
+            ],
+            "identifier": "8e9604e5-028d-46ed-8f10-524904d3e60d",
             "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "claims",
                 "community health",
@@ -142030,31 +142044,15 @@
                 "utlization",
                 "website"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "MONAHRQ user support",
-                "hasEmail": "mailto:monahrq@ahrq.gov"
-            },
+            "landingPage": "https://www.ahrq.gov/professionals/systems/monahrq/index.html",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services, Agency for Healthcare Research and Quality"
             },
-            "identifier": "8e9604e5-028d-46ed-8f10-524904d3e60d",
-            "description": "<p>MONAHRQ\u00ae is a desktop software tool that enables organizations\u2014such as state and local data organizations, regional reporting collaborations, hospitals and hospital systems, nursing homes and nursing home organizations, and health plans\u2014to quickly and easily generate a health care reporting website.</p>\n<p>Effective September 27, 2017, technical support and software updates will no longer be available. Version 7, build 5, will be the final update. Existing software and supporting materials will remain available on this site. In addition, the open source project will remain active with software and materials available through GitHub: <a href=\"https://github.com/AHRQ/MONAHRQ-Open-Source\">https://github.com/AHRQ/MONAHRQ-Open-Source</a></p>",
-            "title": "MONAHRQ",
-            "programCode": [
-                "009:072"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://monahrq.ahrq.gov/download.shtml",
-                    "mediaType": "text/html",
-                    "title": "Widget "
-                }
-            ],
-            "describedBy": "https://www.ahrq.gov/professionals/systems/monahrq/software/index.html",
-            "dataQuality": true,
             "theme": [
                 "Community",
                 "Health",
@@ -142064,86 +142062,65 @@
                 "Inpatient",
                 "National",
                 "State"
-            ]
+            ],
+            "title": "MONAHRQ"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nlm.nih.gov/databases/databases_oldmedline.html",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ht7d-jhpy",
             "description": "The OLDMEDLINE subset in PubMed\u00ae represents journal article citations from two print indexes: Cumulated Index Medicus (CIM) and the Current List of Medical Literature (CLML). Created by the National Library of Medicine\u00ae (NLM\u00ae), there are approximately 2,011,000 article citations from international biomedical journals that cover the fields of medicine, preclinical sciences and allied health sciences from 1946 through 1965. OLDMEDLINE records, which are included in the MEDLINE\u00ae database, can be searched via PubMed.\n\nThe OLDMEDLINE subset in PubMed contains citations from the 1960 through 1965 Cumulated Index Medicus (CIM) print indexes and the 1946 through 1959 Current List of Medical Literature (CLML) print indexes. The OLDMEDLINE subset does not include citations from the Quarterly Cumulative Index Medicus (QCIM) print indexes. A hand search of the QCIM print indexes is necessary to ensure comprehensive review of medical periodical literature of the world from 1946 through 1956.",
-            "title": "OLDMEDLINE Data",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nlm.nih.gov/databases/databases_oldmedline.html",
-                    "description": "Information on searching the OLDMEDLINE subset in PubMed",
                     "@type": "dcat:Distribution",
+                    "description": "Information on searching the OLDMEDLINE subset in PubMed",
+                    "downloadURL": "https://www.nlm.nih.gov/databases/databases_oldmedline.html",
+                    "mediaType": "text/html",
                     "title": "OLDMEDLINE Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ht7d-jhpy",
+            "issued": "2021-08-26",
+            "keyword": [
+                "dataset",
+                "literature"
+            ],
+            "landingPage": "https://www.nlm.nih.gov/databases/databases_oldmedline.html",
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
+            "title": "OLDMEDLINE Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/mortality-restricted.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-08",
-            "@type": "dcat:Dataset",
-            "temporal": "1979/2019",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/LMF2019-DataDictionary-MortVars.pdf"
-            ],
-            "keyword": [
-                "linked mortality files",
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
-            "identifier": "https://data.cdc.gov/api/views/m97v-d4fn",
-            "description": "NCHS has linked data from various surveys with death certificate records from the National Death Index (NDI). Linkage of the NCHS survey participant data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality. The Linked Mortality Files (LMF) have been updated with mortality follow-up data through December 31, 2019.",
-            "title": "NCHS Survey Data Linked to National Death Index (NDI) Mortality Files",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate tables (see Tables 1 and 2 on page 10) here: https://www.cdc.gov/nchs/data/datalinkage/2019NDI-Linkage-Methods-and-Analytic-Considerations-508.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "NCHS has linked data from various surveys with death certificate records from the National Death Index (NDI). Linkage of the NCHS survey participant data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality. The Linked Mortality Files (LMF) have been updated with mortality follow-up data through December 31, 2019.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142151,53 +142128,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables (see Tables 1 and 2 on page 10) here: https://www.cdc.gov/nchs/data/datalinkage/2019NDI-Linkage-Methods-and-Analytic-Considerations-508.pdf",
+            "identifier": "https://data.cdc.gov/api/views/m97v-d4fn",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-08",
+            "keyword": [
+                "linked mortality files",
+                "nchs surveys",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/mortality-restricted.htm",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/LMF2019-DataDictionary-MortVars.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "1979/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Survey Data Linked to National Death Index (NDI) Mortality Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-epidemiologic-survey-alcohol-and-related-conditions-nesarc%E2%80%94wave-1-2001%E2%80%932002-and-3",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2014-04-08",
-            "temporal": "2001-01-01T00:00:00-05:00/2005-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "adult",
-                "alcohol",
-                "anxiety",
-                "cohort",
-                "disability",
-                "epidemiology",
-                "longitudinal survey",
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
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "ff29c1d0-8d38-44ed-a49f-c86eea464c06",
+            "dataQuality": true,
             "description": "<p>National Epidemiologic Survey on Alcohol and Related Conditions (NESARC) was designed to assess the prevalence of alcohol use disorders (AUD) and their associated disabilities in the general population. The survey is the largest ever comorbidity study of multiple mental health disorders among U.S. adults, including alcohol and other substance use disorders, personality disorders, and anxiety and mood disorders. NESARC is designed to be a longitudinal survey with the first wave fielded in 2001\u20132002. The second wave of interviews was completed in 2004\u20132005 and used the same sample of respondents.</p>\n<p>NESARC is a nationwide household survey with a probability sample representative of US adults. The final sample for Wave 1 was 43,093 respondents; Wave 2 was 34,653 of the Wave 1 respondents.</p>\n<p>Data are not publicly available; however, researchers may request specific analyses via Census.</p>",
-            "title": "National Epidemiologic Survey on Alcohol and Related Conditions (NESARC)\u2014Wave 1 (2001\u20132002), and Wave 2 (2004\u20132005)",
-            "programCode": [
-                "009:062"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142224,59 +142196,52 @@
                     "title": " "
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ff29c1d0-8d38-44ed-a49f-c86eea464c06",
+            "issued": "2014-04-08",
+            "keyword": [
+                "adult",
+                "alcohol",
+                "anxiety",
+                "cohort",
+                "disability",
+                "epidemiology",
+                "longitudinal survey",
+                "mental health",
+                "mood disorder",
+                "other",
+                "population statistics",
+                "sexual assault",
+                "substance use"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-epidemiologic-survey-alcohol-and-related-conditions-nesarc%E2%80%94wave-1-2001%E2%80%932002-and-3",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:062"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "temporal": "2001-01-01T00:00:00-05:00/2005-12-31T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "National Epidemiologic Survey on Alcohol and Related Conditions (NESARC)\u2014Wave 1 (2001\u20132002), and Wave 2 (2004\u20132005)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-08-05",
-            "temporal": "1983/2021",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
-            "keyword": [
-                "american indian and alaskan native",
-                "asian",
-                "asian or pacific islander",
-                "black",
-                "bridged race",
-                "fetal death data set",
-                "fetal deaths",
-                "fetal mortality",
-                "health us",
-                "late fetal deaths",
-                "late fetal mortality",
-                "national vital statistics system",
-                "native hawaiian or pacific islander",
-                "non-hispanic",
-                "nvss",
-                "perinatal deaths",
-                "perinatal mortality",
-                "race and hispanic origin of mother",
-                "single race",
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
-            "identifier": "https://data.cdc.gov/api/views/vac9-j9wr",
             "description": "Data on fetal, late fetal, and perinatal mortality rates in the United States, by detailed race and Hispanic origin of mother. Data are from Health, United States. Source: National Center for Health Statistics, National Vital Statistics System, Fetal Death Data Set.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS_Fetal, late fetal, and perinatal mortality rates, by detailed race and Hispanic origin of mother United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142299,45 +142264,58 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/vac9-j9wr",
+            "issued": "2024-08-05",
+            "keyword": [
+                "american indian and alaskan native",
+                "asian",
+                "asian or pacific islander",
+                "black",
+                "bridged race",
+                "fetal death data set",
+                "fetal deaths",
+                "fetal mortality",
+                "health us",
+                "late fetal deaths",
+                "late fetal mortality",
+                "national vital statistics system",
+                "native hawaiian or pacific islander",
+                "non-hispanic",
+                "nvss",
+                "perinatal deaths",
+                "perinatal mortality",
+                "race and hispanic origin of mother",
+                "single race",
+                "white"
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
+            "temporal": "1983/2021",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS_Fetal, late fetal, and perinatal mortality rates, by detailed race and Hispanic origin of mother United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ybum-psnc",
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
-            "identifier": "https://data.cdc.gov/api/views/ybum-psnc",
             "description": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142360,47 +142338,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ybum-psnc",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "vancomycin-resistant staphylococcus aureus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ybum-psnc",
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
+            "title": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-original-medicare-enrollment",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/3997fb87-a6d5-41d0-823f-7a62283e8035/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
             "description": "The CMS Program Statistics -\u00a0Original Medicare Enrollment tables provide data on characteristics of the Original Medicare\u00a0population.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR ENROLL AB 9. \u00a0Original Medicare Enrollment: \u00a0Part A and/or Part B Total, Aged, and Disabled Enrollees, Yearly Trend\n\tMDCR ENROLL AB 10. \u00a0Original Medicare Enrollment: Part A and/or Part B Enrollees, by Age Group, Yearly Trend\n\tMDCR ENROLL AB 11. \u00a0Original Medicare Enrollment: \u00a0Part A and/or Part B Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 12. \u00a0Original Medicare Enrollment: \u00a0Part A and/or Part B Enrollees, by Type of Entitlement and Demographic Characteristics\n\tMDCR ENROLL AB 13. \u00a0Original Medicare Enrollment: \u00a0Part A and/or Part B Total, Aged, and Disabled Enrollees, by Area of Residence\n\tMDCR ENROLL AB 14. \u00a0Original Medicare Enrollment: \u00a0Part A and/or Part B Enrollees, by Type of Entitlement and Area of Residence",
-            "title": "CMS Program Statistics - Original Medicare Enrollment",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142457,46 +142435,50 @@
                     "title": "CMS Program Statistics - Original Medicare Enrollment : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/3997fb87-a6d5-41d0-823f-7a62283e8035/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "beneficiary enrollment",
+                "health equity",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-original-medicare-enrollment",
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
+            "title": "CMS Program Statistics - Original Medicare Enrollment"
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
-                "ncird",
-                "respiratory-virus-response"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alicia Budd, Krista Kniss, and Arielle Colon",
                 "hasEmail": "mailto:acp4@cdc.gov, krk9@cdc.gov, nnp8@cdc.gov  "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
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
@@ -142519,80 +142501,74 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/6svj-q4zv",
+            "issued": "2023-09-26",
+            "keyword": [
+                "ncird",
+                "respiratory-virus-response"
+            ],
+            "landingPage": "https://data.cdc.gov/d/6svj-q4zv",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-18",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "US",
+            "temporal": "2022-10-08/2024-02-17",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Outpatient Respiratory Illness Activity Map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://zork5.wustl.edu/nida/",
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
                 "fn": "POLLOCK, JONATHAN D",
                 "hasEmail": "mailto:jpollock@nida.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "2e9312a6-a8e4-4351-abc2-21d355b6ce19",
+            "dataQuality": true,
             "description": "<p>Blood and other biospecimens along with phenotypic data collected, archived and stored.</p>",
-            "title": "NIDA Center on Genetics Studies",
+            "identifier": "2e9312a6-a8e4-4351-abc2-21d355b6ce19",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "https://zork5.wustl.edu/nida/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:059"
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
+            "title": "NIDA Center on Genetics Studies"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -142615,44 +142591,47 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1NN. Viral hemorrhagic fevers, Junin virus to Viral hemorrhagic fevers, Lujo virus"
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
-                "https://www.vsp.com",
-                "https://www.cdc.gov/visionhealth/vehss/data/claims/vsp.html"
-            ],
-            "keyword": [
-                "claims",
-                "medical diagnoses",
-                "vsp"
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
-            "identifier": "https://data.cdc.gov/api/views/4r3g-hv9c",
+            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Vision-Service-Plan-VSP-Vision-and-Eye-Health-Surv/4r3g-hv9c",
             "description": "2016. This dataset is a de-identified summary table of vision and eye health data indicators from VSP, stratified by all available combinations of age group, race/ethnicity, gender, and state. VSP claims for VEHSS provides a convenience sample of vision insurance members representing approximately more than 1 in 4 of the U.S. population. VSP uses a web-based claims submissions system to collect and process claims. The denominator of the rates represents persons with VSP benefits as reported by employers, and is subject to some uncertainty.  VSP data for VEHSS include Service Utilization and Eye Health Condition indicators.  Certain ophthalmic conditions and procedures are covered by health insurance and are not covered by managed vision insurance, claims based eye disease prevalence may therefore be expected to undercount true prevalence.  Person level claims and person counts are not publically available.  Reported rates were suppressed for de-identification to ensure protection of patient privacy. Detailed information on VEHSS VSP analyses can be found on the VEHSS VSP webpage (link). Information on VSP data can be found on the VSP website (www.vsp.com). The VEHSS VSP dataset was last updated in June 2018.",
-            "title": "Vision Service Plan (VSP) \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142675,45 +142654,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Vision-Service-Plan-VSP-Vision-and-Eye-Health-Surv/4r3g-hv9c",
+            "identifier": "https://data.cdc.gov/api/views/4r3g-hv9c",
+            "issued": "2023-09-21",
+            "keyword": [
+                "claims",
+                "medical diagnoses",
+                "vsp"
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
+                "https://www.vsp.com",
+                "https://www.cdc.gov/visionhealth/vehss/data/claims/vsp.html"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "Vision Service Plan (VSP) \u2013 Vision and Eye Health Surveillance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024, 2024-2025",
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
-            "identifier": "https://data.cdc.gov/api/views/4g6p-3ed6",
             "description": "\u2022 Weekly Influenza Vaccination Coverage and Comparison among adults 18 Years and Older by Jurisdiction\n\n \u2022 Weekly estimates of influenza vaccination coverage and intent for vaccination among adults are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/).",
-            "title": "Weekly Differences in Cumulative Influenza Vaccination Coverage and Comparison Between 2024-25 and 2023-24 Among Adults 18 Years, Overall, by Selected Demographics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142736,59 +142715,58 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
-            "theme": [
-                "Flu Vaccinations"
+            "identifier": "https://data.cdc.gov/api/views/4g6p-3ed6",
+            "issued": "2024-09-26",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
+                "vsd"
             ],
+            "landingPage": "https://www.cdc.gov/fluvaxview/dashboard/index.html",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-29",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024, 2024-2025",
+            "theme": [
+                "Flu Vaccinations"
+            ],
+            "title": "Weekly Differences in Cumulative Influenza Vaccination Coverage and Comparison Between 2024-25 and 2023-24 Among Adults 18 Years, Overall, by Selected Demographics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-geographic-comparisons/medicare-advantage-geographic-variation-national-state",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-11-01",
-            "temporal": "2021-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-30",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-05/1633f75a-93d4-4600-80f4-ba033c9d8e38/Medicare%20Advantage%20Geographic%20Variation%20National%20%20State_Methods_RY24_508.pdf"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "inpatient",
-                "medicare",
-                "medicare advantage",
-                "national",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/8e989bc0-2260-49a7-9c6d-8e9e10af7cea/data-viewer",
-            "description": "The Medicare Advantage Geographic Variation National & State dataset provides information on demographic characteristics and service utilization for hospital inpatient, skilled nursing facility services, outpatient, DME, and professional services between 2016-2021 for Medicare Advantage beneficiaries at the national and state levels.",
-            "title": "Medicare Advantage Geographic Variation - National & State",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-06/7ae600cf-5662-4462-8d86-7aab3f58e7b8/Medicare%20Advantage%20Geographic%20Variation%20National%20%20State%20Data%20Dictionary_RY24.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Medicare Advantage Geographic Variation National & State dataset provides information on demographic characteristics and service utilization for hospital inpatient, skilled nursing facility services, outpatient, DME, and professional services between 2016-2021 for Medicare Advantage beneficiaries at the national and state levels.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8e989bc0-2260-49a7-9c6d-8e9e10af7cea/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8e989bc0-2260-49a7-9c6d-8e9e10af7cea/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Advantage Geographic Variation - National & State : 2021-01-15"
                 },
                 {
@@ -142804,46 +142782,50 @@
                     "title": "Medicare Advantage Geographic Variation - National & State : 2021-01-15"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-06/7ae600cf-5662-4462-8d86-7aab3f58e7b8/Medicare%20Advantage%20Geographic%20Variation%20National%20%20State%20Data%20Dictionary_RY24.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/8e989bc0-2260-49a7-9c6d-8e9e10af7cea/data-viewer",
+            "issued": "2022-11-01",
+            "keyword": [
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "medicare advantage",
+                "national",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-geographic-comparisons/medicare-advantage-geographic-variation-national-state",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-30",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-05/1633f75a-93d4-4600-80f4-ba033c9d8e38/Medicare%20Advantage%20Geographic%20Variation%20National%20%20State_Methods_RY24_508.pdf"
+            ],
+            "temporal": "2021-01-01/2021-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Advantage Geographic Variation - National & State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/protein",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/2xvy-u8hi",
             "description": "The Protein database is a collection of sequences from several sources, including translations from annotated coding regions in GenBank, RefSeq and TPA, as well as records from SwissProt, PIR, PRF, and PDB. Protein sequences are the fundamental determinants of biological structure and function.",
-            "title": "Protein",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142852,40 +142834,41 @@
                     "title": "Protein - Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/2xvy-u8hi",
+            "issued": "2021-08-26",
+            "keyword": [
+                "api",
+                "dataset",
+                "protein"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/protein",
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
+            "title": "Protein"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/vtdc-bx7p",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-07-27",
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
-            "identifier": "eec7fbe6-c4c4-5915-b3d0-be5828ef4e9d",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2021",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142893,47 +142876,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "eec7fbe6-c4c4-5915-b3d0-be5828ef4e9d",
+            "issued": "2021-07-27",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/vtdc-bx7p",
             "license": "https://www.usa.gov/government-works",
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
+            "title": "State Drug Utilization Data 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qvvb-s7gu",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "animal",
-                "congenital syndrome",
-                "nedss",
-                "netss",
-                "nndss",
-                "rabies",
-                "rubella",
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
-            "identifier": "https://data.cdc.gov/api/views/qvvb-s7gu",
             "description": "NNDSS - Table II. Rabies, animal to Rubella, congenital syndrome - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum.\r\n \r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Rabies, animal to Rubella, congenital syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -142956,44 +142932,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qvvb-s7gu",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "animal",
+                "congenital syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "rabies",
+                "rubella",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qvvb-s7gu",
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
+            "title": "NNDSS - Table II. Rabies, animal to Rubella, congenital syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/txmx-urgu",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/txmx-urgu",
             "description": "TOXLINE was the National Library of Medicine (NLM) bibliographic database for toxicology, a varied science encompassing many disciplines. TOXLINE records provide bibliographic information covering the biochemical, pharmacological, physiological, and toxicological effects of drugs and other chemicals. TOXLINE references were drawn from various sources organized into component subfiles.\n\nThis version of TOXLINE is no longer updated. Updated TOXLINE content is available in PubMed or by searching PubMed using the search string: tox [sb] .",
-            "title": "Toxicology Information Online (TOXLINE) (RETIRED)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/toxspeclease/",
-                    "description": "NOTE - This version of TOXLINE is no longer updated. Updated TOXLINE content is available in PubMed by searching using the search string: tox [su]. These data are provided for archival and research purposes only.",
                     "@type": "dcat:Distribution",
+                    "description": "NOTE - This version of TOXLINE is no longer updated. Updated TOXLINE content is available in PubMed by searching using the search string: tox [su]. These data are provided for archival and research purposes only.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/toxspeclease/",
+                    "mediaType": "text/html",
                     "title": "Download - TOXLINE Archival Data"
                 },
                 {
@@ -143003,21 +142987,49 @@
                     "title": "Sample Data "
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/txmx-urgu",
+            "issued": "2020-09-21",
+            "keyword": [
+                "data distribution"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/txmx-urgu",
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
+            "title": "Toxicology Information Online (TOXLINE) (RETIRED)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/study-womens-health-across-nation-swan-biospecimen-repository",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Steffenie Merillat",
+                "hasEmail": "mailto:swan.repository@umich.edu"
+            },
+            "describedBy": "http://datawarehouse.swanrepository.com/userLogIn",
+            "description": "<p>The SWAN Repository is the biospecimen bank of the SWAN study. All stored specimens are from the 3,302 SWAN participants, collected across the 14 clinic visits (Baseline and 13 follow-up visits). Available biospecimen types include serum, plasma, urine and DNA which total nearly 1.8 million. Both Repository specimens and data generated through Repository studies and subsequently returned are available through the SWAN Repository. Through the Repository website, registered users can submit inquiries and applications for access to these resources.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.swanstudy.org/swan-research/data-access/",
+                    "mediaType": "text/html",
+                    "title": "HTML "
+                }
+            ],
+            "identifier": "f6f8f6a1-280b-48a2-a3bc-517cdfab8b76",
             "issued": "2015-03-04",
-            "temporal": "2000-09-01T00:00:00-04:00/2000-09-01T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "biobank",
                 "bone loss",
@@ -143038,65 +143050,35 @@
                 "vasomotor symptoms",
                 "women s health"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Steffenie Merillat",
-                "hasEmail": "mailto:swan.repository@umich.edu"
-            },
+            "landingPage": "https://healthdata.gov/dataset/study-womens-health-across-nation-swan-biospecimen-repository",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "f6f8f6a1-280b-48a2-a3bc-517cdfab8b76",
-            "description": "<p>The SWAN Repository is the biospecimen bank of the SWAN study. All stored specimens are from the 3,302 SWAN participants, collected across the 14 clinic visits (Baseline and 13 follow-up visits). Available biospecimen types include serum, plasma, urine and DNA which total nearly 1.8 million. Both Repository specimens and data generated through Repository studies and subsequently returned are available through the SWAN Repository. Through the Repository website, registered users can submit inquiries and applications for access to these resources.</p>",
-            "title": "Study of Womens Health Across the Nation (SWAN) Biospecimen Repository",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.swanstudy.org/swan-research/data-access/",
-                    "mediaType": "text/html",
-                    "title": "HTML "
-                }
-            ],
-            "describedBy": "http://datawarehouse.swanrepository.com/userLogIn",
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2000-09-01T00:00:00-04:00/2000-09-01T00:00:00-04:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Study of Womens Health Across the Nation (SWAN) Biospecimen Repository"
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
-            "identifier": "https://data.cdc.gov/api/views/kevv-m5vs",
             "description": "Weekly COVID-19 Vaccination Coverage of Adults 18 Years and Older by Jurisdiction \n\n\u2022 COVID-19 vaccination coverage among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module, providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html) \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
-            "title": "Weekly Differences in Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine by Selected Demographics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143119,29 +143101,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/kevv-m5vs",
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
+            "title": "Weekly Differences in Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine by Selected Demographics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/ehr-developers-reported-health-care-providers-participating-federal-programs",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/health-care-professional-health-it-developers",
-                "https://www.healthit.gov/data/quickstats/hospital-health-it-developers"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/ehr-developers-reported-health-care-providers-participating-federal-programs",
+            "description": "The Medicare &amp; Medicaid Electronic Health Record (EHR) Incentive Programs provide incentives to eligible ambulatory and inpatient providers to adopt electronic health records. This dataset provides the counts of health care providers that have reported a developer's product through participation in the Medicare EHR Incentive Program. The data are provided beginning in 2011. This dataset enables the tracking of trends in the adoption of healthIT by developer and by both office-based health care providers and non-federal acute-care hospitals. Filter the data by Program Year to get the most recent counts by health care provider type. The most recent data is available through the 2016 Program Year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/EHR-vendors-count-dataset.csv",
+                    "mediaType": "text/csv",
+                    "title": "EHR-vendors-count-dataset.csv"
+                }
             ],
+            "identifier": "5d6zvokd-upg9-fobb-lzgn-ep6jo1du8lkd",
+            "issued": "2023-10-03",
             "keyword": [
                 "adoption",
                 "cehrt",
@@ -143152,55 +143161,33 @@
                 "federal programs",
                 "health it"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/ehr-developers-reported-health-care-providers-participating-federal-programs",
+            "modified": "2017-07-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "5d6zvokd-upg9-fobb-lzgn-ep6jo1du8lkd",
-            "description": "The Medicare &amp; Medicaid Electronic Health Record (EHR) Incentive Programs provide incentives to eligible ambulatory and inpatient providers to adopt electronic health records. This dataset provides the counts of health care providers that have reported a developer's product through participation in the Medicare EHR Incentive Program. The data are provided beginning in 2011. This dataset enables the tracking of trends in the adoption of healthIT by developer and by both office-based health care providers and non-federal acute-care hospitals. Filter the data by Program Year to get the most recent counts by health care provider type. The most recent data is available through the 2016 Program Year.",
-            "title": "EHR Developers Reported by Health Care Providers Participating in Federal Programs",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/EHR-vendors-count-dataset.csv",
-                    "mediaType": "text/csv",
-                    "title": "EHR-vendors-count-dataset.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/quickstats/health-care-professional-health-it-developers",
+                "https://www.healthit.gov/data/quickstats/hospital-health-it-developers"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/ehr-developers-reported-health-care-providers-participating-federal-programs"
+            "title": "EHR Developers Reported by Health Care Providers Participating in Federal Programs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/cuyd-c53m",
             "bureauCode": [
                 "009:20"
             ],
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -143208,39 +143195,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/cuyd-c53m",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/cuyd-c53m",
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
+            "title": "Correlation between graphitic carbon and elemental carbon in diesel particulate matter in workplace atmospheres-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/Traces/trace.cgi",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ixrk-4tte",
             "description": "A repository of DNA sequence chromatograms (traces), base calls, and quality estimates for single-pass reads from various large-scale sequencing projects.",
-            "title": "Trace Archive",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143249,39 +143232,39 @@
                     "title": "Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ixrk-4tte",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "genomics"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Traces/trace.cgi",
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
+            "title": "Trace Archive"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rmzv-dc5f",
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
-            "identifier": "https://data.cdc.gov/api/views/rmzv-dc5f",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 national data: National Highway Traffic Safety Administration's (NHTSA) National Occupant Protection Use Survey (NOPUS), 2014. Source for 2014 state data: National Highway Traffic Safety Administration's (NHTSA) State Observation of Seat Belt Use, 2014",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, All States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143304,45 +143287,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rmzv-dc5f",
+            "issued": "2016-09-26",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rmzv-dc5f",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, All States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3svv-v5nh",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
-                "arboviral diseases",
-                "babesiosis",
-                "nedss",
-                "netss",
-                "nndss",
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
-            "identifier": "https://data.cdc.gov/api/views/3svv-v5nh",
             "description": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\nFootnotes:\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143365,41 +143342,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3svv-v5nh",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "arboviral diseases",
+                "babesiosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "western equine encephalitis virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/3svv-v5nh",
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
+            "title": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis"
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
-                "dentists",
-                "health us",
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
-            "identifier": "https://data.cdc.gov/api/views/9epi-jrff",
             "description": "Data on active dentists in the United States by state. Data are from Health, United States. SOURCE: American Dental Association, Health Policy Institute.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Dentists, by state: United States.",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143422,42 +143404,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9epi-jrff",
+            "issued": "2024-07-05",
+            "keyword": [
+                "dentists",
+                "health us",
+                "state"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cdc.gov/d/45um-c62r",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2014-04-02",
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
-            "identifier": "https://data.cdc.gov/api/views/45um-c62r",
             "description": "In general, total combined rates for traumatic brain injury (TBI)-related emergency department (ED) visits, hospitalizations and deaths have increased over the past decade.  Total combined rates of TBI-related hospitalizations, ED visits, and deaths climbed slowly from a rate of 521.0 per 100,000 in 2001 to 615.7 per 100,000 in 2005.  The rates then dipped to 595.1 per 100,000 in 2006 and 566.7 per 100,000 in 2007.  The rates then spiked sharply in 2008 and continued to climb through 2010 to a rate of 823.7 per 100,000.  Total combined rates of TBI-related hospitalizations, ED visits, and deaths are driven in large part by the relatively high number of TBI-related ED visits.  In comparison to ED visits, the overall rates of TBI-related hospitalizations remained relatively stable changing from 82.7 per 100,000 in 2001 to 91.7 per 100,000 in 2010.  TBI-related deaths also decreased slightly over time from 18.5 per 100,000 in 2001 to 17.1 per 100,000 in 2010.  Note that the axis scale for TBI-related deaths appears to the right of the chart and differs from TBI-related hospitalizations and ED visits.Go to http://www.cdc.gov/traumaticbraininjury/data/index.html to view more TBI data & statistics.",
-            "title": "Rates of TBI-related Emergency Department Visits, Hospitalizations, and Deaths - United States, 2001 \u2013 2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143480,40 +143461,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/45um-c62r",
+            "issued": "2014-04-02",
+            "keyword": [
+                "brain injury",
+                "head trauma",
+                "tbi",
+                "traumatic brain injury"
+            ],
+            "landingPage": "https://data.cdc.gov/d/45um-c62r",
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
+            "title": "Rates of TBI-related Emergency Department Visits, Hospitalizations, and Deaths - United States, 2001 \u2013 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/omim",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-01",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/hra4-qimf",
             "description": "Comprehensive, authoritative, and timely compendium of human genes and genetic phenotypes.",
-            "title": "OMIM (Online Mendelian Inheritance in Man)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143522,47 +143504,41 @@
                     "title": "OMIM (Online Mendelian Inheritance in Man)"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/hra4-qimf",
+            "issued": "2022-03-01",
+            "keyword": [
+                "api",
+                "genetics",
+                "genomics"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/omim",
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
+            "title": "OMIM (Online Mendelian Inheritance in Man)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-21",
-            "references": [
-                "https://www.resdac.org",
-                "https://www.cdc.gov/visionhealth/vehss/data/claims/medicare.html"
-            ],
-            "keyword": [
-                "claims",
-                "eye exams",
-                "medical diagnoses",
-                "medicare",
-                "service utilization",
-                "treated prevalence"
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
-            "identifier": "https://data.cdc.gov/api/views/e28h-tx85",
+            "describedBy": "https://chronicdata.cdc.gov/d/e28h-tx85",
             "description": "2014-2019. This dataset is a de-identified summary table of vision and eye health data indicators from Medicare claims, stratified by all available combinations of age group, race/ethnicity, gender, and state. Medicare claims for VEHSS includes beneficiaries who were fully enrolled in Medicare Part B Fee-for-Service (FFS) for the duration of the year. Medicare claims provide a convenience sample that includes approximately 30 million individuals annually, which represents nearly 89% of the US population aged 65 and older and 3.3% of the US population younger than 65, including persons disabled due to blindness. Medicare data for VEHSS include Service Utilization and Medical Diagnoses indicators. Data were suppressed for de-identification to ensure protection of patient privacy. Data will be updated as it becomes available. Detailed information on VEHSS Medicare analyses can be found on the VEHSS Medicare webpage (cdc.gov/visionhealth/vehss/data/claims/medicare.html). Information on available Medicare claims data can be found on the ResDac website (www.resdac.org). The VEHSS Medicare dataset was last updated May 2023.",
-            "title": "Medicare Claims \u2013 Vision and Eye Health Surveillance",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143585,55 +143561,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/d/e28h-tx85",
+            "identifier": "https://data.cdc.gov/api/views/e28h-tx85",
+            "issued": "2021-06-15",
+            "keyword": [
+                "claims",
+                "eye exams",
+                "medical diagnoses",
+                "medicare",
+                "service utilization",
+                "treated prevalence"
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
+                "https://www.resdac.org",
+                "https://www.cdc.gov/visionhealth/vehss/data/claims/medicare.html"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "Medicare Claims \u2013 Vision and Eye Health Surveillance"
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
-            "identifier": "https://data.cdc.gov/api/views/9gay-j69q",
             "description": "Data on obesity among children and adolescents aged 2-19 years by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health and Nutrition Examination Survey. For more information on the National Health and Nutrition Examination Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Obesity among children and adolescents aged 2\u201319 years, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143656,46 +143625,55 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -143718,68 +143696,77 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/986w-8kut",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "cryptosporidiosis",
+                "cyclosporiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/986w-8kut",
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
+            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.tcdb.org/",
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
                 "fn": "RAVICHANDRAN, VEERASAMY\u00a0",
                 "hasEmail": "mailto:veerasamy.ravichandra@nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "25c28438-56d2-49ac-8acc-c19c9dbbc6c7",
+            "dataQuality": true,
             "description": "<p>The Transporter Classification Database details a comprehensive classification system for membrane transport proteins known as the Transporter Classification (TC) system. The TC system is analogous to the Enzyme Commission (EC) system for classification of enzymes, except that it incorporates both functional and phylogenetic information. Descriptions, TC numbers, and examples of over 600 families of transport proteins are provided.</p>",
-            "title": "Transporter Classification Database (TCDB)",
+            "identifier": "25c28438-56d2-49ac-8acc-c19c9dbbc6c7",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.tcdb.org/",
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
+            "title": "Transporter Classification Database (TCDB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/phkb-u384",
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
-            "identifier": "https://data.cdc.gov/api/views/phkb-u384",
             "description": "Gulf War Illness (GWI) is a persistent chronic neuroinflammatory illness exacerbated by external stressors and characterized by fatigue, musculoskeletal pain, cognitive and neurological problems linked to underlying immunological dysfunction for which there is no known treatment.  Here, we constructed a logic model of immune regulatory behavior between human clinical samples and mouse models of GWI subtyped by exposure to traumatic stress.  We identify several ideal multi-intervention strategies and potential drug candidates that may be used to treat chronic neuroinflammation in GWI.",
-            "title": "Modeling Neuroimmune Interactions in Human Subjects and Animal Models to Predict Subtype Specific Multidrug Treatments for Gulf War Illness",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143787,46 +143774,41 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/phkb-u384",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/phkb-u384",
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
+            "title": "Modeling Neuroimmune Interactions in Human Subjects and Animal Models to Predict Subtype Specific Multidrug Treatments for Gulf War Illness"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/wgs/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/8hqv-4ds7",
             "description": "Whole Genome Shotgun (WGS) projects are genome assemblies of incomplete genomes or incomplete chromosomes of prokaryotes or eukaryotes that are generally being sequenced by a whole genome shotgun strategy. WGS projects may be annotated, but annotation is not required. NCBI has a Prokaryotic Genomes Annotation Pipeline that may be requested at the time the genome files are submitted to GenBank. This pipeline generates a submission-ready annotated file that is posted back to the submitter for review and which the submitter could edit prior to data release.\n\nThe public WGS projects are at the list of WGS projects. https://www.ncbi.nlm.nih.gov/Traces/wgs/",
-            "title": "Whole Genome Shotgun Submissions",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/genomesubmit/",
-                    "description": "Both WGS and non-WGS genomes, including gapless complete bacterial chromosomes, can be submitted via the Submission Portal. You will be asked to choose whether the genome being submitted is considered WGS or not",
                     "@type": "dcat:Distribution",
+                    "description": "Both WGS and non-WGS genomes, including gapless complete bacterial chromosomes, can be submitted via the Submission Portal. You will be asked to choose whether the genome being submitted is considered WGS or not",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/genomesubmit/",
+                    "mediaType": "text/html",
                     "title": "Prokaryotic and Eukaryotic Genomes Submission Guide"
                 },
                 {
@@ -143836,83 +143818,88 @@
                     "title": "Download Whole Genome Shotgun Sequences Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/8hqv-4ds7",
+            "issued": "2021-08-26",
+            "keyword": [
+                "computational biology",
+                "dataset",
+                "genomics"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/wgs/",
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
+            "title": "Whole Genome Shotgun Submissions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/w2ns-vn28",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-10-08",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
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
-            "identifier": "a1a4d739-514c-5952-a6e0-8bc9a2bb2709",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_measure_allStates_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220509_ETL_DEV/measure_allStates_download.csv",
-                    "description": "{\"dataset\": \"measure_allStates_download\", \"stage\": \"devAuto\", \"update_id\": \"20220509_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates_download\", \"stage\": \"devAuto\", \"update_id\": \"20220509_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220509_ETL_DEV/measure_allStates_download.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates_download csv file"
                 }
             ],
+            "identifier": "a1a4d739-514c-5952-a6e0-8bc9a2bb2709",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/w2ns-vn28",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2022-05-09",
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
+            "title": "devAuto_measure_allStates_download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gjsp-ircr",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-27",
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
-            "identifier": "https://data.cdc.gov/api/views/gjsp-ircr",
             "description": "Footnotes for Health, US - Asthma in children younger than age 18, by selected characteristics: United States. \n\nData on asthma in children younger than age 18 in the United States, by selected characteristics. Data are from Health, United States. Source: National Center for Health Statistics, National Health Interview Survey.",
-            "title": "HUS_Footnote_Look_Up_ASTHCH",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143935,46 +143922,35 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gjsp-ircr",
+            "issued": "2024-09-27",
+            "landingPage": "https://data.cdc.gov/d/gjsp-ircr",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "HUS_Footnote_Look_Up_ASTHCH"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/tdge-ieq8",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/tdge-ieq8",
             "description": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S, a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -143997,68 +143973,105 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/tdge-ieq8",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "acute",
+                "chronic",
+                "nedss",
+                "netss",
+                "nndss",
+                "q fever",
+                "total",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/tdge-ieq8",
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
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/w2xy-hgqk",
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_concernLevel.csv",
+                    "mediaType": "text/csv",
+                    "title": "measure_concernLevel csv file"
+                }
             ],
+            "identifier": "1afe96ca-dd06-5002-b4c4-5f4f45e5a171",
+            "issued": "2021-10-08",
             "keyword": [
                 "dqatlas",
                 "dqatlas_prodauto",
                 "utility"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DataConnect Support Team",
-                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/d/w2xy-hgqk",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-07",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Medicare & Medicaid Services"
             },
-            "identifier": "1afe96ca-dd06-5002-b4c4-5f4f45e5a171",
-            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_measure_concernLevel",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_concernLevel.csv",
-                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
-                    "@type": "dcat:Distribution",
-                    "title": "measure_concernLevel csv file"
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
+            "title": "prodAuto_measure_concernLevel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2011-0",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2011 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2011) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2011-nid13563",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2011-nid13563"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2011-nid13563",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -144099,113 +144112,78 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2011-0",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2011-nid13563",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2011 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2011)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2011-nid13563",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2011) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2011-nid13563"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2011)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/w36q-qgu2",
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
-            "identifier": "4bc725b5-e88e-525c-880b-8547f0edd081",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_measure_allStates_downloadLink",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates_downloadLink.csv",
-                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates_downloadLink.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_allStates_downloadLink csv file"
                 }
             ],
+            "identifier": "4bc725b5-e88e-525c-880b-8547f0edd081",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/w36q-qgu2",
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
+            "title": "devAuto_measure_allStates_downloadLink"
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
-                "https://chronicdata.cdc.gov/d/p8tr-pquj"
-            ],
-            "keyword": [
-                "cdc",
-                "office on smoking and health",
-                "osh",
-                "tobacco",
-                "youth tobacco sales"
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
-            "identifier": "https://data.cdc.gov/api/views/escb-scz6",
+            "describedBy": "https://chronicdata.cdc.gov/Policy/SAMHSA-Synar-Reports-Youth-Tobacco-Sales/escb-scz6",
             "description": "1997-2018. Substance Abuse and Mental Health Services Administration (SAMHSA). Synar Reports: Youth Tobacco Sales. Policy \u2013 Youth Tobacco Sales. SAMHSA\u2019s Synar Report on Youth Tobacco Sales presents findings on compliance of the Synar Amendment aimed at decreasing youth access to tobacco, and reviews progress in enforcing State youth tobacco access laws and in reducing the percentage of retailers selling tobacco products to minors.",
-            "title": "SAMHSA Synar Reports: Youth Tobacco Sales",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144228,41 +144206,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Policy/SAMHSA-Synar-Reports-Youth-Tobacco-Sales/escb-scz6",
+            "identifier": "https://data.cdc.gov/api/views/escb-scz6",
+            "issued": "2023-07-14",
+            "keyword": [
+                "cdc",
+                "office on smoking and health",
+                "osh",
+                "tobacco",
+                "youth tobacco sales"
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
+                "https://chronicdata.cdc.gov/d/p8tr-pquj"
+            ],
             "theme": [
                 "Policy"
-            ]
+            ],
+            "title": "SAMHSA Synar Reports: Youth Tobacco Sales"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/nkri-ptxd",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-08-14",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "children",
-                "hus",
-                "vaccination"
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
-            "identifier": "https://data.cdc.gov/api/views/nkri-ptxd",
             "description": "Health, United States is an annual report on trends in health statistics, find more information at http://www.cdc.gov/nchs/hus.htm.",
-            "title": "Selected Trend Table from Health, United States, 2011. Vaccination coverage among children 19 - 35 months of age for selected diseases, by race, Hispanic origin, poverty level, and location of residence in metropolitan statistical area: United States, sel",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144285,35 +144267,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/nkri-ptxd",
+            "issued": "2013-08-14",
+            "keyword": [
+                "children",
+                "hus",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/nkri-ptxd",
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
+            "title": "Selected Trend Table from Health, United States, 2011. Vaccination coverage among children 19 - 35 months of age for selected diseases, by race, Hispanic origin, poverty level, and location of residence in metropolitan statistical area: United States, sel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rdfw-s4u4",
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
-            "identifier": "https://data.cdc.gov/api/views/rdfw-s4u4",
             "description": "Concentrated collection of aerosol particles on a substrate is essential for their chemical analysis using various microscopy and laser spectroscopic techniques. An impaction-based aerosol concentration system was developed for focused collection of particles using a multi-stage nozzle that consists of a succession of multiple smooth converging stages. Converging sections of the nozzle were designed to focus and concentrate a particle diameter range of 900 to 2500 nm into a relatively narrower particle beam to obtain particulate deposits with spot diameters of 0.5-1.56 mm. A slightly diverging section before the last contractions was included to allow for better focusing of particles at the lower end of the collectable diameter range. The characterization of this multi-stage nozzle and the impaction-based aerosol concentration system encompassing the nozzle was accomplished both numerically and experimentally. The numerical and experimental trends in collection efficiency and spot diameters agreed well qualitatively; however, the quantitative agreement between numerical and experimental results for wall losses was poor, particularly for larger particle diameters. The resulting concentrated particulate deposit, a spot sample, was analysed using Raman spectroscopy to probe effect of spot size on analytical sensitivity of measurement. The method\u2019s sensitivity was compared against other conventional techniques, such as filtration and aerosol focused impaction, implementing condensational growth.  Impaction encompassing the multi-stage focusing nozzle is the only method that can ensure high sensitivity at Reynolds numbers greater than 2000, that can be supported by small pumps which renders such method suitable for portable instrumentation.",
-            "title": "Characterization of a multi-stage focusing nozzle for collection of spot samples for aerosol chemical analysis",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144321,59 +144308,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rdfw-s4u4",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/rdfw-s4u4",
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
+            "title": "Characterization of a multi-stage focusing nozzle for collection of spot samples for aerosol chemical analysis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-15",
-            "temporal": "2010/2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "american indian and alaska native only",
-                "asian only",
-                "black non-hispanic",
-                "black only",
-                "domains of functioning",
-                "female",
-                "functional limitation",
-                "health us",
-                "hispanic",
-                "male",
-                "metropolitan statistical area",
-                "national health interview survey",
-                "native hawaiian or pacific islander only",
-                "nhis",
-                "poverty level",
-                "rural",
-                "sdoh-poverty-income",
-                "sdoh-social-emotional",
-                "urban",
-                "white non-hispanic",
-                "white only"
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
-            "identifier": "https://data.cdc.gov/api/views/bjpq-vm2t",
             "description": "Data on functional limitation (or functional difficulties) in adults age 18 and older in the United States, by selected characteristics. Data are from Health, United States. Source: National Center for Health Statistics, National Health Interview Survey. \nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Functional difficulties in adults age 18 and older, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144396,46 +144360,59 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bjpq-vm2t",
+            "issued": "2024-10-15",
+            "keyword": [
+                "american indian and alaska native only",
+                "asian only",
+                "black non-hispanic",
+                "black only",
+                "domains of functioning",
+                "female",
+                "functional limitation",
+                "health us",
+                "hispanic",
+                "male",
+                "metropolitan statistical area",
+                "national health interview survey",
+                "native hawaiian or pacific islander only",
+                "nhis",
+                "poverty level",
+                "rural",
+                "sdoh-poverty-income",
+                "sdoh-social-emotional",
+                "urban",
+                "white non-hispanic",
+                "white only"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-11-05",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
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
-            "landingPage": "https://data.cdc.gov/d/mvsw-zuaf",
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
-                "severe acute respiratory syndrome-associated coronavirus disease",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mvsw-zuaf",
             "description": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144458,44 +144435,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mvsw-zuaf",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe acute respiratory syndrome-associated coronavirus disease",
+                "shiga toxin-producing escherichia coli",
+                "shigellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mvsw-zuaf",
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
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.atsdr.cdc.gov/placeandhealth/svi/index.html",
+            "accrualPeriodicity": "biennial",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-03-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2018",
-            "modified": "2022-02-14",
-            "keyword": [
-                "2018",
-                "social vulnerability",
-                "social vulnerability index",
-                "tract",
-                "united states",
-                "vulnerable populations"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SVI Coordinator",
                 "hasEmail": "mailto:svi_coordinator@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4d8n-kk8a",
             "description": "ATSDR\u2019s Geospatial Research, Analysis & Services Program (GRASP) created Centers for Disease Control and Prevention Social Vulnerability Index (CDC SVI or simply SVI, hereafter) to help public health officials and emergency response planners identify and map the communities that will most likely need support before, during, and after a hazardous event.\n\nSVI indicates the relative vulnerability of every U.S. Census tract. Census tracts are subdivisions of counties for which the Census collects statistical data. SVI ranks the tracts on 15 social factors, including unemployment, minority status, and disability, and further groups them into four related themes. Thus, each tract receives a\nranking for each Census variable and for each of the four themes, as well as an overall ranking.\n\nIn addition to tract-level rankings, SVI 2018 also has corresponding rankings at the\ncounty level. Notes below that describe \u201ctract\u201d methods also refer to county methods.",
-            "title": "Social Vulnerability Index 2018 - United States, tract",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144518,22 +144497,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
+            "identifier": "https://data.cdc.gov/api/views/4d8n-kk8a",
+            "issued": "2020-03-11",
+            "keyword": [
+                "2018",
+                "social vulnerability",
+                "social vulnerability index",
+                "tract",
+                "united states",
+                "vulnerable populations"
+            ],
+            "landingPage": "https://www.atsdr.cdc.gov/placeandhealth/svi/index.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "biennial",
+            "modified": "2022-02-14",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "USA",
+            "temporal": "2018",
             "theme": [
                 "Health Statistics"
-            ]
+            ],
+            "title": "Social Vulnerability Index 2018 - United States, tract"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "Contains data for FDA Hydrolyzed Vegetable Protein (HVP) Containing Products recalls since February, 2010.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "97f8facf-a2b8-47f0-847b-d7e7bc165c09",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "community health",
                 "health",
@@ -144544,44 +144555,42 @@
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
-            "identifier": "97f8facf-a2b8-47f0-847b-d7e7bc165c09",
-            "description": "Contains data for FDA Hydrolyzed Vegetable Protein (HVP) Containing Products recalls since February, 2010.",
-            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xls",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nsrcf/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
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
+            "description": "The 2010 National Survey of Residential Care Facilities (NSRCF) is a first-ever national probability sample survey that collects data on U.S. residential care providers, their staffs and services, and the people they serve. It is designed to provide national estimates of the number of residential care facilities operating in the United States, the number of residents receiving care, and the characteristics of both the facilities and their residents. NSRCF was conducted between March and November 2010. All residential care facilities that participated in the survey were places that were licensed, registered, listed, certified, or otherwise regulated by the state and that had 4 or more licensed, certified, or registered beds, provided room and board with at least two meals a day, around-the-clock on-site supervision, and help with personal care such as bathing and dressing or health related services such as medication management. These facilities served a predominantly adult population and had at least one current resident. Facilities licensed to serve the mentally ill or the developmentally disabled populations exclusively were excluded from the survey.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The 2010 NSRCF data were collected through in-person interviews with facility directors and their \ndesignated staffs; no interviews were conducted directly with residents. Facility data included\nquestions on facility characteristics such as ownership, size, types of living arrangements and \namenities, policies, staffing, services, and general resident characteristics. Data collected on \nresidents included questions on the sampled residents\u2019 demographics, living arrangements, \nactivities, health conditions, cognitive and physical functioning, and services received. The total \nnumber of facilities that participated in the 2010 NSRCF is 2,302, and data are available on 8,094\nresidents from these facilities.",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "National Survey of Residential Care Facilities - Restricted Resident-Level Dataset"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5586-cehn",
+            "isPartOf": "https://www.cdc.gov/nchs/nsrcf/nsrcf_questionnaires.htm",
+            "issued": "2023-07-03",
             "keyword": [
                 "assisted living facilities",
                 "long-term care",
@@ -144592,73 +144601,42 @@
                 "sdoh-access-to-health-care",
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
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-07-03",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/5586-cehn",
-            "description": "The 2010 National Survey of Residential Care Facilities (NSRCF) is a first-ever national probability sample survey that collects data on U.S. residential care providers, their staffs and services, and the people they serve. It is designed to provide national estimates of the number of residential care facilities operating in the United States, the number of residents receiving care, and the characteristics of both the facilities and their residents. NSRCF was conducted between March and November 2010. All residential care facilities that participated in the survey were places that were licensed, registered, listed, certified, or otherwise regulated by the state and that had 4 or more licensed, certified, or registered beds, provided room and board with at least two meals a day, around-the-clock on-site supervision, and help with personal care such as bathing and dressing or health related services such as medication management. These facilities served a predominantly adult population and had at least one current resident. Facilities licensed to serve the mentally ill or the developmentally disabled populations exclusively were excluded from the survey.",
-            "title": "National Survey of Residential Care Facilities - Restricted Resident-Level Dataset",
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
-                    "title": "National Survey of Residential Care Facilities - Restricted Resident-Level Dataset"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/data/nsrcf/2010NSRCF_SurveyMethodologyandDocumentation.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "temporal": "2010-03/2010-10",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Survey of Residential Care Facilities - Restricted Resident-Level Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/smic-9bf9",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "congenital syndrome",
-                "nedss",
-                "netss",
-                "nndss",
-                "rubella",
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
-            "identifier": "https://data.cdc.gov/api/views/smic-9bf9",
             "description": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144681,44 +144659,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/smic-9bf9",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "congenital syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/smic-9bf9",
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
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fztq-uwup",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/fztq-uwup",
             "description": "NNDSS - Table 1H. Cholera to Coccidioidomycosis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - Table 1H. Cholera to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144741,45 +144719,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fztq-uwup",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "cholera",
+                "coccidioidomycosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fztq-uwup",
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
+            "title": "NNDSS - Table 1H. Cholera to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gepg-djaz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/gepg-djaz",
             "description": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144802,46 +144779,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gepg-djaz",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "anaplasma phagocytophilum infection",
+                "ehrlichia chaffeensis infection",
+                "ehrlichiosis and anaplasmosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/gepg-djaz",
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
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/j6gu-p9yd",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/j6gu-p9yd",
             "description": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -144864,68 +144840,104 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/j6gu-p9yd",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "acute",
+                "chronic",
+                "nedss",
+                "netss",
+                "nndss",
+                "q fever",
+                "total",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/j6gu-p9yd",
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
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/w63d-rrbu",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-27",
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
-            "identifier": "eba2c172-07ba-4a6a-877e-5373ca442243",
             "description": "All states (including the District of Columbia) are required to provide data to The Centers for Medicare &amp; Medicaid Services (CMS) on a range of indicators related to key application, eligibility, and enrollment processes within the state Medicaid and Children\u2019s Health Insurance Programs (CHIP). These data reflect enrollment activity for all populations receiving comprehensive Medicaid and CHIP benefits in all states, as well as state program performance.",
-            "title": "CHIP Applications, Eligibility Determinations, and Enrollment Data",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/StateMedicaidandCHIPApplicationsEligibilityDeterminationsandEnrollmentData04282022.csv",
-                    "description": "All states (including the District of Columbia) are required to provide data to The Centers for Medicare &amp; Medicaid Services (CMS) on a range of indicators related to key application, eligibility, and enrollment processes within the state Medicaid and Children\u2019s Health Insurance Programs (CHIP). These data reflect enrollment activity for all populations receiving comprehensive Medicaid and CHIP benefits in all states, as well as state program performance.",
                     "@type": "dcat:Distribution",
+                    "description": "All states (including the District of Columbia) are required to provide data to The Centers for Medicare &amp; Medicaid Services (CMS) on a range of indicators related to key application, eligibility, and enrollment processes within the state Medicaid and Children\u2019s Health Insurance Programs (CHIP). These data reflect enrollment activity for all populations receiving comprehensive Medicaid and CHIP benefits in all states, as well as state program performance.",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/StateMedicaidandCHIPApplicationsEligibilityDeterminationsandEnrollmentData04282022.csv",
+                    "mediaType": "text/csv",
                     "title": "State Medicaid and CHIP Applications, Eligibility Determinations, and Enrollment Data-09012021"
                 }
             ],
+            "identifier": "eba2c172-07ba-4a6a-877e-5373ca442243",
+            "issued": "2022-03-02",
+            "keyword": [
+                "applications",
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/w63d-rrbu",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2022-04-27",
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
+            "title": "CHIP Applications, Eligibility Determinations, and Enrollment Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-behavioral-risk-factor-surveillance-system-brfss",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Behavioral Risk Factor Surveillance System (BRFSS) is a state-based system of health surveys that collects information on health risk behaviors, preventive health practices, and health care access primarily related to chronic disease and injury. For many states, the BRFSS is the only available source of timely, accurate data on health-related behaviors.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/brfss/",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "15ece528-43c1-45c3-ba01-0b9a4f5a31f0",
             "issued": "2012-05-30",
-            "temporal": "1984-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "chronic disease",
                 "health",
@@ -144939,63 +144951,34 @@
                 "survey",
                 "trends"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-behavioral-risk-factor-surveillance-system-brfss",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "15ece528-43c1-45c3-ba01-0b9a4f5a31f0",
-            "description": "<p>The Behavioral Risk Factor Surveillance System (BRFSS) is a state-based system of health surveys that collects information on health risk behaviors, preventive health practices, and health care access primarily related to chronic disease and injury. For many states, the BRFSS is the only available source of timely, accurate data on health-related behaviors.</p>",
-            "title": "CDC Behavioral Risk Factor Surveillance System (BRFSS)",
-            "programCode": [
-                "009:072"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cdc.gov/brfss/",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1984-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "CDC Behavioral Risk Factor Surveillance System (BRFSS)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -145018,127 +145001,131 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9y49-tura",
+            "issued": "2021-06-23",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9y49-tura",
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
+            "title": "Active Bacterial Core surveillance (ABCs) Group A Streptococcus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/w6wc-sdh5",
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
-            "identifier": "05abc6c7-8d36-521a-82a8-3182ea85a1ea",
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
+            "identifier": "05abc6c7-8d36-521a-82a8-3182ea85a1ea",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/w6wc-sdh5",
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
-            "landingPage": "https://healthdata.gov/d/w73y-7zz6",
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
-            "identifier": "1632da10-d16e-57f6-8e2d-29bdd77949de",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure v2.11.16 (cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/measure.csv",
-                    "description": "Scorecard measure v2.11.16 (cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure v2.11.16 (cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/measure.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure v2.11.16 (cmsdev)"
                 }
             ],
+            "identifier": "1632da10-d16e-57f6-8e2d-29bdd77949de",
+            "issued": "2023-04-21",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/w73y-7zz6",
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
+            "title": "Scorecard measure v2.11.16 (cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/64br-p84f",
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
-            "identifier": "https://data.cdc.gov/api/views/64br-p84f",
             "description": "Triclosan is an antimicrobial chemical used in healthcare settings that can be absorbed through the skin. Exposure to triclosan has been positively associated with food and aeroallergy and asthma exacerbation in humans and, although not directly sensitizing, has been demonstrated to augment the allergic response in a mouse model of asthma. The skin barrier and microbiome are thought to play important roles in mediating inflammation and allergy and disruptions may contribute to development of allergic disease. To investigate potential connections of the skin barrier and microbiome with immune responses to triclosan, SKH1 mice were dermally exposed to triclosan (0.5-2%) or vehicle for up to 7 consecutive days.",
-            "title": "Dermal exposure to the immunomodulatory antimicrobial chemical triclosan alters the skin barrier integrity and microbiome in mice",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145146,41 +145133,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/64br-p84f",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/64br-p84f",
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
+            "title": "Dermal exposure to the immunomodulatory antimicrobial chemical triclosan alters the skin barrier integrity and microbiome in mice"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-13",
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
-            "identifier": "https://data.cdc.gov/api/views/ku7p-zn4c",
             "description": "Monthly Cumulative Number and Percent of Children <20 Months Who Received Nirsevimab by Age Group and Jurisdiction\n\n\u2022 Estimated nirsevimab coverage for children 0-19 months is assessed through U.S. jurisdictions\u2019 Immunization Information Systems (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group. \n\n\u2022 Starting in July 2023, the CDC recommended the RSV vaccine to protect against serious illness from RSV. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)\n\u2003",
-            "title": "Monthly Cumulative Number and Percent of Children <20 Months Who Received Nirsevimab by Age Group and Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145203,46 +145185,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "identifier": "https://data.cdc.gov/api/views/ku7p-zn4c",
+            "issued": "2024-02-13",
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
+            "title": "Monthly Cumulative Number and Percent of Children <20 Months Who Received Nirsevimab by Age Group and Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK143764/",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/64f9-ag6i",
             "description": "An extensive collection of articles about NCBI databases, data models, and software.",
-            "title": "NCBI Handbook",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145251,46 +145232,41 @@
                     "title": "NCBI Handbook"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/64f9-ag6i",
+            "issued": "2022-03-01",
+            "keyword": [
+                "computational biology",
+                "education",
+                "reference",
+                "training and instruction"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK143764/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "theme": [
-                "Other"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/v2mh-3yzr",
-            "bureauCode": [
-                "009:00"
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:041"
             ],
-            "issued": "2020-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
-                "anthrax",
-                "arboviral diseases",
-                "chikungunya virus disease",
-                "eastern equine encephalitis virus disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "wonder"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "theme": [
+                "Other"
+            ],
+            "title": "NCBI Handbook"
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/v2mh-3yzr",
             "description": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145313,39 +145289,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/v2mh-3yzr",
+            "issued": "2020-01-17",
+            "keyword": [
+                "2020",
+                "anthrax",
+                "arboviral diseases",
+                "chikungunya virus disease",
+                "eastern equine encephalitis virus disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/v2mh-3yzr",
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
+            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/vecscreen/univec/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/gw7j-gxtx",
             "description": "UniVec and UniVec_Core databases in FASTA format.",
-            "title": "UniVec",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145360,40 +145343,40 @@
                     "title": "About UniVec Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/gw7j-gxtx",
+            "issued": "2022-03-02",
+            "keyword": [
+                "computational biology",
+                "dataset"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/vecscreen/univec/",
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
+            "title": "UniVec"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/w8hn-p5hf",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-07-20",
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
-            "identifier": "776a3880-a62d-5990-8b40-4406e6861dbb",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2017",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145401,46 +145384,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "776a3880-a62d-5990-8b40-4406e6861dbb",
+            "issued": "2017-07-20",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/w8hn-p5hf",
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
+            "title": "State Drug Utilization Data 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gp24-kfxi",
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
-            "identifier": "https://data.cdc.gov/api/views/gp24-kfxi",
             "description": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145463,49 +145440,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gp24-kfxi",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/gp24-kfxi",
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
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital"
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
-                "city",
-                "gis",
-                "outcomes",
-                "place",
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
-            "identifier": "https://data.cdc.gov/api/views/ndzg-9nmv",
             "description": "This dataset contains model-based place (incorporated and census designated places) level estimates for the PLACES project 2020 release in GIS-friendly format. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 27 measures at the place level. An ArcGIS Online feature service is also available at https://www.arcgis.com/home/item.html?id=8eca985039464f4d83467b8f6aeb1320 for users to make maps online or to add data to desktop GIS software.",
-            "title": "PLACES: Place Data (GIS Friendly Format), 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145528,35 +145501,49 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ndzg-9nmv",
+            "issued": "2021-09-29",
+            "keyword": [
+                "behaviors",
+                "city",
+                "gis",
+                "outcomes",
+                "place",
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
+            "title": "PLACES: Place Data (GIS Friendly Format), 2020 release"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -145579,91 +145566,79 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "https://data.cdc.gov/api/views/bst4-hnte",
+            "issued": "2023-11-20",
+            "landingPage": "https://data.cdc.gov/d/bst4-hnte",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-11-20",
+            "programCode": [
+                "009:030"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "title": "JMK_DHDS_POC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/w9p6-ixjq",
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
-            "identifier": "77bfc8f8-bd07-5ac2-895b-546636b7c458",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet pillar v2.10.64 (coreset-dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
-                    "description": "CoreSet pillar v2.10.64 (coreset-dev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet pillar v2.10.64 (coreset-dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet pillar v2.10.64 (coreset-dev)"
                 }
             ],
+            "identifier": "77bfc8f8-bd07-5ac2-895b-546636b7c458",
+            "issued": "2024-11-06",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/w9p6-ixjq",
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
+            "title": "CoreSet pillar v2.10.64 (coreset-dev)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -145686,42 +145661,50 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/d/wa3r-khqx",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-12-01",
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
-            "identifier": "d890d3a9-6b00-43fd-8b31-fcba4c8e2909",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2023",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145729,45 +145712,40 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "d890d3a9-6b00-43fd-8b31-fcba4c8e2909",
+            "issued": "2023-12-01",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/wa3r-khqx",
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
+            "title": "State Drug Utilization Data 2023"
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
@@ -145790,44 +145768,45 @@
                     "mediaType": "application/xml"
                 }
             ],
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
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-08-24",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Heart Disease & Stroke Prevention"
-            ]
+            ],
+            "title": "Rates and Trends in Heart Disease and Stroke Mortality Among US Adults (35+) by County, Age Group, Race/Ethnicity, and Sex \u2013 2000-2019"
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
-            "identifier": "https://data.cdc.gov/api/views/24w5-nppr",
+            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Su/24w5-nppr/revisions/0",
             "description": "Data were updated on September 11, 2024.\n\nART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Summary dataset provides a full snapshot of clinic services and profile, patient characteristics, and ART success rates. It is worth noting that patient medical characteristics, such as age, diagnosis, and ovarian reserve, affect ART treatment\u2019s success. Comparison of success rates across clinics may not be meaningful because of differences in patient populations and ART treatment methods. The success rates displayed in this dataset do not reflect any one patient\u2019s chance of success. Patients should consult with a doctor to understand their chance of success based on their own characteristics.",
-            "title": "2021 Final Assisted Reproductive Technology (ART) Summary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145850,42 +145829,46 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Su/24w5-nppr/revisions/0",
+            "identifier": "https://data.cdc.gov/api/views/24w5-nppr",
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
+            "title": "2021 Final Assisted Reproductive Technology (ART) Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/head-start-impact-study",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-06-18",
-            "temporal": "2002-01-01T00:00:00-05:00/2006-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "children's health",
-                "child well-being",
-                "head start"
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
-            "identifier": "989e4cbb-2319-4c3c-a61c-ce2fa009549b",
+            "dataQuality": true,
+            "describedBy": "http://www.researchconnections.org/childcare/studies/29462/documentation",
             "description": "<p>Nationally representative, longitudinal information from an evaluation where children were randomly assigned to Head Start or community services as usual;direct assessments and observations of children as well as parent and staff interviews were conducted</p>",
-            "title": "Head Start Impact Study",
-            "programCode": [
-                "009:092"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145894,43 +145877,39 @@
                     "title": "API "
                 }
             ],
-            "describedBy": "http://www.researchconnections.org/childcare/studies/29462/documentation",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "989e4cbb-2319-4c3c-a61c-ce2fa009549b",
+            "issued": "2013-06-18",
+            "keyword": [
+                "children's health",
+                "child well-being",
+                "head start"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/head-start-impact-study",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:092"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "temporal": "2002-01-01T00:00:00-05:00/2006-01-01T00:00:00-05:00",
+            "title": "Head Start Impact Study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/rsvvaxview/",
+            "accrualPeriodicity": "Monthly",
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
-            "identifier": "https://data.cdc.gov/api/views/vdz4-qrri",
             "description": "Infant Protection Against RSV by Maternal RSV Vaccination or Receipt of Nirsevimab and Intent for Nirsevimab Receipt, Reported by Females Aged 18-49 Years Who Have an Infant <8 Months During the RSV Season (born since April 1, 2024)\n\nMonthly estimates of infant protection against RSV by maternal RSV vaccination or receipt of nirsevimab, as well as intent for nirsevimab receipt, were calculated using data from the from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM). (https://www.cdc.gov/nis/about/index.html). Data were reported by adult females aged 18-49 years with infants under the age of 8 months during the RSV season (born since April 1, 2024). The NIS\u2013ACM is an ongoing random-digit-dial cellular telephone survey of households with adults 18 years and older. All estimates are based upon parent-reported receipt of nirsevimab.",
-            "title": "Infant Protection Against Respiratory Syncytial Virus (RSV) by Maternal RSV Vaccination or Receipt of Nirsevimab, and Intent for Nirsevimab Receipt, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -145953,56 +145932,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
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
+            "spatial": "United States- National, Region, State",
+            "temporal": "2024-2025",
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Infant Protection Against Respiratory Syncytial Virus (RSV) by Maternal RSV Vaccination or Receipt of Nirsevimab, and Intent for Nirsevimab Receipt, United States"
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
-            "temporal": "1988/2018",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-11",
-            "keyword": [
-                "black or african american",
-                "body mass index",
-                "body weight",
-                "children and adolescents",
-                "chronic conditions",
-                "health risk factors",
-                "health us",
-                "hispanic or latino",
-                "mexican",
-                "obesity",
-                "overweight",
-                "poverty",
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
-            "identifier": "https://data.cdc.gov/api/views/w9cp-q6sg",
             "description": "Data on obesity among children and adolescents aged 2-19 years in the United States, by selected characteristics, including sex, age, race, Hispanic origin, and poverty level. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Obesity among children and adolescents aged 2\u201319 years, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -146025,40 +145997,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/w9cp-q6sg",
+            "issued": "2024-02-21",
+            "keyword": [
+                "black or african american",
+                "body mass index",
+                "body weight",
+                "children and adolescents",
+                "chronic conditions",
+                "health risk factors",
+                "health us",
+                "hispanic or latino",
+                "mexican",
+                "obesity",
+                "overweight",
+                "poverty",
+                "white"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "1988/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Obesity among children and adolescents aged 2\u201319 years, by selected characteristics: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/idgn-d2g2",
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
-            "identifier": "https://data.cdc.gov/api/views/idgn-d2g2",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Tobacco Use Supplement to the Current Population Survey (TUS-CPS) Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -146066,41 +146049,40 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/idgn-d2g2",
+            "issued": "2015-02-05",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/idgn-d2g2",
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
+            "title": "Tobacco Use Supplement to the Current Population Survey (TUS-CPS) Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/wdvd-qg2g",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-14",
-            "keyword": [
-                "benefits and cost sharing",
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
-            "identifier": "958672e5-d4f3-464f-b75f-411000f1dafd",
             "description": "The Benefits and Cost Sharing PUF (BenCS-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BenCS-PUF contains plan variant-level data on essential health benefits, coverage limits, and cost sharing for each QHP and SADP.",
-            "title": "Benefits and Cost Sharing PUF - PY2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -146108,40 +146090,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "958672e5-d4f3-464f-b75f-411000f1dafd",
+            "issued": "2024-08-06",
+            "keyword": [
+                "benefits and cost sharing",
+                "exchange puf",
+                "marketplace puf",
+                "py2024"
+            ],
+            "landingPage": "https://healthdata.gov/d/wdvd-qg2g",
+            "modified": "2024-08-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Benefits and Cost Sharing PUF - PY2024"
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
-                "iis",
-                "iqvia",
-                "nis",
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
-            "identifier": "https://data.cdc.gov/api/views/nqu5-vn7d",
             "description": "\u2022 Weekly Cumulative RSV Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged 75 years\n\n\u2022 RSV vaccination coverage among Medicare-Fee-for-service beneficiaries aged 75 years and older and enrolled in a Part D plan in assessed using data files from the Medicare Fee-for-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS).",
-            "title": "Weekly Cumulative RSV Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226575 years and enrolled in a Part D plan, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -146164,55 +146144,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/nqu5-vn7d",
+            "issued": "2025-01-29",
+            "keyword": [
+                "iis",
+                "iqvia",
+                "nis",
+                "rsv vaccination",
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
+            "temporal": "2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative RSV Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226575 years and enrolled in a Part D plan, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-02-26",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
-            "keyword": [
-                "deaths",
-                "drug overdose",
-                "mortality",
-                "nchs",
-                "nowcasting",
-                "nvss",
-                "provisional",
-                "state",
-                "suicide",
-                "transport accidents",
-                "united states",
-                "vsrr",
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
-            "identifier": "https://data.cdc.gov/api/views/v2g4-wqg2",
             "description": "This dataset provides model-based provisional estimates of the weekly numbers of drug overdose, suicide, and transportation-related deaths using \u201cnowcasting\u201d methods to account for the normal lag between the occurrence and reporting of these deaths. Estimates less than 10 are suppressed. These early model-based provisional estimates were generated using a multi-stage hierarchical Bayesian modeling process to generate smoothed estimates of the weekly numbers of death, accounting for reporting lags. These estimates are based on several assumptions about how the reporting lags have changed in recent months across different jurisdictions, and the resulting estimates differ from other sources of provisional mortality data.  For now, these estimates should be considered highly uncertain until further evaluations can be done to determine the validity of these assumptions about timeliness. The true patterns in reporting lags will not be known until data are finalized, typically 11\u201312 months after the end of the calendar year. Importantly, these estimates are not a replacement for monthly provisional drug overdose death counts, or quarterly provisional mortality estimates. For more detail about the nowcasting methods and models, see:\n\nRossen LM, Hedegaard H, Warner M, Ahmad FB, Sutton PD. Early provisional estimates of drug overdose, suicide, and transportation-related deaths: Nowcasting methods to account for reporting lags. Vital Statistics Rapid Release; no 11. Hyattsville, MD: National Center for Health Statistics. February 2021. DOI: https://doi.org/10.15620/ cdc:101132",
-            "title": "Early Model-based Provisional Estimates of Drug Overdose, Suicide, and Transportation-related Deaths",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -146235,53 +146207,94 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/v2g4-wqg2",
+            "issued": "2021-02-26",
+            "keyword": [
+                "deaths",
+                "drug overdose",
+                "mortality",
+                "nchs",
+                "nowcasting",
+                "nvss",
+                "provisional",
+                "state",
+                "suicide",
+                "transport accidents",
+                "united states",
+                "vsrr",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
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
+            "title": "Early Model-based Provisional Estimates of Drug Overdose, Suicide, and Transportation-related Deaths"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://ccdb.ucsd.edu/home",
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
                 "fn": "DEATHERAGE, JAMES F.\u00a0",
                 "hasEmail": "mailto:deatherj@nigms.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "4368a9ec-2999-4c06-80c6-6e50d160a1b2",
+            "dataQuality": true,
             "description": "<p>The Cell Centered Database (CCDB) is a web accessible database for high resolution 2D, 3D and 4D data from light and electron microscopy, including correlated imaging.</p>",
-            "title": "Cell Centred Database (CCDB)",
+            "identifier": "4368a9ec-2999-4c06-80c6-6e50d160a1b2",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://ccdb.ucsd.edu/home",
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
+            "title": "Cell Centred Database (CCDB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1998",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1998) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1998-nid13615",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1998-nid13615"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1998-nid13615",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -146294,74 +146307,39 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1998",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1998-nid13615",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1998)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1998-nid13615",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1998) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1998-nid13615"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1998)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/home-health-agency-all-owners",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/fc009b2d-7846-44b1-b4a1-692f0c143879/data-viewer",
-            "description": "The Home Health Agency (HHA) All Owners dataset provides ownership information on all HHAs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
-            "title": "Home Health Agency All Owners",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/HHA_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Home Health Agency (HHA) All Owners dataset provides ownership information on all HHAs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fc009b2d-7846-44b1-b4a1-692f0c143879/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fc009b2d-7846-44b1-b4a1-692f0c143879/data",
+                    "mediaType": "text/html",
                     "title": "Home Health Agency All Owners : 2025-01-01"
                 },
                 {
@@ -146461,45 +146439,51 @@
                     "title": "Home Health Agency All Owners : 2023-04-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/HHA_All_Owners_Data_Dictionary.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/fc009b2d-7846-44b1-b4a1-692f0c143879/data-viewer",
+            "issued": "2023-04-20",
+            "keyword": [
+                "home health",
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/home-health-agency-all-owners",
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
+            "title": "Home Health Agency All Owners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/wh9n-d2tx",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-18",
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
-            "identifier": "dfa2ab14-06c2-457a-9e36-5cb6d80f8d93",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2022",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -146508,43 +146492,40 @@
                     "title": "NADAC (National Average Drug Acquisition Cost) 2022"
                 }
             ],
+            "identifier": "dfa2ab14-06c2-457a-9e36-5cb6d80f8d93",
+            "issued": "2022-01-05",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/wh9n-d2tx",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2023-01-18",
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
+            "title": "NADAC (National Average Drug Acquisition Cost) 2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/ipap-cksm",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ipap-cksm",
             "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Preferred Term Update Report lists changes to the Preferred Term of a Descriptor or a Supplementary Concept Record (SCR).  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
-            "title": "MeSH 2025 Update - Preferred Term Update Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -146567,21 +146548,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ipap-cksm",
+            "issued": "2023-12-14",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/ipap-cksm",
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
+            "title": "MeSH 2025 Update - Preferred Term Update Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.hcup-us.ahrq.gov/db/state/sasddbdocumentation.jsp",
             "bureauCode": [
                 "009:33"
             ],
-            "rights": "N/A",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HCUP Technical Support",
+                "hasEmail": "mailto:hcup@ahrq.gov"
+            },
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/state/sasddbdocumentation.jsp",
+            "description": "The Healthcare Cost and Utilization Project (HCUP) State Ambulatory Surgery Databases (SASD) contain the universe of hospital-based ambulatory surgery encounters in participating States.  The SASD include encounter-level data for ambulatory surgeries and may also include various types of outpatient services such as observation stays, lithotripsy, radiation therapy, imaging, chemotherapy, and labor and delivery. The specific types of ambulatory surgery and outpatient services included in each SASD vary by State and data year. All SASD include data from hospital-owned ambulatory surgery facilities. In addition, some States include data from nonhospital-owned facilities. The data are translated into a uniform format to facilitate multi-State comparisons and analyses. The SASD include all patients in participating settings, regardless of the expected payer including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality (AHRQ), HCUP data inform decision making at the national, State, and community levels.\n\nThe SASD contain clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and facilities (as required by data sources). Data elements include but are not limited to: diagnoses, procedures, admission and discharge status, patient demographics (e.g., gender, age), total charges, and expected payment source. In addition to the core set of uniform data elements common to all SASD, some include State-specific data elements. The SASD exclude data elements that could directly or indirectly identify individuals. For some States, hospital and county identifiers are included that permit linkage to the American Hospital Association Annual Survey File and the Bureau of Health Professions' Area Resource File except in States that do not allow the release of hospital identifiers.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
+            "identifier": "eabeb3a6-d2d7-43be-b43d-f83414eb7ee1",
             "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "ambulatory surgery",
                 "claims",
@@ -146596,112 +146600,89 @@
                 "procedures",
                 "utilization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HCUP Technical Support",
-                "hasEmail": "mailto:hcup@ahrq.gov"
-            },
+            "landingPage": "https://www.hcup-us.ahrq.gov/db/state/sasddbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
             },
-            "identifier": "eabeb3a6-d2d7-43be-b43d-f83414eb7ee1",
-            "description": "The Healthcare Cost and Utilization Project (HCUP) State Ambulatory Surgery Databases (SASD) contain the universe of hospital-based ambulatory surgery encounters in participating States.  The SASD include encounter-level data for ambulatory surgeries and may also include various types of outpatient services such as observation stays, lithotripsy, radiation therapy, imaging, chemotherapy, and labor and delivery. The specific types of ambulatory surgery and outpatient services included in each SASD vary by State and data year. All SASD include data from hospital-owned ambulatory surgery facilities. In addition, some States include data from nonhospital-owned facilities. The data are translated into a uniform format to facilitate multi-State comparisons and analyses. The SASD include all patients in participating settings, regardless of the expected payer including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality (AHRQ), HCUP data inform decision making at the national, State, and community levels.\n\nThe SASD contain clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and facilities (as required by data sources). Data elements include but are not limited to: diagnoses, procedures, admission and discharge status, patient demographics (e.g., gender, age), total charges, and expected payment source. In addition to the core set of uniform data elements common to all SASD, some include State-specific data elements. The SASD exclude data elements that could directly or indirectly identify individuals. For some States, hospital and county identifiers are included that permit linkage to the American Hospital Association Annual Survey File and the Bureau of Health Professions' Area Resource File except in States that do not allow the release of hospital identifiers.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
-            "title": "HCUP State Ambulatory Surgery Databases (SASD) - Restricted Access Files",
-            "programCode": [
-                "009:072"
-            ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/db/state/sasddbdocumentation.jsp",
-            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "rights": "N/A",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "HCUP State Ambulatory Surgery Databases (SASD) - Restricted Access Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/wjrc-wdfw",
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
-            "identifier": "ce69c011-1dc5-5ffa-94fb-d3e9b05afc4b",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard measure_value v2.11.9 (prod)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure_value.csv",
-                    "description": "Scorecard measure_value v2.11.9 (prod)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard measure_value v2.11.9 (prod)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard measure_value v2.11.9 (prod)"
                 }
             ],
+            "identifier": "ce69c011-1dc5-5ffa-94fb-d3e9b05afc4b",
+            "issued": "2023-07-22",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/wjrc-wdfw",
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
+            "title": "Scorecard measure_value v2.11.9 (prod)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/medicare-fee-for-service-public-provider-enrollment",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2023-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/resources/fee-for-service-public-provider-enrollment-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/2457ea29-fc82-48b0-86ec-3b0755de7515/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-fee-for-service-public-provider-enrollment-data-dictionary",
             "description": "The Medicare Fee-For-Service Public Provider Enrollment dataset includes information on providers who are actively approved to bill Medicare or have completed the 855O at the time the data was pulled from the Provider Enrollment, Chain, and Ownership System (PECOS). The release of this provider enrollment data is not related to other provider information releases such as Physician Compare or Data Transparency.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Medicare Fee-For-Service  Public Provider Enrollment",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2457ea29-fc82-48b0-86ec-3b0755de7515/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2457ea29-fc82-48b0-86ec-3b0755de7515/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-12-31"
                 },
                 {
@@ -146801,26 +146782,58 @@
                     "title": "Medicare Fee-For-Service Public Provider Enrollment : 2023-03-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-fee-for-service-public-provider-enrollment-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/2457ea29-fc82-48b0-86ec-3b0755de7515/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/medicare-fee-for-service-public-provider-enrollment",
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
+                "https://data.cms.gov/resources/fee-for-service-public-provider-enrollment-methodology"
+            ],
+            "temporal": "2023-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Fee-For-Service  Public Provider Enrollment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2007",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) primarily<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions included age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2007 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Background information<br />\nincludes gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2007) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2007-nid13532",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2007-nid13532"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2007-nid13532",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -146861,45 +146874,41 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2007",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2007-nid13532",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) primarily<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions included age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2007 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Background information<br />\nincludes gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Survey on Drug Use and Health (NSDUH-2007)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2007-nid13532",
-                    "description": "National Survey on Drug Use and Health (NSDUH-2007) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2007-nid13532"
-                }
-            ]
+            "title": "National Survey on Drug Use and Health (NSDUH-2007)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/doc2016_clas.pdf",
+            "accrualPeriodicity": "Survey will not be updated.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/",
-            "issued": "2018-11-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2016",
-            "modified": "2023-09-27",
-            "references": [
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/readme2016_clas.txt"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov "
+            },
+            "describedBy": "https://www.cdc.gov/nchs/data/ahcd/2016_NAMCS_CLAS_Sample_Card.pdf",
+            "describedByType": "application/pdf",
+            "description": "The purpose of the National CLAS Physician Survey was to understand the provision of culturally and linguistically appropriate services among office-based physicians. The National CLAS Physician Survey was a supplement to the National Ambulatory Medical Care Survey (NAMCS), which is a national probability sample survey of visits to office-based physicians. NAMCS is a component of the National Health Care Surveys that measured health care utilization across a variety of health care providers\u2019 settings. NAMCS and the National CLAS Physician Survey were conducted by the National Center for Health Statistics (NCHS). The National CLAS Physician Survey public use file includes data from office-based physicians. No patient level data were collected. This documentation describes the public use micro-data file produced from data collected in the National CLAS Physician Survey.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/jy4b-8v6u/text/plain",
+                    "mediaType": "text/plain"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jy4b-8v6u",
+            "issued": "2018-11-20",
             "keyword": [
                 "cultural-health-beliefs",
                 "health-practices",
@@ -146908,65 +146917,40 @@
                 "physicians",
                 "preferred-languages"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov "
-            },
+            "landingPage": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/doc2016_clas.pdf",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/jy4b-8v6u",
-            "description": "The purpose of the National CLAS Physician Survey was to understand the provision of culturally and linguistically appropriate services among office-based physicians. The National CLAS Physician Survey was a supplement to the National Ambulatory Medical Care Survey (NAMCS), which is a national probability sample survey of visits to office-based physicians. NAMCS is a component of the National Health Care Surveys that measured health care utilization across a variety of health care providers\u2019 settings. NAMCS and the National CLAS Physician Survey were conducted by the National Center for Health Statistics (NCHS). The National CLAS Physician Survey public use file includes data from office-based physicians. No patient level data were collected. This documentation describes the public use micro-data file produced from data collected in the National CLAS Physician Survey.",
-            "title": "National Ambulatory Medical Care Survey: Culturally and Linguistically Appropriate Services Supplement, 2016",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/jy4b-8v6u/text/plain",
-                    "mediaType": "text/plain"
-                }
+            "references": [
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/readme2016_clas.txt"
             ],
+            "rights": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/",
             "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data/ahcd/2016_NAMCS_CLAS_Sample_Card.pdf",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Survey will not be updated.",
+            "temporal": "2016",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey: Culturally and Linguistically Appropriate Services Supplement, 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/k62p-6esq",
+            "accrualPeriodicity": "Annually",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dhds",
-                "disability"
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
-            "identifier": "https://data.cdc.gov/api/views/k62p-6esq",
             "description": "Disability and Health Data System (DHDS) is an online source of state-level data on adults with disabilities. Users can access information on six functional disability types: cognitive (serious difficulty concentrating, remembering or making decisions), hearing (serious difficulty hearing or deaf), mobility (serious difficulty walking or climbing stairs), vision (serious difficulty seeing), self-care (difficulty dressing or bathing) and independent living (difficulty doing errands alone).",
-            "title": "Disability and Health Data System (DHDS)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -146989,40 +146973,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/k62p-6esq",
+            "issued": "2021-05-04",
+            "keyword": [
+                "dhds",
+                "disability"
+            ],
+            "landingPage": "https://data.cdc.gov/d/k62p-6esq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Annually",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Disability & Health"
-            ]
+            ],
+            "title": "Disability and Health Data System (DHDS)"
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
-                "infectious disease"
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
-            "identifier": "https://data.cdc.gov/api/views/pqn7-e45s",
             "description": "These data represent prevalence estimates of select infectious diseases from the National Health and Nutrition Examination Survey (NHANES).",
-            "title": "NHANES Select Infectious Diseases Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -147045,48 +147029,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/pqn7-e45s",
+            "issued": "2023-03-02",
+            "keyword": [
+                "infectious disease"
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
+            "title": "NHANES Select Infectious Diseases Prevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/brfss/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-06",
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
-            "identifier": "https://data.cdc.gov/api/views/y4ft-s73h",
             "description": "1995-2010. BRFSS land line only prevalence data. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct/data",
-            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Prevalence Data (2010 and prior)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -147109,48 +147088,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/y4ft-s73h",
+            "issued": "2023-07-19",
+            "keyword": [
+                "...",
+                "behavioral",
+                "brfss",
+                "factor",
+                "risk",
+                "survey"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2023-09-06",
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
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Prevalence Data (2010 and prior)"
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
-                "500 cities",
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
@@ -147173,50 +147148,57 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2016-relea/9z78-nsfp",
+            "identifier": "https://data.cdc.gov/api/views/9z78-nsfp",
+            "issued": "2023-07-18",
+            "keyword": [
+                "500 cities",
+                "census",
+                "estimates",
+                "prevalence",
+                "tracts"
+            ],
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-            "landingPage": "https://data.cms.gov/provider-compliance/public-reporting-of-missing-digital-contact-information",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2023-01-01/2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-25",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2021-12/8eb2b4bf-6e5f-4e05-bcdb-39c07ad8f77a/Missing_Digital_Contact_Info_Methods%20.pdf"
-            ],
-            "keyword": [
-                "medicare",
-                "provider enrollment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CMS Health Informatics and Interoperability Group - CPI",
                 "hasEmail": "mailto:CMSInteroperability@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/63a83bb1-4c02-43b3-8ef4-e3d3c6cf62fa/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/public-reporting-of-missing-digital-contact-information-data-dictionary",
             "description": "In the May 2020 CMS Interoperability and Patient Access final rule, CMS finalized the policy to publicly report the names and NPIs of those providers who do not have digital contact information included in the NPPES system (85 FR 25584). This data includes the NPI and provider name of providers and clinicians without digital contact information in NPPES.",
-            "title": "Public Reporting of Missing Digital Contact Information",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/63a83bb1-4c02-43b3-8ef4-e3d3c6cf62fa/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/63a83bb1-4c02-43b3-8ef4-e3d3c6cf62fa/data",
+                    "mediaType": "text/html",
                     "title": "Public Reporting of Missing Digital Contact Information : 2024-09-01"
                 },
                 {
@@ -147292,46 +147274,47 @@
                     "title": "Public Reporting of Missing Digital Contact Information : 2023-03-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/public-reporting-of-missing-digital-contact-information-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/63a83bb1-4c02-43b3-8ef4-e3d3c6cf62fa/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-compliance/public-reporting-of-missing-digital-contact-information",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-10-25",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2021-12/8eb2b4bf-6e5f-4e05-bcdb-39c07ad8f77a/Missing_Digital_Contact_Info_Methods%20.pdf"
+            ],
+            "temporal": "2023-01-01/2024-09-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Public Reporting of Missing Digital Contact Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/wrj4-twjv",
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
-            "identifier": "acbd1537-69b8-548d-a90f-eedb416acd71",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 1992",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -147339,51 +147322,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "acbd1537-69b8-548d-a90f-eedb416acd71",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/wrj4-twjv",
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
+            "title": "State Drug Utilization Data 1992"
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
-            "temporal": "1940/2015",
-            "modified": "2022-03-29",
-            "references": [
-                "http://www.cdc.gov/nchs/data/databriefs/db162.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
-                "http://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf",
-                "http://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm"
-            ],
-            "keyword": [
-                "births",
-                "nchs",
-                "nonmarital",
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
-            "identifier": "https://data.cdc.gov/api/views/g6qk-ngsf",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes number of births to unmarried women by age group in the United States since 1940. \n\nMethods for collecting information on marital status changed over the reporting period and have been documented in:\n\n\u2022 Ventura SJ, Bachrach CA. Nonmarital childbearing in the United States, 1940\u201399. National vital statistics reports; vol 48 no 16. Hyattsville, Maryland: National Center for Health Statistics. 2000. Available from: http://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf.\n\u2022 National Center for Health Statistics. User guide to the 2013 natality public use file. Hyattsville, Maryland: National Center for Health Statistics. 2014. Available from: http://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm.",
-            "title": "NCHS - Births to Unmarried Women by Age Group: United States",
-            "isPartOf": "NCHS - Births to Unmarried Women by Age Group: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -147406,60 +147379,64 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/g6qk-ngsf",
+            "isPartOf": "NCHS - Births to Unmarried Women by Age Group: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "births",
+                "nchs",
+                "nonmarital",
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
+                "http://www.cdc.gov/nchs/data/databriefs/db162.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "http://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf",
+                "http://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm"
+            ],
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1940/2015",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Births to Unmarried Women by Age Group: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-internet-quality-improvement-and-evaluation-system-home-health-agency-ambulatory-surgical-center-and-hospice-providers",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-02-28",
-            "temporal": "2023-10-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
-            "references": [
-                "https://data.cms.gov/resources/pos-file-iqies-for-hha-asc-and-hospice-providers-methodology"
-            ],
-            "keyword": [
-                "home health",
-                "hospice",
-                "hospitals & facilities",
-                "medicare",
-                "medicare advantage",
-                "original medicare",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/086e48c4-87a6-4be1-8823-29e8da8f225b/data-viewer",
-            "description": "The Provider of Services File (POS) - Internet Quality Improvement and Evaluation System (iQIES) - Home Health Agency (HHA), Ambulatory Surgical Center (ASC), and Hospice Providers data\u00a0provides information on provider demographic and associated certification information. In this file you will find provider number (CMS Certification Number), name, address, and other characteristics of the participating institution providers.",
-            "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2025-01/47cff7a0-5575-4a62-be85-ae72dcedf677/iQIES%20POS%20Data%20Dictionary.zip",
             "describedByType": "application/zip",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Provider of Services File (POS) - Internet Quality Improvement and Evaluation System (iQIES) - Home Health Agency (HHA), Ambulatory Surgical Center (ASC), and Hospice Providers data\u00a0provides information on provider demographic and associated certification information. In this file you will find provider number (CMS Certification Number), name, address, and other characteristics of the participating institution providers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/086e48c4-87a6-4be1-8823-29e8da8f225b/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/086e48c4-87a6-4be1-8823-29e8da8f225b/data",
+                    "mediaType": "text/html",
                     "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-12-02"
                 },
                 {
@@ -147523,47 +147500,52 @@
                     "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2023-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2025-01/47cff7a0-5575-4a62-be85-ae72dcedf677/iQIES%20POS%20Data%20Dictionary.zip",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/086e48c4-87a6-4be1-8823-29e8da8f225b/data-viewer",
+            "issued": "2024-02-28",
+            "keyword": [
+                "home health",
+                "hospice",
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-internet-quality-improvement-and-evaluation-system-home-health-agency-ambulatory-surgical-center-and-hospice-providers",
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
+                "https://data.cms.gov/resources/pos-file-iqies-for-hha-asc-and-hospice-providers-methodology"
+            ],
+            "temporal": "2023-10-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/wsfv-b883",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-18",
-            "keyword": [
-                "business rules",
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
-            "identifier": "d849f3cc-64da-408a-92d8-790ba4973737",
             "description": "The Business Rules PUF (BR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BR-PUF contains plan-level data on rating business rules, such as maximum age for a dependent and allowed dependent relationships.",
-            "title": "Business Rules PUF - PY2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -147571,48 +147553,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "d849f3cc-64da-408a-92d8-790ba4973737",
+            "issued": "2024-12-10",
+            "keyword": [
+                "business rules",
+                "exchange puf",
+                "marketplace puf",
+                "py2025"
+            ],
+            "landingPage": "https://healthdata.gov/d/wsfv-b883",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "Business Rules PUF - PY2025"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -147635,26 +147607,66 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/dataset/cdc-child-growth-charts",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>CDC child growth charts consist of a series of percentile curves that illustrate the distribution of selected body measurements in U.S. children. Pediatric growth charts have been used by pediatricians, nurses, and parents to track the growth of infants, children, and adolescents in the United States since 1977.   Growth charts are not intended to be used as a sole diagnostic instrument. Instead, growth charts are tools that contribute to forming an overall clinical impression for the child being measured.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/growthcharts/",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "d161b0bc-177d-4dd8-85aa-8fcf912a49f4",
             "issued": "2012-05-30",
-            "temporal": "1965-01-01T00:00:00-05:00/2000-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "age",
                 "babies",
@@ -147673,107 +147685,82 @@
                 "weight",
                 "z-scores"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-child-growth-charts",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:029"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "d161b0bc-177d-4dd8-85aa-8fcf912a49f4",
-            "description": "<p>CDC child growth charts consist of a series of percentile curves that illustrate the distribution of selected body measurements in U.S. children. Pediatric growth charts have been used by pediatricians, nurses, and parents to track the growth of infants, children, and adolescents in the United States since 1977.   Growth charts are not intended to be used as a sole diagnostic instrument. Instead, growth charts are tools that contribute to forming an overall clinical impression for the child being measured.</p>",
-            "title": "CDC Child Growth Charts",
-            "programCode": [
-                "009:029"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cdc.gov/growthcharts/",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1965-01-01T00:00:00-05:00/2000-12-31T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health"
-            ]
+            ],
+            "title": "CDC Child Growth Charts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/wtr7-pvy6",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-05",
-            "keyword": [
-                "chip",
-                "dental",
-                "dq atlas",
-                "medicaid",
-                "service use",
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
-            "identifier": "2aa0ed3d-6ef8-47a8-90b0-06b6d2fa3953",
             "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of dental services provided to Medicaid and CHIP beneficiaries under the age of 19 (as of the first day of the month), by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating dental services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Dental Services Provided to Medicaid and CHIP Beneficiaries Under Age 19",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Dental-Services-Provided-to-MedicaidCHIP-Beneficiaries-Under-Age-19.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of dental services provided to Medicaid and CHIP beneficiaries under the age of 19 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating dental services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of dental services provided to Medicaid and CHIP beneficiaries under the age of 19 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating dental services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Dental-Services-Provided-to-MedicaidCHIP-Beneficiaries-Under-Age-19.csv",
+                    "mediaType": "text/csv",
                     "title": "Dental Services Provided to Medicaid and CHIP Beneficiaries Under Age 19"
                 }
             ],
+            "identifier": "2aa0ed3d-6ef8-47a8-90b0-06b6d2fa3953",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dental",
+                "dq atlas",
+                "medicaid",
+                "service use",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/wtr7-pvy6",
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
+            "title": "Dental Services Provided to Medicaid and CHIP Beneficiaries Under Age 19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kkvj-587h",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-27",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Allergy and Clinical Immunology Branch (ACIB), Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/kkvj-587h",
             "description": "Diesel exhaust (DE) is an air pollutant containing gaseous compounds and particulate matter.  Diesel engines are common on gas extraction and oil sites, leading to complex DE exposure to a broad range of compounds through occupational settings.  The US EPA concluded that short-term exposure to DE leads to allergic inflammatory disorders of the airways.  To further evaluate the immunotoxicity of DE, the effects of whole-body inhalation of 0.2 and 1 mg/m3 DE (total carbon; 6 h/d for 4 days) were investigated 1-, 7-, and 27-days post exposure in Sprague-Dawley rats using an occupationally relevant exposure system.  DE exposure of 1 mg/m3 increased total cellularity, number of CD4+ and CD8+ T-cells, and B-cells at 1 d post-exposure in the lung lymph nodes.  At 7 d post-exposure to 1 mg/m3, cellularity and the number of CD4+ and CD8+ T-cells decreased in the LLNs.  In the bronchoalveolar lavage, B-cell number and frequency increased at 1 d post-exposure, Natural Killer cell number and frequency decreased at 7 d post-exposure, and at 27 d post-exposure CD8+ T-cell and CD11b+ cell number and frequency decreased with 0.2 mg/m3 exposure.  In the spleen, 0.2 mg/m3 increased CD4+ T-cell frequency at 1 and 7 d post-exposure and at 27 d post-exposure increased CD4+ and CD8+ T-cell number and CD8+ T-cell frequency.  B-cells were the only immune cell subset altered in the three tissues (spleen, LLNs, and BALF), suggesting the induction of the adaptive immune response.  The increase in lymphocytes in several different organ types also suggests an induction of a systemic inflammatory response occurring following DE exposure.  These results show that DE exposure induced modifications of cellularity of phenotypic subsets that may impair immune function and contribute to airway inflammation induced by DE exposure in rats.",
-            "title": "Effects of inhaled tier-2 diesel engine exhaust on immunotoxicity in a rat model:  A hazard identification study. Part III. Immunotoxicology",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -147781,46 +147768,37 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kkvj-587h",
+            "issued": "2024-12-27",
+            "landingPage": "https://data.cdc.gov/d/kkvj-587h",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-27",
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
+            "title": "Effects of inhaled tier-2 diesel engine exhaust on immunotoxicity in a rat model:  A hazard identification study. Part III. Immunotoxicology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/53mp-bpbv",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2019",
-            "modified": "2023-04-20",
-            "keyword": [
-                "chronic conditions",
-                "disability",
-                "e-cigarette use",
-                "opioid use",
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
-            "identifier": "https://data.cdc.gov/api/views/53mp-bpbv",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 3 was administered by the National Opinion Research Center (NORC) using the \nAmerispeak Panel in the spring of 2019 and contains existing questions from \nthe National Health Interview Survey (NHIS) as well as embedded probe questions \nand split-panel experiments for cognitive evaluations.",
-            "title": "NCHS Research and Development Survey (RANDS) Round 3 Restricted File",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS3_technical_documentation.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 3 was administered by the National Opinion Research Center (NORC) using the \nAmerispeak Panel in the spring of 2019 and contains existing questions from \nthe National Health Interview Survey (NHIS) as well as embedded probe questions \nand split-panel experiments for cognitive evaluations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -147828,90 +147806,92 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS3_technical_documentation.pdf",
+            "identifier": "https://data.cdc.gov/api/views/53mp-bpbv",
+            "issued": "2022-06-15",
+            "keyword": [
+                "chronic conditions",
+                "disability",
+                "e-cigarette use",
+                "opioid use",
+                "physical activity",
+                "research-data-center"
+            ],
+            "landingPage": "https://data.cdc.gov/d/53mp-bpbv",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-20",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 3 Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/wunw-h7a2",
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
-            "identifier": "08b59dc2-a89b-512a-bab9-e8f83e4b7848",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard filters v2.11.16 (cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/filters.csv",
-                    "description": "Scorecard filters v2.11.16 (cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard filters v2.11.16 (cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard filters v2.11.16 (cmsdev)"
                 }
             ],
+            "identifier": "08b59dc2-a89b-512a-bab9-e8f83e4b7848",
+            "issued": "2023-04-21",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/wunw-h7a2",
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
+            "title": "Scorecard filters v2.11.16 (cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qjxm-7fny",
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
-            "identifier": "https://data.cdc.gov/api/views/qjxm-7fny",
             "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2011-2015. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2011-2015",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -147934,53 +147914,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qjxm-7fny",
+            "issued": "2020-05-28",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "particulate matter",
+                "pm2.5"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qjxm-7fny",
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
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2011-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-providers",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/e0eba16f-ce0d-4037-96ce-2af70c718c98/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-reach-provider-data-dictionary",
             "description": "The Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Providers Public Use File (PUF) data details Participant Providers and Preferred Providers in the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model. This dataset includes information on each providers capitation arrangement, Advanced Payment Option and elected waivers.",
-            "title": "ACO Realizing Equity, Access and Community Health Providers",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e0eba16f-ce0d-4037-96ce-2af70c718c98/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e0eba16f-ce0d-4037-96ce-2af70c718c98/data",
+                    "mediaType": "text/html",
                     "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31"
                 },
                 {
@@ -147996,56 +147974,59 @@
                     "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/aco-reach-provider-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/e0eba16f-ce0d-4037-96ce-2af70c718c98/data-viewer",
+            "issued": "2023-05-26",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-providers",
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
+            "title": "ACO Realizing Equity, Access and Community Health Providers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/facility-level-minimum-data-set-frequency",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-08-01",
-            "temporal": "2023-10-01/2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "references": [
-                "https://data.cms.gov/resources/facility-level-minimum-data-set-frequency-methodology"
-            ],
-            "keyword": [
-                "hospitals & facilities",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/facility-level-minimum-data-set-frequency-data-dictionary",
             "description": "The Facility-Level Minimum Data Set (MDS) Frequency\u00a0dataset provides information for active nursing home residents on topics, such as race/ethnicity, age, or marital status; discharge dispositions; hearing, speech, and vision; cognitive patterns; mood; functional abilities and goals; bladder and bowel; active diagnoses; health conditions; swallowing/nutritional status; oral/dental status; skin conditions; medications; special treatments, procedures, and programs; restraints and alarms; and participation in assessment and goal setting.\n\n\u00a0\n\nNote: The MDS dataset contains more records than most spreadsheet programs can handle. The use of a database or statistical software is generally required. The dataset can be filtered to a more manageable size for use in a spreadsheet program by clicking on the \u201cView Data\u201d button. Additional filter information can be found in the methodology, if needed.",
-            "title": "Facility-Level Minimum Data Set Frequency",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data",
+                    "mediaType": "text/html",
                     "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01"
                 },
                 {
@@ -148097,46 +148078,48 @@
                     "title": "Facility-Level Minimum Data Set Frequency : 2023-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/facility-level-minimum-data-set-frequency-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data-viewer",
+            "issued": "2024-08-01",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "skilled nursing"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/facility-level-minimum-data-set-frequency",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-11-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/facility-level-minimum-data-set-frequency-methodology"
+            ],
+            "temporal": "2023-10-01/2024-09-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Facility-Level Minimum Data Set Frequency"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/wxsh-768y",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2014-11-07",
-            "temporal": "2019-01-01T00:00:00+00:00/2020-01-01T00:00:00+00:00",
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
-            "identifier": "76a1984a-6d69-5e4d-86c8-65eb31f0506d",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2019",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148145,47 +148128,41 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "76a1984a-6d69-5e4d-86c8-65eb31f0506d",
+            "issued": "2014-11-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/wxsh-768y",
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
+            "temporal": "2019-01-01T00:00:00+00:00/2020-01-01T00:00:00+00:00",
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ex65-qa8z",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/ex65-qa8z",
             "description": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148208,43 +148185,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ex65-qa8z",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "hemolytic uremic syndrome post-diarrheal",
+                "hepatitis (viral acute) type a",
+                "hepatitis (viral acute) type b",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ex65-qa8z",
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
+            "title": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute"
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
-            "modified": "2025-01-14",
-            "keyword": [
-                "ecigarette",
-                "legislation",
-                "osh",
-                "policy",
-                "smokefree indoor air",
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
-            "identifier": "https://data.cdc.gov/api/views/i8t6-whzd",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Ind/2snk-eav4",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. E-Cigarette Legislation \u2013 Smokefree Indoor Air. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to state legislation on smokefree indoor air that apply to use of e-cigarettes in private worksites, restaurants, and bars.",
-            "title": "CDC STATE System E-Cigarette Legislation - Smokefree Indoor Air Summary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148267,36 +148247,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Ind/2snk-eav4",
+            "identifier": "https://data.cdc.gov/api/views/i8t6-whzd",
+            "issued": "2023-07-19",
+            "keyword": [
+                "ecigarette",
+                "legislation",
+                "osh",
+                "policy",
+                "smokefree indoor air",
+                "state system"
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
+            "title": "CDC STATE System E-Cigarette Legislation - Smokefree Indoor Air Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xy5u-nzbq",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-12-03",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-03",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division (HELD)",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/xy5u-nzbq",
             "description": "Workers that regularly use vibrating hand tools as part of their job are at risk of developing hand-arm vibration syndrome (HAVS).  HAVS is characterized by cold-induced vasospasms that result in blanching of the fingers and hands, loss of sensation, pain, and reductions in manual dexterity, all of which can affect a worker\u2019s ability to perform their job and their quality of life.  Vibration exposure significantly contributes to the development of these symptoms by increasing the stress and strain within exposed tissues, which in turn can affect functioning of blood vessels, nerves and sensory receptors in those tissues.",
-            "title": "Applied pressure alters circulating hormone levels and biomarkers of peripheral vascular, sensorineural dysfunction",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148304,66 +148291,92 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xy5u-nzbq",
+            "issued": "2024-12-03",
+            "landingPage": "https://data.cdc.gov/d/xy5u-nzbq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-03",
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
+            "title": "Applied pressure alters circulating hormone levels and biomarkers of peripheral vascular, sensorineural dysfunction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/wyqi-qmra",
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
-            "identifier": "076d0bf4-50f5-52f4-b142-f49d558e1bcd",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard filters v2.11.9 (impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/filters.csv",
-                    "description": "Scorecard filters v2.11.9 (impl)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard filters v2.11.9 (impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/filters.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard filters v2.11.9 (impl)"
                 }
             ],
+            "identifier": "076d0bf4-50f5-52f4-b142-f49d558e1bcd",
+            "issued": "2023-06-29",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/wyqi-qmra",
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
+            "title": "Scorecard filters v2.11.9 (impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1999",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. Respondents are also asked about personal and family income<br />\nsources and amounts, health care access and coverage, illegal<br />\nactivities and arrest record, problems resulting from the use of<br />\ndrugs, and needle-sharing. Questions introduced in previous NHSDA<br />\nadministrations were retained in the 1999 survey, including questions<br />\nasked only of respondents aged 12 to 17. These \"youth experiences\"<br />\nitems covered a variety of topics, such as neighborhood environment,<br />\nillegal activities, gang involvement, drug use by friends, social<br />\nsupport, extracurricular activities, exposure to substance abuse<br />\nprevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Also retained were<br />\nquestions on mental health and access to care, perceived risk of using<br />\ndrugs, perceived availability of drugs, driving behavior and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Demographic data include<br />\ngender, race, age, ethnicity, marital status, educational level, job<br />\nstatus, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1999) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1999-nid13544",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1999-nid13544"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1999-nid13544",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -148387,61 +148400,29 @@
                 "substance abuse treatment",
                 "tranquilizers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1999",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1999-nid13544",
-            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. Respondents are also asked about personal and family income<br />\nsources and amounts, health care access and coverage, illegal<br />\nactivities and arrest record, problems resulting from the use of<br />\ndrugs, and needle-sharing. Questions introduced in previous NHSDA<br />\nadministrations were retained in the 1999 survey, including questions<br />\nasked only of respondents aged 12 to 17. These \"youth experiences\"<br />\nitems covered a variety of topics, such as neighborhood environment,<br />\nillegal activities, gang involvement, drug use by friends, social<br />\nsupport, extracurricular activities, exposure to substance abuse<br />\nprevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Also retained were<br />\nquestions on mental health and access to care, perceived risk of using<br />\ndrugs, perceived availability of drugs, driving behavior and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Demographic data include<br />\ngender, race, age, ethnicity, marital status, educational level, job<br />\nstatus, veteran status, and current household composition.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1999)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1999-nid13544",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1999) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1999-nid13544"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1999)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/epap-ayij",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-16",
-            "keyword": [
-                "care cascade",
-                "cascade of care",
-                "latent tuberculosis infection (ltbi)",
-                "tuberculosis (tb)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tuberculosis Epidemiologic Studies Consortium",
                 "hasEmail": "mailto:tbesc3@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/epap-ayij",
             "description": "This study focused on describing and quantifying the steps in the tuberculosis (TB) prevention cascade of care within health department clinics. This included better understanding the proportions of patients with latent TB infection who are identified, offered treatment, accept treatment, and complete treatment.",
-            "title": "Tuberculosis Epidemiologic Studies Consortium (TBESC)-II Part B: Strengthening Public Health Surveillance for Latent Tuberculosis Infection",
-            "programCode": [
-                "009:027"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148449,58 +148430,45 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/epap-ayij",
+            "issued": "2024-10-16",
+            "keyword": [
+                "care cascade",
+                "cascade of care",
+                "latent tuberculosis infection (ltbi)",
+                "tuberculosis (tb)"
+            ],
+            "landingPage": "https://data.cdc.gov/d/epap-ayij",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-16",
+            "programCode": [
+                "009:027"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "National Center for HIV",
                 "Viral Hepatitis",
                 "STD",
                 "and TB Prevention"
-            ]
+            ],
+            "title": "Tuberculosis Epidemiologic Studies Consortium (TBESC)-II Part B: Strengthening Public Health Surveillance for Latent Tuberculosis Infection"
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
-            "modified": "2022-03-29",
-            "references": [
-                "https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf",
-                "https://www.cdc.gov/nchs/data/misc/usvss.pdf",
-                "https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
-                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
-                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
-            ],
-            "keyword": [
-                "age",
-                "birth rate",
-                "ethnicity",
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
-            "identifier": "https://data.cdc.gov/api/views/e8kx-wbww",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes teen birth rates for females by age group, race, and Hispanic origin in the United States since 1960. \n\nData availability varies by race and ethnicity groups. All birth data by race before 1980 are based on race of the child. Since 1980, birth data by race are based on race of the mother. For race, data are available for Black and White births since 1960, and for American Indians/Alaska Native and Asian/Pacific Islander births since 1980. Data on Hispanic origin are available since 1989. Teen birth rates for specific racial and ethnic categories are also available since 1989. From 2003 through 2015, the birth data by race were based on the \u201cbridged\u201d race categories (5). Starting in 2016, the race categories for reporting birth data changed; the new race and Hispanic origin categories are: Non-Hispanic, Single Race White; Non-Hispanic, Single Race Black; Non-Hispanic, Single Race American Indian/Alaska Native; Non-Hispanic, Single Race Asian; and, Non-Hispanic, Single Race Native Hawaiian/Pacific Islander (5,6). Birth data by the prior, \u201cbridged\u201d race (and Hispanic origin) categories are included through 2018 for comparison.\n\nNational data on births by Hispanic origin exclude data for Louisiana, New Hampshire, and Oklahoma in 1989; New Hampshire and Oklahoma in 1990; and New Hampshire in 1991 and 1992. Birth and fertility rates for the Central and South American population includes other and unknown Hispanic. Information on reporting Hispanic origin is detailed in the Technical Appendix for the 1999 public-use natality data file (see ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat1999doc.pdf).",
-            "title": "NCHS - Teen Birth Rates for Females by Age Group, Race, and Hispanic Origin: United States",
-            "isPartOf": "NCHS - Teen Birth Rates for Females by Age Group, Race, and Hispanic Origin: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148523,48 +148491,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/e8kx-wbww",
+            "isPartOf": "NCHS - Teen Birth Rates for Females by Age Group, Race, and Hispanic Origin: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "age",
+                "birth rate",
+                "ethnicity",
+                "hispanic origin",
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
+            "references": [
+                "https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf",
+                "https://www.cdc.gov/nchs/data/misc/usvss.pdf",
+                "https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
+            ],
+            "rights": "public",
+            "spatial": "United States",
+            "temporal": "1960/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Teen Birth Rates for Females by Age Group, Race, and Hispanic Origin: United States"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -148587,50 +148563,49 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n8mc-b4w4",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-03-22",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2024-07-05",
-            "modified": "2025-01-13",
-            "references": [
-                "https://github.com/CDCgov/covid_case_privacy_review/blob/master/analysis/public%2019%20utility%20summary.pdf"
-            ],
-            "keyword": [
-                "cases",
-                "coronavirus",
-                "county",
-                "covid19",
-                "covid-19",
-                "microdata",
-                "state",
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
-            "identifier": "https://data.cdc.gov/api/views/n8mc-b4w4",
-            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated.\n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance public use dataset has 19 elements for all COVID-19 cases shared with CDC and includes demographics, geography (county and state of residence), any exposure history, disease severity indicators and outcomes, and presence of any underlying medical conditions and risk behaviors.\n\nCurrently, CDC provides the public with three versions of COVID-19 case surveillance line-listed data: this <a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">19 data element dataset with geography</a>, a <a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">12 data element public use dataset</a>, and a <a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">33 data element restricted access dataset</a>.\n\nThe following apply to the public use datasets and the restricted access dataset:\n<ul><li>Data elements can be found on the COVID-19 case report form located at www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf.</li><li>Data are considered provisional by CDC and are subject to change until the data are reconciled and verified with the state and territorial data providers.</li><li>Some data are suppressed to protect individual privacy.</li><li>Datasets will include all cases with the earliest date available in each record (date received by CDC or date related to illness/specimen collection) at least 14 days prior to the creation of the current datasets. This 14-day lag allows case reporting to be stabilized and ensure that time-dependent outcome data are accurately captured.</li><li>Datasets are updated monthly.</li><li>Datasets are created using CDC\u2019s <a href=\"https://www.cdc.gov/grants/additional-requirements/ar-25.html\">Policy on Public Health Research and Nonresearch Data Management and Access</a> and include protections designed to protect individual privacy.</li><li>For more information about data collection and reporting, please see\u202f<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html\">https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html.</a></li><li>For more information about the COVID-19 case surveillance data, please see <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\"> https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html</a><br></li></ul>\n\n<b>Overview</b>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and autonomous reporting entities, including New York City and the District of Columbia (D.C.), as well as U.S. territories and affiliates. On April 5, 2020, COVID-19 was added to the <a href=\"https://ndc.services.cdc.gov/search-results-year/\">Nationally Notifiable Condition List</a> and classified as \u201cimmediately notifiable, urgent (within 24 hours)\u201d by a Council of State and Territorial Epidemiologists (CSTE) Interim Position Statement (<a href=\"https://cdn.ymaws.com/www.cste.org/resource/resmgr/ps/positionstatement2020/Interim-20-ID-01_COVID",
-            "title": "COVID-19 Case Surveillance Public Use Data with Geography",
+            "describedBy": "https://data.cdc.gov/api/views/n8mc-b4w4/files/f24e6a39-6419-4958-81d2-a22da947f8fc?download=true&filename=data_dictionary_covid_cases_public_geo.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated.\n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance public use dataset has 19 elements for all COVID-19 cases shared with CDC and includes demographics, geography (county and state of residence), any exposure history, disease severity indicators and outcomes, and presence of any underlying medical conditions and risk behaviors.\n\nCurrently, CDC provides the public with three versions of COVID-19 case surveillance line-listed data: this <a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">19 data element dataset with geography</a>, a <a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">12 data element public use dataset</a>, and a <a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">33 data element restricted access dataset</a>.\n\nThe following apply to the public use datasets and the restricted access dataset:\n<ul><li>Data elements can be found on the COVID-19 case report form located at www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf.</li><li>Data are considered provisional by CDC and are subject to change until the data are reconciled and verified with the state and territorial data providers.</li><li>Some data are suppressed to protect individual privacy.</li><li>Datasets will include all cases with the earliest date available in each record (date received by CDC or date related to illness/specimen collection) at least 14 days prior to the creation of the current datasets. This 14-day lag allows case reporting to be stabilized and ensure that time-dependent outcome data are accurately captured.</li><li>Datasets are updated monthly.</li><li>Datasets are created using CDC\u2019s <a href=\"https://www.cdc.gov/grants/additional-requirements/ar-25.html\">Policy on Public Health Research and Nonresearch Data Management and Access</a> and include protections designed to protect individual privacy.</li><li>For more information about data collection and reporting, please see\u202f<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html\">https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html.</a></li><li>For more information about the COVID-19 case surveillance data, please see <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\"> https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html</a><br></li></ul>\n\n<b>Overview</b>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and autonomous reporting entities, including New York City and the District of Columbia (D.C.), as well as U.S. territories and affiliates. On April 5, 2020, COVID-19 was added to the <a href=\"https://ndc.services.cdc.gov/search-results-year/\">Nationally Notifiable Condition List</a> and classified as \u201cimmediately notifiable, urgent (within 24 hours)\u201d by a Council of State and Territorial Epidemiologists (CSTE) Interim Position Statement (<a href=\"https://cdn.ymaws.com/www.cste.org/resource/resmgr/ps/positionstatement2020/Interim-20-ID-01_COVID",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148653,42 +148628,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
-            "describedBy": "https://data.cdc.gov/api/views/n8mc-b4w4/files/f24e6a39-6419-4958-81d2-a22da947f8fc?download=true&filename=data_dictionary_covid_cases_public_geo.xlsx",
+            "identifier": "https://data.cdc.gov/api/views/n8mc-b4w4",
+            "issued": "2021-03-22",
+            "keyword": [
+                "cases",
+                "coronavirus",
+                "county",
+                "covid19",
+                "covid-19",
+                "microdata",
+                "state",
+                "surveillance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n8mc-b4w4",
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
+                "https://github.com/CDCgov/covid_case_privacy_review/blob/master/analysis/public%2019%20utility%20summary.pdf"
+            ],
+            "spatial": "US",
+            "temporal": "2020-01-01/2024-07-05",
             "theme": [
                 "Case Surveillance"
-            ]
+            ],
+            "title": "COVID-19 Case Surveillance Public Use Data with Geography"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/3nrv-cydv",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2023-03-03",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
-            "keyword": [
-                "mesh",
-                "population groups"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/3nrv-cydv",
             "description": "Working with partners across NIH, led by NIMHD and the NLM OBSSR-Behavioral Ontology Working Group, MeSH on November 29, 2022 added Federally recognized American Indian and Alaskan Native (AI/AN) tribal names and ethnic/ethnolinguistic minority terms as newly created type 5 SCR designated as \u201cPopulation Groups\u201d. These minority names (1,700+ terms) were mapped and reviewed by subject matter experts and scientists within NIH and from outside including Network of the National Library of Medicine members.\n\nStructure: All type 5 SCRs have common fields\n1.\tCC=5 Population Group \n2.\tST=T098 Population Groups\n3.\tHM= At least one HM is to an MH under Population Groups [M01.686]\n4.\tTH= NIMHD(2023)",
-            "title": "MeSH Population Groups (Type 5 SCR)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148711,42 +148694,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/3nrv-cydv",
+            "issued": "2023-03-03",
+            "keyword": [
+                "mesh",
+                "population groups"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/3nrv-cydv",
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
+            "title": "MeSH Population Groups (Type 5 SCR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/x4ie-279c",
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
-            "identifier": "492db9fe-b288-4c5b-a75b-72c642fbc4bf",
             "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2023 Individual Dental",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148754,17 +148735,49 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "492db9fe-b288-4c5b-a75b-72c642fbc4bf",
+            "issued": "2023-08-09",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2023",
+                "qhp landscape instructions",
+                "sadp"
+            ],
+            "landingPage": "https://healthdata.gov/d/x4ie-279c",
+            "modified": "2023-08-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2023 Individual Dental"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The DC Metropolitan Area Drug Study (DC<em>MADS) was<br />\nconducted in 1991, and included special analyses of homeless and<br />\ntransient populations and of women delivering live births in the DC<br />\nhospitals. DC</em>MADS was undertaken to assess the full extent of the<br />\ndrug problem in one metropolitan area. The study was comprised of 16<br />\nseparate studies that focused on different sub-groups, many of which<br />\nare typically not included or are underrepresented in household<br />\nsurveys. The Homeless and Transient Population<br />\nstudy examines the prevalence of illicit drug, alcohol, and tobacco<br />\nuse among members of the homeless and transient population aged 12 and<br />\nolder in the Washington, DC, Metropolitan Statistical Area (DC<br />\nMSA). The sample frame included respondents from shelters, soup<br />\nkitchens and food banks, major cluster encampments, and literally<br />\nhomeless people. Data from the questionnaires include history of<br />\nhomelessness, living arrangements and population movement, tobacco,<br />\ndrug, and alcohol use, consequences of use, treatment history, illegal<br />\nbehavior and arrest, emergency room treatment and hospital stays,<br />\nphysical and mental health, pregnancy, insurance, employment and<br />\nfinances, and demographics. Drug specific data include age at first<br />\nuse, route of administration, needle use, withdrawal symptoms,<br />\npolysubstance use, and perceived risk.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Washington  DC  Metropolitan Area Drug Study Homeless and Transient Population (DC-MADST-1991) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "arrests",
                 "cocaine",
@@ -148795,59 +148808,29 @@
                 "substance abuse treatment",
                 "urban population"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991",
-            "description": "<p>The DC Metropolitan Area Drug Study (DC<em>MADS) was<br />\nconducted in 1991, and included special analyses of homeless and<br />\ntransient populations and of women delivering live births in the DC<br />\nhospitals. DC</em>MADS was undertaken to assess the full extent of the<br />\ndrug problem in one metropolitan area. The study was comprised of 16<br />\nseparate studies that focused on different sub-groups, many of which<br />\nare typically not included or are underrepresented in household<br />\nsurveys. The Homeless and Transient Population<br />\nstudy examines the prevalence of illicit drug, alcohol, and tobacco<br />\nuse among members of the homeless and transient population aged 12 and<br />\nolder in the Washington, DC, Metropolitan Statistical Area (DC<br />\nMSA). The sample frame included respondents from shelters, soup<br />\nkitchens and food banks, major cluster encampments, and literally<br />\nhomeless people. Data from the questionnaires include history of<br />\nhomelessness, living arrangements and population movement, tobacco,<br />\ndrug, and alcohol use, consequences of use, treatment history, illegal<br />\nbehavior and arrest, emergency room treatment and hospital stays,<br />\nphysical and mental health, pregnancy, insurance, employment and<br />\nfinances, and demographics. Drug specific data include age at first<br />\nuse, route of administration, needle use, withdrawal symptoms,<br />\npolysubstance use, and perceived risk.This study has 1 Data Set.</p>",
-            "title": "Washington  DC  Metropolitan Area Drug Study Homeless and Transient Population (DC-MADST-1991)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991",
-                    "description": "Washington  DC  Metropolitan Area Drug Study Homeless and Transient Population (DC-MADST-1991) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991"
-                }
-            ]
+            "title": "Washington  DC  Metropolitan Area Drug Study Homeless and Transient Population (DC-MADST-1991)"
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
-                "mesh",
-                "mesh 2023 update"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/aqtu-bnvm",
             "description": "This dataset includes all newly added MeSH Main Headings for 2023. Headings play a central role in MeSH vocabulary as a unit of Indexing and retrieval. With the exception of Class 3 Descriptors, all descriptors are organized into a numbered tree structure or hierarchy that allows users to browse in a orderly fashion from broader to narrower topics.  Scope Notes provide a concise summary describing the meaning and scope of the MeSH Descriptor.",
-            "title": "MeSH 2023 - New Headings with Scope Notes",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148870,26 +148853,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/aqtu-bnvm",
+            "issued": "2022-12-19",
+            "keyword": [
+                "mesh",
+                "mesh 2023 update"
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
+            "title": "MeSH 2023 - New Headings with Scope Notes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "accrualPeriodicity": "Dataset will no longer be updated.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
-            "issued": "2023-06-14",
-            "@type": "dcat:Dataset",
-            "temporal": "1992-2022",
-            "modified": "2024-07-24",
-            "references": [
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHAMCS/",
-                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHAMCS/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo.cdc.gov"
+            },
+            "describedBy": "For the survey, findings are based on a national sample of visits to emergency departments (EDs) in noninstitutional general and short-stay hospitals, exclusive of Federal, military, and Veterans Administration hospitals, located in the 50 States and the District of Columbia. The sampling frame for the 2021 NHAMCS was constructed from IQVIA\u2019s database. A three-stage probability sampling design is used. The first stage consists of a sample of geographically defined areas also known as Primary Sampling Units (PSU). In the second stage, is of hospitals within those PSU and all emergency service areas within the emergency department are selected. Emergency service areas (ESAs) are not sampled at this stage. In the third stage ESAs are sampled.",
+            "description": "The National Hospital Ambulatory Medical Care Survey (NHAMCS) has been fielded annually since 1992 to collect data on the utilization and provision of ambulatory care services in hospital emergency and outpatient departments. Data collection from hospital-based ambulatory surgery centers began in 2009. And between 2010 and 2012 NHAMCS gathered data on visits to freestanding ambulatory surgery centers. In 2018, the survey began focusing on just the ambulatory visits made to emergency departments.\nEach emergency department is randomly assigned to a 4-week reporting period. During this period, data for a systematic random sample of visits are recorded by Census interviewers using a computerized Patient Record Form. Data are obtained on patient characteristics such as age, sex, race, and ethnicity, and visit characteristics such as patient\u2019s reason for visit, provider\u2019s diagnosis, services ordered or provided, and treatments, including medication therapy. In addition, data about the facility are collected as part of a survey induction interview.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Links to 1992-2022 .ZIP and .EXE data files. Data documentation links also inlcuded.",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHAMCS/",
+                    "mediaType": "text/html",
+                    "title": "NHAMCS 1992-2022"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/tqpr-vcrm",
+            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "issued": "2023-06-14",
             "keyword": [
                 "cause of injury",
                 "diagnosis",
@@ -148904,66 +148914,41 @@
                 "prescription drugs",
                 "reason for visit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo.cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-07-24",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/tqpr-vcrm",
-            "description": "The National Hospital Ambulatory Medical Care Survey (NHAMCS) has been fielded annually since 1992 to collect data on the utilization and provision of ambulatory care services in hospital emergency and outpatient departments. Data collection from hospital-based ambulatory surgery centers began in 2009. And between 2010 and 2012 NHAMCS gathered data on visits to freestanding ambulatory surgery centers. In 2018, the survey began focusing on just the ambulatory visits made to emergency departments.\nEach emergency department is randomly assigned to a 4-week reporting period. During this period, data for a systematic random sample of visits are recorded by Census interviewers using a computerized Patient Record Form. Data are obtained on patient characteristics such as age, sex, race, and ethnicity, and visit characteristics such as patient\u2019s reason for visit, provider\u2019s diagnosis, services ordered or provided, and treatments, including medication therapy. In addition, data about the facility are collected as part of a survey induction interview.",
-            "title": "National Hospital Ambulatory Medical Care Survey, Public-use data 1992-2022",
-            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHAMCS/",
-                    "description": "Links to 1992-2022 .ZIP and .EXE data files. Data documentation links also inlcuded.",
-                    "@type": "dcat:Distribution",
-                    "title": "NHAMCS 1992-2022"
-                }
+            "references": [
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHAMCS/",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHAMCS/"
             ],
+            "rights": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
             "spatial": "United States",
-            "describedBy": "For the survey, findings are based on a national sample of visits to emergency departments (EDs) in noninstitutional general and short-stay hospitals, exclusive of Federal, military, and Veterans Administration hospitals, located in the 50 States and the District of Columbia. The sampling frame for the 2021 NHAMCS was constructed from IQVIA\u2019s database. A three-stage probability sampling design is used. The first stage consists of a sample of geographically defined areas also known as Primary Sampling Units (PSU). In the second stage, is of hospitals within those PSU and all emergency service areas within the emergency department are selected. Emergency service areas (ESAs) are not sampled at this stage. In the third stage ESAs are sampled.",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Dataset will no longer be updated.",
+            "temporal": "1992-2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Ambulatory Medical Care Survey, Public-use data 1992-2022"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/x5cu-d9pq",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-03-12",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-10",
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
-            "identifier": "207d084f-0d9d-4cab-b210-ba813d63b572",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-28 to 2022-03-06",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -148971,38 +148956,36 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "207d084f-0d9d-4cab-b210-ba813d63b572",
+            "issued": "2022-03-12",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/x5cu-d9pq",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-03-10",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-28 to 2022-03-06"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.hcup-us.ahrq.gov",
             "bureauCode": [
                 "009:33"
             ],
-            "issued": "2022-06-07",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
-                "ambulatory surgery",
-                "hcup"
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
-            "identifier": "https://healthdata.gov/api/views/x5sw-xtqj",
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/nass/nassdbdocumentation.jsp",
             "description": "The largest all-payer ambulatory surgery database in the United States, the Healthcare Cost and Utilization Project (HCUP) Nationwide Ambulatory Surgery Sample (NASS) produces national estimates of major ambulatory surgery encounters in hospital-owned facilities. Major ambulatory surgeries are defined as selected major therapeutic procedures that require the use of an operating room, penetrate or break the skin, and involve regional anesthesia, general anesthesia, or sedation to control pain (i.e., surgeries flagged as \"narrow\" in the HCUP Surgery Flag Software).  Unweighted, the NASS contains approximately 9.0 million ambulatory surgery encounters each year and approximately 11.8 million ambulatory surgery procedures. Weighted, it estimates approximately 11.9 million ambulatory surgery encounters and 15.7 million ambulatory surgery procedures.\n\nSampled from the HCUP State Ambulatory Surgery and Services Databases (SASD) and State Emergency Department Databases (SEDD) in order to capture both planned and emergent major ambulatory surgeries, the NASS can be used to examine selected ambulatory surgery utilization patterns.  Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels.\n\nThe NASS contains clinical and resource-use information that is included in a typical hospital-owned facility record, including patient characteristics, clinical diagnostic and surgical procedure codes, disposition of patients, total charges, facility characteristics, and expected source of payment, regardless of payer, including patients covered by Medicaid, private insurance, and the uninsured. The NASS excludes data elements that could directly or indirectly identify individuals, hospitals, or states.  The NASS is limited to encounters with at least one in-scope major ambulatory surgery on the record, performed at hospital-owned facilities. Procedures intended primarily for diagnostic purposes are not considered in-scope.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
-            "title": "HCUP Nationwide Ambulatory Surgery Sample (NASS) Database \u2013 Restricted Access",
-            "programCode": [
-                "009:074"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149011,137 +148994,130 @@
                     "title": "HCUP Nationwide Ambulatory Surgery Sample (NASS) Database \u2013 Restricted Access"
                 }
             ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/nass/nassdbdocumentation.jsp",
-            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx"
+            "identifier": "https://healthdata.gov/api/views/x5sw-xtqj",
+            "issued": "2022-06-07",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "ambulatory surgery",
+                "hcup"
+            ],
+            "landingPage": "https://www.hcup-us.ahrq.gov",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:074"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "title": "HCUP Nationwide Ambulatory Surgery Sample (NASS) Database \u2013 Restricted Access"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/x6kx-6hpr",
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
-            "identifier": "c1c4b0cf-c957-4b00-bcf4-c0905045a5b3",
             "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of COVID-19 testing services provided to Medicaid and CHIP beneficiaries, by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-19 testing services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "COVID Testing  and Testing-Related  Services Provided to Medicaid and CHIP Beneficiaries",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/COVID-Testing-and-Testing-Related-Services-Provided-to-MedicaidCHIP-Beneficiaries.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of COVID-19 testing services provided to Medicaid and CHIP beneficiaries, by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-19 testing services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of COVID-19 testing services provided to Medicaid and CHIP beneficiaries, by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-19 testing services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/COVID-Testing-and-Testing-Related-Services-Provided-to-MedicaidCHIP-Beneficiaries.csv",
+                    "mediaType": "text/csv",
                     "title": "COVID Testing  and Testing-Related  Services Provided to Medicaid and CHIP Beneficiaries"
                 }
             ],
+            "identifier": "c1c4b0cf-c957-4b00-bcf4-c0905045a5b3",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "covid-19",
+                "dq atlas",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/x6kx-6hpr",
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
+            "title": "COVID Testing  and Testing-Related  Services Provided to Medicaid and CHIP Beneficiaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/x6me-tvjr",
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
-            "identifier": "4acd783c-272d-5db4-b86d-361a297722de",
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
+            "identifier": "4acd783c-272d-5db4-b86d-361a297722de",
+            "issued": "2024-11-20",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/x6me-tvjr",
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
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-09-30",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
-            "modified": "2024-05-03",
-            "references": [
-                "Vaccine Safety Datalink"
-            ],
-            "keyword": [
-                "children",
-                "flu",
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
-            "identifier": "https://data.cdc.gov/api/views/fz77-au2z",
             "description": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years\n\t\n\u2022  These monthly flu vaccination coverage estimates for pregnant persons are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD), a collaboration between CDC\u2019s Immunization Safety Office and nine integrated health care organizations.\u00a7 This system has been used annually to estimate vaccination coverage among pregnant persons. COVID-19 vaccination coverage for pregnant persons is available here. \n\n\u2022\tFigure 3A. Monthly Cumulative Influenza Vaccination Coverage*, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years, United States, Data Source: Vaccine Safety Datalink \n\n\u2022\tFigure 3B. Cumulative Influenza Vaccination Coverage*, by Month, Flu Season, and Race/Ethnicity, Pregnant Persons 18-49 years, United States, Data Source: Vaccine Safety Datalink \n\n\u2022\tFor any month\u2019s coverage estimate, the denominator is the number of persons with a pregnancy during the current flu season (defined as August through March) beginning before or during the specified month. The numerator is the subset of the denominator who have received flu vaccination prior to, during, or after pregnancy. The denominator increases as more persons are identified as pregnant or having been pregnant during the flu season. Cumulative vaccination coverage for one month may be lower than cumulative coverage for a previous month due to addition to the denominator of persons who are less likely to have received vaccination.",
-            "title": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149164,73 +149140,110 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/fz77-au2z",
+            "issued": "2022-09-30",
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
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2024-05-03",
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
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/x7c4-svex",
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
-            "identifier": "b0ba435a-a21a-5283-a470-7051321da5b1",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "implAuto_states",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states.csv",
-                    "description": "{\"dataset\": \"states\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states.csv",
+                    "mediaType": "text/csv",
                     "title": "states csv file"
                 }
             ],
+            "identifier": "b0ba435a-a21a-5283-a470-7051321da5b1",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/x7c4-svex",
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
+            "title": "implAuto_states"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
             },
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "bureauCode": [
-                "009:30"
+                    "@type": "dcat:Distribution",
+                    "description": "Drug Abuse Warning Network (DAWN-2004) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2004-nid13613",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2004-nid13613"
+                }
             ],
-            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2004",
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2004-nid13613",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "demographic characteristics",
@@ -149243,86 +149256,60 @@
                 "substance abuse",
                 "suicide"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2004",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2004-nid13613",
-            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
-            "title": "Drug Abuse Warning Network (DAWN-2004)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2004-nid13613",
-                    "description": "Drug Abuse Warning Network (DAWN-2004) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2004-nid13613"
-                }
-            ]
+            "title": "Drug Abuse Warning Network (DAWN-2004)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/corporate-integrity-agreement-cia-documents-0",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "department-of-health-human-services",
-                "health care providers"
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
-            "identifier": "41153824-e789-49e9-8543-5fa710bb94e3",
+            "dataQuality": true,
             "description": "<p>OIG negotiates corporate integrity agreements (CIA) with health care providers and other entities as part of the settlement of Federal health care program investigations arising under a variety of civil false claims statutes. Providers or entities agree to the obligations, and in exchange, OIG agrees not to seek their exclusion from participation in Medicare, Medicaid, or other Federal health care programs.</p>",
-            "title": "Corporate Integrity Agreement (CIA) documents",
+            "identifier": "41153824-e789-49e9-8543-5fa710bb94e3",
+            "issued": "2012-05-30",
+            "keyword": [
+                "department-of-health-human-services",
+                "health care providers"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/corporate-integrity-agreement-cia-documents-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "422:013"
             ],
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "title": "Corporate Integrity Agreement (CIA) documents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mscq-ew9n",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Safety Research Protective Technology Branch; Health Effects Laboratory Division Physical Effects Research Branch",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mscq-ew9n",
             "description": "Type I industrial helmets have been widely used at construction sites and by manufacturers as \u201cgeneral purpose\u201d safety helmets. The performance of Type I industrial helmets for fall protection is not required to be tested in standardized tests. Chin straps and suspension system adjustment mechanisms are two important components of a typical industrial helmet, but the effects of proper use of them on the protective performance of Type I helmets have not been evaluated. The current study was designed to analyze the fall protection performance of Type I industrial helmets and to evaluate if the use of a chin strap and the suspension system tightness have any effect on protection performance. Head impact tests were performed by letting an instrumented manikin free fall backwards, from a standing posture, so that the manikin would make head-first contact with a solid surface of two different materials (concrete and plywood-covered). The results showed that all four tested helmet models demonstrated excellent performances for fall protection compared to the control group without wearing helmets. The fall protection performance of the advanced helmet models was substantially better than the basic helmet models. However, the effects of the use of chin straps and suspension system tightness on the helmets\u2019 fall protection performance were statistically not significant. The findings of our study provide information to help construction companies and manufacturers better manage the use of Type I helmets for fall protection, thereby reducing work-related traumatic brain injury risks.",
-            "title": "Evaluation of the fall protection of Type I industrial helmets",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -149330,20 +149317,47 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mscq-ew9n",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/mscq-ew9n",
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
+            "title": "Evaluation of the fall protection of Type I industrial helmets"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2002",
             "bureauCode": [
                 "009:30"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HealthData.gov",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.icpsr.umich.edu/icpsrweb/SAMHDA/ssvd/studies/03903/variables",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covers substance abuse treatment history and perceived need for treatment, and includes questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing.</p>\n <ul><li>National Survey on Drug Use and Health, 2002 (ICPSR 3903): http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/64/studies/3903?archive=ICPSR&sortBy=7</li><li>National Survey on Drug Use and Health, 2003 (ICPSR 4138): http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/64/studies/4138?archive=ICPSR&sortBy=7</li></ul>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://nsduhweb.rti.org/respweb/homepage.cfm",
+                    "mediaType": "text/html",
+                    "title": "HTML"
+                }
+            ],
+            "identifier": "c4e3821e-0f45-4202-8893-665f48c998ed",
             "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -149386,91 +149400,90 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HealthData.gov",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2002",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:061"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "c4e3821e-0f45-4202-8893-665f48c998ed",
-            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covers substance abuse treatment history and perceived need for treatment, and includes questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing.</p>\n <ul><li>National Survey on Drug Use and Health, 2002 (ICPSR 3903): http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/64/studies/3903?archive=ICPSR&sortBy=7</li><li>National Survey on Drug Use and Health, 2003 (ICPSR 4138): http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/64/studies/4138?archive=ICPSR&sortBy=7</li></ul>",
-            "title": "National Survey on Drug Use and Health (NSDUH), 2002",
-            "programCode": [
-                "009:061"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://nsduhweb.rti.org/respweb/homepage.cfm",
-                    "mediaType": "text/html",
-                    "title": "HTML"
-                }
-            ],
-            "describedBy": "http://www.icpsr.umich.edu/icpsrweb/SAMHDA/ssvd/studies/03903/variables",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "National Survey on Drug Use and Health (NSDUH), 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/x7rp-ggcs",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-03-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-20",
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
-            "identifier": "c0bef49e-46ea-4b9d-9153-76b4078d58b7",
             "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by managed care participation (comprehensive managed care, primary care case management, MLTSS, including PACE, behavioral health organizations, nonmedical prepaid health plans, medical-only prepaid health plans, and other). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each managed care plan type over the year (duplicated count); (2) the number of beneficiaries enrolled in each managed care plan type as of an individual\u2019s last month of enrollment (duplicated count); and (3) average monthly enrollment in each managed care plan type.  \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some cells have a value of \u201cDS\u201d. Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topics Enrollment in CMC, Enrollment in PCCM Programs, and Enrollment in BHO Plans. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Managed Care Information for Medicaid and CHIP Beneficiaries by Year",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/ManagedCare-anul.csv",
-                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by managed care participation (comprehensive managed care, primary care case management, MLTSS, including PACE, behavioral health organizations, nonmedical prepaid health plans, medical-only prepaid health plans, and other). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each managed care plan type over the year (duplicated count); (2) the number of beneficiaries enrolled in each managed care plan type as of an individual\u2019s last month of enrollment (duplicated count); and (3) average monthly enrollment in each managed care plan type.  \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some cells have a value of \u201cDS\u201d. Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topics Enrollment in CMC, Enrollment in PCCM Programs, and Enrollment in BHO Plans. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by managed care participation (comprehensive managed care, primary care case management, MLTSS, including PACE, behavioral health organizations, nonmedical prepaid health plans, medical-only prepaid health plans, and other). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each managed care plan type over the year (duplicated count); (2) the number of beneficiaries enrolled in each managed care plan type as of an individual\u2019s last month of enrollment (duplicated count); and (3) average monthly enrollment in each managed care plan type.  \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some cells have a value of \u201cDS\u201d. Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topics Enrollment in CMC, Enrollment in PCCM Programs, and Enrollment in BHO Plans. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/ManagedCare-anul.csv",
+                    "mediaType": "text/csv",
                     "title": "Managed Care Information for Medicaid and CHIP Beneficiaries by Year"
                 }
             ],
+            "identifier": "c0bef49e-46ea-4b9d-9153-76b4078d58b7",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "managed care",
+                "medicaid",
+                "t-msis analytic files"
+            ],
```

