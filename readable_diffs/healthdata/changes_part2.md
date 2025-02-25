# Change History for healthdata.json (Part 2)

### Changes from 31606f9 to dd2190f (Part 1/11)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index b017330..4c48019 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -3,35 +3,20 @@
     "@id": "https://healthdata.gov/data.json",
     "@type": "dcat:Catalog",
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "dataset": [
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/238m-ezg9",
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
-            "identifier": "e28727b2-fe6b-46cb-8617-408de290200d",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210726 to 20210801",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39,43 +24,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "e28727b2-fe6b-46cb-8617-408de290200d",
+            "issued": "2021-10-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/238m-ezg9",
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
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210726 to 20210801"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kyph-4i8d",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/kyph-4i8d",
             "description": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98,49 +75,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kyph-4i8d",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "confirmed",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "vibriosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kyph-4i8d",
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
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-25",
-            "references": [
-                "https://chronicdata.cdc.gov/d/f8gx-sdye"
-            ],
-            "keyword": [
-                "administration and management",
-                "best practices for comprehensive tobacco control programs",
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
-            "identifier": "https://data.cdc.gov/api/views/n4v6-56e8",
+            "describedBy": "https://chronicdata.cdc.gov/Funding/CDC-Best-Practices-for-Comprehensive-Tobacco-Contr/n4v6-56e8",
             "description": "2007. Centers for Disease Control and Prevention (CDC). Best Practices for Comprehensive Tobacco Control Programs. Funding. CDC's Best Practices for Comprehensive Tobacco Control Programs is an evidence-based guide to help states plan and establish effective tobacco control programs to prevent and reduce tobacco use.  Data are reported at total and per capita funding levels. Data include recommended, upper, and lower total funding levels for state programs, in addition to funding breakdowns by intervention areas such as: State and Community Interventions, Health Communication Interventions, Cessation Interventions, Surveillance and Evaluation, and Administration and Management.",
-            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2007",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -163,23 +137,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Funding/CDC-Best-Practices-for-Comprehensive-Tobacco-Contr/n4v6-56e8",
+            "identifier": "https://data.cdc.gov/api/views/n4v6-56e8",
+            "issued": "2023-07-18",
+            "keyword": [
+                "administration and management",
+                "best practices for comprehensive tobacco control programs",
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
+            "references": [
+                "https://chronicdata.cdc.gov/d/f8gx-sdye"
+            ],
             "theme": [
                 "Funding"
-            ]
+            ],
+            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2007"
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
@@ -189,71 +200,36 @@
                 "opioid use",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/cjr4-kj3n",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-20",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
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
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -276,44 +252,47 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1F. Brucellosis to Candida auris, clinical"
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
@@ -336,46 +315,44 @@
                     "mediaType": "application/xml"
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
                 "Assisted Reproductive Technology (ART)"
-            ]
+            ],
+            "title": "2020 Final Assisted Reproductive Technology (ART) Services and Profiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/m8jv-u92i",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/m8jv-u92i",
             "description": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -398,38 +375,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/m8jv-u92i",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "other serogroups",
+                "unknown serogroup",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/m8jv-u92i",
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
+            "title": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/25ak-3iyd",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-02-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-12",
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
-            "identifier": "5457e951-66dc-42aa-a626-2704bce39266",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-05-2024-to-02-11-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -438,42 +423,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-05-2024-to-02-11-2024"
                 }
             ],
+            "identifier": "5457e951-66dc-42aa-a626-2704bce39266",
+            "issued": "2024-02-14",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/25ak-3iyd",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2024-02-12",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-05-2024-to-02-11-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rbrz-y4zd",
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
-            "identifier": "https://data.cdc.gov/api/views/rbrz-y4zd",
             "description": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -496,38 +474,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rbrz-y4zd",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "tuberculosis",
+                "tularemia",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rbrz-y4zd",
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
+            "title": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/25f9-qkkx",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-07-06",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-05",
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
-            "identifier": "8185fa9f-cf59-49a4-9d67-10cef09f9aa4",
             "description": "The Reference Document link for the downable Blood Disorder Treatment Spreadsheet can be accessed below under the Additional Information table under Related Documents.",
-            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 6/1/2023)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -535,94 +520,86 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "8185fa9f-cf59-49a4-9d67-10cef09f9aa4",
+            "issued": "2023-07-06",
+            "keyword": [
+                "drug products"
+            ],
+            "landingPage": "https://healthdata.gov/d/25f9-qkkx",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2023-07-05",
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
+            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 6/1/2023)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/25ya-rxer",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-09-28",
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
-            "identifier": "3badba63-9497-512e-b2ed-c8d3be0ea213",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_states",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states.csv",
-                    "description": "{\"dataset\": \"states\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states.csv",
+                    "mediaType": "text/csv",
                     "title": "states csv file"
                 }
             ],
+            "identifier": "3badba63-9497-512e-b2ed-c8d3be0ea213",
+            "issued": "2022-09-28",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/25ya-rxer",
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
+            "title": "featAuto_states"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/s5s8-d82d",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
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
-            "identifier": "https://data.cdc.gov/api/views/s5s8-d82d",
             "description": "NNDSS - Table II. Babesiosis to Campylobacteriosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -645,39 +622,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/s5s8-d82d",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "babesiosis",
+                "campylobacteriosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/s5s8-d82d",
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
+            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/Traces/wgs/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jsga-gefc",
             "description": "This site is for browsing WGS (Whole Genome Shotgun) genomes, TSA (Transcriptome Shotgun Assemblies) and TLS (Targeted Locus Study) sets. WGS sequences are incomplete genomes that have been sequenced by a whole genome shotgun strategy. TSA sequences are transcript sequences that have been computationally assembled from primary RNA sequence data. TLS sequences are large-scale marker gene sequencing studies.\n\nPlease consult WGS Submission or TSA Submission pages for more details.\nhttps://www.ncbi.nlm.nih.gov/genbank/wgs\nhttps://www.ncbi.nlm.nih.gov/genbank/tsa",
-            "title": "Sequence Set Browser",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -686,53 +669,40 @@
                     "title": "Sequence Set Browser - Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jsga-gefc",
