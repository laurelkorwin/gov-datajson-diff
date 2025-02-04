# Change History for cdc.json (Part 4)

### Changes from 9cd27cf to 452e48f (Part 4/8)
**Author:** Automated

**Date:** 2025-02-03 20:01:08+00:00

**Message:** Updated data: Mon Feb  3 20:01:08 UTC 2025

```diff
                     "describedBy": "https://data.cdc.gov/api/views/e539-uadk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e539-uadk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e539-uadk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e539-uadk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e539-uadk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/e539-uadk",
+            "issued": "2023-10-26",
+            "keyword": [
+                "acs",
+                "estimates",
+                "places",
+                "sdoh",
+                "tract"
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
+            "title": "SDOH Measures for Census Tract, ACS 2017-2021"
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -31611,76 +31521,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e5zk-7tx5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e5zk-7tx5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e5zk-7tx5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/e5zk-7tx5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e5zk-7tx5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e5zk-7tx5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e5zk-7tx5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e5zk-7tx5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e5zk-7tx5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-                "name": "National Center for Health Statistics"
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
@@ -31688,65 +31590,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e6fc-ccez/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e6fc-ccez/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e6fc-ccez/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/e6fc-ccez/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e6fc-ccez/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e6fc-ccez/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e6fc-ccez/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e6fc-ccez/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e6fc-ccez/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "data.cdc.gov"
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
@@ -31754,75 +31668,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e8fc-yrqd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e8fc-yrqd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e8fc-yrqd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e8fc-yrqd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/e8fc-yrqd",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/e8fc-yrqd",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 1 - Boston"
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
-                "name": "National Center for Health Statistics"
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
@@ -31830,43 +31729,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e8kx-wbww/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e8kx-wbww/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e8kx-wbww/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/e92c-t3mi",
             "bureauCode": [
                 "009:20"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "description": "Explore the Going Smokefree Matters \u2013 Bars and Restaurants Infographic which outlines key facts related to the effects of secondhand smoke exposure in bars and restaurants.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/e92c-t3mi/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/e92c-t3mi",
             "issued": "2016-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-27",
             "keyword": [
                 "bars",
                 "fact sheet",
@@ -31876,61 +31818,32 @@
                 "smokefree",
                 "state system"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/e92c-t3mi",
+            "modified": "2023-07-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Centers for Disease Control and Prevention"
             },
-            "identifier": "https://data.cdc.gov/api/views/e92c-t3mi",
-            "description": "Explore the Going Smokefree Matters \u2013 Bars and Restaurants Infographic which outlines key facts related to the effects of secondhand smoke exposure in bars and restaurants.",
-            "title": "Going Smokefree Matters - Bars and Restaurants Infographic",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/download/e92c-t3mi/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
             "theme": [
                 "Policy"
-            ]
+            ],
+            "title": "Going Smokefree Matters - Bars and Restaurants Infographic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/e9r5-5hjr",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2015-08-10",
-            "@type": "dcat:Dataset",
-            "modified": "2015-08-27",
-            "keyword": [
-                "americas",
-                "chikungunya",
-                "paho"
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
-            "identifier": "https://data.cdc.gov/api/views/e9r5-5hjr",
             "description": "Derived from Pan American Health Organization reports: http://www.paho.org/hq/index.php?option=com_topics&view=article&id=343&Itemid=40931",
-            "title": "New Chikungunya Cases Reported in the Americas",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31938,59 +31851,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e9r5-5hjr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e9r5-5hjr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/e9r5-5hjr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/e9r5-5hjr",
+            "issued": "2015-08-10",
+            "keyword": [
+                "americas",
+                "chikungunya",
+                "paho"
+            ],
+            "landingPage": "https://data.cdc.gov/d/e9r5-5hjr",
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
+            "title": "New Chikungunya Cases Reported in the Americas"
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
-                "name": "data.cdc.gov"
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
@@ -31998,64 +31912,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ea3z-m7eh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ea3z-m7eh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ea3z-m7eh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ea3z-m7eh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ea3z-m7eh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ea3z-m7eh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ea3z-m7eh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ea3z-m7eh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ea3z-m7eh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ea3z-m7eh",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ea3z-m7eh",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 7 - Kansas City"
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
-            "temporal": "2024-2025",
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
-            "identifier": "https://data.cdc.gov/api/views/eanj-9nie",
             "description": "Weekly COVID-19 Vaccination Coverage of Adults18 Years and Older by Jurisdiction \u2022 Weekly estimates of COVID-19 vaccination coverage and intent among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM)(https://www.cdc.gov/nis/about/index.html). \n\nWeekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.",
-            "title": "Weekly Differences in Cumulative COVID-19 Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324, Overall, by Jurisdiction Among Adults 18 Years",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32063,78 +31973,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eanj-9nie/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eanj-9nie/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eanj-9nie/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eanj-9nie/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National, Region, State",
+            "identifier": "https://data.cdc.gov/api/views/eanj-9nie",
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
+            "temporal": "2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Differences in Cumulative COVID-19 Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324, Overall, by Jurisdiction Among Adults 18 Years"
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
@@ -32142,64 +32044,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eav7-hnsx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eav7-hnsx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eav7-hnsx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eav7-hnsx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
@@ -32207,61 +32118,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eb4y-d4ic/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eb4y-d4ic/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eb4y-d4ic/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/eb4y-d4ic/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eb4y-d4ic/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eb4y-d4ic/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eb4y-d4ic/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eb4y-d4ic/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eb4y-d4ic/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "data.cdc.gov"
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
@@ -32269,55 +32183,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ebbj-sh54/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ebbj-sh54/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ebbj-sh54/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ebbj-sh54/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ebbj-sh54/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ebbj-sh54/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ebbj-sh54/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ebbj-sh54/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ebbj-sh54/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ebbj-sh54",
+            "issued": "2016-09-26",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ebbj-sh54",
+            "modified": "2016-09-26",
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
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, All States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/eddk-effy",
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
-            "identifier": "https://data.cdc.gov/api/views/eddk-effy",
             "description": "Growing evidence suggests that Gulf War Illness (GWI) is the result of underlying neuroimmune dysfunction.  For example, previously we found that several Gulf War-relevant organophosphate, acetylcholinesterase inhibitors produce heightened neuroinflammatory responses following a sub chronic stressor exposure.  The goal of the study was to evaluate the potential for the \u03b2-adrenergic receptor inhibitor and anti-inflammatory drug, propranolol, to treat neuroinflammation in a novel long-term mouse model of GWI. We established that our long-term GWI model produces enhanced and prolonged neuroinflammation that is dependent upon Gulf War-relevant organophosphate exposure. Propranolol treatment abrogated the neuroinflammation instigated in our model specifically, having no treatment effects in non-DFP exposed groups. Our results indicate that propranolol may be a promising therapy for GWI by treating the underlying neuroinflammation associated with Gulf War-relevant physiological stress and organophosphate exposures.",
-            "title": "The \u03b2-adrenergic receptor blocker and anti-inflammatory drug propranolol mitigates brain cytokine expression in a long-term model of Gulf War Illness",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32325,45 +32243,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/eddk-effy",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/eddk-effy",
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
+            "title": "The \u03b2-adrenergic receptor blocker and anti-inflammatory drug propranolol mitigates brain cytokine expression in a long-term model of Gulf War Illness"
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
-                "place",
-                "places",
-                "sdoh"
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
-            "identifier": "https://data.cdc.gov/api/views/edkk-ze78",
             "description": "This dataset contains place-level (incorporated and census-designated places) social determinants of health (SDOH) measures from the American Community Survey 5-year data for the entire United States\u201450 states and the District of Columbia. Data were downloaded from data.census.gov using Census API and processed by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. These measures complement existing PLACES measures, including PLACES SDOH measures (e.g., health insurance, routine check-up). These data can be used together with PLACES data to identify which health and SDOH issues overlap in a community to help inform public health planning.  \n\nTo access spatial data, please use the ArcGIS Online service: https://cdcarcgis.maps.arcgis.com/home/item.html?id=d51009ea78b54635be95c6ec9955ec17.",
-            "title": "SDOH Measures for Place, ACS 2017-2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32371,68 +32278,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/edkk-ze78/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/edkk-ze78/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/edkk-ze78/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/edkk-ze78/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/edkk-ze78",
+            "issued": "2023-10-26",
+            "keyword": [
+                "acs",
+                "estimates",
+                "place",
+                "places",
+                "sdoh"
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
+            "title": "SDOH Measures for Place, ACS 2017-2021"
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
-                "name": "data.cdc.gov"
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
@@ -32440,70 +32345,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/edtz-vibe/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/edtz-vibe/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/edtz-vibe/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/edtz-vibe/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/edtz-vibe/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/edtz-vibe/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/edtz-vibe/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/edtz-vibe/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/edtz-vibe/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Ehrlichiosis/Anaplasmosis"
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
-                "name": "data.cdc.gov"
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
@@ -32511,66 +32414,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ee48-w5t6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ee48-w5t6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ee48-w5t6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ee48-w5t6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ee48-w5t6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ee48-w5t6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ee48-w5t6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ee48-w5t6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ee48-w5t6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2024-09-12",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
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
-                "name": "data.cdc.gov"
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
@@ -32578,55 +32485,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eez9-q5m5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eez9-q5m5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eez9-q5m5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/eez9-q5m5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eez9-q5m5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eez9-q5m5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eez9-q5m5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eez9-q5m5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eez9-q5m5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon to Powassan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/ef89-9ik2",
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
-            "identifier": "https://data.cdc.gov/api/views/ef89-9ik2",
             "description": "Interleukin (IL)-11, a pleiotropic, cationic cytokine, contributes to numerous biological processes, including adipogenesis, hematopoiesis, and inflammation.  Asthma, a chronic respiratory disease, is notably characterized by reversible airway obstruction, persistent lung inflammation, and airway hyperresponsiveness (AHR).  Nasal insufflation of IL-11 causes AHR in wild-type mice while lung inflammation induced by antigen sensitization and challenge, which mimics features of atopic asthma in humans, is attenuated in mice genetically deficient in IL-11 receptor subunit alpha-1 (IL-11R\u03b11-deficient mice), a transmembrane receptor that is required along with glycoprotein 130 to transduce IL-11 intracellular signaling.  Nevertheless, the contribution of IL-11R\u03b11 to the manifestation of phenotypic features of non-atopic asthma are not presently known. Thus, based on the aforementioned observations, we hypothesized that genetic deficiency of IL-11R\u03b11 would attenuate lung inflammation and increases in airway responsiveness following acute inhalation exposure to ozone, a criteria pollutant and non-atopic asthma stimulus.",
-            "title": "Interleukin-11 Receptor Subunit Alpha-1 is Required for Maximal Airway Responsiveness to Methacholine After Acute Exposure to Ozone",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32634,43 +32552,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ef89-9ik2",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/ef89-9ik2",
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
+            "title": "Interleukin-11 Receptor Subunit Alpha-1 is Required for Maximal Airway Responsiveness to Methacholine After Acute Exposure to Ozone"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/efb8-zbb7",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/efb8-zbb7",
             "description": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia \u2013 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Tuberculosis data for weeks 4-31 are incorrect for New York City; the Middle Atlantic region total; U.S. Residents, excluding U.S. Territories total; and the grand total, due to data processing issues. \nNotice: Tuberculosis data for weeks 32-33 are incorrect for the U.S. Residents, excluding U.S. Territories total and the grand total, due to data processing issues. \n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32678,65 +32587,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/efb8-zbb7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/efb8-zbb7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/efb8-zbb7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/efb8-zbb7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/efb8-zbb7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/efb8-zbb7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/efb8-zbb7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/efb8-zbb7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/efb8-zbb7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/efpc-rr7b",
-            "bureauCode": [
-                "009:00"
-            ],
-            "issued": "2019-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-03",
+            "identifier": "https://data.cdc.gov/api/views/efb8-zbb7",
+            "issued": "2020-01-21",
             "keyword": [
-                "2018",
+                "2020",
                 "nedss",
                 "netss",
                 "nndss",
-                "primary and secondary",
-                "spotted fever rickettsiosis",
-                "syphilis",
+                "tuberculosis",
+                "tularemia",
                 "wonder"
             ],
+            "landingPage": "https://data.cdc.gov/d/efb8-zbb7",
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
+            "title": "NNDSS - TABLE 1JJ. Tuberculosis to Tularemia"
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
-            "identifier": "https://data.cdc.gov/api/views/efpc-rr7b",
             "description": "NNDSS - Table II. Spotted fever rickettsiosis to Syphilis, primary and secondary - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum.\r\n \r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Spotted fever rickettsiosis to Syphilis, primary and secondary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32744,62 +32652,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/efpc-rr7b/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/efpc-rr7b/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/efpc-rr7b/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/efpc-rr7b",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "nedss",
+                "netss",
+                "nndss",
+                "primary and secondary",
+                "spotted fever rickettsiosis",
+                "syphilis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/efpc-rr7b",
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
+            "title": "NNDSS - Table II. Spotted fever rickettsiosis to Syphilis, primary and secondary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-03",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2025-01-31",
-            "keyword": [
-                "adult",
-                "covid-19 vaccination",
-                "pregnancy",
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
-            "identifier": "https://data.cdc.gov/api/views/efqg-e273",
             "description": "Weekly COVID-19 Vaccination Coverage, Pregnant Women 18-49 Years Old\n\n\u2022 COVID-19 vaccination coverage among pregnant women is assessed through the Vaccine Safety Datalink* \n\n\u2022 Data on updated 2023-24 COVID-19 vaccinations among pregnant women was available starting September 23, 2023, and includes doses received starting September 14, 2023.",
-            "title": "Weekly COVID-19 Vaccination Coverage among Pregnant Women by Race and Ethnicity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32807,61 +32719,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/efqg-e273/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/efqg-e273/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/efqg-e273/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/efqg-e273/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/efqg-e273/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/efqg-e273/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/efqg-e273/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/efqg-e273/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/efqg-e273/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/efqg-e273",
+            "issued": "2023-11-03",
+            "keyword": [
+                "adult",
+                "covid-19 vaccination",
+                "pregnancy",
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
+            "temporal": "2023-2024",
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly COVID-19 Vaccination Coverage among Pregnant Women by Race and Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/eg2p-49pd",
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
-            "identifier": "https://data.cdc.gov/api/views/eg2p-49pd",
             "description": "Working with vibrating hand tools is associated with the development of hand-arm vibration syndrome (HAVS).  HAVS is characterized by cold-induced vasospasms, finger blanching and changes in sensory function.  Vibration plays a major role in the development of the symptoms that are characteristic of HAVS, however, the hands and fingers of worker using tools are also exposed to pressure applied as the workers grip tools.  The pressure applied by gripping a tool might also affect blood flow and sensorineural function.  Therefore, this study examined the effects of applied pressure [2 and 4 newtons (N)] on peripheral vascular and sensorineural function using a characterized rat tail model.  The tails of rats were exposed to 0, 2 or 4N of applied force for 10 days.  Blood flow (laser doppler) and sensitivity of the tail to pressure (Randall-Selitto pressure test) was measured on days 1, 5 and 10 of the exposure.  The sensitivity of the tail nerves to electrical stimulation was measured on days 2 and 9.",
-            "title": "Applied force alters sensorineural and peripheral vascular function in an animal model of hand-arm vibration syndrome",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32869,47 +32787,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/eg2p-49pd",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.cdc.gov/d/eg2p-49pd",
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
+            "title": "Applied force alters sensorineural and peripheral vascular function in an animal model of hand-arm vibration syndrome"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/egm8-9wq7",
+            "accrualPeriodicity": "Archived",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-12-13 to 2021-09-30",
-            "modified": "2022-09-28",
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
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/egm8-9wq7",
             "description": "The Federal Pharmacy Partnership for Long-Term Care (LTC) Program was a partnership between CDC and CVS, Walgreens, and Managed Health Care Associates, Inc. The program offered on-site COVID-19 vaccination services for residents of nursing homes and assisted living facilities. The Federal Pharmacy Partnership for LTC Program was in effect after vaccines became available to April 23, 2021. This is the historical archived data related to the LTC Program and represents data that was shown on COVID Data Tracker through September 30, 2021. Twelve variables that provided data on residents and staff vaccinated through the program were removed from\u00a0the\u00a0COVID-19 Vaccinations in the United States,Jurisdiction dataset. LTC was removed as an option from the location variable in the following datasets: COVID-19 Vaccinations in the United States,Jurisdiction and COVID-19 Vaccination Trends in the United States,National and Jurisdictional.",
-            "title": "Archive: COVID-19 LTC Program Vaccinations and Trends in the United States, Jurisdiction",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32917,68 +32823,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/egm8-9wq7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/egm8-9wq7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/egm8-9wq7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/egm8-9wq7",
+            "issued": "2021-10-06",
+            "keyword": [
+                "administration",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "report date",
+                "vaccination"
+            ],
+            "landingPage": "https://data.cdc.gov/d/egm8-9wq7",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Archived",
+            "modified": "2022-09-28",
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
+            "temporal": "2020-12-13 to 2021-09-30",
             "theme": [
                 "Vaccinations"
-            ]
+            ],
+            "title": "Archive: COVID-19 LTC Program Vaccinations and Trends in the United States, Jurisdiction"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ehf4-c7tw",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ehf4-c7tw",
             "description": "NNDSS - TABLE 1U. Legionellosis to Listeriosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1U. Legionellosis to Listeriosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32986,65 +32894,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ehf4-c7tw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ehf4-c7tw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ehf4-c7tw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ehf4-c7tw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ehf4-c7tw",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/ehf4-c7tw",
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
+            "title": "NNDSS - TABLE 1U. Legionellosis to Listeriosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ei7y-3g6s",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2016-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2016-01-14",
-            "keyword": [
-                "2015",
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
-            "identifier": "https://data.cdc.gov/api/views/ei7y-3g6s",
             "description": "NNDSS - Table IV. Tuberculosis - 2015.This Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States will exclude counts from US territories.  Footnote:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Min: Minimum.    Max: Maximum. * Case counts for reporting year 2014 and 2015 are provisional through the end of the quarter,  January 2, 2016. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf Data for TB are displayed quarterly.",
-            "title": "NNDSS - Table IV. Tuberculosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33052,68 +32960,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ei7y-3g6s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ei7y-3g6s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ei7y-3g6s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ei7y-3g6s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ei7y-3g6s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ei7y-3g6s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ei7y-3g6s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ei7y-3g6s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ei7y-3g6s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ei7y-3g6s",
+            "issued": "2016-01-14",
+            "keyword": [
+                "2015",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "tb",
+                "tuberculosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ei7y-3g6s",
+            "modified": "2016-01-14",
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
+            "title": "NNDSS - Table IV. Tuberculosis"
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
-                "name": "data.cdc.gov"
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
@@ -33121,66 +33026,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ekcb-r85s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ekcb-r85s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ekcb-r85s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ekcb-r85s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ekcb-r85s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ekcb-r85s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ekcb-r85s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ekcb-r85s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ekcb-r85s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype"
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
-                "name": "data.cdc.gov"
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
@@ -33188,71 +33095,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ekd3-qu3w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ekd3-qu3w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ekd3-qu3w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis"
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
@@ -33260,60 +33163,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/em5e-5hvn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/em5e-5hvn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/em5e-5hvn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/em5e-5hvn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/em5e-5hvn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/em5e-5hvn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/em5e-5hvn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/em5e-5hvn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/em5e-5hvn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
-            "theme": [
-                "500 Cities & Places"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/en3s-hzsr",
-            "bureauCode": [
-                "009:20"
-            ],
-            "issued": "2021-06-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-03",
+            "identifier": "https://data.cdc.gov/api/views/em5e-5hvn",
+            "issued": "2024-07-15",
             "keyword": [
-                "abcs",
-                "bactfacts"
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
+            "theme": [
+                "500 Cities & Places"
+            ],
+            "title": "PLACES: Local Data for Better Health, Census Tract Data 2023 release"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Active Bacterial Core surveillance",
                 "hasEmail": "mailto:abcs@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/en3s-hzsr",
             "description": "ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul>  <li> <a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\n                Find details about surveillance population, case determination, surveillance evaluation, and more.  </li>                    <li> <a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>  \n                 Get official interpretations from reports and publications created from ABCs data.        </li> </ul>",
-            "title": "Active Bacterial Core surveillance (ABCs) Streptococcus pneumoniae",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33321,59 +33235,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/en3s-hzsr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/en3s-hzsr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/en3s-hzsr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/en3s-hzsr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/en3s-hzsr",
+            "issued": "2021-06-23",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "landingPage": "https://data.cdc.gov/d/en3s-hzsr",
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
+            "title": "Active Bacterial Core surveillance (ABCs) Streptococcus pneumoniae"
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
-                "name": "data.cdc.gov"
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
@@ -33381,71 +33295,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/en5r-5ds4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/en5r-5ds4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/en5r-5ds4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/en5r-5ds4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/en5r-5ds4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/en5r-5ds4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/en5r-5ds4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/en5r-5ds4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/en5r-5ds4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/en5r-5ds4",
+            "issued": "2018-07-26",
+            "keyword": [
+                "drought",
+                "environmental health"
+            ],
+            "landingPage": "https://data.cdc.gov/d/en5r-5ds4",
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
+            "title": "Palmer Drought Severity Index, 1895-2016"
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
-                "city",
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
-            "identifier": "https://data.cdc.gov/api/views/epbn-9bv3",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
             "description": "This dataset contains model-based place (incorporated and census-designated places) level estimates for the PLACES 2022 release. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. More information about the methodology can be found at   www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, Place Data 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33453,64 +33356,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/epbn-9bv3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/epbn-9bv3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/epbn-9bv3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/epbn-9bv3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Place-Data-202/eav7-hnsx",
+            "identifier": "https://data.cdc.gov/api/views/epbn-9bv3",
+            "issued": "2023-06-15",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "city",
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
+            "title": "PLACES: Local Data for Better Health, Place Data 2022 release"
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
-                "infant",
-                "mortality",
-                "nchs",
-                "neonatal",
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
-            "identifier": "https://data.cdc.gov/api/views/epev-k6ss",
             "description": "Rates are infants (under 1 year) and neonatal (under 28 days) deaths per 1,000 live births.\r\n\r\nhttps://www.cdc.gov/nchs/data-visualization/mortality-trends/",
-            "title": "NCHS - Infant and neonatal mortality rates: United States, 1915-2013",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33518,74 +33428,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/epev-k6ss/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/epev-k6ss/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/epev-k6ss/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/epev-k6ss/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/epev-k6ss/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/epev-k6ss/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/epev-k6ss/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/epev-k6ss/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/epev-k6ss/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/epev-k6ss",
+            "issued": "2015-07-14",
+            "keyword": [
+                "infant",
+                "mortality",
+                "nchs",
+                "neonatal",
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
+            "title": "NCHS - Infant and neonatal mortality rates: United States, 1915-2013"
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
@@ -33593,67 +33495,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/equ4-92qe/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/equ4-92qe/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/equ4-92qe/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/equ4-92qe/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
@@ -33661,46 +33570,97 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/escb-scz6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/escb-scz6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/escb-scz6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DRH Public Inquiries",
+                "hasEmail": "mailto:PRAMSProposals@cdc.gov"
+            },
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2011/ese6-rqpq",
+            "description": "2011.  Centers for Disease Control and Prevention (CDC).  PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments.  PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy.\r\nData will be updated annually as it becomes available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ese6-rqpq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ese6-rqpq/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/ese6-rqpq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ese6-rqpq/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/ese6-rqpq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ese6-rqpq/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/ese6-rqpq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ese6-rqpq",
+            "issued": "2023-07-18",
             "keyword": [
                 "abuse",
                 "alcohol use",
@@ -33722,78 +33682,36 @@
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
-                "name": "Centers for Disease Control and Prevention, Pregnancy Risk Assessment Monitoring System (PRAMS), Division of Reproductive Health"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ese6-rqpq",
-            "description": "2011.  Centers for Disease Control and Prevention (CDC).  PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments.  PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy.\r\nData will be updated annually as it becomes available.",
-            "title": "CDC PRAMStat Data for 2011",
+            "landingPage": "http://www.cdc.gov/prams/index.htm",
+            "modified": "2023-09-05",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/ese6-rqpq/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ese6-rqpq/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ese6-rqpq/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ese6-rqpq/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ese6-rqpq/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Pregnancy Risk Assessment Monitoring System (PRAMS), Division of Reproductive Health"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ese6-rqpq/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ese6-rqpq/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "https://www.cdc.gov/prams/index.htm",
+                "https://www.cdc.gov/prams/pramstat/index.html"
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2011/ese6-rqpq",
             "theme": [
                 "Maternal & Child Health"
-            ]
+            ],
+            "title": "CDC PRAMStat Data for 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/esmz-a36m",
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
-                "name": "data.cdc.gov"
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
@@ -33801,43 +33719,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/esmz-a36m",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/esmz-a36m",
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
+            "title": "Fit evaluation of NIOSH Approved N95 filtering facepiece respirators with various skin protectants: a pilot study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/espg-acwi",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-            "identifier": "https://data.cdc.gov/api/views/espg-acwi",
             "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses. With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2012 have been variant influenza viruses.",
-            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33845,68 +33754,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/espg-acwi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/espg-acwi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/espg-acwi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/espg-acwi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/espg-acwi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/espg-acwi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/espg-acwi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/espg-acwi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/espg-acwi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/espg-acwi",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a virus infections",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/espg-acwi",
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
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections"
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
-                "NIS-Flu"
-            ],
-            "keyword": [
-                "children",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/eudc-n39h",
             "description": "Weekly Cumulative Influenza Vaccination Coverage, Children 6 months through 17 years, United States\n\n\u2022 Archived data are available here:  https://data.cdc.gov/resource/vfj2-bfuw \n\u2022 Influenza vaccination coverage among children is assessed through the National Immunization Survey-Flu (NIS-Flu) annually, providing weekly influenza vaccination coverage estimates for children 6 months\u201317 years based upon parental report. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\no NIS-Flu is a national random-digit-dialed cellular telephone survey of households conducted during the flu season (October-June).\n\u2022 Final estimates for prior seasons and other flu vaccination data are available at CDC\u2019s FluVaxView:  https://www.cdc.gov/flu/fluvaxview/index.htm.",
-            "title": "Weekly Cumulative Influenza Vaccination Coverage, Children 6 months through 17 years, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33914,61 +33820,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eudc-n39h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eudc-n39h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eudc-n39h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/eudc-n39h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eudc-n39h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eudc-n39h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/eudc-n39h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/eudc-n39h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/eudc-n39h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/eudc-n39h",
+            "issued": "2023-12-01",
+            "keyword": [
+                "children",
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
+                "NIS-Flu"
+            ],
+            "spatial": "United States",
+            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/eur4-ng38",
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
-            "identifier": "https://data.cdc.gov/api/views/eur4-ng38",
             "description": "Adipose tissue (AT), an endocrine organ, plays a central role in maintenance of whole-body energy homeostasis through its release of adipokines. Obesity, affecting over 40% of American adults, disrupts adipocyte metabolism leading to chronic systemic inflammation and metabolic dysfunction (MetDys). MetDys is associated with impaired lung function, pulmonary hypertension, and asthma. The aim of this study was to investigate the effects of high-fat Western diet (HFWD)-consumption on silica-induced pulmonary inflammation and fibrosis in the F344 rat.",
-            "title": "High-fat western diet consumption exacerbates silica-induced pulmonary inflammation and fibrosis",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33976,42 +33894,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/eur4-ng38",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/eur4-ng38",
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
+            "title": "High-fat western diet consumption exacerbates silica-induced pulmonary inflammation and fibrosis"
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
-            "modified": "2025-01-31",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -34019,71 +33930,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ewpg-rz7g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ewpg-rz7g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ewpg-rz7g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ewpg-rz7g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ewpg-rz7g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ewpg-rz7g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ewpg-rz7g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ewpg-rz7g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ewpg-rz7g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
-                "name": "data.cdc.gov"
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
@@ -34091,66 +33999,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ex65-qa8z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ex65-qa8z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ex65-qa8z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute"
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
-                "ncird-corvd",
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
-                "name": "CDC/NCIRD/CORVD"
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
@@ -34158,66 +34065,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/exs3-hbne/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/exs3-hbne/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/exs3-hbne/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "ncird-corvd",
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
+                "name": "CDC/NCIRD/CORVD"
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
-            "identifier": "https://data.cdc.gov/api/views/ey8b-ejrf",
+            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Su/ey8b-ejrf/revisions/0",
             "description": "Data were updated on September 11, 2024.\n\nART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Success Rates dataset contains success rates for ART cycles started during the year indicated. Since ART success depends on whether patients are using their own eggs or donor eggs, success rates are included separately for these two groups. Success rates for patients using their own eggs are shown per intended retrieval, per actual retrieval, and per transfer. These success rates are reported as cumulative success rates, which take into account transfers that occur within 1 year after an egg retrieval. Since ART success depends on whether patients are using ART for the first time or had prior ART cycles, users can examine success rates for all \u201cPatients using their own eggs\u201d or for \u201cPatients with no prior ART using their own eggs.\u201d For new patients using ART for the first time, the success rates are also shown after 1, 2, or all intended egg retrievals during the reporting year. In addition, the average number of transfers per intended retrieval and the average number of intended retrievals per live-birth delivery are shown. Success rates for ART cycles that involve the transfer of embryos created from donor eggs or donated embryos are shown and are not cumulative. They are based on donor cycles started in the year indicated that had embryo transfers, regardless of when the donor eggs were retrieved. Success rates in this section are not presented by patient age group because previous data show that an intended parent\u2019s age does not substantially affect success when using donor eggs or donated embryos. The success rates are presented by types of embryos and eggs used in the transfer. This dataset excludes cycles that were considered research\u2014that is, cycles performed to evaluate new procedures.",
-            "title": "2021 Final Assisted Reproductive Technology (ART) Success Rates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34225,62 +34135,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ey8b-ejrf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ey8b-ejrf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ey8b-ejrf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ey8b-ejrf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ey8b-ejrf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ey8b-ejrf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ey8b-ejrf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ey8b-ejrf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ey8b-ejrf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Su/ey8b-ejrf/revisions/0",
+            "identifier": "https://data.cdc.gov/api/views/ey8b-ejrf",
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
+            "title": "2021 Final Assisted Reproductive Technology (ART) Success Rates"
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
@@ -34288,42 +34201,93 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezab-8sq5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ezab-8sq5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ezab-8sq5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezab-8sq5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ezab-8sq5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ezab-8sq5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezab-8sq5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ezab-8sq5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ezab-8sq5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                    "describedBy": "https://data.cdc.gov/api/views/ezfr-g6hf/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ezfr-g6hf/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/ezfr-g6hf/columns.xml",
+                    "describedByType": "application/xml",
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
@@ -34352,85 +34316,35 @@
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
-                "name": "National Center for Health Statistics"
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
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ezfr-g6hf/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ezfr-g6hf/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ezfr-g6hf/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/ezfr-g6hf/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
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
-                "healthy people 2020",
-                "sdoh-access-to-health-care"
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
-            "identifier": "https://data.cdc.gov/api/views/f3a8-hmpp",
             "description": "The Foundation Health Measures component of the Healthy People 2020 (HP2020) Final Review includes data on 14 global summary measures used to monitor improvement in population health. See Technical Notes of the Foundation Health Measures in the HP2020 Final Review for additional information on the definition and construction of these measures included.",
-            "title": "Healthy People 2020 Foundation Health Measures",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34438,62 +34352,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/f3a8-hmpp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/f3a8-hmpp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/f3a8-hmpp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/f3a8-hmpp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/f3a8-hmpp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/f3a8-hmpp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/f3a8-hmpp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/f3a8-hmpp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/f3a8-hmpp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/f3a8-hmpp",
+            "issued": "2022-01-14",
+            "keyword": [
+                "healthy people 2020",
+                "sdoh-access-to-health-care"
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
+                "name": "National Center for Health Statistics"
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
-            "landingPage": "https://data.cdc.gov/d/f3zz-zga5",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-11-08",
-            "temporal": "9/1/2023 - Present",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Syndromic Surveillance Program",
                 "hasEmail": "mailto:nssp@cdc.gov "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
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
@@ -34501,61 +34419,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/f3zz-zga5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/f3zz-zga5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/f3zz-zga5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/f3zz-zga5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
-            "accrualPeriodicity": "R/P1W",
-            "theme": [
+            "identifier": "https://data.cdc.gov/api/views/f3zz-zga5",
+            "issued": "2024-11-08",
+            "landingPage": "https://data.cdc.gov/d/f3zz-zga5",
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:038"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "spatial": "U.S.",
+            "temporal": "9/1/2023 - Present",
+            "theme": [
                 "Public Health Surveillance"
-            ]
+            ],
+            "title": "Level of Acute Respiratory Illness (ARI) Activity by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-01-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-30",
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
-            "identifier": "https://data.cdc.gov/api/views/f8gx-sdye",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2007 Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34563,48 +34477,39 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/f8gx-sdye",
+            "issued": "2015-01-28",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
+            "modified": "2023-08-30",
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
+            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2007 Glossary and Methodology"
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
@@ -34612,66 +34517,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fbbf-hgkc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fbbf-hgkc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fbbf-hgkc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fbbf-hgkc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fbbf-hgkc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fbbf-hgkc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fbbf-hgkc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fbbf-hgkc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fbbf-hgkc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/fc5f-ixvg",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-07",
-            "keyword": [
-                "2019",
-                "arboviral diseases",
-                "babesiosis",
-                "nedss",
-                "netss",
-                "nndss",
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
-                "name": "data.cdc.gov"
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
@@ -34679,62 +34587,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fc5f-ixvg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fc5f-ixvg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fc5f-ixvg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fc5f-ixvg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2020-01-07",
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
+            "title": "NNDSS - TABLE 1D. Arboviral diseases, West Nile virus to Babesiosis"
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
-                "name": "data.cdc.gov"
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
@@ -34742,41 +34653,93 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fcqm-xrf4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fcqm-xrf4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fcqm-xrf4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fcqm-xrf4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fcqm-xrf4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fcqm-xrf4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fcqm-xrf4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fcqm-xrf4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fcqm-xrf4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2011-2014"
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
+            "description": "The Overview of Health Disparities analysis is a component of the Healthy People 2020 (HP2020) Final Review. The analysis included 611 objectives in HP2020. This file contains summary level information used for the evaluation of changes in disparities during HP2020, including calculations for the disparities measures and the disparities change categories for all objectives and population characteristics in the analysis. See Technical Notes for the Healthy People 2020 Overview of Health Disparities (https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities-technical-notes.htm) for additional information and criteria for objectives, data years, and population characteristics included in the analysis and statistical formulas and definitions for the disparities measures. \n\nData for additional years during the HP2020 tracking period that are not included in the Overview of Health Disparities are available on the HP2020 website (https://www.healthypeople.gov/2020/). \n\nNote that \u201crate\u201d as used may refer to a statistical rate expressed per unit population or a proportion, depending on how the HP2020 objective was defined.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fdpm-fddm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/fdpm-fddm/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/fdpm-fddm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/fdpm-fddm/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/fdpm-fddm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/fdpm-fddm/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/fdpm-fddm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/fdpm-fddm",
             "issued": "2022-03-09",
-            "@type": "dcat:Dataset",
-            "temporal": "1997-01-01/2018-12-31",
-            "modified": "2023-08-23",
             "keyword": [
                 "health disparities",
                 "healthy people 2020",
@@ -34805,89 +34768,38 @@
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
-            "identifier": "https://data.cdc.gov/api/views/fdpm-fddm",
-            "description": "The Overview of Health Disparities analysis is a component of the Healthy People 2020 (HP2020) Final Review. The analysis included 611 objectives in HP2020. This file contains summary level information used for the evaluation of changes in disparities during HP2020, including calculations for the disparities measures and the disparities change categories for all objectives and population characteristics in the analysis. See Technical Notes for the Healthy People 2020 Overview of Health Disparities (https://www.cdc.gov/nchs/healthy_people/hp2020/health-disparities-technical-notes.htm) for additional information and criteria for objectives, data years, and population characteristics included in the analysis and statistical formulas and definitions for the disparities measures. \n\nData for additional years during the HP2020 tracking period that are not included in the Overview of Health Disparities are available on the HP2020 website (https://www.healthypeople.gov/2020/). \n\nNote that \u201crate\u201d as used may refer to a statistical rate expressed per unit population or a proportion, depending on how the HP2020 objective was defined.",
-            "title": "Healthy People 2020 Overview of Health Disparities",
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
-                    "downloadURL": "https://data.cdc.gov/api/views/fdpm-fddm/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fdpm-fddm/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/fdpm-fddm/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fdpm-fddm/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/fdpm-fddm/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fdpm-fddm/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/fdpm-fddm/columns.xml",
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
+            "title": "Healthy People 2020 Overview of Health Disparities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fdyw-m38t",
             "bureauCode": [
                 "009:032"
             ],
-            "issued": "2018-08-01",
-            "@type": "dcat:Dataset",
-            "modified": "2018-11-27",
-            "keyword": [
-                "environmental health",
-                "skin cancer",
-                "sunlight",
-                "total solar irradiance"
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
-            "identifier": "https://data.cdc.gov/api/views/fdyw-m38t",
             "description": "This dataset provides data at the county level for the contiguous United States. It includes daily Global Horizontal Irradiance (GHI) data from 1991-2012 provided by the Environmental Remote Sensing group at the Rollins School of Public Health at Emory University. Please refer to the metadata attachment for more information.\r\n\r\nThese data are used by the CDC's National Environmental Public Health Tracking Network to generate sunlight and ultraviolet (UV) measures. Learn more about sunlight and UV on the Tracking Network's website: https://ephtracking.cdc.gov/showUVLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
-            "title": "Population-Weighted Global Horizontal Irradiance, 1991-2012",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34895,42 +34807,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fdyw-m38t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fdyw-m38t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fdyw-m38t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fdyw-m38t",
+            "issued": "2018-08-01",
+            "keyword": [
+                "environmental health",
+                "skin cancer",
+                "sunlight",
+                "total solar irradiance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fdyw-m38t",
+            "modified": "2018-11-27",
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
+            "title": "Population-Weighted Global Horizontal Irradiance, 1991-2012"
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
@@ -34940,72 +34884,36 @@
                 "preferred-languages",
                 "research-data-center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/doc2016_clas.pdf",
+            "modified": "2024-02-29",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
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
@@ -35013,66 +34921,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ffbi-is3j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ffbi-is3j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ffbi-is3j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ffbi-is3j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "data.cdc.gov"
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
@@ -35080,75 +34989,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fhc9-h3em/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fhc9-h3em/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fhc9-h3em/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fhc9-h3em/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fhc9-h3em/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fhc9-h3em/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fhc9-h3em/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fhc9-h3em/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fhc9-h3em/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue virus infection"
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
-                "name": "data.cdc.gov"
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
@@ -35156,59 +35054,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fhky-rtsk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fhky-rtsk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fhky-rtsk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fhky-rtsk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fhky-rtsk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fhky-rtsk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fhky-rtsk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fhky-rtsk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fhky-rtsk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2024-09-26",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
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
-            "landingPage": "https://data.cdc.gov/d/fip8-rcng",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2015-02-02",
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
-            "identifier": "https://data.cdc.gov/api/views/fip8-rcng",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "The Tax Burden on Tobacco Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35216,46 +35130,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fip8-rcng",
+            "issued": "2015-02-02",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fip8-rcng",
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
+            "title": "The Tax Burden on Tobacco Glossary and Methodology"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fj6i-3v3k",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/fj6i-3v3k",
             "description": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35263,59 +35169,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fj6i-3v3k/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fj6i-3v3k/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fj6i-3v3k/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6i-3v3k/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fj6i-3v3k",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
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
+            "landingPage": "https://data.cdc.gov/d/fj6i-3v3k",
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
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C, acute, Probable"
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
-                "name": "data.cdc.gov"
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
@@ -35323,59 +35237,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fj6s-ssz6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fj6s-ssz6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6s-ssz6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fj6s-ssz6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fj6s-ssz6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6s-ssz6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fj6s-ssz6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fj6s-ssz6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fj6s-ssz6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fj6s-ssz6",
+            "issued": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fj6s-ssz6",
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
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 2 - New York"
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
-                "name": "data.cdc.gov"
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
@@ -35383,43 +35297,90 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fkfk-2j5x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fkfk-2j5x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fkfk-2j5x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fkfk-2j5x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fkfk-2j5x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fkfk-2j5x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fkfk-2j5x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fkfk-2j5x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fkfk-2j5x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fkfk-2j5x",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fkfk-2j5x",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 9 - San Francisco"
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
+                    "describedBy": "https://data.cdc.gov/api/views/fpp2-pp25/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/fpp2-pp25/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/fpp2-pp25/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fpp2-pp25",
+            "issued": "2025-01-31",
             "keyword": [
                 "adult",
                 "age",
@@ -35453,86 +35414,36 @@
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
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/fpp2-pp25/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/fpp2-pp25/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpp2-pp25/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/fpp2-pp25/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
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
-            "landingPage": "https://data.cdc.gov/d/fpqb-s69d",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2018-07-16",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fpqb-s69d",
             "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2006-2010. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
-            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2006-2010",
-            "programCode": [
-                "009:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35540,65 +35451,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpqb-s69d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fpqb-s69d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fpqb-s69d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpqb-s69d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fpqb-s69d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fpqb-s69d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpqb-s69d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fpqb-s69d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fpqb-s69d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fpqb-s69d",
+            "issued": "2018-07-16",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "particulate matter",
+                "pm2.5"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fpqb-s69d",
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
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2006-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fpsi-y8tj",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-13",
-            "temporal": "2019-01-01/Present",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/fpsi-y8tj",
             "description": "This file contains death counts and death rates for drug overdose, suicide, homicide and firearm injuries by state of residence (additional datasets exist for other levels of geography). The data is grouped by 2 different time periods including yearly and trailing twelve months. Please see data dictionary for intents and mechanisms included in each measure.",
-            "title": "Mapping Injury, Overdose, and Violence - State",
-            "programCode": [
-                "009:033"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35606,68 +35515,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpsi-y8tj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fpsi-y8tj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fpsi-y8tj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpsi-y8tj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fpsi-y8tj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fpsi-y8tj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fpsi-y8tj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fpsi-y8tj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fpsi-y8tj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fpsi-y8tj",
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
+            "landingPage": "https://data.cdc.gov/d/fpsi-y8tj",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:033"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "temporal": "2019-01-01/Present",
             "theme": [
                 "Injury & Violence"
-            ]
+            ],
+            "title": "Mapping Injury, Overdose, and Violence - State"
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
-                "name": "data.cdc.gov"
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
@@ -35675,55 +35582,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fqve-8wzt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fqve-8wzt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fqve-8wzt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fqve-8wzt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fqve-8wzt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fqve-8wzt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fqve-8wzt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fqve-8wzt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fqve-8wzt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2016-04-29",
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/fsf9-trph",
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
-                "name": "data.cdc.gov"
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
@@ -35731,44 +35649,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fsf9-trph",
+            "issued": "2024-12-12",
+            "landingPage": "https://data.cdc.gov/d/fsf9-trph",
+            "modified": "2024-12-12",
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
+            "title": "Comparative in vitro toxicity of different thermal spray particulates in human bronchial cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fuzh-wm4c",
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
-            "identifier": "https://data.cdc.gov/api/views/fuzh-wm4c",
             "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 In previous years, cases were reported as Salmonellosis. Beginning in January 2019, cases began to be reported as Salmonella Paratyphi infection.\r\n\u00b6 In previous years, cases were reported as typhoid fever. Beginning in January 2019, cases began to be reported as Salmonella Typhi infection.\r\n** In previous years, cases were reported as Salmonellosis (excluding paratyphoid fever and typhoid fever). Beginning in January 2019, cases began to be reported as Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection).",
-            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35776,55 +35684,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fuzh-wm4c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fuzh-wm4c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fuzh-wm4c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fuzh-wm4c",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonella paratyphi infection",
+                "salmonella typhi infection",
+                "salmonellosis (excluding salmonella typhi infection and salmonella paratyphi infection)",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/fuzh-wm4c",
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
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/fveu-vvk9",
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
-            "identifier": "https://data.cdc.gov/api/views/fveu-vvk9",
             "description": "E-cigarettes utilize a wide range of flavoring chemicals whose respiratory health effects are not well understood. In this study, we used pulmonary-associated cell lines to assess the in vitro cytotoxic effects of thirty flavoring chemicals. Human bronchial epithelial cells (BEAS-2B) and both na\u00efve and activated macrophages (THP-1) were treated with 10, 100, and 1000 \u00b5M of flavoring chemicals and analyzed for changes in viability, cell membrane damage, reactive oxygen species (ROS) production, and inflammatory cytokine release. Viability was most greatly affected by decanal, hexanal, nonanal, cinnamaldehyde, eugenol, vanillin, alpha-pinene, eugenol, and limonene. High amounts of ROS were elicited by vanillin, ethyl maltol, and the diketones (2,3-pentanedione, 2,3-heptanedione, and 2,3-hexanedione) from both cell lines. Na\u00efve THP-1 cells produced significant levels of IL-1\u03b2, IL-8, and TNF-\u03b1 when exposed to ethyl maltol and hexanal. Activated THP-1 cells released increased IL-1\u03b2 and TNF-\u03b1 when exposed to ethyl maltol, but many flavoring chemicals had an apparent suppressive effect on inflammatory cytokines released by activated macrophages, with varying degrees of accompanying cytotoxicity. The diketones, L-carvone, and linalool, suppressed cytokine release in the absence of cytotoxicity. These findings provide insight into patterns of cytotoxicity and inflammatory cytokine release potentially relevant to the development of pathological changes in the lungs of e-cigarette users.",
-            "title": "Effects of E-Cigarette Flavoring Chemicals on Human Macrophages and Bronchial Epithelial Cells",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35832,41 +35750,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fveu-vvk9",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/fveu-vvk9",
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
+            "title": "Effects of E-Cigarette Flavoring Chemicals on Human Macrophages and Bronchial Epithelial Cells"
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
-                "name": "CDC"
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
@@ -35874,71 +35786,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fvm6-ic5r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fvm6-ic5r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fvm6-ic5r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fvm6-ic5r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "CDC"
+            },
+            "spatial": "US",
             "theme": [
                 "Foodborne, Waterborne, and Related Diseases"
-            ]
+            ],
+            "title": "BEAM Dashboard - Serotypes of concern: Illnesses and Outbreaks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/fyv2-xffj",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/fyv2-xffj",
             "description": "NNDSS - TABLE 1Q.  Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n * Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 For acute Hepatitis C, only confirmed cases were verified.",
-            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35946,64 +35851,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fyv2-xffj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fyv2-xffj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fyv2-xffj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fyv2-xffj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fyv2-xffj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fyv2-xffj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fyv2-xffj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fyv2-xffj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fyv2-xffj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/fyv2-xffj",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/fyv2-xffj",
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
+            "title": "NNDSS - TABLE 1Q. Hepatitis B, perinatal infection to Hepatitis C (viral, acute), Probable"
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
-                "name": "data.cdc.gov"
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
@@ -36011,62 +35920,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fztq-uwup/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fztq-uwup/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/fztq-uwup/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1H. Cholera to Coccidioidomycosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-02-01",
-            "@type": "dcat:Dataset",
-            "temporal": "Flu Seasons-2021-22, 2022-23, 2023-24",
-            "modified": "2024-09-03",
-            "keyword": [
-                "flu vaccination",
-                "iis",
-                "immunization information system",
-                "vaccination coverage"
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
-            "identifier": "https://data.cdc.gov/api/views/g2ck-geg5",
             "description": "Monthly Cumulative Number and Percent of Persons Who Receive \u22651 Influenza Vaccination Doses and Comparison Between 2023-2024 and Two Previous Seasons, by Jurisdiction, United States\n\n\u2022 Influenza vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group. More information about the IIS can be found at https://www.cdc.gov/vaccines/programs/iis/about.html. \n\n\u2022 Influenza vaccination coverage estimate numerators include the number of people receiving at least one dose of influenza vaccine in a given flu season, based on information that state, territorial, and local public health agencies report to CDC. Some jurisdictions\u2019 data may include data submitted by tribes. Estimates include persons who are deceased but received a vaccination during the current season. People receiving doses are attributed to the jurisdiction in which the person resides unless noted otherwise. Quality and completeness of data may vary across jurisdictions. Influenza vaccination coverage denominators are obtained from 2020 U.S. Census Bureau population estimates. \n\n\u2022 Monthly estimates shown are cumulative, reflecting all persons vaccinated from July through a given month of that flu season. Cumulative estimates include any historical data reported since the previous submission. National estimates are not presented since not all U.S. jurisdictions are currently reporting their IIS data to CDC. Jurisdictions reporting data to CDC include U.S. states, some localities, and territories. \n\n\u2022 Because IIS data contain all vaccinations administered within a jurisdiction rather than a sample, standard errors were not calculated and statistical testing for differences in estimates across years were not performed. \n\n\u2022 Laws and policies regarding the submission of vaccination data to an IIS vary by state, which may impact the completeness of vaccination coverage reflected for a jurisdiction. More information on laws and policies are found at https://www.cdc.gov/vaccines/programs/iis/policy-legislation.html. \n\n\u2022 Coverage estimates based on IIS data are expected to differ from National Immunization Survey (NIS) estimates for children (https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-coverage-race.html)                 \nand adults (https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-adult-coverage.html) because NIS estimates are based on a sample that may not be representative after survey weighting and vaccination status is determined by survey respondent rather than vaccine records or administrations, and quality and completeness of IIS data may vary across jurisdictions. In general, NIS estimates tend to overestimate coverage due to overreporting and IIS estimates may underestimate coverage due to incompleteness of data in certain jurisdictions.",
-            "title": "Monthly Cumulative Number and Percent of Persons Who Receive \u22651 Influenza Vaccination Doses and Comparison Between 2023-2024 and Two Previous Seasons, by Jurisdiction, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36074,71 +35986,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g2ck-geg5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g2ck-geg5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g2ck-geg5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g2ck-geg5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g2ck-geg5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g2ck-geg5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g2ck-geg5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g2ck-geg5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g2ck-geg5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "identifier": "https://data.cdc.gov/api/views/g2ck-geg5",
+            "issued": "2024-02-01",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "immunization information system",
+                "vaccination coverage"
+            ],
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-09-03",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
+            },
+            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
+            "temporal": "Flu Seasons-2021-22, 2022-23, 2023-24",
             "theme": [
                 "Flu Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Cumulative Number and Percent of Persons Who Receive \u22651 Influenza Vaccination Doses and Comparison Between 2023-2024 and Two Previous Seasons, by Jurisdiction, United States"
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
-                "name": "data.cdc.gov"
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
@@ -36146,66 +36054,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g3c9-wbme/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g3c9-wbme/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g3c9-wbme/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g3c9-wbme/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g3c9-wbme/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g3c9-wbme/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g3c9-wbme/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g3c9-wbme/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g3c9-wbme/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g3g2-srtq",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2020-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-07",
-            "keyword": [
-                "2020",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/g3g2-srtq",
             "description": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus \u2013 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote:\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
-            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36213,60 +36120,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g3g2-srtq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g3g2-srtq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g3g2-srtq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g3g2-srtq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g3g2-srtq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g3g2-srtq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g3g2-srtq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g3g2-srtq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g3g2-srtq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g3g2-srtq",
+            "issued": "2020-01-21",
+            "keyword": [
+                "2020",
+                "machupo virus",
+                "marburg virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "sabia virus",
+                "viral hemorrhagic fevers",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/g3g2-srtq",
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
+            "title": "NNDSS - TABLE 1OO. Viral hemorrhagic fevers, Machupo virus to Viral hemorrhagic fevers, Sabia virus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g3k9-gyw7",
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
-            "identifier": "https://data.cdc.gov/api/views/g3k9-gyw7",
             "description": "This dataset includes deidentified data on patients receiving artesunate through the National Artesunate for Severe Malaria Program from April- December 2019. \n\nThis dataset contains the data from the case report form only.\nPlease see the links below for the other datasets and the attached document 'Guide to NASMP Datasets':\nData from Case Report Form- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Cas/igaz-icki\nData on Artesunate Dosing- https://data.cdc.gov/dataset/National-Artesunate-for-Severe-Malaria-Program-Art/qan4-gt4k\nData on Microscopy (Parasitemia values)- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Mic/v2k9-ctv4\n\nAll data can be easily linked using the ParticipantID field, a unique ID number assigned to each participant.",
-            "title": "National Artesunate for Severe Malaria Program Follow-On Antimalarial Dosing Data- April to December 2019",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36274,59 +36187,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g3k9-gyw7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g3k9-gyw7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g3k9-gyw7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g3k9-gyw7",
+            "issued": "2020-04-10",
+            "keyword": [
+                "artesunate",
+                "division of parasitic diseases and malaria",
+                "malaria"
+            ],
+            "landingPage": "https://data.cdc.gov/d/g3k9-gyw7",
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
+            "title": "National Artesunate for Severe Malaria Program Follow-On Antimalarial Dosing Data- April to December 2019"
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
-                "name": "data.cdc.gov"
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
@@ -36334,61 +36248,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4ag-jrdn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g4ag-jrdn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g4ag-jrdn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4ag-jrdn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g4ag-jrdn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g4ag-jrdn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4ag-jrdn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g4ag-jrdn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g4ag-jrdn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g4ag-jrdn",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/g4ag-jrdn",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 2 - New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-11",
-            "@type": "dcat:Dataset",
-            "temporal": "2023-2024",
-            "modified": "2025-01-31",
-            "keyword": [
-                "pregnancy",
-                "rsv",
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
-            "identifier": "https://data.cdc.gov/api/views/g4jn-64pd",
             "description": "Weekly RSV Vaccination Coverage, Pregnant Women 18-49 Years Old\n\n\u2022 RSV vaccination coverage among pregnant women is assessed through the Vaccine Safety Datalink*\n\n\u2022 Data on RSV vaccinations among pregnant women was available starting September 22, 2023, and includes doses received starting September 24, 2023.",
-            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant Women by Race and Ethnicity",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36396,79 +36309,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g4jn-64pd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g4jn-64pd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g4jn-64pd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/g4jn-64pd",
+            "issued": "2023-12-11",
+            "keyword": [
+                "pregnancy",
+                "rsv",
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
+            "temporal": "2023-2024",
             "theme": [
                 "Pregnancy & Vaccination"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant Women by Race and Ethnicity"
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
-                "name": "National Center for Health Statistics"
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
@@ -36476,67 +36377,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4z9-a9d3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g4z9-a9d3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g4z9-a9d3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4z9-a9d3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g4z9-a9d3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g4z9-a9d3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g4z9-a9d3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g4z9-a9d3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g4z9-a9d3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
@@ -36544,61 +36454,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g57i-yx3r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g57i-yx3r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g57i-yx3r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/g5ts-294x",
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pathology and Physiology Branch, HELD",
                 "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/g5ts-294x",
             "description": "Silicosis is an irreversible occupational lung disease resulting from crystalline silica exposure. Previously, we discovered that Western diet (HFWD)-consumption increases susceptibility to silica-induced pulmonary inflammation and fibrosis. This study investigates the potential of HFWD to alter silica-induced effects on airway epithelial ion transport and smooth muscle reactivity.",
-            "title": "High-Fat Western Diet Alters Silica-induced airway epithelium ion exchange but not airway smooth muscle reactivity",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36606,37 +36524,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g5ts-294x",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/g5ts-294x",
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
+            "title": "High-Fat Western Diet Alters Silica-induced airway epithelium ion exchange but not airway smooth muscle reactivity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/g653-rqe2",
+            "accrualPeriodicity": "Daily",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-22",
-            "keyword": [
-                "wastewater"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Wastewater Surveillance System",
                 "hasEmail": "mailto:nwss@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/g653-rqe2",
             "description": "This dataset provides a complete time history of SARS-CoV-2 concentrations in wastewater for each sampling location.",
-            "title": "NWSS Public SARS-CoV-2 Concentration in Wastewater Data",
-            "programCode": [
-                "009:028"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36644,72 +36560,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g653-rqe2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g653-rqe2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g653-rqe2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "Daily",
-            "theme": [
-                "Public Health Surveillance"
+            "identifier": "https://data.cdc.gov/api/views/g653-rqe2",
+            "issued": "2024-06-25",
+            "keyword": [
+                "wastewater"
             ],
+            "landingPage": "https://data.cdc.gov/d/g653-rqe2",
             "language": [
                 "English"
-            ]
+            ],
+            "modified": "2025-01-22",
+            "programCode": [
+                "009:028"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "theme": [
+                "Public Health Surveillance"
+            ],
+            "title": "NWSS Public SARS-CoV-2 Concentration in Wastewater Data"
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
-                "name": "data.cdc.gov"
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
@@ -36717,70 +36622,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g6fu-zp23/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g6fu-zp23/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g6fu-zp23/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g6fu-zp23/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, Age <5 years, Non-b serotype to Unknown serotype"
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
-                "name": "National Center for Health Statistics"
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
@@ -36788,48 +36692,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g6qk-ngsf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g6qk-ngsf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g6qk-ngsf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/g76d-z8vy",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_2_technical_documentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 2 is the second round of a three-round survey. The probability sample of RANDS during COVID-19 Round 2 was recruited using NORC at the University of Chicago (NORC)'s AmeriSpeak Panel, and the survey was administered by NORC from August 3, 2020 to August 20, 2020.  The RANDS during COVID-19 Round 2 Probability Sample has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/g76d-z8vy",
             "issued": "2022-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2020",
-            "modified": "2023-04-24",
             "keyword": [
                 "anxiety",
                 "covid-19",
@@ -36848,46 +36790,47 @@
                 "sdoh-workplace",
                 "telemedicine"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/g76d-z8vy",
+            "modified": "2023-04-24",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/g76d-z8vy",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 2 is the second round of a three-round survey. The probability sample of RANDS during COVID-19 Round 2 was recruited using NORC at the University of Chicago (NORC)'s AmeriSpeak Panel, and the survey was administered by NORC from August 3, 2020 to August 20, 2020.  The RANDS during COVID-19 Round 2 Probability Sample has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates",
-            "title": "NCHS Research and Development Survey (RANDS) Round 2 during COVID-19 probability sampled Restricted File",
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
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_2_technical_documentation.pdf",
+            "temporal": "2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 2 during COVID-19 probability sampled Restricted File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.cdc.gov/nchs/namcs/hcc/aboutnamcs.htm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component has randomly selected a nationally representative sample of health centers that provide health care services to the public and have an electronic health record, or EHR, system. Eligible health centers include:  Federally Qualified Health Centers (FQHCs; section 330-funded) FQHC Look-alikes (FQHC\u2013LALs; not federally funded) Currently, Indian Health Service Centers are not eligible for the NAMCS Health Center Component.",
+            "description": "The National Ambulatory Medical Care Survey (NAMCS) is designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. NAMCS began in 1973 as a national probability sample survey of visits to nonfederally employed office-based physicians. NCHS conducted the survey annually through 1981, again in 1985, and annually through 2021 (collection of visit data from physicians was stopped during 2020\u20132021 due to the burden placed on respondents by the COVID-19 pandemic). In 2006, a separate sample of Community Health Centers (CHCs) was added to the survey; the CHC component samples visits to both physicians and advanced practice providers (nurse practitioners, PAs [physician assistants and physician associates], and certified nurse midwives). Starting in 2012, in addition to the traditional NAMCS file, a separate data file for CHCs including physicians and advanced practice providers has been released.\n\nIn 2021, the former CHC sample of NAMCS was redesigned and launched as the NAMCS Health Center (HC) Component, collecting visit data from HCs using electronic health records, or EHR, systems of the participating health centers. The NAMCS Health Center Component contains critical data about health centers and the care they provide.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Link to the Standard Application Process attached.",
+                    "downloadURL": "https://www.cdc.gov/rdc/b3prosal/pp300.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/g795-gzp9",
             "issued": "2023-08-25",
-            "@type": "dcat:Dataset",
-            "temporal": "2021-2022",
-            "modified": "2024-03-05",
             "keyword": [
                 "advanced practice providers",
                 "electronic health records",
@@ -36903,74 +36846,36 @@
                 "visit characteristics",
                 "visit data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/namcs/hcc/aboutnamcs.htm",
+            "modified": "2024-03-05",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/g795-gzp9",
-            "description": "The National Ambulatory Medical Care Survey (NAMCS) is designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. NAMCS began in 1973 as a national probability sample survey of visits to nonfederally employed office-based physicians. NCHS conducted the survey annually through 1981, again in 1985, and annually through 2021 (collection of visit data from physicians was stopped during 2020\u20132021 due to the burden placed on respondents by the COVID-19 pandemic). In 2006, a separate sample of Community Health Centers (CHCs) was added to the survey; the CHC component samples visits to both physicians and advanced practice providers (nurse practitioners, PAs [physician assistants and physician associates], and certified nurse midwives). Starting in 2012, in addition to the traditional NAMCS file, a separate data file for CHCs including physicians and advanced practice providers has been released.\n\nIn 2021, the former CHC sample of NAMCS was redesigned and launched as the NAMCS Health Center (HC) Component, collecting visit data from HCs using electronic health records, or EHR, systems of the participating health centers. The NAMCS Health Center Component contains critical data about health centers and the care they provide.",
-            "title": "National Ambulatory Medical Care Survey, Health Center Component, 2021-2022, restricted data",
-            "programCode": [
-                "009:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.cdc.gov/rdc/b3prosal/pp300.htm",
-                    "mediaType": "text/html",
-                    "description": "Link to the Standard Application Process attached."
-                }
-            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
             "spatial": "United States",
-            "describedBy": "The National Ambulatory Medical Care Survey (NAMCS) Health Center Component has randomly selected a nationally representative sample of health centers that provide health care services to the public and have an electronic health record, or EHR, system. Eligible health centers include:  Federally Qualified Health Centers (FQHCs; section 330-funded) FQHC Look-alikes (FQHC\u2013LALs; not federally funded) Currently, Indian Health Service Centers are not eligible for the NAMCS Health Center Component.",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2021-2022",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "National Ambulatory Medical Care Survey, Health Center Component, 2021-2022, restricted data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-10-02",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-01",
-            "keyword": [
-                "age",
-                "age group",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "mortality",
-                "nchs",
-                "nvss",
-                "place of death",
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
-            "identifier": "https://data.cdc.gov/api/views/g7hk-rc8d",
             "description": "Provisional death counts of COVID-19 deaths by place of death, week, and age.\n\nData source: National Center for Health Statistics National Vital Statistics System. Provisional data for 2020-2021.",
-            "title": "AH Provisional COVID-19 Deaths by Week, Place of Death, and Age",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36978,57 +36883,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g7hk-rc8d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g7hk-rc8d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/g7hk-rc8d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
-            "theme": [
-                "NCHS"
-            ]
-        },
-        {
+            "identifier": "https://data.cdc.gov/api/views/g7hk-rc8d",
+            "issued": "2020-10-02",
+            "keyword": [
+                "age",
+                "age group",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "place of death",
+                "provisional",
+                "united states",
+                "weekly"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-01",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "theme": [
+                "NCHS"
+            ],
+            "title": "AH Provisional COVID-19 Deaths by Week, Place of Death, and Age"
+        },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/g7ty-3t6s",
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
-            "identifier": "https://data.cdc.gov/api/views/g7ty-3t6s",
             "description": "Our investigation examined the efficacy of Do-It-Yourself (DIY) air filtration units in reducing recipient exposure to simulated respiratory aerosols within a mock classroom. Seven commercially available box style fans were evaluated using five performance parameters. Two fans with the highest and lowest airflow rates were subsequently evaluated in two DIY unit configurations using either 2.5 or 5 cm deep minimum efficiency reporting value (MERV) 13 filters. DIY air filtration units were tested with the central HVAC system set at 2 air changes/hour (ACH) to represent a classroom with low ventilation. Results of the investigation provide a better understanding of DIY units and their potential to reduce exposure to infectious aerosols that can transmit SARS-CoV-2 and other diseases.\n\nNon-Endorsement Disclaimer:\nMention of any company or product does not constitute endorsement by the National Institute for Occupational Safety and Health (NIOSH), Centers for Disease Control and Prevention (CDC).",
-            "title": "Efficacy of Do-It-Yourself Air Filtration Units in Reducing Exposure to Simulated Respiratory Aerosols",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37036,19 +36954,43 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/g7ty-3t6s",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/g7ty-3t6s",
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
+            "title": "Efficacy of Do-It-Yourself Air Filtration Units in Reducing Exposure to Simulated Respiratory Aerosols"
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
@@ -37073,56 +37015,32 @@
                 "tobacco use",
                 "youth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "OSHData Support",
-                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/g9dy-mhts",
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
             "theme": [
                 "Survey Data"
-            ]
+            ],
+            "title": "Youth And Tobacco Use Infographic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/ga52-qyaz",
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
-            "identifier": "https://data.cdc.gov/api/views/ga52-qyaz",
             "description": "There is strong evidence associating the indoor environment with transmission of SARS-CoV-2, the virus that causes COVID-19. SARS-CoV-2 can spread by exposure to droplets and very fine aerosol particles from respiratory fluids that are released by infected persons. Layered mitigation strategies, including but not limited to maintaining physical distancing, adequate ventilation, universal masking, avoiding overcrowding, and vaccination, have shown to be effective in re-ducing the spread of SARS-CoV-2 within the indoor environment. Here, we examine the effect of mitigation strategies on reducing the risk of exposure to simulated respiratory aerosol particles within a classroom-style meeting room. To quantify exposure of uninfected individuals (Recip-ients), surrogate respiratory aerosol particles were generated by a breathing simulator with a headform (Source) that mimicked breath exhalations. Recipients, represented by three breathing simulators with manikin headforms, were placed in a meeting room and affixed with optical particle counters to measure 0.3\u20133 \u00b5m aerosol particles.",
-            "title": "Efficacy of ventilation, HEPA air cleaners, universal masking, and physical distancing for reducing exposure to simulated exhaled aerosols in a meeting room-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37130,49 +37048,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ga52-qyaz",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/ga52-qyaz",
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
+            "title": "Efficacy of ventilation, HEPA air cleaners, universal masking, and physical distancing for reducing exposure to simulated exhaled aerosols in a meeting room-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/prov-county-drug-overdose.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-10-05",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-01/2024-06-30",
-            "modified": "2025-01-15",
-            "keyword": [
-                "county",
-                "deaths",
-                "drug",
-                "drug overdose",
-                "monthly",
-                "mortality",
-                "nchs",
-                "nvss",
-                "provisional",
-                "sdoh-environmental",
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
-            "identifier": "https://data.cdc.gov/api/views/gb4e-yj24",
             "description": "This data visualization presents county-level provisional counts for drug overdose deaths based on a current flow of mortality data in the National Vital Statistics System. County-level provisional counts include deaths occurring within the 50 states and the District of Columbia, as of the date specified and may not include all deaths that occurred during a given time period. Provisional counts are often incomplete and causes of death may be pending investigation resulting in an underestimate relative to final counts (see Technical Notes).\n\nThe provisional data presented on the dashboard below include reported 12 month-ending provisional counts of death due to drug overdose by the decedent\u2019s county of residence and the month in which death occurred.\n\nPercentages of deaths with a cause of death pending further investigation and a note on historical completeness (e.g. if the percent completeness was under 90% after 6 months) are included to aid in interpretation of provisional data as these measures are related to the accuracy of provisional counts (see Technical Notes). Counts between 1-9 are suppressed in accordance with NCHS confidentiality standards. Provisional data presented on this page will be updated on a quarterly basis as additional records are received.\n\nTechnical Notes\n\nNature and Sources of Data\n\nProvisional drug overdose death counts are based on death records received and processed by the National Center for Health Statistics (NCHS) as of a specified cutoff date. The cutoff date is generally the first Sunday of each month. National provisional estimates include deaths occurring within the 50 states and the District of Columbia. NCHS receives the death records from the state vital registration offices through the Vital Statistics Cooperative Program (VSCP).\n\nThe timeliness of provisional mortality surveillance data in the National Vital Statistics System (NVSS) database varies by cause of death and jurisdiction in which the death occurred. The lag time (i.e., the time between when the death occurred and when the data are available for analysis) is longer for drug overdose deaths compared with other causes of death due to the time often needed to investigate these deaths (1). Thus, provisional estimates of drug overdose deaths are reported 6 months after the date of death.\n\nProvisional death counts presented in this data visualization are for \u201c12 month-ending periods,\u201d defined as the number of deaths occurring in the 12 month period ending in the month indicated. For example, the 12 month-ending period in June 2020 would include deaths occurring from July 1, 2019 through June 30, 2020. The 12 month-ending period counts include all seasons of the year and are insensitive to reporting variations by seasonality. These provisional counts of drug overdose deaths and related data quality metrics are provided for public health surveillance and monitoring of emerging trends. Provisional drug overdose death data are often incomplete, and the degree of completeness varies by jurisdiction and 12 month-ending period. Consequently, the numbers of drug overdose deaths are underestimated based on provisional data relative to final data and are subject to random variation.\n\nCause of Death Classification and Definition of Drug Deaths\n\nMortality statistics are compiled in accordance with the World Health Organizations (WHO) regulations specifying that WHO member nations classify and code causes of death with the current revision of the International Statistical Classification of Diseases and Related Health Problems (ICD). ICD provides the basic guidance used in virtually all countries to code and classify causes of death. It provides not only disease, injury, and poisoning categories but also the rules used to select the single underlying cause of death for tabulation from the several diagnoses that may be reported on a single death certificate, as well as definitions, tabulation lists, the format of the death certificate, and regul",
-            "title": "VSRR Provisional County-Level Drug Overdose Death Counts",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37180,51 +37083,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gb4e-yj24/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gb4e-yj24/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gb4e-yj24/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gb4e-yj24/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/gb4e-yj24",
+            "issued": "2021-10-05",
+            "keyword": [
+                "county",
+                "deaths",
+                "drug",
+                "drug overdose",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "sdoh-environmental",
+                "united states",
+                "vsrr"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/prov-county-drug-overdose.htm",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-15",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2015-01-01/2024-06-30",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "VSRR Provisional County-Level Drug Overdose Death Counts"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gb67-x49c",
-            "issued": "2023-10-18",
             "@type": "dcat:Dataset",
-            "modified": "2023-10-18",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SOZ9@cdc.gov",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/gb67-x49c",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "edav-demo-dataset-api",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37232,68 +37153,50 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gb67-x49c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gb67-x49c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gb67-x49c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gb67-x49c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gb67-x49c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gb67-x49c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gb67-x49c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gb67-x49c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gb67-x49c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/gb67-x49c",
+            "issued": "2023-10-18",
+            "landingPage": "https://data.cdc.gov/d/gb67-x49c",
+            "modified": "2023-10-18",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "edav-demo-dataset-api"
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
-            "identifier": "https://data.cdc.gov/api/views/gd4x-jyhw",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
             "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates for the PLACES 2022 release. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, ZCTA Data 2022 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37301,66 +37204,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gd4x-jyhw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gd4x-jyhw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gd4x-jyhw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gd4x-jyhw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gd4x-jyhw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gd4x-jyhw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gd4x-jyhw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gd4x-jyhw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gd4x-jyhw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
+            "identifier": "https://data.cdc.gov/api/views/gd4x-jyhw",
+            "issued": "2023-06-15",
+            "keyword": [
+                "behaviors",
+                "brfss",
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
+            "title": "PLACES: Local Data for Better Health, ZCTA Data 2022 release"
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
-                "name": "data.cdc.gov"
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
@@ -37368,64 +37276,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gepg-djaz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gepg-djaz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gepg-djaz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection"
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
-            "modified": "2023-09-08",
-            "keyword": [
-                "health statistics",
-                "nchs",
-                "nhanes",
-                "oral health",
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
-            "identifier": "https://data.cdc.gov/api/views/ggsw-596z",
             "description": "These data represent prevalence estimates of select oral health topics from the National Health and Nutrition Examination Survey (NHANES).",
-            "title": "NHANES Select Oral Health Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37433,61 +37343,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ggsw-596z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ggsw-596z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ggsw-596z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/ggsw-596z",
+            "issued": "2023-03-02",
+            "keyword": [
+                "oral health",
+                "nchs",
+                "nhanes",
+                "health statistics",
+                "surveillance",
+                "survey"
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
+            "title": "NHANES Select Oral Health Prevalence Estimates"
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
-                "name": "data.cdc.gov"
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
@@ -37495,56 +37413,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gjsp-ircr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gjsp-ircr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gjsp-ircr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "data.cdc.gov"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/gkpu-vawv",
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
-            "identifier": "https://data.cdc.gov/api/views/gkpu-vawv",
             "description": "According to the North American Industry Classification System, workers employed in the oil and gas extraction industry are working in one of three areas; 1) extraction, 2) drilling, or 3) processing and refinement (Bureau of Labor Statistics, April 15, 2014).  Both workers and people living in communities that are in close proximity to areas where gas and oil extraction and refinement occur have a higher incidence of respiratory, cardiovascular, digestive, reproductive and nervous system disorders,\n\nThe goal of these studies was to identify mechanisms underlying the development of cardiovascular disease after inhalation of crude oil vapors (COV). The oil used for this study was a surrogate of the crude oil that leaked into the Gulf of Mexico after the Deepwater Horizon oil spill (McKinney et al., 2021). We tested the hypothesis that changes in cardiovascular function after inhalation of COV are manifested as changes in the responsiveness of the heart and peripheral vascular system to vasoconstricting and vasodilating agonists.  Based on previous studies, we also predicted that inhalation of COV would affect the expression of biomarkers of cardiac and kidney function that are associated with blood pressure regulation and disease.",
-            "title": "Biological effects of crude oil vapor. IV. Cardiovascular effects-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37552,21 +37470,45 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gkpu-vawv",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/gkpu-vawv",
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
+            "title": "Biological effects of crude oil vapor. IV. Cardiovascular effects-Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.cdc.gov/d/gn5f-ec35",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS1_technical_documentation.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 1 was administered by Gallup using the Gallup Panel in the fall of 2015 \nand contains existing questions from the National Health Interview Survey (NHIS).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.cdc.gov/api/views/gn5f-ec35",
             "issued": "2022-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2015",
-            "modified": "2023-04-20",
             "keyword": [
                 "chronic conditions",
                 "food security",
@@ -37584,69 +37526,35 @@
                 "sdoh-poverty-income",
                 "sdoh-workplace"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://data.cdc.gov/d/gn5f-ec35",
+            "modified": "2023-04-20",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/gn5f-ec35",
-            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 1 was administered by Gallup using the Gallup Panel in the fall of 2015 \nand contains existing questions from the National Health Interview Survey (NHIS).",
-            "title": "NCHS Research and Development Survey (RANDS) Round 1 Restricted File",
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
-            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS1_technical_documentation.pdf",
+            "temporal": "2015",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "NCHS Research and Development Survey (RANDS) Round 1 Restricted File"
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
-                "name": "data.cdc.gov"
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
@@ -37654,76 +37562,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gp24-kfxi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gp24-kfxi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gp24-kfxi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital"
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
-            "issued": "2024-04-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2023",
-            "modified": "2025-01-31",
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
                 "hasEmail": "mailto:CDCINFO@CDC.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gpsd-ru5i",
-            "description": "List of footnotes, notes, and source information for NHIS Adult Summary Statistics. Each row of this dataset contains the accompanying text for a footnote found in the NHIS Adults Summary Statistics Dataset.",
-            "title": "DQS NHIS Adult Summary Statistics Footnotes",
-            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "describedBy": "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "009:020"
-            ],
+            "description": "List of footnotes, notes, and source information for NHIS Adult Summary Statistics. Each row of this dataset contains the accompanying text for a footnote found in the NHIS Adults Summary Statistics Dataset.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37731,64 +37631,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gpsd-ru5i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gpsd-ru5i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gpsd-ru5i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gpsd-ru5i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gpsd-ru5i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gpsd-ru5i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gpsd-ru5i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gpsd-ru5i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gpsd-ru5i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://wwwn.cdc.gov/NHISDataQueryTool/SHS_adult/SHS_Tech_Notes.pdf",
+            "identifier": "https://data.cdc.gov/api/views/gpsd-ru5i",
+            "isPartOf": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+            "issued": "2024-04-08",
+            "keyword": [
+                "nhis",
+                "sdoh-access-to-health-care",
+                "sdoh-employment",
+                "sdoh-food-access",
+                "sdoh-food-insecurity",
+                "sdoh-higher-education",
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
+            "modified": "2025-01-31",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
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
+            "title": "DQS NHIS Adult Summary Statistics Footnotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/gr26-95h2",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-06-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-03",
-            "keyword": [
-                "covid-19 vaccination",
-                "covid tracker",
-                "nis-ccm"
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
-            "identifier": "https://data.cdc.gov/api/views/gr26-95h2",
             "description": "National Immunization Survey Child COVID Module (NIS-CCM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics.",
-            "title": "National Immunization Survey Child COVID Module (NIS-CCM): Vaccination Status and Intent by Demographics | Data | Centers for Disease Control and Prevention (cdc.gov)",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37796,60 +37709,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gr26-95h2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gr26-95h2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gr26-95h2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gr26-95h2",
+            "issued": "2022-06-21",
+            "keyword": [
+                "covid-19 vaccination",
+                "covid tracker",
+                "nis-ccm"
+            ],
+            "landingPage": "https://data.cdc.gov/d/gr26-95h2",
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
+            "title": "National Immunization Survey Child COVID Module (NIS-CCM): Vaccination Status and Intent by Demographics | Data | Centers for Disease Control and Prevention (cdc.gov)"
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
-                "name": "National Center for Health Statistics"
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
@@ -37857,61 +37771,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gsea-w83j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gsea-w83j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gsea-w83j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/gt5d-asw4",
-            "issued": "2023-09-01",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-01",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Test",
                 "hasEmail": "mailto:Test"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gt5d-asw4",
             "description": "",
-            "title": "SocrataDataRefresh_Test",
-            "programCode": [
-                "009:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37919,52 +37837,52 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gt5d-asw4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gt5d-asw4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gt5d-asw4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/gt5d-asw4",
+            "issued": "2023-09-01",
+            "landingPage": "https://data.cdc.gov/d/gt5d-asw4",
+            "modified": "2023-09-01",
+            "programCode": [
+                "009:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "SocrataDataRefresh_Test"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/gt7a-q73y",
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
-            "identifier": "https://data.cdc.gov/api/views/gt7a-q73y",
             "description": "Copper-based preservatives consisting of micronized and nanoscale copper particles have been widely used in applications for wood protection. The presence of micronized/nanoscale particles and soluble aqueous copper in copper-treated wood has raised questions regarding the forms of released particles and the potential hazards of exposure during the use of these products. However, the lack of a comprehensive understanding of the chemistry of these Cu species is limiting the future investigation of the toxicity of these materials and their potential health impact on workers. In this work, we used a combination of scanning transmission electron microscope (STEM) and electron energy loss spectroscopy (EELS) to analyze the particles released during the sanding/sawing of copper-treated lumber. We have demonstrated using EELS Cu L2,3 edges with comparative reference spectra to determine the Cu species. Three types of species, including basic copper carbonate (BCC), Cu(0), and Cu(II)-Wood complex, were identified in released wood dust particles. The unbound copper particles also exist as a form of BCC or reduced Cu(0). The morphologies and chemical states of emitted copper particles indicate the potential chemical transformation due to copper-wood interactions.",
-            "title": "Revealing the Structural and Chemical Properties of Copper-based Nanoparticles Released from Copper Treated Wood-Dataset",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37972,45 +37890,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gt7a-q73y",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/gt7a-q73y",
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
+            "title": "Revealing the Structural and Chemical Properties of Copper-based Nanoparticles Released from Copper Treated Wood-Dataset"
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
-                "name": "data.cdc.gov"
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
@@ -38018,64 +37925,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gui6-i83p/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gui6-i83p/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gui6-i83p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gui6-i83p/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gui6-i83p/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gui6-i83p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gui6-i83p/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gui6-i83p/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gui6-i83p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#trends",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-06-06",
-            "temporal": "Data from 2020-03-14 to present (posted starting 2023-06-06)",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "references": [
-                "https://covid.cdc.gov/covid-data-tracker/"
-            ],
-            "keyword": [
-                "covid19",
-                "nrevss",
-                "test"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Virologic Unit, Surveillance and Analytics Team",
                 "hasEmail": "mailto:nrevss@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDC"
-            },
-            "identifier": "https://data.cdc.gov/api/views/gvsb-yw6g",
             "description": "More than 450 public health and clinical laboratories located throughout the United States participate in surveillance for severe acute respiratory virus coronavirus type 2 (SARS-CoV-2), the virus that causes COVID-19, through CDC's National Respiratory and Enteric Virus Surveillance System (NREVSS). The dataset contains a weekly summary of aggregate counts of the total SARS-CoV-2 tests and SARS-CoV-2 detections reported to NREVSS since March 14, 2020. These data are reported weekly on a voluntary basis. Clinical laboratories do not report demographic data through NREVSS. Testing practices may vary regionally, and the number of participating laboratories may change from year to year. Results can be changed for up to 2 years after the initial reporting week. However, discrepancies may be noted and updated at the discretion of the data stewards and key stakeholders.\n\nWhile NREVSS strives to present the most precise estimates of respiratory viral trends with reporting burden minimized for participating laboratories, there are several inherent limitations to this surveillance system.\n\nNREVSS does not collect patient-specific data or demographic information. Multiple samples may be collected from a single patient, so NREVSS results do not necessarily reflect the number of patients tested, nor do they directly reflect hospitalizations or deaths related to COVID-19.\n\nParticipating laboratories vary in size, testing capabilities, and areas served. Some institutions may receive and test samples from sites across a given state or even from multiple states. Without direct knowledge of the population base, NREVSS cannot be used to determine the prevalence or incidence of infection.\n\nFor more information on NREVSS and COVID-19 surveillance please visit: https://www.cdc.gov/surveillance/nrevss. These data appear starting May 25, 2023 on the CDC COVID Data Tracker at the following URLs: https://covid.cdc.gov/covid-data-tracker/#trends ; https://covid.cdc.gov/covid-data-tracker/#cases.   \n\nNREVSS data are reported at the national and HHS regional levels. The ten (10) U.S. Department of HHS regions are defined here: https://www.hhs.gov/about/agencies/iea/regional-offices/index.html. \n\nThe data represent SARS-CoV-2 Nucleic Acid Amplification Test (NAAT) results, which include reverse transcriptase-polymerase chain reaction (RT-PCR) tests from a voluntary, sentinel network of participating laboratories in the United States, including clinical, public health and commercial laboratories (https://www.cdc.gov/surveillance/nrevss/labs/index.html). \n\nThese data exclude antigen, antibody, and at-home test results. \n\nAll data are provisional and subject to change. Reporting is less complete for the past 1 week, and more complete (>90%) for the period 2 weeks earlier. \n\nThere are data from all states across the 10 HHS regions. Because the data are from a sentinel network of laboratories, however, results may vary geographically. The data do not include all test results within a jurisdiction and therefore do not reflect all SARS-CoV-2 NAATs administered in the United States. \n\nPercent positivity is one of the surveillance metrics used to monitor COVID-19 transmission over time and by area. Percent positivity is calculated by dividing the number of positive NAATs by the total number of NAATs administered, then multiplying by 100 [(# of positive NAAT tests / total NAAT tests) x 100].\n\nThe data represent laboratory tests performed, not individual (deduplicated) results in people. In the table and upon hovering on the map, the total test counts in the data reflect the latest data reported from NREVSS laboratories and may not match the data presented by various jurisdictions.\n\nOn May 11, 2023, CDC discontinued utilizing the COVID electronic laboratory reporting (CELR) platform as the primary laboratory source of COVID-19 results. These data are archived at health.data.gov.\n\nFor more information about NREVSS, please see: https://www.cdc.gov/surveillance/nrevss/",
-            "title": "Percent Positivity of COVID-19 Nucleic Acid Amplification Tests by HHS Region, National Respiratory and Enteric Virus Surveillance System",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38083,74 +37993,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gvsb-yw6g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gvsb-yw6g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gvsb-yw6g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gvsb-yw6g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gvsb-yw6g",
+            "issued": "2023-06-06",
+            "keyword": [
+                "covid19",
+                "nrevss",
+                "test"
+            ],
+            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#trends",
+            "language": [
+                "English"
+            ],
+            "modified": "2025-01-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDC"
+            },
+            "references": [
+                "https://covid.cdc.gov/covid-data-tracker/"
+            ],
             "spatial": "US",
-            "accrualPeriodicity": "Weekly",
+            "temporal": "Data from 2020-03-14 to present (posted starting 2023-06-06)",
             "theme": [
                 "Laboratory Surveillance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Percent Positivity of COVID-19 Nucleic Acid Amplification Tests by HHS Region, National Respiratory and Enteric Virus Surveillance System"
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
-                "name": "CDC"
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
@@ -38158,44 +38063,102 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gxj9-t96f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gxj9-t96f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gxj9-t96f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "CDC"
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
+                    "describedBy": "https://data.cdc.gov/api/views/gypc-kpgn/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/gypc-kpgn/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/gypc-kpgn/columns.xml",
+                    "describedByType": "application/xml",
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
@@ -38226,95 +38189,38 @@
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
-                "name": "National Center for Health Statistics"
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
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/gypc-kpgn/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/gypc-kpgn/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gypc-kpgn/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/gypc-kpgn/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
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
-            "landingPage": "https://data.cdc.gov/d/gz3p-wzwf",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "anaplasma phagocytophilum",
-                "ehrlichia chaffeensis",
-                "ehrlichiosis and anaplasmosis",
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
-            "identifier": "https://data.cdc.gov/api/views/gz3p-wzwf",
             "description": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. \r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n *Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Please refer to the MMWR publication for weekly updates to the footnote for this condition.",
-            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38322,61 +38228,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gz3p-wzwf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gz3p-wzwf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gz3p-wzwf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/gz3p-wzwf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gz3p-wzwf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gz3p-wzwf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/gz3p-wzwf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/gz3p-wzwf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/gz3p-wzwf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/gz3p-wzwf",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "anaplasma phagocytophilum",
+                "ehrlichia chaffeensis",
+                "ehrlichiosis and anaplasmosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/gz3p-wzwf",
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
+            "title": "NNDSS - Table II. Ehrlichiosis and Anaplasmosis"
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
-                "name": "data.cdc.gov"
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
@@ -38384,71 +38296,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h28b-t43q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h28b-t43q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h28b-t43q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/h28b-t43q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h28b-t43q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h28b-t43q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h28b-t43q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h28b-t43q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h28b-t43q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "Population-Weighted Ultraviolet Irradiance, 2004-2015"
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
-            "modified": "2024-08-23",
-            "references": [
-                "https://www.cdc.gov/places/measure-definitions/index.html"
-            ],
-            "keyword": [
-                "behaviors",
-                "brfss",
-                "county",
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
-            "identifier": "https://data.cdc.gov/api/views/h3ej-a9ec",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
             "description": "This dataset contains model-based county estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. This dataset includes estimates for 36 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2021 or 2020 county population estimate data, and American Community Survey 2017\u20132021, or 2016\u20132020 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. More information about the methodology can be found at  www.cdc.gov/places.",
-            "title": "PLACES: Local Data for Better Health, County Data 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38456,66 +38359,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h3ej-a9ec/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h3ej-a9ec/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h3ej-a9ec/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/h3ej-a9ec/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h3ej-a9ec/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h3ej-a9ec/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h3ej-a9ec/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h3ej-a9ec/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h3ej-a9ec/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
+            "identifier": "https://data.cdc.gov/api/views/h3ej-a9ec",
+            "issued": "2024-07-15",
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "county",
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
+            "title": "PLACES: Local Data for Better Health, County Data 2023 release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/h3kf-bqpq",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2022-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-11",
-            "keyword": [
-                "2022",
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
-            "identifier": "https://data.cdc.gov/api/views/h3kf-bqpq",
             "description": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38523,49 +38431,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h3kf-bqpq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h3kf-bqpq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h3kf-bqpq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h3kf-bqpq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h3kf-bqpq",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
+                "chancroid",
+                "chlamydia trachomatis infection",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/h3kf-bqpq",
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
+            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/h3my-dzpj",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/h3my-dzpj",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38573,62 +38494,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h3my-dzpj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h3my-dzpj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h3my-dzpj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/h3my-dzpj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h3my-dzpj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h3my-dzpj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h3my-dzpj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h3my-dzpj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h3my-dzpj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/h3my-dzpj",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/h3my-dzpj",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/h4pd-hu6x",
             "description": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38636,69 +38544,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h4pd-hu6x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h4pd-hu6x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h4pd-hu6x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/h4pd-hu6x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h4pd-hu6x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h4pd-hu6x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h4pd-hu6x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h4pd-hu6x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h4pd-hu6x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "data.cdc.gov"
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
@@ -38706,45 +38610,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h4wb-nae4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h4wb-nae4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h4wb-nae4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/h4wb-nae4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h4wb-nae4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h4wb-nae4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h4wb-nae4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h4wb-nae4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h4wb-nae4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h4wb-nae4",
+            "issued": "2019-04-24",
+            "keyword": [
+                "2019",
+                "age <5 years",
+                "all ages",
+                "all serotypes",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "invasive disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "serotype b",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/h4wb-nae4",
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
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease (age <5 years), Serotype b"
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
-            "temporal": "2021/2022",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-23",
-            "references": [
-                "https://www.cdc.gov/nchs/data/datalinkage/NAMCS-HC-Codebook-Mortality-Variables.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 9) here: https://www.cdc.gov/nchs/data/datalinkage/NAMCS-HC-NDI-Methodology-Analytic-Considerations.pdf",
+            "describedByType": "application/pdf",
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the 2021 National Ambulatory Medical Care Survey (NAMCS) by augmenting it with mortality data from the National Death Index (NDI). Linkage of NAMCS data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h5rx-ppfj",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "issued": "2024-10-23",
             "keyword": [
                 "linked ndi data",
                 "namcs",
@@ -38753,63 +38693,37 @@
                 "sdoh-source-of-health-care",
                 "sdoh-use-of-health-care"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NCHS Data Linkage Program",
-                "hasEmail": "mailto:DataLinkage@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/namcs-linkage.htm",
+            "modified": "2024-10-23",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/h5rx-ppfj",
-            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the 2021 National Ambulatory Medical Care Survey (NAMCS) by augmenting it with mortality data from the National Death Index (NDI). Linkage of NAMCS data with the NDI mortality data provides the opportunity to conduct a vast array of outcome studies designed to investigate the association of a wide variety of health factors with mortality.",
-            "title": "National Ambulatory Medical Care Survey (NAMCS) Linked to National Death Index (NDI) Data",
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
+                "https://www.cdc.gov/nchs/data/datalinkage/NAMCS-HC-Codebook-Mortality-Variables.pdf"
             ],
-            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 9) here: https://www.cdc.gov/nchs/data/datalinkage/NAMCS-HC-NDI-Methodology-Analytic-Considerations.pdf",
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
@@ -38817,90 +38731,84 @@
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
             "accessLevel": "restricted public",
-            "landingPage": "https://wwwdev.cdc.gov/nchs/rss/rapid-surveys-system.html",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:20"
             ],
-            "rights": "Rapid Surveys questionnaires are composed of questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes. Each round of Rapid Surveys has at least 4,000 adult participants. Each file includes questionnaire data, limited paradata, some demographic and characteristic data, and sample weights. The datafiles include records on both survey responders, partial responders, and sampled non-responders.",
-            "issued": "2024-07-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2023",
-            "modified": "2024-10-18",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/h6vx-wafp",
             "description": "The NCHS Rapid Surveys System includes questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes.",
-            "title": "NCHS Rapid Survey Systems Restricted Use File",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cdc.gov/rdc/b1datatype/rdcrss.htm",
-                    "description": "The NCHS Rapid Surveys System is a platform for CDC to provide reliable, actionable data of known quality to public health experts, government officials, and community leaders. The Rapid Surveys System includes probability-sampled commercial online surveys. Data are collected quarterly from a minimum of 4,000 adult participants from two commercial panels: AmeriSpeak (conducted by NORC at the University of Chicago) and KnowledgePanel (conducted by Ipsos). Results from commercial online surveys are available faster than from traditional population health surveys, thus enabling timelier access to relevant health-related data. Rapid Surveys questionnaires are composed of questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes. Each round of Rapid Surveys has at least 4,000 adult participants. Each file includes questionnaire data, limited paradata, some demographic and characteristic data, and sample weights. The datafiles include records on both survey responders, partial responders, and sampled non-responders.",
                     "@type": "dcat:Distribution",
+                    "description": "The NCHS Rapid Surveys System is a platform for CDC to provide reliable, actionable data of known quality to public health experts, government officials, and community leaders. The Rapid Surveys System includes probability-sampled commercial online surveys. Data are collected quarterly from a minimum of 4,000 adult participants from two commercial panels: AmeriSpeak (conducted by NORC at the University of Chicago) and KnowledgePanel (conducted by Ipsos). Results from commercial online surveys are available faster than from traditional population health surveys, thus enabling timelier access to relevant health-related data. Rapid Surveys questionnaires are composed of questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes. Each round of Rapid Surveys has at least 4,000 adult participants. Each file includes questionnaire data, limited paradata, some demographic and characteristic data, and sample weights. The datafiles include records on both survey responders, partial responders, and sampled non-responders.",
+                    "downloadURL": "https://www.cdc.gov/rdc/b1datatype/rdcrss.htm",
+                    "mediaType": "text/html",
                     "title": "NCHS Rapid Surveys System Restricted Use File"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.cdc.gov/api/views/h6vx-wafp",
+            "issued": "2024-07-17",
+            "keyword": [
+                "dhis",
+                "nchs"
+            ],
+            "landingPage": "https://wwwdev.cdc.gov/nchs/rss/rapid-surveys-system.html",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-10-18",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "rights": "Rapid Surveys questionnaires are composed of questions sponsored by CDC programs and other partners to address time-sensitive data needs, public health attitudes or behaviors, and developmental work to improve concept measurement and inform future question design. It also includes standard variables used for sample weighting and calibration, as well as selected portions of existing content from NCHS surveys (such as the National Health Interview Survey) to compare panel estimates to these benchmarks, assess the fitness-for-use of the panel survey data, and for other methodological purposes. Each round of Rapid Surveys has at least 4,000 adult participants. Each file includes questionnaire data, limited paradata, some demographic and characteristic data, and sample weights. The datafiles include records on both survey responders, partial responders, and sampled non-responders.",
+            "spatial": "United States",
+            "temporal": "2023",
             "theme": [
                 "National Center for Health Statistics"
-            ]
+            ],
+            "title": "NCHS Rapid Survey Systems Restricted Use File"
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
-                "name": "data.cdc.gov"
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
@@ -38908,61 +38816,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h7pm-wmjc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h7pm-wmjc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h7pm-wmjc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "modified": "2025-01-13",
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
+            "title": "Vaccination Coverage among Pregnant Women"
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
-                "sdoh-use-of-health-care",
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
-            "identifier": "https://data.cdc.gov/api/views/h7xa-837u",
             "description": "To rapidly monitor recent changes in the use of telemedicine, the National Center for Health Statistics (NCHS) and the Health Resources and Services Administration\u2019s Maternal and Child Health Bureau (HRSA MCHB) partnered with the Census Bureau on an experimental data system called the Household Pulse Survey. This 20-minute online survey was designed to complement the ability of the federal statistical system to rapidly respond and provide relevant information about the impact of the coronavirus pandemic in the U.S.\n\nThe U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of the COVID-19 pandemic on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, sex, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions.",
-            "title": "Telemedicine Use in the Last 4 Weeks",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38970,61 +38883,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h7xa-837u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h7xa-837u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/h7xa-837u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/h7xa-837u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "US",
+            "identifier": "https://data.cdc.gov/api/views/h7xa-837u",
+            "issued": "2021-04-27",
+            "keyword": [
+                "covid-19",
+                "sdoh-use-of-health-care",
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
+                "name": "National Center for Health Statistics"
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
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/h98p-htn6",
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
-                "name": "data.cdc.gov"
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
@@ -39032,34 +38950,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/h98p-htn6",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/h98p-htn6",
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
+            "title": "Effects of Welding Fume Exposure on Human Placental Cells"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/ha59-j5yk",
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Division of Field Studies and Evaluation, Hazard Evaluation and Technical Assistance Branch",
                 "hasEmail": "mailto:HHERequestHelp@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/ha59-j5yk",
             "description": "The April 20, 2010, explosion and collapse of the BP Deepwater Horizon oil platform in the Gulf of Mexico resulted in the release of millions of barrels of oil into Gulf waters. The response to this disaster involved the efforts of tens of thousands of workers in a variety of capacities across Louisiana, Mississippi, Alabama, Florida, Texas, and in the Gulf of Mexico itself. The diverse work included oil and tar ball removal from beaches, oil skimming and booming near shores, burning of surface oil near the source of the oil release, surface application of dispersant by vessels and aircraft, and containment and recovery work on vessels at the release site. The nature of these activities raised concerns about potential occupational exposures to chemical and physical hazards and mental stressors.\n\nNIOSH investigators conducted health hazard evaluations (HHEs) of Deepwater Horizon Response onshore and offshore workers. The goals of the NIOSH HHE assessments were to describe acute health effects, evaluate occupational exposures in qualitative or quantitative assessments, and generate hypotheses regarding symptoms potentially related to work activities. Environmental air samples were collected in support of the goals.\n\nNIOSH investigators conducted the following exposure evaluations:\n\n- We conducted evaluations on board vessels releasing dispersant. These vessels were deployed to perform small\u2010scale releases of dispersant in an area with surface oil contamination.\n- We assessed exposures during in\u2010situ (i.e., on site) burns of surface oil.\n- We assessed exposures on fishing and shrimping trawlers in the Vessels of Opportunity (VoO) program that were assigned to remove surface oil by booming and skimming.\n- We assessed exposures aboard vessels located at the Deepwater Horizon incident site.\n- We assessed exposures during boom and vessel decontamination operations.",
-            "title": "Deepwater Horizon Response Air Sampling Data",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39067,38 +38985,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ha59-j5yk",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.cdc.gov/d/ha59-j5yk",
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
+            "title": "Deepwater Horizon Response Air Sampling Data"
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
-                "name": "data.cdc.gov"
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
@@ -39106,67 +39020,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/haed-k2ka/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/haed-k2ka/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/haed-k2ka/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/haed-k2ka/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/haed-k2ka/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/haed-k2ka/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/haed-k2ka/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/haed-k2ka/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/haed-k2ka/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/haed-k2ka",
+            "issued": "2016-09-26",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/haed-k2ka",
+            "modified": "2016-09-26",
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
+            "title": "Occupant and Alcohol-Impaired Driving Deaths in States, 2005-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hatw-7gqy",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2018-01-04",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-04",
-            "keyword": [
-                "2017",
-                "all serogroups",
-                "meningococcal disease (neisseria meningitidis)",
-                "mmwr",
-                "mumps",
-                "nedss",
-                "netss",
-                "nndss",
-                "pertussis",
-                "wonder"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CC INFO",
                 "hasEmail": "mailto:cdcinfo@cdc.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hatw-7gqy",
             "description": "NNDSS - Table II. Meningococcal to Pertussis - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Data for meningococcal disease, invasive caused by serogroups ACWY, serogroup B, other serogroups, and unknown serogroups are available in Table I.",
-            "title": "NNDSS - Table II. Meningococcal to Pertussis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39174,59 +39080,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hatw-7gqy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hatw-7gqy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hatw-7gqy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hatw-7gqy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hatw-7gqy",
+            "issued": "2018-01-04",
+            "keyword": [
+                "2017",
+                "all serogroups",
+                "meningococcal disease (neisseria meningitidis)",
+                "mmwr",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "pertussis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hatw-7gqy",
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
+            "title": "NNDSS - Table II. Meningococcal to Pertussis"
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
-                "name": "data.cdc.gov"
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
@@ -39234,66 +39148,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hauf-e9a4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hauf-e9a4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hauf-e9a4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hauf-e9a4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hauf-e9a4",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hauf-e9a4",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 3 - Philadelphia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hbbg-vj7f",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/hbbg-vj7f",
             "description": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39301,73 +39208,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hbbg-vj7f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hbbg-vj7f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hbbg-vj7f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hbbg-vj7f",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "all serogroups",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "serogroup b",
+                "serogroups acwy",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hbbg-vj7f",
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
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2020-04-02",
-            "@type": "dcat:Dataset",
-            "temporal": "2019/2020",
-            "modified": "2022-04-01",
-            "keyword": [
-                "age",
-                "age group",
-                "all causes",
-                "coronavirus",
-                "covid-19",
-                "deaths",
-                "influenza",
-                "mortality",
-                "nchs",
-                "pneumonia",
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
-                "name": "National Center for Health Statistics"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hc4f-j6nb",
             "description": "This dataset is no longer updated.  Please see the following datasets for recent data:\n\nProvisional COVID-19 Deaths by Week (https://data.cdc.gov/dataset/Provisional-COVID-19-Death-Counts-by-Week-Ending-D/r8kw-7aab/)\n\nProvisional COVID-19 Deaths by Sex, Age, and State (https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-Sex-Age-and-S/9bhg-hcku)",
-            "title": "Provisional Death Counts for Coronavirus Disease (COVID-19)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39375,58 +39276,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hc4f-j6nb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hc4f-j6nb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hc4f-j6nb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hc4f-j6nb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hc4f-j6nb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hc4f-j6nb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hc4f-j6nb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hc4f-j6nb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hc4f-j6nb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States, Puerto Rico",
+            "identifier": "https://data.cdc.gov/api/views/hc4f-j6nb",
+            "issued": "2020-04-02",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "influenza",
+                "mortality",
+                "nchs",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
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
+            "spatial": "United States, Puerto Rico",
+            "temporal": "2019/2020",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Provisional Death Counts for Coronavirus Disease (COVID-19)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/hcxx-dqtx",
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
-                "name": "data.cdc.gov"
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
@@ -39434,58 +39352,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hcxx-dqtx",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/hcxx-dqtx",
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
+            "title": "Resolution of Pulmonary Inflammation Induced by Carbon Nanotubes and Fullerenes in Mice: Role of Macrophage Polarization"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2024-04-11",
-            "temporal": "1997/2019",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-30",
-            "keyword": [
-                "adults",
-                "american indian or alaska native",
-                "asian",
-                "black or african american",
-                "children and adolescents",
-                "education",
-                "female",
-                "functional limitation status",
-                "health insurance",
-                "hispanic or latino",
-                "male",
-                "medicaid",
-                "metropolitan and nonmetropolitan",
-                "mexican",
-                "multiple race",
-                "native hawaiian or other pacific islander",
-                "poverty",
-                "region",
-                "rural population",
-                "urban population",
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
-            "identifier": "https://data.cdc.gov/api/views/hdja-ybdg",
             "description": "Data on Medicaid coverage among people under age 65, in the United States, by selected population characteristics. Data from Health, United States. SOURCE: National Center for Health Statistics, National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
-            "title": "DQS Medicaid coverage among persons under age 65, by selected characteristics: United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39493,47 +39388,92 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hdja-ybdg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hdja-ybdg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hdja-ybdg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hdja-ybdg",
+            "issued": "2024-04-11",
+            "keyword": [
+                "adults",
+                "american indian or alaska native",
+                "asian",
+                "black or african american",
+                "children and adolescents",
+                "education",
+                "female",
+                "functional limitation status",
+                "health insurance",
+                "hispanic or latino",
+                "male",
+                "medicaid",
+                "metropolitan and nonmetropolitan",
+                "mexican",
+                "multiple race",
+                "native hawaiian or other pacific islander",
+                "poverty",
+                "region",
+                "rural population",
+                "urban population",
+                "white"
+            ],
+            "landingPage": "https://www.cdc.gov/nchs/hus",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-10-30",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
+            },
+            "temporal": "1997/2019",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "DQS Medicaid coverage among persons under age 65, by selected characteristics: United States"
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
@@ -39544,69 +39484,39 @@
                 "surveillance",
                 "survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:NHANESGenetics@cdc.gov"
-            },
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/biospecimens/dnaspecimens.htm",
+            "modified": "2023-03-27",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
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
-                "hispanic women",
-                "nchs",
-                "pregnancy rate",
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
-            "identifier": "https://data.cdc.gov/api/views/hdy7-e2a3",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "description": "https://www.cdc.gov/nchs/data-visualization/natality-trends/index.htm",
-            "title": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010",
-            "isPartOf": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39614,69 +39524,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hdy7-e2a3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hdy7-e2a3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hdy7-e2a3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "50 states and District of Columbia",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "identifier": "https://data.cdc.gov/api/views/hdy7-e2a3",
+            "isPartOf": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010",
+            "issued": "2015-12-02",
+            "keyword": [
+                "hispanic women",
+                "nchs",
+                "pregnancy rate",
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
+            "rights": "public",
+            "spatial": "50 states and District of Columbia",
+            "temporal": "1990/2010",
             "theme": [
                 "NCHS"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "accrualPeriodicity": "Weekly",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2025-01-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2024-2025",
-            "modified": "2025-01-31",
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
-                "name": "National Center for Immunization and Respiratory Diseases (NCIRD)"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hea5-6w9c",
             "description": "\u2022Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Retail Pharmacies and Physicians\u2019 Medical Offices, Adults 60 to 74 Years and 75 Years and Older, United States  \n\n\u2022 Estimated Number of RSV vaccinations among adults 60 years and older is assessed through IQVIA (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, food stores, and independent pharmacies) and physician medical offices.",
-            "title": "Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Retail Pharmacies and Physicians\u2019 Medical Offices, Adults 60 to 74 Years and 75 years and older, United States",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39684,71 +39595,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hea5-6w9c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hea5-6w9c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hea5-6w9c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hea5-6w9c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hea5-6w9c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hea5-6w9c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hea5-6w9c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hea5-6w9c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hea5-6w9c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States- National",
+            "identifier": "https://data.cdc.gov/api/views/hea5-6w9c",
+            "issued": "2025-01-28",
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
+            "temporal": "2024-2025",
             "theme": [
                 "Vaccinations"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Retail Pharmacies and Physicians\u2019 Medical Offices, Adults 60 to 74 Years and 75 years and older, United States"
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
-                "name": "data.cdc.gov"
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
@@ -39756,64 +39664,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hf2a-3ebq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hf2a-3ebq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hf2a-3ebq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hf2a-3ebq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hf2a-3ebq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hf2a-3ebq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hf2a-3ebq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hf2a-3ebq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hf2a-3ebq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "data.cdc.gov"
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
-                "name": "data.cdc.gov"
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
@@ -39821,63 +39735,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hget-9fst/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hget-9fst/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hget-9fst/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hget-9fst/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hget-9fst",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hget-9fst",
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
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 2 - New York"
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
-                "legislation",
-                "osh",
-                "policy",
-                "state system",
-                "tobacco",
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
-            "identifier": "https://data.cdc.gov/api/views/hgv5-3wrn",
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Youth-Access/hgv5-3wrn",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation\u2014Youth Access. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies.  Data are reported on a quarterly basis. Data include information related to restrictions, enforcement and penalties associated with the sale of cigarettes to youth through retail sales and vending machines.",
-            "title": "CDC STATE System Tobacco Legislation - Youth Access",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39885,65 +39796,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hgv5-3wrn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hgv5-3wrn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hgv5-3wrn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hgv5-3wrn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hgv5-3wrn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hgv5-3wrn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hgv5-3wrn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hgv5-3wrn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hgv5-3wrn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Youth-Access/hgv5-3wrn",
+            "identifier": "https://data.cdc.gov/api/views/hgv5-3wrn",
+            "issued": "2023-07-18",
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "state system",
+                "tobacco",
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
             "theme": [
                 "Legislation"
-            ]
+            ],
+            "title": "CDC STATE System Tobacco Legislation - Youth Access"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cdc.gov/oralhealth/about/index.htm",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-27",
-            "keyword": [
-                "community water fluoridation",
-                "county level",
-                "fluoridation",
-                "oral health",
-                "state level",
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
-            "identifier": "https://data.cdc.gov/api/views/hgyx-uuxz",
             "description": "State, 2016 \u20132020; County, 2020. The report includes both state and county level water fluoridation data generated from the Water Fluoridation Reporting System (WFRS). State level statistics include data from the biennial report originally published at https://www.cdc.gov/fluoridation/statistics/reference_stats.htm. State and county data include percentage of people, number of people, and number of water systems receiving fluoridated water. County level data is not displayed for all states. Participation in sharing county level data is voluntary and state programs determine if data will be shown.",
-            "title": "Community Water Fluoridation \u2013 State and County Level Statistics",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39951,56 +39861,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hgyx-uuxz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hgyx-uuxz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hgyx-uuxz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hgyx-uuxz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hgyx-uuxz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hgyx-uuxz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hgyx-uuxz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hgyx-uuxz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hgyx-uuxz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hgyx-uuxz",
+            "issued": "2023-07-18",
+            "keyword": [
+                "community water fluoridation",
+                "county level",
+                "fluoridation",
+                "oral health",
+                "state level",
+                "wfrs"
+            ],
+            "landingPage": "https://www.cdc.gov/oralhealth/about/index.htm",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
             "theme": [
                 "Oral Health"
-            ]
+            ],
+            "title": "Community Water Fluoridation \u2013 State and County Level Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/hh8a-ys2f",
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
-            "identifier": "https://data.cdc.gov/api/views/hh8a-ys2f",
             "description": "The association between human respiratory disease transmission by respiratory droplets and aerosols is well established for several known pathogens.1 Given that the average individual spends > 90% of their day indoors, there has been intense focus on factors associated with indoor transmission. To minimize exposure risks, the Centers for Disease Control and Prevention (CDC) recommends behavioral and personal protective equipment mitigation strategies to limit COVID-19 transmission, including wearing masks, maintaining physical distances of  \u2265 1.8 m, and avoiding crowded indoor and outdoor spaces. As such, the current investigation examines the combined effect of physical distancing, universal masking, and ventilation on exposure to airborne particles generated during breathing and coughing within a controlled indoor environment. The results of this investigation quantitatively examine the contribution of the matrix of controls employed and provides guidance on respiratory disease mitigation strategies within the indoor environment.",
-            "title": "Reduction of exposure to simulated respiratory aerosols using ventilation, physical distancing, and universal masking",
-            "programCode": [
-                "009:034"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40008,42 +39926,35 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hh8a-ys2f",
+            "issued": "2024-11-15",
+            "landingPage": "https://data.cdc.gov/d/hh8a-ys2f",
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
+            "title": "Reduction of exposure to simulated respiratory aerosols using ventilation, physical distancing, and universal masking"
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
@@ -40051,66 +39962,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hhew-mxbt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hhew-mxbt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hhew-mxbt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hhew-mxbt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hhew-mxbt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hhew-mxbt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hhew-mxbt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hhew-mxbt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hhew-mxbt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/hhvg-83jq",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-12-13",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "antibodies",
-                "covid-19",
-                "immunoassays",
-                "ncird-corvd",
-                "neutralization assay",
-                "sars-cov-2",
-                "serological tests"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CDC-INFO",
                 "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hhvg-83jq",
             "description": "Severe acute respiratory syndrome (SARS) coronavirus 2 (SARS-CoV-2) is a novel human coronavirus that was identified in 2019. SARS-CoV-2 infection results in an acute, severe respiratory disease called coronavirus disease 2019 (COVID-19).  The emergence and rapid spread of SARS-CoV-2 has led to a global public health crisis, which continues to affect populations across the globe. Real time reverse transcription polymerase chain reaction (rRT-PCR) is the reference standard test for COVID-19 diagnosis. Serological tests are valuable tools for serosurveillance programs and establishing correlates of protection from disease. This study evaluated the performance of one in-house enzyme linked immunosorbent assay (ELISA) utilizing the pre-fusion stabilized ectodomain of SARS-CoV-2 spike (S), two commercially available chemiluminescence assays Ortho VITROS Immunodiagnostic Products Anti-SARS-CoV-2 Total Reagent Pack and Abbott SARS-CoV-2 IgG assay and one commercially available Surrogate Virus Neutralization Test (sVNT), GenScript USA Inc., cPass SARS-CoV-2 Neutralization Antibody Detection Kit for the detection of SARS-CoV-2 specific antibodies.  Using a panel of rRT-PCR confirmed COVID-19 patients\u2019 sera and a negative control group as a reference standard, all three immunoassays demonstrated high comparable positivity rates and low discordant rates.  All three immunoassays were highly sensitive with estimated sensitivities ranging from 95.4%-96.6%. ROC curve analysis indicated that all three immunoassays had high diagnostic accuracies with area under the curve (AUC) values ranging from 0.9698-0.9807. High positive correlation was demonstrated among the conventional microneutralization test (MNT) titers and the sVNT inhibition percent values.  Our study indicates that independent evaluations are necessary to optimize the overall utility and the interpretation of the results of serological tests.  Overall, we demonstrate that all serological tests evaluated in this study are suitable for the detection of SARS-CoV-2 antibodies.",
-            "title": "Examination of SARS-CoV-2 serological test results from multiple commercial and laboratory platforms with an in-house serum panel",
-            "programCode": [
-                "009:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40118,64 +40027,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hhvg-83jq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hhvg-83jq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hhvg-83jq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hhvg-83jq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hhvg-83jq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hhvg-83jq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hhvg-83jq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hhvg-83jq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hhvg-83jq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hhvg-83jq",
+            "issued": "2023-12-13",
+            "keyword": [
+                "antibodies",
+                "covid-19",
+                "immunoassays",
+                "ncird-corvd",
+                "neutralization assay",
+                "sars-cov-2",
+                "serological tests"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hhvg-83jq",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "009:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
             "theme": [
                 "Coronavirus and Other Respiratory Viruses"
-            ]
+            ],
+            "title": "Examination of SARS-CoV-2 serological test results from multiple commercial and laboratory platforms with an in-house serum panel"
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
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Preemption-Su/hj2x-85ya",
             "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation - Preemption. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to summary state preemption of more stringent or differing local laws on smokefree indoor air, youth access and licensure.",
-            "title": "CDC STATE System Tobacco Legislation - Preemption Summary",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40183,67 +40094,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hj2x-85ya/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hj2x-85ya/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hj2x-85ya/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/hjax-h34q",
             "bureauCode": [
                 "009:00"
             ],
-            "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
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
-            "identifier": "https://data.cdc.gov/api/views/hjax-h34q",
             "description": "NNDSS - TABLE 1V. Malaria to Measles, Imported - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1V. Malaria to Measles, Imported",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40251,41 +40159,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hjax-h34q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hjax-h34q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hjax-h34q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hjax-h34q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hjax-h34q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hjax-h34q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hjax-h34q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hjax-h34q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hjax-h34q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hjax-h34q",
+            "issued": "2019-04-26",
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
+            "landingPage": "https://data.cdc.gov/d/hjax-h34q",
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
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Imported"
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
+                    "describedBy": "https://data.cdc.gov/api/views/hk9y-quqm/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/hk9y-quqm/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.cdc.gov/api/views/hk9y-quqm/columns.xml",
+                    "describedByType": "application/xml",
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
@@ -40325,94 +40288,36 @@
                 "united states",
                 "yearly"
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
-            "identifier": "https://data.cdc.gov/api/views/hk9y-quqm",
-            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis dataset shows health conditions and contributing causes mentioned in conjunction with deaths involving coronavirus disease 2019 (COVID-19) by age group and jurisdiction of occurrence.\n\n2022 and 2023 data are provisional. Estimates for 2020 and 2021 are based on final data.",
-            "title": "Conditions Contributing to COVID-19 Deaths, by State and Age, Provisional 2020-2023",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-09-27",
             "programCode": [
                 "009:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hk9y-quqm/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hk9y-quqm/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hk9y-quqm/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/hk9y-quqm/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2020/2023",
             "theme": [
                 "NCHS"
-            ]
+            ],
+            "title": "Conditions Contributing to COVID-19 Deaths, by State and Age, Provisional 2020-2023"
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
-                "name": "National Center for Health Statistics"
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
@@ -40420,68 +40325,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hkhc-f7hg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hkhc-f7hg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hkhc-f7hg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hkhc-f7hg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
-            "landingPage": "https://data.cdc.gov/d/hkr7-mcee",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/hkr7-mcee",
             "description": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40489,64 +40397,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hkr7-mcee/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hkr7-mcee/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hkr7-mcee/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hkr7-mcee/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hkr7-mcee/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hkr7-mcee/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hkr7-mcee/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hkr7-mcee/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hkr7-mcee/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hkr7-mcee",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "arboviral diseases",
+                "babesiosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "western equine encephalitis virus disease",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hkr7-mcee",
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
+            "title": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis"
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
@@ -40554,72 +40463,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hksd-2xuw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hksd-2xuw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hksd-2xuw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "identifier": "https://data.cdc.gov/api/views/hky2-3tpn",
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
             "description": "This dataset contains model-based census tract level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the census tract 2015 boundary file in a GIS system to produce maps for 36 measures at the census tract level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
-            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2023 release",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40627,68 +40530,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hky2-3tpn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hky2-3tpn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hky2-3tpn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
+            "identifier": "https://data.cdc.gov/api/views/hky2-3tpn",
+            "issued": "2024-07-15",
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
+            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2023 release"
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
-                "name": "Environmental Public Health Tracking"
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
@@ -40696,62 +40602,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm3s-vk7u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hm3s-vk7u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hm3s-vk7u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm3s-vk7u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hm3s-vk7u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hm3s-vk7u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hm3s-vk7u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hm3s-vk7u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hm3s-vk7u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
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
+            "modified": "2022-09-09",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Environmental Public Health Tracking"
+            },
+            "theme": [
                 "Policy Surveillance"
-            ]
+            ],
+            "title": "U.S. State and Territorial Stay-At-Home Orders: March 15, 2020 \u2013 May 31, 2021 by County by Day"
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
-            "modified": "2025-01-31",
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
-                "name": "CDC"
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
@@ -40759,72 +40671,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hmye-mqgq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hmye-mqgq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hmye-mqgq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hmye-mqgq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hmye-mqgq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hmye-mqgq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hmye-mqgq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hmye-mqgq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hmye-mqgq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "Preliminary Estimates of Cumulative RSV-associated Hospitalizations by Week for 2024-2025 season"
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
-                "name": "National Center for Health Statistics"
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
@@ -40832,73 +40737,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hmz2-vwda/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hmz2-vwda/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hmz2-vwda/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hmz2-vwda/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hmz2-vwda/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hmz2-vwda/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hmz2-vwda/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hmz2-vwda/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hmz2-vwda/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "National Center for Health Statistics"
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
@@ -40906,59 +40810,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hn4x-zwk7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hn4x-zwk7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hn4x-zwk7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hn4x-zwk7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "Nutrition, Physical Activity, and Obesity - Behavioral Risk Factor Surveillance System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:00"
             ],
-            "landingPage": "https://data.cdc.gov/d/hp6w-4ap6",
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
-                "name": "data.cdc.gov"
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
@@ -40966,62 +40881,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hp6w-4ap6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hp6w-4ap6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hp6w-4ap6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/hp6w-4ap6",
+            "issued": "2015-06-08",
+            "keyword": [
+                "youth risk behavior risk surveillance school-based surveillance"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hp6w-4ap6",
+            "modified": "2015-08-27",
+            "programCode": [
+                "009:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.cdc.gov"
+            },
+            "title": "YRBS State Tobacco Variables  2013 - v2"
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
-                "name": "data.cdc.gov"
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
@@ -41029,68 +40938,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hrdz-jaxc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hrdz-jaxc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hrdz-jaxc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hrdz-jaxc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "laboratory",
+                "ncird-corvd"
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
+                "name": "data.cdc.gov"
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
-            "landingPage": "https://data.cdc.gov/d/hs59-amfp",
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
-            "identifier": "https://data.cdc.gov/api/views/hs59-amfp",
             "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 In previous years, cases were reported as Salmonellosis. Beginning in January 2019, cases began to be reported as Salmonella Paratyphi infection.\r\n\u00b6 In previous years, cases were reported as typhoid fever. Beginning in January 2019, cases began to be reported as Salmonella Typhi infection.\r\n** In previous years, cases were reported as Salmonellosis (excluding paratyphoid fever and typhoid fever). Beginning in January 2019, cases began to be reported as Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection).",
-            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41098,64 +41006,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hs59-amfp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hs59-amfp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hs59-amfp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hs59-amfp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hs59-amfp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hs59-amfp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hs59-amfp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hs59-amfp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hs59-amfp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "theme": [
-                "NNDSS"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/ht29-hwxw",
-            "bureauCode": [
-                "009:00"
-            ],
+            "identifier": "https://data.cdc.gov/api/views/hs59-amfp",
             "issued": "2019-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-30",
             "keyword": [
                 "2019",
                 "nedss",
                 "netss",
                 "nndss",
-                "rubella",
-                "rubella congenital syndrome",
+                "salmonella paratyphi infection",
+                "salmonella typhi infection",
+                "salmonellosis (excluding salmonella typhi infection and salmonella paratyphi infection)",
                 "wonder"
             ],
+            "landingPage": "https://data.cdc.gov/d/hs59-amfp",
+            "modified": "2019-05-30",
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
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)"
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
-            "identifier": "https://data.cdc.gov/api/views/ht29-hwxw",
             "description": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome  - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41163,49 +41072,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ht29-hwxw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ht29-hwxw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ht29-hwxw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ht29-hwxw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ht29-hwxw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ht29-hwxw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ht29-hwxw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ht29-hwxw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ht29-hwxw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/ht29-hwxw",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "rubella congenital syndrome",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/ht29-hwxw",
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
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/htq2-rqve",
-            "issued": "2024-07-23",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Disability and Health Data System (CDC)",
                 "hasEmail": "mailto:no-reply@data.cdc.gov"
             },
-            "identifier": "https://data.cdc.gov/api/views/htq2-rqve",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.cdc.gov"
-            },
             "description": "",
-            "title": "dhds_dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41213,65 +41134,50 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/htq2-rqve/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/htq2-rqve/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/htq2-rqve/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/htq2-rqve/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/htq2-rqve/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/htq2-rqve/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/htq2-rqve/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/htq2-rqve/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/htq2-rqve/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.cdc.gov/api/views/htq2-rqve",
+            "issued": "2024-07-23",
+            "landingPage": "https://data.cdc.gov/d/htq2-rqve",
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
-                "name": "CDC"
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
@@ -41279,70 +41185,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hwk8-wu83/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hwk8-wu83/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hwk8-wu83/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "name": "CDC"
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
-                "name": "data.cdc.gov"
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
@@ -41350,65 +41256,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hwyq-75wu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hwyq-75wu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyq-75wu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hwyq-75wu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hwyq-75wu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyq-75wu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hwyq-75wu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hwyq-75wu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyq-75wu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table II. Salmonellosis to Shigellosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hwyy-s2tt",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2021-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "2021",
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
-            "identifier": "https://data.cdc.gov/api/views/hwyy-s2tt",
             "description": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Reporting jurisdictions were informed CDC could receive data for this condition in August 2019. Please note there will be a delay in reporting of case notifications for this condition to CDC.",
-            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41416,55 +41324,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hwyy-s2tt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hwyy-s2tt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hwyy-s2tt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hwyy-s2tt",
+            "issued": "2021-01-21",
+            "keyword": [
+                "2021",
+                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
+                "chancroid",
+                "chlamydia trachomatis infection",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hwyy-s2tt",
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
+            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "009:20"
             ],
-            "landingPage": "https://data.cdc.gov/d/hyai-856q",
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
-                "name": "data.cdc.gov"
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
@@ -41472,44 +41390,34 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hyai-856q",
+            "issued": "2024-11-14",
+            "landingPage": "https://data.cdc.gov/d/hyai-856q",
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
+            "title": "A model for detecting the effects of vibration on peripheral blood flow"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/hyak-nxqs",
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
-            "identifier": "https://data.cdc.gov/api/views/hyak-nxqs",
             "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
-            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41517,69 +41425,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hyak-nxqs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hyak-nxqs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hyak-nxqs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/hyak-nxqs",
+            "issued": "2022-01-14",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "toxic shock syndrome (other than streptococcal)",
+                "trichinellosis",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/hyak-nxqs",
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
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis"
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
-                "name": "National Center for Health Statistics"
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
@@ -41587,140 +41492,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hzd8-r9mj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hzd8-r9mj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/hzd8-r9mj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
-            "license": "https://www.usa.gov/government-works",
-            "theme": [
-                "NCHS"
+            "identifier": "https://data.cdc.gov/api/views/hzd8-r9mj",
+            "isPartOf": "NCHS - Percent Distribution of Births to Unmarried Women by Age Group: United States",
+            "issued": "2015-12-02",
+            "keyword": [
+                "age",
+                "births",
+                "nchs",
+                "nonmarital",
+                "percent distribution"
             ],
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
             "language": [
                 "English"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i2a4-xk9k",
-            "bureauCode": [
-                "009:20"
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
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-29",
+            "programCode": [
+                "009:020"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Jasmine Chaitram",
-                "hasEmail": "mailto:zoa6@cdc.gov"
-            },
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Laboratory Data Section"
-            },
-            "identifier": "https://data.cdc.gov/api/views/i2a4-xk9k",
-            "description": "This dataset includes COVID-19 self-test result data voluntarily reported by users of tests through the MakeMyTestCount website (makemytestcount.org). All fields are self-reported by the user with the exception of  fields derived from the self-reported zip code. This dataset will be updated monthly. If there are any questions, please direct them to the data steward, Jasmine Chaitram <zoa6@cdc.gov>. \n\nThis dataset includes the following self-reported data:  \n- Date (by week)\u2013 date of test shown by week starting date  \n- Age group (years) \u2013 age of individual taking the test, categorized into the following: 2-4, 5-11, 12-15, 16-17, 18-29, 30-39, 40-49, 50-64, 65-74, 75+  \n- Race \u2013 race of individual taking the test: American Indian or Alaska Native, Asian, Black, Native Hawaiian or Other Pacific Islander, White, Multiple or Other, missing \n- Ethnicity \u2013 ethnicity of individual taking the test: Hispanic, Non-Hispanic, missing \n- Sex \u2013 sex of individual taking the test: male, female, missing \n- Test result \u2013 positive, negative, inconclusive \n\nThe dataset also includes the following columns to support analyses. These columns are based on the self-reported zip code:  \n- State abbreviation  \n- State name  \n- State FIPS code \n- FEMA region  \n\nPlease note that there are limitations with these data, including: \n\n1. Data are not comprehensive of all self-tests performed. Data represent results voluntarily reported by an individual via the MakeMyTestCount website. These data do not include self-test results that were reported to state and local health departments if they were not also reported through the MakeMyTestCount website. The true denominator (known number of tests completed in the US) cannot be ascertained and reflects a small fraction of the number of self-tests used.    \n\n2. Data are not verified. The quality of specimen, appropriate execution of self-test, result produced, and person tested are unverified; therefore, reported interpretation of results cannot be confirmed. All results and accompanying demographic information are also self-reported and cannot be verified.  \n\n3. Data reports are not complete. Individual submissions vary widely in terms of the data elements collected. Not all data elements are required (only date, age, and zip code), and some results are missing demographic information.  \n\n4. Data are not representative. Based on the limited number of self-reported test results, this dataset is not representative of the use of self-testing by demographic, nor is the dataset inclusive of all self-testing completed within each jurisdiction. This dataset represents a small proportion of overall COVID-19 testing conducted and reported volumes are much lower than testing conducted in point of care and laboratory settings.   \n\n5. Data represent individual test results, not persons tested. Data in this dataset are not linkable and do not allow for analyses around serial testing. Data also cannot be disaggregated to identify multiple reports by the same individual.  \n\nAll analyses should be completed with these limitations in mind.  \n\nFor more information about the challenges and opportunities around self-test data, please refer to the following article: Ritchey MD, Rosenblum HG, Del Guercio K, et al. COVID-19 Self-Test Data: Challenges and Opportunities \u2014 United States, October 31, 2021\u2013June 11, 2022. MMWR Morb Mortal Wkly Rep 2022;71:1005\u20131010. DOI: http://dx.doi.org/10.15585/mmwr.mm7132a1",
-            "title": "U.S. COVID-19 MakeMyTestCount Self-Test Data",
-            "programCode": [
-                "009:038"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2a4-xk9k/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2a4-xk9k/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/i2a4-xk9k/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2a4-xk9k/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/i2a4-xk9k/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                "name": "National Center for Health Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i2a4-xk9k/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.cdc.gov/api/views/i2a4-xk9k/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "http://www.cdc.gov/nchs/data/databriefs/db162.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf"
             ],
-            "spatial": "US",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "rights": "public",
+            "spatial": "United States",
+            "temporal": "1970/2015",
             "theme": [
-                "Public Health Surveillance"
+                "NCHS"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NCHS - Percent Distribution of Births to Unmarried Women by Age Group: United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i42d-szcv",
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
-                "tetanus",
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
-            "identifier": "https://data.cdc.gov/api/views/i42d-szcv",
             "description": "NNDSS - Table II. Tetanus to Varicella  - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
-            "title": "NNDSS - Table II. Tetanus to Varicella",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41728,66 +41567,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i42d-szcv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i42d-szcv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i42d-szcv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i42d-szcv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i42d-szcv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i42d-szcv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i42d-szcv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i42d-szcv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i42d-szcv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i42d-szcv",
+            "issued": "2019-01-03",
+            "keyword": [
+                "2018",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i42d-szcv",
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
+            "title": "NNDSS - Table II. Tetanus to Varicella"
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
-                "name": "data.cdc.gov"
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
@@ -41795,71 +41632,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i43m-djm6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i43m-djm6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i43m-djm6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i43m-djm6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+            "title": "NNDSS - Table 1F. Brucellosis to Candida auris, clinical"
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
@@ -41867,64 +41699,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i46a-9kgh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i46a-9kgh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i46a-9kgh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i46a-9kgh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i46a-9kgh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i46a-9kgh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i46a-9kgh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i46a-9kgh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i46a-9kgh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-            "landingPage": "https://data.cdc.gov/d/i4eq-dgfc",
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
-                "name": "data.cdc.gov"
-            },
-            "identifier": "https://data.cdc.gov/api/views/i4eq-dgfc",
             "description": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
-            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41932,59 +41771,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i4eq-dgfc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i4eq-dgfc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i4eq-dgfc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i4eq-dgfc",
+            "issued": "2019-04-26",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "vibriosis confirmed",
+                "vibriosis probable",
+                "wonder"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i4eq-dgfc",
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
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.cdc.gov/d/i54f-wv8z",
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
-            "identifier": "https://data.cdc.gov/api/views/i54f-wv8z",
             "description": "Download the latest version of the Glossary and Methodology File",
-            "title": "Youth Risk Behavior Surveillance System (YRBSS) Glossary and Methodology",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41992,43 +41836,39 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i54f-wv8z",
+            "issued": "2015-02-05",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i54f-wv8z",
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
+            "title": "Youth Risk Behavior Surveillance System (YRBSS) Glossary and Methodology"
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
-            "modified": "2023-09-08",
-            "keyword": [
-                "chronic conditions",
-                "health statistics",
-                "nchs",
-                "nhanes",
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
-            "identifier": "https://data.cdc.gov/api/views/i667-sjhg",
             "description": "These data represent prevalence estimates of select chronic conditions from the National Health and Nutrition Examination Survey (NHANES).",
-            "title": "NHANES Select Chronic Conditions Prevalence Estimates",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42036,78 +41876,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i667-sjhg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i667-sjhg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i667-sjhg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S.",
+            "identifier": "https://data.cdc.gov/api/views/i667-sjhg",
+            "issued": "2023-03-02",
+            "keyword": [
+                "chronic conditions",
+                "nchs",
+                "nhanes",
+                "health statistics",
+                "surveillance",
+                "survey"
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
+            "title": "NHANES Select Chronic Conditions Prevalence Estimates"
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
-                "sdoh-higher-education",
-                "sdoh-high-school",
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
-            "identifier": "https://data.cdc.gov/api/views/i6ej-9eac",
             "description": "Provisional counts of deaths in the United States by race and educational attainment. The dataset includes cumulative provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
-            "title": "AH Provisional COVID-19 Deaths by Race and Educational Attainment",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42115,62 +41947,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i6ej-9eac/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i6ej-9eac/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i6ej-9eac/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
+                "sdoh-higher-education",
+                "sdoh-high-school",
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
+                "name": "National Center for Health Statistics"
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
@@ -42178,45 +42022,38 @@
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
-            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
             "bureauCode": [
                 "009:20"
             ],
-            "issued": "2023-11-16",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-04",
-            "references": [
-                "https://www.census.gov/programs-surveys/acs/data.html",
-                "https://www.census.gov/programs-surveys/acs/library/handbooks/general.html"
-            ],
-            "keyword": [
-                "acs",
-                "county",
-                "estimates",
-                "places",
-                "sdoh"
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
-            "identifier": "https://data.cdc.gov/api/views/i6u4-y3g4",
             "description": "This dataset contains county-level social determinants of health (SDOH) measures from the American Community Survey 5-year data for the entire United States\u201450 states and the District of Columbia. Data were downloaded from data.census.gov using Census API and processed by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. These measures complement existing PLACES measures, including PLACES SDOH measures (e.g., health insurance, routine check-up). These data can be used together with PLACES data to identify which health and SDOH issues overlap in a community to help inform public health planning.  \n\nTo access spatial data, please use the ArcGIS Online service:  https://cdcarcgis.maps.arcgis.com/home/item.html?id=d51009ea78b54635be95c6ec9955ec17.",
-            "title": "SDOH Measures for County, ACS 2017-2021",
-            "programCode": [
-                "009:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42224,63 +42061,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i6u4-y3g4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i6u4-y3g4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i6u4-y3g4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i6u4-y3g4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i6u4-y3g4",
+            "issued": "2023-11-16",
+            "keyword": [
+                "acs",
+                "county",
+                "estimates",
+                "places",
+                "sdoh"
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
+            "title": "SDOH Measures for County, ACS 2017-2021"
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
@@ -42288,61 +42129,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i8t6-whzd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i8t6-whzd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i8t6-whzd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
-                "name": "data.cdc.gov"
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
@@ -42350,68 +42194,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i9qr-47vu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i9qr-47vu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i9qr-47vu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/i9qr-47vu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i9qr-47vu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i9qr-47vu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/i9qr-47vu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/i9qr-47vu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/i9qr-47vu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.cdc.gov/api/views/i9qr-47vu",
+            "issued": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "landingPage": "https://data.cdc.gov/d/i9qr-47vu",
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
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 9 - San Francisco"
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
@@ -42419,46 +42255,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ib3w-k9rq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ib3w-k9rq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.cdc.gov/api/views/ib3w-k9rq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.cdc.gov/api/views/ib3w-k9rq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
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
@@ -42485,64 +42355,38 @@
                 "surveillance",
                 "survey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Center for Health Statistics",
-                "hasEmail": "mailto:cdcinfo@cdc.gov"
-            },
+            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/DataPage.aspx?Component=LimitedAccess&Cycle=1959-1994",
+            "modified": "2023-04-17",
+            "programCode": [
+                "009:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Health Statistics"
             },
-            "identifier": "https://data.cdc.gov/api/views/ic32-yq9m",
```

