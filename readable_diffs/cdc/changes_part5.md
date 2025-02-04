# Change History for cdc.json (Part 5)

### Changes from 9cd27cf to 452e48f (Part 5/8)
**Author:** Automated

**Date:** 2025-02-03 20:01:08+00:00

**Message:** Updated data: Mon Feb  3 20:01:08 UTC 2025

```diff
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
@@ -42550,64 +42394,57 @@
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
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ifsm-x42a",
-            "issued": "2022-10-04",
             "@type": "dcat:Dataset",
-            "modified": "2022-10-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD-CORVD",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
+            "description": "Beginning on October 20, 2022, CDC will be reporting and publishing aggregate case and death data from jurisdictional and state partners on a weekly basis rather than daily. As a result, several datasets reported on data.cdc.gov will be updated weekly on Thursdays, typically by 8 PM ET, instead of daily.",
             "identifier": "https://data.cdc.gov/api/views/ifsm-x42a",
+            "issued": "2022-10-04",
+            "landingPage": "https://data.cdc.gov/d/ifsm-x42a",
+            "modified": "2022-10-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "description": "Beginning on October 20, 2022, CDC will be reporting and publishing aggregate case and death data from jurisdictional and state partners on a weekly basis rather than daily. As a result, several datasets reported on data.cdc.gov will be updated weekly on Thursdays, typically by 8 PM ET, instead of daily.",
             "title": "Upcoming Reporting Cadence Change"
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
-                "name": "data.cdc.gov"
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
@@ -42615,60 +42452,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ig4m-ub43/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ig4m-ub43/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ig4m-ub43/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ig4m-ub43/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Varicella to West Nile virus disease"
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
-                "name": "data.cdc.gov"
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
@@ -42676,45 +42519,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/igaz-icki/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/igaz-icki/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/igaz-icki/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/igaz-icki/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/igaz-icki/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/igaz-icki/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/igaz-icki/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/igaz-icki/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/igaz-icki/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2020-04-10",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Global Health"
-            ]
+            ],
+            "title": "National Artesunate for Severe Malaria Program Case Report Data- April to December 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nsfg/index.htm",
+            "accrualPeriodicity": "Irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
-            "issued": "2020-10-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2017/2019",
-            "modified": "2023-12-12",
-            "references": [
-                "https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-MainText-508.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:nsfg@cdc.gov"
+            },
+            "describedBy": "Nationally representative sample of women and men in the household population ages 15-49",
+            "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
+                    "downloadURL": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
+                    "mediaType": "text/html",
+                    "title": "National Survey of Family Growth 2017-2019 Public-Use Files"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ihtq-qs57",
+            "isPartOf": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
+            "issued": "2020-10-20",
             "keyword": [
                 "births",
                 "cohabitation",
@@ -42737,81 +42609,39 @@
                 "sdoh-use-of-health-care",
                 "survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:nsfg@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nsfg/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-12-12",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/ihtq-qs57",
-            "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
-            "title": "National Survey of Family Growth 2017-2019 Public-Use Files",
-            "isPartOf": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
-                    "description": "The National Survey of Family Growth (NSFG) gathers information on pregnancies and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.\u00a0Public-use files include a female respondent, male respondent, and female pregnancy file.",
-                    "@type": "dcat:Distribution",
-                    "title": "National Survey of Family Growth 2017-2019 Public-Use Files"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/data/nsfg/NSFG-2017-2019-UG-MainText-508.pdf"
             ],
+            "rights": "https://www.cdc.gov/nchs/nsfg/nsfg_2017_2019_puf.htm",
             "spatial": "US",
-            "describedBy": "Nationally representative sample of women and men in the household population ages 15-49",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Irregular",
+            "temporal": "2017/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Survey of Family Growth 2017-2019 Public-Use Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/schoolvaxview/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "keyword": [
-                "any exemption",
-                "dt",
-                "dtap",
-                "dtp",
-                "hepatitis b",
-                "immunization",
-                "medical exemption",
-                "mmr",
-                "non-medical exemption",
-                "polio",
-                "school exemption",
-                "school vaccination",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ijqb-a7ye",
             "description": "Vaccination Coverage and Exemptions among Kindergartners\n\n\u2022 Data on school vaccination coverage and exemptions from the School Vaccination Assessment Program for kindergartners at the national and state levels.\n\n\u2022 Additional information available at https://www.cdc.gov/vaccines/imz-managers/coverage/schoolvaxview/index.html",
-            "title": "Vaccination Coverage and Exemptions among Kindergartners",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42819,48 +42649,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ijqb-a7ye/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ijqb-a7ye/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ijqb-a7ye/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ijqb-a7ye/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ijqb-a7ye/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ijqb-a7ye/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ijqb-a7ye/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ijqb-a7ye/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ijqb-a7ye/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ijqb-a7ye",
+            "issued": "2021-05-13",
+            "keyword": [
+                "any exemption",
+                "dt",
+                "dtap",
+                "dtp",
+                "hepatitis b",
+                "immunization",
+                "medical exemption",
+                "mmr",
+                "non-medical exemption",
+                "polio",
+                "school exemption",
+                "school vaccination",
+                "vaccination",
+                "vaccination coverage",
+                "varicella",
+                "vaxviews"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/schoolvaxview/index.html",
+            "modified": "2024-10-17",
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
+            "title": "Vaccination Coverage and Exemptions among Kindergartners"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nhcs/index.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
-            "issued": "2018-06-14",
-            "@type": "dcat:Dataset",
-            "temporal": "2013-2016, 2019-2021",
-            "modified": "2024-03-05",
-            "references": [
-                "https://www.cdc.gov/rdc/data/b1/2013_NHCS.pdf",
-                "https://www.cdc.gov/rdc/data/b1/2015_NHCS_RDC_Data_Dictionary.pdf",
-                "https://www.cdc.gov/rdc/data/b1/2016_NHCS_DATA-DICTIONARY.pdf",
-                "https://www.cdc.gov/rdc/data/b1/NHCS-RDC-Data-Dictionary.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "NHCS collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings include inpatient, emergency (EDs), and outpatient departments (OPDs). The survey will provide hospital utilization statistics for the Nation.",
+            "description": "The National Hospital Care Survey (NHCS) is designed to provide accurate and reliable health care statistics that answer key questions of interest to health care and public health professionals, researchers, and health care policy makers. This includes tracking the latest trends affecting hospitals and health care organizations and factors that influence the use of health care resources, the quality of health care, and disparities in health care services provided to population subgroups in the United States.\nNHCS collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings include inpatient, emergency (EDs), and outpatient departments (OPDs). The survey will provide hospital utilization statistics for the Nation. In addition, NHCS will also be able to monitor national trends in substance use-related ED visits including opioid visits.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Standard application process link attached.",
+                    "downloadURL": "https://www.cdc.gov/rdc/b3prosal/pp300.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ijr5-qdv2",
+            "isPartOf": "https://www.cdc.gov/nchs/nhds/nhds_questionnaires.htm",
+            "issued": "2018-06-14",
             "keyword": [
                 "emergency departments",
                 "healthcare",
@@ -42873,76 +42741,42 @@
                 "outpatient departments",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhcs/index.htm",
+            "modified": "2024-03-05",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/ijr5-qdv2",
-            "description": "The National Hospital Care Survey (NHCS) is designed to provide accurate and reliable health care statistics that answer key questions of interest to health care and public health professionals, researchers, and health care policy makers. This includes tracking the latest trends affecting hospitals and health care organizations and factors that influence the use of health care resources, the quality of health care, and disparities in health care services provided to population subgroups in the United States.\nNHCS collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings include inpatient, emergency (EDs), and outpatient departments (OPDs). The survey will provide hospital utilization statistics for the Nation. In addition, NHCS will also be able to monitor national trends in substance use-related ED visits including opioid visits.",
-            "title": "National Hospital Care Survey 2013-2016, 2019-2021, restricted data",
-            "isPartOf": "https://www.cdc.gov/nchs/nhds/nhds_questionnaires.htm",
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
+            "references": [
+                "https://www.cdc.gov/rdc/data/b1/2013_NHCS.pdf",
+                "https://www.cdc.gov/rdc/data/b1/2015_NHCS_RDC_Data_Dictionary.pdf",
+                "https://www.cdc.gov/rdc/data/b1/2016_NHCS_DATA-DICTIONARY.pdf",
+                "https://www.cdc.gov/rdc/data/b1/NHCS-RDC-Data-Dictionary.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "United States",
-            "describedBy": "NHCS collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings include inpatient, emergency (EDs), and outpatient departments (OPDs). The survey will provide hospital utilization statistics for the Nation.",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2013-2016, 2019-2021",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Care Survey 2013-2016, 2019-2021, restricted data"
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
-                "name": "National Center for Health Statistics"
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
@@ -42950,62 +42784,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ikd3-vynf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ikd3-vynf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ikd3-vynf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ikd3-vynf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ikd3-vynf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ikd3-vynf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ikd3-vynf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ikd3-vynf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ikd3-vynf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "accrualPeriodicity": "NA",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-07",
-            "temporal": "1999-2018",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/visualization/"
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
-            "identifier": "https://data.cdc.gov/api/views/iqm3-hbev",
+            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "description": "List of footnotes, notes, and source information for NHANES Summary Statistics. Each row of this dataset contains the accompanying text for a footnote found in the NHANES Datasets.",
-            "title": "DQS NHANES Footnotes",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43013,70 +42859,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iqm3-hbev/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iqm3-hbev/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iqm3-hbev/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iqm3-hbev/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "identifier": "https://data.cdc.gov/api/views/iqm3-hbev",
+            "issued": "2024-02-07",
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "NA",
+            "modified": "2025-01-31",
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
+            "title": "DQS NHANES Footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/irpc-yf8f",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "giardiasis",
-                "gonorrhea",
-                "haemophilus influenza",
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
-            "identifier": "https://data.cdc.gov/api/views/irpc-yf8f",
             "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Data for Haemophilus influenzae (age <5 for serotype b, nontypeable, non-b serotype, and unknown serotype) are available in Table I.",
-            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43084,72 +42921,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/irpc-yf8f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/irpc-yf8f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/irpc-yf8f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/irpc-yf8f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/irpc-yf8f",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenza",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/irpc-yf8f",
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
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza"
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
-            "temporal": "1933/2018",
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
-                "births",
-                "maternal age",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/isx2-c2ii",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "This dataset includes percent distribution of births for females by age group in the United States since 1933.\n\nThe number of states in the reporting area differ historically. In 1915 (when the birth registration area was established), 10 states and the District of Columbia reported births; by 1933, 48 states and the District of Columbia were reporting births, with the last two states, Alaska and Hawaii, added to the registration area in 1959 and 1960, when these regions gained statehood. Reporting area information is detailed in references 1 and 2 below. Trend lines for 1909\u20131958 are based on live births adjusted for under-registration; beginning with 1959, trend lines are based on registered live births.",
-            "title": "NCHS - Percent Distribution of Births for Females by Age Group: United States",
-            "isPartOf": "NCHS - Percent Distribution of Births for Females by Age Group: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43157,72 +42989,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/isx2-c2ii/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/isx2-c2ii/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/isx2-c2ii/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/isx2-c2ii/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
-            "license": "https://www.usa.gov/government-works",
-            "theme": [
-                "NCHS"
+            "identifier": "https://data.cdc.gov/api/views/isx2-c2ii",
+            "isPartOf": "NCHS - Percent Distribution of Births for Females by Age Group: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "births",
+                "maternal age",
+                "nchs",
+                "united states"
             ],
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-29",
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
+            "temporal": "1933/2018",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "NCHS - Percent Distribution of Births for Females by Age Group: United States"
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
-                "name": "National Center for Health Statistics"
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
@@ -43230,73 +43068,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/it4f-frdc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/it4f-frdc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/it4f-frdc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/it4f-frdc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/it4f-frdc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/it4f-frdc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/it4f-frdc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/it4f-frdc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/it4f-frdc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-                "sdoh-environmental",
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
-            "identifier": "https://data.cdc.gov/api/views/ite7-j2w7",
             "description": "Provisional count of deaths involving COVID-19 by United States county of occurrence, by week of death.",
-            "title": "AH COVID-19 Death Counts by County and Week, 2020-present",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43304,63 +43138,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ite7-j2w7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ite7-j2w7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ite7-j2w7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ite7-j2w7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "sdoh-environmental",
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
+                "name": "National Center for Health Statistics"
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
-            "identifier": "https://data.cdc.gov/api/views/ithv-4e9m",
             "description": "\u2022 COVID-19 vaccination coverage and parental intent among children 6 months to 17 years is assessed through the National Immunization Survey providing weekly COVID-19 vaccination coverage estimates (https://www.cdc.gov/vaccines/imz-managers/nis/about.html). \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey-Child COVID Module (NIS-CCM). Beginning January 2, 2024, the NIS-CCM was discontinued, and questions regarding receipt of COVID-19 vaccination among children were added to the NIS-Flu (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-cim). \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19.",
-            "title": "Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months-17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43368,69 +43212,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ithv-4e9m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ithv-4e9m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ithv-4e9m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/ithv-4e9m",
+            "issued": "2023-11-07",
+            "keyword": [
+                "covid-19 vaccination",
+                "nis"
+            ],
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/children-coverage-vaccination.html",
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2023-2024",
             "theme": [
                 "Child Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months-17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine"
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
@@ -43438,66 +43279,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/itia-u6fu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/itia-u6fu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/itia-u6fu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/itia-u6fu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/itia-u6fu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/itia-u6fu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/itia-u6fu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/itia-u6fu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/itia-u6fu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "data.cdc.gov"
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
@@ -43505,55 +43344,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iu3b-5ngj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iu3b-5ngj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iu3b-5ngj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/iu3b-5ngj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iu3b-5ngj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iu3b-5ngj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iu3b-5ngj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iu3b-5ngj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iu3b-5ngj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/iudi-d4pc",
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
-                "name": "data.cdc.gov"
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
@@ -43561,47 +43409,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/iudi-d4pc",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/iudi-d4pc",
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
+            "title": "Multi-Walled Carbon Nanotubes Induce Arachidonate 5-Lipoxygenase Expression and Enhance the Polarization and Function of M1 Macrophages in vitro"
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
@@ -43609,64 +43445,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iuq5-y9ct/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iuq5-y9ct/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iuq5-y9ct/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/iuq5-y9ct/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iuq5-y9ct/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iuq5-y9ct/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iuq5-y9ct/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iuq5-y9ct/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iuq5-y9ct/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
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
             "theme": [
                 "Behavioral Risk Factors"
-            ]
+            ],
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Historical Questions"
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
-            "identifier": "https://data.cdc.gov/api/views/ivdz-qhnr",
             "description": "\u2022\tMonthly Cumulative Percent of Persons Who Received \u22651 Influenza Vaccination Doses, by Influenza Season, Age Group and Jurisdiction.\n\n\u2022\tInfluenza (flu) vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly, in aggregate, by age group (https://www.cdc.gov/iis/about/).",
-            "title": "Monthly Cumulative Number and Percent of Persons Children 6 Months\u201317 Years Who Received \u22651 Influenza Vaccination Doses, by Influenza Season, Age Group, and Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43674,66 +43515,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ivdz-qhnr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ivdz-qhnr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ivdz-qhnr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ivdz-qhnr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ivdz-qhnr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ivdz-qhnr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ivdz-qhnr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ivdz-qhnr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ivdz-qhnr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/ivdz-qhnr",
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
+            "title": "Monthly Cumulative Number and Percent of Persons Children 6 Months\u201317 Years Who Received \u22651 Influenza Vaccination Doses, by Influenza Season, Age Group, and Jurisdiction, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccine-confidence",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-06-22",
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
-            "identifier": "https://data.cdc.gov/api/views/iwxc-qftf",
             "description": "National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent by demographics. \n\nFollowing collection of August 2021 survey data, an error in data processing led to incorrect categorization of some survey respondents; some respondents who should have been categorized as MSA: Principal City instead were categorized as MSA: Non-Principal City. Data downloaded during the period September 12, 2021 through September 30, 2021 may have incorrect estimates by MSA status, SVI of county of residence, and political leaning of county of residence.",
-            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Vaccination Status and Intent by Demographics",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43741,64 +43584,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iwxc-qftf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iwxc-qftf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iwxc-qftf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/iwxc-qftf",
+            "issued": "2022-06-22",
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
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Vaccination Status and Intent by Demographics"
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
-            "identifier": "https://data.cdc.gov/api/views/ix4g-rt8v",
+            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Se/ix4g-rt8v",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Services and Profiles dataset provides an overview of clinic services, the clinic\u2019s contact information, location, the medical director\u2019s name, and summary statistics.",
-            "title": "2022 Final Assisted Reproductive Technology (ART) Services and Profiles",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43806,60 +43646,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ix4g-rt8v/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ix4g-rt8v/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ix4g-rt8v/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Se/ix4g-rt8v",
+            "identifier": "https://data.cdc.gov/api/views/ix4g-rt8v",
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
+            "title": "2022 Final Assisted Reproductive Technology (ART) Services and Profiles"
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
-                "food safety",
-                "restaurant grading"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hao Tian",
                 "hasEmail": "mailto:ejq7@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
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
@@ -43867,60 +43711,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iyx3-z4r8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iyx3-z4r8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iyx3-z4r8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/iyx3-z4r8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iyx3-z4r8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iyx3-z4r8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iyx3-z4r8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iyx3-z4r8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iyx3-z4r8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/iyx3-z4r8",
+            "issued": "2022-10-17",
+            "keyword": [
+                "food safety",
+                "restaurant grading"
+            ],
+            "landingPage": "https://data.cdc.gov/d/iyx3-z4r8",
+            "modified": "2022-10-27",
+            "programCode": [
+                "009:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "spatial": "United States",
             "theme": [
                 "Environmental Health & Toxicology"
-            ]
+            ],
+            "title": "Outbreak Data - Restaurant Grading"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/iz46-hpaa",
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
-            "identifier": "https://data.cdc.gov/api/views/iz46-hpaa",
             "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
-            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 8 - Denver",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43928,66 +43772,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iz46-hpaa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iz46-hpaa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iz46-hpaa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/iz46-hpaa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iz46-hpaa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iz46-hpaa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/iz46-hpaa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/iz46-hpaa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/iz46-hpaa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/iz46-hpaa",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/iz46-hpaa",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 8 - Denver"
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
-            "modified": "2025-01-14",
-            "references": [
-                "https://www.cdc.gov/brfss/"
-            ],
-            "keyword": [
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
-            "identifier": "https://data.cdc.gov/api/views/j32a-sa6u",
+            "describedBy": "https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factors-Selected-Metropolitan-Area/j32a-sa6u",
             "description": "2011 to present. BRFSS SMART MMSA Prevalence combined land line and cell phone data. The Selected Metropolitan Area Risk Trends (SMART) project uses the Behavioral Risk Factor Surveillance System (BRFSS) to analyze the data of selected metropolitan statistical areas (MMSAs) with 500 or more respondents. BRFSS data can be used to identify emerging health problems, establish and track health objectives, and develop and evaluate public health policies and programs. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
-            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) MMSA Prevalence Data (2011 to Present)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43995,56 +43833,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/j32a-sa6u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j32a-sa6u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j32a-sa6u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/j32a-sa6u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j32a-sa6u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j32a-sa6u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/j32a-sa6u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j32a-sa6u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j32a-sa6u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factors-Selected-Metropolitan-Area/j32a-sa6u",
+            "identifier": "https://data.cdc.gov/api/views/j32a-sa6u",
+            "issued": "2023-07-18",
+            "keyword": [
+                "behavioral",
+                "brfss",
+                "mmsa",
+                "risk",
+                "smart",
+                "survey"
+            ],
+            "landingPage": "https://www.cdc.gov/brfss/",
+            "modified": "2025-01-14",
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
+            "title": "Behavioral Risk Factors: Selected Metropolitan Area Risk Trends (SMART) MMSA Prevalence Data (2011 to Present)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/j63e-g9bn",
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
-                "name": "data.cdc.gov"
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
@@ -44052,45 +43900,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/j63e-g9bn",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/j63e-g9bn",
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
+            "title": "Agreement of hip kinematics between two tracking marker configurations used with the 1 CODA pelvis during ergonomic roofing tasks"
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
-                "name": "data.cdc.gov"
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
@@ -44098,60 +43935,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j6gu-p9yd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j6gu-p9yd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j6gu-p9yd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic"
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
-                "name": "data.cdc.gov"
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
@@ -44159,67 +44002,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/j8jk-5ztv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j8jk-5ztv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j8jk-5ztv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/j8jk-5ztv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j8jk-5ztv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j8jk-5ztv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/j8jk-5ztv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j8jk-5ztv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j8jk-5ztv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "BRFSS Prevalence And Trends Data: Tobacco Use - Adults Who Are Current Smokers for 1995-2010"
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
-                "name": "data.cdc.gov"
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
@@ -44227,63 +44063,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/j9id-xrm6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j9id-xrm6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j9id-xrm6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/j9id-xrm6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j9id-xrm6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j9id-xrm6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/j9id-xrm6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/j9id-xrm6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/j9id-xrm6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis"
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
-                "sdoh-access-to-health-care",
-                "uninsured"
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
-            "identifier": "https://data.cdc.gov/api/views/jb9g-gnvr",
-            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
-            "title": "Indicators of Health Insurance Coverage at the Time of Interview",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, sex, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44291,67 +44132,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jb9g-gnvr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jb9g-gnvr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jb9g-gnvr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jb9g-gnvr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jb9g-gnvr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jb9g-gnvr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jb9g-gnvr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jb9g-gnvr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jb9g-gnvr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/jb9g-gnvr",
+            "issued": "2020-05-20",
+            "keyword": [
+                "uninsured",
+                "public coverage",
+                "private coverage",
+                "covid-19",
+                "sdoh-access-to-health-care"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/health-insurance-coverage.htm",
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
+            "title": "Indicators of Health Insurance Coverage at the Time of Interview"
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
-                "name": "CDC"
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
@@ -44359,52 +44202,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jbhn-e8xn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jbhn-e8xn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jbhn-e8xn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jbhn-e8xn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jbhn-e8xn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jbhn-e8xn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jbhn-e8xn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jbhn-e8xn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jbhn-e8xn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "CDC"
+            },
+            "spatial": "US",
             "theme": [
                 "Foodborne, Waterborne, and Related Diseases"
-            ]
+            ],
+            "title": "BEAM Dashboard - Report Data"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jbmi-9jqv",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/jbmi-9jqv",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44412,46 +44263,46 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jbmi-9jqv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jbmi-9jqv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jbmi-9jqv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jbmi-9jqv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jbmi-9jqv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jbmi-9jqv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jbmi-9jqv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jbmi-9jqv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jbmi-9jqv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/jbmi-9jqv",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/jbmi-9jqv",
+            "modified": "2024-07-23",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "dhds_dataset"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/jbxj-8pnr",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/jbxj-8pnr",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44459,62 +44310,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jbxj-8pnr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jbxj-8pnr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jbxj-8pnr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jbxj-8pnr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jbxj-8pnr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jbxj-8pnr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jbxj-8pnr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jbxj-8pnr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jbxj-8pnr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/jbxj-8pnr",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/jbxj-8pnr",
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
-                "name": "data.cdc.gov"
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
@@ -44522,49 +44360,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jcn4-jcv5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jcn4-jcv5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jcn4-jcv5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jcn4-jcv5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jcn4-jcv5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jcn4-jcv5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jcn4-jcv5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jcn4-jcv5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jcn4-jcv5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "data.cdc.gov"
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
-            "landingPage": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-04-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2020",
-            "modified": "2024-05-02",
-            "references": [
-                "https://www.cdc.gov/nchs/data/nhcs/2020-NHCS-PUF-Tech-Doc-508.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-INPATIENT-CODEBOOK-508.pdf, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-ED-CODEBOOK-508.pdf",
+            "describedByType": "application/pdf",
+            "description": "As a principal source of information on health care utilization in the United States, NHCS collects inpatient and emergency department data from a nationally representative sample of U.S. hospitals sourced from administrative and electronic health records data. The 2020 NHCS is conducted by the National Center for Health Statistics (NCHS) and is a member of the National Health Care Surveys \u2013 a family of surveys which measure health care utilization across a variety of health care providers and settings.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Inpatient and emergency department datasets are available for SAS, STATA, AND R at the link below.",
+                    "downloadURL": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
+                    "mediaType": "text/html",
+                    "title": "2020 NATIONAL HOSPITAL CARE SURVEY"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jdch-es95",
+            "issued": "2024-04-03",
             "keyword": [
                 "electronic health records",
                 "emergency departments",
@@ -44575,73 +44448,38 @@
                 "nhcs",
                 "united states"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-02",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/jdch-es95",
-            "description": "As a principal source of information on health care utilization in the United States, NHCS collects inpatient and emergency department data from a nationally representative sample of U.S. hospitals sourced from administrative and electronic health records data. The 2020 NHCS is conducted by the National Center for Health Statistics (NCHS) and is a member of the National Health Care Surveys \u2013 a family of surveys which measure health care utilization across a variety of health care providers and settings.",
-            "title": "National Hospital Care Survey, 2020 public-use file",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/nchs/nhcs/2020nhcs.htm",
-                    "description": "Inpatient and emergency department datasets are available for SAS, STATA, AND R at the link below.",
-                    "@type": "dcat:Distribution",
-                    "title": "2020 NATIONAL HOSPITAL CARE SURVEY"
-                }
+            "references": [
+                "https://www.cdc.gov/nchs/data/nhcs/2020-NHCS-PUF-Tech-Doc-508.pdf"
             ],
             "spatial": "United States",
-            "describedBy": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-INPATIENT-CODEBOOK-508.pdf, https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHCS/2020/2020-NHCS-PUF-ED-CODEBOOK-508.pdf",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Hospital Care Survey, 2020 public-use file"
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
-                "name": "data.cdc.gov"
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
@@ -44649,41 +44487,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jf8m-mtc3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jf8m-mtc3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jf8m-mtc3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jf8m-mtc3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2020-03-20",
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
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Imported"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "The Overview of Health Disparities analysis is a component of the Healthy People 2020 (HP2020) Final Review. The analysis included 611 objectives in HP2020. See Technical Notes for the Healthy People 2020 Overview of Health Disparities (https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities.htm) for additional information and criteria for objectives, data years, and population characteristics included in the analysis and statistical formulas and definitions for the disparities measures. \n\nThis file contains estimates and standard errors for the baseline and final years for individual population groups used in the Overview of Health Disparities analysis. The number and definitions of population groups varied across the HP2020 objectives and data sources used. These population groups are shown in the disparities file as originally reported by the data source, rather than the harmonized categories that were used for the HP2020 Progress by Population Group analysis (https://www.cdc.gov/nchs/healthy_people/hp2020/population-groups.htm). Additionally, for any given objective, the baseline and final years used for the disparities analysis do not necessarily correspond to the baseline and final years used to evaluate progress toward target attainment in the HP2020 Final Review Progress Table (https://www.cdc.gov/nchs/healthy_people/hp2020/progress-tables.htm) and Progress by Population Group analysis (https://www.cdc.gov/nchs/healthy_people/hp2020/population-groups.htm). These distinctions should be considered when merging the downloadable Progress Table or Progress by Population Group data files with the Overview of Health Disparities data files, or when integrative analyses that incorporate both disparities and progress data are conducted.  \n    \nData for additional years during the HP2020 tracking period that are not included in the Overview of Health Disparities are available on the HP2020 website (https://www.healthypeople.gov/2020/).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jfbs-8cpp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/jfbs-8cpp/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/jfbs-8cpp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/jfbs-8cpp/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/jfbs-8cpp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/jfbs-8cpp/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/jfbs-8cpp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/jfbs-8cpp",
             "issued": "2022-03-09",
-            "@type": "dcat:Dataset",
-            "temporal": "1997-01-01/2018-12-31",
-            "modified": "2023-08-23",
             "keyword": [
                 "health disparities",
                 "healthy people 2020",
@@ -44712,96 +44605,39 @@
                 "sdoh-use-of-health-care",
                 "sdoh-workplace"
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
-            "identifier": "https://data.cdc.gov/api/views/jfbs-8cpp",
-            "description": "The Overview of Health Disparities analysis is a component of the Healthy People 2020 (HP2020) Final Review. The analysis included 611 objectives in HP2020. See Technical Notes for the Healthy People 2020 Overview of Health Disparities (https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities.htm) for additional information and criteria for objectives, data years, and population characteristics included in the analysis and statistical formulas and definitions for the disparities measures. \n\nThis file contains estimates and standard errors for the baseline and final years for individual population groups used in the Overview of Health Disparities analysis. The number and definitions of population groups varied across the HP2020 objectives and data sources used. These population groups are shown in the disparities file as originally reported by the data source, rather than the harmonized categories that were used for the HP2020 Progress by Population Group analysis (https://www.cdc.gov/nchs/healthy_people/hp2020/population-groups.htm). Additionally, for any given objective, the baseline and final years used for the disparities analysis do not necessarily correspond to the baseline and final years used to evaluate progress toward target attainment in the HP2020 Final Review Progress Table (https://www.cdc.gov/nchs/healthy_people/hp2020/progress-tables.htm) and Progress by Population Group analysis (https://www.cdc.gov/nchs/healthy_people/hp2020/population-groups.htm). These distinctions should be considered when merging the downloadable Progress Table or Progress by Population Group data files with the Overview of Health Disparities data files, or when integrative analyses that incorporate both disparities and progress data are conducted.  \n    \nData for additional years during the HP2020 tracking period that are not included in the Overview of Health Disparities are available on the HP2020 website (https://www.healthypeople.gov/2020/).",
-            "title": "Population Group Estimates used in the Healthy People 2020 Overview of Health Disparities",
+            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities.htm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-08-23",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/jfbs-8cpp/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jfbs-8cpp/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/jfbs-8cpp/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jfbs-8cpp/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/jfbs-8cpp/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jfbs-8cpp/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/jfbs-8cpp/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
             "spatial": "US",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
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
-            "identifier": "https://data.cdc.gov/api/views/jgk8-6dpn",
             "description": "Reporting of Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. This dataset will receive a final update on June 1, 2023, to reconcile historical data through May 10, 2023, and will remain publicly available.\n\nThis archived public use dataset contains historical case and percent positivity data updated weekly for all available counties and jurisdictions. Each week, the dataset was refreshed to capture any historical updates. Please note, percent positivity data may be incomplete for the most recent time period.\n\n<b>Related data </b>\nCDC provides the public with two active versions of COVID-19 county-level community transmission level data: this dataset with historical case and percent positivity data for each county from January 22, 2020 (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">Weekly Historical Changes dataset</a>) and a dataset with the levels as originally posted (<a href=\"https://data.cdc.gov/dataset/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly Originally Posted dataset</a>) since October 20, 2022. <b>Please navigate to the <a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly Originally Posted dataset</a> for the Community Transmission Levels published weekly on Thursdays.</b>\n\n<b>Methods for calculating county level of community transmission indicator</b>\nThe County Level of Community Transmission indicator uses two metrics: (1) total new COVID-19 cases per 100,000 persons in the last 7 days and (2) percentage of positive SARS-CoV-2 diagnostic nucleic acid amplification tests (NAAT) in the last 7 days. For each of these metrics, CDC classifies transmission values as low, moderate, substantial, or high (below and <a href=\"https://www.cdc.gov/mmwr/volumes/70/wr/mm7030e2.htm?s_cid=mm7030e2_w#T1_down\">here</a>). If the values for each of these two metrics differ (e.g., one indicates moderate and the other low), then the higher of the two should be used for decision-making. \n\n<b>CDC core metrics of and thresholds for community transmission levels of SARS-CoV-2</b>\n<b>Total New Case Rate Metric:</b> \"New cases per 100,000 persons in the past 7 days\" is calculated by adding the number of new cases in the county (or other administrative level) in the last 7 days divided by the population in the county (or other administrative level) and multiplying by 100,000. \"New cases per 100,000 persons in the past 7 days\" is considered to have transmission level of Low (0-9.99); Moderate (10.00-49.99); Substantial (50.00-99.99); and High (greater than or equal to 100.00). \n\n<b>Test Percent Positivity Metric:</b> \"Percentage of positive NAAT in the past 7 days\" is calculated by dividing the number of positive tests in the county (or other administrative level) during the last 7 days by the total number of tests resulted over the last 7 days. \"Percentage of positive NAAT in the past 7 days\" is considered to have transmission level of Low (less than 5.00); Moderate (5.00-7.99); Substantial (8.00-9.99); and High (greater than or equal to 10.00). \n\n\nThe data in this dataset are considered provisional by CDC and are subject to change until the data are reconciled and verified with the state and territorial data providers. \n\nThis dataset is created using <a href=\"https://www.cdc.gov/maso/policy/policy385.pdf\">CDC\u2019s Policy on Public Health Research and Nonresearch Data Management and Access</a>.\n\n\n<b>Archived data </b>\nCDC has archived two prior versions of these datasets. Both versions contain the same 7 data elements reflecting community transmission levels for all available counties and jurisdictions; however, the datasets updated daily. The archived datasets can be found here:  \n\n<a href=\"https://data.cdc.gov/Public-Health-Surveillance/United-States-COVID-19-County-Level-of-Community-T",
-            "title": "Weekly COVID-19 County Level of Community Transmission Historical Changes - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44809,58 +44645,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jgk8-6dpn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jgk8-6dpn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jgk8-6dpn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jgk8-6dpn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jgk8-6dpn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jgk8-6dpn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jgk8-6dpn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jgk8-6dpn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jgk8-6dpn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "laboratory",
+                "ncird-corvd"
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
+                "name": "CDC"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/jgkt-w9bh",
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
-            "identifier": "https://data.cdc.gov/api/views/jgkt-w9bh",
             "description": "Air pollution serves as a major risk factor for the development of asthma, respiratory disease and heart disease. Diesel particulate and fumes are a major contributor to air pollution. Workers in a number of different occupations, including mining, oil and gas exploration and refining, and drivers of heavy equipment who are regularly exposed to diesel exhaust while on the job, and persons living in areas with high levels of air pollution, are at an increased risk for developing asthma, cardiovascular disease and certain cancers.\n\nUnderstanding the physiological and cellular effects of diesel exhaust inhalation on Various organs in the body is critical for identifying exposure-induced biological and physiological markers of disease or dysfunction. The experiments in this manuscript, focus on the effects of diesel exhaust (DE) inhalation on peripheral and cardiovascular function. In the current studies, we hypothesized that the development of cardiovascular disease in workers regularly exposed to DE is the result of the inhalation of volatile gases and particulate within the vapor that affect the cardiovascular system by altering physiological and cellular processes that affect peripheral vascular responsiveness to agents that cause blood vessels to constrict and vessels that cause blood vessels to dilate, blood pressure, cardiac output and kidney function (kidney function as it may contribute to changes in blood pressure). We also predicted that these changes in physiology would be associated with changes in the expression of proteins and the production of genes that play a role in regulating oxidative stress, responses to decreases in oxygen, and markers of kidney function that are associated with blood pressure.",
-            "title": "The effects of diesel exhaust inhalation on cardiovascular function",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44868,34 +44716,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jgkt-w9bh",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/jgkt-w9bh",
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
+            "title": "The effects of diesel exhaust inhalation on cardiovascular function"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/jj3m-siz7",
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
-                "name": "data.cdc.gov"
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
@@ -44903,42 +44751,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jj3m-siz7",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.cdc.gov/d/jj3m-siz7",
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
+            "title": "Gene Expression Profiles of Di-n-butyl Phthalate in Normal Human Mammary Epithelial Cells"
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
-            "modified": "2025-01-31",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -44946,78 +44787,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jjpx-mxt8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jjpx-mxt8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jjpx-mxt8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jjpx-mxt8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jjpx-mxt8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jjpx-mxt8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jjpx-mxt8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jjpx-mxt8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jjpx-mxt8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-            "landingPage": "https://data.cdc.gov/d/jk8p-fqhn",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-02-17",
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
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/jk8p-fqhn",
             "description": "<p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>This site provides historical data related to COVID-19 booster dose eligibility presented on two CDC COVID Data Tracker sites:&nbsp;</span><a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccinations\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Vaccinations in the US</span></a><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;and&nbsp;</span><a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccination-equity\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Vaccination Equity</span></a><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>.&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Data are updated weekly on Thursdays.</span></p><p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Some COVID-19 vaccine recipients are&nbsp;</span><a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>eligible to receive booster doses</span></a><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>,&nbsp;</span><span style=\"font-size:11px;\">&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>and criteria for booster eligibility may change over time. Data and footnotes will be updated to align with the current recommendations.&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span></p><p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>CDC counts people as having &ldquo;received a booster dose&rdquo; if they are fully vaccinated and received another dose of any COVID-19 vaccine on or after August 13, 2021. This does not distinguish whether the recipient is&nbsp;</span><a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/recommendations/immuno.html\" target=\"_blank\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>immunocompromised and received an additional dose</span></a></p><p style=\"margin:0in;vertical-align:baseline;\"><strong><em><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Data Limitations:</span></em></strong><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span></p><ul style=\"list-style-type: undefined;margin-left:0in;\"><li><span style='font-family:\"Calibri\",sans-serif;color:black;font-size:11.0pt;color:black;'>The booster eligibility metric excludes fully vaccinated recipients who have an &ldquo;Other&rdquo; primary series vaccine type.\u202f</span><span style='font-family:\"Calibri\",sans-serif;font-size:11.0pt;color:black;'>&nbsp;</span></li><li><span style='font-family:\"Calibri\",sans-serif;color:black;font-size:11.0pt;color:black;'>Booster eligibility counts and percentages exclude vaccine administrations reported by Texas as the primary series cannot be linked to booster dose in the aggregate data submitted by Texas.</span><span style='font-family:\"Calibri\",sans-serif;font-size:11.0pt;color:black;'>&nbsp;</span></li></ul><p style=\"margin:0in;vertical-align:baseline;\"><strong><em><span style='font-size:15px;font-family:\"Calibri\",sans-serif;'>Footnotes:</span></em></strong></p><p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;'>CDC counts people as being &ldquo;</span><a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:windowtext;'>eligible to get a booster dose</span></a><",
-            "title": "COVID-19 Booster Dose Eligibility in the United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45025,63 +44857,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jk8p-fqhn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jk8p-fqhn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jk8p-fqhn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.xml?accessType=DOWNLOAD",
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
-            "landingPage": "https://data.cdc.gov/d/jkmz-c8jz",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2022-01-12",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
+            "identifier": "https://data.cdc.gov/api/views/jk8p-fqhn",
+            "issued": "2022-02-17",
             "keyword": [
-                "community mitigation",
+                "administration",
+                "age",
+                "coronavirus",
                 "covid-19",
-                "school closure"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Nicole Zviedrite",
-                "hasEmail": "mailto:jmu6@cdc.gov"
-            },
+                "demographics",
+                "ethnicity",
+                "immunization",
+                "izdl",
+                "race",
+                "sex",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/jk8p-fqhn",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-05-12",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "CI-ICU/DGMQ/CDC"
+                "name": "CDC"
             },
-            "identifier": "https://data.cdc.gov/api/views/jkmz-c8jz",
-            "description": "Data on distance learning and supplemental feeding programs were collected from a stratified sample of 600 school districts. School districts were divided into quartiles based on the percentage of students eligible for free/reduced-price lunch, an indicator of family economic status, as reported by the National Center for Education Statistics (https://nces.ed.gov/ccd/). A simple random sample was taken in each stratum, and sample size per stratum was calculated using 95% confidence interval of 50% \u00b1 10%. Data on the availability and method of delivery of both distance learning and supplemental feeding programs were collected from publicly available announcements on school district websites and their official social media pages (Facebook, Twitter). Google searches were performed for news resources when information was not available from online district sources.",
-            "title": "Efforts to sustain education and subsidized meal programs during COVID-19-related school closures, United States, March-June 2020",
-            "programCode": [
-                "009:020"
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "spatial": "US",
+            "temporal": "2020-12-13/2023-05-12",
+            "theme": [
+                "Vaccinations"
+            ],
+            "title": "COVID-19 Booster Dose Eligibility in the United States"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Nicole Zviedrite",
+                "hasEmail": "mailto:jmu6@cdc.gov"
+            },
+            "description": "Data on distance learning and supplemental feeding programs were collected from a stratified sample of 600 school districts. School districts were divided into quartiles based on the percentage of students eligible for free/reduced-price lunch, an indicator of family economic status, as reported by the National Center for Education Statistics (https://nces.ed.gov/ccd/). A simple random sample was taken in each stratum, and sample size per stratum was calculated using 95% confidence interval of 50% \u00b1 10%. Data on the availability and method of delivery of both distance learning and supplemental feeding programs were collected from publicly available announcements on school district websites and their official social media pages (Facebook, Twitter). Google searches were performed for news resources when information was not available from online district sources.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45089,46 +44932,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jkmz-c8jz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jkmz-c8jz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jkmz-c8jz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jkmz-c8jz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jkmz-c8jz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jkmz-c8jz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jkmz-c8jz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jkmz-c8jz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jkmz-c8jz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "CI-ICU/DGMQ/CDC"
+            },
             "theme": [
                 "Policy Surveillance"
-            ]
+            ],
+            "title": "Efforts to sustain education and subsidized meal programs during COVID-19-related school closures, United States, March-June 2020"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/MatchRate-Tables.pdf",
+            "describedByType": "application/pdf",
+            "description": "NCHS has linked data from various surveys with End Stage Renal Disease (ESRD) data obtained from the United States Renal Data System (USRDS). Linkage of the data from NCHS survey participants with the USRDS ESRD data provides the opportunity to study changes in health status and health care utilization among patients diagnosed with ESRD.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jmgj-74h4",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-16",
             "keyword": [
                 "linked usrds esrd files",
                 "nchs surveys",
@@ -45154,80 +45024,38 @@
                 "sdoh-use-of-health-care",
                 "sdoh-workplace"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCHS Data Linkage Program",
-                "hasEmail": "mailto:DataLinkage@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/esrd-restricted.htm",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/jmgj-74h4",
-            "description": "NCHS has linked data from various surveys with End Stage Renal Disease (ESRD) data obtained from the United States Renal Data System (USRDS). Linkage of the data from NCHS survey participants with the USRDS ESRD data provides the opportunity to study changes in health status and health care utilization among patients diagnosed with ESRD.",
-            "title": "NCHS Survey Data Linked to United States Renal Data System (USRDS) End-Stage Renal Disease Files",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/Variable-List.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/MatchRate-Tables.pdf",
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
-                "name": "data.cdc.gov"
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
@@ -45235,76 +45063,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jnru-aqxk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jnru-aqxk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jnru-aqxk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "data.cdc.gov"
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
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-05-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-08",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "excess deaths",
-                "hispanic origin",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "race",
-                "sex",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/jqg8-ycmh",
             "description": "Quarterly data on the number of deaths from all causes by state (of occurrence), sex, age group, and race/Hispanic origin group for the United States. Counts of deaths in more recent time periods can be compared with counts from earlier years (2015-2019) to determine if the number is higher than expected. Annual and cumulative counts (from Quarter 2, 2020 through the most recent quarter) are also shown.",
-            "title": "AH Quarterly Excess Deaths by State, Sex, Age, and Race",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45312,71 +45142,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jqg8-ycmh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jqg8-ycmh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jqg8-ycmh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jqg8-ycmh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jqg8-ycmh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jqg8-ycmh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jqg8-ycmh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jqg8-ycmh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jqg8-ycmh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/jqg8-ycmh",
+            "issued": "2021-05-20",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "excess deaths",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "sex",
+                "state",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-09-08",
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
+            "title": "AH Quarterly Excess Deaths by State, Sex, Age, and Race"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/infant-mortality.htm",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2016-11-21",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-01-01/2024-06-30",
-            "modified": "2024-11-27",
-            "keyword": [
-                "causes of death",
-                "deaths",
-                "infant mortality",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "quarterly",
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
-            "identifier": "https://data.cdc.gov/api/views/jqwm-z2g9",
             "description": "Provisional estimates of infant mortality (deaths of infants under 1 year per 1,000 live births), neonatal mortality (deaths of infants aged 0-27 days per 1,000 live births), postneonatal mortality (deaths of infants aged 28 days through 11 months per 1,000 live births), and death rates for the five leading causes of infant death.",
-            "title": "NCHS - VSRR Quarterly provisional estimates for infant mortality",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45384,68 +45220,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jqwm-z2g9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jqwm-z2g9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jqwm-z2g9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jqwm-z2g9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jqwm-z2g9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jqwm-z2g9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jqwm-z2g9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jqwm-z2g9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jqwm-z2g9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/jqwm-z2g9",
+            "issued": "2016-11-21",
+            "keyword": [
+                "causes of death",
+                "deaths",
+                "infant mortality",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "quarterly",
+                "united states",
+                "vsrr"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/infant-mortality.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-11-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2022-01-01/2024-06-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - VSRR Quarterly provisional estimates for infant mortality"
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
-                "name": "data.cdc.gov"
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
@@ -45453,63 +45291,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jr4g-zdpg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jr4g-zdpg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jr4g-zdpg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup"
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
-            "modified": "2025-01-31",
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
-                "name": "data.cdc.gov"
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
@@ -45517,69 +45358,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jr58-6ysp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jr58-6ysp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jr58-6ysp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jr58-6ysp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jr58-6ysp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jr58-6ysp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jr58-6ysp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jr58-6ysp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jr58-6ysp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
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
-            "landingPage": "https://data.cdc.gov/d/ju63-2fep",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-28",
-            "keyword": [
-                "2021",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ju63-2fep",
             "description": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45587,61 +45424,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ju63-2fep/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ju63-2fep/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ju63-2fep/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ju63-2fep/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ju63-2fep/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ju63-2fep/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ju63-2fep/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ju63-2fep/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ju63-2fep/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ju63-2fep",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "anthrax",
+                "arboviral diseases",
+                "chikungunya virus disease",
+                "eastern equine encephalitis virus disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ju63-2fep",
+            "modified": "2022-01-28",
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
+            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease"
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
-            "identifier": "https://data.cdc.gov/api/views/judz-8etw",
             "description": "\u2022 Weekly Influenza Vaccination Status and Intent for Vaccination, Overall, by Selected Demographics, and Jurisdiction, Children 6 Months-17 Years. \n\n\u2022 Weekly Influenza vaccination coverage and parental intent for vaccination among children is calculated using data from the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html). NIS\u2013Flu is a national random-digit-dialed cellular telephone survey of households with children ages 6 months\u201317 years conducted during October-June. The respondent to a NIS\u2013Flu survey is a parent or guardian who said they were knowledgeable about the child\u2019s vaccination history. All estimates are based upon parental report of receipt of vaccination and month of that vaccination.",
-            "title": "Weekly Influenza Vaccination Status and Intent for Vaccination, Overall, by Selected Demographics, and Jurisdiction, Children 6 Months-17 Years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45649,71 +45492,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/judz-8etw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/judz-8etw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/judz-8etw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/judz-8etw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/judz-8etw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/judz-8etw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/judz-8etw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/judz-8etw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/judz-8etw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "Weekly Influenza Vaccination Status and Intent for Vaccination, Overall, by Selected Demographics, and Jurisdiction, Children 6 Months-17 Years, United States"
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
-                "name": "National Center for Health Statistics"
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
@@ -45721,76 +45560,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jvf6-ix4w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jvf6-ix4w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jvf6-ix4w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jvf6-ix4w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jvf6-ix4w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jvf6-ix4w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jvf6-ix4w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jvf6-ix4w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jvf6-ix4w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-                "name": "National Center for Health Statistics"
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
@@ -45798,70 +45631,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jwta-jxbg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jwta-jxbg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jwta-jxbg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jwta-jxbg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jwta-jxbg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jwta-jxbg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jwta-jxbg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jwta-jxbg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jwta-jxbg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-                "name": "National Center for Health Statistics"
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
@@ -45869,64 +45705,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jx6g-fdh6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jx6g-fdh6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jx6g-fdh6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jx6g-fdh6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jx6g-fdh6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jx6g-fdh6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jx6g-fdh6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jx6g-fdh6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jx6g-fdh6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
@@ -45934,46 +45775,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jxu8-x79m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jxu8-x79m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jxu8-x79m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jxu8-x79m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jxu8-x79m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jxu8-x79m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jxu8-x79m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jxu8-x79m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jxu8-x79m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
@@ -45982,80 +45852,40 @@
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
                 "name": "National Center for Health Statistics"
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
@@ -46063,66 +45893,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jz6n-v26y/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jz6n-v26y/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jz6n-v26y/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jz6n-v26y/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jz6n-v26y/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jz6n-v26y/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jz6n-v26y/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jz6n-v26y/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jz6n-v26y/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/jz7r-jrma",
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
-                "tetanus",
-                "varicella",
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
-            "identifier": "https://data.cdc.gov/api/views/jz7r-jrma",
             "description": "NNDSS - Table II. Tetanus to Varicella - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
-            "title": "NNDSS - Table II. Tetanus to Varicella",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46130,73 +45968,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jz7r-jrma/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jz7r-jrma/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/jz7r-jrma/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/jz7r-jrma/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/jz7r-jrma",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "varicella",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/jz7r-jrma",
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
+            "title": "NNDSS - Table II. Tetanus to Varicella"
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
@@ -46204,41 +46034,104 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k25u-mg9b/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k25u-mg9b/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k25u-mg9b/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k25u-mg9b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "500 Cities & Places"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
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
+            "theme": [
+                "500 Cities & Places"
+            ],
+            "title": "500 Cities: Census Tract-level Data (GIS Friendly Format), 2018 release"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Annual (R/P1Y)",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:healthus@cdc.gov"
+            },
+            "description": "Data on cholesterol in adults age 20 and older in the United States, by selected characteristics. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k2e8-8t3h/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/k2e8-8t3h/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/k2e8-8t3h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/k2e8-8t3h/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/k2e8-8t3h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/k2e8-8t3h/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/k2e8-8t3h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/k2e8-8t3h",
             "issued": "2024-07-11",
-            "temporal": "1988/2020",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
             "keyword": [
                 "cholesterol",
                 "chronic conditions",
@@ -46261,99 +46154,149 @@
                 "sdoh-use-of-health-care",
                 "total cholesterol"
             ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-07",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "temporal": "1988/2020",
+            "theme": [
+                "National Center for Health Statistics"
+            ],
+            "title": "DQS Cholesterol in adults age 20 and older, by selected characteristics: United States"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:healthus@cdc.gov"
+                "fn": "Health Effects Laboratory Division, Toxicology and Molecular Biology Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
+            "description": "Nanomaterials represent a new class of materials with numerous industrial applications. Considering the projected increase in the production and use of nanomaterials, a corresponding increase in occupational exposure to nanomaterials and their resulting adverse health effects may be anticipated among workers. There is substantial evidence in the literature, based on cell culture and animal studies, supporting the potential toxicity and detrimental health effects associated with exposure to nanomaterials. Intervention and/or prevention of adverse health effects associated with occupational exposure to toxic nanomaterials is a concern for health providers and regulatory and non-regulatory government agencies as the use of nanomaterials expand. A key element in the intervention and/or prevention of the adverse health effects associated with occupational exposure to toxic nanomaterials is a clear understanding of the molecular mechanisms underlying the pulmonary toxicity induced by nanomaterials.\n\nDue to its physicochemical and mechanical properties, multi-walled carbon nanotubes (MWCNT) have found many industrial applications. There is potential for human exposure to MWCNT or products that contain MWCNT both during the production and use of the materials that contain MWCNT. The objectives of the current study were to investigate MWCNT-induced lung toxicity and the molecular mechanisms underlying that toxicity. A rat inhalation exposure model was employed to determine the lung toxicity induced by MWCNT. Global gene expression profiles in the lung and blood were conducted to determine the molecular mechanisms underlying MWCNT-induced lung toxicity.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/k2fe-zny8/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/k2fe-zny8",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/k2fe-zny8",
+            "modified": "2024-11-20",
+            "programCode": [
+                "009:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
+                "name": "data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/k2e8-8t3h",
-            "description": "Data on cholesterol in adults age 20 and older in the United States, by selected characteristics. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Cholesterol in adults age 20 and older, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
+            "theme": [
+                "National Institute for Occupational Safety and Health"
             ],
+            "title": "Pulmonary toxicity and gene expression changes in response to whole-body inhalation exposure to multi-walled carbon nanotubes in rats-Dataset"
+        },
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
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/k2e8-8t3h/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k2e8-8t3h/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/k2e8-8t3h/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/k4cb-dxd7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k2e8-8t3h/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/k2e8-8t3h/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/k4cb-dxd7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k2e8-8t3h/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/k2e8-8t3h/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/k4cb-dxd7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k4cb-dxd7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
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
-            "accrualPeriodicity": "Annual (R/P1Y)",
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
-                "National Center for Health Statistics"
-            ]
+                "Vaccinations"
+            ],
+            "title": "Weekly Cumulative RSV Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 75 and Older and 60-74 Years with High-Risk Conditions Ever Vaccinated, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/k2fe-zny8",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "Health Effects Laboratory Division, Toxicology and Molecular Biology Branch",
-                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/k2fe-zny8",
-            "description": "Nanomaterials represent a new class of materials with numerous industrial applications. Considering the projected increase in the production and use of nanomaterials, a corresponding increase in occupational exposure to nanomaterials and their resulting adverse health effects may be anticipated among workers. There is substantial evidence in the literature, based on cell culture and animal studies, supporting the potential toxicity and detrimental health effects associated with exposure to nanomaterials. Intervention and/or prevention of adverse health effects associated with occupational exposure to toxic nanomaterials is a concern for health providers and regulatory and non-regulatory government agencies as the use of nanomaterials expand. A key element in the intervention and/or prevention of the adverse health effects associated with occupational exposure to toxic nanomaterials is a clear understanding of the molecular mechanisms underlying the pulmonary toxicity induced by nanomaterials.\n\nDue to its physicochemical and mechanical properties, multi-walled carbon nanotubes (MWCNT) have found many industrial applications. There is potential for human exposure to MWCNT or products that contain MWCNT both during the production and use of the materials that contain MWCNT. The objectives of the current study were to investigate MWCNT-induced lung toxicity and the molecular mechanisms underlying that toxicity. A rat inhalation exposure model was employed to determine the lung toxicity induced by MWCNT. Global gene expression profiles in the lung and blood were conducted to determine the molecular mechanisms underlying MWCNT-induced lung toxicity.",
-            "title": "Pulmonary toxicity and gene expression changes in response to whole-body inhalation exposure to multi-walled carbon nanotubes in rats-Dataset",
-            "programCode": [
-                "009:034"
-            ],
+            "description": "Explore the Going Smokefree Matters \u2013 In Your Home Infographic which outlines key facts related to the effects of secondhand smoke exposure in the home.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/k2fe-zny8/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
+                    "downloadURL": "https://data.cdc.gov/download/k4xj-uge6/application/pdf",
+                    "mediaType": "application/pdf"
                 }
             ],
-            "theme": [
-                "National Institute for Occupational Safety and Health"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/k4xj-uge6",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/k4xj-uge6",
             "issued": "2016-06-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
             "keyword": [
                 "fact sheet",
                 "housing",
@@ -46361,68 +46304,33 @@
                 "secondhand smoke",
                 "smokefree"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/k4xj-uge6",
+            "modified": "2023-07-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/k4xj-uge6",
-            "description": "Explore the Going Smokefree Matters \u2013 In Your Home Infographic which outlines key facts related to the effects of secondhand smoke exposure in the home.",
-            "title": "Going Smokefree Matters - In Your Home Infographic",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/k4xj-uge6/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
             "theme": [
                 "Policy"
-            ]
+            ],
+            "title": "Going Smokefree Matters - In Your Home Infographic"
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
-                "city",
-                "estimates",
-                "prevalence"
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
-            "identifier": "https://data.cdc.gov/api/views/k56w-7tny",
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-City-level-Data-GIS-Friendly-Format-201/k56w-7tny",
             "description": "2014, 2013. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project census city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level.",
-            "title": "500 Cities: City-level Data (GIS Friendly Format), 2016 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46430,76 +46338,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k56w-7tny/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k56w-7tny/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k56w-7tny/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k56w-7tny/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k56w-7tny/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k56w-7tny/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k56w-7tny/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k56w-7tny/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k56w-7tny/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-City-level-Data-GIS-Friendly-Format-201/k56w-7tny",
+            "identifier": "https://data.cdc.gov/api/views/k56w-7tny",
+            "issued": "2023-07-18",
+            "keyword": [
+                "500cities",
+                "city",
+                "estimates",
+                "prevalence"
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
+            "title": "500 Cities: City-level Data (GIS Friendly Format), 2016 release"
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
-                "name": "National Center for Health Statistics"
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
@@ -46507,62 +46407,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5dc-apj8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k5dc-apj8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k5dc-apj8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5dc-apj8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k5dc-apj8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k5dc-apj8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k5dc-apj8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k5dc-apj8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k5dc-apj8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-                "name": "data.cdc.gov"
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
@@ -46570,69 +46486,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k62p-6esq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k62p-6esq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k62p-6esq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "Annually",
+            "identifier": "https://data.cdc.gov/api/views/k62p-6esq",
+            "issued": "2021-05-04",
+            "keyword": [
+                "dhds",
+                "disability"
+            ],
+            "landingPage": "https://data.cdc.gov/d/k62p-6esq",
+            "modified": "2024-07-19",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
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
-                "name": "National Center for Health Statistics"
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
@@ -46640,77 +46548,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k6sd-3kb8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k6sd-3kb8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k6sd-3kb8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k6sd-3kb8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k6sd-3kb8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k6sd-3kb8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k6sd-3kb8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k6sd-3kb8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k6sd-3kb8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "ftp.cdc.gov - /pub/Health_Statistics/NCHS/Dataset_Documentation/NHAMCS/",
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
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annually. Dataset will no longer be updated after the 2022 release in summer 2024.",
+            "modified": "2024-10-24",
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
+            "temporal": "2016-2022",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Estimate of Emergency Department Visits in the United States, 2016-2022"
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
@@ -46718,65 +46620,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k86t-wghb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k86t-wghb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k86t-wghb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k86t-wghb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k86t-wghb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k86t-wghb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k86t-wghb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k86t-wghb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k86t-wghb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -46784,72 +46695,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k87d-gv3u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k87d-gv3u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k87d-gv3u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-09",
-            "references": [
-                "https://www.cdc.gov/nccdphp/dnpao/index.html"
-            ],
-            "keyword": [
-                "breastfeeding",
-                "dnpao",
-                "fruit",
-                "nutrition",
-                "physical activity",
-                "vegetable"
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
-            "identifier": "https://data.cdc.gov/api/views/k8w5-7ju6",
+            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Policy-and/k8w5-7ju6",
             "description": "This dataset includes data on policy and environmental supports for physical activity, diet, and breastfeeding. This data is used for DNPAO's Data, Trends, and Maps database, which provides national and state specific data on obesity, nutrition, physical activity, and breastfeeding.",
-            "title": "Nutrition, Physical Activity, and Obesity - Policy and Environmental Data",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46857,71 +46766,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k8w5-7ju6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k8w5-7ju6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k8w5-7ju6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k8w5-7ju6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k8w5-7ju6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k8w5-7ju6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k8w5-7ju6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k8w5-7ju6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k8w5-7ju6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Nutrition-Physical-Activity-and-Obesity/Nutrition-Physical-Activity-and-Obesity-Policy-and/k8w5-7ju6",
+            "identifier": "https://data.cdc.gov/api/views/k8w5-7ju6",
+            "issued": "2023-07-18",
+            "keyword": [
+                "breastfeeding",
+                "dnpao",
+                "fruit",
+                "nutrition",
+                "physical activity",
+                "vegetable"
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
+            "title": "Nutrition, Physical Activity, and Obesity - Policy and Environmental Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-06-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "county",
-                "covid-19",
-                "deaths",
-                "hispanic origin",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "race",
-                "sdoh-environmental",
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
-            "identifier": "https://data.cdc.gov/api/views/k8wy-p9cg",
             "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nCounty data on race and Hispanic origin is available for counties with more than 100 COVID-19 deaths.\u00a0Deaths are cumulative from the week ending January 4, 2020 to the most recent reporting week, and based on county of occurrence. Data is provisional. \n\nUrban-rural classification is based on the 2013 National Center for Health Statistics Urban-Rural Classification Scheme for Counties (https://www.cdc.gov/nchs/data_access/urban_rural.htm).",
-            "title": "Provisional COVID-19 Deaths by County, and Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46929,62 +46834,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k8wy-p9cg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k8wy-p9cg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k8wy-p9cg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/k8wy-p9cg",
+            "issued": "2020-06-24",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "deaths",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "sdoh-environmental",
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
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 Deaths by County, and Race and Hispanic Origin"
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
-                "name": "data.cdc.gov"
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
@@ -46992,66 +46907,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k9ai-xgx2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k9ai-xgx2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k9ai-xgx2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/k9ai-xgx2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k9ai-xgx2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k9ai-xgx2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/k9ai-xgx2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/k9ai-xgx2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/k9ai-xgx2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/k9ai-xgx2",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/k9ai-xgx2",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 6 - Dallas"
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
-                "name": "data.cdc.gov"
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
@@ -47059,72 +46967,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kebt-3t25/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kebt-3t25/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kebt-3t25/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.xml?accessType=DOWNLOAD",
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
             ],
-            "issued": "2024-08-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-23",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
+            "landingPage": "https://data.cdc.gov/d/kebt-3t25",
+            "modified": "2022-01-12",
+            "programCode": [
+                "009:020"
             ],
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
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
+                "NNDSS"
+            ],
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic"
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
@@ -47132,68 +47035,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kee5-23sr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kee5-23sr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kee5-23sr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kee5-23sr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kee5-23sr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kee5-23sr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kee5-23sr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kee5-23sr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kee5-23sr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "data.cdc.gov"
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
@@ -47201,60 +47108,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/keia-pvvn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/keia-pvvn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/keia-pvvn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/keia-pvvn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis"
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
-            "modified": "2025-01-31",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -47262,61 +47177,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ker6-gs6z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ker6-gs6z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ker6-gs6z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months -17 Years Who are Up to date with the COVID-19 Vaccines by Season, United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/kgid-f54m",
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
-                "name": "data.cdc.gov"
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
@@ -47324,39 +47243,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kgid-f54m",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/kgid-f54m",
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
+            "title": "Evaluation of A Passive Back-Support Exoskeleton during In-Bed Patient Handling Tasks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kh8y-3es6",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:15"
             ],
-            "issued": "2020-05-06",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "cares act",
-                "health system",
-                "provider relief fund"
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
-            "identifier": "https://data.cdc.gov/api/views/kh8y-3es6",
             "description": "HHS is providing support to healthcare providers fighting the coronavirus disease 2019 (COVID-19) pandemic through the bipartisan Coronavirus Aid, Relief, & Economic Security (CARES) Act; the Paycheck Protection Program and Health Care Enhancement Act (PPPHCEA); and the Coronavirus Response and Relief Supplemental Appropriations (CRRSA) Act, which provide a total of $178 billion for relief funds to hospitals and other healthcare providers on the front lines of the COVID-19 response. This funding supports healthcare-related expenses or lost revenue attributable to COVID-19 and ensures uninsured Americans can get treatment for COVID-19. HHS is distributing this Provider Relief Fund (PRF) money and these payments do not need to be repaid.\n\nThe Department allocated $50 billion in PRF payments for general distribution to Medicare facilities and providers impacted by COVID-19, based on eligible providers' net reimbursement. HHS has made other PRF distributions to a wide array of health care providers and more information on those distributions can be found here: https://www.hhs.gov/coronavirus/cares-act-provider-relief-fund/data/index.html",
-            "title": "HHS Provider Relief Fund",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47364,64 +47279,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kh8y-3es6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kh8y-3es6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kh8y-3es6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kh8y-3es6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/kh8y-3es6",
+            "issued": "2020-05-06",
+            "keyword": [
+                "cares act",
+                "health system",
+                "provider relief fund"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kh8y-3es6",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
+            "modified": "2025-01-17",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "HRSA"
+            },
+            "spatial": "US",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "HHS Provider Relief Fund"
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
-                "name": "CDC"
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
@@ -47429,66 +47343,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/khic-yj26/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/khic-yj26/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/khic-yj26/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/khic-yj26/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "CDC"
+            },
             "theme": [
                 "Foodborne, Waterborne, and Related Diseases"
-            ]
+            ],
+            "title": "BEAM Dashboard - Isolates by HHS Region"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/khjf-tq2k",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
-            "keyword": [
-                "2019",
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
-            "identifier": "https://data.cdc.gov/api/views/khjf-tq2k",
             "description": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1I. Cryptosporidiosis to Cyclosporiasis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47496,67 +47406,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/khjf-tq2k/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/khjf-tq2k/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/khjf-tq2k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/khjf-tq2k/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/khjf-tq2k/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/khjf-tq2k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/khjf-tq2k/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/khjf-tq2k/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/khjf-tq2k/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/khjf-tq2k",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "cryptosporidiosis",
+                "cyclosporiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/khjf-tq2k",
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
+            "title": "NNDSS - TABLE 1I. Cryptosporidiosis to Cyclosporiasis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kikd-77zw",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2017-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "keyword": [
-                "2016",
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
-            "identifier": "https://data.cdc.gov/api/views/kikd-77zw",
             "description": "NNDSS - Table II. Cryptosporidiosis to Dengue - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP:  Nationally notifiable but not published.  Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.   Data for TB are displayed in Table IV, which appears quarterly. \r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\u00a7 Includes data for dengue and dengue-like illness. Office of Management and Budget approval of the NNDSS Revision #0920-0728 on January 21, 2016, authorized CDC to receive data for these conditions. CDC is in the process of soliciting data for these conditions.",
-            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47564,74 +47471,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kikd-77zw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kikd-77zw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kikd-77zw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kikd-77zw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kikd-77zw",
+            "issued": "2017-01-05",
+            "keyword": [
+                "2016",
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
+            "landingPage": "https://data.cdc.gov/d/kikd-77zw",
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
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue"
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
-                "ncird-corvd",
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
-                "name": "CDC"
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
@@ -47639,62 +47539,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kipu-qxy8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kipu-qxy8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kipu-qxy8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kipu-qxy8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kipu-qxy8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kipu-qxy8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kipu-qxy8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kipu-qxy8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kipu-qxy8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "ncird-corvd",
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
+                "name": "CDC"
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
-            "landingPage": "https://www.cdc.gov/nchs/covid19/namcs.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-15/2022-05-06",
-            "modified": "2023-01-12",
-            "keyword": [
-                "covid-19",
-                "physicians"
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
-            "identifier": "https://data.cdc.gov/api/views/kk8c-wtm4",
             "description": "The National Ambulatory Medical Care Survey (NAMCS), conducted by the National Center for Health Statistics (NCHS), collects data on visits to physician offices to describe patterns of ambulatory care delivery in the United States. As part of NAMCS, the Physician Induction Interview collects information about practice characteristics at physician offices. Partway through the 2020 NAMCS, NCHS added questions to the Physician Induction Interview to assess physician experiences related to COVID-19 in office-based settings.\n\nThe data include nationally representative estimates of experiences related to COVID-19 among office-based physicians in the United States, including: shortages of personal protective equipment (PPE) in the past 3 months; the ability to test for COVID-19 in the past 3 months; providers testing positive for COVID-19 in the past 3 months; turning away COVID-19 patients in the past 3 months; and telemedicine or telehealth technology use before and after March 2020.  Estimates were derived from interviews with physicians in periods 3 and 4 of 2020 NAMCS and periods 1 through 4 of 2021 NAMCS, which occurred between December 15, 2020 and May 6, 2022.  The data are considered preliminary, and the results may change with the final data release.",
-            "title": "Physician Experiences Related to COVID-19 from the National Ambulatory Medical Care Survey",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47702,72 +47617,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kk8c-wtm4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kk8c-wtm4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kk8c-wtm4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kk8c-wtm4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kk8c-wtm4",
+            "issued": "2021-10-18",
+            "keyword": [
+                "covid-19",
+                "physicians"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/namcs.htm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-01-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2020-12-15/2022-05-06",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Physician Experiences Related to COVID-19 from the National Ambulatory Medical Care Survey"
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
-                "name": "data.cdc.gov"
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
@@ -47775,55 +47683,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kkix-nh4v/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kkix-nh4v/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kkix-nh4v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kkix-nh4v/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kkix-nh4v/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kkix-nh4v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kkix-nh4v/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kkix-nh4v/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kkix-nh4v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/kkvj-587h",
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
-                "name": "data.cdc.gov"
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
@@ -47831,51 +47750,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kkvj-587h",
+            "issued": "2024-12-27",
+            "landingPage": "https://data.cdc.gov/d/kkvj-587h",
+            "modified": "2024-12-27",
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
+            "title": "Effects of inhaled tier-2 diesel engine exhaust on immunotoxicity in a rat model:  A hazard identification study. Part III. Immunotoxicology"
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
-                "name": "CDC"
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
@@ -47883,79 +47786,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/km4m-vcsb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/km4m-vcsb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/km4m-vcsb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/km4m-vcsb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/km4m-vcsb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/km4m-vcsb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/km4m-vcsb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/km4m-vcsb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/km4m-vcsb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "CDC"
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
-                "sdoh-access-to-health-care",
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
-            "identifier": "https://data.cdc.gov/api/views/km5s-4339",
             "description": "Data on Medicaid coverage among persons under age 65 by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health Interview Survey, health insurance supplements (1984, 1989, 1994-1996). Starting with 1997, data are from the family core and the sample adult questionnaires. Data for level of difficulty are from the 2010 Quality of Life, 2011-2017 Functioning and Disability, and 2018 Sample Adult questionnaires. For more information on the National Health Interview Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
-            "title": "Medicaid coverage among persons under age 65, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47963,70 +47862,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/km5s-4339/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/km5s-4339/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/km5s-4339/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/km5s-4339/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/km5s-4339/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/km5s-4339/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/km5s-4339/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/km5s-4339/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/km5s-4339/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "sdoh-access-to-health-care",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -48034,74 +47941,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kmap-fsfn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kmap-fsfn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kmap-fsfn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kmap-fsfn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kmap-fsfn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kmap-fsfn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kmap-fsfn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kmap-fsfn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kmap-fsfn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -48109,64 +48013,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kmvs-jkvx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kmvs-jkvx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kmvs-jkvx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kmvs-jkvx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kmvs-jkvx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kmvs-jkvx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kmvs-jkvx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kmvs-jkvx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kmvs-jkvx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "CORVD"
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
@@ -48174,124 +48084,120 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kmxt-xb3i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kmxt-xb3i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kmxt-xb3i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kmxt-xb3i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kmxt-xb3i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kmxt-xb3i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kmxt-xb3i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kmxt-xb3i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kmxt-xb3i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "mortality",
+                "ncird-corvd"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kmxt-xb3i",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-21",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CORVD"
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
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/deaths.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-            "issued": "2022-05-31",
-            "@type": "dcat:Dataset",
-            "temporal": "1950-2020",
-            "modified": "2023-03-27",
-            "references": [
-                "https://www.cdc.gov/nchs/nvss/deaths.htm"
-            ],
-            "keyword": [
-                "deaths",
-                "injury",
-                "mortality",
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
-            "identifier": "https://data.cdc.gov/api/views/kn6j-fsdu",
+            "describedBy": "All death certificate records issued by each state and independent jurisdiction each year",
             "description": "Data are based on information from all death certificates filed in the 50 states and the District of Columbia and processed by the National Center for Health Statistics (NCHS). Restricted data available through the Research Data Center include geographical indicators, exact date of birth and death of decedent, among others.",
-            "title": "Restricted mortality data from the National Vital Statistics System",
-            "isPartOf": "https://www.cdc.gov/nchs/nvss/deaths.htm",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "Data are based on information from all death certificates filed in the 50 states and the District of Columbia and processed by the National Center for Health Statistics (NCHS). Restricted data available through the Research Data Center include geographical indicators, exact date of birth and death of decedent, among others.",
                     "@type": "dcat:Distribution",
+                    "description": "Data are based on information from all death certificates filed in the 50 states and the District of Columbia and processed by the National Center for Health Statistics (NCHS). Restricted data available through the Research Data Center include geographical indicators, exact date of birth and death of decedent, among others.",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
                     "title": "Restricted mortality data from the National Vital Statistics System"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "All death certificate records issued by each state and independent jurisdiction each year",
+            "identifier": "https://data.cdc.gov/api/views/kn6j-fsdu",
+            "isPartOf": "https://www.cdc.gov/nchs/nvss/deaths.htm",
+            "issued": "2022-05-31",
+            "keyword": [
+                "deaths",
+                "injury",
+                "mortality",
+                "research-data-center"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/deaths.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-03-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "references": [
+                "https://www.cdc.gov/nchs/nvss/deaths.htm"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "spatial": "United States",
+            "temporal": "1950-2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Restricted mortality data from the National Vital Statistics System"
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
-                "sdoh-environmental",
-                "united states"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/kn79-hsxy",
             "description": "Effective June 28, 2023, this dataset will no longer be updated. Similar data are accessible from  CDC WONDER (https://wonder.cdc.gov/mcd-icd10-provisional.html)\n\nProvisional count of deaths involving COVID-19 by county of occurrence, in the United States, 2020-2023.",
-            "title": "Provisional COVID-19 Death Counts in the United States by County",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48299,67 +48205,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kn79-hsxy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kn79-hsxy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kn79-hsxy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kn79-hsxy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kn79-hsxy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kn79-hsxy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kn79-hsxy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kn79-hsxy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kn79-hsxy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "sdoh-environmental",
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
+                "name": "National Center for Health Statistics"
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
-            "identifier": "https://data.cdc.gov/api/views/knu9-e7pg",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Pa/knu9-e7pg",
             "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Patient and Cycle Characteristics dataset summarizes the types of ART services performed and the kinds of patients who received ART procedures in a specific clinic. Please note patient characteristics are presented per cycle rather than per patient. As a result, patients who had more than one ART cycle within the reporting year are represented more than once.",
-            "title": "2020 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48367,68 +48278,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/knu9-e7pg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/knu9-e7pg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/knu9-e7pg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/knu9-e7pg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Pa/knu9-e7pg",
+            "identifier": "https://data.cdc.gov/api/views/knu9-e7pg",
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
+            "title": "2020 Final Assisted Reproductive Technology (ART) Patient and Cycle Characteristics"
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
-                "name": "Environmental Public Health Tracking"
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
@@ -48436,66 +48343,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kp49-9dp8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kp49-9dp8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kp49-9dp8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kp49-9dp8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2024-01-30",
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
+            "title": "U.S. State and Territorial Orders Closing and Reopening Bars Issued from March 11, 2020 through May 31, 2021 by County by Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kpbd-vsd5",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/kpbd-vsd5",
             "description": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48503,73 +48411,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kpbd-vsd5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kpbd-vsd5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kpbd-vsd5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kpbd-vsd5",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "imported",
+                "indigenous",
+                "malaria",
+                "measles",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kpbd-vsd5",
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
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous"
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
                 "fn": "National Center for Health Statistics",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
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
@@ -48577,60 +48479,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/krhz-spsc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/krhz-spsc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/krhz-spsc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/krhz-spsc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/krhz-spsc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/krhz-spsc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/krhz-spsc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/krhz-spsc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/krhz-spsc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/krhz-spsc",
+            "issued": "2022-02-09",
+            "keyword": [
+                "ethnicity",
+                "nhis",
+                "race",
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
+            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-03-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/krkm-t59m",
-            "issued": "2015-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2015-11-17",
-            "keyword": [
-                "malaria"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Gimnig",
                 "hasEmail": "mailto:hzg1@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/krkm-t59m",
             "description": "This data set is from 3 surveys conducted in two districts in western Kenya following the scale up of insecticide treated nets and the implementation of IRS in one of the districts.",
-            "title": "PONE-D-15-23803",
-            "programCode": [
-                "009:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48638,40 +48554,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/krkm-t59m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/krkm-t59m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/krkm-t59m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/krkm-t59m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/krkm-t59m",
+            "issued": "2015-11-17",
+            "keyword": [
+                "malaria"
+            ],
+            "landingPage": "https://data.cdc.gov/d/krkm-t59m",
+            "modified": "2015-11-17",
+            "programCode": [
+                "009:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "PONE-D-15-23803"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PLACES Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
+            "description": "This dataset contains model-based place (incorporated and census-designated places) estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 36 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. More information about the methodology can be found at  www.cdc.gov/places.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/krqc-563j/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/krqc-563j/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/krqc-563j/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/krqc-563j",
+            "issued": "2024-07-15",
             "keyword": [
                 "behaviors",
                 "brfss",
@@ -48686,64 +48648,66 @@
                 "risk",
                 "status"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "PLACES Public Inquiries",
-                "hasEmail": "mailto:places@cdc.gov"
-            },
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "modified": "2024-07-15",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/krqc-563j",
-            "description": "This dataset contains model-based place (incorporated and census-designated places) estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 36 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. More information about the methodology can be found at  www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Place Data 2023 release",
-            "programCode": [
-                "009:020"
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "theme": [
+                "500 Cities & Places"
+            ],
+            "title": "PLACES: Local Data for Better Health, Place Data 2023 release"
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
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19, pneumonia, and influenza reported to NCHS by race, age, and jurisdiction of occurrence.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/ks3g-spdg/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/krqc-563j/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ks3g-spdg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ks3g-spdg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/krqc-563j/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ks3g-spdg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ks3g-spdg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/krqc-563j/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/krqc-563j/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ks3g-spdg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ks3g-spdg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
-            "theme": [
-                "500 Cities & Places"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/ks3g-spdg",
             "issued": "2020-05-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2023-07-29",
-            "modified": "2023-09-27",
             "keyword": [
                 "age",
                 "age group",
@@ -48763,165 +48727,186 @@
                 "state",
                 "united states"
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
-            "identifier": "https://data.cdc.gov/api/views/ks3g-spdg",
-            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19, pneumonia, and influenza reported to NCHS by race, age, and jurisdiction of occurrence.",
-            "title": "Provisional COVID-19 Deaths by Race and Hispanic Origin, and Age",
-            "programCode": [
-                "009:020"
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2020-01-01/2023-07-29",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "Provisional COVID-19 Deaths by Race and Hispanic Origin, and Age"
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
+            "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ks3g-spdg/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ks3g-spdg/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ks3g-spdg/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ksf9-pem2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ks3g-spdg/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ks3g-spdg/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ksf9-pem2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ks3g-spdg/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ks3g-spdg/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ksf9-pem2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.xml?accessType=DOWNLOAD",
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
-            "landingPage": "https://data.cdc.gov/d/ksf9-pem2",
-            "bureauCode": [
-                "009:00"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/ksf9-pem2",
             "issued": "2016-09-14",
-            "@type": "dcat:Dataset",
-            "modified": "2016-09-14",
             "keyword": [
                 "cdc",
                 "centers for disease control and prevention"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC INFO",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/ksf9-pem2",
+            "modified": "2016-09-14",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/ksf9-pem2",
-            "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
-            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 1 - Boston",
-            "programCode": [
-                "009:020"
+            "theme": [
+                "Motor Vehicle"
+            ],
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 1 - Boston"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Weekly",
+            "bureauCode": [
+                "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "description": "Weekly COVID-19 Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \u2022 Weekly estimates of COVID-19 vaccination coverage and intent among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/). \n\nWeekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ksf9-pem2/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ksfb-ug5d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ksf9-pem2/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ksfb-ug5d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ksf9-pem2/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ksfb-ug5d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "United States- National, Region, State",
+            "temporal": "2024-2025",
             "theme": [
-                "Motor Vehicle"
-            ]
+                "Vaccinations"
+            ],
+            "title": "Weekly Cumulative COVID-19 Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ktba-rcfx",
-            "issued": "2021-11-24",
             "@type": "dcat:Dataset",
-            "modified": "2022-01-19",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tim Turner",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
+            "description": "",
             "identifier": "https://data.cdc.gov/api/views/ktba-rcfx",
+            "issued": "2021-11-24",
+            "landingPage": "https://data.cdc.gov/d/ktba-rcfx",
+            "modified": "2022-01-19",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "description": "",
             "title": "Data Update Notice"
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -48929,61 +48914,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ku7p-zn4c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ku7p-zn4c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ku7p-zn4c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/kuas-t2xn",
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
-            "identifier": "https://data.cdc.gov/api/views/kuas-t2xn",
             "description": "Occupational exposure to 4,4\u2019-methylene diphenyl diisocyanate (MDI), the most widely used monomeric diisocyanate (dNCO), is associated with occupational asthma (OA) development. Recruitment of immune cells to the lung microenvironment via secreted chemokines by alveolar macrophages may play a role during asthma pathogenesis. Our prior study identified that alternatively activated (M2) macrophage-associated markers and chemokines were induced by MDI/MDI-Glutathione (GSH)-mediated Kr\u00fcppel-Like Factor 4 (KLF4) upregulation in macrophages and induced chemotaxis abilities to na\u00efve T-cells and eosinophils; however, the underlying molecular mechanism(s) by which MDI upregulated KLF4 expression is unclear. Previously, we identified that two microRNAs (miRs) including hsa-miR-206-3p and hsa-miR-381-3p were significantly downregulated in MDI-GSH-exposed THP-1 macrophages. In silico analysis revealed that one hsa-miR-206-3p and two hsa-miR-381-3p predicted binding sites exist on the 3\u2019 untranslated region (UTR) of KLF4 transcripts. We hypothesize that MDI/MDI-GSH exposure induces M2 macrophage-associated markers and chemokines through hsa-miR-206-3p/hsa-miR-381-3p mediated KLF4 upregulation in macrophages. The first aim of this study was to examine whether hsa-miR-206-3p/hsa-miR-381-3p regulates KLF4 expression in THP-1 macrophages through a posttranscriptional regulation mechanism. Our second aim was to determine whether hsa-miR-206-3p/hsa-miR-381-3p participates in KLF4-regulated M2 macrophage-associated markers and chemokines after MDI-exposure. After identifying the role of endogenous hsa-miR-206-3p/hsa-miR-381-3p in regulation of KLF4 transcription factor after MDI-exposure, we investigated the role of hsa-miR-206-3p/hsa-miR-381-3p in regulation of M2 macrophage-associated markers and chemokines\u2019 expressions in relation to the exposure to MDI.",
-            "title": "MicroRNA-Mediated Kr\u00fcppel-Like Factor 4 upregulation Induces Alternatively Activated Macrophage-Associated Markers and Chemokines Transcription in 4,4\u2019-Methylene Diphenyl Diisocyanate Exposed Macrophages",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48991,52 +48981,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kuas-t2xn",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/kuas-t2xn",
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
+            "title": "MicroRNA-Mediated Kr\u00fcppel-Like Factor 4 upregulation Induces Alternatively Activated Macrophage-Associated Markers and Chemokines Transcription in 4,4\u2019-Methylene Diphenyl Diisocyanate Exposed Macrophages"
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
@@ -49044,40 +49016,104 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kucs-wizg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kucs-wizg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kucs-wizg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kucs-wizg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kucs-wizg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kucs-wizg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kucs-wizg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kucs-wizg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kucs-wizg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://www.cdc.gov/resp-net/dashboard/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "RESP-NET",
+                "hasEmail": "mailto:CovidRSV-Net@cdc.gov"
+            },
+            "description": "The Respiratory Virus Hospitalization Surveillance Network (RESP-NET) is a network that conducts, active, population-based surveillance for laboratory confirmed hospitalizations associated with Influenza, COVID-19, and RSV. The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. Hospitalization rates show how many people in the surveillance area are hospitalized with influenza, COVID-19, and RSV compared to the total number of people residing in that area. \n\nData will be updated weekly. Data are preliminary and subject to change as more data become available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/kvib-3txy/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/kvib-3txy/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/kvib-3txy/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/kvib-3txy",
             "issued": "2024-05-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
             "keyword": [
                 "covid",
                 "covid19",
@@ -49104,99 +49140,53 @@
                 "rsv",
                 "surveillance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "RESP-NET",
-                "hasEmail": "mailto:CovidRSV-Net@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/kvib-3txy",
-            "description": "The Respiratory Virus Hospitalization Surveillance Network (RESP-NET) is a network that conducts, active, population-based surveillance for laboratory confirmed hospitalizations associated with Influenza, COVID-19, and RSV. The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. Hospitalization rates show how many people in the surveillance area are hospitalized with influenza, COVID-19, and RSV compared to the total number of people residing in that area. \n\nData will be updated weekly. Data are preliminary and subject to change as more data become available.",
-            "title": "Rates of Laboratory-Confirmed RSV, COVID-19, and Flu Hospitalizations from the RESP-NET Surveillance Systems",
+            "landingPage": "https://www.cdc.gov/resp-net/dashboard/index.html",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-31",
             "programCode": [
                 "009:038"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/kvib-3txy/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/kvib-3txy/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kvib-3txy/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/kvib-3txy/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
             "spatial": "RESP-NET Sites",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Weekly",
             "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Rates of Laboratory-Confirmed RSV, COVID-19, and Flu Hospitalizations from the RESP-NET Surveillance Systems"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kvms-atr7",
-            "issued": "2022-10-27",
             "@type": "dcat:Dataset",
-            "modified": "2022-11-10",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCIRD-CORVD",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
+            "description": "As of 11/10/2022, this dataset will continue to incorporate historical updates made to case and percent positivity data; however, community transmission level will only be published in the corresponding Weekly COVID-19 County Level of Community Transmission as Originally Posted dataset.",
             "identifier": "https://data.cdc.gov/api/views/kvms-atr7",
+            "issued": "2022-10-27",
+            "landingPage": "https://data.cdc.gov/d/kvms-atr7",
+            "modified": "2022-11-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "description": "As of 11/10/2022, this dataset will continue to incorporate historical updates made to case and percent positivity data; however, community transmission level will only be published in the corresponding Weekly COVID-19 County Level of Community Transmission as Originally Posted dataset.",
             "title": "Dataset Update"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/kw6u-z8u2",
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
-            "identifier": "https://data.cdc.gov/api/views/kw6u-z8u2",
             "description": "This dataset contains all state and territorial vaccine mandates that were issued from July 26, 2021 to ____, regardless of whether the law has been superseded by a subsequent law, postponed by subsequent law, or otherwise modified. State and territorial laws are collected from publicly available government websites and cataloged and coded using HHS Protect by one coder with one or more additional coders conducting quality assurance. \nData were collected to determine when certain groups were subject to vaccine mandates. Data can be used to determine when states announced and required different groups to be vaccinated. \nThese data are derived from publicly available state and territorial laws and official policy documents found by CDC\u2019s COVID-19 Mitigation Policy Analysis Unit, and CDC\u2019s Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from July 26, 2021 through _____. These data will be updated as new laws are collected. Any orders not available through publicly accessible websites are not included in this dataset. Recommendations not included in a law are not included in these data. Effective and expiration dates were coded using only the date provided in the law. These data do not necessarily represent the official position of the Centers for Disease Control and Prevention.",
-            "title": "State-Level Vaccine Mandates - All",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49204,63 +49194,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kw6u-z8u2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kw6u-z8u2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kw6u-z8u2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kw6u-z8u2",
+            "issued": "2022-03-23",
+            "landingPage": "https://data.cdc.gov/d/kw6u-z8u2",
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
+            "title": "State-Level Vaccine Mandates - All"
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
-                "state system",
-                "tax"
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
-            "identifier": "https://data.cdc.gov/api/views/kwbr-syv2",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Tax/kwbr-syv2",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  E-Cigarette Legislation\u2014Tax. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include state excise taxes on e-cigarettes and tax stamps.",
-            "title": "CDC STATE System E-Cigarette Legislation - Tax",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49268,67 +49251,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kwbr-syv2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kwbr-syv2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kwbr-syv2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Tax/kwbr-syv2",
+            "identifier": "https://data.cdc.gov/api/views/kwbr-syv2",
+            "issued": "2023-07-18",
+            "keyword": [
+                "e-cigarette",
+                "legislation",
+                "osh",
+                "policy",
+                "state system",
+                "tax"
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
+            "title": "CDC STATE System E-Cigarette Legislation - Tax"
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
-                "name": "data.cdc.gov"
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
@@ -49336,64 +49316,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kx9y-asbg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kx9y-asbg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kx9y-asbg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kx9y-asbg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kx9y-asbg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kx9y-asbg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kx9y-asbg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kx9y-asbg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kx9y-asbg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chancroid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/kxvg-q6s7",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/kxvg-q6s7",
             "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49401,65 +49382,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kxvg-q6s7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kxvg-q6s7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kxvg-q6s7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/kxvg-q6s7",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a virus infections",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/kxvg-q6s7",
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
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
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
-                "name": "data.cdc.gov"
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
@@ -49467,60 +49447,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kyph-4i8d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kyph-4i8d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kyph-4i8d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/kyph-4i8d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kyph-4i8d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kyph-4i8d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/kyph-4i8d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/kyph-4i8d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/kyph-4i8d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable"
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
-                "500cities",
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
@@ -49528,61 +49514,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m35w-spkz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m35w-spkz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m35w-spkz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/m35w-spkz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m35w-spkz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m35w-spkz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m35w-spkz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m35w-spkz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m35w-spkz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/500-Cities-Places/PLACES-and-500-Cities-Data-Dictionary/m35w-spkz",
+            "identifier": "https://data.cdc.gov/api/views/m35w-spkz",
+            "issued": "2024-08-26",
+            "keyword": [
+                "500cities",
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
-                "name": "data.cdc.gov"
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
@@ -49590,64 +49576,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m4es-3af4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m4es-3af4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m4es-3af4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/m4es-3af4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m4es-3af4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m4es-3af4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m4es-3af4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m4es-3af4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m4es-3af4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/m4es-3af4",
+            "issued": "2013-07-29",
+            "keyword": [
+                "hus",
+                "low birthweight"
+            ],
+            "landingPage": "https://data.cdc.gov/d/m4es-3af4",
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
+            "title": "Selected Trend Table from Health, United States, 2011. Low birthweight live births, by race and Hispanic origin of mother, and state: United States, 2000 - 2002, 2003 - 2005, and 2006 - 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/m5zs-rf6r",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/m5zs-rf6r",
             "description": "NNDSS - Table II. West Nile virus disease - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Updated weekly from the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance). Data for Jamestown Canyon virus, La Crosse virus, Chikungunya virus, Eastern equine encephalitis virus, Powassan virus, St. Louis virus, and Western equine encephalitis virus diseases are available in Table I. \r\n\r\n\u00b6 Not reportable in all states. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.",
-            "title": "NNDSS - Table II. West Nile virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49655,67 +49636,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m5zs-rf6r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m5zs-rf6r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m5zs-rf6r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/m5zs-rf6r",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "west nile virus",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/m5zs-rf6r",
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
+            "title": "NNDSS - Table II. West Nile virus disease"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/m6gf-vfkz",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
-            "keyword": [
-                "2018",
-                "all serotypes)",
-                "giardiasis",
-                "gonorrhea",
-                "haemophilus influenza",
-                "invasive disease (all ages",
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
-            "identifier": "https://data.cdc.gov/api/views/m6gf-vfkz",
             "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49723,40 +49701,98 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m6gf-vfkz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m6gf-vfkz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m6gf-vfkz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/m6gf-vfkz",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "all serotypes)",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenza",
+                "invasive disease (all ages",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/m6gf-vfkz",
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
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "description": "Weekly data on the number of deaths from all causes by sex, age group, and race/Hispanic origin group for the United States. Counts of deaths in more recent weeks can be compared with counts from earlier years (2015-2019) to determine if the number is higher than expected.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m74n-4hbs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/m74n-4hbs/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/m74n-4hbs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/m74n-4hbs/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/m74n-4hbs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/m74n-4hbs/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/m74n-4hbs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/m74n-4hbs",
             "issued": "2020-11-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-26",
             "keyword": [
                 "age",
                 "age group",
@@ -49775,66 +49811,65 @@
                 "united states",
                 "weekly"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-04-26",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/m74n-4hbs",
-            "description": "Weekly data on the number of deaths from all causes by sex, age group, and race/Hispanic origin group for the United States. Counts of deaths in more recent weeks can be compared with counts from earlier years (2015-2019) to determine if the number is higher than expected.",
-            "title": "AH Excess Deaths by Sex, Age, and Race and Hispanic Origin",
-            "programCode": [
-                "009:020"
+            "spatial": "United States",
+            "theme": [
+                "NCHS"
+            ],
+            "title": "AH Excess Deaths by Sex, Age, and Race and Hispanic Origin"
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
+            "description": "Data on infant, neonatal, and postneonatal mortality rates in the United States, by detailed race and Hispanic origin of mother. Data are from Health, United States. Source: National Center for Health Statistics, National Vital Statistics System, Linked Birth/Infant Death Data Set.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/m74n-4hbs/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m74n-4hbs/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/m74n-4hbs/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/m7w3-utaq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/m74n-4hbs/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/m74n-4hbs/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/m7w3-utaq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m74n-4hbs/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/m74n-4hbs/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/m7w3-utaq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.xml?accessType=DOWNLOAD",
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
-            "landingPage": "https://www.cdc.gov/nchs/hus",
-            "bureauCode": [
-                "009:20"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/m7w3-utaq",
             "issued": "2024-08-05",
-            "temporal": "1983/2021",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-08",
             "keyword": [
                 "american indian and alaska native",
                 "asian",
@@ -49863,89 +49898,34 @@
                 "single race",
                 "white"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:healthus@cdc.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/m7w3-utaq",
-            "description": "Data on infant, neonatal, and postneonatal mortality rates in the United States, by detailed race and Hispanic origin of mother. Data are from Health, United States. Source: National Center for Health Statistics, National Vital Statistics System, Linked Birth/Infant Death Data Set.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Infant, neonatal, and postneonatal mortality rates, by detailed race and Hispanic origin of mother: United States",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-08",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/m7w3-utaq/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/m7w3-utaq/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/m7w3-utaq/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "temporal": "1983/2021",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "DQS Infant, neonatal, and postneonatal mortality rates, by detailed race and Hispanic origin of mother: United States"
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
-                "name": "data.cdc.gov"
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
@@ -49953,45 +49933,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m8jv-u92i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m8jv-u92i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m8jv-u92i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/m8jv-u92i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m8jv-u92i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m8jv-u92i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/m8jv-u92i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/m8jv-u92i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/m8jv-u92i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "describedBy": "Match status can be found in the match rate tables (see Tables 1 and 2 on page 10) here: https://www.cdc.gov/nchs/data/datalinkage/2019NDI-Linkage-Methods-and-Analytic-Considerations-508.pdf",
+            "describedByType": "application/pdf",
+            "description": "NCHS has linked data from various surveys with death certificate records from the National Death Index (NDI). Linkage of the NCHS survey participant data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality. The Linked Mortality Files (LMF) have been updated with mortality follow-up data through December 31, 2019.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/m97v-d4fn",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-08",
             "keyword": [
                 "linked mortality files",
                 "nchs surveys",
@@ -50017,74 +50029,39 @@
                 "sdoh-use-of-health-care",
                 "sdoh-workplace"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCHS Data Linkage Program",
-                "hasEmail": "mailto:DataLinkage@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/mortality-restricted.htm",
+            "modified": "2024-10-11",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/m97v-d4fn",
-            "description": "NCHS has linked data from various surveys with death certificate records from the National Death Index (NDI). Linkage of the NCHS survey participant data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality. The Linked Mortality Files (LMF) have been updated with mortality follow-up data through December 31, 2019.",
-            "title": "NCHS Survey Data Linked to National Death Index (NDI) Mortality Files",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/LMF2019-DataDictionary-MortVars.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables (see Tables 1 and 2 on page 10) here: https://www.cdc.gov/nchs/data/datalinkage/2019NDI-Linkage-Methods-and-Analytic-Considerations-508.pdf",
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
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2020/2021",
-            "modified": "2022-03-28",
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
-            "identifier": "https://data.cdc.gov/api/views/mawz-airi",
             "description": "Provisional deaths involving coronavirus disease 2019 (COVID-19) reported to NCHS by age group among United States residents, from MMWR Week 40 2020 through MMWR Week 39 2021.\n\nAge groups: 0-4, 5-11, 12-15, 16-17, 18-24, 25-39, 40-49, 50-64, 65-74, and 75+ years",
-            "title": "AH Provisional COVID-19 Deaths by Age, United States, Week 40 2020 through Week 39 2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50092,73 +50069,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mawz-airi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mawz-airi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mawz-airi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mawz-airi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/mawz-airi",
+            "issued": "2021-10-06",
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
+            "spatial": "United States",
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
@@ -50166,45 +50142,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mb5y-ytti/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mb5y-ytti/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mb5y-ytti/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mb5y-ytti/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mb5y-ytti/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mb5y-ytti/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mb5y-ytti/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mb5y-ytti/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mb5y-ytti/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/mbd7-r32t",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC-INFO",
+                "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
+            },
+            "describedBy": "https://data.cdc.gov/api/views/mbd7-r32t/files/4697b7f1-c0ea-403a-9583-6a02fd33a21c?download=true&filename=data_dictionary_covid_cases_restricted_detailed_updated.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated. \n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance publicly available dataset has 33 elements for all COVID-19 cases shared with CDC and includes demographics, geography (county and state of residence), any exposure history, disease severity indicators and outcomes, and presence of any underlying medical conditions and risk behaviors. This dataset requires a registration process and a data use agreement.\n\n<h4><b>CDC has three COVID-19 case surveillance datasets:</b></h4><ul><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">COVID-19 Case Surveillance Public Use Data with Geography</a>: Public use, patient-level dataset with clinical data (including symptoms), demographics, and county and state of residence. (19 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">COVID-19 Case Surveillance Public Use Data</a>: Public use, patient-level dataset with clinical and symptom data and demographics, with no geographic data. (12 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">COVID-19 Case Surveillance Restricted Access Detailed Data</a>: Restricted access, patient-level dataset with clinical and symptom data, demographics, and state and county of residence. Access requires a registration process and a data use agreement. (33 data elements)</li></ul>\n\n<b>Requesting Access to the COVID-19 Case Surveillance Restricted Access Detailed Data</b>\nPlease review the following documents to determine your interest in accessing the COVID-19 Case Surveillance Restricted Access Detailed Data file:\n1) <a href=\"https://data.cdc.gov/api/views/mbd7-r32t/files/9aad836e-5aa5-4047-aa5c-15996becc87c?download=true&filename=summary_guidance_and_limitations_information_and_restricted_access_data_use_agreement_information_updated.pdf\"> CDC COVID-19 Case Surveillance Restricted Access Detailed Data: Summary, Guidance, Limitations Information, and Restricted Access Data Use Agreement Information</a>\n\n2) <a href=\"https://data.cdc.gov/api/views/mbd7-r32t/files/4697b7f1-c0ea-403a-9583-6a02fd33a21c?download=true&filename=data_dictionary_covid_cases_restricted_detailed_updated.xlsx\"> Data Dictionary for the COVID-19 Case Surveillance Restricted Access Detailed Data</a>\n\nThe next step is to complete the Registration Information and Data Use Restrictions Agreement (<a href=\"https://app.smartsheetgov.com/b/form/20e9cf9b42d04a92a67585043cf34fbe\">RIDURA</a>). Once complete, CDC will review your agreement. After access is granted, Ask SRRG (<a href=\"mailto:eocevent394@cdc.gov\">eocevent394@cdc.gov</a>) will email you information about how to access the data through GitHub. If you have questions about obtaining access, email <a href=\"mailto:eocevent394@cdc.gov\">eocevent394@cdc.gov</a>. \n\n<h4><b>Overview</b></h4>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and autonomous reporting entities, including New York City and the District of Columbia (D.C.), as well as U.S. territories and affili",
+            "identifier": "https://data.cdc.gov/api/views/mbd7-r32t",
             "issued": "2020-05-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-01-01/2024-06-21",
-            "modified": "2025-01-13",
-            "references": [
-                "https://data.cdc.gov/api/views/mbd7-r32t/files/53195382-2916-4a7a-b97f-010111f3aaa1?download=true&filename=public%2033%20utility%20summary.pdf"
-            ],
             "keyword": [
                 "cases",
                 "coronavirus",
@@ -50215,64 +50221,38 @@
                 "restricted",
                 "surveillance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "CDC-INFO",
-                "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
-            },
+            "landingPage": "https://data.cdc.gov/d/mbd7-r32t",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CDC"
             },
-            "identifier": "https://data.cdc.gov/api/views/mbd7-r32t",
-            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated. \n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance publicly available dataset has 33 elements for all COVID-19 cases shared with CDC and includes demographics, geography (county and state of residence), any exposure history, disease severity indicators and outcomes, and presence of any underlying medical conditions and risk behaviors. This dataset requires a registration process and a data use agreement.\n\n<h4><b>CDC has three COVID-19 case surveillance datasets:</b></h4><ul><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">COVID-19 Case Surveillance Public Use Data with Geography</a>: Public use, patient-level dataset with clinical data (including symptoms), demographics, and county and state of residence. (19 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">COVID-19 Case Surveillance Public Use Data</a>: Public use, patient-level dataset with clinical and symptom data and demographics, with no geographic data. (12 data elements)</li><li><a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">COVID-19 Case Surveillance Restricted Access Detailed Data</a>: Restricted access, patient-level dataset with clinical and symptom data, demographics, and state and county of residence. Access requires a registration process and a data use agreement. (33 data elements)</li></ul>\n\n<b>Requesting Access to the COVID-19 Case Surveillance Restricted Access Detailed Data</b>\nPlease review the following documents to determine your interest in accessing the COVID-19 Case Surveillance Restricted Access Detailed Data file:\n1) <a href=\"https://data.cdc.gov/api/views/mbd7-r32t/files/9aad836e-5aa5-4047-aa5c-15996becc87c?download=true&filename=summary_guidance_and_limitations_information_and_restricted_access_data_use_agreement_information_updated.pdf\"> CDC COVID-19 Case Surveillance Restricted Access Detailed Data: Summary, Guidance, Limitations Information, and Restricted Access Data Use Agreement Information</a>\n\n2) <a href=\"https://data.cdc.gov/api/views/mbd7-r32t/files/4697b7f1-c0ea-403a-9583-6a02fd33a21c?download=true&filename=data_dictionary_covid_cases_restricted_detailed_updated.xlsx\"> Data Dictionary for the COVID-19 Case Surveillance Restricted Access Detailed Data</a>\n\nThe next step is to complete the Registration Information and Data Use Restrictions Agreement (<a href=\"https://app.smartsheetgov.com/b/form/20e9cf9b42d04a92a67585043cf34fbe\">RIDURA</a>). Once complete, CDC will review your agreement. After access is granted, Ask SRRG (<a href=\"mailto:eocevent394@cdc.gov\">eocevent394@cdc.gov</a>) will email you information about how to access the data through GitHub. If you have questions about obtaining access, email <a href=\"mailto:eocevent394@cdc.gov\">eocevent394@cdc.gov</a>. \n\n<h4><b>Overview</b></h4>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and autonomous reporting entities, including New York City and the District of Columbia (D.C.), as well as U.S. territories and affili",
-            "title": "COVID-19 Case Surveillance Restricted Access Detailed Data",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "009:020"
+            "references": [
+                "https://data.cdc.gov/api/views/mbd7-r32t/files/53195382-2916-4a7a-b97f-010111f3aaa1?download=true&filename=public%2033%20utility%20summary.pdf"
             ],
             "spatial": "US",
-            "describedBy": "https://data.cdc.gov/api/views/mbd7-r32t/files/4697b7f1-c0ea-403a-9583-6a02fd33a21c?download=true&filename=data_dictionary_covid_cases_restricted_detailed_updated.xlsx",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "temporal": "2020-01-01/2024-06-21",
             "theme": [
                 "Case Surveillance"
-            ]
+            ],
+            "title": "COVID-19 Case Surveillance Restricted Access Detailed Data"
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
-                "name": "data.cdc.gov"
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
@@ -50280,62 +50260,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mbsb-z5f8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mbsb-z5f8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mbsb-z5f8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mbsb-z5f8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Invasive Pneumococcal Diseases, All Ages"
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
-                "name": "National Center for Health Statistics"
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
@@ -50343,71 +50327,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mc4y-cbbv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mc4y-cbbv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mc4y-cbbv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-                "name": "data.cdc.gov"
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
@@ -50415,55 +50395,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mcdp-77g7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mcdp-77g7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mcdp-77g7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mcdp-77g7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mcdp-77g7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mcdp-77g7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mcdp-77g7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mcdp-77g7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mcdp-77g7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1AA. Poliovirus infection, nonparalytic to Psittacosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/mhj9-4wi2",
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
@@ -50471,44 +50461,34 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mhj9-4wi2",
+            "issued": "2016-11-30",
+            "landingPage": "https://data.cdc.gov/d/mhj9-4wi2",
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
-                "name": "data.cdc.gov"
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
@@ -50516,64 +50496,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mi28-ze7h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mi28-ze7h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mi28-ze7h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human"
         },
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
-                "name": "data.cdc.gov"
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
@@ -50581,45 +50562,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mik5-by93/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mik5-by93/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mik5-by93/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mik5-by93/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mik5-by93/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mik5-by93/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mik5-by93/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mik5-by93/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mik5-by93/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1JJ. Tularemia to  Vancomycin-intermediate Staphylococcus aureus"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/cms_medicare_linked_data_match_rate_tables_1.pdf",
+            "describedByType": "application/pdf",
+            "description": "NCHS has linked data from various surveys with Medicare program enrollment and health care utilization and expenditure data from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicare data provides the opportunity to study changes in health status, health care utilization and costs, and prescription drug use among Medicare enrollees. Medicare is the federal health insurance program for people who are 65 or older, certain younger people with disabilities, and people with End-Stage Renal Disease.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mjpe-bnz8",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2022-06-16",
             "keyword": [
                 "linked medicare files",
                 "nchs surveys",
@@ -50645,69 +50657,38 @@
                 "sdoh-use-of-health-care",
                 "sdoh-workplace"
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
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/mjpe-bnz8",
-            "description": "NCHS has linked data from various surveys with Medicare program enrollment and health care utilization and expenditure data from the Centers for Medicare & Medicaid Services (CMS). Linkage of the NCHS survey participants with the CMS Medicare data provides the opportunity to study changes in health status, health care utilization and costs, and prescription drug use among Medicare enrollees. Medicare is the federal health insurance program for people who are 65 or older, certain younger people with disabilities, and people with End-Stage Renal Disease.",
-            "title": "NCHS Survey Data Linked to Centers for Medicare & Medicaid Services (CMS) Medicare Data Files",
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
+                "https://www.cdc.gov/nchs/data-linkage/cms/nchs-cms_medicare14_18_linked_data-list_of_variables.pdf"
             ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/cms_medicare_linked_data_match_rate_tables_1.pdf",
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
-                "name": "data.cdc.gov"
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
@@ -50715,66 +50696,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mk6z-83q2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mk6z-83q2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mk6z-83q2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mk6z-83q2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mk6z-83q2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mk6z-83q2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mk6z-83q2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mk6z-83q2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mk6z-83q2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Invasive pneumococcal disease, age <5"
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
-                "name": "data.cdc.gov"
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
@@ -50782,55 +50761,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mkns-9vjv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mkns-9vjv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mkns-9vjv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mkns-9vjv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/mkyn-icix",
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
-                "name": "data.cdc.gov"
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
@@ -50838,40 +50828,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mkyn-icix",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/mkyn-icix",
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
+            "title": "Economic Burden of Occupational Fatal Injuries in the United States Based on the Census of Fatal Occupational Injuries, 2003-2010"
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
-                "name": "data.cdc.gov"
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
@@ -50879,56 +50863,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mmi4-8ajr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mmi4-8ajr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mmi4-8ajr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2015-08-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
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
-                "name": "National Center for Health Statistics"
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
@@ -50936,48 +50926,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mnaa-qctp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mnaa-qctp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mnaa-qctp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mnaa-qctp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
+            "describedBy": "All registered fetal deaths occurring to residents of the United States for a given year",
+            "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/mny7-y385",
+            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "issued": "2022-12-22",
-            "@type": "dcat:Dataset",
-            "temporal": "1982/2020",
-            "modified": "2023-04-14",
             "keyword": [
                 "county",
                 "date of delivery",
@@ -50991,61 +51007,35 @@
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
-            "identifier": "https://data.cdc.gov/api/views/mny7-y385",
-            "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
-            "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery",
-            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
-                    "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
-                    "@type": "dcat:Distribution",
-                    "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery"
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
             "spatial": "50 states and District of Columbia, all counties and cities with a population of 100,000 or greater",
-            "describedBy": "All registered fetal deaths occurring to residents of the United States for a given year",
+            "temporal": "1982/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/mpb9-a9up",
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
-            "identifier": "https://data.cdc.gov/api/views/mpb9-a9up",
             "description": "This study investigated the inhalation toxicity of the emissions from 3-D printing with acrylonitrile butadiene styrene (ABS) filament using an air-liquid interface (ALI) in vitro model. Primary normal human-derived bronchial epithelial cells (NHBEs) were exposed to ABS filament emissions in an ALI for 4 h. The mean and mode diameters of ABS emitted particles in the medium were 175 \u00b1 24 nm and 153 \u00b1 15 nm, respectively. The average particle deposition per surface area of the epithelium was 2.29 \u00d7 107 \u00b1 1.47 \u00d7 107 particle/cm2, equivalent to an estimated average particle mass of 0.144 \u00b1 0.042 \u00b5g/cm2.",
-            "title": "Evaluation of pulmonary effects of 3-D printer emissions from acrylonitrile butadiene styrene using an air-liquid interface model of primary normal human-derived bronchial epithelial cells",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51053,45 +51043,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mpb9-a9up",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/mpb9-a9up",
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
+            "title": "Evaluation of pulmonary effects of 3-D printer emissions from acrylonitrile butadiene styrene using an air-liquid interface model of primary normal human-derived bronchial epithelial cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mpdg-hf57",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-07",
-            "keyword": [
-                "2015",
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
-            "identifier": "https://data.cdc.gov/api/views/mpdg-hf57",
             "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Data for H. influenzae (age <5 years for serotype b, nonserotype b, and unknown serotype) are available in Table I.",
-            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51099,77 +51078,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mpdg-hf57/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mpdg-hf57/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mpdg-hf57/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mpdg-hf57",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mpdg-hf57",
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
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza"
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
-                "name": "CDC"
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
@@ -51177,77 +51148,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mpgq-jmmr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mpgq-jmmr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mpgq-jmmr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "CDC"
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
-            "landingPage": "https://data.cdc.gov/d/mpx5-t7tu",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-03-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-12-29/2023-07-29",
-            "modified": "2025-01-30",
-            "keyword": [
-                "coronavirus",
-                "covid-19",
-                "death rate",
-                "deaths",
-                "hhs region",
-                "mortality",
-                "nchs",
-                "nvss",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mpx5-t7tu",
             "description": "This file contains COVID-19 death counts, death rates, and percent of total deaths by jurisdiction of residence. The data is grouped by different time periods including 3-month period, weekly, and total (cumulative since January 1, 2020). United States death counts and rates include the 50 states, plus the District of Columbia and New York City. New York state estimates exclude New York City. Puerto Rico is included in HHS Region 2 estimates.\n\nDeaths with confirmed or presumed COVID-19, coded to ICD\u201310 code U07.1. Number of deaths reported in this file are the total number of COVID-19 deaths received and coded as of the date of analysis and may not represent all deaths that occurred in that period. Counts of deaths occurring before or after the reporting period are not included in the file.\n\nData during recent periods are incomplete because of the lag in time between when the death occurred and when the death certificate is completed, submitted to NCHS and processed for reporting purposes. This delay can range from 1 week to 8 weeks or more, depending on the jurisdiction and cause of death.\n\nDeath counts should not be compared across states. Data timeliness varies by state. Some states report deaths on a daily basis, while other states report deaths weekly or monthly. \n\nThe ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City, Puerto Rico; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.\n\nRates were calculated using the population estimates for 2021, which are estimated as of July 1, 2021 based on the Blended Base produced by the US Census Bureau in lieu of the April 1, 2020 decennial population count. The Blended Base consists of the blend of Vintage 2020 postcensal population estimates, 2020 Demographic Analysis Estimates, and 2020 Census PL 94-171 Redistricting File (see https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2020-2021/methods-statement-v2021.pdf).\n\nRates are based on deaths occurring in the specified week/month and are age-adjusted to the 2000 standard population using the direct method (see https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-08-508.pdf). These rates differ from annual age-adjusted rates, typically presented in NCHS publications based on a full year of data and annualized weekly/monthly age-adjusted rates which have been adjusted to allow comparison with annual rates.  Annualization rates presents deaths per year per 100,000 population that would be expected in a year if the observed period specific (weekly/monthly) rate prevailed for a full year.\n\nSub-national death counts between 1-9 are suppressed in accordance with NCHS data confidentiality standards. Rates based on death counts less than 20 are suppressed in accordance with NCHS standards of reliability as specified in NCHS Data Presentation Standards for Proportions (available from: https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf.).",
-            "title": "Provisional COVID-19 death counts, rates, and percent of total deaths, by jurisdiction of residence",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51255,73 +51232,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mpx5-t7tu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mpx5-t7tu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mpx5-t7tu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mpx5-t7tu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/mpx5-t7tu",
+            "issued": "2023-03-31",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "death rate",
+                "deaths",
+                "hhs region",
+                "mortality",
+                "nchs",
+                "nvss",
+                "puerto rico",
+                "state",
+                "united states"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mpx5-t7tu",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2019-12-29/2023-07-29",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional COVID-19 death counts, rates, and percent of total deaths, by jurisdiction of residence"
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
-            "temporal": "2015-01-04/2021-07-03",
-            "modified": "2023-11-16",
-            "keyword": [
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "hospital referral region",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "sdoh-access-to-health-care",
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
-            "identifier": "https://data.cdc.gov/api/views/mqmc-4b9n",
             "description": "Provisional count of deaths involving coronavirus disease 2019 (COVID-19) in the United States by week of death and by hospital referral region (HRR). HRR is determined by county of occurrence. Weekly weighted counts of deaths from all causes and due to COVID-19 are provided by HRR overall and for decedents 65 years and older. The weighted counts by HRRs are based on published methods for aggregating county-level data to HRRs. More detail about aggregating to HRRs from counties can be found in the following: https://github.com/Dartmouth-DAC/covid-19-hrr-mapping\nhttps://dartmouthatlas.org/covid-19/hrr-mapping/",
-            "title": "AH Provisional COVID-19 Deaths by Hospital Referral Region",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51329,70 +51305,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mqmc-4b9n/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mqmc-4b9n/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mqmc-4b9n/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/mqmc-4b9n",
+            "issued": "2021-05-12",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hospital referral region",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "sdoh-access-to-health-care",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-11-16",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2015-01-04/2021-07-03",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Hospital Referral Region"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mr4u-abm2",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mr4u-abm2",
             "description": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 years, Confirmed to Legionellosis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, Age<5 years, Confirmed to Legionellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51400,60 +51378,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mr4u-abm2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mr4u-abm2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mr4u-abm2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mr4u-abm2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mr4u-abm2",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
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
+            "landingPage": "https://data.cdc.gov/d/mr4u-abm2",
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
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, Age<5 years, Confirmed to Legionellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:000"
             ],
-            "landingPage": "https://data.cdc.gov/d/mr8w-325u",
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
-                "name": "data.cdc.gov"
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
@@ -51461,63 +51446,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mr8w-325u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mr8w-325u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mr8w-325u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mr8w-325u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mr8w-325u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mr8w-325u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mr8w-325u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mr8w-325u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mr8w-325u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/mr8w-325u",
+            "issued": "2016-10-06",
+            "keyword": [
+                "122 cities",
+                "mmwr table iii",
+                "mortality"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mr8w-325u",
+            "modified": "2016-10-06",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "Deaths in 122 U.S. cities - 1962-2016. 122 Cities Mortality Reporting System"
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
-                "name": "data.cdc.gov"
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
@@ -51525,55 +51504,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mrip-2k2a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mrip-2k2a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mrip-2k2a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mrip-2k2a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mrip-2k2a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mrip-2k2a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mrip-2k2a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mrip-2k2a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mrip-2k2a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/mscq-ew9n",
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
-                "name": "data.cdc.gov"
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
@@ -51581,38 +51571,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mscq-ew9n",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/mscq-ew9n",
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
+            "title": "Evaluation of the fall protection of Type I industrial helmets"
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
-                "name": "data.cdc.gov"
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
@@ -51620,68 +51606,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/msjj-a7q2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/msjj-a7q2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/msjj-a7q2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/msjj-a7q2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/msjj-a7q2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/msjj-a7q2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/msjj-a7q2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/msjj-a7q2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/msjj-a7q2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/msjj-a7q2",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/msjj-a7q2",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 10 - Seattle"
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
-                "county",
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
-            "identifier": "https://data.cdc.gov/api/views/mssc-ksj7",
             "description": "This dataset contains model-based county-level estimates for the PLACES project 2020 release in GIS-friendly format. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2018 or 2017 county population estimates, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the census 2015 county boundary file in a GIS system to produce maps for 27 measures at the county level. An ArcGIS Online feature service is also available at https://www.arcgis.com/home/item.html?id=8eca985039464f4d83467b8f6aeb1320 for users to make maps online or to add data to desktop GIS software.",
-            "title": "PLACES: County Data (GIS Friendly Format), 2020 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51689,68 +51666,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mssc-ksj7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mssc-ksj7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mssc-ksj7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mssc-ksj7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mssc-ksj7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mssc-ksj7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mssc-ksj7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mssc-ksj7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mssc-ksj7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mssc-ksj7",
+            "issued": "2021-09-29",
+            "keyword": [
+                "behaviors",
+                "county",
+                "gis",
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
+            "title": "PLACES: County Data (GIS Friendly Format), 2020 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/mtc3-kq6r",
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
-            "identifier": "https://data.cdc.gov/api/views/mtc3-kq6r",
             "description": "CDC is collaborating with the National Institutes of Health (NIH), the Food and Drug Administration (FDA), Vitalant Research Institute (VRI), Westat Inc., and numerous blood collection organizations across the United States to conduct a nationwide COVID-19 seroprevalence survey of blood donors. This is the largest nationwide COVID-19 seroprevalence survey to date. De-identified blood samples are tested for antibodies to SARS-CoV-2 to better understand the percentage of people in the United States who have antibodies against SARS-CoV-2 (the virus that causes COVID-19) and to track how this percentage changes over time. Both SARS-CoV-2 infection and COVID-19 vaccines currently used in the United States result in production of anti-spike (anti-S) antibodies but only infection results in production of anti-nucleocapsid (anti-N) antibodies. Infection-induced seroprevalence estimates the proportion of the population with evidence of previous SARS-CoV-2 infection and refers to the prevalence of the population with both anti-S and anti-N antibodies.\n\nThis link connects to a webpage that displays the data from the Nationwide Blood Donor Seroprevalence Survey. It offers an interactive visualization available at https://covid.cdc.gov/covid-data-tracker/#nationwide-blood-donor-seroprevalence\n\nAdditional information is available at: https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/blood-bank-serosurvey.html",
-            "title": "2020-2021 Nationwide Blood Donor Seroprevalence Survey Infection-Induced Seroprevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51758,64 +51736,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mtc3-kq6r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mtc3-kq6r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mtc3-kq6r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/mtc3-kq6r",
+            "issued": "2021-10-01",
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
+            "landingPage": "https://data.cdc.gov/d/mtc3-kq6r",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "spatial": "US",
+            "temporal": "2020-07-01/2021-12-14",
             "theme": [
                 "Laboratory Surveillance"
-            ]
+            ],
+            "title": "2020-2021 Nationwide Blood Donor Seroprevalence Survey Infection-Induced Seroprevalence Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/muep-c3qd",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-09-03",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-20",
-            "keyword": [
-                "covid-19 vaccination",
-                "covid tracker",
-                "disability",
-                "hps"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Assessment Branch, Immunization Services Division, NCIRD, CDC",
                 "hasEmail": "mailto:VaxView@cdc.gov "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/muep-c3qd",
             "description": "Household Pulse Survey (HPS): HPS is a rapid-response survey of adults ages \u226518 years led by the U.S. Census Bureau, in partnership with seven other federal statistical agencies, to measure household experiences during the COVID-19 pandemic. Detailed information on probability sampling using the U.S. Census Bureau\u2019s Master Address File, questionnaires, response rates, and bias assessment is available on the Census Bureau website (https://www.census.gov/data/experimental-data-products/household-pulse-survey.html).\n\nData from adults age \u226518 years are collected by 20-minute online survey from randomly sampled households stratified by state and the top 15 metropolitan statistical areas (MSAs). Data are weighted to represent total persons age 18 and older living within households and to mitigate possible bias that can result from non-responses and incomplete survey frame. Data from adults age \u226518 years are collected by 20-minute online survey from randomly sampled households stratified by state and the top 15 metropolitan statistical areas (MSAs). For more information on this survey, see https://www.census.gov/programs-surveys/household-pulse-survey.html.\n\nData are weighted to represent total persons age 18 and older living within households and to mitigate possible bias that can result from non-responses and incomplete survey frame. Responses in the Household Pulse Survey (https://www.census.gov/programs-surveys/household-pulse-survey.html) are self-reported.\u202fEstimates of vaccination coverage may differ from vaccine administration data reported at\u202fCOVID-19 Vaccinations in the United States (https://covid.cdc.gov/covid-data-tracker/#vaccinations).",
-            "title": "Household Pulse Survey (HPS): COVID-19 Vaccination among People with Disabilities",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51823,41 +51807,92 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/muep-c3qd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/muep-c3qd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/muep-c3qd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/muep-c3qd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/muep-c3qd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/muep-c3qd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/muep-c3qd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/muep-c3qd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/muep-c3qd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/muep-c3qd",
+            "issued": "2021-09-03",
+            "keyword": [
+                "covid-19 vaccination",
+                "covid tracker",
+                "disability",
+                "hps"
+            ],
+            "landingPage": "https://data.cdc.gov/d/muep-c3qd",
+            "modified": "2022-12-20",
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
+            "title": "Household Pulse Survey (HPS): COVID-19 Vaccination among People with Disabilities"
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
+                    "describedBy": "https://data.cdc.gov/api/views/muzy-jte6/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/muzy-jte6/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/muzy-jte6/columns.xml",
+                    "describedByType": "application/xml",
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
@@ -51885,90 +51920,35 @@
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/muzy-jte6",
-            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional counts of deaths by the week the deaths occurred, by state of occurrence, and by select underlying causes of death for 2020-2023.  The dataset also includes weekly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.\n\nNOTE: death counts are presented with a one week lag.",
-            "title": "Weekly Provisional Counts of Deaths by State and Select Causes, 2020-2023",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/muzy-jte6/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/muzy-jte6/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/muzy-jte6/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/muzy-jte6/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
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
-            "landingPage": "https://data.cdc.gov/d/mv87-mh7a",
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
-                "smallpox",
-                "spotted fever rickettsiosis confirmed",
-                "spotted fever rickettsiosis probable",
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
-            "identifier": "https://data.cdc.gov/api/views/mv87-mh7a",
             "description": "NNDSS - TABLE 1GG.  Spotted fever rickettsiosis, Confirmed to Smallpox - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1GG. Spotted fever rickettsiosis, Confirmed to Smallpox",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51976,65 +51956,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mv87-mh7a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mv87-mh7a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mv87-mh7a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mv87-mh7a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mv87-mh7a",
+            "issued": "2019-04-23",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "smallpox",
+                "spotted fever rickettsiosis confirmed",
+                "spotted fever rickettsiosis probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/mv87-mh7a",
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
+            "title": "NNDSS - TABLE 1GG. Spotted fever rickettsiosis, Confirmed to Smallpox"
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
-                "name": "data.cdc.gov"
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
@@ -52042,65 +52022,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mvaf-qxac/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mvaf-qxac/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mvaf-qxac/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mvaf-qxac/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mvaf-qxac/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mvaf-qxac/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mvaf-qxac/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mvaf-qxac/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mvaf-qxac/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)"
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
-                "name": "data.cdc.gov"
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
@@ -52108,64 +52088,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mvsw-zuaf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mvsw-zuaf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mvsw-zuaf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "accrualPeriodicity": "NA",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-03-04",
-            "@type": "dcat:Dataset",
-            "temporal": "1999-2018",
-            "modified": "2024-10-24",
-            "references": [
-                "https://www.cdc.gov/nchs/nhanes/visualization/"
-            ],
-            "keyword": [
-                "chronic conditions",
-                "dqs",
-                "nhanes"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCHS",
                 "hasEmail": "mailto:dqs@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
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
@@ -52173,45 +52156,97 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mvup-dmxz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mvup-dmxz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mvup-dmxz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mvup-dmxz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mvup-dmxz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mvup-dmxz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mvup-dmxz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mvup-dmxz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mvup-dmxz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "DQS NHANES Select Chronic Conditions Prevalence Estimates"
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
+            "description": "Cumulative provisional counts of deaths sex, race/Hispanic origin, age group, and by select underlying causes of death.  The dataset also includes provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.  Includes deaths that occurred between January 1, 2020 to July 28, 2020.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/mwk9-wnfr/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/mwk9-wnfr/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/mwk9-wnfr/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/mwk9-wnfr",
             "issued": "2020-07-22",
-            "temporal": "2020-01-01/2020-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
             "keyword": [
                 "age",
                 "age group",
@@ -52241,91 +52276,34 @@
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
-                "name": "National Center for Health Statistics"
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
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/mwk9-wnfr/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/mwk9-wnfr/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwk9-wnfr/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/mwk9-wnfr/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
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
-            "landingPage": "https://data.cdc.gov/d/mwkk-wzmy",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/mwkk-wzmy",
             "description": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 For acute Hepatitis C, only confirmed cases were verified.",
-            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52333,64 +52311,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mwkk-wzmy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mwkk-wzmy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/mwkk-wzmy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/mwkk-wzmy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/mwkk-wzmy",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
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
+            "landingPage": "https://data.cdc.gov/d/mwkk-wzmy",
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
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable"
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
-                "name": "National Center for Health Statistics"
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
@@ -52398,46 +52381,44 @@
                     "mediaType": "text/html"
                 }
             ],
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
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm\u201d",
             "spatial": "United States",
-            "describedBy": "The sampling frame was composed of Master files for all American physicians who met the following criteria: Office-based; Principally engaged in patient care activities; Non-federally employed; Not in specialties of anesthesiology, pathology, or radiology; and Younger than 85 years of age at the time of the survey.",
-            "accrualPeriodicity": "Future funding patterns past 2024 are uncertain however, we expect yearly or biannually is reasonable R/P1Y or R/P2Y",
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
-                "name": "data.cdc.gov"
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
@@ -52445,49 +52426,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n24i-76tn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n24i-76tn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n24i-76tn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n24i-76tn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n24i-76tn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n24i-76tn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n24i-76tn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n24i-76tn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n24i-76tn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Invasive pneumococcal disease, all ages"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n2x4-haas",
-            "issued": "2024-07-24",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/n2x4-haas",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52495,60 +52488,50 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n2x4-haas/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n2x4-haas/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n2x4-haas/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n2x4-haas/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n2x4-haas/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n2x4-haas/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n2x4-haas/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n2x4-haas/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n2x4-haas/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/n2x4-haas",
+            "issued": "2024-07-24",
+            "landingPage": "https://data.cdc.gov/d/n2x4-haas",
+            "modified": "2024-07-24",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "dhds_dataset"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2024-11-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-31",
-            "keyword": [
-                "iis",
-                "iqvia",
-                "nis-acm",
-                "rsv vaccination",
-                "vsd"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "Monthly",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VaxView Team",
                 "hasEmail": "mailto:VaxView@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -52556,72 +52539,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n2zz-25mk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n2zz-25mk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n2zz-25mk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "Monthly Cumulative Number and Percent of Adults 75 Years and Older Who Received 1+ RSV Vaccination Doses by Jurisdiction, United States"
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
-                "name": "data.cdc.gov"
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
@@ -52629,66 +52608,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n322-ce6f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n322-ce6f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n322-ce6f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n322-ce6f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n322-ce6f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n322-ce6f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n322-ce6f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n322-ce6f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n322-ce6f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical"
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/n3wf-wtep",
             "description": "NNDSS - Table II. Shiga toxin to Shigellosis - 2015.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Includes E. coli O157:H7; Shiga toxin-positive, serogroup non-O157; and Shiga toxin-positive, not serogrouped.",
-            "title": "NNDSS - Table II. Shiga toxin to Shigellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52696,61 +52675,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n3wf-wtep/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n3wf-wtep/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n3wf-wtep/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n3wf-wtep/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n3wf-wtep",
+            "issued": "2016-01-07",
+            "keyword": [
+                "2015",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "shiga toxin-producing e. coli",
+                "shigellosis",
+                "stec",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n3wf-wtep",
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
+            "title": "NNDSS - Table II. Shiga toxin to Shigellosis"
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
-                "500cities",
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
@@ -52758,48 +52742,41 @@
                     "mediaType": "application/zip"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n44h-hy2j",
+            "issued": "2016-11-08",
+            "keyword": [
+                "500cities",
+                "boundaries",
+                "city",
+                "shapefile"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n44h-hy2j",
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
@@ -52807,51 +52784,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n4v6-56e8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n4v6-56e8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n4v6-56e8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n4v6-56e8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n4v6-56e8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n4v6-56e8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n4v6-56e8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n4v6-56e8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n4v6-56e8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/n5b3-jati",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/n5b3-jati",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52859,63 +52852,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n5b3-jati/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n5b3-jati/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n5b3-jati/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n5b3-jati/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n5b3-jati/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n5b3-jati/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n5b3-jati/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n5b3-jati/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n5b3-jati/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/n5b3-jati",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/n5b3-jati",
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
-            "landingPage": "https://data.cdc.gov/d/n5qs-vw3x",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "coronavirus",
-                "covid",
-                "covid-19",
-                "covid cases",
-                "covid deaths",
-                "dialysis",
-                "hemodialysis",
-                "ncird-corvd",
-                "sars-cov-2"
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
-            "identifier": "https://data.cdc.gov/api/views/n5qs-vw3x",
             "description": "Mandated reporting of Weekly Aggregate Case and Death Count data among dialysis patients and dialysis facility staff (healthcare personnel or HCP) in the United States was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. This dataset will contain weekly aggregate data from January 1, 2021, through May 10, 2023, and will remain publicly available.\n\nThis archived public use dataset contains reported COVID-19 case and death data per week for all states and territories, along with weekly totals for the entire United States, throughout the given timeframe.",
-            "title": "Weekly United States COVID-19 Cases and Deaths among Dialysis Patients - ARCHIVED",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52923,57 +52902,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n5qs-vw3x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n5qs-vw3x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n5qs-vw3x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/n5qs-vw3x",
+            "issued": "2023-10-03",
+            "keyword": [
+                "coronavirus",
+                "covid",
+                "covid-19",
+                "covid cases",
+                "covid deaths",
+                "dialysis",
+                "hemodialysis",
+                "ncird-corvd",
+                "sars-cov-2"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n5qs-vw3x",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "spatial": "United States",
             "theme": [
                 "Case Surveillance"
-            ]
+            ],
+            "title": "Weekly United States COVID-19 Cases and Deaths among Dialysis Patients - ARCHIVED"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/n7uz-829a",
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
-            "identifier": "https://data.cdc.gov/api/views/n7uz-829a",
             "description": "SARS-CoV-2 is a highly infectious respiratory virus that is primarily transmitted by respiratory aerosols and droplets emitted during activities such as talking, breathing, and coughing.  Because symptomatic and asymptomatic individuals with COVID-19 can exhibit a high viral load of SARS-CoV-2 in their respiratory fluids, the CDC recommends that people wear a face mask that covers the nose and mouth to reduce community transmission during the COVID-19 pandemic. Wearing a face mask to protect others from potentially infectious droplets, called source control, has been shown to be a highly effective infection control strategy to limit the spread of COVID-19.  The presence of mask face seal leaks enables respiratory aerosols to escape out rather than pass through the filtering materials of the mask, consequently reducing the benefits of wearing a face mask for source control.  As such, the current investigation examines various modifications that improve the fit of a medical or cloth face mask and reduce the amounts of expelled aerosols during simulated coughs and exhalations.",
-            "title": "Face mask fit modifications that improve source control performance dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52981,44 +52971,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/n7uz-829a",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/n7uz-829a",
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
+            "title": "Face mask fit modifications that improve source control performance dataset"
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
-                "name": "data.cdc.gov"
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
@@ -53026,64 +53006,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n835-hpyp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n835-hpyp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n835-hpyp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n835-hpyp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis"
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
-                "name": "data.cdc.gov"
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
@@ -53091,71 +53072,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n83i-w4cq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n83i-w4cq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n83i-w4cq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n83i-w4cq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n83i-w4cq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n83i-w4cq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n83i-w4cq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n83i-w4cq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n83i-w4cq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis"
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
-                "ncird-corvd",
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
-                "name": "CDC"
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
@@ -53163,64 +53140,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n8mc-b4w4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n8mc-b4w4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/n8mc-b4w4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "ncird-corvd",
+                "state",
+                "surveillance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/n8mc-b4w4",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-13",
```