+            "issued": "2021-08-26",
+            "keyword": [
+                "genomics",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Traces/wgs/",
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
+            "title": "Sequence Set Browser"
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
-            "modified": "2023-11-09",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "hhs region",
-                "influenza",
-                "mortality",
-                "nchs",
-                "nvss",
-                "pneumonia",
-                "provisional",
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
-            "identifier": "https://data.cdc.gov/api/views/ynw2-4viq",
             "description": "Deaths counts for influenza, pneumonia, and COVID-19 reported to NCHS by week ending date, by state and HHS region, and age group.",
-            "title": "Provisional Death Counts for Influenza, Pneumonia, and COVID-19",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -755,41 +725,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/ynw2-4viq",
+            "issued": "2020-09-24",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hhs region",
+                "influenza",
+                "mortality",
+                "nchs",
+                "nvss",
+                "pneumonia",
+                "provisional",
+                "state",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-11-09",
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
+            "title": "Provisional Death Counts for Influenza, Pneumonia, and COVID-19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fkfk-2j5x",
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
-            "identifier": "https://data.cdc.gov/api/views/fkfk-2j5x",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 9 - San Francisco",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -812,48 +795,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fkfk-2j5x",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fkfk-2j5x",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 9 - San Francisco"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/medicare-telehealth-trends",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-01-06",
-            "temporal": "2024-04-01/2024-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-12",
-            "references": [
-                "https://data.cms.gov/resources/medicare-telehealth-trends-methodology-current"
-            ],
-            "keyword": [
-                "medicare"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/939226be-b107-476e-8777-f199a840138a/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-telehealth-trends-data-dictionary",
             "description": "The Medicare Telehealth Trends dataset provides information about people with Medicare who used telehealth services between January 1, 2020 and June 30, 2024. The data were used to generate the Medicare Telehealth Trends Report.",
-            "title": "Medicare Telehealth Trends",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/939226be-b107-476e-8777-f199a840138a/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/939226be-b107-476e-8777-f199a840138a/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Telehealth Trends : 2024-04-01"
                 },
                 {
@@ -869,27 +852,63 @@
                     "title": "Medicare Telehealth Trends : 2024-04-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-telehealth-trends-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/939226be-b107-476e-8777-f199a840138a/data-viewer",
+            "issued": "2022-01-06",
+            "keyword": [
+                "medicare"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/medicare-telehealth-trends",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-12-12",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-telehealth-trends-methodology-current"
+            ],
+            "temporal": "2024-04-01/2024-06-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Telehealth Trends"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/health-insurance-marketplace-summary-enrollment-data-initial-annual-open-enrollment-period-1",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Audrey McDowell",
+                "hasEmail": "mailto:audrey.mcdowell@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://aspe.hhs.gov/health/reports/2014/MarketPlaceEnrollment/Apr2014/Marketplace_StateSum.cfm",
+            "description": "<p>This file includes data for states that are implementing their own Marketplaces, also known as State-Based Marketplaces or SBMs, and states with Marketplaces that are supported by or fully run by the federal government, including those run in partnership with states, also known as the Federally-Facilitated Marketplace or FFM. Includes demographic characteristics, and plan selected (by metal level). Please refer to the full report listed under Resources.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aspe.hhs.gov/health/reports/2014/MarketPlaceEnrollment/Apr2014/excel/workbook.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "XLS "
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aspe.hhs.gov/health/reports/2014/MarketPlaceEnrollment/Apr2014/Marketplace_StateSum.cfm",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "identifier": "44105b16-a92a-4233-ac87-1357e41a4953",
             "issued": "2014-06-16",
-            "temporal": "2013-10-01T00:00:00-04:00/2014-03-31T00:00:00-04:00",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
             "keyword": [
                 "administrative",
                 "affordable care act",
@@ -909,74 +928,34 @@
                 "plan",
                 "state"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Audrey McDowell",
-                "hasEmail": "mailto:audrey.mcdowell@hhs.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Health & Human Services"
-            },
-            "identifier": "44105b16-a92a-4233-ac87-1357e41a4953",
-            "description": "<p>This file includes data for states that are implementing their own Marketplaces, also known as State-Based Marketplaces or SBMs, and states with Marketplaces that are supported by or fully run by the federal government, including those run in partnership with states, also known as the Federally-Facilitated Marketplace or FFM. Includes demographic characteristics, and plan selected (by metal level). Please refer to the full report listed under Resources.</p>",
-            "title": "Health Insurance Marketplace: Summary Enrollment Data for the Initial Annual Open Enrollment Period",
+            "landingPage": "https://healthdata.gov/dataset/health-insurance-marketplace-summary-enrollment-data-initial-annual-open-enrollment-period-1",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2025-01-28",
             "programCode": [
                 "009:082"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aspe.hhs.gov/health/reports/2014/MarketPlaceEnrollment/Apr2014/excel/workbook.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "XLS "
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://aspe.hhs.gov/health/reports/2014/MarketPlaceEnrollment/Apr2014/Marketplace_StateSum.cfm",
-                    "mediaType": "text/html",
-                    "title": "Text "
-                }
-            ],
-            "describedBy": "https://aspe.hhs.gov/health/reports/2014/MarketPlaceEnrollment/Apr2014/Marketplace_StateSum.cfm",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2013-10-01T00:00:00-04:00/2014-03-31T00:00:00-04:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Health Insurance Marketplace: Summary Enrollment Data for the Initial Annual Open Enrollment Period"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ncbi.nlm.nih.gov/gene",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-09-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "api",
-                "dataset",
-                "genes",
-                "genomics",
-                "phenotype",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ddn9-p8cj",
             "description": "Gene integrates information from a wide range of species. A record may include nomenclature, Reference Sequences (RefSeqs), maps, pathways, variations, phenotypes, and links to genome-, phenotype-, and locus-specific resources worldwide.",
-            "title": "Gene",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -997,39 +976,43 @@
                     "title": "Access Gene via E-Utilities API"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ddn9-p8cj",
+            "issued": "2016-09-01",
+            "keyword": [
+                "api",
+                "dataset",
+                "genes",
+                "genomics",
+                "phenotype",
+                "tools & utilities"
+            ],
+            "landingPage": "http://www.ncbi.nlm.nih.gov/gene",
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
+            "title": "Gene"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/3se3-rwj2",
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
-            "identifier": "https://data.cdc.gov/api/views/3se3-rwj2",
             "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 9 - San Francisco",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1052,52 +1035,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/3se3-rwj2",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/3se3-rwj2",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 9 - San Francisco"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-12",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
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
-            "identifier": "https://data.cdc.gov/api/views/siwp-yg6m",
             "description": "Provisional deaths involving COVID-19 reported to NCHS by MMWR week, race and Hispanic origin, and age group. Deaths occurred in the United States.\n\nAge groups: 0-4, 5-11, 12-17, 18-29, 30-39, 40-49, 50-64, 65-74, and 75+ years",
-            "title": "AH Provisional COVID-19 Death Counts by Week, Race, and Age, United States 2020-2023",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1120,40 +1091,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/siwp-yg6m",
+            "issued": "2021-10-21",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
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
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Death Counts by Week, Race, and Age, United States 2020-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/haed-k2ka",
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
-            "identifier": "https://data.cdc.gov/api/views/haed-k2ka",
             "description": "Alcohol-Impaired Driving Fatalities 2005-2014; All persons killed in crashes involving a driver with BAC >= .08 g/dL. Occupant Fatalities 2005-2014; All occupants killed where body type = 1-79. Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2005-2013 Final Reports and 2014 Annual Report File",
-            "title": "Occupant and Alcohol-Impaired Driving Deaths in States, 2005-2014",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1176,55 +1159,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/haed-k2ka",
+            "issued": "2016-09-26",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/haed-k2ka",
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
+            "title": "Occupant and Alcohol-Impaired Driving Deaths in States, 2005-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/childvaxview/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-26",
-            "keyword": [
-                "child vaccination",
-                "combined 7 series",
-                "dtap",
-                "hepa",
-                "hepatitis a",
-                "hepatitis b",
-                "hepb",
-                "hib",
-                "immunization",
-                "influenza",
-                "mmr",
-                "pcv",
-                "polio",
-                "rotavirus",
-                "vaccination",
-                "vaccination coverage",
-                "varicella",
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
-            "identifier": "https://data.cdc.gov/api/views/fhky-rtsk",
             "description": "Vaccination Coverage among Young Children (0-35 Months)\n\n\u2022 National, regional, state, and selected local area vaccination coverage estimates for 2-year-old children by birth year and birth year cohorts from the National Immunization Survey-Child.\n\n\u2022 Additional information available at https://www.cdc.gov/vaccines/imz-managers/coverage/childvaxview/index.html",
-            "title": "Vaccination Coverage among Young Children (0-35 Months)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1247,20 +1214,64 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fhky-rtsk",
+            "issued": "2021-05-13",
+            "keyword": [
+                "child vaccination",
+                "combined 7 series",
+                "dtap",
+                "hepa",
+                "hepatitis a",
+                "hepatitis b",
+                "hepb",
+                "hib",
+                "immunization",
+                "influenza",
+                "mmr",
+                "pcv",
+                "polio",
+                "rotavirus",
+                "vaccination",
+                "vaccination coverage",
+                "varicella",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/childvaxview/index.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-26",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Child Vaccinations"
-            ]
+            ],
+            "title": "Vaccination Coverage among Young Children (0-35 Months)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "Contains data for FDA pet food recalls since January 1, 2006.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/newpetfoodrecalls/PetFoodRecallProductsList2009.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "617db889-3907-4429-aa64-b4747156d437",
             "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "community health",
                 "health",
@@ -1270,65 +1281,30 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "617db889-3907-4429-aa64-b4747156d437",
-            "description": "Contains data for FDA pet food recalls since January 1, 2006.",
-            "title": "FDA Pet Food Recalls",
-            "programCode": [
-                "009:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/newpetfoodrecalls/PetFoodRecallProductsList2009.xls",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "title": "FDA Pet Food Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/visionhealth/vehss/estimates/amd-prevalence.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-08-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-18",
-            "references": [
-                "JAMA-Opthalmology forthcoming",
-                "https://jamanetwork.com/journals/jamaophthalmology"
-            ],
-            "keyword": [
-                "blind",
-                "blindness",
-                "prevalence",
-                "vision",
-                "visual"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC Info",
                 "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/qeru-k2y2",
             "description": "VEHSS Composite Prevalence Estimates\n2017, 2019, 2021, 2022. This dataset contains estimates of the prevalence of visual acuity loss and major eye diseases generated using a Bayesian meta-analytic modeling approach that combines information from multiple data sources to produce comprehensive estimates of prevalence by age, race, and gender at the national, state and county levels. These composite prevalence estimates are the primary surveillance measures developed by the Centers for Disease Control and Prevention\u2019s Vision & Eye Health Surveillance System (VEHSS).  \n\nFor more information about these estimates including summary tables and maps, methods, and links to related publications visit https://www.cdc.gov/visionhealth/vehss/estimates/index.html\nTo view this data in the VEHSS interactive data visualization application, visit https://ddt-vehss.cdc.gov/ and search for \u201cVEHSS Composite Prevalence Estimate\u201d.\n\n\nVisual Acuity Loss:\nVisual acuity loss prevalence estimates represent best-corrected visual acuity in the better-seeing eye and are included in rows where Category=\u2019Measured Visual Acuity\u2019.  Rows with Subgroup = \u2018Any vision loss' represents any impairment or blindness of 20/40 or worse; rows with Subgroup = 'US-defined blindness' refers to the subset of vision loss that is 20/200 or worse.\n\n\nAge Related Macular Degeneration:\nThe age-related macular degeneration (AMD) estimates represent AMD as measured with retinal imaging examination, and are included in rows where Category = \u2018Age Related Macular Degeneration\u2019.  The Subgroup \u2018Vision threatening AMD\u2019 includes patients with geographic atrophy, wet-form AMD, or choroidal neovascularization in either eye. The Subgroup \u2018Non-vision threatening AMD\u2019 includes patients with early or intermediate dry-form AMD defined as retinal pigment epithelium abnormalities or drusen \u2265125 \u00b5m in the worse-affected eye, and do not have vision threatening AMD.\n\n\nDiabetic Retinopathy:\nThe diabetic retinopathy (DR) estimates represent DR as measured with retinal imaging examination, and are included in rows where Category=\u2019Diabetic Eye Diseases\u2019.  The Subgroup \u2018Vision threatening DR\u2019 includes patients with severe non-proliferative DR, proliferative DR, and diabetic macular edema. The Subgroup \u2018Non-vision threatening DR\u2019 is defined as patients with mild-moderate non-proliferative DR or unspecified DR, and do not have vision threatening DR.\n\n\nGlaucoma:\nThe glaucoma estimates represent glaucoma as measured with retinal imaging examination and are included in rows where Category=\u2019Glaucoma\u2019. The Subgroup \u2018Vision affecting glaucoma\u2019 includes people with glaucoma and abnormal visual field. The Subgroup \u2018Non-vision affecting glaucoma\u2019 is defined as people with glaucoma without an abnormal visual field.\n\n\nAge Groups:\nThe VEHSS Composite Prevalence Estimates are available by major age groups (All ages, ages 0-17, 18-39, 40-64, 65-84, 85+) and detailed (5-year) age groups, which are indicated by the text \u201cby detailed age groups\u201d in the \u2018Indicator\u2019 field. \n\n\nPrevalence Data Type:\nThese estimates are also available as crude (Data_Value_Type = \u2018Crude Prevalence\u2019) or adjusted data (Data_Value_Type=\u2019Adjusted Prevalence).  Crude Prevalence is the estimate of the actual number and percentage of people living with each condition.  Adjusted Prevalence estimates are adjusted to match the national population by age, race/ethnicity, and gender.  Adjusted prevalence estimates can be used to help identify disparities in prevalence between geographic areas that are not explained by differences in demographic characteristics.\n\n  \nData Sources:\nData sources for VEHSS Composite Prevalence Estimates include the National Health and Nutrition Examination Survey (NHANES), the American Community Survey (ACS), the National Survey of Children\u2019s Health (NSCH), the Behavioral Risk Factor Surveillance System (BRFSS), Medicare Fee-For-Service claims, the Transformed Medicaid Statistical Information System, MarketScan commercial insurance",
-            "title": "VEHSS Composite Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1351,47 +1327,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qeru-k2y2",
+            "issued": "2024-08-20",
+            "keyword": [
+                "blind",
+                "blindness",
+                "prevalence",
+                "vision",
+                "visual"
+            ],
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/estimates/amd-prevalence.html",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-18",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "references": [
+                "JAMA-Opthalmology forthcoming",
+                "https://jamanetwork.com/journals/jamaophthalmology"
+            ],
             "theme": [
                 "Vision & Eye Health"
-            ]
+            ],
+            "title": "VEHSS Composite Prevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jgk8-6dpn",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-02-24",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-22/ 2023-05-10",
-            "modified": "2025-01-13",
-            "references": [
-                "https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6"
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
-            "identifier": "https://data.cdc.gov/api/views/jgk8-6dpn",
             "description": "Reporting of Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. This dataset will receive a final update on June 1, 2023, to reconcile historical data through May 10, 2023, and will remain publicly available.\n\nThis archived public use dataset contains historical case and percent positivity data updated weekly for all available counties and jurisdictions. Each week, the dataset was refreshed to capture any historical updates. Please note, percent positivity data may be incomplete for the most recent time period.\n\n<b>Related data </b>\nCDC provides the public with two active versions of COVID-19 county-level community transmission level data: this dataset with historical case and percent positivity data for each county from January 22, 2020 (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">Weekly Historical Changes dataset</a>) and a dataset with the levels as originally posted (<a href=\"https://data.cdc.gov/dataset/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly Originally Posted dataset</a>) since October 20, 2022. <b>Please navigate to the <a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly Originally Posted dataset</a> for the Community Transmission Levels published weekly on Thursdays.</b>\n\n<b>Methods for calculating county level of community transmission indicator</b>\nThe County Level of Community Transmission indicator uses two metrics: (1) total new COVID-19 cases per 100,000 persons in the last 7 days and (2) percentage of positive SARS-CoV-2 diagnostic nucleic acid amplification tests (NAAT) in the last 7 days. For each of these metrics, CDC classifies transmission values as low, moderate, substantial, or high (below and <a href=\"https://www.cdc.gov/mmwr/volumes/70/wr/mm7030e2.htm?s_cid=mm7030e2_w#T1_down\">here</a>). If the values for each of these two metrics differ (e.g., one indicates moderate and the other low), then the higher of the two should be used for decision-making. \n\n<b>CDC core metrics of and thresholds for community transmission levels of SARS-CoV-2</b>\n<b>Total New Case Rate Metric:</b> \"New cases per 100,000 persons in the past 7 days\" is calculated by adding the number of new cases in the county (or other administrative level) in the last 7 days divided by the population in the county (or other administrative level) and multiplying by 100,000. \"New cases per 100,000 persons in the past 7 days\" is considered to have transmission level of Low (0-9.99); Moderate (10.00-49.99); Substantial (50.00-99.99); and High (greater than or equal to 100.00). \n\n<b>Test Percent Positivity Metric:</b> \"Percentage of positive NAAT in the past 7 days\" is calculated by dividing the number of positive tests in the county (or other administrative level) during the last 7 days by the total number of tests resulted over the last 7 days. \"Percentage of positive NAAT in the past 7 days\" is considered to have transmission level of Low (less than 5.00); Moderate (5.00-7.99); Substantial (8.00-9.99); and High (greater than or equal to 10.00). \n\n\nThe data in this dataset are considered provisional by CDC and are subject to change until the data are reconciled and verified with the state and territorial data providers. \n\nThis dataset is created using <a href=\"https://www.cdc.gov/maso/policy/policy385.pdf\">CDC\u2019s Policy on Public Health Research and Nonresearch Data Management and Access</a>.\n\n\n<b>Archived data </b>\nCDC has archived two prior versions of these datasets. Both versions contain the same 7 data elements reflecting community transmission levels for all available counties and jurisdictions; however, the datasets updated daily. The archived datasets can be found here:  \n\n<a href=\"https://data.cdc.gov/Public-Health-Surveillance/United-States-COVID-19-County-Level-of-Community-T",
-            "title": "Weekly COVID-19 County Level of Community Transmission Historical Changes - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1414,37 +1390,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/jgk8-6dpn",
+            "issued": "2023-02-24",
+            "keyword": [
+                "cases",
+                "community transmission",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "laboratory"
+            ],
+            "landingPage": "https://data.cdc.gov/d/jgk8-6dpn",
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
+                "https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6"
+            ],
+            "spatial": "US",
+            "temporal": "2020-01-22/ 2023-05-10",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Weekly COVID-19 County Level of Community Transmission Historical Changes - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gt7a-q73y",
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
-            "identifier": "https://data.cdc.gov/api/views/gt7a-q73y",
             "description": "Copper-based preservatives consisting of micronized and nanoscale copper particles have been widely used in applications for wood protection. The presence of micronized/nanoscale particles and soluble aqueous copper in copper-treated wood has raised questions regarding the forms of released particles and the potential hazards of exposure during the use of these products. However, the lack of a comprehensive understanding of the chemistry of these Cu species is limiting the future investigation of the toxicity of these materials and their potential health impact on workers. In this work, we used a combination of scanning transmission electron microscope (STEM) and electron energy loss spectroscopy (EELS) to analyze the particles released during the sanding/sawing of copper-treated lumber. We have demonstrated using EELS Cu L2,3 edges with comparative reference spectra to determine the Cu species. Three types of species, including basic copper carbonate (BCC), Cu(0), and Cu(II)-Wood complex, were identified in released wood dust particles. The unbound copper particles also exist as a form of BCC or reduced Cu(0). The morphologies and chemical states of emitted copper particles indicate the potential chemical transformation due to copper-wood interactions.",
-            "title": "Revealing the Structural and Chemical Properties of Copper-based Nanoparticles Released from Copper Treated Wood-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1452,38 +1439,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gt7a-q73y",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/gt7a-q73y",
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
+            "title": "Revealing the Structural and Chemical Properties of Copper-based Nanoparticles Released from Copper Treated Wood-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/2dxe-m7jx",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-04-05",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-31",
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
-            "identifier": "f7162680-b174-48b4-b3e3-3f0f735264ab",
             "description": "SDUD",
-            "title": "SDUD",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1491,39 +1476,35 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "f7162680-b174-48b4-b3e3-3f0f735264ab",
+            "issued": "2022-04-05",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/2dxe-m7jx",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-03-31",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "SDUD"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-10-20",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
-            "keyword": [
-                "injury",
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
-            "identifier": "https://data.cdc.gov/api/views/nt65-c7a7",
             "description": "This dataset describes injury mortality in the United States beginning in 1999. Two concepts are included in the circumstances of an injury death: intent of injury and mechanism of injury. Intent of injury describes whether the injury was inflicted purposefully (intentional injury) and, if purposeful, whether the injury was self-inflicted (suicide or self-harm) or inflicted by another person (homicide). Injuries that were not purposefully inflicted are considered unintentional (accidental) injuries. Mechanism of injury describes the source of the energy transfer that resulted in physical or physiological harm to the body. Examples of mechanisms of injury include falls, motor vehicle traffic crashes, burns, poisonings, and drownings (1,2). \r\n\r\nData are based on information from all resident death certificates filed in the 50 states and the District of Columbia. Age-adjusted death rates (per 100,000 standard population) are based on the 2000 U.S. standard population. Populations used for computing death rates for 2011\u20132015 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for non-census years before 2010 are revised using updated intercensal population estimates and may differ from rates previously published.\r\n\r\nCauses of injury death are classified by the International Classification of Diseases, Tenth Revision (ICD\u201310). Categories of injury intent and injury mechanism generally follow the categories in the external-cause-of-injury mortality matrix (1,2). Cause-of-death statistics are based on the underlying cause of death.\r\n\r\nSOURCES\r\n\r\nCDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\r\n\r\nREFERENCES \r\n\r\n1. National Center for Health Statistics. ICD\u201310: External cause of injury mortality matrix.\r\n\r\n2. National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.\r\n\r\n3. Murphy SL, Xu JQ, Kochanek KD, Curtin SC, and Arias E. Deaths: Final data for 2015. National vital statistics reports; vol 66. no. 6. Hyattsville, MD: National Center for Health Statistics. 2017. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_06.pdf.\r\n\r\n4. Mini\u00f1o AM, Anderson RN, Fingerhut LA, Boudreault MA, Warner M. Deaths: Injuries, 2002. National vital statistics reports; vol 54 no 10. Hyattsville, MD: National Center for Health Statistics. 2006.",
-            "title": "NCHS - Injury Mortality: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1546,85 +1527,88 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/nt65-c7a7",
+            "issued": "2016-10-20",
+            "keyword": [
+                "injury",
+                "mortality",
+                "nchs",
+                "united states"
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
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Injury Mortality: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/2epp-ybzx",
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
-            "identifier": "56d78962-1395-5e57-a336-b485a630f390",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard STATE vCORESET.1.1-test (coreset-local)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/STATE.csv",
-                    "description": "Scorecard STATE vCORESET.1.1-test (coreset-local)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard STATE vCORESET.1.1-test (coreset-local)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/CORESET.1.1-test/20240430/STATE.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard STATE vCORESET.1.1-test (coreset-local)"
                 }
             ],
+            "identifier": "56d78962-1395-5e57-a336-b485a630f390",
+            "issued": "2024-05-08",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/2epp-ybzx",
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
+            "title": "Scorecard STATE vCORESET.1.1-test (coreset-local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/binw-6h77",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-10-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-30",
-            "keyword": [
-                "vision"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC Info",
                 "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/binw-6h77",
             "description": "The Department of Defense Health Agency\u2019s (DHA) Vision Center of Excellence (VCE) analyzed data from the MHS MART database on behalf of the VEHSS project.  MHS MART is a data management and reporting system used to support decision-making, health care analysis, and operational reporting. MART integrates various sources within MHS to provide a centralized repository for health care data, facilitating access to information that aids in managing health care services, resources, and performance across MHS.\n\nData are based on claims and encounter records in the MHS Management Analysis and Reporting Tool (MART) database. The population includes all active-duty and retired military members and their dependents in the MHS. The sample size is approximately 9.08 million persons.\n\nThese data are also available in the VEHSS Data Explorer, an interactive data visualization tool reporting prevalence information from more than 10 data sources: https://www.cdc.gov/vision-health-data/index.html",
-            "title": "Military Health System (MHS) - Vision and Eye Health Surveillance System (VEHSS)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1647,50 +1631,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/binw-6h77",
+            "issued": "2024-10-28",
+            "keyword": [
+                "vision"
+            ],
+            "landingPage": "https://data.cdc.gov/d/binw-6h77",
             "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2024-10-30",
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
+            "title": "Military Health System (MHS) - Vision and Eye Health Surveillance System (VEHSS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-19",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
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
-            "identifier": "https://data.cdc.gov/api/views/ikd3-vynf",
             "description": "Deaths involving coronavirus disease 2019 (COVID-19) reported to NCHS by jurisdiction of occurrence, week, and age group.",
-            "title": "AH Provisional COVID-19 Deaths by Week and Age",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1713,42 +1686,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/ikd3-vynf",
+            "issued": "2021-05-19",
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
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Week and Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/v2k9-ctv4",
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
-            "identifier": "https://data.cdc.gov/api/views/v2k9-ctv4",
             "description": "This dataset includes deidentified data on patients receiving artesunate through the National Artesunate for Severe Malaria Program from April- December 2019. \n\nThis dataset contains microscopy data only.\nPlease see the links below for the other datasets and the attached document 'Guide to NASMP Datasets:\nData from Case Report Form- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Cas/igaz-icki\nData on Artesunate Dosing- https://data.cdc.gov/dataset/National-Artesunate-for-Severe-Malaria-Program-Art/qan4-gt4k\nData on Follow-On Dosing- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Fol/g3k9-gyw7\n\nAll data can be easily linked using the ParticipantID field, a unique ID number assigned to each participant.",
-            "title": "National Artesunate for Severe Malaria Program Microscopy Data- April to December 2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1771,40 +1753,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/v2k9-ctv4",
+            "issued": "2020-04-10",
+            "keyword": [
+                "artesunate",
+                "division of parasitic diseases and malaria",
+                "malaria"
+            ],
+            "landingPage": "https://data.cdc.gov/d/v2k9-ctv4",
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
+            "title": "National Artesunate for Severe Malaria Program Microscopy Data- April to December 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/2far-xqbh",
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
-            "identifier": "d371b0f4-db36-56f0-8aab-8f8ecb2b66e7",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 1998",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1812,63 +1795,89 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "d371b0f4-db36-56f0-8aab-8f8ecb2b66e7",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/2far-xqbh",
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
+            "title": "State Drug Utilization Data 1998"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/2feh-qqv7",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2014-09-12",
-            "keyword": [
-                "web modules"
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
-            "identifier": "8DFE05EA-9FA0-4DB8-B803-D3AA70564592",
             "description": "This system shares public data that can be downloaded.",
-            "title": "CFSAN Web Modules",
-            "programCode": [
-                "009:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "description": "This system shares public data that can be downloaded.  ",
                     "downloadURL": "http://www.accessdata.fda.gov/scripts/fdcc/",
-                    "mediaType": "text/html",
-                    "description": "This system shares public data that can be downloaded.  "
+                    "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "8DFE05EA-9FA0-4DB8-B803-D3AA70564592",
+            "issued": "2021-02-25",
+            "keyword": [
+                "web modules"
+            ],
+            "landingPage": "https://healthdata.gov/d/2feh-qqv7",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2014-09-12",
+            "programCode": [
+                "009:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "CFSAN Web Modules"
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
@@ -1881,64 +1890,42 @@
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
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-07-03",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
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
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-            "landingPage": "https://data.cdc.gov/d/235m-gsry",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pathology and Physiology Branch, Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/235m-gsry",
             "description": "Additive manufacturing (AM) is a broad manufacturing term that encompasses a range of processes that create objects by adding material through a computer-aided design model.  Three-dimensional (3D) printing is a form of AM, which builds objects layer-by-layer deposition of feedstock material using a 3D printer machine and computer software.  Fused filament fabrication (FFF, also known as Filament Freeform Fabrication) is one 3D printing process in which filaments are melted and extruded from a heated nozzle to deposit material.  FFF is an emerging technology and one of the most popular additive manufacturing processes, especially for consumers and small manufacturers.  Polycarbonate (PC) is a versatile material and PC filaments are widely used for fused filament fabrication 3D printing.  PC filaments are often loaded with additives to achieve different properties of the print objects.  These additives range from dyes, organometallic compounds, carbon nanomaterials, nanometal oxides to micrometer-scale particles such as copper, bronze, steel, tungsten, gold, and aluminum nitride (Vance et al., 2017).   Several engineered nanomaterials were infused into PC filaments, such as silicon dioxide nanoparticles, titanium nitride nanoparticles (Vidakis et al., 2021), titanium carbide nanopowder (Vidakis et al., 2022a), aluminum nitride nanoparticles (Vidakis et al., 2022b), and carbon nanotubes (Potter et al., 2021).\n\nDuring heating, PC filament undergoes thermal degradation and releases fine particles (0.1 to 2.5 um) and incidental nanoparticles (d < 100 nm) as well as numerous volatile, and semi-volatile organic compounds that are likely derived from PC polymer and additives in the polymer (Azimi et al., 2016; Byrley et al., 2020; Gu et al., 2019; Stefaniak et al., 2017; Stefaniak et al., 2019; Alijagic et al., 2022; Tedla et al., 2022).   These emissions could pose a potential hazard to human health.  Currently, the potential health hazard of PC filament printing emissions has not been determined.\n\nA NIOSH research group used a condensation nuclei counter to study PC filament emission rates, and determined that the number-based particle emission rates from an industrial-scale material extrusion AM machine were around 2.2 x1011 number/minute and the total volatile organic compound emission rates were around 1.9 x 104 \u00b5g/minute (Stefaniak et al., 2019).  The same group also found low levels of acetone, benzene, toluene, and m,p-xylene during PC filament printing processes.  Potter et al showed that PC filament emissions contained bisphenol A (BPA), phenol, chlorobenzene, DEHP, and di-tert-butylphenol (Potter et al., 2019).  In our previous studies on PC filament printer emission-induced cell toxicity (Farcas et al., 2019), emissions from a commercial PC 3D printer were generated in a chamber using a 3D printer and collected in cell culture medium.  The number-based size distribution of the particles inside the chamber was between 140-170 nm and the mean particle sizes in cell culture medium were 201\u00b118 nm.  Analysis of elemental composition of particles collected in the cell culture medium found C, O, Ca, Na, Si, Ni, Cr, Fe, S, Al, and Cl.  The organic compounds in the emission collection cell culture medium were BPA, p-isopropenylphenol, and phenol.  At 24 h post-exposure, PC emissions were internalized in human small airway epithelial cells (SAEC) and induced a dose-dependent cytotoxicity, oxidative stress, apoptosis, necrosis, and increases in pro-inflammatory cytokine and chemokine production in SAEC (Farcas et al., 2019).  The results demonstrated that PC filament 3D printing emissions induce a cellular toxicity in SAEC.\n\nAlthough cell-based in vitro toxicity analysis is increasingly applied to screen and rank chemicals for prioritizing toxicity studies, as well as to study toxic mechanisms, the toxicological significance of in vitro study-generated data in hazard and risk assessment is limited.  In comparison with animal-based in",
-            "title": "Pulmonary evaluation of whole-body inhalation exposure of polycarbonate (PC) filament 3D printer emissions in rats",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1946,48 +1933,41 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/235m-gsry",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/235m-gsry",
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
+            "title": "Pulmonary evaluation of whole-body inhalation exposure of polycarbonate (PC) filament 3D printer emissions in rats"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/structure/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "computational biology",
-                "dataset",
-                "macromolecules",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/b58i-eyqq",
             "description": "Three dimensional structures provide a wealth of information on the biological function and the evolutionary history of macromolecules. They can be used to examine sequence-structure-function relationships, interactions, active sites, and more.",
-            "title": "Structure - Molecular Modeling Database (MMDB)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/structure/",
-                    "description": "Experimentally resolved structures of proteins, RNA, and DNA, derived from the Protein Data Bank (PDB), with value-added features such as explicit chemical graphs, computationally identified 3D domains (compact substructures) that are used to identify similar 3D structures, as well as links to literature, similar sequences, information about chemicals bound to the structures, and more. These connections make it possible, for example, to find 3D structures for homologs of a protein sequence of interest, then interactively view the sequence-structure relationships, active sites, bound chemicals, journal articles, and more.",
                     "@type": "dcat:Distribution",
+                    "description": "Experimentally resolved structures of proteins, RNA, and DNA, derived from the Protein Data Bank (PDB), with value-added features such as explicit chemical graphs, computationally identified 3D domains (compact substructures) that are used to identify similar 3D structures, as well as links to literature, similar sequences, information about chemicals bound to the structures, and more. These connections make it possible, for example, to find 3D structures for homologs of a protein sequence of interest, then interactively view the sequence-structure relationships, active sites, bound chemicals, journal articles, and more.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/structure/",
+                    "mediaType": "text/html",
                     "title": "Molecular Modeling Database (MMDB) query interface"
                 },
                 {
@@ -1997,39 +1977,42 @@
                     "title": "Download Molecular Modeling Database (MMDB) Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/b58i-eyqq",
+            "issued": "2022-02-08",
+            "keyword": [
+                "computational biology",
+                "dataset",
+                "macromolecules",
+                "protein",
+                "tools & utilities"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/structure/",
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
+            "title": "Structure - Molecular Modeling Database (MMDB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/h6kq-aiu7",
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
-            "identifier": "https://data.cdc.gov/api/views/h6kq-aiu7",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Quitline Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2037,49 +2020,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h6kq-aiu7",
+            "issued": "2015-02-20",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/h6kq-aiu7",
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
                 "Quitline"
-            ]
+            ],
+            "title": "Quitline Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-physician-non-physician-practitioner-supplier",
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
-                "medical suppliers & equipment",
-                "medicare",
-                "national",
-                "original medicare",
-                "physicians & practitioners",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/5d40af0b-17a7-4f03-b0bb-bee1aa815d73/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare Physician, Non-Physician Practitioner and Supplier tables provide use and payment data for physicians, other practitioners, limited-licensed practitioners, and durable medical equipment, prosthetic, and orthotic (DMEPOS) suppliers.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR PHYSSUPP 1. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization, Program Payments, Cost Sharing, and Balance Billing for Original Medicare Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR PHYSSUPP 2. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization, Program Payments, Cost Sharing, and Balance Billing for Original Medicare Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR PHYSSUPP 3. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization, Program Payments, Cost Sharing, and Balance Billing for Original Medicare Beneficiaries, by Area of Residence\n\tMDCR PHYSSUPP 4. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization, Program Payments, and Balance Billing for Original Medicare Beneficiaries, by Type of Service\n\tMDCR PHYSSUPP 5. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization, Program Payments, and Balance Billing for Original Medicare Beneficiaries, by Place of Service\n\tMDCR PHYSSUPP 6. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization, Program Payments, and Balance Billing for Original Medicare Beneficiaries, by Physician Specialty\n\tMDCR PHYSSUPP 7. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Berenson-Eggers Type of Service (BETOS) Classification",
-            "title": "CMS Program Statistics - Medicare Physician, Non-Physician Practitioner & Supplier",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2136,48 +2112,52 @@
                     "title": "CMS Program Statistics - Medicare Physician, Non-Physician Practitioner & Supplier : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/5d40af0b-17a7-4f03-b0bb-bee1aa815d73/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medical suppliers & equipment",
+                "medicare",
+                "national",
+                "original medicare",
+                "physicians & practitioners",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-physician-non-physician-practitioner-supplier",
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
+            "title": "CMS Program Statistics - Medicare Physician, Non-Physician Practitioner & Supplier"
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
@@ -2185,52 +2165,51 @@
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
+            "title": "Going Smokefree Matters - Multiunit Housing Infographic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-physician-other-practitioners-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-physician-other-practitioners-by-provider-and-service-data-dictionary",
             "description": "The Medicare Physician & Other Practitioners by Provider and Service dataset provides information on use, payments, and submitted charges organized by National Provider Identifier (NPI), Healthcare Common Procedure Coding System (HCPCS) code, and place of service.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Medicare Physician & Other Practitioners - by Provider and Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Physician & Other Practitioners - by Provider and Service : 2022-12-01"
                 },
                 {
@@ -2354,44 +2333,50 @@
                     "title": "Medicare Physician & Other Practitioners - by Provider and Service : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-physician-other-practitioners-by-provider-and-service-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "original medicare",
+                "physicians & practitioners"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service",
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
+                "https://data.cms.gov/resources/medicare-physician-other-practitioners-methodology"
+            ],
+            "temporal": "2013-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Physician & Other Practitioners - by Provider and Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/2j5w-7sj3",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-06-22",
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
-            "identifier": "8483cef4-972a-4c39-8290-c9d19bead88d",
             "description": "Dataset.",
-            "title": "2020 Managed Care Programs By State",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2399,39 +2384,36 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "8483cef4-972a-4c39-8290-c9d19bead88d",
+            "issued": "2022-06-22",
+            "keyword": [
+                "medicaid"
+            ],
+            "landingPage": "https://healthdata.gov/d/2j5w-7sj3",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-06-13",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "2020 Managed Care Programs By State"
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
-            "keyword": [
-                "osh",
-                "sae",
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
-            "identifier": "https://data.cdc.gov/api/views/ezab-8sq5",
+            "describedBy": "https://chronicdata.cdc.gov/Health-Consequences-and-Costs/Smoking-Attributable-Mortality-Morbidity-and-Econo/ezab-8sq5",
             "description": "2005-2009. SAMMEC - Smoking-Attributable Mortality, Morbidity, and Economic Costs. Smoking-attributable expenditures (SAEs) are excess health care expenditures attributable to cigarette smoking by type of service among adults ages 19 years of age and older.",
-            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Expenditures (SAE)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2454,21 +2436,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Health-Consequences-and-Costs/Smoking-Attributable-Mortality-Morbidity-and-Econo/ezab-8sq5",
+            "identifier": "https://data.cdc.gov/api/views/ezab-8sq5",
+            "issued": "2023-07-18",
+            "keyword": [
+                "osh",
+                "sae",
+                "sammec",
+                "tobacco"
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
                 "Health Consequences and Costs"
-            ]
+            ],
+            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Expenditures (SAE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-2001",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. Respondents are also asked about personal and family income<br />\nsources and amounts, health care access and coverage, illegal<br />\nactivities and arrest record, problems resulting from the use of<br />\ndrugs, and needle-sharing. Questions introduced in previous NHSDA<br />\nadministrations were retained in the 2001 survey, including questions<br />\nasked only of respondents aged 12 to 17. These \"youth experiences\"<br />\nitems covered a variety of topics, such as neighborhood environment,<br />\nillegal activities, gang involvement, drug use by friends, social<br />\nsupport, extracurricular activities, exposure to substance abuse<br />\nprevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Also retained were<br />\nquestions on mental health and access to care, perceived risk of using<br />\ndrugs, perceived availability of drugs, driving behavior and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey and have been retained<br />\nthrough the 2001 survey. Demographic data include gender, race, age,<br />\nethnicity, marital status, educational level, job status, veteran<br />\nstatus, and current household composition. In addition, in 2001 questions on purchase of marijuana were added.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-2001) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2001-nid13525",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2001-nid13525"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2001-nid13525",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "addiction",
                 "alcohol",
@@ -2500,60 +2513,30 @@
                 "substance abuse treatment",
                 "tranquilizers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-2001",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2001-nid13525",
-            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. Respondents are also asked about personal and family income<br />\nsources and amounts, health care access and coverage, illegal<br />\nactivities and arrest record, problems resulting from the use of<br />\ndrugs, and needle-sharing. Questions introduced in previous NHSDA<br />\nadministrations were retained in the 2001 survey, including questions<br />\nasked only of respondents aged 12 to 17. These \"youth experiences\"<br />\nitems covered a variety of topics, such as neighborhood environment,<br />\nillegal activities, gang involvement, drug use by friends, social<br />\nsupport, extracurricular activities, exposure to substance abuse<br />\nprevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Also retained were<br />\nquestions on mental health and access to care, perceived risk of using<br />\ndrugs, perceived availability of drugs, driving behavior and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey and have been retained<br />\nthrough the 2001 survey. Demographic data include gender, race, age,<br />\nethnicity, marital status, educational level, job status, veteran<br />\nstatus, and current household composition. In addition, in 2001 questions on purchase of marijuana were added.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-2001)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2001-nid13525",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-2001) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-2001-nid13525"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-2001)"
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
-            "identifier": "https://data.cdc.gov/api/views/jfbs-8cpp",
             "description": "The Overview of Health Disparities analysis is a component of the Healthy People 2020 (HP2020) Final Review. The analysis included 611 objectives in HP2020. See Technical Notes for the Healthy People 2020 Overview of Health Disparities (https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities.htm) for additional information and criteria for objectives, data years, and population characteristics included in the analysis and statistical formulas and definitions for the disparities measures. \n\nThis file contains estimates and standard errors for the baseline and final years for individual population groups used in the Overview of Health Disparities analysis. The number and definitions of population groups varied across the HP2020 objectives and data sources used. These population groups are shown in the disparities file as originally reported by the data source, rather than the harmonized categories that were used for the HP2020 Progress by Population Group analysis (https://www.cdc.gov/nchs/healthy_people/hp2020/population-groups.htm). Additionally, for any given objective, the baseline and final years used for the disparities analysis do not necessarily correspond to the baseline and final years used to evaluate progress toward target attainment in the HP2020 Final Review Progress Table (https://www.cdc.gov/nchs/healthy_people/hp2020/progress-tables.htm) and Progress by Population Group analysis (https://www.cdc.gov/nchs/healthy_people/hp2020/population-groups.htm). These distinctions should be considered when merging the downloadable Progress Table or Progress by Population Group data files with the Overview of Health Disparities data files, or when integrative analyses that incorporate both disparities and progress data are conducted.  \n    \nData for additional years during the HP2020 tracking period that are not included in the Overview of Health Disparities are available on the HP2020 website (https://www.healthypeople.gov/2020/).",
-            "title": "Population Group Estimates used in the Healthy People 2020 Overview of Health Disparities",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2576,45 +2559,44 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/jfbs-8cpp",
+            "issued": "2022-03-09",
+            "keyword": [
+                "health disparities",
+                "healthy people 2020"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities.htm",
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
+            "temporal": "1997-01-01/2018-12-31",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Population Group Estimates used in the Healthy People 2020 Overview of Health Disparities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qan4-gt4k",
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
-            "identifier": "https://data.cdc.gov/api/views/qan4-gt4k",
             "description": "This dataset includes deidentified data on patients receiving artesunate through the National Artesunate for Severe Malaria Program from April- December 2019. \n\nThis dataset contains artesunate dosing data only.\nPlease see the links below for the other datasets and the attached word document, 'Guide to NASMP Datasets':\n\nData from Case Report- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Cas/igaz-icki\n\nData on Follow-On Antimalarial Dosing- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Fol/g3k9-gyw7\n\nData on Microscopy (Parasitemia values)- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Mic/v2k9-ctv4\n\nAll data can be easily linked using the ParticipantID field, a unique ID number assigned to each participant.",
-            "title": "National Artesunate for Severe Malaria Program Artesunate Dosing Data- April to December 2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2637,108 +2619,89 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qan4-gt4k",
+            "issued": "2020-04-10",
+            "keyword": [
+                "artesunate",
+                "division of parasitic diseases and malaria",
+                "malaria"
+            ],
+            "landingPage": "https://data.cdc.gov/d/qan4-gt4k",
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
+            "title": "National Artesunate for Severe Malaria Program Artesunate Dosing Data- April to December 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/2mdq-v3d3",
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
-            "identifier": "6c64c58e-34fe-59bb-9d32-dcbbe8f49d13",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_states_measures_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures_download.csv",
-                    "description": "{\"dataset\": \"states_measures_download\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"states_measures_download\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures_download.csv",
+                    "mediaType": "text/csv",
                     "title": "states_measures_download csv file"
                 }
             ],
+            "identifier": "6c64c58e-34fe-59bb-9d32-dcbbe8f49d13",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/2mdq-v3d3",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
-            "theme": [
-                "Uncategorized"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/prams/index.htm",
-            "bureauCode": [
-                "009:20"
+            "modified": "2024-11-07",
+            "programCode": [
+                "009:000"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-05",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
             "references": [
-                "https://www.cdc.gov/prams/index.htm",
-                "https://www.cdc.gov/prams/pramstat/index.html"
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
             ],
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
+            "theme": [
+                "Uncategorized"
+            ],
+            "title": "prodAuto_states_measures_download"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DRH Public Inquiries",
                 "hasEmail": "mailto:PRAMSProposals@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/4ya2-fkvt",
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2008/4ya2-fkvt",
             "description": "2008. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2008",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2761,48 +2724,60 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2008/4ya2-fkvt",
+            "identifier": "https://data.cdc.gov/api/views/4ya2-fkvt",
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
+            "title": "CDC PRAMStat Data for 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5hvx-krph",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/5hvx-krph",
             "description": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 years, Confirmed to Legionellosis - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
-            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, Age<5 years, Confirmed to Legionellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2825,46 +2800,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5hvx-krph",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
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
+            "landingPage": "https://data.cdc.gov/d/5hvx-krph",
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
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, Age<5 years, Confirmed to Legionellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/nr42-fsyk",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/nr42-fsyk",
             "description": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2887,43 +2863,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/nr42-fsyk",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "dengue",
+                "dengue-like illness",
+                "dengue virus infections",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe dengue",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/nr42-fsyk",
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
+            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/radlex",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-04-13",
-            "temporal": "2006-01-01T00:00:00-05:00/2006-11-15T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "biomedical research",
-                "health informatics",
-                "health it",
-                "imaging",
-                "radiology"
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
-            "identifier": "3c4eddf8-7c83-436a-9f48-5304d84d318b",
+            "dataQuality": true,
+            "describedBy": "http://radlex.org/",
             "description": "<p>RadLex is a controlled terminology for radiology and serves as a single unified source of radiology terms for radiology practice, education, and research. RadLex is a comprehensive lexicon for standardized indexing and retrieval of radiology information resources. With more than 30,000 terms, RadLex satisfies the needs of software developers, system vendors and radiology users by adopting the best features of existing terminology systems while producing new terms to fill critical gaps. RadLex also provides a comprehensive and technology-friendly replacement for the ACR Index for Radiological Diagnoses. It unifies and supplements other lexicons and standards, such as SNOMED-CT, LOINC, and DICOM. As images, image reports, and medical records continue to move online RadLex meets the need of physicians to organize and retrieve image data using a common set of terms.&#13;<br />\n&#13;<br />\nRadReport is a radiology reporting initiative that is a part of RadLex. RadReport aims to improve reporting practices by creating a library of clear and consistent report templates.  Report templates and information about RadReport is available at the link in Resource 2.&#13;<br />\n&#13;</p>",
-            "title": "RadLex",
-            "programCode": [
-                "009:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2938,47 +2919,43 @@
                     "title": "Query Tool "
                 }
             ],
-            "describedBy": "http://radlex.org/",
-            "dataQuality": true,
+            "identifier": "3c4eddf8-7c83-436a-9f48-5304d84d318b",
+            "issued": "2013-04-13",
+            "keyword": [
+                "biomedical research",
+                "health informatics",
+                "health it",
+                "imaging",
+                "radiology"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/radlex",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
+            },
+            "temporal": "2006-01-01T00:00:00-05:00/2006-11-15T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "RadLex"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xuah-ug7z",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
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
-            "identifier": "https://data.cdc.gov/api/views/xuah-ug7z",
             "description": "NNDSS - Table II. Babesiosis to Campylobacteriosis - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.\r\n \r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3001,46 +2978,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xuah-ug7z",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "babesiosis",
+                "campylobacteriosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xuah-ug7z",
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
+            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qwf3-87ny",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
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
-            "identifier": "https://data.cdc.gov/api/views/qwf3-87ny",
             "description": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified) - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1E. Botulism, Foodborne to Botulism, Other",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3063,40 +3039,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qwf3-87ny",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/qwf3-87ny",
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
+            "title": "NNDSS - TABLE 1E. Botulism, Foodborne to Botulism, Other"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jkmz-c8jz",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-12",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "community mitigation",
-                "covid-19",
-                "school closure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nicole Zviedrite",
                 "hasEmail": "mailto:jmu6@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/jkmz-c8jz",
             "description": "Data on distance learning and supplemental feeding programs were collected from a stratified sample of 600 school districts. School districts were divided into quartiles based on the percentage of students eligible for free/reduced-price lunch, an indicator of family economic status, as reported by the National Center for Education Statistics (https://nces.ed.gov/ccd/). A simple random sample was taken in each stratum, and sample size per stratum was calculated using 95% confidence interval of 50% \u00b1 10%. Data on the availability and method of delivery of both distance learning and supplemental feeding programs were collected from publicly available announcements on school district websites and their official social media pages (Facebook, Twitter). Google searches were performed for news resources when information was not available from online district sources.",
-            "title": "Efforts to sustain education and subsidized meal programs during COVID-19-related school closures, United States, March-June 2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3119,55 +3101,85 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jkmz-c8jz",
+            "issued": "2022-01-12",
+            "keyword": [
+                "community mitigation",
+                "covid-19",
+                "school closure"
+            ],
+            "landingPage": "https://data.cdc.gov/d/jkmz-c8jz",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-01-12",
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
+            "title": "Efforts to sustain education and subsidized meal programs during COVID-19-related school closures, United States, March-June 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.rcsb.org/pdb/home/home.do",
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
                 "fn": "PREUSCH, PETER\u00a0",
                 "hasEmail": "mailto:preuschp@nigms.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "d9f3932a-9c55-41b3-ad3a-0b4e18ee4752",
+            "dataQuality": true,
             "description": "<p>The Protein Data Bank (PDB) archive is the single worldwide repository of information about the 3D structures of large biological molecules, including proteins and nucleic acids found in all organisms including bacteria, yeast, plants, flies, other animals, and humans.</p>",
-            "title": "Protein Data Bank (PDB)",
+            "identifier": "d9f3932a-9c55-41b3-ad3a-0b4e18ee4752",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.rcsb.org/pdb/home/home.do",
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
+            "title": "Protein Data Bank (PDB)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/dhcs/prelim-hc-visits/index.htm",
+            "accrualPeriodicity": "R/P6M",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "https://www.cdc.gov/nchs/dhcs/prelim-hc-visits/index.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component, conducted by the National Center for Health Statistics (NCHS), collects annual data on visits to health centers to describe patterns of utilization and provision of ambulatory care delivery in the United States. Health centers are local clinics that are community-based and provide comprehensive health care services to populations that are often vulnerable and underserved. Health centers are either federally qualified health centers (FQHCs), which receive federal funding from the Health Resources and Services Administration (HRSA), or FQHC look-alikes, which meet HRSA requirements but do not receive HRSA funding.\n\nThis visualization depicts preliminary, biannual counts and rates of health center visits from January 2022-June 2023 by medical diagnosis chapters, stratified by selected patient characteristics. This visualization also depicts measures related to maternal health care at health centers to help expand the availability of data related to maternal health and maternal morbidity.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Data is updated biannually.",
+                    "downloadURL": "https://www.cdc.gov/nchs/dhcs/prelim-hc-visits/index.htm",
+                    "mediaType": "text/html",
+                    "title": "Preliminary Estimates for NAMCS Health Center Component"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/55k8-ajvf",
             "issued": "2024-07-24",
-            "@type": "dcat:Dataset",
-            "temporal": "January 2022-June 2023",
-            "modified": "2024-07-24",
             "keyword": [
                 "ambulatory-care",
                 "health center",
@@ -3176,68 +3188,36 @@
                 "namcs",
                 "reproductive health"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/dhcs/prelim-hc-visits/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-07-24",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/55k8-ajvf",
-            "description": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component, conducted by the National Center for Health Statistics (NCHS), collects annual data on visits to health centers to describe patterns of utilization and provision of ambulatory care delivery in the United States. Health centers are local clinics that are community-based and provide comprehensive health care services to populations that are often vulnerable and underserved. Health centers are either federally qualified health centers (FQHCs), which receive federal funding from the Health Resources and Services Administration (HRSA), or FQHC look-alikes, which meet HRSA requirements but do not receive HRSA funding.\n\nThis visualization depicts preliminary, biannual counts and rates of health center visits from January 2022-June 2023 by medical diagnosis chapters, stratified by selected patient characteristics. This visualization also depicts measures related to maternal health care at health centers to help expand the availability of data related to maternal health and maternal morbidity.",
-            "title": "National Ambulatory Medical Care Survey, Health Center Component, Preliminary Estimates dashboard",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/dhcs/prelim-hc-visits/index.htm",
-                    "description": "Data is updated biannually.",
-                    "@type": "dcat:Distribution",
-                    "title": "Preliminary Estimates for NAMCS Health Center Component"
-                }
-            ],
+            "rights": "https://www.cdc.gov/nchs/dhcs/prelim-hc-visits/index.htm",
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P6M",
+            "temporal": "January 2022-June 2023",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey, Health Center Component, Preliminary Estimates dashboard"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK501922/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "consumer health",
-                "data distribution",
-                "dataset",
-                "environmental health",
-                "toxicology"
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/r48h-qc9c",
             "description": "LactMed (Drugs and Lactation Database) contains information on drugs and other chemicals to which breastfeeding mothers may be exposed. It includes information on the levels of such substances in breast milk and infant blood, and the possible adverse effects in the nursing infant. Suggested therapeutic alternatives to those drugs are provided, where appropriate.",
-            "title": "LactMed (Drugs and Lactation Database)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3252,28 +3232,61 @@
                     "title": "Download LactMed Data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ftp.nlm.nih.gov/projects/lactmedlease/",
-                    "description": "These previous versions of LactMed data are no longer updated and are for research and development purposes only.",
                     "@type": "dcat:Distribution",
+                    "description": "These previous versions of LactMed data are no longer updated and are for research and development purposes only.",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/lactmedlease/",
+                    "mediaType": "text/html",
                     "title": "Download LactMed Data 2015-2019"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/r48h-qc9c",
+            "issued": "2020-09-18",
+            "keyword": [
+                "consumer health",
+                "data distribution",
+                "dataset",
+                "environmental health",
+                "toxicology"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK501922/",
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
                 "Consumer Health"
-            ]
+            ],
+            "title": "LactMed (Drugs and Lactation Database)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-mortality-multiple-cause-death-0",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/mcd.html",
+            "description": "<p>The Mortality - Multiple Cause of Death data on CDC WONDER are county-level national mortality and population data spanning the years 1999-2006. These data are available in two separate data sets: one data set for years 1999-2004 with 3 race groups, and another data set for years 2005-2006 with 4 race groups and 3 Hispanic origin categories. Data are based on death certificates for U.S. residents. Each death certificate contains a single underlying cause of death, up to twenty additional multiple causes, and demographic data. The number of deaths, crude death rates,  age-adjusted death rates, standard errors and 95% confidence intervals for death rates can be obtained by place of residence (total U.S., state, and county), age group (including infants), race, Hispanic ethnicity (years 2005-2006 only), gender, year of death, and cause-of-death (4-digit ICD-10 code or group of codes). The data are produced by the National Center for Health Statistics.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/mcd.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "43857256-b635-456e-84b2-ec722454326d",
             "issued": "2012-05-30",
-            "temporal": "1999-01-01T00:00:00-05:00/2006-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "age",
                 "births",
@@ -3293,75 +3306,38 @@
                 "state",
                 "urbanization"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-mortality-multiple-cause-death-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "43857256-b635-456e-84b2-ec722454326d",
-            "description": "<p>The Mortality - Multiple Cause of Death data on CDC WONDER are county-level national mortality and population data spanning the years 1999-2006. These data are available in two separate data sets: one data set for years 1999-2004 with 3 race groups, and another data set for years 2005-2006 with 4 race groups and 3 Hispanic origin categories. Data are based on death certificates for U.S. residents. Each death certificate contains a single underlying cause of death, up to twenty additional multiple causes, and demographic data. The number of deaths, crude death rates,  age-adjusted death rates, standard errors and 95% confidence intervals for death rates can be obtained by place of residence (total U.S., state, and county), age group (including infants), race, Hispanic ethnicity (years 2005-2006 only), gender, year of death, and cause-of-death (4-digit ICD-10 code or group of codes). The data are produced by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Mortality - Multiple Cause of Death",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://wonder.cdc.gov/mcd.html",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/mcd.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "1999-01-01T00:00:00-05:00/2006-12-31T00:00:00-05:00",
             "theme": [
                 "Health",
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Mortality - Multiple Cause of Death"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-advantage-physician-non-physician-practitioner-supplier",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2024-05-17",
-            "temporal": "2016-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-16",
-            "references": [
-                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
-                "medical suppliers & equipment",
-                "medicare",
-                "medicare advantage",
-                "national",
-                "physicians & practitioners",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/900059a0-0a10-4f2f-8c3d-d8da432a421e/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics \u2013 Medicare Advantage, Physician, Non-Physician Practitioner and Supplier tables provide utilization data for physician, non-physician practitioners, and suppliers, by Medicare Advantage beneficiaries.\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\nBelow is the list of tables:\n\n\n\tMDCR PHYSSUPP MA 1. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: Utilization for Medicare Advantage Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR PHYSSUPP MA 2. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: Utilization for Medicare Advantage Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR PHYSSUPP MA 3. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: Utilization for Medicare Advantage Beneficiaries, by Area of Residence\n\tMDCR PHYSSUPP MA 4. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization for Medicare Advantage Beneficiaries, by Place of Service\n\tMDCR PHYSSUPP MA 5. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization for Medicare Advantage Beneficiaries, by Restructured BETOS Classification System",
-            "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3400,45 +3376,53 @@
                     "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2016-01-15"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/900059a0-0a10-4f2f-8c3d-d8da432a421e/data-viewer",
+            "issued": "2024-05-17",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medical suppliers & equipment",
+                "medicare",
+                "medicare advantage",
+                "national",
+                "physicians & practitioners",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-advantage-physician-non-physician-practitioner-supplier",
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
+            "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/2tf3-vhn2",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-04-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-11",
-            "keyword": [
-                "cms-64 expenditures",
-                "financial management report"
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
-            "identifier": "5b19d1d4-ae43-5fcd-ba14-3cecd99f473f",
             "description": "This dataset reports summary state-by-state total expenditures by program for the Medicaid Program, Medicaid Administration and CHIP programs. These state expenditures are tracked through the automated Medicaid Budget and Expenditure System/State Children's Health Insurance Program Budget and Expenditure System (MBES/CBES).\r\n\r\nFor more information, visit https://medicaid.gov/medicaid/finance/state-expenditure-reporting/expenditure-reports/index.html.",
-            "title": "Medicaid Financial Management Data",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3447,23 +3431,51 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "5b19d1d4-ae43-5fcd-ba14-3cecd99f473f",
+            "issued": "2018-04-10",
+            "keyword": [
+                "cms-64 expenditures",
+                "financial management report"
+            ],
+            "landingPage": "https://healthdata.gov/d/2tf3-vhn2",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-12-11",
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
+            "title": "Medicaid Financial Management Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://healthdata.gov/dataset/study-womens-health-across-nation-swan-public-use-data",
             "bureauCode": [
                 "009:00"
             ],
-            "rights": "N/A",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Alicia Colvin Greene",
+                "hasEmail": "mailto:swanaccess@edc.pitt.edu"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/253",
+            "description": "<p>The SWAN Public Use Datasets provide access to longitudinal data describing the physical, biological, psychological, and social changes that occur during the menopausal transition. Data collected from 3,302 SWAN participants from Baseline through the 10th Annual Follow-Up visit are currently available to the public.  Registered users are able to download datasets in a variety of formats, search variables and view recent publications.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.icpsr.umich.edu/web/ICPSR/series/253",
+                    "mediaType": "text/html",
+                    "title": "https://www.icpsr.umich.edu/web/ICPSR/series/253"
+                }
+            ],
+            "identifier": "fc814791-05e7-4b65-8feb-3767c722c361",
             "issued": "2015-03-04",
-            "@type": "dcat:Dataset",
-            "temporal": "2010-09-02T00:00:00-04:00/2011-11-22T00:00:00-05:00",
-            "modified": "2023-07-26",
             "keyword": [
                 "bone loss",
                 "cardiovascular disease",
@@ -3481,71 +3493,35 @@
                 "vasomotor symptoms",
                 "women s health"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Alicia Colvin Greene",
-                "hasEmail": "mailto:swanaccess@edc.pitt.edu"
-            },
+            "landingPage": "https://healthdata.gov/dataset/study-womens-health-across-nation-swan-public-use-data",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:048"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Institutes of Health (NIH)"
             },
-            "identifier": "fc814791-05e7-4b65-8feb-3767c722c361",
-            "description": "<p>The SWAN Public Use Datasets provide access to longitudinal data describing the physical, biological, psychological, and social changes that occur during the menopausal transition. Data collected from 3,302 SWAN participants from Baseline through the 10th Annual Follow-Up visit are currently available to the public.  Registered users are able to download datasets in a variety of formats, search variables and view recent publications.</p>",
-            "title": "Study of Womens Health Across the Nation (SWAN) Public Use Data",
-            "programCode": [
-                "009:048"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.icpsr.umich.edu/web/ICPSR/series/253",
-                    "mediaType": "text/html",
-                    "title": "https://www.icpsr.umich.edu/web/ICPSR/series/253"
-                }
-            ],
-            "describedBy": "http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/253",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "rights": "N/A",
+            "temporal": "2010-09-02T00:00:00-04:00/2011-11-22T00:00:00-05:00",
             "theme": [
                 "Health"
-            ]
+            ],
+            "title": "Study of Womens Health Across the Nation (SWAN) Public Use Data"
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
-            "identifier": "https://data.cdc.gov/api/views/uxgd-cqqc",
             "description": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States\n\n- Since 2019, CDC has been exploring use of data obtained from (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, food stores, and independent pharmacies) and physician medical offices. These data are being presented publicly for the first time this season; further evaluations of these data are underway.\n\n- The pharmacy data include flu vaccinations that were billed for (i.e. claims) or paid by cash. Medical office data are claims based.\n\n- The sampled pharmacies and physician medical offices and the captured volume of transactions represent approximately 92% and 82% of influenza vaccines administered nationally, respectively.\n\n- Vaccinations administered in other settings such as workplaces and community settings are not included in these data.\n\n- Weekly Number of Influenza Vaccinations Administered, in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States, Data Source(s): IQVIA Pharmacy and Physician Medical Office Claims.",
-            "title": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States (ARCHIVED)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3568,54 +3544,56 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/uxgd-cqqc",
+            "issued": "2022-09-28",
+            "keyword": [
+                "flu",
+                "influenza",
+                "iqvia",
+                "pharmacy vaccinations",
+                "physician medical office vaccinations",
+                "vaccine coverage"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
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
+                "IQVIA Pharmacy and Physician Medical Office Claims"
+            ],
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Weekly Cumulative Estimated Number of Influenza Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 18 years and older, United States (ARCHIVED)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/quality-of-care/medicare-dialysis-facilities",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2009-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-29",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-02/FY2024_DFR_Guide%20and%20Methodology.pdf"
-            ],
-            "keyword": [
-                "chronic conditions",
-                "end stage renal disease facilities",
-                "hospitals & facilities",
-                "medicare",
-                "original medicare",
-                "outpatient facilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ESRD Questions - CCSQ",
                 "hasEmail": "mailto:ESRDQuestions@cms.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Medicare & Medicaid Services"
-            },
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/f8610e87-ba25-43a3-a49e-927dbc8701ae/data-viewer",
-            "description": "The Medicare Dialysis Facilities data provides information on clinical and patient measures for Medicare-certified\u00a0ESRD\u00a0facilities, also known as dialysis facilities. It contains data on patient characteristics, treatment patterns, hospitalization, mortality, and transplantation patterns in Medicare-certified dialysis facilities.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Medicare Dialysis Facilities",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-02/FY2024%20Data%20Dictionary.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Medicare Dialysis Facilities data provides information on clinical and patient measures for Medicare-certified\u00a0ESRD\u00a0facilities, also known as dialysis facilities. It contains data on patient characteristics, treatment patterns, hospitalization, mortality, and transplantation patterns in Medicare-certified dialysis facilities.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f8610e87-ba25-43a3-a49e-927dbc8701ae/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f8610e87-ba25-43a3-a49e-927dbc8701ae/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Dialysis Facilities : 2024-01-01"
                 },
                 {
@@ -3745,53 +3723,50 @@
                     "title": "Medicare Dialysis Facilities : 2009-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2024-02/FY2024%20Data%20Dictionary.xlsx",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/f8610e87-ba25-43a3-a49e-927dbc8701ae/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "chronic conditions",
+                "end stage renal disease facilities",
+                "hospitals & facilities",
+                "medicare",
+                "original medicare",
+                "outpatient facilities"
+            ],
+            "landingPage": "https://data.cms.gov/quality-of-care/medicare-dialysis-facilities",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-02-29",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-02/FY2024_DFR_Guide%20and%20Methodology.pdf"
+            ],
+            "temporal": "2009-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Dialysis Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hwyq-75wu",
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
-            "identifier": "https://data.cdc.gov/api/views/hwyq-75wu",
             "description": "NNDSS - Table II. Salmonellosis to Shigellosis - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n$ Includes E. coli O157:H7, Shiga toxin-positive, serogroup non-O157, and Shiga toxin-positive, not serogrouped.",
-            "title": "NNDSS - Table II. Salmonellosis to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3814,35 +3789,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hwyq-75wu",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
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
+            "landingPage": "https://data.cdc.gov/d/hwyq-75wu",
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
+            "title": "NNDSS - Table II. Salmonellosis to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/v6bq-c4f3",
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
-            "identifier": "https://data.cdc.gov/api/views/v6bq-c4f3",
             "description": "Workers in a number of sectors including Transportation, Warehousing and Utilities, Construction, Agriculture, Forestry\u2019s and Fisheries and Mining are regularly exposed to whole-body vibration (WBV) while driving large transportation or earth moving vehicles or while using large vibrating tools such as chain saws or rock drills.  Exposure to WBV has been associated with an increased risk for neck and back pain.  However, the findings of other studies have suggested that occupational exposure to WBV may also serve as a risk factor for the development of a number of diseases such as cardiovascular disease and cancer.  In addition, it may result in pre-term births and preclampsia in women and interfere with normal reproductive physiology in both men and women.",
-            "title": "Effects of whole-body vibration on reproductive physiology in a rat model",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3850,45 +3837,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/v6bq-c4f3",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/v6bq-c4f3",
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
+            "title": "Effects of whole-body vibration on reproductive physiology in a rat model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/xna8-x7qg",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/xna8-x7qg",
             "description": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Since [INSERT DATE], XXX influenza-associated pediatric deaths occurring during the 2017-18 season have been reported.",
-            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3911,45 +3888,47 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xna8-x7qg",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "hepatitis c",
+                "influenza-associated pediatric mortality",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/xna8-x7qg",
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
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-census",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-05-30",
-            "temporal": "1970-01-01T00:00:00-05:00/2030-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "age",
-                "county",
-                "population statistics",
-                "race",
-                "sex",
-                "state",
-                "year"
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
-            "identifier": "4e273172-5ab5-4db6-bb27-573f15386778",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/population.html",
             "description": "<p>The Population online databases  contain data from the US Census Bureau.  The Census Estimates online database contains contains county-level population counts for years 1970 - 2000.  The data comprise the April 1st Census counts for years 1970, 1980, 1990 and 2000, the July 1st intercensal estimates for years 1971-1979 and 1981-1989, and the July 1st postcensal estimates for years 1991-1999.  The Census Projections online database contains population projections for years 2004-2030 by year, state, age, race and sex,  prodyced by teh Cenus Bureau in 2005. The data are produced by the United States Department of Commerce, U.S. Census Bureau, Population Division.</p>",
-            "title": "CDC WONDER: Population (from Census)",
-            "programCode": [
-                "006:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3958,42 +3937,46 @@
                     "title": "Query Tool "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/population.html",
-            "dataQuality": true,
+            "identifier": "4e273172-5ab5-4db6-bb27-573f15386778",
+            "issued": "2012-05-30",
+            "keyword": [
+                "age",
+                "county",
+                "population statistics",
+                "race",
+                "sex",
+                "state",
+                "year"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-population-census",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "006:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1970-01-01T00:00:00-05:00/2030-12-31T00:00:00-05:00",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Population (from Census)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://wwwdev.cdc.gov/nchs/rss/rapid-surveys-system.html",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-08-22",
-            "temporal": "2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-12",
-            "keyword": [
-                "dhis",
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
-            "identifier": "https://data.cdc.gov/api/views/p89x-xx88",
             "description": "The NCHS Rapid Surveys System includes questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes.",
-            "title": "NCHS Rapid Surveys System",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4016,54 +3999,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/p89x-xx88",
+            "issued": "2024-08-22",
+            "keyword": [
+                "dhis",
+                "nchs"
+            ],
+            "landingPage": "https://wwwdev.cdc.gov/nchs/rss/rapid-surveys-system.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-12-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Rapid Surveys System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-07-22",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-02-01/2020-07-18",
-            "modified": "2022-04-01",
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
-                "place of death",
-                "pneumonia",
-                "provisional",
-                "puerto rico",
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
-            "identifier": "https://data.cdc.gov/api/views/g4z9-a9d3",
             "description": "Deaths involving coronavirus disease 2019 (COVID-19) and pneumonia reported to NCHS by jurisdiction of occurrence, place of death, and age group.",
-            "title": "AH Cumulative Provisional COVID-19 Death Counts by Place of Death and Age Group from 2/1/2020 to 7/18/2020",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4086,54 +4056,63 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/g4z9-a9d3",
+            "issued": "2020-07-22",
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
+                "place of death",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
+                "state",
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
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2020-02-01/2020-07-18",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Cumulative Provisional COVID-19 Death Counts by Place of Death and Age Group from 2/1/2020 to 7/18/2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-physician-other-practitioners-methodology"
-            ],
-            "keyword": [
-                "health care use & payments",
-                "health equity",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/8889d81e-2ee7-448f-8713-f071038289b5/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-physician-other-practitioners-by-provider-data-dictionary",
             "description": "The Medicare Physician & Other Practitioners by Provider dataset provides information on\u00a0use, payments, submitted charges and beneficiary demographic and health characteristics organized by National Provider Identifier (NPI).\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
-            "title": "Medicare Physician & Other Practitioners - by Provider",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8889d81e-2ee7-448f-8713-f071038289b5/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8889d81e-2ee7-448f-8713-f071038289b5/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Physician & Other Practitioners - by Provider : 2022-12-01"
                 },
                 {
@@ -4257,46 +4236,49 @@
                     "title": "Medicare Physician & Other Practitioners - by Provider : 2013-12-16"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-physician-other-practitioners-by-provider-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/8889d81e-2ee7-448f-8713-f071038289b5/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "original medicare",
+                "physicians & practitioners"
+            ],
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider",
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
+                "https://data.cms.gov/resources/medicare-physician-other-practitioners-methodology"
+            ],
+            "temporal": "2013-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Physician & Other Practitioners - by Provider"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-09-06",
-            "temporal": "2021-2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
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
-            "identifier": "https://data.cdc.gov/api/views/5pqj-rvh4",
             "description": "Interactive Summary Health Statistics for Teens provide estimates of selected health topics for youth aged 12-17 years based on final data from the National Health Interview Survey\u2014 Teen.",
-            "title": "NHIS Teen",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4319,46 +4301,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5pqj-rvh4",
+            "issued": "2023-09-06",
+            "keyword": [
+                "nhis",
+                "summary health statistics"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2021-2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NHIS Teen"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/nf22-99pv",
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
-                "tetanus",
-                "varicella",
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
-            "identifier": "https://data.cdc.gov/api/views/nf22-99pv",
             "description": "NNDSS - Table II. Tetanus to Vibriosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Any species of the family Vibrionaceae, other than toxigenic Vibrio cholerae O1 or O139.",
-            "title": "NNDSS - Table II. Tetanus to Vibriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4381,85 +4357,80 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/nf22-99pv",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "varicella",
+                "vibriosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/nf22-99pv",
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
+            "title": "NNDSS - Table II. Tetanus to Vibriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.icpsr.umich.edu/icpsrweb/NAHDAP/index.jsp",
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
                 "fn": "Etz, Kathy",
                 "hasEmail": "mailto:ketz@nida.nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "d2073e47-2472-417c-9431-0797be6d35a8",
+            "dataQuality": true,
             "description": "<p>NAHDAP acquires, preserves and disseminates data relevant to drug addiction and HIV research. By preserving and making available an easily accessible library of electronic data on drug addiction and HIV infection in the United States, NAHDAP offers scholars the opportunity to conduct secondary analysis on major issues of social and behavioral sciences and public policy.</p>",
-            "title": "National Addiction & HIV Data Archive Program (NAHDAP)",
+            "identifier": "d2073e47-2472-417c-9431-0797be6d35a8",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://www.icpsr.umich.edu/icpsrweb/NAHDAP/index.jsp",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:027"
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
+            "title": "National Addiction & HIV Data Archive Program (NAHDAP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/km4m-vcsb",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-11-23",
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
-            "identifier": "https://data.cdc.gov/api/views/km4m-vcsb",
             "description": "Overall\u00a0Demographic Characteristics of People Receiving COVID-19 Vaccinations in the United States\u00a0at national level. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u00a0",
-            "title": "COVID-19 Vaccination Demographics in the United States,National",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4482,55 +4453,53 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/km4m-vcsb",
+            "issued": "2022-11-23",
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
+            "landingPage": "https://data.cdc.gov/d/km4m-vcsb",
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
+            "title": "COVID-19 Vaccination Demographics in the United States,National"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/surveillance/nvsn/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-01-30",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-Present",
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
-            "identifier": "https://data.cdc.gov/api/views/kipu-qxy8",
             "description": "Percent positivity of 9 viral pathogens, by season and age group, 2017\u2013Present.",
-            "title": "Percent Positivity of Viral Detections Among Enrolled Children in the New Vaccine Surveillance Network (NVSN), Acute Respiratory Illnesses (ARI), 2017\u2013Present",
-            "isPartOf": "Yes",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4553,43 +4522,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/kipu-qxy8",
+            "isPartOf": "Yes",
+            "issued": "2024-01-30",
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
+            "temporal": "2017-Present",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Percent Positivity of Viral Detections Among Enrolled Children in the New Vaccine Surveillance Network (NVSN), Acute Respiratory Illnesses (ARI), 2017\u2013Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fcqm-xrf4",
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
-            "identifier": "https://data.cdc.gov/api/views/fcqm-xrf4",
             "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2011-2014. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2011-2014",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4612,53 +4592,43 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fcqm-xrf4",
+            "issued": "2018-07-25",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "particulate matter",
+                "pm2.5"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fcqm-xrf4",
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
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2011-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-05",
-            "temporal": "2000/2018",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
-            "keyword": [
-                "ambulatory care",
-                "black or african american",
-                "child and adolescent",
-                "emergency department visits",
-                "emergency service",
-                "health care use",
-                "health us",
-                "hospital use",
-                "men",
-                "office visits",
-                "older persons",
-                "physician office visits",
-                "physicians",
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
-            "identifier": "https://data.cdc.gov/api/views/xmjk-wh9b",
             "description": "Data on visits to physician offices and hospital emergency departments in the United States, by age, sex, and race. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Ambulatory Medical Care Survey and National Hospital Ambulatory Medical Care Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Visits to physician offices, hospital outpatient departments, and hospital emergency departments, by age, sex, and race: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4681,39 +4651,53 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/xmjk-wh9b",
+            "issued": "2024-03-05",
+            "keyword": [
+                "ambulatory care",
+                "black or african american",
+                "child and adolescent",
+                "emergency department visits",
+                "emergency service",
+                "health care use",
+                "health us",
+                "hospital use",
+                "men",
+                "office visits",
+                "older persons",
+                "physician office visits",
+                "physicians",
+                "white",
+                "women"
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
+            "temporal": "2000/2018",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Visits to physician offices, hospital outpatient departments, and hospital emergency departments, by age, sex, and race: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/32du-kggf",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-03",
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
-            "identifier": "1bbe0db1-6c72-4368-8e44-467ee86662d0",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-25-2024-to-12-01-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4721,43 +4705,36 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "1bbe0db1-6c72-4368-8e44-467ee86662d0",
+            "issued": "2024-12-04",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/32du-kggf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-03",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-25-2024-to-12-01-2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/uny6-e3dx",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-06-16",
-            "@type": "dcat:Dataset",
-            "temporal": "July 2022-June 2023",
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
-            "identifier": "https://data.cdc.gov/api/views/uny6-e3dx",
             "description": "National Immunization Survey Child COVID Module (NIS-CCM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data.  These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics.",
-            "title": "National Immunization Survey Child COVID Module (NIS-CCM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)-Archived",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4780,52 +4757,50 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "National",
+            "identifier": "https://data.cdc.gov/api/views/uny6-e3dx",
+            "issued": "2022-06-16",
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
+            "landingPage": "https://data.cdc.gov/d/uny6-e3dx",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-01-24",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "National",
+            "temporal": "July 2022-June 2023",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "National Immunization Survey Child COVID Module (NIS-CCM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)-Archived"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-28",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "references": [
-                "IPSOS Knowledge Panel Omnibus and NORC AmeriSpeak Omnibus Surveys"
-            ],
-            "keyword": [
-                "adults",
-                "age group",
-                "ethnicity",
-                "flu",
-                "flu vaccination",
-                "race",
-                "vaccination"
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
-            "identifier": "https://data.cdc.gov/api/views/kmap-fsfn",
             "description": "Cumulative Influenza Vaccination Coverage, Adults 18 years and older, by Age Group and Race/Ethnicity, United States, 2020-21, IPSOS Knowledge Panel Omnibus and NORC AmeriSpeak Omnibus Surveys",
-            "title": "Cumulative Influenza Vaccination Coverage, Adults 18 years and older, by Age Group and Race/Ethnicity, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4848,45 +4823,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kmap-fsfn",
+            "issued": "2021-01-28",
+            "keyword": [
+                "adults",
+                "age group",
+                "ethnicity",
+                "flu",
+                "flu vaccination",
+                "race",
+                "vaccination"
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
+                "IPSOS Knowledge Panel Omnibus and NORC AmeriSpeak Omnibus Surveys"
+            ],
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Cumulative Influenza Vaccination Coverage, Adults 18 years and older, by Age Group and Race/Ethnicity, United States"
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
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-22/2023-05-10",
-            "modified": "2025-01-13",
-            "keyword": [
-                "aggregate county data",
-                "cases",
-                "coronavirus",
-                "covid-19"
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
-            "identifier": "https://data.cdc.gov/api/views/7pvw-pdbr",
             "description": "The Public Health Emergency (PHE) declaration for COVID-19 expired on May 11, 2023. As a result, the Aggregate Case and Death Surveillance System will be discontinued. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\nOn October 20, 2022, CDC began retrieving aggregate case and death data from jurisdictional and state partners weekly instead of daily. \n\nThis dataset includes the URLs that were used by the aggregate county data collection process that compiled aggregate case and death counts by county. Within this file, each of the states (plus select jurisdictions and territories) are listed along with the county web sources which were used for pulling these numbers. Some states had a single statewide source for collecting the county data, while other states and local health jurisdictions may have had standalone sources for individual counties. In the cases where both local and state web sources were listed, a composite approach was taken so that the maximum value reported for a location from either source was used. The initial raw data were sourced from these links and ingested into the CDC aggregate county dataset before being published on the COVID Data Tracker.",
-            "title": "United States COVID-19 County Level Data Sources - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4909,55 +4890,52 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/7pvw-pdbr",
+            "issued": "2022-05-18",
+            "keyword": [
+                "aggregate county data",
+                "cases",
+                "coronavirus",
+                "covid-19"
+            ],
+            "landingPage": "https://data.cdc.gov/d/7pvw-pdbr",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/realizing-equity-access-and-community-health-acos",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-05-26",
-            "temporal": "2021-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "references": [
-                "https://data.cms.gov/resources/aco-reach-model-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/eddc0a1b-dab8-478e-a883-3385e0275a17/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-reach-model-data-dictionary-2024",
             "description": "The Accountable Care Organization Realizing Equity, Access, and Community Health (ACO REACH) Model dataset provides overview information on REACH ACOs including their name, number of years in the program, and contact information of key personnel. \u00a0\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to ACO information occur periodically. Each ACO has the most up-to-date information about their organization. Consider contacting the ACO for the latest information.",
-            "title": "Realizing Equity, Access, and Community Health ACOs",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/eddc0a1b-dab8-478e-a883-3385e0275a17/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/eddc0a1b-dab8-478e-a883-3385e0275a17/data",
+                    "mediaType": "text/html",
                     "title": "Realizing Equity, Access, and Community Health ACOs : 2024-01-01"
                 },
                 {
@@ -5009,46 +4987,51 @@
                     "title": "Realizing Equity, Access, and Community Health ACOs : 2021-04-28"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/aco-reach-model-data-dictionary-2024",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/eddc0a1b-dab8-478e-a883-3385e0275a17/data-viewer",
+            "issued": "2023-05-26",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/realizing-equity-access-and-community-health-acos",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-01",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/aco-reach-model-methodology"
+            ],
+            "temporal": "2021-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Realizing Equity, Access, and Community Health ACOs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/child-welfare-outcomes-data-portal",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-05-30",
-            "temporal": "2004-01-01T00:00:00-05:00/2007-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "children's health",
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
-            "identifier": "f7707293-3a86-4f71-9e8c-6ca27c4c4eca",
+            "dataQuality": true,
             "description": "<p>The most current Child Welfare Outcomes data is featured on this site. Through the site, you can view the data before the full report is published. The most recently published full report is Child Welfare Outcomes 2004-2007: Report to Congress.</p>",
-            "title": "Child Welfare Outcomes Data Portal",
-            "programCode": [
-                "009:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5057,40 +5040,37 @@
                     "title": "Query Tool "
                 }
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "f7707293-3a86-4f71-9e8c-6ca27c4c4eca",
+            "issued": "2012-05-30",
+            "keyword": [
+                "children's health",
+                "department-of-health-human-services"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/child-welfare-outcomes-data-portal",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "temporal": "2004-01-01T00:00:00-05:00/2007-12-31T00:00:00-05:00",
+            "title": "Child Welfare Outcomes Data Portal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/35fs-iknb",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "eligibility",
-                "home and community-based services",
-                "medicaid",
-                "section 1915(c) waivers",
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
-            "identifier": "4d4eaf55-33d3-4468-80b4-63553f4530ae",
             "description": "This data set includes annual counts and percentages of Medicaid and Children\u2019s Health Insurance Program (CHIP) enrollees who received a well-child visit paid for by Medicaid or CHIP, overall and by five subpopulation topics: age group, race and ethnicity, urban or rural residence, program type, and primary language.\r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands, except where otherwise noted. Enrollees in Guam, American Samoa, and the Northern Mariana Islands are not included. Results include enrollees with comprehensive Medicaid or CHIP benefits for all 12 months of the year and who were younger than age 19 at the end of the calendar year. Results shown for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown for the primary language subpopulation topic exclude select states with data quality issues with the primary language variable in TAF. Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Medicaid and CHIP enrollees who received a well-child visit in 2020.\" Enrollees are identified as receiving a well-child visit in the year according to the Line 6 criteria in the Form CMS-416 reporting instructions. Enrollees are assigned to an age group subpopulation using age as of December 31st of the calendar year. Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to an urban or rural subpopulation based on the 2010 Rural-Urban Commuting Area (RUCA) code associated with their home or mailing address ZIP code in TAF (Rural Medicaid and CHIP enrollees in 2020). Enrollees are assigned to a program type subpopulation based on the CHIP code and eligibility group code that applies to the majority of their enrolled-months during the year (Medicaid-Only Enrollment; M-CHIP and S-CHIP Enrollment). Enrollees are assigned to a primary language subpopulation based on their reported ISO language code in TAF (English/missing, Spanish, and all other language codes) (Primary Language). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
-            "title": "Section 1915(c) waiver program participants",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5098,39 +5078,40 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "4d4eaf55-33d3-4468-80b4-63553f4530ae",
+            "issued": "2025-01-18",
+            "keyword": [
+                "eligibility",
+                "home and community-based services",
+                "medicaid",
+                "section 1915(c) waivers",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/35fs-iknb",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Section 1915(c) waiver program participants"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/35iy-s4en",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-17",
-            "keyword": [
-                "individual",
-                "individual market medical",
-                "py2022",
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
-            "identifier": "7322f647-1be7-4e61-a91f-f5bced1d7795",
             "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2022 Individual Medical",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5138,85 +5119,85 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "7322f647-1be7-4e61-a91f-f5bced1d7795",
+            "issued": "2022-08-10",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2022",
+                "qhp",
+                "qhp landscape instructions"
+            ],
+            "landingPage": "https://healthdata.gov/d/35iy-s4en",
+            "modified": "2022-08-17",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2022 Individual Medical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/35q4-9x42",
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
-            "identifier": "ba1910df-24b8-5d09-9490-356d1b06c0ae",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard version v2.11.9 (impl)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/version.csv",
-                    "description": "Scorecard version v2.11.9 (impl)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard version v2.11.9 (impl)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/version.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard version v2.11.9 (impl)"
                 }
             ],
+            "identifier": "ba1910df-24b8-5d09-9490-356d1b06c0ae",
+            "issued": "2023-06-29",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/35q4-9x42",
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
+            "title": "Scorecard version v2.11.9 (impl)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "references": [
-                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm#zip",
-                "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAssem/assembler.cfm"
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
-            "identifier": "aae3533d-6b69-4648-833c-a73700e51f51",
             "description": "Federal regulations require that an assembler who installs one or more certified components of a diagnostic x-ray system submit a report of assembly. This database contains the releasable information submitted including Equipment Location, General Information and Component Information. Note: Data does not include dental system installations.",
-            "title": "X-Ray Assembler Data",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5224,51 +5205,40 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "aae3533d-6b69-4648-833c-a73700e51f51",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm#zip",
+                "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAssem/assembler.cfm"
+            ],
+            "title": "X-Ray Assembler Data"
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
-            "modified": "2023-11-14",
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
-            "identifier": "https://data.cdc.gov/api/views/k86t-wghb",
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-level-Data-GIS-Friendly-Fo/k86t-wghb",
             "description": "2017, 2016. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census tract-level data in GIS-friendly format can be joined with census tract spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-Boundaries/x7zy-2xmx) in a geographic information system (GIS) to produce maps of 27 measures at the census tract level. There are 7 measures (all teeth lost, dental visits, mammograms, Pap tests, colorectal cancer screening, core preventive services among older adults, and sleep less than 7 hours) in this 2019 release from the 2016 BRFSS that were the same as the 2018 release.",
-            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2019 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5291,44 +5261,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Census-Tract-level-Data-GIS-Friendly-Fo/k86t-wghb",
+            "identifier": "https://data.cdc.gov/api/views/k86t-wghb",
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
+            "modified": "2023-11-14",
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
+            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2019 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-12-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1940/2018",
-            "modified": "2022-03-29",
-            "keyword": [
-                "age of mother",
-                "birth rates",
-                "nchs",
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
-            "identifier": "https://data.cdc.gov/api/views/yt7u-eiyg",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes birth rates for females by age group in the United States since 1940.\n\nThe number of states in the reporting area differ historically. In 1915 (when the birth registration area was established), 10 states and the District of Columbia reported births; by 1933, 48 states and the District of Columbia were reporting births, with the last two states, Alaska and Hawaii, added to the registration area in 1959 and 1960, when these regions gained statehood. Reporting area information is detailed in references 1 and 2 below. Trend lines for 1909\u20131958 are based on live births adjusted for under-registration; beginning with 1959, trend lines are based on registered live births.",
-            "title": "NCHS - Birth Rates for Females by Age Group: United States",
-            "isPartOf": "NCHS - Birth Rates for Females by Age Group: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5351,43 +5331,47 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/yt7u-eiyg",
+            "isPartOf": "NCHS - Birth Rates for Females by Age Group: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "age of mother",
+                "birth rates",
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
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1940/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Birth Rates for Females by Age Group: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/379c-in3d",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-11-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
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
-            "identifier": "3ff8a0e5-3f2e-49b2-80f6-f4db684f235a",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 10-28-2024-to-11-03-2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5395,41 +5379,36 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "3ff8a0e5-3f2e-49b2-80f6-f4db684f235a",
+            "issued": "2024-11-06",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/379c-in3d",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-11-04",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 10-28-2024-to-11-03-2024"
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
-            "identifier": "https://data.cdc.gov/api/views/8fbp-accd",
             "description": "Weekly Influenza Vaccination Coverage, Pregnant Women 18-49 Years Old by Race and Ethnicity\n  \nWeekly influenza vaccination coverage estimates for pregnant women 18\u201349 years are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD) (https://www.cdc.gov/vaccine-safety-systems/vsd/), a collaboration between CDC\u2019s Immunization Safety Office and multiple integrated health care organizations.",
-            "title": "Weekly Influenza Vaccination Coverage Among Pregnant Women 18-49 Years, by Race and Ethnicity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5452,56 +5431,57 @@
                     "mediaType": "application/xml"
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
+            "title": "Weekly Influenza Vaccination Coverage Among Pregnant Women 18-49 Years, by Race and Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/opt-out-affidavits",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2023-04-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-22",
-            "references": [
-                "https://data.cms.gov/resources/opt-out-affidavits-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/9887a515-7552-4693-bf58-735c77af46d7/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/opt-out-affidavits-data-dictionary",
             "description": "ATTENTION USERS\n\n\nSome Providers' Opt-Out Status may end early due to COVID 19 waivers. Please contact your respective MAC for further information.\n\n\u00a0\n\nFor more information on the opt-out process, see Manage Your Enrollment\u00a0or view the FAQ section below.\n\n\u00a0\n\nThe Opt Out Affidavits dataset provides information on providers who have decided not to participate in Medicare. It contains provider's NPI, specialty, address, and effective dates.",
-            "title": "Opt Out Affidavits",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9887a515-7552-4693-bf58-735c77af46d7/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9887a515-7552-4693-bf58-735c77af46d7/data",
+                    "mediaType": "text/html",
                     "title": "Opt Out Affidavits : 2024-12-01"
                 },
                 {
@@ -5757,50 +5737,49 @@
                     "title": "Opt Out Affidavits : 2023-04-30"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/opt-out-affidavits-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9887a515-7552-4693-bf58-735c77af46d7/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/opt-out-affidavits",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-22",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/opt-out-affidavits-methodology"
+            ],
+            "temporal": "2023-04-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Opt Out Affidavits"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.atsdr.cdc.gov/placeandhealth/svi/index.html",
+            "accrualPeriodicity": "biennial",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-03-10",
-            "@type": "dcat:Dataset",
-            "temporal": "2018",
-            "modified": "2022-02-14",
-            "keyword": [
-                "2018",
-                "county",
-                "social vulnerability",
-                "social vulnerability index",
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
-            "identifier": "https://data.cdc.gov/api/views/48va-t53r",
             "description": "ATSDR\u2019s Geospatial Research, Analysis & Services Program (GRASP) created Centers for Disease Control and Prevention Social Vulnerability Index (CDC SVI or simply SVI, hereafter) to help public health officials and emergency response planners identify and map the communities that will most likely need support before, during, and after a hazardous event. \n\nSVI indicates the relative vulnerability of every U.S. Census tract. Census tracts are subdivisions of counties for which the Census collects statistical data. SVI ranks the tracts on 15 social factors, including unemployment, minority status, and disability, and further groups them into four related themes. Thus, each tract receives a\nranking for each Census variable and for each of the four themes, as well as an overall ranking.\n\nIn addition to tract-level rankings, SVI 2018 also has corresponding rankings at the\ncounty level. Notes below that describe \u201ctract\u201d methods also refer to county methods.",
-            "title": "Social Vulnerability Index 2018 -  United States, county",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5823,56 +5802,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
+            "identifier": "https://data.cdc.gov/api/views/48va-t53r",
+            "issued": "2020-03-10",
+            "keyword": [
+                "2018",
+                "county",
+                "social vulnerability",
+                "social vulnerability index",
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
+            "title": "Social Vulnerability Index 2018 -  United States, county"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-geography-and-service",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2013-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "references": [
-                "https://data.cms.gov/resources/medicare-physician-other-practitioners-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/6fea9d79-0129-4e4c-b1b8-23cd86a4f435/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-physician-other-practitioners-by-geography-and-service-data-dictionary",
             "description": "The Medicare Physician & Other Practitioners by Geography and Service dataset contains\u00a0information on use, payments, submitted charges, and beneficiary demographic and health characteristics organized by geography, Healthcare Common Procedure Coding System (HCPCS) code, and place of service.",
-            "title": "Medicare Physician & Other Practitioners - by Geography and Service",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6fea9d79-0129-4e4c-b1b8-23cd86a4f435/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6fea9d79-0129-4e4c-b1b8-23cd86a4f435/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Physician & Other Practitioners - by Geography and Service : 2022-12-01"
                 },
                 {
@@ -5996,41 +5973,51 @@
                     "title": "Medicare Physician & Other Practitioners - by Geography and Service : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-physician-other-practitioners-by-geography-and-service-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6fea9d79-0129-4e4c-b1b8-23cd86a4f435/data-viewer",
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
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-geography-and-service",
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
+                "https://data.cms.gov/resources/medicare-physician-other-practitioners-methodology"
+            ],
+            "temporal": "2013-01-01/2022-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Physician & Other Practitioners - by Geography and Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/x7xw-nitb",
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
-            "identifier": "https://data.cdc.gov/api/views/x7xw-nitb",
             "description": "Perfluoroheptaoinc acid (PFHpA), perfluorohexanoic acid (PFHxA), and perfluoropentanoic acid (PFPeA) are synthetic chemicals belonging to the per- and polyfluoroalkyl substances (PFAS) group that includes over 5,000 chemicals.  PFHpA, PFHxA, and PFPeA are short-chain PFAS (C7, C6, C5, respectively) that have been labeled as a safer alternative to the legacy PFAS perfluorooctanoic acid (PFOA) and perfluorooctane sulfate (PFOS) which have been linked to numerous health effects.  This class of chemicals are incorporated into consumer products such as stain resistant carpeting and textiles, nanosprays, medical devices, and fire-fighting foams.  There is a high potential for occupational exposure and in the environment, short-chain PFAS have been detected in a variety of water sources leading to concerns for dermal exposure, however, these studies are lacking.  In previous studies from our lab, PFOA was demonstrated to be absorbed via the skin and immunomodulatory.  Also, the short-chain PFAS, PFBA, was found to have systemic toxic effects on mice with dermal exposure.  In the present study, the systemic toxicity of a 28-day dermal PFHpA, PFHxA, and PFPeA (1.25-5% w/v or v/v, or 31.25-125 mg/kg/dose) exposure was evaluated in a murine model.",
-            "title": "Systemic toxicity induced by topical application of perfluoroheptanoic acid (PFHpA), perfluorohexanoic acid (PFHxA), and perfluoropentanoic acid (PFPeA) in a murine model",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6038,21 +6025,46 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/x7xw-nitb",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/x7xw-nitb",
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
+            "title": "Systemic toxicity induced by topical application of perfluoroheptanoic acid (PFHpA), perfluorohexanoic acid (PFHxA), and perfluoropentanoic acid (PFPeA) in a murine model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://nhsc.hrsa.gov/",
             "bureauCode": [
                 "009:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HRSA Contact Center",
+                "hasEmail": "mailto:nhscsp@hrsa.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The National Health Service Corps (NHSC) Jobs Center helps doctors and nurses who are interested in working at areas where there is the highest need find out more about opportunities in a particular area or healthcare discipline. The Job Center provides information on the work locations and area. Job opportunities can be searched and identified by a combination of search parameters. The user views the search results on a map and as text and both views provide links to get more detailed information for each returned opportunity.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://connector.hrsa.gov/connector/",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "96140022-54b5-4e69-a7b9-0dbea290b5e0",
             "issued": "2012-05-30",
-            "temporal": "2009-01-01T00:00:00-05:00/2009-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "clinician",
                 "community health",
@@ -6074,74 +6086,37 @@
                 "vacancy",
                 "volunteer"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HRSA Contact Center",
-                "hasEmail": "mailto:nhscsp@hrsa.gov"
-            },
+            "landingPage": "https://nhsc.hrsa.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Health Resources and Services Administration"
             },
-            "identifier": "96140022-54b5-4e69-a7b9-0dbea290b5e0",
-            "description": "<p>The National Health Service Corps (NHSC) Jobs Center helps doctors and nurses who are interested in working at areas where there is the highest need find out more about opportunities in a particular area or healthcare discipline. The Job Center provides information on the work locations and area. Job opportunities can be searched and identified by a combination of search parameters. The user views the search results on a map and as text and both views provide links to get more detailed information for each returned opportunity.</p>",
-            "title": "NHSC Jobs Center for Primary Care Medical, Dental and Mental Health Providers",
-            "programCode": [
-                "009:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://connector.hrsa.gov/connector/",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2009-01-01T00:00:00-05:00/2009-01-01T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health",
                 "National"
-            ]
+            ],
+            "title": "NHSC Jobs Center for Primary Care Medical, Dental and Mental Health Providers"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -6164,62 +6139,50 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://www.cdc.gov/cdi",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "references": [
-                "https://www.cdc.gov/mmwr/pdf/rr/rr6401.pdf"
-            ],
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
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DPH Public Inquiries",
                 "hasEmail": "mailto:dphinquiries@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/g4ie-h725",
+            "describedBy": "https://data.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-CDI-/g4ie-h725",
             "description": "This dataset is based on indicators described in MMWR \"Indicators for Chronic Disease Surveillance \u2014 United States, 2013\" (https://www.cdc.gov/mmwr/preview/mmwrhtml/rr6401a1.htm) before 2024 CDI refresh. It provided cross-cutting set of 124 indicators that were developed by consensus and that allows states and territories to uniformly define, collect, and report chronic disease data that are important to public health practice and available for states, and territories. In addition to providing access to state-specific indicator data, the CDI web site (www.cdc.gov/cdi) provides current release and additional information and data resources.",
-            "title": "U.S. Chronic Disease Indicators (CDI), 2023 Release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6242,102 +6205,152 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/Chronic-Disease-Indicators/U-S-Chronic-Disease-Indicators-CDI-/g4ie-h725",
+            "identifier": "https://data.cdc.gov/api/views/g4ie-h725",
+            "issued": "2023-07-19",
+            "keyword": [
+                "alcohol",
+                "arthritis",
+                "asthma",
+                "cancer",
+                "cardiovascular disease",
+                "cdi",
+                "chronic disease indicators",
+                "chronic kidney disease",
+                "chronic obstructive pulmonary disease",
+                "diabetes",
+                "disability",
+                "immunization",
+                "mental health",
+                "nutrition physical activity and weight status",
+                "older adults",
+                "oral health",
+                "overarching conditions",
+                "public health",
+                "reproductive health",
+                "tobacco"
+            ],
+            "landingPage": "https://www.cdc.gov/cdi",
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
+                "https://www.cdc.gov/mmwr/pdf/rr/rr6401.pdf"
+            ],
             "theme": [
                 "Chronic Disease Indicators"
-            ]
+            ],
+            "title": "U.S. Chronic Disease Indicators (CDI), 2023 Release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/medicaid-fraud-control-units-mfcu-annual-spending-and-performance-statistics-0",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Medicaid Fraud Control Units (MFCU or Unit) investigate and prosecute Medicaid fraud as well as patient abuse and neglect in health care facilities. OIG certifies, and annually recertifies, each MFCU. OIG collects information about MFCU operations and assesses whether they comply with statutes, regulations, and OIG policy. OIG also analyzes MFCU performance based on 12 published performance standards and recommends program improvements where appropriate.</p>",
+            "identifier": "b4a62bb8-24ad-4da3-9ac4-81b41aa9105a",
             "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "fraud",
                 "medicaid",
                 "state spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "admin",
-                "hasEmail": "mailto:HealthData@hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/medicaid-fraud-control-units-mfcu-annual-spending-and-performance-statistics-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:076"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "b4a62bb8-24ad-4da3-9ac4-81b41aa9105a",
-            "description": "<p>Medicaid Fraud Control Units (MFCU or Unit) investigate and prosecute Medicaid fraud as well as patient abuse and neglect in health care facilities. OIG certifies, and annually recertifies, each MFCU. OIG collects information about MFCU operations and assesses whether they comply with statutes, regulations, and OIG policy. OIG also analyzes MFCU performance based on 12 published performance standards and recommends program improvements where appropriate.</p>",
-            "title": "Medicaid Fraud Control Units (MFCUs)",
-            "programCode": [
-                "009:076"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "Medicaid Fraud Control Units (MFCUs)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/39rx-wnpf",
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
-            "identifier": "08befceb-ef7c-5329-b140-4f2246f4da75",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet state v2.10.64 (coreset-cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
-                    "description": "CoreSet state v2.10.64 (coreset-cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet state v2.10.64 (coreset-cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/state.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet state v2.10.64 (coreset-cmsdev)"
                 }
             ],
+            "identifier": "08befceb-ef7c-5329-b140-4f2246f4da75",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/39rx-wnpf",
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
+            "title": "CoreSet state v2.10.64 (coreset-cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2003",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2003) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2003-nid13590",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2003-nid13590"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2003-nid13590",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -6350,59 +6363,29 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2003",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2003-nid13590",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2003)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2003-nid13590",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2003) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2003-nid13590"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2003)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://mbr.nlm.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/exav-tdkk",
             "description": "The MEDLINE/PubMed Baseline Repository (MBR) provides access to each MEDLINE/PubMed Baseline snapshot starting with the 2002 MEDLINE Baseline. Each baseline contains a snapshot of MEDLINE citations in the state they were at a given moment in time without the MeSH vocabulary updates and other revisions that occur during the year. The baseline snapshot is created at the beginning of each new MeSH Indexing Year. The records included in the MEDLINE/PubMed Baseline databases represent a static view of the data at the time each baseline database was created.",
-            "title": "MEDLINE/PubMed Baseline Repository (MBR)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6411,90 +6394,85 @@
                     "title": "Download MEDLINE/PubMed Baseline Repository (MBR) Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/exav-tdkk",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "literature"
+            ],
+            "landingPage": "https://mbr.nlm.nih.gov/",
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
+            "title": "MEDLINE/PubMed Baseline Repository (MBR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3amq-vrs8",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-05-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-25",
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
-            "identifier": "e0c7b1d9-44a1-565a-b975-1a4c61855914",
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
+            "identifier": "e0c7b1d9-44a1-565a-b975-1a4c61855914",
+            "issued": "2023-05-26",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/3amq-vrs8",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-05-25",
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
-            "landingPage": "https://data.cdc.gov/d/2khz-k7sv",
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
-            "identifier": "https://data.cdc.gov/api/views/2khz-k7sv",
             "description": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome  - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6517,38 +6495,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/2khz-k7sv",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "rubella congenital syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/2khz-k7sv",
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
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMQSA/mqsa.cfm",
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
-            "identifier": "705ec42c-0f47-4afd-9096-a73b28958348",
             "description": "The Mammography Facility Database is updated periodically based on information received from the four FDA-approved accreditation bodies: the American College of Radiology (ACR), and the States of Arkansas, Iowa, and Texas. Information received by FDA or Certifying State from accreditation bodies does not specify if the facility is mobile or stationary. In many instances, but not all, the accreditation body notes Mobile following the name of the facility. The certification status of facilities may change, so FDA suggests that you check the facility's current status and look for the MQSA certificate.",
-            "title": "Mammography Facilities",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6556,41 +6540,35 @@
                     "mediaType": "text/html"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "705ec42c-0f47-4afd-9096-a73b28958348",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMQSA/mqsa.cfm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-11-01",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Mammography Facilities"
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
@@ -6613,94 +6591,92 @@
                     "mediaType": "application/xml"
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
-            "landingPage": "https://healthdata.gov/d/3c8f-ja5j",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-06",
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
-            "identifier": "78827f1a-9877-5d7d-9319-ac1f298d86d5",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_footnotes",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/footnotes.csv",
-                    "description": "{\"dataset\": \"footnotes\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"footnotes\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/footnotes.csv",
+                    "mediaType": "text/csv",
                     "title": "footnotes csv file"
                 }
             ],
+            "identifier": "78827f1a-9877-5d7d-9319-ac1f298d86d5",
+            "issued": "2023-06-06",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/3c8f-ja5j",
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
+            "title": "prodAuto_footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/qisn-zjv7",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/qisn-zjv7",
             "description": "NNDSS - Table 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6723,44 +6699,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/qisn-zjv7",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/qisn-zjv7",
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
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/56mi-d4wu",
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
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/56mi-d4wu",
             "description": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6783,20 +6761,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/56mi-d4wu",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "smallpox",
+                "streptococcal toxic shock syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/56mi-d4wu",
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
+            "title": "NNDSS - TABLE 1GG. Smallpox to Streptococcal toxic shock syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-v-nys-1980",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>Youth data for the fifth wave of the National Youth Survey<br />\nare contained in this collection. The first wave of this survey was<br />\nconducted in 1976, the second wave in 1977,<br />\nthe third wave in 1978, and the fourth wave in 1979. For this wave, youths in the United States were interviewed in<br />\nearly 1981 about events and behavior occurring in calendar year 1980.<br />\nData are available on the demographic and socioeconomic status of<br />\nrespondents, disruptive events in the home, neighborhood problems,<br />\nyouth aspirations and current successes, normlessness, labeling by<br />\nparents, friends, and co-workers, perceived disapproval, attitudes<br />\ntoward deviance, exposure and commitment to delinquent peers, sex<br />\nroles, interpersonal violence, attitudes toward sexual violence,<br />\npressure for substance abuse by peers, drug and alcohol use, and<br />\nvictimization.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Youth Survey US: Wave V (NYS-1980) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-v-nys-1980-nid13633",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-v-nys-1980-nid13633"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-v-nys-1980-nid13633",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "aspirations",
                 "behavior problems",
@@ -6828,139 +6841,109 @@
                 "young adults",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-youth-survey-us-wave-v-nys-1980",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-v-nys-1980-nid13633",
-            "description": "<p>Youth data for the fifth wave of the National Youth Survey<br />\nare contained in this collection. The first wave of this survey was<br />\nconducted in 1976, the second wave in 1977,<br />\nthe third wave in 1978, and the fourth wave in 1979. For this wave, youths in the United States were interviewed in<br />\nearly 1981 about events and behavior occurring in calendar year 1980.<br />\nData are available on the demographic and socioeconomic status of<br />\nrespondents, disruptive events in the home, neighborhood problems,<br />\nyouth aspirations and current successes, normlessness, labeling by<br />\nparents, friends, and co-workers, perceived disapproval, attitudes<br />\ntoward deviance, exposure and commitment to delinquent peers, sex<br />\nroles, interpersonal violence, attitudes toward sexual violence,<br />\npressure for substance abuse by peers, drug and alcohol use, and<br />\nvictimization.This study has 1 Data Set.</p>",
-            "title": "National Youth Survey US: Wave V (NYS-1980)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-v-nys-1980-nid13633",
-                    "description": "National Youth Survey US: Wave V (NYS-1980) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-youth-survey-us-wave-v-nys-1980-nid13633"
-                }
-            ]
+            "title": "National Youth Survey US: Wave V (NYS-1980)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/corporate-integrity-agreement-cia-documents",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-03-25",
-            "temporal": "2005-01-01T00:00:00-05:00/2005-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "office-of-inspector-general-department-of-health-human-services",
-                "other"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OIG Public Affairs",
                 "hasEmail": "mailto:Public.Affairs@OIG.HHS.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Inspector General, Department of Health & Human Services"
-            },
-            "identifier": "c1075abe-0e21-4207-b17b-1642cca9af82",
+            "dataQuality": true,
             "description": "<p>OIG negotiates corporate integrity agreements (CIA) with health care providers and other entities as part of the settlement of Federal health care program investigations arising under a variety of civil false claims statutes. Providers or entities agree to the obligations, and in exchange, OIG agrees not to seek their exclusion from participation in Medicare, Medicaid, or other Federal health care programs.</p>",
-            "title": "Corporate Integrity Agreement (CIA) documents",
+            "identifier": "c1075abe-0e21-4207-b17b-1642cca9af82",
+            "issued": "2013-03-25",
+            "keyword": [
+                "office-of-inspector-general-department-of-health-human-services",
+                "other"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/corporate-integrity-agreement-cia-documents",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
             "programCode": [
                 "009:023"
             ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Inspector General, Department of Health & Human Services"
+            },
+            "temporal": "2005-01-01T00:00:00-05:00/2005-01-01T00:00:00-05:00",
+            "title": "Corporate Integrity Agreement (CIA) documents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3egw-xczw",
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
-            "identifier": "e55bd3f1-1645-5751-8b2e-803f5c1b76ef",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
-            "title": "prodAuto_concernLevel",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/concernLevel.csv",
-                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/concernLevel.csv",
+                    "mediaType": "text/csv",
                     "title": "concernLevel csv file"
                 }
             ],
+            "identifier": "e55bd3f1-1645-5751-8b2e-803f5c1b76ef",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/3egw-xczw",
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
+            "title": "prodAuto_concernLevel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i9qr-47vu",
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
-            "identifier": "https://data.cdc.gov/api/views/i9qr-47vu",
             "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
-            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 9 - San Francisco",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6983,40 +6966,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i9qr-47vu",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i9qr-47vu",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 9 - San Francisco"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3fd8-e3zc",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2014-11-07",
-            "temporal": "2020-01-01T00:00:00+00:00/2021-01-01T00:00:00+00:00",
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
-            "identifier": "c933dc16-7de9-52b6-8971-4b75992673e0",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2020",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7025,57 +7008,50 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "c933dc16-7de9-52b6-8971-4b75992673e0",
+            "issued": "2014-11-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/3fd8-e3zc",
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
+            "temporal": "2020-01-01T00:00:00+00:00/2021-01-01T00:00:00+00:00",
             "theme": [
                 "National Average Drug Acquisition Cost",
                 "Drug Pricing and Payment"
-            ]
+            ],
+            "title": "NADAC (National Average Drug Acquisition Cost) 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-opioid-prescribing-rates/medicaid-opioid-prescribing-rates-by-geography",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2022-01-01/2022-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-11",
-            "references": [
-                "https://data.cms.gov/resources/medicaid-opioid-prescribing-rates-by-geography-methodology-2022"
-            ],
-            "keyword": [
-                "counties",
-                "drugs",
-                "health equity",
-                "medicaid",
-                "national",
-                "physicians & practitioners",
-                "rural-urban",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/c37ebe6d-f54f-4d7d-861f-fefe345554e6/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicaid-opioid-prescribing-rates-by-geography-data-dictionary-2022",
             "description": "The Medicaid Opioid Prescribing Rates by Geography dataset provides information on geographic comparisons of the number and percentage of Medicaid opioid prescriptions at the state, county, and ZIP code levels.",
-            "title": "Medicaid Opioid Prescribing Rates - by Geography",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c37ebe6d-f54f-4d7d-861f-fefe345554e6/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c37ebe6d-f54f-4d7d-861f-fefe345554e6/data",
+                    "mediaType": "text/html",
                     "title": "Medicaid Opioid Prescribing Rates - by Geography : 2022-12-01"
                 },
                 {
@@ -7091,44 +7067,52 @@
                     "title": "Medicaid Opioid Prescribing Rates - by Geography : 2022-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicaid-opioid-prescribing-rates-by-geography-data-dictionary-2022",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c37ebe6d-f54f-4d7d-861f-fefe345554e6/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "counties",
+                "drugs",
+                "health equity",
+                "medicaid",
+                "national",
+                "physicians & practitioners",
+                "rural-urban",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-opioid-prescribing-rates/medicaid-opioid-prescribing-rates-by-geography",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicaid-opioid-prescribing-rates-by-geography-methodology-2022"
+            ],
+            "temporal": "2022-01-01/2022-12-31",
             "theme": [
                 "Medicaid"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicaid Opioid Prescribing Rates - by Geography"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/i3a4-n4ma",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2020-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-21",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/i3a4-n4ma",
             "description": "The Clinical Questions Collection is a repository of questions that have been collected between 1991 \u2013 2003 from healthcare providers in clinical settings across the country. The questions have been submitted by investigators who wish to share their data with other researchers. This dataset is no-longer updated with new content. The collection is used in developing approaches to clinical and consumer-health question answering, as well as researching information needs of clinicians and the language they use to express their information needs. All files are formatted in XML.",
-            "title": "Clinical Questions Collection",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7161,39 +7145,38 @@
                     "title": "About the Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/i3a4-n4ma",
+            "issued": "2020-09-22",
+            "keyword": [
+                "data distribution"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/i3a4-n4ma",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-10-21",
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
+            "title": "Clinical Questions Collection"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -7216,39 +7199,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/bjsc-yd7n",
+            "issued": "2016-09-28",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bjsc-yd7n",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-09-28",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 3 - Philadelphia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3ge8-a5ey",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-30",
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
-            "identifier": "9a83ba5e-05f5-47f5-82de-f3a59233a912",
             "description": "Metrics from individual Marketplaces during the current reporting period. The report includes data for the states using HealthCare.gov. As of August 2024, CMS is no longer releasing the \u201cHealthCare.gov\u201d metrics. Historical data between July 2023-July 2024 will remain available. The \u201cHealthCare.gov Transitions\u201d metrics, which are the CAA, 2023 required metrics, will continue to be released.  <br />\r\n<b>Sources:</b> HealthCare.gov application and policy data through May 5, 2024, and T-MSIS Analytic Files (TAF) through March 2024 (TAF version 7.1 with T-MSIS enrollment through the end of March 2024). Data include consumers in HealthCare.gov states where the first unwinding renewal cohort is due on or after the end of reporting month (state identification based on HealthCare.gov policy and application data). State data start being reported in the month when the state's first unwinding renewal cohort is due. April data include Arizona, Arkansas, Florida, Indiana, Iowa, Kansas, Nebraska, New Hampshire, Ohio, Oklahoma, South Dakota, Utah, West Virginia, and Wyoming. May data include the previous states and the following new states: Alaska, Delaware, Georgia, Hawaii, Montana, North Dakota, South Carolina, Texas, and Virginia. June data include the previous states and the following new states: Alabama, Illinois, Louisiana, Michigan, Missouri, Mississippi, North Carolina, Tennessee, and Wisconsin. July data include the previous states and Oregon. All HealthCare.gov states are included in this version of the report.<br />\r\n<b>Notes: </b>\r\n<ol>\r\n<li> This table includes Marketplace consumers who: 1) submitted a HealthCare.gov application on or after the start of each state\u2019s first reporting month; and 2) who can be linked to an enrollment record in TAF that shows Medicaid or CHIP enrollment between March 2023 and the latest reporting month.</li>\r\n<li>Cumulative counts show the number of unique consumers from the included population who had a Marketplace application submitted or a HealthCare.gov Marketplace policy on or after the start of each state\u2019s first reporting month through the latest reporting month. Net counts show the difference between the cumulative counts through a given reporting month and previous reporting months.  </li>\r\n<li>The data used to produce the metrics are organized by week. Reporting months start on the first Monday of the month and end on the first Sunday of the next month when the last day of the reporting month is not a Sunday. For example, the April 2023 reporting period extends from Monday, April 3 through Sunday, April 30.</li>\r\n<li>Data are preliminary and will be restated over time to reflect consumers most recent HealthCare.gov status. Data may change as states resubmit T-MSIS data or data quality issues are identified.</li>\r\n<li>Data do not represent Marketplace consumers who had a confirmed Medicaid/CHIP loss. Future reporting will look at coverage transitions for people who lost Medicaid/CHIP.</li>\r\n<li>See the data and methodology documentation for a full description of the data sources, measure definitions, and general data limitations. </li>\r\n</ol>\r\n<b>Data notes:</b> <ol>\r\n<li> Virginia operated a Federally Facilitated Exchange (FFE) on the HealthCare.gov platform during 2023. In 2024, the state started operating a State Based Marketplace (SBM) platform. This table only includes data on 2023 applications and policies obtained through the HealthCare.gov Marketplace. Due to limited Marketplace activity on the HealthCare.gov platform in December 2023, data from December 2023 onward are excluded. The cumulative count and percentage for Virginia and the HealthCare.gov total reflect Virginia data from April 2023 through November 2023.</li>\r\n<li>The report may include negative 'net counts,' which reflect that there were cumulatively fewer counts from one month to the next.\r\n</li>\r\n<li>Wyoming has negative \u2018net counts\u2019 for most of its metrics in March 2024, including 'Marketplace Consumers with Previous M",
-            "title": "HealthCare.gov Marketplace Medicaid Unwinding Report",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7261,43 +7245,40 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "9a83ba5e-05f5-47f5-82de-f3a59233a912",
+            "issued": "2023-07-28",
+            "keyword": [
+                "marketplace",
+                "transitions in coverage"
+            ],
+            "landingPage": "https://healthdata.gov/d/3ge8-a5ey",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-08-30",
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
+            "title": "HealthCare.gov Marketplace Medicaid Unwinding Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3gvi-tec8",
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
-            "identifier": "2df89ece-d8f2-489f-9baf-b039cd676ce3",
             "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
-            "title": "QHP Landscape Instructions PY2025 Medical SHOP",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7305,45 +7286,39 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S"
+            "identifier": "2df89ece-d8f2-489f-9baf-b039cd676ce3",
+            "issued": "2024-12-10",
+            "keyword": [
+                "py2025",
+                "qhp",
+                "qhp landscape instructions",
+                "shop",
+                "shop market medical"
+            ],
+            "landingPage": "https://healthdata.gov/d/3gvi-tec8",
+            "modified": "2024-12-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "title": "QHP Landscape Instructions PY2025 Medical SHOP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-04-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2020/2023",
-            "modified": "2023-07-12",
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
-            "identifier": "https://data.cdc.gov/api/views/kn79-hsxy",
             "description": "Effective June 28, 2023, this dataset will no longer be updated. Similar data are accessible from  CDC WONDER (https://wonder.cdc.gov/mcd-icd10-provisional.html)\n\nProvisional count of deaths involving COVID-19 by county of occurrence, in the United States, 2020-2023.",
-            "title": "Provisional COVID-19 Death Counts in the United States by County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7366,41 +7341,49 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/kn79-hsxy",
+            "issued": "2020-04-21",
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
+            "temporal": "2020/2023",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 Death Counts in the United States by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rb93-4tgj",
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
-            "identifier": "https://data.cdc.gov/api/views/rb93-4tgj",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 4 - Atlanta",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7423,35 +7406,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rb93-4tgj",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rb93-4tgj",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 4 - Atlanta"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g7ty-3t6s",
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
-            "identifier": "https://data.cdc.gov/api/views/g7ty-3t6s",
             "description": "Our investigation examined the efficacy of Do-It-Yourself (DIY) air filtration units in reducing recipient exposure to simulated respiratory aerosols within a mock classroom. Seven commercially available box style fans were evaluated using five performance parameters. Two fans with the highest and lowest airflow rates were subsequently evaluated in two DIY unit configurations using either 2.5 or 5 cm deep minimum efficiency reporting value (MERV) 13 filters. DIY air filtration units were tested with the central HVAC system set at 2 air changes/hour (ACH) to represent a classroom with low ventilation. Results of the investigation provide a better understanding of DIY units and their potential to reduce exposure to infectious aerosols that can transmit SARS-CoV-2 and other diseases.\n\nNon-Endorsement Disclaimer:\nMention of any company or product does not constitute endorsement by the National Institute for Occupational Safety and Health (NIOSH), Centers for Disease Control and Prevention (CDC).",
-            "title": "Efficacy of Do-It-Yourself Air Filtration Units in Reducing Exposure to Simulated Respiratory Aerosols",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7459,21 +7446,44 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g7ty-3t6s",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/g7ty-3t6s",
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
+            "title": "Efficacy of Do-It-Yourself Air Filtration Units in Reducing Exposure to Simulated Respiratory Aerosols"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm227485.htm",
             "bureauCode": [
                 "009:10"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "description": "On September 22, 2010, Abbott issued a voluntary recall of certain Similac powdered infant formula after identifying a common warehouse beetle (both larvae and adults) in the finished product at their Sturgis, Michigan plant. The company immediately put all product manufactured at the Michigan plant on hold and ceased manufacturing at that location. FDA has advised against consumption of the recalled product and urged consumers to follow the manufacturer's instructions for reporting and returning the formula.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "identifier": "141bcfb1-fd5c-4abc-9e81-0e07cc3c8ca4",
             "issued": "2025-01-29",
-            "temporal": "2010-01-01/2010-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2010-10-01",
             "keyword": [
                 "community health",
                 "food",
@@ -7485,61 +7495,32 @@
                 "recalls",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FDA Enterprise Data Inventory",
-                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
-            },
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm227485.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2010-10-01",
+            "programCode": [
+                "009:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Food and Drug Administration"
             },
-            "identifier": "141bcfb1-fd5c-4abc-9e81-0e07cc3c8ca4",
-            "description": "On September 22, 2010, Abbott issued a voluntary recall of certain Similac powdered infant formula after identifying a common warehouse beetle (both larvae and adults) in the finished product at their Sturgis, Michigan plant. The company immediately put all product manufactured at the Michigan plant on hold and ceased manufacturing at that location. FDA has advised against consumption of the recalled product and urged consumers to follow the manufacturer's instructions for reporting and returning the formula.",
-            "title": "FDA Abbott Infant Formula Recall",
-            "programCode": [
-                "009:001"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xls",
-                    "mediaType": "application/vnd.ms-excel"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "temporal": "2010-01-01/2010-12-31",
+            "title": "FDA Abbott Infant Formula Recall"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hmye-mqgq",
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
-                "hospitalizations",
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
-            "identifier": "https://data.cdc.gov/api/views/hmye-mqgq",
             "description": "This dataset represents preliminary weekly estimates of cumulative U.S. RSV-associated hospitalizations for the 2024-2025 season. Estimates are preliminary, and use reported weekly hospitalizations among laboratory-confirmed respiratory syncytial virus (RSV) infections. The data are updated week-by-week as new RSV-associated hospitalizations are reported to CDC from the RSV-NET surveillance system and include both new admissions that occurred during the reporting week, as well as those admitted in previous weeks that may not have been included in earlier reporting. Each week CDC estimates a range (i.e., lower estimate and an upper estimate) of RSV-associated hospitalizations that have occurred since October 1, 2024. For details, please refer to the publication [7].  \n\n<b>Note:</b> Data are preliminary and subject to change as more data become available. Rates for recent RSV-associated hospital admissions are subject to reporting delays; as new data are received each week, previous rates are updated accordingly.\n\n<b>Note:</b> Preliminary burden estimates are not inclusive of data from all RSV-NET sites. Due to model limitations, sites with small sample sizes can impact estimates in unpredictable ways and are excluded for the benefit of model stability. CDC is working to address model limitations and include data from all sites in final burden estimates.\n\n<b>References</b>\n<ol><li>Reed C, Chaves SS, Daily Kirley P, et al. Estimating influenza disease burden from population-based surveillance data in the United States. PLoS One. 2015;10(3):e0118369. https://doi.org/10.1371/journal.pone.0118369\u202f </li><li>Rolfes, MA, Foppa, IM, Garg, S, et al. Annual estimates of the burden of seasonal influenza in the United States: A tool for strengthening influenza surveillance and preparedness. Influenza Other Respi Viruses. 2018; 12: 132\u2013 137. https://doi.org/10.1111/irv.12486</li><li>Tokars  JI, Rolfes  MA, Foppa  IM, Reed  C.  An evaluation and update of methods for estimating the number of influenza cases averted by vaccination in the United States.   Vaccine. 2018;36(48):7331-7337. doi:10.1016/j.vaccine.2018.10.026\u202f</li><li>Collier SA, Deng L, Adam EA, Benedict KM, Beshearse EM, Blackstock AJ, Bruce BB, Derado G, Edens C, Fullerton KE, Gargano JW, Geissler AL, Hall AJ, Havelaar AH, Hill VR, Hoekstra RM, Reddy SC, Scallan E, Stokes EK, Yoder JS, Beach MJ. Estimate of Burden and Direct Healthcare Cost of Infectious Waterborne Disease in the United States. Emerg Infect Dis. 2021 Jan;27(1):140-149. doi: 10.3201/eid2701.190676. PMID: 33350905; PMCID: PMC7774540.</li><li>Reed C, Kim IK, Singleton JA,\u202f et al. Estimated influenza illnesses and hospitalizations averted by vaccination\u2013United States, 2013-14 influenza season. MMWR Morb Mortal Wkly Rep. 2014 Dec 12;63(49):1151-4. https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6349a2.htm\u202f</li><li>Reed C, Angulo FJ, Swerdlow DL, et al. Estimates of the Prevalence of Pandemic (H1N1) 2009, United States, April\u2013July 2009. Emerg Infect Dis. 2009;15(12):2004-2007. https://dx.doi.org/10.3201/eid1512.091413 \u202f</li><li>Devine O, Pham H, Gunnels B, et al. Extrapolating Sentinel Surveillance Information to Estimate National COVID-19 Hospital Admission Rates: A Bayesian Modeling Approach. Influenza and Other Respiratory Viruses. https://onlinelibrary.wiley.com/doi/10.1111/irv.70026. Volume18, Issue10. October 2024.</li><li><a ref=\"https://www.cdc.gov/covid/php/covid-net/index.html\">COVID-NET | COVID-19 | CDC\u202f</a></li><li>https://www.cdc.gov/covid/hcp/clinical-care/systematic-review-process.html\u202f </li><li><a ref=\"https://academic.oup.com/pnasnexus/article/1/3/pgac079/6604394?login=false\">Excess natural-cause deaths in California by cause and setting: March 2020 through February 2021 | PNAS Nexus | Oxford Academic (oup.com)</a></li><li>Kruschke, J. K. 2011. Doing Bayesian data analysis: a tutorial with R and BUGS. Elsevier, Amsterdam, Section 3.3.5.</li></ol>",
-            "title": "Preliminary Estimates of Cumulative RSV-associated Hospitalizations by Week for 2024-2025 season",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7562,47 +7543,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/hmye-mqgq",
+            "issued": "2024-10-04",
+            "keyword": [
+                "hospitalizations",
+                "respiratory syncytial virus",
+                "rsv"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hmye-mqgq",
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
+            "title": "Preliminary Estimates of Cumulative RSV-associated Hospitalizations by Week for 2024-2025 season"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/9976-4iqj",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/9976-4iqj",
             "description": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7625,35 +7602,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/9976-4iqj",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "animal",
+                "human",
+                "nedss",
+                "netss",
+                "nndss",
+                "rabies",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9976-4iqj",
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
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/esmz-a36m",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Health Effects Laboratory Division",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/esmz-a36m",
             "description": "",
-            "title": "Fit evaluation of NIOSH Approved N95 filtering facepiece respirators with various skin protectants: a pilot study",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7661,20 +7648,46 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/esmz-a36m",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/esmz-a36m",
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
+            "title": "Fit evaluation of NIOSH Approved N95 filtering facepiece respirators with various skin protectants: a pilot study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2010",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov.Data\">http://findtreatment.samhsa.gov.Data</a> are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medication dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2010) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2010-nid13559",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2010-nid13559"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2010-nid13559",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -7687,58 +7700,30 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2010",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2010-nid13559",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov.Data\">http://findtreatment.samhsa.gov.Data</a> are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medication dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2010)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2010-nid13559",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2010) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2010-nid13559"
-                }
-            ]
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2010)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3niq-h6iw",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-08-16",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-15",
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
-            "identifier": "9ad4e7c5-00e5-4f2b-b53b-814b1caf623d",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-07-to-2023-08-13",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7747,38 +7732,36 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-07-to-2023-08-13"
                 }
             ],
+            "identifier": "9ad4e7c5-00e5-4f2b-b53b-814b1caf623d",
+            "issued": "2023-08-16",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/3niq-h6iw",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2023-08-15",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-07-to-2023-08-13"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3nua-y9h4",
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
-            "identifier": "17169c68-671e-5fc3-ae52-73c1dc97aafb",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2003",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7786,41 +7769,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "17169c68-671e-5fc3-ae52-73c1dc97aafb",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/3nua-y9h4",
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
+            "title": "State Drug Utilization Data 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3p9x-sv4s",
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
-            "identifier": "89de7fb8-b9ef-52fb-badc-ffc1128a9ada",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2008",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7828,39 +7811,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "89de7fb8-b9ef-52fb-badc-ffc1128a9ada",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/3p9x-sv4s",
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
+            "title": "State Drug Utilization Data 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3p9z-4b7f",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-02-16",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-14",
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
-            "identifier": "a9a9fa75-a438-4c86-ae2b-361f22fee182",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-07 to 2022-02-13",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7868,81 +7853,80 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "a9a9fa75-a438-4c86-ae2b-361f22fee182",
+            "issued": "2022-02-16",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/3p9z-4b7f",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P10Y"
+            "modified": "2022-02-14",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-07 to 2022-02-13"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://magpie.nlm.nih.gov/demo",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-03",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/hfvt-rpbu",
             "description": "MAGPIE is an interactive tool to help users (e.g., professional coders, researchers, clinicians) find SNOMED CT and ICD-10-PCS codes for medical procedures and interventions. MAGPIE is an NLM research tool (it has not been tested in a production environment), and is developed primarily for the 2018 version of ICD-10-PCS. MAGPIE combines lexical and map-assisted searching strategies to look for SNOMED CT, ICD-9-CM, and ICD-10-PCS codes sequentially.",
-            "title": "MAGPIE (Map Assisted Generation of Procedure and Intervention Encoding) [DEMO]",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://magpie.nlm.nih.gov/demo#?tab=instructions",
-                    "description": "Users of this tool must abide by the terms of the UMLS license, available at https://uts.nlm.nih.gov/license.html",
                     "@type": "dcat:Distribution",
+                    "description": "Users of this tool must abide by the terms of the UMLS license, available at https://uts.nlm.nih.gov/license.html",
+                    "downloadURL": "https://magpie.nlm.nih.gov/demo#?tab=instructions",
+                    "mediaType": "text/html",
                     "title": "Magpie Homepage"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/hfvt-rpbu",
+            "issued": "2021-06-30",
+            "keyword": [
+                "health data standards",
+                "terminologies",
+                "tools & utilities"
+            ],
+            "landingPage": "https://magpie.nlm.nih.gov/demo",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-12-03",
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
+            "title": "MAGPIE (Map Assisted Generation of Procedure and Intervention Encoding) [DEMO]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-detailed-mortality-underlying-cause-death",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2012-08-03",
-            "temporal": "1999-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
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
-            "identifier": "c37c5f79-a2cc-40e4-a69d-45dbceb773e3",
+            "dataQuality": true,
+            "describedBy": "http://wonder.cdc.gov/wonder/help/ucd.html",
             "description": "<p>The Detailed Mortality - Underlying Cause of Death data on CDC WONDER are county-level national mortality and population data spanning the years 1999-2009. Data are based on death certificates for U.S. residents. Each death certificate contains a single underlying cause of death, and demographic data. The number of deaths, crude death rates, age-adjusted death rates, standard errors and 95% confidence intervals for death rates can be obtained by place of residence (total U.S., region, state, and county), age group (including infants and single-year-of-age cohorts), race (4 groups), Hispanic ethnicity, gender, year of death, and cause-of-death (4-digit ICD-10 code or group of codes, injury intent and mechanism categories, or drug and alcohol related causes), year, month and week day of death, place of death and whether an autopsy was performed. The data are produced by the National Center for Health Statistics.</p>",
-            "title": "CDC WONDER: Detailed Mortality - Underlying Cause of Death",
-            "programCode": [
-                "009:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7951,69 +7935,98 @@
                     "title": "Text "
                 }
             ],
-            "describedBy": "http://wonder.cdc.gov/wonder/help/ucd.html",
-            "dataQuality": true,
+            "identifier": "c37c5f79-a2cc-40e4-a69d-45dbceb773e3",
+            "issued": "2012-08-03",
+            "keyword": [
+                "epidemiology",
+                "mortality deaths births health population cause disease icd urbanization state county infant race hi"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-detailed-mortality-underlying-cause-death",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "temporal": "1999-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
             "theme": [
                 "Health",
                 "State"
-            ]
+            ],
+            "title": "CDC WONDER: Detailed Mortality - Underlying Cause of Death"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3px5-aqsb",
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
-            "identifier": "c4bc3468-b66c-5329-9c18-bc76ddc57859",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet version v2.10.64 (coreset-cmsdev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
-                    "description": "CoreSet version v2.10.64 (coreset-cmsdev)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet version v2.10.64 (coreset-cmsdev)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/version.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet version v2.10.64 (coreset-cmsdev)"
                 }
             ],
+            "identifier": "c4bc3468-b66c-5329-9c18-bc76ddc57859",
+            "issued": "2024-11-13",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/3px5-aqsb",
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
+            "title": "CoreSet version v2.10.64 (coreset-cmsdev)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1985",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, tobacco, and nonmedical use of<br />\nprescription drugs among members of United States households aged 12<br />\nand older. Questions include age at first use as well as lifetime,<br />\nannual, and past-month usage for the following drug classes: cannabis,<br />\ncocaine, hallucinogens, heroin, inhalants, alcohol, tobacco,<br />\nnonmedical use of prescription drugs including psychotherapeutics, and<br />\npolysubstance use. Respondents were also asked about health<br />\nconditions, substance abuse treatment history, problems resulting from<br />\ntheir use of drugs, alcohol, and tobacco, their perceptions of the<br />\nrisks involved, and personal and family income sources and<br />\namounts. Demographic data include gender, race, age, ethnicity,<br />\nmarital status, motor vehicle use, educational level, job status,<br />\nincome level, veteran status, past and current household composition,<br />\nand population density.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1985) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1985-nid13542",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1985-nid13542"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1985-nid13542",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "alcohol consumption",
@@ -8039,41 +8052,40 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1985",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1985-nid13542",
-            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, tobacco, and nonmedical use of<br />\nprescription drugs among members of United States households aged 12<br />\nand older. Questions include age at first use as well as lifetime,<br />\nannual, and past-month usage for the following drug classes: cannabis,<br />\ncocaine, hallucinogens, heroin, inhalants, alcohol, tobacco,<br />\nnonmedical use of prescription drugs including psychotherapeutics, and<br />\npolysubstance use. Respondents were also asked about health<br />\nconditions, substance abuse treatment history, problems resulting from<br />\ntheir use of drugs, alcohol, and tobacco, their perceptions of the<br />\nrisks involved, and personal and family income sources and<br />\namounts. Demographic data include gender, race, age, ethnicity,<br />\nmarital status, motor vehicle use, educational level, job status,<br />\nincome level, veteran status, past and current household composition,<br />\nand population density.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1985)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1985-nid13542",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1985) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1985-nid13542"
-                }
-            ]
+            "title": "National Household Survey on Drug Abuse (NHSDA-1985)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-intimate-partner-and-sexual-violence-survey-nisvs",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "nisvs@cdc.gov",
+                "hasEmail": "mailto:nisvs@cdc.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The National Intimate Partner and Sexual Violence Survey (NISVS) is an ongoing, nationally representative survey to assess experiences of intimate partner violence, sexual violence and stalking among adults in the United States. It measures lifetime victimization for these types of violence as well as in the previous 12 months. In 2010, a total of 18,049 interviews from the general population sample were conducted.</p>\n<p>Raw data are currently unavailable. State report tables are available in pdf format. Other key statistics are included in the summary and full reports.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/violenceprevention/pdf/cdc_nisvs_digest_final-a.pdf",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "identifier": "527a13e1-5633-420e-a300-67c057fb44f8",
             "issued": "2014-04-08",
-            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "adolescent",
                 "adult",
@@ -8096,111 +8108,81 @@
                 "violence statistics   numerical data",
                 "young adult"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "nisvs@cdc.gov",
-                "hasEmail": "mailto:nisvs@cdc.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-intimate-partner-and-sexual-violence-survey-nisvs",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "527a13e1-5633-420e-a300-67c057fb44f8",
-            "description": "<p>The National Intimate Partner and Sexual Violence Survey (NISVS) is an ongoing, nationally representative survey to assess experiences of intimate partner violence, sexual violence and stalking among adults in the United States. It measures lifetime victimization for these types of violence as well as in the previous 12 months. In 2010, a total of 18,049 interviews from the general population sample were conducted.</p>\n<p>Raw data are currently unavailable. State report tables are available in pdf format. Other key statistics are included in the summary and full reports.</p>",
-            "title": "National Intimate Partner and Sexual Violence Survey (NISVS)",
-            "programCode": [
-                "009:031"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.cdc.gov/violenceprevention/pdf/cdc_nisvs_digest_final-a.pdf",
-                    "mediaType": "text/html",
-                    "title": "Text "
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
             "theme": [
                 "Health",
                 "State"
-            ]
+            ],
+            "title": "National Intimate Partner and Sexual Violence Survey (NISVS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3r6w-uyfn",
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
-            "identifier": "95e685aa-6e0e-51c0-b4ab-2dd1a229c18a",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet pillar v2.10.64 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
-                    "description": "CoreSet pillar v2.10.64 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet pillar v2.10.64 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet pillar v2.10.64 (coreset-etl-test)"
                 }
             ],
+            "identifier": "95e685aa-6e0e-51c0-b4ab-2dd1a229c18a",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/3r6w-uyfn",
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
+            "title": "CoreSet pillar v2.10.64 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3r7e-bsui",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
-            "keyword": [
-                "chip",
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
-            "identifier": "b9e18d80-c765-4fb9-95e7-81951e01a6a3",
             "description": "This data set includes annual counts and percentages of Medicaid and Children\u2019s Health Insurance Program (CHIP) enrollees by race and ethnicity overall and by three subpopulation topics: scope of Medicaid and CHIP benefits, age group, and eligibility category. \r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, and Puerto Rico who were enrolled for at least one day in the calendar year. Enrollees in Guam, American Samoa, the Northern Mariana Islands, and the U.S. Virgin Islands are not included. Results shown for the age group and eligibility category subpopulation topics only include enrollees with comprehensive Medicaid and CHIP benefits in the year. Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on information shown in the brief: \"Race and ethnicity of the national Medicaid and CHIP population in 2020.\" Enrollees are assigned to six race and ethnicity categories using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG). Enrollees are assigned to a child (ages 0-18) or adult (ages 19 and older) subpopulation using age as of December 31st of the calendar year. Enrollees are assigned to the comprehensive benefits or limited benefits subpopulation according to the criteria in the \"Identifying Beneficiaries with Full-Scope, Comprehensive, and Limited Benefits in the TAF\" DQ Atlas brief. Enrollees are assigned to an eligibility category subpopulation using their latest reported eligibility group code, CHIP code, and age in the calendar year. Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
-            "title": "Race and ethnicity of the national Medicaid and CHIP population",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8208,40 +8190,38 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "b9e18d80-c765-4fb9-95e7-81951e01a6a3",
+            "issued": "2025-01-17",
+            "keyword": [
+                "chip",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/3r7e-bsui",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-16",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Race and ethnicity of the national Medicaid and CHIP population"
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
-            "identifier": "https://data.cdc.gov/api/views/2snk-eav4",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Ind/2snk-eav4",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation \u2013 Smokefree Indoor Air. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to state legislation on smokefree indoor air in private worksites, restaurants, and bars.",
-            "title": "CDC STATE System Tobacco Legislation - Smokefree Indoor Air Summary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8264,40 +8244,43 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Ind/2snk-eav4",
+            "identifier": "https://data.cdc.gov/api/views/2snk-eav4",
+            "issued": "2023-07-19",
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
+            "title": "CDC STATE System Tobacco Legislation - Smokefree Indoor Air Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/5nuu-6upy",
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
-            "identifier": "https://data.cdc.gov/api/views/5nuu-6upy",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014,  Region 10 - Seattle",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8320,21 +8303,58 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/5nuu-6upy",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/5nuu-6upy",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014,  Region 10 - Seattle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.insurekidsnow.gov/",
             "bureauCode": [
                 "009:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "IKN Technical Help",
+                "hasEmail": "mailto:IKNTechnicalHelp@hrsa.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Insure Kids Now (IKN) Dental Care Providers in Your State locator provides profile information for oral health providers participating in Medicaid and Children's Health Insurance Program (CHIP) and descriptions of oral health services covered under each Medicaid/CHIP plan. Current and prospective beneficiaries can use this website to search for providers and learn about Programs/Health Plans offered in their resident State. The data for this application is updated at least on a quarter-annual basis.</p>\n<p>Insure Kids Now operates in accordance with the Children's Health Insurance Program Reauthorization Act of 2009 (CHIPRA) and the Centers for Medicare and Medicaid Services (CMS). This service is a partnership between CMS and HRSA.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Insure Kids Now Dental Locator \n",
+                    "downloadURL": "https://www.insurekidsnow.gov/state/find-a-dentist/index.html",
+                    "mediaType": "text/html",
+                    "title": "Insure Kids Now - Find a Dentist"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Find information on health insurance programs and dental providers in your state \n",
+                    "downloadURL": "https://www.insurekidsnow.gov/state/find-a-dentist/index.html",
+                    "mediaType": "application/unknown",
+                    "title": "Insure Kids Now - Find programs in your state"
+                }
+            ],
+            "identifier": "29c1a870-208b-48a5-8e80-eeb5e2f02aab",
             "issued": "2012-05-30",
-            "temporal": "2009-01-01T00:00:00-05:00/2009-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "checkups",
                 "child health care",
@@ -8348,55 +8368,48 @@
                 "low income",
                 "treatment"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "IKN Technical Help",
-                "hasEmail": "mailto:IKNTechnicalHelp@hrsa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Health Resources and Services Administration"
-            },
-            "identifier": "29c1a870-208b-48a5-8e80-eeb5e2f02aab",
-            "description": "<p>The Insure Kids Now (IKN) Dental Care Providers in Your State locator provides profile information for oral health providers participating in Medicaid and Children's Health Insurance Program (CHIP) and descriptions of oral health services covered under each Medicaid/CHIP plan. Current and prospective beneficiaries can use this website to search for providers and learn about Programs/Health Plans offered in their resident State. The data for this application is updated at least on a quarter-annual basis.</p>\n<p>Insure Kids Now operates in accordance with the Children's Health Insurance Program Reauthorization Act of 2009 (CHIPRA) and the Centers for Medicare and Medicaid Services (CMS). This service is a partnership between CMS and HRSA.</p>",
-            "title": "Insure Kids Now (IKN) (Dental Care Providers)",
+            "landingPage": "https://www.insurekidsnow.gov/",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:075"
             ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.insurekidsnow.gov/state/find-a-dentist/index.html",
-                    "description": "Insure Kids Now Dental Locator \n",
-                    "@type": "dcat:Distribution",
-                    "title": "Insure Kids Now - Find a Dentist"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Health Resources and Services Administration"
             },
-                {
-                    "mediaType": "application/unknown",
-                    "downloadURL": "https://www.insurekidsnow.gov/state/find-a-dentist/index.html",
-                    "description": "Find information on health insurance programs and dental providers in your state \n",
-                    "@type": "dcat:Distribution",
-                    "title": "Insure Kids Now - Find programs in your state"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "temporal": "2009-01-01T00:00:00-05:00/2009-01-01T00:00:00-05:00",
             "theme": [
                 "Community",
                 "Health"
-            ]
+            ],
+            "title": "Insure Kids Now (IKN) (Dental Care Providers)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/doc2016_clas.pdf",
+            "accrualPeriodicity": "Survey will not be updated.",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "In 2016, a total of 397 questionnaires were received from physicians who participated in the National CLAS Physician Survey. The basic sampling unit for the National CLAS Physician Survey is the physician. The sampling  frame for the National CLAS Physician Survey included non-federally employed physicians  classified by the American Medical Association (AMA) or the American Osteopathic Association  (AOA) as \"office-based, patient care\" and physicians classified as hospital-employed by the AMA.  Physicians in the specialties of anesthesiology, pathology, and radiology were excluded from the  physician universe.",
+            "description": "The purpose of the National CLAS Physician Survey was to understand the provision of culturally and linguistically appropriate services among office-based physicians. The National CLAS Physician Survey was a supplement to the National Ambulatory Medical Care Survey (NAMCS), which is a national probability sample survey of visits to office-based physicians. NAMCS is a component of the National Health Care Surveys that measured health care utilization across a variety of health care providers\u2019 settings. NAMCS and the National CLAS Physician Survey were conducted by the National Center for Health Statistics (NCHS). The National CLAS Physician Survey public use file includes data from office-based physicians. No patient level data were collected. This documentation describes the public use micro-data file produced from data collected in the National CLAS Physician Survey.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Standard Application process link attached.",
+                    "downloadURL": "https://www.cdc.gov/rdc/index.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/feiy-rryn",
+            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/doc2016_clas.pdf; https://www.cdc.gov/nchs/data/ahcd/2016_NAMCS_CLAS_Sample_Card.pdf; https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/readme2016_clas.txt;",
             "issued": "2018-11-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2016",
-            "modified": "2024-02-29",
             "keyword": [
                 "cultural-health-beliefs",
                 "health-practices",
@@ -8406,47 +8419,47 @@
                 "preferred-languages",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/doc2016_clas.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-02-29",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/feiy-rryn",
-            "description": "The purpose of the National CLAS Physician Survey was to understand the provision of culturally and linguistically appropriate services among office-based physicians. The National CLAS Physician Survey was a supplement to the National Ambulatory Medical Care Survey (NAMCS), which is a national probability sample survey of visits to office-based physicians. NAMCS is a component of the National Health Care Surveys that measured health care utilization across a variety of health care providers\u2019 settings. NAMCS and the National CLAS Physician Survey were conducted by the National Center for Health Statistics (NCHS). The National CLAS Physician Survey public use file includes data from office-based physicians. No patient level data were collected. This documentation describes the public use micro-data file produced from data collected in the National CLAS Physician Survey.",
-            "title": "National Ambulatory Medical Care Survey: Culturally and Linguistically Appropriate Services Supplement, 2016 Restricted-data",
-            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/doc2016_clas.pdf; https://www.cdc.gov/nchs/data/ahcd/2016_NAMCS_CLAS_Sample_Card.pdf; https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/readme2016_clas.txt;",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/index.htm",
-                    "mediaType": "text/html",
-                    "description": "Standard Application process link attached."
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "describedBy": "In 2016, a total of 397 questionnaires were received from physicians who participated in the National CLAS Physician Survey. The basic sampling unit for the National CLAS Physician Survey is the physician. The sampling  frame for the National CLAS Physician Survey included non-federally employed physicians  classified by the American Medical Association (AMA) or the American Osteopathic Association  (AOA) as \"office-based, patient care\" and physicians classified as hospital-employed by the AMA.  Physicians in the specialties of anesthesiology, pathology, and radiology were excluded from the  physician universe.",
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "Survey will not be updated.",
+            "temporal": "2016",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey: Culturally and Linguistically Appropriate Services Supplement, 2016 Restricted-data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2010",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2010) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2010-nid13593",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2010-nid13593"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2010-nid13593",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -8459,59 +8472,30 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2010",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2010-nid13593",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2010)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2010-nid13593",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2010) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2010-nid13593"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2010)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3tha-57c6",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2024-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-23",
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
-            "identifier": "99315a95-37ac-4eee-946a-3c523b4c481e",
             "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
-            "title": "NADAC (National Average Drug Acquisition Cost) 2024",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8519,97 +8503,87 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "99315a95-37ac-4eee-946a-3c523b4c481e",
+            "issued": "2024-01-03",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "landingPage": "https://healthdata.gov/d/3tha-57c6",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2024-12-23",
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
+            "title": "NADAC (National Average Drug Acquisition Cost) 2024"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3u8b-2i5p",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2023-06-25",
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
-            "identifier": "3aa5d241-b6e1-5614-8313-1088c06c7509",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "Scorecard version v2.11.16 (dev)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/version.csv",
-                    "description": "Scorecard version v2.11.16 (dev)",
                     "@type": "dcat:Distribution",
+                    "description": "Scorecard version v2.11.16 (dev)",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/version.csv",
+                    "mediaType": "text/csv",
                     "title": "Scorecard version v2.11.16 (dev)"
                 }
             ],
+            "identifier": "3aa5d241-b6e1-5614-8313-1088c06c7509",
+            "issued": "2023-06-25",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/3u8b-2i5p",
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
+            "title": "Scorecard version v2.11.16 (dev)"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -8632,25 +8606,61 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://www.healthit.gov/data/datasets/strategic-health-it-advanced-research-projects-sharp-output-inventory",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2014-09-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/strategic-health-it-advanced-research-projects-sharp-program"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/strategic-health-it-advanced-research-projects-sharp-output-inventory",
+            "description": "ONC established the SHARP program to support innovative research and to address well-documented problems that impede the adoption and use of health IT. The program covers four subject areas managed by four distinct project groups: health IT security (SHARPS), patient-centered cognitive support (SHARPc), health care application and network design (SMART), and secondary use of EHR information (SHARPn). This dataset provides the full inventory of project outputs from the SHARP program, ranging from presentations and manuscripts to APIs and software.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/sharp-projects-outputs.csv",
+                    "mediaType": "text/csv",
+                    "title": "sharp-projects-outputs.csv"
+                }
             ],
+            "identifier": "qn0t3pcy-5dzz-6msx-hscw-qu1jb9837oaj",
+            "issued": "2023-10-03",
             "keyword": [
                 "ehr",
                 "health it",
@@ -8661,114 +8671,80 @@
                 "sharp",
                 "strategic health it advanced research projects"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/strategic-health-it-advanced-research-projects-sharp-output-inventory",
+            "modified": "2014-09-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "qn0t3pcy-5dzz-6msx-hscw-qu1jb9837oaj",
-            "description": "ONC established the SHARP program to support innovative research and to address well-documented problems that impede the adoption and use of health IT. The program covers four subject areas managed by four distinct project groups: health IT security (SHARPS), patient-centered cognitive support (SHARPc), health care application and network design (SMART), and secondary use of EHR information (SHARPn). This dataset provides the full inventory of project outputs from the SHARP program, ranging from presentations and manuscripts to APIs and software.",
-            "title": "Strategic Health IT Advanced Research Projects (SHARP) Output Inventory",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/sharp-projects-outputs.csv",
-                    "mediaType": "text/csv",
-                    "title": "sharp-projects-outputs.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/quickstats/strategic-health-it-advanced-research-projects-sharp-program"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/strategic-health-it-advanced-research-projects-sharp-output-inventory"
+            "title": "Strategic Health IT Advanced Research Projects (SHARP) Output Inventory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3vbh-rieb",
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
-            "identifier": "c5a62c7c-5c25-5ba3-b3f3-82f7f9c5a9a3",
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
+            "identifier": "c5a62c7c-5c25-5ba3-b3f3-82f7f9c5a9a3",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/3vbh-rieb",
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
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/data-linkage/va-restricted.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-09-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2005/2020",
-            "modified": "2024-10-11",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/va-match-status-all.pdf"
-            ],
-            "keyword": [
-                "linked va files",
-                "nchs surveys",
-                "research-data-center",
-                "veterans"
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
-            "identifier": "https://data.cdc.gov/api/views/nxu4-tewx",
-            "description": "NCHS has linked 2005-2018 National Health Interview Survey (NHIS) and 2005-2018 National Health and Nutrition Examination Survey (NHANES) to Department of Veterans Affairs (VA) administrative data through fiscal year 2020. Linkage of NCHS survey participants with VA administrative data provides the opportunity to examine a wide range of health-related topics for Veterans, including Veteran status and utilization of VA benefit programs.",
-            "title": "NCHS Survey Data Linked to Department of Veterans Affairs Administrative Data Files",
-            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/va-match-status-all.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "NCHS has linked 2005-2018 National Health Interview Survey (NHIS) and 2005-2018 National Health and Nutrition Examination Survey (NHANES) to Department of Veterans Affairs (VA) administrative data through fiscal year 2020. Linkage of NCHS survey participants with VA administrative data provides the opportunity to examine a wide range of health-related topics for Veterans, including Veteran status and utilization of VA benefit programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8776,42 +8752,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/va-match-status-all.pdf",
+            "identifier": "https://data.cdc.gov/api/views/nxu4-tewx",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-09-16",
+            "keyword": [
+                "linked va files",
+                "nchs surveys",
+                "research-data-center",
+                "veterans"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/va-restricted.htm",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/va-match-status-all.pdf"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "2005/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Survey Data Linked to Department of Veterans Affairs Administrative Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/j8jk-5ztv",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-08-01",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "adults",
-                "brfss",
-                "current smokers"
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
-            "identifier": "https://data.cdc.gov/api/views/j8jk-5ztv",
             "description": "Percentages are weighted to population characteristics. Data are not available if it did not meet BRFSS stability requirements.For more information on these requirements, as well as risk factors and calculated variables, see the Technical Documents and Survey Data for a specific year - http://www.cdc.gov/brfss/annual_data/annual_data.htm.Recommended citation: Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, [appropriate year].",
-            "title": "BRFSS Prevalence And Trends Data: Tobacco Use - Adults Who Are Current Smokers for 1995-2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8834,42 +8816,41 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/j8jk-5ztv",
+            "issued": "2013-08-01",
+            "keyword": [
+                "adults",
+                "brfss",
+                "current smokers"
+            ],
+            "landingPage": "https://data.cdc.gov/d/j8jk-5ztv",
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
+            "title": "BRFSS Prevalence And Trends Data: Tobacco Use - Adults Who Are Current Smokers for 1995-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-02-09",
-            "temporal": "2019-2021",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-30",
-            "keyword": [
-                "ethnicity",
-                "nhis",
-                "race",
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
-            "identifier": "https://data.cdc.gov/api/views/krhz-spsc",
             "description": "Interactive Summary Health Statistics for Adults, by Detailed Race and Ethnicity provide estimates as three-year averages of selected health topics for adults aged 18 years and over based on final data from the National Health Interview Survey.",
-            "title": "NHIS Adult 3-Year Summary Health Statistics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8892,54 +8873,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/krhz-spsc",
+            "issued": "2022-02-09",
+            "keyword": [
+                "ethnicity",
+                "nhis",
+                "race",
+                "summary health statistics"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-03-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "temporal": "2019-2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NHIS Adult 3-Year Summary Health Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "api",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qbit-hxvw",
             "description": "Not all articles in PMC are available for text mining and other reuse, many have copyright protection, however articles in the PMC Open Access Subset are made available for download under a Creative Commons or similar license that generally allows more liberal redistribution and reuse than a traditional copyrighted work.",
-            "title": "PubMed Central Open Access Subset (PMC OA)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/",
-                    "description": "The AWS RODA, PMC OAI service, the PMC FTP service and BioC API are the only services that may be used for automated downloading of PMC content. Systematic retrieval (or bulk downloading) of articles through any other automated process is prohibited.",
                     "@type": "dcat:Distribution",
+                    "description": "The AWS RODA, PMC OAI service, the PMC FTP service and BioC API are the only services that may be used for automated downloading of PMC content. Systematic retrieval (or bulk downloading) of articles through any other automated process is prohibited.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/",
+                    "mediaType": "text/html",
                     "title": "Query Interface - PubMed Central Open Access Subset (PMC OA)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/pmcaws/",
-                    "description": "PubMed Central (PMC) has several datasets of articles hosted the cloud and listed in the Registry of Open Data on Amazon Web Services (AWS), all of which can be accessed freely, without charge, through either an HTTPS or S3 URL. The datasets of articles are organized on AWS based on their license type: PMC Open Access (OA) Subset - all articles in PMC with a machine-readable Creative Commons license",
                     "@type": "dcat:Distribution",
+                    "description": "PubMed Central (PMC) has several datasets of articles hosted the cloud and listed in the Registry of Open Data on Amazon Web Services (AWS), all of which can be accessed freely, without charge, through either an HTTPS or S3 URL. The datasets of articles are organized on AWS based on their license type: PMC Open Access (OA) Subset - all articles in PMC with a machine-readable Creative Commons license",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/pmcaws/",
+                    "mediaType": "text/html",
                     "title": "PMC Article Datasets in the AWS Cloud"
                 },
                 {
@@ -8949,110 +8931,103 @@
                     "title": "Open Access (OA) Subset Individual Article Download (FTP)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/oai/",
-                    "description": "The PubMed Central OAI-PMH service (PMC-OAI) provides access to metadata of all items in the PubMed Central (PMC) archive, as well as to the full text of a subset of these items. PMC-OAI is an implementation of the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH), a standard for retrieving metadata from digital document repositories. Visit the Open Archives Initiative site for more information about the protocol and other activities of the OAI group. PMC-OAI supports OAI-PMH version 2.0. It does not support earlier versions of the protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "The PubMed Central OAI-PMH service (PMC-OAI) provides access to metadata of all items in the PubMed Central (PMC) archive, as well as to the full text of a subset of these items. PMC-OAI is an implementation of the Open Archives Initiative Protocol for Metadata Harvesting (OAI-PMH), a standard for retrieving metadata from digital document repositories. Visit the Open Archives Initiative site for more information about the protocol and other activities of the OAI group. PMC-OAI supports OAI-PMH version 2.0. It does not support earlier versions of the protocol.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pmc/tools/oai/",
+                    "mediaType": "text/html",
                     "title": "OAI-PMH Service"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/research/bionlp/APIs/BioC-PMC/",
-                    "description": "All the PubMed Central (PMC) Open Access articles are available in the BioC format. This provides a large number of full text research articles for text mining and information retrieval research. BioC is a simple format designed for straightforward text processing. These articles are available in BioC XML or BioC JSON, in Unicode or ASCII, and via PubMed ID or PMC ID.",
                     "@type": "dcat:Distribution",
+                    "description": "All the PubMed Central (PMC) Open Access articles are available in the BioC format. This provides a large number of full text research articles for text mining and information retrieval research. BioC is a simple format designed for straightforward text processing. These articles are available in BioC XML or BioC JSON, in Unicode or ASCII, and via PubMed ID or PMC ID.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/research/bionlp/APIs/BioC-PMC/",
+                    "mediaType": "text/html",
                     "title": "BioC API for PMC"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/qbit-hxvw",
+            "issued": "2021-08-26",
+            "keyword": [
+                "api",
+                "dataset",
+                "literature"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/",
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
+            "title": "PubMed Central Open Access Subset (PMC OA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/3wwn-xcgc",
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
-            "identifier": "cfaaa35e-901c-5d78-a11d-b8e59d0225f5",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_measure_backgroundAndMethods",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_backgroundAndMethods.csv",
-                    "description": "{\"dataset\": \"measure_backgroundAndMethods\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_backgroundAndMethods\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_backgroundAndMethods.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_backgroundAndMethods csv file"
                 }
             ],
+            "identifier": "cfaaa35e-901c-5d78-a11d-b8e59d0225f5",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/3wwn-xcgc",
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
+            "title": "devAuto_measure_backgroundAndMethods"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-04-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
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
-            "identifier": "https://data.cdc.gov/api/views/pj7m-y5uh",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis data file contains the following indicators that can be used to illustrate potential differences in the burden of deaths due to COVID-19 according to race and ethnicity:\ncount of COVID-19 deaths, distribution of COVID-19 deaths, unweighted distribution of population, and weighted distribution of population.",
-            "title": "Provisional COVID-19 Deaths: Distribution of Deaths by Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9075,61 +9050,94 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/pj7m-y5uh",
+            "issued": "2020-04-13",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
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
+            "title": "Provisional COVID-19 Deaths: Distribution of Deaths by Race and Hispanic Origin"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/repository-evaluation-reports-0",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OIG Public Affairs",
+                "hasEmail": "mailto:public.affairs@oig.hhs.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>To inform the HHS, Congress, and the public about the efficiency, effectiveness, and integrity of HHS programs and to recommend actions to promote those goals.</p>",
+            "identifier": "01f61930-6f40-4ea4-a95c-27204e377b8e",
             "issued": "2013-03-25",
-            "temporal": "1998-01-01T00:00:00-05:00/1998-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "health care cost",
                 "medicaid",
                 "medicare",
                 "office-of-inspector-general"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OIG Public Affairs",
-                "hasEmail": "mailto:public.affairs@oig.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/repository-evaluation-reports-0",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:109"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Inspector General"
             },
-            "identifier": "01f61930-6f40-4ea4-a95c-27204e377b8e",
-            "description": "<p>To inform the HHS, Congress, and the public about the efficiency, effectiveness, and integrity of HHS programs and to recommend actions to promote those goals.</p>",
-            "title": "Repository of Evaluation Reports",
-            "programCode": [
-                "009:109"
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "temporal": "1998-01-01T00:00:00-05:00/1998-01-01T00:00:00-05:00",
+            "title": "Repository of Evaluation Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.healthit.gov/data/datasets/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2014-01-01",
-            "references": [
-                "https://www.healthit.gov/data/quickstats/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency-1",
-                "https://www.healthit.gov/data/quickstats/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency",
-                "https://www.healthit.gov/data/quickstats/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency-0"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "describedBy": "https://www.healthit.gov/data/datasets/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency",
+            "description": "The Updated Systematic Review reviews the January 2010 to August 2013 health IT literature to examine the effects of health IT across three aspects of care: efficiency, quality, and safety. This report updates previous systematic reviews of the health IT literature, focusing specifically on identifying and summarizing the evidence related to the use of health IT as outlined in the Meaningful Use regulations. The review examined the literature to determine the article authors' findings related to the effects or associations of a meaningful use functionality on an aspect of care. Each article's findings was scored as positive (defined as: health IT improved key aspect of care but none worse off), mixed-positive (defined as: positive effects of health IT outweight negative effects), neutral (defined as: health IT not associated with change in outcome), or negative (defined as: negative effects of health IT on outcome). The full review data: article, related meaningful use functionality, aspect of care, and author sentiment are provided in this dataset.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/systematic-lit-review-appendix.csv",
+                    "mediaType": "text/csv",
+                    "title": "systematic-lit-review-appendix.csv"
+                }
             ],
+            "identifier": "wzhfo0gu-gr6b-767p-cts4-7reu5e5mx4po",
+            "issued": "2023-10-03",
             "keyword": [
                 "ehr",
                 "functionalities",
@@ -9139,68 +9147,35 @@
                 "public health measures",
                 "regulations"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ONC Request",
-                "hasEmail": "mailto:onc.request@hhs.gov"
-            },
+            "landingPage": "https://www.healthit.gov/data/datasets/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency",
+            "modified": "2014-01-01",
+            "programCode": [
+                "009:110"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the National Coordinator for Health Information Technology"
             },
-            "identifier": "wzhfo0gu-gr6b-767p-cts4-7reu5e5mx4po",
-            "description": "The Updated Systematic Review reviews the January 2010 to August 2013 health IT literature to examine the effects of health IT across three aspects of care: efficiency, quality, and safety. This report updates previous systematic reviews of the health IT literature, focusing specifically on identifying and summarizing the evidence related to the use of health IT as outlined in the Meaningful Use regulations. The review examined the literature to determine the article authors' findings related to the effects or associations of a meaningful use functionality on an aspect of care. Each article's findings was scored as positive (defined as: health IT improved key aspect of care but none worse off), mixed-positive (defined as: positive effects of health IT outweight negative effects), neutral (defined as: health IT not associated with change in outcome), or negative (defined as: negative effects of health IT on outcome). The full review data: article, related meaningful use functionality, aspect of care, and author sentiment are provided in this dataset.",
-            "title": "Effects of Meaningful Use Functionalities on Health Care Quality, Safety, and Efficiency",
-            "programCode": [
-                "009:110"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/systematic-lit-review-appendix.csv",
-                    "mediaType": "text/csv",
-                    "title": "systematic-lit-review-appendix.csv"
-                }
+            "references": [
+                "https://www.healthit.gov/data/quickstats/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency-1",
+                "https://www.healthit.gov/data/quickstats/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency",
+                "https://www.healthit.gov/data/quickstats/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency-0"
             ],
-            "describedBy": "https://www.healthit.gov/data/datasets/effects-meaningful-use-functionalities-health-care-quality-safety-and-efficiency"
+            "title": "Effects of Meaningful Use Functionalities on Health Care Quality, Safety, and Efficiency"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -9223,56 +9198,49 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -9295,41 +9263,57 @@
                     "mediaType": "application/xml"
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
+            "modified": "2025-01-24",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://healthdata.gov/dataset/neuroimaging-informatics-tools-and-resources-clearinghouse-nitrc",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-07-09",
-            "temporal": "2007-01-01T00:00:00-05:00/2007-01-10T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "biomedical research",
-                "neuroimaging"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NITRC Info",
                 "hasEmail": "mailto:nitrcinfo@nitrc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
-            },
-            "identifier": "ec022df2-4230-4a24-9416-69efa6fd476a",
+            "dataQuality": true,
+            "describedBy": "http://www.nitrc.org/",
             "description": "<p>The Neuroimaging Informatics Tools and Resources Clearinghouse (NITRC) facilitates finding and comparing neuroimaging resources for functional and structural neuroimaging analyses\u2014including popular tools as well as those that once might have been hidden in another researcher's laboratory or some obscure corner of cyberspace. NITRC collects and points to standardized information about tools, making the task of finding and comparing them easier than before. The site can help researchers find the right functional or structural neuroimaging tool or resource for their research. NITRC has recently added services such as cloud-based computing and data storage, and is broadening the range of scientific domains from MR to PET, SPECT, CT, MEG/EEG and optical imaging. Additional domains of interest are digital atlasing, and computational neuroscience, including large-scale and multi-scale modeling. The NITRC team searches out relevant research tools and resources to house on the site. Researchers can compare tools on NITRC and developers can seek and receive help from the community to make their tools more usable and accessible.</p>",
-            "title": "Neuroimaging Informatics Tools and Resources Clearinghouse (NITRC)",
-            "programCode": [
-                "009:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9338,44 +9322,37 @@
                     "title": "API "
                 }
             ],
-            "describedBy": "http://www.nitrc.org/",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "ec022df2-4230-4a24-9416-69efa6fd476a",
+            "issued": "2013-07-09",
+            "keyword": [
+                "biomedical research",
+                "neuroimaging"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/neuroimaging-informatics-tools-and-resources-clearinghouse-nitrc",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
+            },
+            "temporal": "2007-01-01T00:00:00-05:00/2007-01-10T00:00:00-05:00",
+            "title": "Neuroimaging Informatics Tools and Resources Clearinghouse (NITRC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mvaf-qxac",
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
-            "identifier": "https://data.cdc.gov/api/views/mvaf-qxac",
             "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 In previous years, cases were reported as Salmonellosis. Beginning in January 2019, cases began to be reported as Salmonella Paratyphi infection.\n\u00b6 In previous years, cases were reported as typhoid fever. Beginning in January 2019, cases began to be reported as Salmonella Typhi infection.\n** In previous years, cases were reported as Salmonellosis (excluding paratyphoid fever and typhoid fever). Beginning in January 2019, cases began to be reported as Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection).",
-            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9398,53 +9375,54 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mvaf-qxac",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonella paratyphi infection",
+                "salmonella typhi infection",
+                "salmonellosis (excluding salmonella typhi infection and salmonella paratyphi infection)",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mvaf-qxac",
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
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-aligned-beneficiaries",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/1cd9eded-d2c9-4215-a064-aac6dae3b714/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-reach-aligned-beneficiaries-data-dictionary",
             "description": "The Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Aligned Beneficiary Public Use File (PUF) data details Medicare Beneficiaries aligned to the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model, including counties, eligibility months and total aligned beneficiaries. This data is redacted and does not include identifiable information.",
-            "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1cd9eded-d2c9-4215-a064-aac6dae3b714/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1cd9eded-d2c9-4215-a064-aac6dae3b714/data",
+                    "mediaType": "text/html",
                     "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries : 2021-12-31"
                 },
                 {
@@ -9460,44 +9438,50 @@
                     "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries : 2021-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/aco-reach-aligned-beneficiaries-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/1cd9eded-d2c9-4215-a064-aac6dae3b714/data-viewer",
+            "issued": "2023-05-26",
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-aligned-beneficiaries",
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
+            "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/xtvu-8j6w",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2023-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-06",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xtvu-8j6w",
             "description": "*A file containing all Min/Max Baseline Reports for 2005-2023 in their original format is available in the <b>Attachments</b> section below. A second file includes a separate set of reports, made available from 2002-2017, that did not include OLDMEDLINE records.* \n\nMEDLINE/PubMed annual statistical reports are based upon the data elements in the baseline versions of MEDLINE\u00ae/PubMed are available. For each year covered the reports include: total citations containing each element; total occurrences of each element; minimum/average/maximum occurrences of each element in a record; minimum/average/maximum length of a single element occurrence; average record size; and other statistical data describing the content and size of the elements.",
-            "title": "MEDLINE/PubMed Baseline Statistics: Min/Max Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9520,43 +9504,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xtvu-8j6w",
+            "issued": "2023-03-21",
+            "keyword": [
+                "pubmed"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/xtvu-8j6w",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2024-09-06",
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
+            "title": "MEDLINE/PubMed Baseline Statistics: Min/Max Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jr58-6ysp",
+            "accrualPeriodicity": "Two Weeks",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "covid-19",
-                "nowcasting",
-                "sars-cov-2",
-                "surveillance",
-                "variant proportion",
-                "variant surveillance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Clinton Paden",
                 "hasEmail": "mailto:respvirus@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/jr58-6ysp",
             "description": "To identify and track SARS-CoV-2 variants, CDC uses genomic surveillance. CDC's national genomic surveillance system collects SARS-CoV-2 specimens for sequencing through the National SARS-CoV-2 Strain Surveillance (NS3) program, as well as SARS-CoV-2 sequences generated by commercial or academic laboratories contracted by CDC and state or local public health laboratories. Viral genomic sequences are analyzed and classified as a particular variant. The proportions of variants in a population are estimated nationally, by HHS region, and by jurisdiction. The thousands of sequences analyzed every week through CDC\u2019s national genomic sequencing and bioinformatics efforts fuel this comprehensive and population-based U.S. surveillance system established to identify and monitor the spread of variants.\n\nThese data appear on the CDC COVID Data Tracker at the following URL: <a href=\"https://covid.cdc.gov/covid-data-tracker/#variant-proportions\">https://covid.cdc.gov/covid-data-tracker/#variant-proportions</a>\n\n\nFor more information on how these data are generated and used to provide estimates of variant proportions, please see the following references:\n\n<ul>\n<li>Paul P, France AM, Aoki Y, et al. Genomic Surveillance for SARS-CoV-2 Variants Circulating in the United States, December 2020\u2013May 2021. MMWR Morb Mortal Wkly Rep 2021;70:846\u2013850. DOI: <a href=\"http://dx.doi.org/10.15585/mmwr.mm7023a3\">http://dx.doi.org/10.15585/mmwr.mm7023a3</a></li>\n<li>Lambrou AS, Shirk P, Steele MK, et al. Genomic Surveillance for SARS-CoV-2 Variants: Predominance of the Delta (B.1.617.2) and Omicron (B.1.1.529) Variants \u2014 United States, June 2021\u2013January 2022. MMWR Morb Mortal Wkly Rep 2022;71:206\u2013211. DOI: <a href=\"http://dx.doi.org/10.15585/mmwr.mm7106a4\">http://dx.doi.org/10.15585/mmwr.mm7106a4</a></li></ul>",
-            "title": "SARS-CoV-2 Variant Proportions",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9579,49 +9559,45 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/jr58-6ysp",
+            "issued": "2024-09-30",
+            "keyword": [
+                "covid-19",
+                "nowcasting",
+                "sars-cov-2",
+                "surveillance",
+                "variant proportion",
+                "variant surveillance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/jr58-6ysp",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Two Weeks",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States",
             "theme": [
                 "Laboratory Surveillance"
-            ]
+            ],
+            "title": "SARS-CoV-2 Variant Proportions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wi5c-cscz",
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
-            "identifier": "https://data.cdc.gov/api/views/wi5c-cscz",
             "description": "CDC is collaborating with the National Institutes of Health (NIH), the Food and Drug Administration (FDA), Vitalant Research Institute (VRI), Westat Inc., and numerous blood collection organizations across the United States to conduct a nationwide COVID-19 seroprevalence survey of blood donors. This is the largest nationwide COVID-19 seroprevalence survey to date. De-identified blood samples are tested for antibodies to SARS-CoV-2 to better understand the percentage of people in the United States who have antibodies against SARS-CoV-2 (the virus that causes COVID-19) and to track how this percentage changes over time. Both SARS-CoV-2 infection and COVID-19 vaccines currently used in the United States result in production of anti-spike (anti-S) antibodies but only infection results in production of anti-nucleocapsid (anti-N) antibodies. Combined seroprevalence estimates the proportion of the population with evidence of previous SARS-CoV-2 infection, COVID-19 vaccination, or both. It estimates the proportion of the population with some presumed protection against infection with the virus that causes COVID-19. The term \u201ccombined seroprevalence\u201d refers to the combined infection- and vaccination-induced SARS-CoV-2 seroprevalences. This is the population that has  anti-S antibodies, regardless of the presence of anti-N antibodies.\n\nThis link connects to a webpage that displays the data from the Nationwide Blood Donor Seroprevalence Survey. It offers an interactive visualization available at https://covid.cdc.gov/covid-data-tracker/#nationwide-blood-donor-seroprevalence\n\nAdditional information is available at: https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/blood-bank-serosurvey.html",
-            "title": "2020-2021 Nationwide Blood Donor Seroprevalence Survey Combined Infection- and Vaccination-Induced Seroprevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9644,88 +9620,95 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/wi5c-cscz",
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
+            "landingPage": "https://data.cdc.gov/d/wi5c-cscz",
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
+            "title": "2020-2021 Nationwide Blood Donor Seroprevalence Survey Combined Infection- and Vaccination-Induced Seroprevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/454d-nzxn",
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
-                "screening",
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
-            "identifier": "37b55242-7cd4-4818-b783-348adf39e50c",
             "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of\u00a0health screenings provided to Medicaid and CHIP beneficiaries under the age of 19 (as of the first day of the month) by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating screening services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Diagnosis Codes - OT, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Health Screenings Provided to Medicaid and CHIP Beneficiaries Under Age 19",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Health-Screenings-Provided-to-MedicaidCHIP-Beneficiaries-Under-Age-19.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of\u00a0health screenings provided to Medicaid and CHIP beneficiaries under the age of 19 (as of the first day of the month) by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating screening services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Diagnosis Codes - OT, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of\u00a0health screenings provided to Medicaid and CHIP beneficiaries under the age of 19 (as of the first day of the month) by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating screening services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Diagnosis Codes - OT, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Health-Screenings-Provided-to-MedicaidCHIP-Beneficiaries-Under-Age-19.csv",
+                    "mediaType": "text/csv",
                     "title": "Health Screenings Provided to Medicaid and CHIP Beneficiaries Under Age 19"
                 }
             ],
+            "identifier": "37b55242-7cd4-4818-b783-348adf39e50c",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "screening",
+                "service use",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/454d-nzxn",
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
+            "title": "Health Screenings Provided to Medicaid and CHIP Beneficiaries Under Age 19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/m4es-3af4",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-07-29",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "hus",
-                "low birthweight"
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
-            "identifier": "https://data.cdc.gov/api/views/m4es-3af4",
             "description": "Health, United States is an annual report on trends in health statistics, find more information at http://www.cdc.gov/nchs/hus.htm.",
-            "title": "Selected Trend Table from Health, United States, 2011. Low birthweight live births, by race and Hispanic origin of mother, and state: United States, 2000 - 2002, 2003 - 2005, and 2006 - 2008",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9748,41 +9731,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/m4es-3af4",
+            "issued": "2013-07-29",
+            "keyword": [
+                "hus",
+                "low birthweight"
+            ],
+            "landingPage": "https://data.cdc.gov/d/m4es-3af4",
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
+            "title": "Selected Trend Table from Health, United States, 2011. Low birthweight live births, by race and Hispanic origin of mother, and state: United States, 2000 - 2002, 2003 - 2005, and 2006 - 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-15",
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
-            "identifier": "https://data.cdc.gov/api/views/jbhn-e8xn",
             "description": "The BEAM (Bacteria, Enterics, Amoeba, and Mycotics) Dashboard is an interactive tool to access and visualize data from the System for Enteric Disease Response, Investigation, and Coordination (SEDRIC). The BEAM Dashboard provides timely data on pathogen trends and serotype details to inform work to prevent illnesses from food and animal contact.",
-            "title": "BEAM Dashboard - Report Data",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9805,57 +9787,54 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/jbhn-e8xn",
+            "issued": "2023-11-15",
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
+            "title": "BEAM Dashboard - Report Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-change-of-ownership",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-04-21",
-            "temporal": "2022-01-01/2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
-            "references": [
-                "https://data.cms.gov/sites/default/files/2024-10/SNF_CHOW_Data_Guidance.pdf"
-            ],
-            "keyword": [
-                "hospitals & facilities",
-                "medicare",
-                "medicare prescription drug",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/f557a6ed-95b3-4a22-8433-4175db2dec1c/data-viewer",
-            "description": "The Skilled Nursing Facility (SNF) Change of Ownership (CHOW) dataset provides information on the SNF ownership changes that occurred on or after January 1, 2016. This data includes information on the buyer and seller organization\u2019s legal business name, provider type, change of ownership type (CHOW, Acquisition/Merger, or Consolidation) and the effective date of the change.",
-            "title": "Skilled Nursing Facility Change of Ownership",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-01/SNF_CHOW_Data_Dictionary_2022.12.30.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:000"
-            ],
+            "description": "The Skilled Nursing Facility (SNF) Change of Ownership (CHOW) dataset provides information on the SNF ownership changes that occurred on or after January 1, 2016. This data includes information on the buyer and seller organization\u2019s legal business name, provider type, change of ownership type (CHOW, Acquisition/Merger, or Consolidation) and the effective date of the change.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f557a6ed-95b3-4a22-8433-4175db2dec1c/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f557a6ed-95b3-4a22-8433-4175db2dec1c/data",
+                    "mediaType": "text/html",
                     "title": "Skilled Nursing Facility Change of Ownership : 2024-12-01"
                 },
                 {
@@ -10003,46 +9982,49 @@
                     "title": "Skilled Nursing Facility Change of Ownership : 2022-03-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/sites/default/files/2023-01/SNF_CHOW_Data_Dictionary_2022.12.30.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/f557a6ed-95b3-4a22-8433-4175db2dec1c/data-viewer",
+            "issued": "2022-04-21",
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare prescription drug",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-change-of-ownership",
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
+                "https://data.cms.gov/sites/default/files/2024-10/SNF_CHOW_Data_Guidance.pdf"
+            ],
+            "temporal": "2022-01-01/2024-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Skilled Nursing Facility Change of Ownership"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/medgen/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/csf9-pt6p",
             "description": "MedGen is NCBI's portal to information about conditions and phenotypes related to Medical Genetics. Terms from the NIH Genetic Testing Registry (GTR), UMLS,  HPO, Orphanet, ClinVar and other sources are aggregated into concepts, each of which is assigned a unique identifier and a preferred name and symbol. The core content of the record may include names, identifiers used by other databases, mode of inheritance, clinical features, and map location of the loci affecting the disorder. The concept identifier (CUI) is used to aggregate information about that concept, similar to the way NCBI Gene serves as a gateway to gene-related information.\n\nMedGen provides links to such resources as: Genetic tests registered in the NIH Genetic Testing Registry (GTR), GeneReviews, ClinVar, OMIM, Related genes, Disorders with similar clinical features, Medical and research literature, Practice guidelines, Consumer resources, Ontologies such as HPO and ORDO.\n\nLinks to the GTR, GeneReviews, and Practice Guidelines are based on curation by NCBI staff. Other data feeds are automated, but reviewed by NCBI staff and informed by feedback from the community.",
-            "title": "MedGen",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10057,50 +10039,40 @@
                     "title": "Query Interface"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/csf9-pt6p",
+            "issued": "2021-06-30",
+            "keyword": [
+                "dataset",
+                "genetics",
+                "genomics"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/medgen/",
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
+            "title": "MedGen"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/teenvaxview/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-12",
-            "keyword": [
-                "adolescent vaccination",
-                "hepb",
-                "hpv",
-                "immunization",
-                "menacwy",
-                "mmr",
-                "sociodemographic data",
-                "td",
-                "tdap",
-                "teen vaccination",
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
-            "identifier": "https://data.cdc.gov/api/views/ee48-w5t6",
             "description": "Vaccination Coverage among Adolescents (13-17 Years)\n\n\u2022 Data on adolescent vaccination coverage and selected sociodemographic characteristics by State, HHS Region, and the United States from the National Immunization Survey-Teen (NIS-Teen).\n\n\u2022 Additional information available at https://www.cdc.gov/vaccines/imz-managers/coverage/teenvaxview/index.html",
-            "title": "Vaccination Coverage among Adolescents (13-17 Years)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10123,39 +10095,51 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ee48-w5t6",
+            "issued": "2021-07-28",
+            "keyword": [
+                "adolescent vaccination",
+                "hepb",
+                "hpv",
+                "immunization",
+                "menacwy",
+                "mmr",
+                "sociodemographic data",
+                "td",
+                "tdap",
+                "teen vaccination",
+                "vaccination",
+                "vaccination coverage",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/teenvaxview/index.html",
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
                 "Teen Vaccinations"
-            ]
+            ],
+            "title": "Vaccination Coverage among Adolescents (13-17 Years)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/47ta-vew3",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2015-08-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
-            "keyword": [
-                "nadac",
-                "nadac comparison"
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
-            "identifier": "a217613c-12bc-5137-8b3a-ada0e4dad1ff",
             "description": "The NADAC Weekly Comparison identifies the drug products with current NADAC rates that are replaced with new NADAC rates.  Other changes (e.g. NDC additions and terminations) to the NADAC file are not reflected in this comparison.\r\n\r\nNote: Effective Date was not recorded in the dataset until 6/7/2017",
-            "title": "NADAC Comparison",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10164,90 +10148,86 @@
                     "title": "NADAC Comparison"
                 }
             ],
+            "identifier": "a217613c-12bc-5137-8b3a-ada0e4dad1ff",
+            "issued": "2015-08-19",
+            "keyword": [
+                "nadac",
+                "nadac comparison"
+            ],
+            "landingPage": "https://healthdata.gov/d/47ta-vew3",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P10Y",
+            "modified": "2025-01-28",
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
+            "title": "NADAC Comparison"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/48nu-pwdc",
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
-                "pregnancy",
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
-            "identifier": "8dd46b48-f004-4245-a51d-a8d864ea586f",
             "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of pregnancy outcomes, including (1) live births and (2) miscarriages, stillbirths, and terminations, for female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating pregnancy measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
-            "title": "Pregnancy Outcomes for Medicaid and CHIP Beneficiaries ages 15 to 44",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/Pregnancy-Outcomes-for-MedicaidCHIP-Beneficiaries-ages-15-to-44.csv",
-                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of pregnancy outcomes, including (1) live births and (2) miscarriages, stillbirths, and terminations, for female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating pregnancy measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
                     "@type": "dcat:Distribution",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of pregnancy outcomes, including (1) live births and (2) miscarriages, stillbirths, and terminations, for female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating pregnancy measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "downloadURL": "https://download.medicaid.gov/data/Pregnancy-Outcomes-for-MedicaidCHIP-Beneficiaries-ages-15-to-44.csv",
+                    "mediaType": "text/csv",
                     "title": "Pregnancy Outcomes for Medicaid and CHIP Beneficiaries ages 15 to 44"
                 }
             ],
+            "identifier": "8dd46b48-f004-4245-a51d-a8d864ea586f",
+            "issued": "2023-03-28",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "pregnancy",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/48nu-pwdc",
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
+            "title": "Pregnancy Outcomes for Medicaid and CHIP Beneficiaries ages 15 to 44"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://lantern.healthit.gov/",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-03",
-            "keyword": [
-                "api",
-                "application programming interface",
-                "endpoints",
-                "fast healthcare interoperability resources",
-                "fhir",
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
-            "identifier": "gm6eogxx-c5b8-70if-wrnc-pdl30x0c4dqh",
+            "describedBy": "https://lantern.healthit.gov/",
             "description": "Lantern is an open source tool for monitoring fielded health IT systems' certified FHIR API endpoints. It gathers availability information and information about FHIR support from endpoints' capability statements and provides visualizations to show FHIR adoption and patient data availability across the nation. Lantern helps to ensure that patients will have digital access to their data by providing visibility into levels of FHIR adoption as well as FHIR endpoint availability and usability.",
-            "title": "Lantern Project",
-            "programCode": [
-                "009:110"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10255,35 +10235,40 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "describedBy": "https://lantern.healthit.gov/"
+            "identifier": "gm6eogxx-c5b8-70if-wrnc-pdl30x0c4dqh",
+            "issued": "2023-10-03",
+            "keyword": [
+                "api",
+                "application programming interface",
+                "endpoints",
+                "fast healthcare interoperability resources",
+                "fhir",
+                "health it"
+            ],
+            "landingPage": "https://lantern.healthit.gov/",
+            "modified": "2023-10-03",
+            "programCode": [
+                "009:110"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "title": "Lantern Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/inspect.cfm",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
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
-            "identifier": "fe84d43d-cad9-4dce-93d8-919358244618",
             "description": "The CDRH Inspections Database provides information about medical device inspections that were the responsibility of CDRH from 2008 to the present.",
-            "title": "CDRH Inspections Database",
-            "programCode": [
-                "009:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10291,40 +10276,35 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "fe84d43d-cad9-4dce-93d8-919358244618",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cdrh"
+            ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/inspect.cfm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1W"
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "CDRH Inspections Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm129662.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-10-31",
-            "references": [
-                "http://www.accessdata.fda.gov/scripts/cder/ob/default.cfm"
-            ],
-            "keyword": [
-                "cder",
-                "orange book"
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
-            "identifier": "c7b84420-8e01-44eb-92de-c5e7f975ab28",
             "description": "The publication Approved Drug Products with Therapeutic Equivalence Evaluations (the List, commonly known as the Orange Book) identifies drug products approved on the basis of safety and effectiveness by the Food and Drug Administration (FDA) under the Federal Food, Drug, and Cosmetic Act (the Act). (For more information, see the Orange Book Preface.)",
-            "title": "Approved Drug Products with Therapuetic Equivalence Evaluations (Orange Book)",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10332,43 +10312,40 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "c7b84420-8e01-44eb-92de-c5e7f975ab28",
+            "issued": "2021-02-25",
+            "keyword": [
+                "cder",
+                "orange book"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm129662.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-10-31",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "references": [
+                "http://www.accessdata.fda.gov/scripts/cder/ob/default.cfm"
+            ],
+            "title": "Approved Drug Products with Therapuetic Equivalence Evaluations (Orange Book)"
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
@@ -10391,42 +10368,46 @@
                     "mediaType": "application/xml"
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
-            "landingPage": "https://datadiscovery.nlm.nih.gov/d/czsr-ugu4",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/czsr-ugu4",
             "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Delete Report lists Descriptors and Supplementary Concept Records (SCRs) that have been removed from MeSH.  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
-            "title": "MeSH 2025 Update - Delete Report",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10449,41 +10430,42 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/czsr-ugu4",
+            "issued": "2023-12-14",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/czsr-ugu4",
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
+            "title": "MeSH 2025 Update - Delete Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/4ay4-9ig4",
+            "accrualPeriodicity": "R/P10Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2022-12-23",
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
-            "identifier": "d8df4c15-38e0-43c8-ba3b-c56ffa61de5f",
             "description": "The Reference Document link for the downable Blood Disorder Treatment Spreadsheet can be accessed below under the Additional Information table under Related Documents.",
-            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 12/1/2022)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10491,39 +10473,41 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "d8df4c15-38e0-43c8-ba3b-c56ffa61de5f",
+            "issued": "2022-12-23",
+            "keyword": [
+                "drug products"
+            ],
+            "landingPage": "https://healthdata.gov/d/4ay4-9ig4",
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
+            "title": "Pricing Comparison for Blood Disorder Treatments (Pricing as of 12/1/2022)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/4bnw-gsxx",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-23",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
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
-            "identifier": "427fca5c-cb3f-41ba-84ae-d27bfc9cc312",
             "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
-            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 01-13-2025-to-01-19-2025",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10532,39 +10516,35 @@
                     "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 01-13-2025-to-01-19-2025"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "427fca5c-cb3f-41ba-84ae-d27bfc9cc312",
+            "issued": "2025-01-23",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "landingPage": "https://healthdata.gov/d/4bnw-gsxx",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2025-01-21",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 01-13-2025-to-01-19-2025"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/4bph-u9pm",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2025-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-18",
-            "keyword": [
-                "chip",
-                "demographics",
-                "medicaid",
-                "primary language",
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
-            "identifier": "3df86994-c0e4-4106-a404-e95e87c824e6",
             "description": "This data set includes annual counts and percentages of Medicaid and Children\u2019s Health Insurance Program (CHIP) enrollees by primary language spoken (English, Spanish, and all other languages). Results are shown overall; by state; and by five subpopulation topics: race and ethnicity, age group, scope of Medicaid and CHIP benefits, urban or rural residence, and eligibility category.\r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands who were enrolled for at least one day in the calendar year, except where otherwise noted. Enrollees in Guam, American Samoa, the Northern Mariana Islands, and select states with data quality issues with the primary language variable in TAF are not included. Results shown for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown overall (where subpopulation topic is \"Total enrollees\") exclude enrollees younger than age 5 and enrollees in the U.S. Virgin Islands. Results for states with TAF data quality issues in the year have a value of \"Unusable data.\" Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Primary language spoken by the Medicaid and CHIP population in 2020.\" Enrollees are assigned to a primary language category based on their reported ISO language code in TAF (English/missing, Spanish, and all other language codes) (Primary Language). Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to an age group subpopulation using age as of December 31st of the calendar year. Enrollees are assigned to the comprehensive benefits or limited benefits subpopulation according to the criteria in the \"Identifying Beneficiaries with Full-Scope, Comprehensive, and Limited Benefits in the TAF\" DQ Atlas brief. Enrollees are assigned to an urban or rural subpopulation based on the 2010 Rural-Urban Commuting Area (RUCA) code associated with their home or mailing address ZIP code in TAF (Rural Medicaid and CHIP enrollees in 2020). Enrollees are assigned to an eligibility category subpopulation using their latest reported eligibility group code, CHIP code, and age in the calendar year. Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
-            "title": "Primary language spoken by the Medicaid and CHIP population",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10572,53 +10552,48 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "3df86994-c0e4-4106-a404-e95e87c824e6",
+            "issued": "2025-01-18",
+            "keyword": [
+                "chip",
+                "demographics",
+                "medicaid",
+                "primary language",
+                "t-msis analytic files"
+            ],
+            "landingPage": "https://healthdata.gov/d/4bph-u9pm",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-18",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "title": "Primary language spoken by the Medicaid and CHIP population"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/medicare-monthly-enrollment",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2024-09-01/2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-27",
-            "references": [
-                "https://data.cms.gov/resources/medicare-monthly-enrollment-methodology"
-            ],
-            "keyword": [
-                "beneficiary enrollment",
-                "counties",
-                "health equity",
-                "medicare",
-                "medicare advantage",
-                "medicare prescription drug",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/d7fabe1e-d19b-4333-9eff-e80e0643f2fd/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-monthly-enrollment-data-dictionary",
             "description": "The Medicare Monthly Enrollment data\u00a0provides current monthly information on the number of Medicare beneficiaries with hospital/medical coverage and prescription drug coverage, available for several geographic areas including national, state/territory, and county. The hospital/medical coverage data can be broken down further by health care delivery (Original Medicare versus Medicare Advantage and Other Health Plans) and the prescription drug coverage data can be examined by those enrolled in stand-alone Prescription Drug Plans and those enrolled in Medicare Advantage Prescription Drug plans. The dataset provides monthly and yearly enrollee trends.",
-            "title": "Medicare Monthly Enrollment",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d7fabe1e-d19b-4333-9eff-e80e0643f2fd/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d7fabe1e-d19b-4333-9eff-e80e0643f2fd/data",
+                    "mediaType": "text/html",
                     "title": "Medicare Monthly Enrollment : 2024-09-01"
                 },
                 {
@@ -10634,45 +10609,53 @@
                     "title": "Medicare Monthly Enrollment : 2024-09-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-monthly-enrollment-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/d7fabe1e-d19b-4333-9eff-e80e0643f2fd/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "beneficiary enrollment",
+                "counties",
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "medicare prescription drug",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/medicare-monthly-enrollment",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2024-12-27",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/medicare-monthly-enrollment-methodology"
+            ],
+            "temporal": "2024-09-01/2024-09-30",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Medicare Monthly Enrollment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ncbi.nlm.nih.gov/pathogens/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2021-08-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4gse-hiry",
             "description": "NCBI Pathogen Detection integrates bacterial pathogen genomic sequences originating in food, environmental sources, and patients. It quickly clusters and identifies related sequences to uncover potential food contamination sources, helping public health scientists investigate foodborne disease outbreaks.",
-            "title": "Pathogen Detection (BETA)",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10681,10 +10664,10 @@
                     "title": "Isolates Browser"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pathogens/microbigge/",
-                    "description": "This interface contains a subset of the isolates from the Isolate Browser that have genomic sequence data available in GenBank and have genotypes identified by AMRFinderPlus at the time they were analyzed.",
                     "@type": "dcat:Distribution",
+                    "description": "This interface contains a subset of the isolates from the Isolate Browser that have genomic sequence data available in GenBank and have genotypes identified by AMRFinderPlus at the time they were analyzed.",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pathogens/microbigge/",
+                    "mediaType": "text/html",
                     "title": "Pathogen Detection Microbial Browser for Identification of Genetic and Genomic Elements (MicroBIGG-E)"
                 },
                 {
@@ -10694,17 +10677,17 @@
                     "title": "Reference Gene Catalog"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pathogens/hmm/",
-                    "description": "Reference set of hidden Markov models (HMMs) used by AMRFinderPlus to identify protein families in conjunction with Reference Gene Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "Reference set of hidden Markov models (HMMs) used by AMRFinderPlus to identify protein families in conjunction with Reference Gene Catalog",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pathogens/hmm/",
+                    "mediaType": "text/html",
                     "title": "Reference HMM Catalog"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncbi.nlm.nih.gov/biosample/?term=antibiogram%5bfilter%5d",
-                    "description": "antibiogram[filter] applied to BioSample",
                     "@type": "dcat:Distribution",
+                    "description": "antibiogram[filter] applied to BioSample",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/biosample/?term=antibiogram%5bfilter%5d",
+                    "mediaType": "text/html",
                     "title": "Isolates with antibiotic resistant phenotypes"
                 },
                 {
@@ -10714,40 +10697,40 @@
                     "title": "Download analysis results (FTP)"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/4gse-hiry",
+            "issued": "2021-08-27",
+            "keyword": [
+                "dataset",
+                "public health"
+            ],
+            "landingPage": "https://www.ncbi.nlm.nih.gov/pathogens/",
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
+            "title": "Pathogen Detection (BETA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/4d2m-mezn",
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
-            "identifier": "57c03da7-5c35-54d5-a1d5-09600eea07c2",
             "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
-            "title": "State Drug Utilization Data 2000",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10755,24 +10738,65 @@
                     "mediaType": "text/csv"
                 }
             ],
+            "identifier": "57c03da7-5c35-54d5-a1d5-09600eea07c2",
+            "issued": "2015-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "landingPage": "https://healthdata.gov/d/4d2m-mezn",
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
+            "title": "State Drug Utilization Data 2000"
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
+            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Behavioral-Risk-Factor-Data-Tobacco-Use-2011-to-pr/wsas-xwh5",
+            "description": "2011-2019. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. BRFSS Survey Data. The BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. The data for the STATE System were extracted from the annual BRFSS surveys from participating states. Tobacco topics included are cigarette and e-cigarette use prevalence by demographics, cigarette and e-cigarette use frequency, and quit attempts. NOTE: these data are not to be compared with BRFSS data collected 2010 and prior, as the methodologies were changed. Please refer to the FAQs / Methodology sections for more details.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wsas-xwh5",
+            "issued": "2025-01-31",
             "keyword": [
                 "adult",
                 "age",
@@ -10807,81 +10831,38 @@
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
-            "identifier": "https://data.cdc.gov/api/views/wsas-xwh5",
-            "description": "2011-2019. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. BRFSS Survey Data. The BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. The data for the STATE System were extracted from the annual BRFSS surveys from participating states. Tobacco topics included are cigarette and e-cigarette use prevalence by demographics, cigarette and e-cigarette use frequency, and quit attempts. NOTE: these data are not to be compared with BRFSS data collected 2010 and prior, as the methodologies were changed. Please refer to the FAQs / Methodology sections for more details.",
-            "title": "Behavioral Risk Factor Data: Tobacco Use (2011 to present)",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/wsas-xwh5/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
+            "references": [
+                "https://chronicdata.cdc.gov/d/5amh-5sx3"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Survey-Data/Behavioral-Risk-Factor-Data-Tobacco-Use-2011-to-pr/wsas-xwh5",
-            "license": "http://opendatacommons.org/licenses/by/1.0/",
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "Behavioral Risk Factor Data: Tobacco Use (2011 to present)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-survey-child-and-adolescent-well-being",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2013-06-18",
-            "temporal": "1999-01-01T00:00:00-05:00/2012-01-01T00:00:00-05:00",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "child abuse and neglect",
-                "child maltreatment",
-                "children's health",
-                "child welfare",
-                "child well-being"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HealthData.gov",
                 "hasEmail": "mailto:HealthData@hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Administration for Children and Families"
-            },
-            "identifier": "22ed32f4-b43d-4bdb-9aa6-cc7e3523595d",
+            "dataQuality": true,
+            "describedBy": "http://www.ndacan.cornell.edu/NDACAN/Datasets/Abstracts/DatasetAbstract_NSCAW-General.html",
             "description": "<p>Nationally representative, longitudinal data describing functioning of and services for children who are reported to child protective services</p>",
-            "title": "National Survey of Child and Adolescent Well-Being",
-            "programCode": [
-                "009:015"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10890,50 +10871,41 @@
                     "title": "NSCAW Dataset"
                 }
             ],
-            "describedBy": "http://www.ndacan.cornell.edu/NDACAN/Datasets/Abstracts/DatasetAbstract_NSCAW-General.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "identifier": "22ed32f4-b43d-4bdb-9aa6-cc7e3523595d",
+            "issued": "2013-06-18",
+            "keyword": [
+                "child abuse and neglect",
+                "child maltreatment",
+                "children's health",
+                "child welfare",
+                "child well-being"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-child-and-adolescent-well-being",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:015"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families"
+            },
+            "temporal": "1999-01-01T00:00:00-05:00/2012-01-01T00:00:00-05:00",
+            "title": "National Survey of Child and Adolescent Well-Being"
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
-            "identifier": "https://data.cdc.gov/api/views/yjkw-uj5s",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
             "description": "This dataset contains model-based census tract level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. These data can be joined with the Census tract 2022 boundary file in a GIS system to produce maps for 40 measures at the census tract level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
-            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2024 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10956,40 +10928,51 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
+            "identifier": "https://data.cdc.gov/api/views/yjkw-uj5s",
+            "issued": "2024-08-23",
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
+            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2024 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fj6s-ssz6",
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
-            "identifier": "https://data.cdc.gov/api/views/fj6s-ssz6",
             "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 2 - New York",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11012,58 +10995,40 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fj6s-ssz6",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fj6s-ssz6",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 2 - New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual (R/P1Y)",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-07-11",
-            "temporal": "1988/2020",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "cholesterol",
-                "chronic conditions",
-                "female",
-                "health us",
-                "high cholesterol",
-                "hispanic",
-                "hypercholesterolemia",
-                "male",
-                "mean serum total cholesterol",
-                "mexican",
-                "national health and nutrition examination survey",
-                "nhanes",
-                "non-hispanic asian",
-                "non-hispanic black",
-                "non-hispanic white",
-                "poverty level",
-                "sdoh-access-to-health-care",
-                "sdoh-poverty-income",
-                "sdoh-use-of-health-care",
-                "total cholesterol"
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
-            "identifier": "https://data.cdc.gov/api/views/k2e8-8t3h",
             "description": "Data on cholesterol in adults age 20 and older in the United States, by selected characteristics. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Cholesterol in adults age 20 and older, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11086,43 +11051,58 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/k2e8-8t3h",
+            "issued": "2024-07-11",
+            "keyword": [
+                "cholesterol",
+                "chronic conditions",
+                "female",
+                "health us",
+                "high cholesterol",
+                "hispanic",
+                "hypercholesterolemia",
+                "male",
+                "mean serum total cholesterol",
+                "mexican",
+                "national health and nutrition examination survey",
+                "nhanes",
+                "non-hispanic asian",
+                "non-hispanic black",
+                "non-hispanic white",
+                "poverty level",
+                "sdoh-access-to-health-care",
+                "sdoh-poverty-income",
+                "sdoh-use-of-health-care",
+                "total cholesterol"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual (R/P1Y)",
+            "modified": "2024-11-07",
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
+            "title": "DQS Cholesterol in adults age 20 and older, by selected characteristics: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2013-08-16",
-            "keyword": [
-                "adverse event",
-                "cder",
-                "drugs",
-                "faers",
-                "reporting system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDER OSE Tracking",
                 "hasEmail": "mailto:cderosetracking@fda.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Food and Drug Administration"
-            },
-            "identifier": "c696c4f7-6de9-45db-988a-7195c2ade1d0",
             "description": "The FDA Adverse Event Reporting System (FAERS) is a database that contains information on adverse event and medication error reports submitted to FDA. The database is designed to support the FDA's post-marketing safety surveillance program for drug and therapeutic biologic products.",
-            "title": "FDA Adverse Event Reporting System (FAERS): Latest Quartely Data Files",
-            "programCode": [
-                "009:002"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11130,65 +11110,96 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/"
+            "identifier": "c696c4f7-6de9-45db-988a-7195c2ade1d0",
+            "issued": "2021-02-25",
+            "keyword": [
+                "adverse event",
+                "cder",
+                "drugs",
+                "faers",
+                "reporting system"
+            ],
+            "landingPage": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2013-08-16",
+            "programCode": [
+                "009:002"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "FDA Adverse Event Reporting System (FAERS): Latest Quartely Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/4fwu-3ss7",
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
-            "identifier": "f2be0940-700b-5b90-94ce-b1751ed24c29",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "featAuto_measureSearchInfo",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measureSearchInfo.csv",
-                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measureSearchInfo.csv",
+                    "mediaType": "text/csv",
                     "title": "measureSearchInfo csv file"
                 }
             ],
+            "identifier": "f2be0940-700b-5b90-94ce-b1751ed24c29",
+            "issued": "2022-08-31",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/4fwu-3ss7",
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
+            "title": "featAuto_measureSearchInfo"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/u6k2-rtt3",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Danielle Sharpe",
+                "hasEmail": "mailto:svi_coordinator@cdc.gov"
+            },
+            "description": "Social vulnerability refers to the resilience of communities when confronted by external stresses on human health, stresses such as natural or human-caused disasters, or disease outbreaks. Reducing social vulnerability can decrease both human suffering and economic loss. ATSDR's Social Vulnerability Index uses U.S. census variables at tract level to help local officials identify communities that may need support in preparing for hazards, or recovering from disaster.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://svi.cdc.gov/SVIDataToolsDownload.html",
+                    "mediaType": "application/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/u6k2-rtt3",
             "issued": "2015-03-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-13",
             "keyword": [
                 "american community survey",
                 "at-risk",
@@ -11199,66 +11210,34 @@
                 "svi",
                 "vulnerability"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Danielle Sharpe",
-                "hasEmail": "mailto:svi_coordinator@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/u6k2-rtt3",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-02-13",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/u6k2-rtt3",
-            "description": "Social vulnerability refers to the resilience of communities when confronted by external stresses on human health, stresses such as natural or human-caused disasters, or disease outbreaks. Reducing social vulnerability can decrease both human suffering and economic loss. ATSDR's Social Vulnerability Index uses U.S. census variables at tract level to help local officials identify communities that may need support in preparing for hazards, or recovering from disaster.",
-            "title": "CDC Social Vulnerability Index (SVI)",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://svi.cdc.gov/SVIDataToolsDownload.html",
-                    "mediaType": "application/html"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
             "theme": [
                 "Health Statistics"
-            ]
+            ],
+            "title": "CDC Social Vulnerability Index (SVI)"
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
-            "identifier": "https://data.cdc.gov/api/views/k4cb-dxd7",
             "description": "\u2022 Weekly Cumulative RSV Vaccination Coverage and Intent Among Adults 75 Years and Older and 60\u250074 Years with High Risk Conditions Ever Vaccinated with RSV Vaccine by Demographic Characteristics and Jurisdiction \n\n\u2022 Weekly estimates of RSV vaccination coverage and intent among adults 75 years and older and 60\u250074 years with high risk conditions are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html). \n\n\u2022 In June 2023, the Advisory Committee on Immunization Practices (ACIP) voted to recommend that adults aged \u226560 years may receive a single dose of an RSV vaccine, using shared clinical decision-making. In June 2024, the ACIP voted to recommend a single dose of RSV vaccine for all adults 75 years and older and adults 60\u201374 years who are at increased risk for severe RSV disease. The data below captures ever receiving a dose of an RSV vaccine by adults 60 years and older.",
-            "title": "Weekly Cumulative RSV Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 75 and Older and 60-74 Years with High-Risk Conditions Ever Vaccinated, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11281,45 +11260,48 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
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
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative RSV Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 75 and Older and 60-74 Years with High-Risk Conditions Ever Vaccinated, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-11-17",
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
-            "identifier": "https://data.cdc.gov/api/views/25m4-6qqq",
             "description": "Interactive Summary Health Statistics for Adults provide annual estimates of selected health topics for adults aged 18 years and over based on final data from the National Health Interview Survey.",
-            "title": "NHIS Adult Summary Health Statistics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11342,20 +11324,52 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/25m4-6qqq",
+            "issued": "2021-11-17",
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
+            "title": "NHIS Adult Summary Health Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/state-cancer-profiles-web-site",
             "bureauCode": [
                 "009:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "openFDA",
+                "hasEmail": "mailto:open@fda.hhs.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://statecancerprofiles.cancer.gov/faq.html",
+            "description": "<p>The State Cancer Profiles (SCP) web site provides statistics to help guide and prioritize cancer control activities at the state and local levels.  SCP is a collaborative effort using local and national level cancer data from  the Centers for Disease Control and Prevention's National Program of Cancer Registries (NPCR)  and National Cancer Institute's Surveillance, Epidemiology and End Results Registries (SEER).  SCP address select types of cancer and select behavioral risk factors for which there are evidence-based control interventions. The site provides incidence, mortality and prevalence comparison tables as well as interactive graphs and maps and support data.  The graphs and maps provide visual support for deciding where to focus cancer control efforts.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://statecancerprofiles.cancer.gov",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "identifier": "9f8175a9-c8b3-4cd5-89c5-6c80e42db3e6",
             "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "all cancer sites",
                 "bladder",
@@ -11374,64 +11388,33 @@
                 "urban",
                 "white collar"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "openFDA",
-                "hasEmail": "mailto:open@fda.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/state-cancer-profiles-web-site",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:047"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Health & Human Services"
             },
-            "identifier": "9f8175a9-c8b3-4cd5-89c5-6c80e42db3e6",
-            "description": "<p>The State Cancer Profiles (SCP) web site provides statistics to help guide and prioritize cancer control activities at the state and local levels.  SCP is a collaborative effort using local and national level cancer data from  the Centers for Disease Control and Prevention's National Program of Cancer Registries (NPCR)  and National Cancer Institute's Surveillance, Epidemiology and End Results Registries (SEER).  SCP address select types of cancer and select behavioral risk factors for which there are evidence-based control interventions. The site provides incidence, mortality and prevalence comparison tables as well as interactive graphs and maps and support data.  The graphs and maps provide visual support for deciding where to focus cancer control efforts.</p>",
-            "title": "State Cancer Profiles Web site",
-            "programCode": [
-                "009:047"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://statecancerprofiles.cancer.gov",
-                    "mediaType": "text/html",
-                    "title": "Query Tool "
-                }
-            ],
-            "describedBy": "http://statecancerprofiles.cancer.gov/faq.html",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
             "theme": [
                 "State"
-            ]
+            ],
+            "title": "State Cancer Profiles Web site"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -11454,45 +11437,39 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/azgh-hvnt",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/azgh-hvnt",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days),  2012 & 2014, Region 4 - Atlanta"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mcdp-77g7",
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
-            "identifier": "https://data.cdc.gov/api/views/mcdp-77g7",
             "description": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11515,25 +11492,57 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mcdp-77g7",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "nonparalytic",
+                "poliovirus infection",
+                "psittacosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mcdp-77g7",
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
+            "title": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis"
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
@@ -11543,78 +11552,40 @@
                 "surveillance",
                 "survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=LimitedAccess",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2023-04-17",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
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
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
-            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "public",
-            "issued": "2015-12-02",
-            "@type": "dcat:Dataset",
-            "temporal": "1909/2018",
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
-                "birth rate",
-                "fertility rate",
-                "nchs",
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
-            "identifier": "https://data.cdc.gov/api/views/e6fc-ccez",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes crude birth rates and general fertility rates in the United States since 1909. \n\nThe number of states in the reporting area differ historically. In 1915 (when the birth registration area was established), 10 states and the District of Columbia reported births; by 1933, 48 states and the District of Columbia were reporting births, with the last two states, Alaska and Hawaii, added to the registration area in 1959 and 1960, when these regions gained statehood. Reporting area information is detailed in references 1 and 2 below. Trend lines for 1909\u20131958 are based on live births adjusted for under-registration; beginning with 1959, trend lines are based on registered live births.",
-            "title": "NCHS - Births and General Fertility Rates: United States",
-            "isPartOf": "NCHS - Births and General Fertility Rates: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11637,25 +11608,67 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/e6fc-ccez",
+            "isPartOf": "NCHS - Births and General Fertility Rates: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "birth rate",
+                "fertility rate",
+                "nchs",
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
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1909/2018",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Births and General Fertility Rates: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2007",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment<br />\nFacility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>. Data are collected on topics including facility operation, services offered (assessment and pre-treatment, pharmacotherapies, testing, transitional, ancillary), detoxification, primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, counseling and therapeutic approaches, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2007) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2007-nid13536",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2007-nid13536"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2007-nid13536",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -11668,40 +11681,53 @@
                 "treatment facilities",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2007",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2007-nid13536",
-            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), to analyze general treatment services trends, and to generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment<br />\nFacility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>. Data are collected on topics including facility operation, services offered (assessment and pre-treatment, pharmacotherapies, testing, transitional, ancillary), detoxification, primary focus (substance abuse, mental health, both, general health, and other), hotline operation, Opioid Treatment Programs and medication dispensed/prescribed, counseling and therapeutic approaches, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
-            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2007)",
-            "programCode": [
-                "009:030"
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2007)"
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
+            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2017.  In this Table, provisional cases of selected infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  \r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in these tables are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnote:\r\n\u2014: No reported cases. N: Not reportable. NA: Not available. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. \r\n\r\n* Case counts for reporting year 2017 are provisional and subject to change. Data for years 2012 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. \r\n\r\n\u2020 This table does not include cases from the U.S. territories. Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u00a7 Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years. Additional information is available at http://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf.\r\n\r\n\u00b6 Updated weekly reports from the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance). Data for West Nile virus are available in Table II. \r\n\r\n** Not reportable in all jurisdictions. Data from states where the condition is not reportable are excluded from this table, except for the arboviral diseases and influenza-associated pediatric mortality. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.\r\n\r\n\u2020\u2020 Data for Haemophilus influenzae (all ages, all serotypes) are available in Table II.\r\n\r\n\u00a7\u00a7 In 2016, the nationally notifiable condition \u2018Hepatitis B Perinatal Infection\u2019 was renamed to \u2018Perinatal Hepatitis B Virus Infection\u2019 and reflects updates in the 2016 CSTE position statement for Perinatal Hepatitis B Virus Infection.\r\n\r\n\u00b6\u00b6 Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n\r\n*** Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n\r\n\u2020\u2020\u2020 Data for meningococcal disease (all serogroups) are available in Table II.\r\n\r\n\u00a7\u00a7\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses.  With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2011 have been variant influenza viruses.  Total case counts are provided by the Influenza Division, National Center for Immunization and Respiratory Diseases (NCIRD).\r\n\r\n\u00b6\u00b6\u00b6 Updated weekly from reports to the Division of STD Prevention, National Center for HIV/AIDS, Viral Hepatitis, STD, and TB Prevention.\r\n\r\n**** Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". Beginning in 2015, NNDSS has been updated to receive data for each of",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2007-nid13536",
-                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2007) \n",
                     "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2007-nid13536"
-                }
-            ]
+                    "downloadURL": "https://data.cdc.gov/api/views/45b4-9j7u/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
                 },
                 {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/45b4-9j7u",
-            "bureauCode": [
-                "009:00"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/45b4-9j7u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/45b4-9j7u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/45b4-9j7u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/45b4-9j7u",
             "issued": "2019-02-12",
-            "@type": "dcat:Dataset",
-            "modified": "2019-02-12",
             "keyword": [
                 "2017",
                 "acute",
@@ -11789,75 +11815,34 @@
                 "yellow fever",
                 "zika virus disease"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC INFO",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/45b4-9j7u",
-            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2017.  In this Table, provisional cases of selected infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  \r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in these tables are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnote:\r\n\u2014: No reported cases. N: Not reportable. NA: Not available. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. \r\n\r\n* Case counts for reporting year 2017 are provisional and subject to change. Data for years 2012 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. \r\n\r\n\u2020 This table does not include cases from the U.S. territories. Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u00a7 Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years. Additional information is available at http://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf.\r\n\r\n\u00b6 Updated weekly reports from the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance). Data for West Nile virus are available in Table II. \r\n\r\n** Not reportable in all jurisdictions. Data from states where the condition is not reportable are excluded from this table, except for the arboviral diseases and influenza-associated pediatric mortality. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.\r\n\r\n\u2020\u2020 Data for Haemophilus influenzae (all ages, all serotypes) are available in Table II.\r\n\r\n\u00a7\u00a7 In 2016, the nationally notifiable condition \u2018Hepatitis B Perinatal Infection\u2019 was renamed to \u2018Perinatal Hepatitis B Virus Infection\u2019 and reflects updates in the 2016 CSTE position statement for Perinatal Hepatitis B Virus Infection.\r\n\r\n\u00b6\u00b6 Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n\r\n*** Please refer to the MMWR publication for weekly updates to the footnote for this condition. \r\n\r\n\u2020\u2020\u2020 Data for meningococcal disease (all serogroups) are available in Table II.\r\n\r\n\u00a7\u00a7\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses.  With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2011 have been variant influenza viruses.  Total case counts are provided by the Influenza Division, National Center for Immunization and Respiratory Diseases (NCIRD).\r\n\r\n\u00b6\u00b6\u00b6 Updated weekly from reports to the Division of STD Prevention, National Center for HIV/AIDS, Viral Hepatitis, STD, and TB Prevention.\r\n\r\n**** Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". Beginning in 2015, NNDSS has been updated to receive data for each of",
-            "title": "NNDSS - Table I. infrequently reported notifiable diseases",
+            "landingPage": "https://data.cdc.gov/d/45b4-9j7u",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2019-02-12",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/45b4-9j7u/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/45b4-9j7u/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/45b4-9j7u/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/45b4-9j7u/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table I. infrequently reported notifiable diseases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.fda.gov/ICECI/EnforcementActions/ucm346077.htm",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:10"
             ],
-            "issued": "2021-02-25",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
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
-            "identifier": "74aed734-91b4-41f2-8418-a0aae396f9ef",
             "description": "Disclosure of reporting citations provide the public with a rationale for the Agency\ufffds enforcement actions and will also help to inform public and industry decision-making, allowing them to make more informed marketplace choices and help to encourage compliance.",
-            "title": "Inspection Citations",
-            "programCode": [
-                "009:008"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11865,53 +11850,36 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "74aed734-91b4-41f2-8418-a0aae396f9ef",
+            "issued": "2021-02-25",
+            "keyword": [
+                "ora"
+            ],
+            "landingPage": "http://www.fda.gov/ICECI/EnforcementActions/ucm346077.htm",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/P1M"
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:008"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "title": "Inspection Citations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-03-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2015/2022",
-            "modified": "2022-12-27",
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
-            "identifier": "https://data.cdc.gov/api/views/k5dc-apj8",
             "description": "Deaths from all causes and deaths involving coronavirus disease 2019 (COVID-19) reported to NCHS by time-period, HHS region, race and Hispanic origin, and age group.\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City, Puerto Rico; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
-            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age, 2015 to date",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11934,47 +11902,56 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/k5dc-apj8",
+            "issued": "2022-03-23",
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
+            "modified": "2022-12-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2015/2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age, 2015 to date"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/q8j9-sue7",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/q8j9-sue7",
             "description": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\nFootnotes:\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11997,49 +11974,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/q8j9-sue7",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "arboviral diseases",
+                "nedss",
+                "netss",
+                "nndss",
+                "st. louis virus disease",
+                "west nile virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/q8j9-sue7",
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
+            "title": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/h4wb-nae4",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "age <5 years",
-                "all ages",
-                "all serotypes",
-                "gonorrhea",
-                "haemophilus influenzae",
-                "invasive disease",
-                "nedss",
-                "netss",
-                "nndss",
-                "serotype b",
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
-            "identifier": "https://data.cdc.gov/api/views/h4wb-nae4",
             "description": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease (age <5 years), Serotype b - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease (age <5 years), Serotype b",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12062,48 +12035,49 @@
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
-            "landingPage": "https://data.cdc.gov/d/cvcu-witw",
-            "bureauCode": [
-                "009:00"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/h4wb-nae4",
             "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
             "keyword": [
                 "2019",
-                "(age <5 years)",
+                "age <5 years",
+                "all ages",
+                "all serotypes",
+                "gonorrhea",
                 "haemophilus influenzae",
                 "invasive disease",
                 "nedss",
                 "netss",
                 "nndss",
-                "non-b serotype",
-                "nontypeable",
-                "unknown serotype",
+                "serotype b",
                 "wonder"
             ],
+            "landingPage": "https://data.cdc.gov/d/h4wb-nae4",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2020-01-02",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease (age <5 years), Serotype b"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -12126,46 +12100,48 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/tfcp-ufzp",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/tfcp-ufzp",
             "description": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u00a7 Prior to 2015, this condition was not nationally notifiable and data for this condition was not submitted to CDC's National Notifiable Diseases Surveillance System (NNDSS).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12188,41 +12164,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/tfcp-ufzp",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "hansen's disease",
+                "hantavirus infection",
+                "hantavirus pulmonary syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-hantavirus pulmonary syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/tfcp-ufzp",
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
+            "title": "NNDSS - TABLE 1O. Hansen's disease to Hantavirus pulmonary syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://oculus.nlm.nih.gov/cgi/f/findaid/findaid-idx",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2022-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "keyword": [
-                "dataset",
-                "history of medicine",
-                "images",
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
-            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xtxk-p3k7",
             "description": "HMD Finding Aids is the central access point for electronic finding aids provided by the Archives and Modern Manuscripts and Prints and Photographs collections.",
-            "title": "History of Medicine Finding Aids",
-            "programCode": [
-                "009:041"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12237,124 +12218,121 @@
                     "title": "Download History of Medicine Finding Aids XML Data"
                 }
             ],
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xtxk-p3k7",
+            "issued": "2022-02-08",
+            "keyword": [
+                "dataset",
+                "history of medicine",
+                "images",
+                "reference"
+            ],
+            "landingPage": "https://oculus.nlm.nih.gov/cgi/f/findaid/findaid-idx",
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
+            "title": "History of Medicine Finding Aids"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/national-health-interview-survey",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-02-03",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "centers-for-disease-control-and-prevention-department-of-health-human-services",
-                "population statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeannine Schiller",
                 "hasEmail": "mailto:jschiller@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
-            },
-            "identifier": "a8f0a8b3-d514-4b7f-9572-17df46727789",
+            "dataQuality": true,
+            "describedBy": "http://www.cdc.gov/nchs/nhis/nhis_2012_data_release.htm",
             "description": "<p>The National Health Interview Survey (NHIS) is the principal source of information on the health of the civilian noninstitutionalized population of the United States and is one of the major data collection programs of the National Center for Health Statistics (NCHS) which is part of the Centers for Disease Control and Prevention (CDC). The National Health Survey Act of 1956 provided for a continuing survey and special studies to secure accurate and current statistical information on the amount, distribution, and effects of illness and disability in the United States and the services rendered for or because of such conditions. The survey referred to in the Act, now called the National Health Interview Survey, was initiated in July 1957. Since 1960, the survey has been conducted by NCHS, which was formed when the National Health Survey and the National Vital Statistics Division were combined.<br />\nNHIS data are used widely throughout the Department of Health and Human Services (DHHS) to monitor trends in illness and disability and to track progress toward achieving national health objectives. The data are also used by the public health research community for epidemiologic and policy analysis of such timely issues as characterizing those with various health problems, determining barriers to accessing and using appropriate health care, and evaluating Federal health programs.<br />\nThe NHIS also has a central role in the ongoing integration of household surveys in DHHS. The designs of two major DHHS national household surveys have been or are linked to the NHIS. The National Survey of Family Growth used the NHIS sampling frame in its first five cycles and the Medical Expenditure Panel Survey currently uses half of the NHIS sampling frame. Other linkage includes linking NHIS data to death certificates in the National Death Index (NDI).<br />\nWhile the NHIS has been conducted continuously since 1957, the content of the survey has been updated about every 10-15 years. In 1996, a substantially revised NHIS questionnaire began field testing. This revised questionnaire, described in detail below, was implemented in 1997 and has improved the ability of the NHIS to provide important health information.</p>",
-            "title": "National Health Interview Survey",
+            "identifier": "a8f0a8b3-d514-4b7f-9572-17df46727789",
+            "issued": "2015-02-03",
+            "keyword": [
+                "centers-for-disease-control-and-prevention-department-of-health-human-services",
+                "population statistics"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-health-interview-survey",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2023-07-25",
             "programCode": [
                 "009:048"
             ],
-            "describedBy": "http://www.cdc.gov/nchs/nhis/nhis_2012_data_release.htm",
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "title": "National Health Interview Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/4mjx-6na2",
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
-            "identifier": "0ae93c4e-85f9-5ecb-a850-61cc5875f824",
             "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
-            "title": "devAuto_measure_compare_download",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare_download.csv",
-                    "description": "{\"dataset\": \"measure_compare_download\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
                     "@type": "dcat:Distribution",
+                    "description": "{\"dataset\": \"measure_compare_download\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare_download.csv",
+                    "mediaType": "text/csv",
                     "title": "measure_compare_download csv file"
                 }
             ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "accrualPeriodicity": "R/PT1S",
-            "theme": [
-                "Uncategorized"
-            ]
-        },
+            "identifier": "0ae93c4e-85f9-5ecb-a850-61cc5875f824",
+            "issued": "2021-10-08",
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/4mjx-6na2",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
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
+            "title": "devAuto_measure_compare_download"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mik5-by93",
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
-                "tularemia",
-                "vancomycin-intermediate staphylococcus aureus",
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
-            "identifier": "https://data.cdc.gov/api/views/mik5-by93",
             "description": "NNDSS - TABLE 1JJ. Tularemia to  Vancomycin-intermediate Staphylococcus aureus - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1JJ. Tularemia to  Vancomycin-intermediate Staphylococcus aureus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12377,45 +12355,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mik5-by93",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "tularemia",
+                "vancomycin-intermediate staphylococcus aureus",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mik5-by93",
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
+            "title": "NNDSS - TABLE 1JJ. Tularemia to  Vancomycin-intermediate Staphylococcus aureus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/rezz-ypcg",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/rezz-ypcg",
             "description": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12438,46 +12415,45 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/rezz-ypcg",
+            "issued": "2020-01-17",
+            "keyword": [
+                "2020",
+                "arboviral diseases",
+                "babesiosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "western equine encephalitis virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/rezz-ypcg",
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
+            "title": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -12500,40 +12476,47 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/4ph7-u4md",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-12-01",
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
-            "identifier": "45a28339-17a5-55e6-8e74-e9004fc703d8",
             "description": "Performance rates on frequently reported health care quality measures in the CMS Medicaid/CHIP Child and Adult Core Sets, for FFY 2015 reporting.\r\n\r\nSource: Mathematica analysis of MACPro and Form CMS-416 reports for the FFY 2015 reporting cycle. For more information, see the <a href=\"https://www.medicaid.gov/medicaid/quality-of-care/performance-measurement/child-core-set/index.html\">Children's Health Care Quality Measures</a> and <a href=\"https://www.medicaid.gov/medicaid/quality-of-care/performance-measurement/adult-core-set/index.html\">Adult Health Care Quality Measures</a> webpages.",
-            "title": "2015 Child and Adult Health Care Quality Measures",
-            "programCode": [
-                "009:076"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12542,83 +12525,76 @@
                     "title": "CSV"
                 }
             ],
+            "identifier": "45a28339-17a5-55e6-8e74-e9004fc703d8",
+            "issued": "2016-12-01",
+            "keyword": [
+                "core sets",
+                "performance rates",
+                "quality measures"
+            ],
+            "landingPage": "https://healthdata.gov/d/4ph7-u4md",
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
+            "title": "2015 Child and Adult Health Care Quality Measures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://phenome.jax.org/db/q?rtn=docs/home",
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
-            "identifier": "c1422c56-e3b7-4742-85aa-d696bdd11673",
+            "dataQuality": true,
             "description": "<p>The Mouse Phenome Database (MPD) has characterizations of hundreds of strains of laboratory mice to facilitate translational discoveries and to assist in selection of strains for experimental studies.</p>",
-            "title": "Mouse Phenome Database (MPD)",
+            "identifier": "c1422c56-e3b7-4742-85aa-d696bdd11673",
+            "issued": "2016-07-17",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "landingPage": "http://phenome.jax.org/db/q?rtn=docs/home",
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
+            "title": "Mouse Phenome Database (MPD)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-medicaid-dual-enrollment",
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
-                "medicaid",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/3ff3dcc3-7608-448d-9b35-4f184697e37c/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
             "description": "The CMS Program Statistics -\u00a0Medicare-Medicaid Enrollment tables provide data on characteristics of the Medicare-Medicaid enrollee population.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR ENROLL AB 40. \u00a0Medicare-Medicaid Enrollment (MME): \u00a0Total Medicare-Medicaid Enrollees by Type of Eligibility, Yearly Trend\n\tMDCR ENROLL AB 41. \u00a0Medicare-Medicaid Enrollment (MME): \u00a0Total Medicare-Medicaid Enrollees by Type of Eligibility and by Demographic Characteristics\n\tMDCR ENROLL AB 42. \u00a0Medicare-Medicaid Enrollment (MME): \u00a0Total Medicare-Medicaid Enrollees by Type of Eligibility and Area of Residence\n\tMDCR ENROLL AB 43. \u00a0Medicare-Medicaid Enrollment (MME): \u00a0Original Medicare Enrollees by Type of Eligibility, Yearly Trend\n\tMDCR ENROLL AB 44. \u00a0Medicare-Medicaid Enrollment (MME): \u00a0Original Medicare Enrollees by Type of Eligibility and\u00a0by Demographic Characteristics\n\tMDCR ENROLL AB 45. \u00a0Medicare-Medicaid Enrollment (MME): \u00a0Original Medicare Enrollees by Type of Eligibility and Area of Residence\n\tMDCR ENROLL AB 46. \u00a0Medicare-Medicaid Enrollment (MME): \u00a0Medicare Advantage and Other Health Plan Enrollees by Type of Eligibility, Yearly Trend\n\tMDCR ENROLL AB 47. \u00a0Medicare-Medicaid Enrollment (MME): \u00a0Medicare Advantage and Other Health Plan Enrollees by Type of Eligibility and by Demographic Characteristics\n\tMDCR ENROLL AB 48. \u00a0Medicare-Medicaid Enrollment (MME): \u00a0Medicare Advantage and Other Health Plan Enrollees by Type of Eligibility and Area of Residence",
-            "title": "CMS Program Statistics - Medicare-Medicaid Dual Enrollment",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12675,50 +12651,54 @@
                     "title": "CMS Program Statistics - Medicare-Medicaid Dual Enrollment : 2013-12-31"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/3ff3dcc3-7608-448d-9b35-4f184697e37c/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "beneficiary enrollment",
+                "health equity",
+                "medicaid",
+                "medicare",
+                "medicare advantage",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-medicaid-dual-enrollment",
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
                 "Medicare",
                 "Medicaid"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS Program Statistics - Medicare-Medicaid Dual Enrollment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-trends/index.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-07-09",
-            "@type": "dcat:Dataset",
-            "temporal": "1900/2017",
-            "modified": "2022-03-30",
-            "keyword": [
-                "death rates",
-                "life expectancy",
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
-            "identifier": "https://data.cdc.gov/api/views/w9j2-ggv5",
             "description": "This dataset of U.S. mortality trends since 1900 highlights the differences in age-adjusted death rates and life expectancy at birth by race and sex.\n\nAge-adjusted death rates (deaths per 100,000) after 1998 are calculated based on the 2000 U.S. standard population. Populations used for computing death rates for 2011\u20132017 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years between 2000 and 2010 are revised using updated intercensal population estimates and may differ from rates previously published. Data on age-adjusted death rates prior to 1999 are taken from historical data (see References below).\n\nLife expectancy data are available up to 2017. Due to changes in categories of race used in publications, data are not available for the black population consistently before 1968, and not at all before 1960. More information on historical data on age-adjusted death rates is available at https://www.cdc.gov/nchs/nvss/mortality/hist293.htm.\n\nSOURCES\n\nCDC/NCHS, National Vital Statistics System, historical data, 1900-1998 (see https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm); CDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\n\nREFERENCES\n\n1. National Center for Health Statistics, Data Warehouse. Comparability of cause-of-death between ICD revisions. 2008. Available from: http://www.cdc.gov/nchs/nvss/mortality/comparability_icd.htm.\n\n2. National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.\n\n3. Kochanek KD, Murphy SL, Xu JQ, Arias E. Deaths: Final data for 2017. National Vital Statistics Reports; vol 68 no 9. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_09-508.pdf.\n\n4. Arias E, Xu JQ. United States life tables, 2017. National Vital Statistics Reports; vol 68 no 7. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_07-508.pdf.\n\n5. National Center for Health Statistics. Historical Data, 1900-1998. 2009. Available from: https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm.",
-            "title": "NCHS - Death rates and life expectancy at birth",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12741,22 +12721,55 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/w9j2-ggv5",
+            "issued": "2015-07-09",
+            "keyword": [
+                "death rates",
+                "life expectancy",
+                "mortality",
+                "nchs",
+                "united states"
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
+            "temporal": "1900/2017",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - Death rates and life expectancy at birth"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1979",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>This series measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, tobacco, and nonmedical use of prescription drugs among members of United States households aged 12 and older. Questions include age at first use, as well as lifetime, annual, and past-month usage for the following drug classes: cannabis, cocaine, hallucinogens, heroin, inhalants, alcohol, tobacco, nonmedical use of prescription drugs including psychotherapeutics, and polysubstance use. Respondents were also asked about their knowledge of drugs, perceptions of the risks involved, population movement, and sequencing of drug use. Fifty-seven percent of respondents were asked specific questions about their perceptions of the consequences of marijuana and alcohol use. The other 43 percent were asked about heroin use among friends. Demographic data include gender, race, age, ethnicity, marital status, educational level, job status, income level, and household composition.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1979) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1979-nid13635",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1979-nid13635"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1979-nid13635",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "alcohol",
                 "alcohol abuse",
@@ -12784,40 +12797,47 @@
                 "tranquilizers",
                 "youths"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1979",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1979-nid13635",
-            "description": "<p>This series measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, tobacco, and nonmedical use of prescription drugs among members of United States households aged 12 and older. Questions include age at first use, as well as lifetime, annual, and past-month usage for the following drug classes: cannabis, cocaine, hallucinogens, heroin, inhalants, alcohol, tobacco, nonmedical use of prescription drugs including psychotherapeutics, and polysubstance use. Respondents were also asked about their knowledge of drugs, perceptions of the risks involved, population movement, and sequencing of drug use. Fifty-seven percent of respondents were asked specific questions about their perceptions of the consequences of marijuana and alcohol use. The other 43 percent were asked about heroin use among friends. Demographic data include gender, race, age, ethnicity, marital status, educational level, job status, income level, and household composition.This study has 1 Data Set.</p>",
-            "title": "National Household Survey on Drug Abuse (NHSDA-1979)",
-            "programCode": [
-                "009:030"
+            "title": "National Household Survey on Drug Abuse (NHSDA-1979)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Veto Violence",
+                "hasEmail": "mailto:VetoViolence@cdc.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>VetoViolence.cdc.gov has been developed by the Centers for Disease Control and Prevention (CDC) to provide grantees and partners with access to training and tools that focus on the primary prevention of violence. The portal includes free training, program planning resources, and an online application for the creation of success stories.</p>",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1979-nid13635",
-                    "description": "National Household Survey on Drug Abuse (NHSDA-1979) \n",
                     "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1979-nid13635"
-                }
-            ]
+                    "downloadURL": "http://vetoviolence.cdc.gov/",
+                    "mediaType": "text/html",
+                    "title": "Text "
                 },
                 {
-            "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/veto-violence-violence-education-tools-online",
-            "bureauCode": [
-                "009:20"
+                    "@type": "dcat:Distribution",
+                    "description": "Strengthen Your Prevention Toolkit\n\nDive deeper into topics about violence prevention programs and practice, such as how to address risks shared by different forms of violence or how to effectively build partnerships. Each tool and training will equip you with a unique set of skills that can bolster your work to stop violence before it starts.",
+                    "downloadURL": "https://vetoviolence.cdc.gov/apps/main/tools-and-trainings",
+                    "mediaType": "text/html",
+                    "title": " Tools and Tranings"
+                }
             ],
+            "identifier": "8066116e-e17a-42cb-af33-96bbd0e302c0",
             "issued": "2014-04-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
             "keyword": [
                 "child maltreatment",
                 "health care providers",
@@ -12833,51 +12853,57 @@
                 "violence prevention",
                 "youth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Veto Violence",
-                "hasEmail": "mailto:VetoViolence@cdc.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/veto-violence-violence-education-tools-online",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "modified": "2025-01-28",
+            "programCode": [
+                "009:099"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
             },
-            "identifier": "8066116e-e17a-42cb-af33-96bbd0e302c0",
-            "description": "<p>VetoViolence.cdc.gov has been developed by the Centers for Disease Control and Prevention (CDC) to provide grantees and partners with access to training and tools that focus on the primary prevention of violence. The portal includes free training, program planning resources, and an online application for the creation of success stories.</p>",
-            "title": "Veto Violence - Violence Education Tools Online",
-            "programCode": [
-                "009:099"
+            "theme": [
+                "Community"
+            ],
+            "title": "Veto Violence - Violence Education Tools Online"
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
+            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2014.In this Table, provisional cases of selected infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in these tables are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnote:-: No reported cases    N: Not reportable    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts. * Case counts for reporting year 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. \ufffd\ufffd\ufffd Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years. The total sum of incident cases is then divided by 25 weeks. Additional information is available at http://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf. \ufffd\ufffd Not reportable in all states. Data from states where the condition is not reportable are excluded from this table except starting in 2007 for the Arboviral diseases, STD data, TB data, and influenza-associated pediatric mortality, and in 2003 for SARS-CoV. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/document/SRCA_FINAL_REPORT_2006-2012_final.xlsx. \ufffd\ufffd Includes both neuroinvasive and nonneuroinvasive. Updated weekly from reports to the Division of Vector-Borne Infectious Diseases, National Center for Zoonotic, Vector-Borne, and Enteric Diseases (ArboNET Surveillance). Data for West Nile virus are available in Table II. ** Data for H. influenzae (all ages, all serotypes) are available in Table II. \ufffd\ufffd\u0289\ufffd\ufffd Updated weekly from reports to the Influenza Division, National Center for Immunization and Respiratory Diseases. Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\ufffd\ufffd Data for meningococcal disease (all serogroups) are available in Table II. *** Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\u0289\ufffd\u0289\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Updated weekly from reports to the Division of STD Prevention, National Center for HIV/AIDS, Viral Hepatitis, STD, and TB Prevention. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition. See Table II for Dengue Hemorrhagic Fever.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "http://vetoviolence.cdc.gov/",
-                    "mediaType": "text/html",
-                    "title": "Text "
+                    "downloadURL": "https://data.cdc.gov/api/views/wcwi-x3uk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://vetoviolence.cdc.gov/apps/main/tools-and-trainings",
-                    "description": "Strengthen Your Prevention Toolkit\n\nDive deeper into topics about violence prevention programs and practice, such as how to address risks shared by different forms of violence or how to effectively build partnerships. Each tool and training will equip you with a unique set of skills that can bolster your work to stop violence before it starts.",
                     "@type": "dcat:Distribution",
-                    "title": " Tools and Tranings"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "theme": [
-                "Community"
-            ]
+                    "downloadURL": "https://data.cdc.gov/api/views/wcwi-x3uk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wcwi-x3uk",
-            "bureauCode": [
-                "009:00"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wcwi-x3uk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wcwi-x3uk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wcwi-x3uk",
             "issued": "2015-01-12",
-            "@type": "dcat:Dataset",
-            "modified": "2016-03-29",
             "keyword": [
                 "2014",
                 "anthrax",
@@ -12933,82 +12959,33 @@
                 "wonder",
                 "yellow fever"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC INFO",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/wcwi-x3uk",
-            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2014.In this Table, provisional cases of selected infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in these tables are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnote:-: No reported cases    N: Not reportable    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts. * Case counts for reporting year 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. \ufffd\ufffd\ufffd Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years. The total sum of incident cases is then divided by 25 weeks. Additional information is available at http://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf. \ufffd\ufffd Not reportable in all states. Data from states where the condition is not reportable are excluded from this table except starting in 2007 for the Arboviral diseases, STD data, TB data, and influenza-associated pediatric mortality, and in 2003 for SARS-CoV. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/document/SRCA_FINAL_REPORT_2006-2012_final.xlsx. \ufffd\ufffd Includes both neuroinvasive and nonneuroinvasive. Updated weekly from reports to the Division of Vector-Borne Infectious Diseases, National Center for Zoonotic, Vector-Borne, and Enteric Diseases (ArboNET Surveillance). Data for West Nile virus are available in Table II. ** Data for H. influenzae (all ages, all serotypes) are available in Table II. \ufffd\ufffd\u0289\ufffd\ufffd Updated weekly from reports to the Influenza Division, National Center for Immunization and Respiratory Diseases. Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\ufffd\ufffd Data for meningococcal disease (all serogroups) are available in Table II. *** Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\u0289\ufffd\u0289\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Updated weekly from reports to the Division of STD Prevention, National Center for HIV/AIDS, Viral Hepatitis, STD, and TB Prevention. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition. See Table II for Dengue Hemorrhagic Fever.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
-            "title": "NNDSS - Table I. infrequently reported notifiable diseases",
+            "landingPage": "https://data.cdc.gov/d/wcwi-x3uk",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "modified": "2016-03-29",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/wcwi-x3uk/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/wcwi-x3uk/rows.rdf?accessType=DOWNLOAD",
-                    "mediaType": "application/rdf+xml"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/wcwi-x3uk/rows.json?accessType=DOWNLOAD",
-                    "mediaType": "application/json"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/wcwi-x3uk/rows.xml?accessType=DOWNLOAD",
-                    "mediaType": "application/xml"
-                }
-            ],
-            "license": "http://opendefinition.org/licenses/odc-odbl/",
             "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - Table I. infrequently reported notifiable diseases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/484g-ihkb",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
-            "keyword": [
-                "2019",
-                "legionellosis",
-                "leptospirosis",
-                "listeriosis",
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
-            "identifier": "https://data.cdc.gov/api/views/484g-ihkb",
             "description": "NNDSS - TABLE 1U. Legionellosis to Listeriosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1U. Legionellosis to Listeriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13031,21 +13008,48 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/484g-ihkb",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "legionellosis",
+                "leptospirosis",
+                "listeriosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/484g-ihkb",
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
+            "title": "NNDSS - TABLE 1U. Legionellosis to Listeriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.hcup-us.ahrq.gov/db/nation/nrd/nrddbdocumentation.jsp",
             "bureauCode": [
                 "009:33"
             ],
-            "rights": "Restricted Public",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HCUP Technical Support",
+                "hasEmail": "mailto:hcup@ahrq.gov"
+            },
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/nrd/nrddbdocumentation.jsp",
+            "description": "The Healthcare Cost and Utilization Project (HCUP) Nationwide Readmissions Database (NRD) is a unique and powerful database designed to support various types of analyses of national readmission rates for all payers and the uninsured. The NRD includes discharges for patients with and without repeat hospital visits in a year and those who have died in the hospital. Repeat stays may or may not be related. The criteria to determine the relationship between hospital admissions is left to the analyst using the NRD. This database addresses a large gap in health care data - the lack of nationally representative information on hospital readmissions for all ages.  Outcomes of interest include national readmission rates, reasons for returning to the hospital for care, and the hospital costs for discharges with and without readmissions. Unweighted, the NRD contains data from approximately 18 million discharges each year. Weighted, it estimates roughly 35 million discharges. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels. \n\nThe NRD is drawn from HCUP State Inpatient Databases (SID) containing verified patient linkage numbers that can be used to track a person across hospitals within a State, while adhering to strict privacy guidelines.  The NRD is not designed to support regional, State-, or hospital-specific readmission analyses.  \n\nThe NRD contains more than 100 clinical and non-clinical data elements provided in a hospital discharge abstract. Data elements include but are not limited to: diagnoses, procedures, patient demographics (e.g., sex, age), expected source of payer, regardless of expected payer, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge, discharge month, quarter, and year, total charges, length of stay, and data elements essential to readmission analyses.  The NIS excludes data elements that could directly or indirectly identify individuals. \n\nRestricted access data files are available with a data use agreement and brief online security training.",
+            "identifier": "b2fbf730-37f9-407b-bc31-452ff181cef5",
             "issued": "2021-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
             "keyword": [
                 "ambulatory surgery",
                 "emergency department",
@@ -13053,95 +13057,78 @@
                 "readmissions",
                 "revisits"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "HCUP Technical Support",
-                "hasEmail": "mailto:hcup@ahrq.gov"
-            },
+            "landingPage": "https://www.hcup-us.ahrq.gov/db/nation/nrd/nrddbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "modified": "2023-07-25",
+            "programCode": [
+                "009:072"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
             },
-            "identifier": "b2fbf730-37f9-407b-bc31-452ff181cef5",
-            "description": "The Healthcare Cost and Utilization Project (HCUP) Nationwide Readmissions Database (NRD) is a unique and powerful database designed to support various types of analyses of national readmission rates for all payers and the uninsured. The NRD includes discharges for patients with and without repeat hospital visits in a year and those who have died in the hospital. Repeat stays may or may not be related. The criteria to determine the relationship between hospital admissions is left to the analyst using the NRD. This database addresses a large gap in health care data - the lack of nationally representative information on hospital readmissions for all ages.  Outcomes of interest include national readmission rates, reasons for returning to the hospital for care, and the hospital costs for discharges with and without readmissions. Unweighted, the NRD contains data from approximately 18 million discharges each year. Weighted, it estimates roughly 35 million discharges. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels. \n\nThe NRD is drawn from HCUP State Inpatient Databases (SID) containing verified patient linkage numbers that can be used to track a person across hospitals within a State, while adhering to strict privacy guidelines.  The NRD is not designed to support regional, State-, or hospital-specific readmission analyses.  \n\nThe NRD contains more than 100 clinical and non-clinical data elements provided in a hospital discharge abstract. Data elements include but are not limited to: diagnoses, procedures, patient demographics (e.g., sex, age), expected source of payer, regardless of expected payer, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge, discharge month, quarter, and year, total charges, length of stay, and data elements essential to readmission analyses.  The NIS excludes data elements that could directly or indirectly identify individuals. \n\nRestricted access data files are available with a data use agreement and brief online security training.",
-            "title": "HCUP Nationwide Readmissions Database (NRD)- Restricted Access Files",
-            "programCode": [
-                "009:072"
-            ],
-            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/nrd/nrddbdocumentation.jsp",
-            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx"
+            "rights": "Restricted Public",
+            "title": "HCUP Nationwide Readmissions Database (NRD)- Restricted Access Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/d/4tnx-a42n",
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
-            "identifier": "58d9a2f4-82e2-5603-af3f-90338b11fbe7",
             "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
-            "title": "CoreSet measure_value v2.10.64 (coreset-etl-test)",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
-                    "description": "CoreSet measure_value v2.10.64 (coreset-etl-test)",
                     "@type": "dcat:Distribution",
+                    "description": "CoreSet measure_value v2.10.64 (coreset-etl-test)",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
+                    "mediaType": "text/csv",
                     "title": "CoreSet measure_value v2.10.64 (coreset-etl-test)"
                 }
             ],
+            "identifier": "58d9a2f4-82e2-5603-af3f-90338b11fbe7",
+            "issued": "2024-11-02",
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "landingPage": "https://healthdata.gov/d/4tnx-a42n",
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
+            "title": "CoreSet measure_value v2.10.64 (coreset-etl-test)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ukww-au2k",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-06-17",
-            "temporal": "March 27, 2022 - September 24, 2022",
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
-            "identifier": "https://data.cdc.gov/api/views/ukww-au2k",
             "description": "Data for CDC\u2019s COVID Data Tracker site on Rates of COVID-19 Cases and Deaths by Vaccination Status.\nClick 'More' for important dataset description and footnotes\n\nDataset and data visualization details:\nThese data were posted on October 21, 2022, archived on November 18, 2022, and revised on February 22, 2023. These data reflect cases among persons with a positive specimen collection date through September 24, 2022, and deaths among persons with a positive specimen collection date through September 3, 2022. \n\nVaccination status: A person vaccinated with a primary series had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after verifiably completing the primary series of an FDA-authorized or approved COVID-19 vaccine. An unvaccinated person had SARS-CoV-2 RNA or antigen detected on a respiratory specimen and has not been verified to have received COVID-19 vaccine. Excluded were partially vaccinated people who received at least one FDA-authorized vaccine dose but did not complete a primary series \u226514 days before collection of a specimen where SARS-CoV-2 RNA or antigen was detected.\nAdditional or booster dose: A person vaccinated with a primary series and an additional or booster dose had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after receipt of an additional or booster dose of any COVID-19 vaccine on or after August 13, 2021. For people ages 18 years and older, data are graphed starting the week including September 24, 2021, when a COVID-19 booster dose was first recommended by CDC for adults 65+ years old and people in certain populations and high risk occupational and institutional settings. For people ages 12-17 years, data are graphed starting the week of December 26, 2021, 2 weeks after the first recommendation for a booster dose for adolescents ages 16-17 years. For people ages 5-11 years, data are included starting the week of June 5, 2022, 2 weeks after the first recommendation for a booster dose for children aged 5-11 years. For people ages 50 years and older, data on second booster doses are graphed starting the week including March 29, 2022, when the recommendation was made for second boosters. Vertical lines represent dates when changes occurred in U.S. policy for COVID-19 vaccination (details provided above). Reporting is by primary series vaccine type rather than additional or booster dose vaccine type. The booster dose vaccine type may be different than the primary series vaccine type.\n** Because data on the immune status of cases and associated deaths are unavailable, an additional dose in an immunocompromised person cannot be distinguished from a booster dose. This is a relevant consideration because vaccines can be less effective in this group.\nDeaths: A COVID-19\u2013associated death occurred in a person with a documented COVID-19 diagnosis who died; health department staff reviewed to make a determination using vital records, public health investigation, or other data sources. Rates of COVID-19 deaths by vaccination status are reported based on when the patient was tested for COVID-19, not the date they died. Deaths usually occur up to 30 days after COVID-19 diagnosis.\nParticipating jurisdictions: Currently, these 31 health departments that regularly link their case surveillance to immunization information system data are included in these incidence rate estimates: Alabama, Arizona, Arkansas, California, Colorado, Connecticut, District of Columbia, Florida, Georgia, Idaho, Indiana, Kansas, Kentucky, Louisiana, Massachusetts, Michigan, Minnesota, Nebraska, New Jersey, New Mexico, New York, New York City (New York), North Carolina, Philadelphia (Pennsylvania), Rhode Island, South Dakota, Tennessee, Texas, Utah, Washington, and West Virginia; 30 jurisdictions also report deaths among vaccinated and unvaccinated people. These jurisdictions represent 72% of the total U.S. population and all ten of the Health and Human Services Regions. Data on cases",
-            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Vaccination Status and Second Booster Dose",
-            "programCode": [
-                "009:038"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13164,55 +13151,41 @@
                     "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Select US Jurisdictions",
+            "identifier": "https://data.cdc.gov/api/views/ukww-au2k",
+            "issued": "2022-06-17",
+            "landingPage": "https://data.cdc.gov/d/ukww-au2k",
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
+            "temporal": "March 27, 2022 - September 24, 2022",
             "theme": [
                 "Public Health Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Vaccination Status and Second Booster Dose"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -13235,53 +13208,60 @@
                     "mediaType": "application/xml"
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
+                "name": "Centers for Disease Control and Prevention"
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
-            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/alternative-payments-comprehensive-primary-care-initiative-participating-primary-care-practices/cpc-initiative-participating-primary-care-practices",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2021-12-22",
-            "temporal": "2017-01-01/2017-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-11",
-            "references": [
-                "https://data.cms.gov/resources/cpc-initiative-participating-primary-care-practices-methodology"
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/24da2642-7269-4c75-9a62-0dc3a195b205/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/cpc-initiative-participating-primary-care-practices-data-dictionary",
             "description": "The CPC Initiative - Participating Primary Care Practices dataset provides a list of practices involved in a multi-payer initiative which fosters collaboration between public and private health care payers to strengthen primary care.\u00a0",
-            "title": "CPC Initiative - Participating Primary Care Practices",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/24da2642-7269-4c75-9a62-0dc3a195b205/data",
-                    "description": "latest",
                     "@type": "dcat:Distribution",
+                    "description": "latest",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/24da2642-7269-4c75-9a62-0dc3a195b205/data",
+                    "mediaType": "text/html",
                     "title": "CPC Initiative - Participating Primary Care Practices : 2017-09-25"
                 },
                 {
@@ -13297,41 +13277,48 @@
                     "title": "CPC Initiative - Participating Primary Care Practices : 2017-09-25"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/cpc-initiative-participating-primary-care-practices-data-dictionary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/24da2642-7269-4c75-9a62-0dc3a195b205/data-viewer",
+            "issued": "2021-12-22",
+            "keyword": [
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/alternative-payments-comprehensive-primary-care-initiative-participating-primary-care-practices/cpc-initiative-participating-primary-care-practices",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-12-11",
+            "programCode": [
+                "009:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "references": [
+                "https://data.cms.gov/resources/cpc-initiative-participating-primary-care-practices-methodology"
+            ],
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "Medicare"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CPC Initiative - Participating Primary Care Practices"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/37ui-3igt",
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
-            "identifier": "https://data.cdc.gov/api/views/37ui-3igt",
             "description": "Heptafluorobutyric acid (PFBA) is a synthetic chemical belonging to the per- and polyfluoroalkyl substances (PFAS) group that includes over 5,000 chemicals.  PFBA is a short-chain PFAS (C4) that has been labeled as a safer alternative to the legacy PFAS perfluorooctanoic acid (PFOA) and perfluorooctane sulfate (PFOS) which have been linked to numerous health effects.  This class of chemicals are incorporated into consumer products such as stain resistant carpeting and textiles, nanosprays, medical devices, and fire-fighting foams.  There is a high potential for occupational exposure and in the environment, PFBA has been detected in a variety of water sources leading to concerns for dermal exposure, however, these studies are lacking.  In previous studies from our lab, PFOA was demonstrated to be absorbed via the skin and immunomodulatory.  In the present study, the systemic toxicity of a 28-day dermal PFBA (3.75-15% w/v, or 93.8-375 mg/kg/dose) exposure was evaluated in a murine model.",
-            "title": "Systemic toxicity induced by topical application of heptafluorobutyric acid (PFBA) in a murine model",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13339,50 +13326,36 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/37ui-3igt",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/37ui-3igt",
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
+            "title": "Systemic toxicity induced by topical application of heptafluorobutyric acid (PFBA) in a murine model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://healthdata.gov/dataset/office-head-start-ohs-head-start-center-locations-search-tool",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2012-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
-            "keyword": [
-                "administrative",
-                "center",
-                "children",
-                "children's health",
-                "early head start",
-                "geocode",
-                "grantee",
-                "head start",
-                "location",
-                "locator",
-                "low income",
-                "program",
-                "services"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Fran Majestic",
                 "hasEmail": "mailto:fmajestic@acf.hhs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Administration for Children and Families, Department of Health & Human Services"
-            },
-            "identifier": "8fce8c8e-dd59-4ab4-9aae-f720d356932d",
+            "dataQuality": true,
             "description": "<p>Office of Head Start (OHS) web based search tool for finding Head Start program office contact information.   Searchable by location, grant number or center type.  Results are downloadable in CSV format.</p>",
-            "title": "Office of Head Start (OHS) Head Start Center Locations Search Tool",
-            "programCode": [
-                "009:092"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13397,45 +13370,47 @@
                     "title": "XLS "
                 }
             ],
+            "identifier": "8fce8c8e-dd59-4ab4-9aae-f720d356932d",
+            "issued": "2012-05-30",
+            "keyword": [
+                "administrative",
+                "center",
+                "children",
+                "children's health",
+                "early head start",
+                "geocode",
+                "grantee",
+                "head start",
+                "location",
+                "locator",
+                "low income",
+                "program",
+                "services"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/office-head-start-ohs-head-start-center-locations-search-tool",
             "license": "https://opendatacommons.org/licenses/odbl/1.0/",
-            "dataQuality": true
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:092"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "title": "Office of Head Start (OHS) Head Start Center Locations Search Tool"
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
-                "name": "Centers for Disease Control and Prevention"
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
@@ -13458,79 +13433,80 @@
                     "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://fitbir.nih.gov/",
             "bureauCode": [
                 "009:25"
             ],
-            "issued": "2016-07-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-25",
-            "keyword": [
-                "tbi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bellogwan, Pat",
                 "hasEmail": "mailto:patrick.frostbellgowan@nih.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Institutes of Health (NIH)"
-            },
-            "identifier": "d804bbb4-dc4c-4d61-bbfe-92a806ab2516",
+            "dataQuality": true,
             "description": "<p>The Federal Interagency Traumatic Brain Injury Research (FITBIR) informatics system is an extensible, scalable informatics platform for TBI relevant imaging, assessment, genomics, and other data types. It was developed to share data across the entire TBI research field and to facilitate collaboration between laboratories, as well as interconnectivity with other informatics platforms.</p>",
-            "title": "Federal Interagency Traumatic Brain Injury Research (FITBIR) Informatics System",
+            "identifier": "d804bbb4-dc4c-4d61-bbfe-92a806ab2516",
+            "issued": "2016-07-17",
+            "keyword": [
+                "tbi"
+            ],
+            "landingPage": "https://fitbir.nih.gov/",
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
+            "title": "Federal Interagency Traumatic Brain Injury Research (FITBIR) Informatics System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gui6-i83p",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-02",
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
-            "identifier": "https://data.cdc.gov/api/views/gui6-i83p",
             "description": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable  - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
-            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13553,44 +13529,46 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gui6-i83p",
+            "issued": "2019-04-24",
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
+            "landingPage": "https://data.cdc.gov/d/gui6-i83p",
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
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/wycc-ffia",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/wycc-ffia",
             "description": "NNDSS - Table 1H. Cholera to Coccidioidomycosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1H. Cholera to Coccidioidomycosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13613,42 +13591,44 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/wycc-ffia",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "cholera",
+                "coccidioidomycosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/wycc-ffia",
             "license": "http://opendefinition.org/licenses/odc-odbl/",
-            "theme": [
+            "modified": "2019-05-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "theme": [
                 "NNDSS"
-            ]
+            ],
+            "title": "NNDSS - TABLE 1H. Cholera to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/37nu-tuw8",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-08-29",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-06",
-            "keyword": [
-                "environmental health",
-                "food safety",
-                "food safety culture",
-                "food workers",
-                "health knowledge"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Adam Kramer",
                 "hasEmail": "mailto:nears@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Centers for Disease Control and Prevention"
-            },
-            "identifier": "https://data.cdc.gov/api/views/37nu-tuw8",
             "description": "A poor food safety culture has been described as an emerging risk factor for foodborne illness outbreaks, yet there has been little research on this topic in the retail food industry. The purpose of this study was to identify and validate conceptual domains around food safety culture and develop an assessment tool that can be used to assess food workers\u2019 perceptions of their restaurant\u2019s food safety culture. The study, conducted from March 2018 through March 2019, surveyed restaurant food workers for their level of agreement with 28 statements. We received 579 responses from 331 restaurants spread across eight different health department jurisdictions. Factor analysis and structural equation modeling supported a model composed of four primary constructs. The highest rated construct was Resource Availability (\n=4.69, sd=0.57), which assessed the availability of resources to maintain good hand hygiene. The second highest rated construct was Employee Commitment (=4.49, sd=0.62), which assessed workers\u2019 perceptions of their coworkers\u2019 commitment to food safety. The last two constructs were related to management. Leadership (=4.28, sd=0.69) assessed the existence of food safety policies, training, and information sharing. Management Commitment (=3.94, sd=1.05) assessed whether food safety was a priority in practice. Finally, the model revealed one higher-order construct, Worker Beliefs about Food Safety Culture (=4.35, sd=0.53). The findings from this study can support efforts by the restaurant industry, food safety researchers, and health departments to examine the influence and effects of food safety culture within restaurants.",
-            "title": "Development of an Empirically Derived Measure of Food Safety Culture in Restaurants",
-            "programCode": [
-                "009:040"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13671,22 +13651,55 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/37nu-tuw8",
+            "issued": "2023-08-29",
+            "keyword": [
+                "environmental health",
+                "food safety",
+                "food safety culture",
+                "food workers",
+                "health knowledge"
+            ],
+            "landingPage": "https://data.cdc.gov/d/37nu-tuw8",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-11-06",
+            "programCode": [
+                "009:040"
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
+            "title": "Development of an Empirically Derived Measure of Food Safety Culture in Restaurants"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:30"
             ],
-            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2013",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2013) \n",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2013-nid16874",
+                    "mediaType": "text/html",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2013-nid16874"
+                }
+            ],
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2013-nid16874",
             "issued": "2016-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-26",
             "keyword": [
                 "alcohol abuse",
                 "drug abuse",
@@ -13699,69 +13712,32 @@
                 "substance abuse treatment",
                 "treatment programs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
-                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
-            },
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2013",
+            "modified": "2023-07-26",
+            "programCode": [
+                "009:030"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Substance Abuse & Mental Health Services Administration"
             },
-            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2013-nid16874",
-            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
-            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2013)",
-            "programCode": [
-                "009:030"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2013-nid16874",
-                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2013) \n",
-                    "@type": "dcat:Distribution",
-                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2013-nid16874"
-                }
-            ]
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2013)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-advantage-inpatient-hospital",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:38"
             ],
-            "issued": "2022-11-01",
-            "temporal": "2016-01-01/2021-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
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
-            "identifier": "https://data.cms.gov/data-api/v1/dataset/f7bc5d11-abce-4600-a680-a429f71e0653/data-viewer",
+            "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics - Medicare Advantage, Inpatient Hospital tables provide utilization data for inpatient hospitals, including short-stay hospitals, critical access hospitals, long term care hospitals, inpatient psychiatric facilities, inpatient rehabilitation facilities, and other hospitals, by Medicare Advantage beneficiaries.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\n\n\tMDCR INPT HOSP MA 4. \u00a0All Medicare Inpatient Hospital Types:\u00a0Utilization for Medicare Advantage Beneficiaries, by Type of Hospital\n\tMDCR INPT HOSP MA 5. \u00a0Medicare Short Stay Hospitals:\u00a0Utilization for Medicare Advantage Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR INPT HOSP MA 6. \u00a0Medicare Short Stay Hospitals: Utilization for Medicare Advantage Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR INPT HOSP MA 7. \u00a0Medicare Short Stay Hospitals: Utilization for Medicare Advantage Beneficiaries, by Area of Residence\n\n\n\u00a0\n\nMDCR INPT HOSP MA 1 \u2013 MDCR INPT HOSP MA 3 are not available at this time.",
-            "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital",
-            "programCode": [
-                "009:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13800,41 +13776,52 @@
                     "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2016-12-01"
                 }
             ],
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
-            "dataQuality": true,
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/f7bc5d11-abce-4600-a680-a429f71e0653/data-viewer",
+            "issued": "2022-11-01",
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
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-advantage-inpatient-hospital",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-24",
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
+            "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/2se8-zi9r",
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
-            "identifier": "https://data.cdc.gov/api/views/2se8-zi9r",
```

