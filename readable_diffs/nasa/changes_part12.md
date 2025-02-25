# Change History for nasa.json (Part 12)

### Changes from 31606f9 to dd2190f (Part 1/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/nasa.json b/nasa.json
index 9f48df2..34f37cd 100644
--- a/nasa.json
+++ b/nasa.json
@@ -3,40 +3,20 @@
     "@id": "https://data.nasa.gov/data.json",
     "@type": "dcat:Catalog",
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "dataset": [
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR2-RAW-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "international rosetta mission",
-                "unknown",
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear2-raw-v3.0_222f-2gsy",
             "description": "This dataset contains EDITED RAW DATA of the second Earth Flyby (EAR2). The closest approach (CA) took place on November 13, 2007 at 20:57",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR2 RAW V3.0",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44,3107 +24,3129 @@
                     "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear2-raw-v3.0_222f-2gsy",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "unknown",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR2-RAW-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "https://pds.nasa.gov"
+            ],
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR2 RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-RSS-1%2F5-EROS%2FORBIT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "eros",
-                "near earth asteroid rendezvous"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The NEAR Eros Radio Science Data Set is a time-ordered collection of raw and partially processed data collected during the NEAR orbital mapping of the asteroid 433 Eros.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-rss-1-5-eros-orbit-v1.0_2245-qgpq",
+            "issued": "2018-06-26",
+            "keyword": [
+                "eros",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-RSS-1%2F5-EROS%2FORBIT-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-rss-1-5-eros-orbit-v1.0_2245-qgpq",
-            "description": "The NEAR Eros Radio Science Data Set is a time-ordered collection of raw and partially processed data collected during the NEAR orbital mapping of the asteroid 433 Eros.",
-            "title": "NEAR EROS RADIO SCIENCE DATA SET - EROS/ORBIT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR EROS RADIO SCIENCE DATA SET - EROS/ORBIT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LEISA-3-KEM1-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "new horizons kuiper belt extended mission",
-                "vega"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the KEM1 ENCOUNTER mission phase.  This is VERSION 2.0 of this data set. This data set contains LEISA observations taken for functional testing, and MU69 [ASTEROID 486958 (2014 MU69)] Encounter operations, including a test of a slow scan rate. Many LEISA Composition and System Scans along with some LEISA Scans as a LORRI Rider. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-leisa-3-kem1-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission",
+                "vega"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LEISA-3-KEM1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-leisa-3-kem1-v2.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the KEM1 ENCOUNTER mission phase.  This is VERSION 2.0 of this data set. This data set contains LEISA observations taken for functional testing, and MU69 [ASTEROID 486958 (2014 MU69)] Encounter operations, including a test of a slow scan rate. Many LEISA Composition and System Scans along with some LEISA Scans as a LORRI Rider. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019.",
-            "title": "NEW HORIZONS\n      LEISA KEM1\n      CALIBRATED V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "NEW HORIZONS\n      LEISA KEM1\n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1080-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-05T10:16:25.000 to 2015-10-05T17:30:49.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1080-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1080-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1080-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-05T10:16:25.000 to 2015-10-05T17:30:49.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1080 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1080 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V14.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through the end of 2015.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v14.0_229k-wz4f",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "support archives",
                 "asteroid",
                 "satellite"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-OCCULTATIONS-V14.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-occultations-v14.0_229k-wz4f",
-            "description": "This data set is intended to include all reported timings of observed asteroid, planet, and planetary satellite occultation events as well as occultation axes derived from those timings by David W. Dunham and David Herald. This version is complete through the end of 2015.",
-            "title": "ASTEROID OCCULTATIONS V14.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ASTEROID OCCULTATIONS V14.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2005-03-11. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDCDAAC/NARSTO/0008.",
-            "issued": "2006-09-19",
-            "temporal": "2000-02-14T00:00:00Z/2002-08-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-18",
-            "keyword": [
-                "atmospheric chemistry",
-                "aerosols",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ASDC USER SERVICES",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2350113375-LARC_ASDC",
             "description": "NARSTO_SHEMP_CANADA_PM_COMPOSTION_DATA was obtained between February 14, 2000 and August 1, 2002 during the Study of the Health Effects of the Mix of Urban Air Pollutants (SHEMP). SHEMP was a three-year Toxic Substances Research Initiative study undertaken to advance Canadian knowledge on the possible relationship between PM 2.5 composition and co-pollutants (e.g., NO2, O3) and health effects and on the behavior of PM 2.5 in Canadian cities. The main objectives of this study were to obtain new information on the sources, formation and chemical make-up of PM 2.5 and the critical components of the air pollution mix responsible for health effects. \r\n\r\nField measurement studies in Toronto and Vancouver were designed to meet these objectives and to provide the data to test the hypothesis that the organic fraction of PM 2.5 was a critical component with respect to cardio-respiratory disease. In this study, the sources, formation and chemical content of breathable particles in air and the co-occurrence of other air pollutants were investigated. Air samples were collected daily from sites in Toronto and Vancouver over 2-3 years. Chemical content and particle size were determined. Data were also collected on the presence of other air pollutants present in the form of gases (co-pollutants). A small number of samples were analyzed to determine whether the content of specific indicator chemicals in air particles could help find their pollution source (vehicle exhaust, cooking, wood burning etc.). \r\n\r\nSpecific chemicals of breathable particles produced by different types of sources were identified. Similarly, a small number of samples were collected to assess if semi-volatile organic compounds (i.e., chemicals that may evaporate from the particle and are thus often not measured properly) were an important contributor to the mass of breathable particles. The SHEMP study was led by the Air Quality Research Branch of the Meteorological Service of Canada (MSC). The main collaborators were the Environmental Technology Centre of the Environmental Protection Service and the Chemistry Department of the University of Toronto. The breadth of the study also necessitated that many other organizations provide support, such as the Greater Vancouver Regional District, the Pacific Environmental Science Centre and the Ontario Ministry of the Environment. North American Research Strategy for Tropospheric Ozone (NARSTO), which has since disbanded, was a public/private partnership, whose membership spanned across government, utilities, industry, and academe throughout Mexico, the United States, and Canada. The primary mission was to coordinate and enhance policy-relevant scientific research and assessment of tropospheric pollution behavior; activities provide input for science-based decision-making and determination of workable, efficient, and effective strategies for local and regional air-pollution management. Data products from local, regional, and international monitoring and research programs are still available.",
-            "title": "NARSTO SHEMP Particulate Matter Composition Data, Canada, 2000-2002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDCDAAC%2FNARSTO%2F0008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/NARSTO",
-                    "description": "ASDC Data and Information for NARSTO",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for NARSTO",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/NARSTO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cdiac.ess-dive.lbl.gov/programs/NARSTO/",
-                    "description": "NARSTO Quality Systems Program Science Systems Legacy Page",
                     "@type": "dcat:Distribution",
+                    "description": "NARSTO Quality Systems Program Science Systems Legacy Page",
+                    "downloadURL": "https://cdiac.ess-dive.lbl.gov/programs/NARSTO/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2350113375-LARC_ASDC",
-                    "description": "Earthdata Search for NARSTO_SHEMP_CANADA_PM_COMPOSITION_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NARSTO_SHEMP_CANADA_PM_COMPOSITION_DATA_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2350113375-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0008",
-                    "description": "DOI data set landing page for NARSTO_SHEMP_CANADA_PM_COMPOSITION_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NARSTO_SHEMP_CANADA_PM_COMPOSITION_DATA_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0008",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_shemp_canada_pm_composition_data.pdf",
-                    "description": "Guide for NARSTO SHEMP Particulate Matter Composition Data, Canada, 2000-2002",
                     "@type": "dcat:Distribution",
+                    "description": "Guide for NARSTO SHEMP Particulate Matter Composition Data, Canada, 2000-2002",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/guide/narsto_shemp_canada_pm_composition_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/SHEMP_TSRI_41.pdf",
-                    "description": "TSRI # 41 - Health Effects Study with Enhanced Characterization of Urban Air Pollutant Mix",
                     "@type": "dcat:Distribution",
+                    "description": "TSRI # 41 - Health Effects Study with Enhanced Characterization of Urban Air Pollutant Mix",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/SHEMP_TSRI_41.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Intro_1_2.pdf",
-                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Introduction through Section 2)",
                     "@type": "dcat:Distribution",
+                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Introduction through Section 2)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Intro_1_2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Section_3.pdf",
-                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Section 3)",
                     "@type": "dcat:Distribution",
+                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Section 3)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Section_3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Section_4.pdf",
-                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Section 4)",
                     "@type": "dcat:Distribution",
+                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Section 4)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Section_4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Sect_5_6.pdf",
-                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Sections 5-6)",
                     "@type": "dcat:Distribution",
+                    "description": "Final Report for the Texas PM2.5 Sampling and Analysis Study (March 11, 1997 - March 12, 1998) (Sections 5-6)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/readme/Sect_5_6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/narsto_texas_final_report.html",
-                    "description": "ASDC URL for the Final Report for the Texas PM2.5 Sampling and Analysis Study",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC URL for the Final Report for the Texas PM2.5 Sampling and Analysis Study",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/narsto/narsto_texas_final_report.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/SHEMP_CANADA_PM_COMPOSITION_DATA_1/",
-                    "description": "ASDC Direct Data Download for NARSTO_SHEMP_CANADA_PM_COMPOSITION_DATA_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NARSTO_SHEMP_CANADA_PM_COMPOSITION_DATA_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NARSTO/SHEMP_CANADA_PM_COMPOSITION_DATA_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2350113375-LARC_ASDC",
+            "issued": "2006-09-19",
+            "keyword": [
+                "atmospheric chemistry",
+                "aerosols",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDCDAAC/NARSTO/0008",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>43.66 -121.98 43.66 -79.4 49.22 -79.4 49.22 -121.98 43.66 -121.98</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2000-02-14T00:00:00Z/2002-08-01T23:59:59.999Z",
             "theme": [
                 "NARSTO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NARSTO SHEMP Particulate Matter Composition Data, Canada, 2000-2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-1.92SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data that have been resampled at a 1.92 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979A Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-1.92sec_22ct-qtg6",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "comet sl9/jupiter collision",
                 "jupiter",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-1.92SEC",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-1.92sec_22ct-qtg6",
-            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data that have been resampled at a 1.92 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979A Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
-            "title": "VOYAGER 2 JUPITER MAGNETOMETER RESAMPLED DATA 1.92 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 2 JUPITER MAGNETOMETER RESAMPLED DATA 1.92 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2118",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lu, X., X. Zhang, F. Li, and M.A. Cochrane. 2023. Fire Particulate Emissions from Combined VIIRS and AHI Data for Indonesia, 2015-2020. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2118",
-            "issued": "2023-03-15",
-            "temporal": "2015-07-04T00:00:00Z/2020-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "human dimensions",
-                "ecological dynamics",
-                "aerosols",
-                "air quality",
-                "natural hazards",
-                "earth science",
-                "atmosphere",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2600303267-ORNL_CLOUD",
             "description": "This dataset provides 10-minute fire emissions within 0.1-degree regularly spaced intervals across Indonesia from July 2015 to December 2020. The dataset was produced with a top-down approach based on fire radiative energy (FRE) and smoke aerosol emission coefficients (Ce) derived from multiple new-generation satellite observations. Specifically, the Ce values of peatland, tropical forest, cropland, or savanna and grassland were derived from fire radiative power (FRP) and emission rates of smoke aerosols based on Visible Infrared Imaging Radiometer Suite (VIIRS) active fire and aerosol products. FRE for each 0.1-degree interval was calculated from the diurnal FRP cycle that was reconstructed by fusing cloud-corrected FRP retrievals from the high temporal-resolution (10 mins) Himawari-8 Advanced Himawari Imager (AHI) with those from high spatial-resolution (375 m) VIIRS. This new dataset was named the Fused AHI-VIIRS based fire Emissions (FAVE). Fire emissions data are provided in comma-separated values (CSV) format with one file per month from July 2015 to December 2020. Each file includes variables of fire observation time, fire geographic location, classification, fire radiative energy, various fire emissions and related standard deviations.",
-            "graphic-preview-description": "Spatial patterns of the (a) mean annual total particulate matter (TPM) from fire emissions during fire seasons from 2015 to 2020 and (b) TPM from fire emissions in October 2015 across Indonesia. Areas marked with green lines represent peatland areas. Source: Lu et al. (2022).",
-            "title": "Fire Particulate Emissions from Combined VIIRS and AHI Data for Indonesia, 2015-2020",
-            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/Fire_Emissions_Indonesia_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2118",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2118",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/cms/Fire_Emissions_Indonesia/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/cms/Fire_Emissions_Indonesia/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Fire_Emissions_Indonesia.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Fire_Emissions_Indonesia.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2118",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2118",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Fire_Emissions_Indonesia/comp/Fire_Emissions_Indonesia.pdf",
-                    "description": "Fire Particulate Emissions from Combined VIIRS and AHI Data for Indonesia, 2015-2020: Fire_Emissions_Indonesia.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Fire Particulate Emissions from Combined VIIRS and AHI Data for Indonesia, 2015-2020: Fire_Emissions_Indonesia.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/cms/Fire_Emissions_Indonesia/comp/Fire_Emissions_Indonesia.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Fire_Emissions_Indonesia_Fig1.jpg",
-                    "description": "Spatial patterns of the (a) mean annual total particulate matter (TPM) from fire emissions during fire seasons from 2015 to 2020 and (b) TPM from fire emissions in October 2015 across Indonesia. Areas marked with green lines represent peatland areas. Source: Lu et al. (2022).",
                     "@type": "dcat:Distribution",
+                    "description": "Spatial patterns of the (a) mean annual total particulate matter (TPM) from fire emissions during fire seasons from 2015 to 2020 and (b) TPM from fire emissions in October 2015 across Indonesia. Areas marked with green lines represent peatland areas. Source: Lu et al. (2022).",
+                    "downloadURL": "https://daac.ornl.gov/CMS/guides/Fire_Emissions_Indonesia_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Spatial patterns of the (a) mean annual total particulate matter (TPM) from fire emissions during fire seasons from 2015 to 2020 and (b) TPM from fire emissions in October 2015 across Indonesia. Areas marked with green lines represent peatland areas. Source: Lu et al. (2022).",
+            "graphic-preview-file": "https://daac.ornl.gov/CMS/guides/Fire_Emissions_Indonesia_Fig1.jpg",
+            "identifier": "C2600303267-ORNL_CLOUD",
+            "issued": "2023-03-15",
+            "keyword": [
+                "human dimensions",
+                "ecological dynamics",
+                "aerosols",
+                "air quality",
+                "natural hazards",
+                "earth science",
+                "atmosphere",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2118",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "89.0 -11.0 153.0 10.1",
+            "temporal": "2015-07-04T00:00:00Z/2020-12-31T23:59:59Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Fire Particulate Emissions from Combined VIIRS and AHI Data for Indonesia, 2015-2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/XHCGUMGNWO9S",
             "citation": "Joel Susskind. 2019-01-15. SNDRSNIML3CMCHTN. Version 1. Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Monthly CHART Normal Spectral Resolution V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/XHCGUMGNWO9S. https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3CMCHTN_1.html. Digital Science Data.",
-            "issued": "2013-01-01",
-            "temporal": "2013-01-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-11-01",
-            "references": [
-                "https://doi.org/10.1117/1.JRS.8.084994",
-                "https://doi.org/10.1109/TGRS.2010.2070508",
-                "https://doi.org/10.1002/2015JD024008",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.1109/TGRS.2002.808236"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "clouds",
-                "ocean temperature",
-                "precipitation",
-                "land surface",
-                "oceans",
-                "surface radiative properties",
-                "atmospheric water vapor",
-                "surface thermal properties",
-                "altitude",
-                "air quality",
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Joel Susskind",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1633993919-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "The objective of this limited edition data collection is to examine products generated by the Climate Heritage AIRS Retrieval Technique (CHART) algorithm to analyze Cross-track Infrared Sounder/Advanced Technology Microwave Sounder (CrIS/ATMS) instruments, also known as CrIMSS (Cross-track Infrared and Microwave Sounding Suite).  The CrIS/ATMS instruments used for this product are on board the Suomi National Polar-orbiting Partnership (SNPP) platform and use the Normal Spectral Resolution (NSR) data. The CrIS instrument is a Fourier transform spectrometer with a total of 1305 NSR infrared sounding channels covering the longwave (655-1095 cm-1), midwave (1210-1750 cm-1), and shortwave (2155-2550 cm-1) spectral regions. The ATMS instrument  is a cross-track scanner with 22 channels in spectral bands from 23 GHz through 183 GHz.\n \nThe CHART algorithm is uses the  basic cloud clearing and retrieval methodologies used including the definition and derivation of Jacobians, the channel noise covariance matrix, and the use of constraints including the background term, are essentially identical to those of AIRS Version-6.6 and previous AIRS Science Team retrieval algorithms.  As with the Version-6.6 AIRS system, the CHART algorithm uses a Neural Network system as an initial guess. The sounding retrieval methodology characterizes the full atmospheric state and the retrievals contains a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; outgoing longwave radiation (OLR); and an infrared-based precipitation estimate.\n\nThe monthly one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products applying the comprehensive quality control (QC) methodology to form a level-2 daily gridded product. The daily level-3 gridded products are averaged to create the monthly average. Comprehensive QC accepts a retrieval if the profile is good to the surface and ensures consistent analysis across all levels and variables. \n \nThe CHART system was designed to serve as a seamless follow on to the Atmospheric Infrared Sounder/Advanced Microwave Sounding Unit (AIRS/AMSU) instrument processing system. For comparison, the AIRS/AMSU data collection with the TqJ suffix (TqJoint) from AIRX3STM contains similar meteorological information to this CHART data collection and the CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) data collection SNDRSNIML3CMCCPN contains CRIMSS data processed with an analogous algorithm.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRSNIML3CMCHTN",
-            "creator": "Joel Susskind",
-            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 CHART Monthly Retrieval.",
-            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Monthly CHART Normal Spectral Resolution V1",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3CMCHTN_01.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXHCGUMGNWO9S",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FXHCGUMGNWO9S",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3CMCHTN_01.png",
-                    "description": "Sample plot of CrIS/ATMS Level 3 CHART Monthly Retrieval.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CrIS/ATMS Level 3 CHART Monthly Retrieval.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3CMCHTN_01.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3CMCHTN_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3CMCHTN_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/limited_editions/SNPP_CHART/SNDRSNIML3CMCHTN.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/limited_editions/SNPP_CHART/SNDRSNIML3CMCHTN.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/limited_editions/SNPP_CHART/SNDRSNIML3CMCHTN.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/limited_editions/SNPP_CHART/SNDRSNIML3CMCHTN.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML3CMCHTN+1",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML3CMCHTN+1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/SNPP_limited_edition/SNPP.CrIMSS.CHART.CLIMCAPS.v1.L3.README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/SNPP_limited_edition/SNPP.CrIMSS.CHART.CLIMCAPS.v1.L3.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/SNPP_limited_edition/SNPP.CrIMSS.CHART_V1.ATBD.pdf",
-                    "description": "ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/SNPP_limited_edition/SNPP.CrIMSS.CHART_V1.ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 CHART Monthly Retrieval.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3CMCHTN_01.png",
+            "identifier": "C1633993919-GES_DISC",
+            "issued": "2013-01-01",
+            "keyword": [
+                "atmospheric chemistry",
+                "clouds",
+                "ocean temperature",
+                "precipitation",
+                "land surface",
+                "oceans",
+                "surface radiative properties",
+                "atmospheric water vapor",
+                "surface thermal properties",
+                "altitude",
+                "air quality",
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/XHCGUMGNWO9S",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-11-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/10.1117/1.JRS.8.084994",
+                "https://doi.org/10.1109/TGRS.2010.2070508",
+                "https://doi.org/10.1002/2015JD024008",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.1109/TGRS.2002.808236"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRSNIML3CMCHTN",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2013-01-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 3 Comprehensive Quality Control Gridded Monthly CHART Normal Spectral Resolution V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-00_05KMPRO",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2018-10-31. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-00_05KMPRO. https://asdc.larc.nasa.gov/project/CATS-ISS.",
-            "issued": "2018-08-13",
-            "temporal": "2015-03-25T00:00:00Z/2017-10-29T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-08-13",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "clouds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MATTHEW MCGILL",
                 "hasEmail": "mailto:matthew.j.mcgill@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1577484501-LARC_ASDC",
             "description": "CATS-ISS_L2O_N-M7.1-V2-01_05kmPro is the Cloud-Aerosol Transport System (CATS) International Space Station (ISS) Level 2 Operational Night Mode 7.2 Version 3-00 5 km Profile data product. This collection spans from March 25, 2015 to October 29, 2017. CATS, which was launched on January 10, 2015, was a lidar remote sensing instrument that provided range-resolved profile measurements of atmospheric aerosols and clouds from the ISS. CATS was intended to operate on-orbit for up to three years. CATS provides vertical profiles at three wavelengths, orbiting between ~230 and ~270 miles above the Earth's surface at a 51-degree inclination with nearly a three-day repeat cycle. For the first time, scientists were able to study diurnal (day-to-night) changes in cloud and aerosol effects from space by observing the same spot on Earth at different times each day. CATS Level 2 Layer data products contain geophysical parameters and are derived from Level 1 data, at 60m vertical and 5km horizontal resolution.",
-            "graphic-preview-description": "CATS Browse and Granule Availability",
-            "title": "CATS-ISS Level 2 Operational Night Mode 7.2 Version 3-00 5 km Profile",
-            "graphic-preview-file": "https://cats.gsfc.nasa.gov/data/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_N-M7.2-V3-00_05KMPRO",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FCATS%2FL2O_N-M7.2-V3-00_05KMPRO",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf",
-                    "description": "CATS Data Management System Data Products Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Data Management System Data Products Catalog",
+                    "downloadURL": "https://cats.gsfc.nasa.gov/media/docs/CATS_Data_Products_Catalog.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/quality_summaries/CATS_Release_Notes6_v2.pdf",
-                    "description": "CATS Data Release Notes, L1B Version 2.08, L2O Version 2.00, L2O Version 2.01",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Data Release Notes, L1B Version 2.08, L2O Version 2.00, L2O Version 2.01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/quality_summaries/CATS_Release_Notes6_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-00_05KMPRO",
-                    "description": "DOI data set landing page for CATS-ISS_L2O_N-M7.2-V3-00_05kmPro_V3-00",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CATS-ISS_L2O_N-M7.2-V3-00_05kmPro_V3-00",
+                    "downloadURL": "https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-00_05KMPRO",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf",
-                    "description": "CATS Algorithm Theoretical Basis Document Level 1 and Level 2 Data Products - Release 1.0 - 12 June2015",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Algorithm Theoretical Basis Document Level 1 and Level 2 Data Products - Release 1.0 - 12 June2015",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cats.gsfc.nasa.gov/data/browse/",
-                    "description": "CATS Browse and Granule Availability",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Browse and Granule Availability",
+                    "downloadURL": "https://cats.gsfc.nasa.gov/data/browse/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CATS-ISS",
-                    "description": "ASDC Data and Information for CATS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CATS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CATS-ISS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1577484501-LARC_ASDC",
-                    "description": "Earthdata Search for CATS-ISS_L2O_N-M7.2-V3-00_05kmPro_V3-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CATS-ISS_L2O_N-M7.2-V3-00_05kmPro_V3-00 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1577484501-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_Data_Products_Catalog_R7.0.pdf",
-                    "description": "CATS Data Management System Data Products Catalog Release 7.0",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Data Management System Data Products Catalog Release 7.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_Data_Products_Catalog_R7.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_Data_Products_Catalog_R6.0.pdf",
-                    "description": "CATS Data Management System Data Products Catalog, Release 6.0",
                     "@type": "dcat:Distribution",
+                    "description": "CATS Data Management System Data Products Catalog, Release 6.0",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/cats/guide/CATS_Data_Products_Catalog_R6.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_N-M7.2-V3-00_05kmPro/contents.html",
-                    "description": "OPeNDAP data access for CATS-ISS_L2O_N-M7.2-V3-00_05kmPro_V3-00",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CATS-ISS_L2O_N-M7.2-V3-00_05kmPro_V3-00",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CATS/L2O_N-M7.2-V3-00_05kmPro/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_N-M7.2-V3-00_05kmPro/",
-                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_N-M7.2-V3-00_05kmPro_V3-00",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CATS-ISS_L2O_N-M7.2-V3-00_05kmPro_V3-00",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CATS/L2O_N-M7.2-V3-00_05kmPro/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84400/dust-and-clouds-dance-over-the-sahara",
-                    "description": "NASA Earth Observatory Article: Dust and Clouds Dance Over the Sahara",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Dust and Clouds Dance Over the Sahara",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84400/dust-and-clouds-dance-over-the-sahara",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84214/blue-marble-eastern-hemisphere",
-                    "description": "NASA Earth Observatory Article: Blue Marble, Eastern Hemisphere",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Blue Marble, Eastern Hemisphere",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84214/blue-marble-eastern-hemisphere",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/86286/nighttime-view-of-raung-volcanic-plume",
-                    "description": "NASA Earth Observatory Article: Nighttime View of Raung Volcanic Plume",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Nighttime View of Raung Volcanic Plume",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/86286/nighttime-view-of-raung-volcanic-plume",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/86218/a-slice-of-cirrus",
-                    "description": "NASA Earth Observatory Article: A Slice of Cirrus",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: A Slice of Cirrus",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/86218/a-slice-of-cirrus",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-description": "CATS Browse and Granule Availability",
+            "graphic-preview-file": "https://cats.gsfc.nasa.gov/data/browse/",
+            "identifier": "C1577484501-LARC_ASDC",
+            "issued": "2018-08-13",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/CATS/L2O_N-M7.2-V3-00_05KMPRO",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-08-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -52.0 180.0 52.0",
+            "temporal": "2015-03-25T00:00:00Z/2017-10-29T23:59:59Z",
             "theme": [
                 "CATS-ISS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CATS-ISS Level 2 Operational Night Mode 7.2 Version 3-00 5 km Profile"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-COSIMA-3-V6.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Rosetta COSIMA data contains the operational history of the 72 dust collecting substrates from the installation inside the instrument. This dataset contains data from 2002-05-29 up to 2016-09-30. The operations are either expose, storage, spectra, peaks, scans, heating, imaging or grain lists. The data is grouped by the substrate and time. Up to the 2014-08 the aim of the data has been the instrument health and operational functionality, not statistically significant substrate background spectra. From 2014-08 onward the D0 substrate set was used to collect dust collected in the vicinity of 67P/CHURYUMOV GERASIMENKO 1 (1969 R1) and dust analysis with TOF-SIMS. From 2014-10-23 onward due to an instrument failure, the SIMS data became scientifically unusable. While other SIMS parameter sets were tested, substrates CF were exposed from mid 2015-12 and C7 from mid 2015-02. End of March 2015 SIMS became operational again. D1 and CD were exposed and SIMS was done with CD, CF and D1. In June TOF-SIMS was done with CF and D1. In July C7 was measured again, while CD was used for expose and TOF-SIMS up to October. D2 was exposed in September. Grains crushing was tested on D0 in February and March. C3 was used for expose from May. Emitter C extractor control voltage got a short in June and from August it was used with tip voltage control only. This data set supersedes all previous COSIMA datasets, like RO-C-COSIMA-3-V1.0, RO-C-COSIMA-3-V2.0, RO-C-COSIMA-3-V3.0, RO-C-COSIMA-3-V4.0, RO-C-COSIMA-3-V5.0, RO-CAL-COSIMA-2-V1.0 and RO-CAL-COSIMA-3-V3.0 Also, in the above previous versions, the values of the temperature in the HK data where given in Celsius although Kelvin was written in the description of the table in the FMT file. This was fixed in the version RO-C-COSIMA-3-V3.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cosima-3-v6.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-COSIMA-3-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cosima-3-v6.0",
-            "description": "The Rosetta COSIMA data contains the operational history of the 72 dust collecting substrates from the installation inside the instrument. This dataset contains data from 2002-05-29 up to 2016-09-30. The operations are either expose, storage, spectra, peaks, scans, heating, imaging or grain lists. The data is grouped by the substrate and time. Up to the 2014-08 the aim of the data has been the instrument health and operational functionality, not statistically significant substrate background spectra. From 2014-08 onward the D0 substrate set was used to collect dust collected in the vicinity of 67P/CHURYUMOV GERASIMENKO 1 (1969 R1) and dust analysis with TOF-SIMS. From 2014-10-23 onward due to an instrument failure, the SIMS data became scientifically unusable. While other SIMS parameter sets were tested, substrates CF were exposed from mid 2015-12 and C7 from mid 2015-02. End of March 2015 SIMS became operational again. D1 and CD were exposed and SIMS was done with CD, CF and D1. In June TOF-SIMS was done with CF and D1. In July C7 was measured again, while CD was used for expose and TOF-SIMS up to October. D2 was exposed in September. Grains crushing was tested on D0 in February and March. C3 was used for expose from May. Emitter C extractor control voltage got a short in June and from August it was used with tip voltage control only. This data set supersedes all previous COSIMA datasets, like RO-C-COSIMA-3-V1.0, RO-C-COSIMA-3-V2.0, RO-C-COSIMA-3-V3.0, RO-C-COSIMA-3-V4.0, RO-C-COSIMA-3-V5.0, RO-CAL-COSIMA-2-V1.0 and RO-CAL-COSIMA-3-V3.0 Also, in the above previous versions, the values of the temperature in the HK data where given in Celsius although Kelvin was written in the description of the table in the FMT file. This was fixed in the version RO-C-COSIMA-3-V3.0.",
-            "title": "ROSETTA-ORBITER 67P COSIMA 3\n                                      V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P COSIMA 3\n                                      V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/514/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-01-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashok Srivastava",
                 "hasEmail": "mailto:ashok.n.srivastava@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_514",
             "description": "One of the primary goals of Integrated Vehicle Health Management (IVHM) is to detect, diagnose, predict, and mitigate adverse events during the flight of an aircraft, regardless of the subsystem(s) from which the adverse event arises. To properly address this problem, it is critical to develop technologies that can integrate large, heterogeneous (meaning that they contain both continuous and discrete signals), asynchronous data streams from multiple subsystems in order to detect a potential adverse event, diagnose its cause, predict the effect of that event on the remaining useful life of the vehicle, and then take appropriate steps to mitigate the event if warranted. These data streams may have highly non-Gaussian distributions and can also contain discrete signals such as caution and warning messages which exhibit non-stationary and obey arbitrary noise models. At the aircraft level, a Vehicle-Level Reasoning System (VLRS) can be developed to provide aircraft with at least two significant capabilities:  improvement of aircraft safety due to enhanced monitoring and reasoning about the aircraft\u2019s health state, and also potential cost savings through Condition Based Maintenance (CBM).  Along with the achieving the benefits of CBM, an important challenge facing aviation safety today is safeguarding against system- and component-level failures and malfunctions. \r\n\r\nCitation:  A. N. Srivastava, D. Mylaraswamy, R. Mah, and E. Cooper, \u201cVehicle Level Reasoning Systems:  Concept and Future Directions,\u201d Society of Automotive Engineers Integrated Vehicle Health Management Book, Ian Jennions, Ed., 2011.",
-            "title": "Vehicle-Level Reasoning Systems:  Integrating System-Wide data to Estimate Instantaneous Health State",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/VLRS_Chapter_v10-dashlink.pdf",
-                    "description": "VLRS Chapter v10-dashlink.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "VLRS Chapter v10-dashlink.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/VLRS_Chapter_v10-dashlink.pdf",
+                    "mediaType": "application/pdf",
                     "title": "VLRS Chapter v10-dashlink.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_514",
+            "issued": "2012-01-27",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/514/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Vehicle-Level Reasoning Systems:  Integrating System-Wide data to Estimate Instantaneous Health State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/B05/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/B05/DATA001.",
-            "issued": "2007-08-21",
-            "temporal": "2007-08-21T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean temperature",
-                "ocean optics",
-                "oceans",
-                "earth science",
-                "salinity/density"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C1633360129-OB_DAAC",
             "description": "Measurements made off the San Diego, Californian coast in 2007.",
-            "title": "Measurements off the San Diego, Californian coast",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FB05%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FB05%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/B05/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/B05/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360129-OB_DAAC",
+            "issued": "2007-08-21",
+            "keyword": [
+                "ocean chemistry",
+                "ocean temperature",
+                "ocean optics",
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/B05/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2007-08-21T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements off the San Diego, Californian coast"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0068",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-11-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0068.",
-            "issued": "1999-11-09",
-            "temporal": "1992-06-02T00:00:00Z/1992-06-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-11",
-            "keyword": [
-                "air quality",
-                "aerosols",
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric chemistry",
-                "earth science",
-                "clouds",
-                "precipitation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DEAN HEGG",
                 "hasEmail": "mailto:deanhegg@atmos.washington.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001052-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data.To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13-November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29-July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13-December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1-June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems. The development of parameterizations requires an understanding of the processes that generate, maintain, and dissipate boundary layer clouds. This development is currently impeded by lack of understanding of the transition from stratocumulus clouds to trade cumulus clouds and the factors that control cloud type and amount in the boundary layer. The Atlantic Stratocumulus Transition EXperiment (ASTEX) was designed to address key issues related to stratocumulus to trade cumulus transition and mode selection. ASTEX involved intensive measurements from several platforms operating from 1-28 June 1992 in the area of the Azores and Madeira Islands. The purpose was to study how the transition and mode selection are effected by 1) cloud-top entrainment instability, 2) diurnal decoupling and clearing due to solar absorption, 3) patchy drizzle and a transition to horizontally inhomogeneous clouds through decoupling, 4) mesoscale variability in cloud thickness and associated mesoscale circulations, and 5) episodic strong subsidence lowering the inversion below the LCL. Detailed descriptions of the scientific goals of ASTEX are in the FIRE Phase II: Research plan (1989) and in the ASTEX Operations Plan (1992).This ASCII formatted data set includes data collected aboard the University of Washington's Corsair 131A airplane. Several different probes were used to gather data on the liquid water content of clouds, the droplet radius/diameter, and condensation nuclei measurements. All sulfur parameter measurements were made using filter methods.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) University of Washington C-131A Discrete Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0068",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0068",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/FIRE",
-                    "description": "ASDC Data and Information for FIRE",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for FIRE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/FIRE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001052-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_UW_DSCRT_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_UW_DSCRT_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001052-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0068",
-                    "description": "DOI data set landing page for FIRE_AX_UW_DSCRT_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_UW_DSCRT_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0068",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_uw_dataset.pdf",
-                    "description": "FIRE ASTEX University of Washington (UW) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX University of Washington (UW) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ax_uw_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/fire_project.pdf",
-                    "description": "Project/Campaign Document: Project/Campaign Document: FIRE Langley DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "Project/Campaign Document: Project/Campaign Document: FIRE Langley DAAC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/fire_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-ASTEX.tar",
-                    "description": "FIRE II-ASTEX Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE II-ASTEX Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-ASTEX.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Cirrus.tar",
-                    "description": "FIRE I-Cirrus Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE I-Cirrus Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Cirrus.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Extended-Time-Observation.tar",
-                    "description": "FIRE I-Extended-Time-Observation Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE I-Extended-Time-Observation Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_I-Extended-Time-Observation.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-Cirrus.tar",
-                    "description": "FIRE II-Cirrus Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE II-Cirrus Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_II-Cirrus.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_III.tar",
-                    "description": "FIRE III Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE III Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/FIRE_III.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_UW_DSCRT/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_UW_DSCRT_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_UW_DSCRT_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_UW_DSCRT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_UW_DSCRT/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_UW_DSCRT_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_UW_DSCRT_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_UW_DSCRT/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001052-LARC_ASDC",
+            "issued": "1999-11-09",
+            "keyword": [
+                "air quality",
+                "aerosols",
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric chemistry",
+                "earth science",
+                "clouds",
+                "precipitation"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0068",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>32.34 -26.75 32.34 -21.23 38.05 -21.23 38.05 -26.75 32.34 -26.75</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-06-02T00:00:00Z/1992-06-27T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) University of Washington C-131A Discrete Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/466/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-09-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "dashlink",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MISTY DAVIES",
                 "hasEmail": "mailto:misty.d.davies@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_466",
             "description": "This is a textbook, created example for illustration purposes.\r\n\r\nThe System takes inputs of Pt, Ps, and Alt, and calculates the Mach number using the Rayleigh Pitot Tube equation if the plane is flying supersonically.  (See Anderson.)  The unit calculates Cd given the Ma and Alt.\r\n\r\nFor more details, see the NASA TM, also on this website.",
-            "title": "Aerospace Example",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/SystemDriver.c",
-                    "description": "SystemDriver.c",
                     "@type": "dcat:Distribution",
+                    "description": "SystemDriver.c",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/algorithm/SystemDriver.c",
+                    "mediaType": "application/octet-stream",
                     "title": "SystemDriver.c"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_466",
+            "issued": "2011-09-12",
+            "keyword": [
+                "ames",
+                "dashlink",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/466/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Aerospace Example"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0203-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "international rosetta mission",
-                "67p/churyumov-gerasimenko 1 (1969 r1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-13T10:00:55.000 to 2014-08-13T13:36:58.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0203-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0203-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0203-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-13T10:00:55.000 to 2014-08-13T13:36:58.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0203 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0203 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1535871788-LARC_ASDC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "1999-10-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC.",
-            "issued": "1999-10-13",
-            "temporal": "1995-09-08T00:00:00Z/1995-09-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "earth science",
-                "aerosols",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EDWARD BROWELL",
                 "hasEmail": "mailto:e.v.browell@larc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1535871788-LARC_ASDC",
             "description": "An extensive validation experiment was conducted in September 1995 from Wallops Island, Virginia, to evaluate the performance of the LASE (Lidar Atmospheric Sensing Experiment) system for the measurement of water vapor profiles under a wide range of atmospheric and solar background conditions. During this experiment, the LASE system was flown on a high-altitude (ER-2) aircraft on ten missions for a total of 60 hours. LASE measurements of tropospheric water vapor were compared with in situ measurements from balloons and aircraft that were flown under the ER-2 and with remote measurements from the ground and from aircraft. A high-altitude aircraft (Lear Jet) was equipped with two in situ hygrometers, and a medium to low altitude aircraft (C-130) had onboard the NASA Langley airborne water vapor DIAL system and two in situ hygrometers. Several radiosondes were launched during each LASE flight, and some of these sondes were part of a concurrent international radiosonde intercomparison campaign sponsored by the World Meteorological Organization. The NASA Goddard Scanning Raman lidar also provided nighttime water vapor profile measurements from the ground. During this field experiment, LASE was also used in a number of atmospheric case studies including measurements of Hurricane Luis, a coastal sea breeze development, a strong cold front, an upper level front, and cirrus clouds.",
-            "graphic-preview-description": "Animated Loop of LASE_VAL - Flight 07 - Total Scattering Ratio on 09/21/1995",
-            "title": "Lidar Atmospheric Sensing Experiment (LASE) Validation",
-            "graphic-preview-file": "https://science.larc.nasa.gov/lidar/las/ip_las07_tsr_log.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LASE",
-                    "description": "ASDC Data and Information for LASE",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for LASE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LASE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science.larc.nasa.gov/lidar/las/ip_las07_tsr_log.html",
-                    "description": "Animated Loop of LASE_VAL - Flight 07 - Total Scattering Ratio on 09/21/1995",
                     "@type": "dcat:Distribution",
+                    "description": "Animated Loop of LASE_VAL - Flight 07 - Total Scattering Ratio on 09/21/1995",
+                    "downloadURL": "https://science.larc.nasa.gov/lidar/las/ip_las07_tsr_log.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1535871788-LARC_ASDC",
-                    "description": "Earthdata Search for LASE_VALIDATION_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for LASE_VALIDATION_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1535871788-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lase/guide/base_lase_validation_dataset.pdf",
-                    "description": "LASE Validation Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "LASE Validation Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lase/guide/base_lase_validation_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lase/readme/readme_lase_validation.txt",
-                    "description": "LASE_VALIDATION",
                     "@type": "dcat:Distribution",
+                    "description": "LASE_VALIDATION",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lase/readme/readme_lase_validation.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lase/read_software/read_lase_gte.c",
-                    "description": "Code for reading LASE data files - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Code for reading LASE data files - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lase/read_software/read_lase_gte.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/GTE",
-                    "description": "ASDC Data and Information for GTE",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for GTE",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/GTE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/CriticalChem",
-                    "description": "NASA Earth Observatory Article: \"Critical Chemistry\" By Dan Whipple, February 14, 2000",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: \"Critical Chemistry\" By Dan Whipple, February 14, 2000",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/CriticalChem",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_project.pdf",
-                    "description": "Global TroposphericExperiment (GTE) Langley DAAC Project/Campaign Document",
                     "@type": "dcat:Distribution",
+                    "description": "Global TroposphericExperiment (GTE) Langley DAAC Project/Campaign Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/pwb-fmat.pdf",
-                    "description": "GTE - Data Archive Format Document, September 1994",
                     "@type": "dcat:Distribution",
+                    "description": "GTE - Data Archive Format Document, September 1994",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/pwb-fmat.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science.larc.nasa.gov/lidar/instruments-lase.html",
-                    "description": "LIDAR Applications Group overview of the LASE system",
                     "@type": "dcat:Distribution",
+                    "description": "LIDAR Applications Group overview of the LASE system",
+                    "downloadURL": "https://science.larc.nasa.gov/lidar/instruments-lase.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's calibration documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_fmt.pdf",
-                    "description": "NASA LaRC GTE Data Format Document, August 2000",
                     "@type": "dcat:Distribution",
+                    "description": "NASA LaRC GTE Data Format Document, August 2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/gte/guide/gte_fmt.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://science.larc.nasa.gov/lidar/",
-                    "description": "NASA Lidar Applications Group",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Lidar Applications Group",
+                    "downloadURL": "https://science.larc.nasa.gov/lidar/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-gte.larc.nasa.gov/",
-                    "description": "NASA Mission Overview of Global Tropospheric Experiment (GTE)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Mission Overview of Global Tropospheric Experiment (GTE)",
+                    "downloadURL": "https://www-gte.larc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lase/guide/lase_project.pdf",
-                    "description": "Project/Campaign Document: LASE Langley DAAC",
                     "@type": "dcat:Distribution",
+                    "description": "Project/Campaign Document: LASE Langley DAAC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/lase/guide/lase_project.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/langley/news/factsheets/LASE.html",
-                    "description": "NASA.gov LASE Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov LASE Fact Sheet",
+                    "downloadURL": "https://www.nasa.gov/centers/langley/news/factsheets/LASE.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/LASE/LASE_VALIDATION_1",
-                    "description": "Data set landing page for LASE_VALIDATION_1",
                     "@type": "dcat:Distribution",
+                    "description": "Data set landing page for LASE_VALIDATION_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/LASE/LASE_VALIDATION_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "ASDC data citation policy",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC data citation policy",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/LASE/LASE_VALIDATION/",
-                    "description": "ASDC Direct Data Download for LASE_VALIDATION_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for LASE_VALIDATION_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/LASE/LASE_VALIDATION/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/LASE/LASE_VALIDATION/contents.html",
-                    "description": "OPeNDAP data access for LASE_VALIDATION_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for LASE_VALIDATION_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/LASE/LASE_VALIDATION/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Animated Loop of LASE_VAL - Flight 07 - Total Scattering Ratio on 09/21/1995",
+            "graphic-preview-file": "https://science.larc.nasa.gov/lidar/las/ip_las07_tsr_log.html",
+            "identifier": "C1535871788-LARC_ASDC",
+            "issued": "1999-10-13",
+            "keyword": [
+                "earth science",
+                "aerosols",
+                "atmosphere"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1535871788-LARC_ASDC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>28.7 -85.74 28.7 -62.66 42.87 -62.66 42.87 -85.74 28.7 -85.74</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1995-09-08T00:00:00Z/1995-09-27T23:59:59.999Z",
             "theme": [
                 "LASE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Lidar Atmospheric Sensing Experiment (LASE) Validation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263932515-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2022-09-13",
-            "temporal": "2018-04-25T00:00:00Z/2024-04-22T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-13",
-            "keyword": [
-                "atmospheric radiation",
-                "oceans",
-                "ocean optics",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sdps@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C2263932515-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Sentinel-3B OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Chlorophyll (CHL) - Near Real-time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/S3B-OLCI",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directdataaccess/Level-3%20Binned/S3B-OLCI",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/resources/atbd/",
-                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/resources/atbd/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/reprocessing/",
-                    "description": "NASA Ocean Color Web - Processing History",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Processing History",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/reprocessing/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/resources/how-to-cite/",
-                    "description": "NASA Ocean Color Web - Data Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Citation Policy",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/resources/how-to-cite/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 }
             ],
+            "identifier": "C2263932515-OB_DAAC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "atmospheric radiation",
+                "oceans",
+                "ocean optics",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2263932515-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-04-25T00:00:00Z/2024-04-22T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-3B OLCI Level-3B Global Binned Earth-observation Reduced Resolution (ERR) Chlorophyll (CHL) - Near Real-time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0501-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-23T00:21:45.000 to 2014-12-23T12:16:10.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0501-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0501-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0501-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-23T00:21:45.000 to 2014-12-23T12:16:10.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0501 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0501 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=M10-H-MAG-4-SUMM-M1-SUMMARY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "mercury",
-                "mariner 10"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Mariner 10 Magnetometer (MAG) averaged M1 SUMMARY data at Mercury.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.m10-h-mag-4-summ-m1-summary-v1.0_22q6-vq88",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mercury",
+                "mariner 10"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=M10-H-MAG-4-SUMM-M1-SUMMARY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.m10-h-mag-4-summ-m1-summary-v1.0_22q6-vq88",
-            "description": "Mariner 10 Magnetometer (MAG) averaged M1 SUMMARY data at Mercury.",
-            "title": "MARINER 10 MERC MAG SUMM M1 SUMMARY V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARINER 10 MERC MAG SUMM M1 SUMMARY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4736NT2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Volcano Mortality Risks and Distribution. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H4736NT2. https://doi.org/10.7927/H4736NT2.",
-            "issued": "2005-12-31",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4BR8Q45",
-                "https://doi.org/10.7927/H4ZK5DMF",
-                "https://doi.org/10.7927/H43B5X3R"
-            ],
-            "keyword": [
-                "natural hazards",
-                "human dimensions",
-                "earth science",
-                "population"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:metadata@ciesin.columbia.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "SEDAC"
-            },
-            "identifier": "C179001787-SEDAC",
-            "description": "Global Volcano Mortality Risks and Distribution is a 2.5 minute grid representing global volcano mortality risks. The data set was constructed using historical hazard-specific mortality loss data from the Emergency Events Database (EM-DAT) maintained by the Centre for Research on the Epidemiology of Disasters (CRED), subnational year 2000 population estimates from Gridded Population of the World, Version 3 (GPWv3), and volcano hazard data from the Global Volcano Hazard Frequency and Distribution data set. Estimates were made as to the mortality numbers associated with volcano hazard. In turn, these mortality estimates were classified into deciles, 10 class of an approximately equal number of grid cells of increasing mortality risk. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank",
-            "title": "Global Volcano Mortality Risks and Distribution",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Global Volcano Mortality Risks and Distribution is a 2.5 minute grid representing global volcano mortality risks. The data set was constructed using historical hazard-specific mortality loss data from the Emergency Events Database (EM-DAT) maintained by the Centre for Research on the Epidemiology of Disasters (CRED), subnational year 2000 population estimates from Gridded Population of the World, Version 3 (GPWv3), and volcano hazard data from the Global Volcano Hazard Frequency and Distribution data set. Estimates were made as to the mortality numbers associated with volcano hazard. In turn, these mortality estimates were classified into deciles, 10 class of an approximately equal number of grid cells of increasing mortality risk. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4736NT2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4736NT2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-volcano-mortality-risks-distribution/volcano-mortality-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-volcano-mortality-risks-distribution/volcano-mortality-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-volcano-mortality-risks-distribution/maps",
+            "identifier": "C179001787-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "natural hazards",
+                "human dimensions",
+                "earth science",
+                "population"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4736NT2",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2005-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4BR8Q45",
+                "https://doi.org/10.7927/H4ZK5DMF",
+                "https://doi.org/10.7927/H43B5X3R"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
             "theme": [
                 "NDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Volcano Mortality Risks and Distribution"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1272",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hess, L.L., J.M. Melack, E.M.L.M. Novo, C.C.F. Barbosa, and M. Gastil-Buhl. 2015. LBA-ECO LC-07 Validation Overflight for Amazon Mosaics, Video, 1999. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1272",
-            "issued": "2023-10-03",
-            "temporal": "1999-06-03T00:00:00Z/1999-06-21T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "ecosystems",
-                "biosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2777292705-ORNL_CLOUD",
             "description": "This data set presents georeferenced digital video files from Validation Overflight for Amazon Mosaics (VOAM) aerial video surveys as part of the Large-Scale Biosphere-Atmosphere Experiment in the Amazon. The VOAM flights were carried out in the wet-season (June) 1999 in the Brazilian Amazon to provide ground verification for mapping of wetland cover with the Global Rain Forest Mapping (GRFM) Project JERS-1 (Japanese Earth Remote Sensing Satellite) mosaics of the Amazon basin. Digital camcorder systems were installed in a Bandeirante survey plane operated by Brazil's National Institute for Space Research. The VOAM99 surveys circumscribed the Brazilian Amazon, documenting ground conditions at resolutions on the order of 1-m (wide-angle format) and 10-cm (zoom format) for wetlands, forests, savannas, and human-impacted areas. Other applications of the VOAM videography include acquisition of ground control points for image geolocation, creation of a high-resolution geocoded mosaic of a forest study area, forest biomass estimation, and rapid assessment of fire damage. Geocoded digital videography provides a cost-effective means of compiling a high-resolution validation data set for land cover mapping in remote, cloud-covered regions.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-07 Validation Overflight for Amazon Mosaics, Video, 1999",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1272",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1272",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC07_Airborne_Videography/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC07_Airborne_Videography/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC07_Airborne_Videography.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC07_Airborne_Videography.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1272",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1272",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990603_170209_170300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990603_170209_170300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990603_170210_170300_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990603_170210_170300_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990605_144235_143000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990605_144235_143000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990606_182800_182827_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990606_182800_182827_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990606_182800_182830_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990606_182800_182830_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990606_182914_183000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990606_182914_183000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990606_182916_183000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990606_182916_183000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990607_171700_174700_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990607_171700_174700_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140700_140800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140700_140800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140700_140800_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140700_140800_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140800_140900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140800_140900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140800_140900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140800_140900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140900_141000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140900_141000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140900_141000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_140900_141000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_141000_141030_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_141000_141030_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_141000_141100_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_141000_141100_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_141100_141145_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990610_141100_141145_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990611_171800_171857_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990611_171800_171857_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990611_171800_171857_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990611_171800_171857_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_131819_131900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_131819_131900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_131822_131900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_131822_131900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_131900_132000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_131900_132000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_131900_132000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_131900_132000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132000_132100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132000_132100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132000_132100_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132000_132100_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132100_132200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132100_132200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132100_132200_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132100_132200_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132200_132300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132200_132300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132200_132300_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132200_132300_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132300_132400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132300_132400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132300_132400_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132300_132400_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132400_132500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132400_132500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132400_132500_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132400_132500_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132500_132600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132500_132600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132500_132600_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132500_132600_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132600_132641_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132600_132641_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132600_132645_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990613_132600_132645_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123437_123500_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123437_123500_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123441_123500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123441_123500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123500_123600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123500_123600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123500_123600_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123500_123600_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123600_123700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123600_123700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123600_123700_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123600_123700_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123700_123800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123700_123800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123700_123800_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123700_123800_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123800_123900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123800_123900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123800_123900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123800_123900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123900_124000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123900_124000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123900_124000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_123900_124000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124000_124100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124000_124100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124000_124100_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124000_124100_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124100_124200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124100_124200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124100_124200_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124100_124200_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124200_124300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124200_124300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124200_124300_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124200_124300_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124300_124400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124300_124400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124300_124400_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124300_124400_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124400_124500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124400_124500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124400_124500_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124400_124500_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124500_124600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124500_124600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124500_124600_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124500_124600_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124600_124700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124600_124700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124600_124700_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124600_124700_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124700_124800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124700_124800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124700_124800_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124700_124800_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124800_124900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124800_124900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124800_124900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990615_124800_124900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140100_140200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140100_140200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140100_140200_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140100_140200_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140200_140300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140200_140300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140200_140300_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140200_140300_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140300_140400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140300_140400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140300_140400_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140300_140400_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140400_140500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140400_140500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140400_140500_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140400_140500_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140500_140600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140500_140600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140500_140600_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140500_140600_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140600_140700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140600_140700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140600_140700_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140600_140700_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140700_140800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140700_140800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140700_140800_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140700_140800_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140800_140900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140800_140900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140800_140900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140800_140900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140900_141000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140900_141000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140900_141000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_140900_141000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_141000_141100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_141000_141100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_141000_141100_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_141000_141100_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151400_151500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151400_151500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151400_151500_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151400_151500_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151500_151600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151500_151600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151500_151600_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151500_151600_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151600_151700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151600_151700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151600_151700_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151600_151700_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151700_151800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151700_151800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151700_151800_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151700_151800_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151800_151900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151800_151900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151800_151900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151800_151900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151900_152000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151900_152000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151900_152000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_151900_152000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152000_152100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152000_152100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152000_152100_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152000_152100_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152100_152200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152100_152200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152100_152200_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152100_152200_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152200_152300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152200_152300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152200_152300_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152200_152300_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152300_152400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152300_152400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152300_152400_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152300_152400_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152400_152500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152400_152500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152400_152500_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152400_152500_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152500_152600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152500_152600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152500_152600_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152500_152600_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152600_152700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152600_152700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152600_152700_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152600_152700_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152700_152800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152700_152800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152700_152800_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152700_152800_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152800_152900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152800_152900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152800_152900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152800_152900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152900_153000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152900_153000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152900_153000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_152900_153000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_153000_153100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_153000_153100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_153100_153200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_153100_153200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_153200_153300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_153200_153300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_153900_154000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_153900_154000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_154000_154100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_154000_154100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_154100_154200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990618_154100_154200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_165600_165644_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_165600_165644_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172318_172400_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172318_172400_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172338_172400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172338_172400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172400_172500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172400_172500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172400_172500_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172400_172500_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172500_172600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172500_172600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172500_172600_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172500_172600_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172600_172700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172600_172700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172600_172700_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172600_172700_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172700_172800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172700_172800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172700_172800_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172700_172800_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172800_172900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172800_172900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172800_172900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172800_172900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172900_173000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172900_173000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172900_173000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_172900_173000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173000_173100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173000_173100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173000_173100_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173000_173100_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173100_173147_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173100_173147_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173100_173200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173100_173200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173200_173300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173200_173300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173216_173245_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173216_173245_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173300_173400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173300_173400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173400_173500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173400_173500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173500_173600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173500_173600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173600_173700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173600_173700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173608_173700_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173608_173700_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173700_173800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173700_173800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173700_173800_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173700_173800_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173800_173900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173800_173900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173800_173900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173800_173900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173900_174000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173900_174000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173900_174000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_173900_174000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174000_174100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174000_174100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174000_174100_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174000_174100_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174100_174200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174100_174200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174100_174200_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174100_174200_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174200_174300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174200_174300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174200_174300_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174200_174300_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174300_174400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174300_174400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174300_174400_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174300_174400_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174400_174500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174400_174500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174400_174500_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174400_174500_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174500_174600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174500_174600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174500_174600_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174500_174600_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174600_174700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174600_174700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174600_174700_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174600_174700_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174700_174800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174700_174800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174700_174800_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174700_174800_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174800_174900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174800_174900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174800_174900_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174800_174900_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174900_175000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174900_175000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174900_175000_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_174900_175000_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175000_175100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175000_175100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175000_175100_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175000_175100_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175100_175200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175100_175200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175100_175200_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175100_175200_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175200_175300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175200_175300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175200_175300_z.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175200_175300_z.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175300_175400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175300_175400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175400_175500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175400_175500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175500_175600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175500_175600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175600_175700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175600_175700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175700_175800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175700_175800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175800_175900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175800_175900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175900_180000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_175900_180000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180000_180100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180000_180100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180100_180200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180100_180200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180200_180300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180200_180300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180300_180400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180300_180400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180400_180500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180400_180500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180500_180600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180500_180600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180600_180700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180600_180700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180700_180800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180700_180800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180800_180900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180800_180900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180900_181000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_180900_181000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181000_181100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181000_181100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181100_181200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181100_181200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181200_181300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181200_181300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181300_181400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181300_181400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181400_181500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181400_181500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181500_181600_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181500_181600_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181600_181700_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181600_181700_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181700_181800_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181700_181800_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181800_181900_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181800_181900_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181900_182000_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_181900_182000_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182000_182100_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182000_182100_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182100_182200_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182100_182200_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182200_182300_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182200_182300_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182300_182400_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182300_182400_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "video/quicktime",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182400_182500_w.mov",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/19990621_182400_182500_w.mov",
+                    "mediaType": "video/quicktime",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/LC07_Airborne_Videography.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/LC07_Airborne_Videography.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/LC07_videos_georef_metadata_v3.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC07_Airborne_Videography/comp/LC07_videos_georef_metadata_v3.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
+            "identifier": "C2777292705-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "ecosystems",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1272",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-68.0 -14.5 -44.0 4.0",
+            "temporal": "1999-06-03T00:00:00Z/1999-06-21T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-07 Validation Overflight for Amazon Mosaics, Video, 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-M3SPEC-3-RDR-SMASS-V2.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Small Main-Belt Asteroid Spectrographic Survey over the visual range.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-m3spec-3-rdr-smass-v2.1_22rz-yjuu",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "863 benkoela",
                 "2558 viv",
@@ -3465,242 +3467,218 @@
                 "2503 liaoning",
                 "2538 vanderlinden"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-M3SPEC-3-RDR-SMASS-V2.1",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-m3spec-3-rdr-smass-v2.1_22rz-yjuu",
-            "description": "Small Main-Belt Asteroid Spectrographic Survey over the visual range.",
-            "title": "SMASS ASTEROID SURVEY V2.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "SMASS ASTEROID SURVEY V2.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP007-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP007 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nMTP007 part of it.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp007-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-PRL-MTP007-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-prl-mtp007-v2.0",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the PRELANDING\nMTP007 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-PRL-EDITED-V1.0 and is only\nMTP007 part of it.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP007 V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nPRL MTP007 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP2-0010-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "unknown",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Commissioning measurement covering the time 2004-09-11T19:30:04.500 to 2004-09-12T02:15:03.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp2-0010-v1.0_22sf-khwb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "unknown",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RSI-1%2F2%2F3-CVP2-0010-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rsi-1-2-3-cvp2-0010-v1.0_22sf-khwb",
-            "description": "This is a Commissioning measurement covering the time 2004-09-11T19:30:04.500 to 2004-09-12T02:15:03.500.",
-            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 2 0010 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CHECK RSI 1/2/3 COMMISSIONING 2 0010 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Johnson, M.S., E. Matthews, D. Bastviken, J. Du, and V. Genovese. 2022. Global-Gridded Daily Methane Emissions Climatology from Lake Systems, 2003-2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2008",
-            "issued": "2023-01-25",
-            "temporal": "2012-01-01T00:00:00Z/2012-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-09-11",
-            "keyword": [
-                "carbon flux",
-                "earth science",
-                "cryospheric indicators",
-                "biosphere",
-                "land surface/agriculture indicators",
-                "terrestrial hydrosphere",
-                "biospheric indicators",
-                "snow/ice",
-                "paleoclimate indicators",
-                "climate indicators",
-                "ecosystems"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2764746271-ORNL_CLOUD",
             "description": "This dataset provides global gridded information on lake surface area and open water CH4 emissions at a resolution of 0.25-degree x 0.25-degree for an annual climatology representative of the average conditions from 2003 to 2015. A compilation of flux data from 575 individual lake systems and 893 aggregated flux values were used, and each flux measurement was classified into one of seven ecoclimatic types. Ice-cover-regulated emission seasonality was derived from satellite microwave observations of ice cover phenology and freeze-thaw dynamics. Global lake area was determined from the merger of HydroLAKES and Climate Change Initiative Inland-Water (CCI-IW) remote-sensing data, and lakes were classified into ecoclimatic regions to facilitate linking these types with ecosystem-specific CH4 measurements in the flux compilation. Exploratory estimates of fluxes associated with ice melt and with spring and fall water-column turnover are also included. The data are provided in NetCDF format.",
-            "graphic-preview-description": "a) Lake area density (fraction of cell area) and b) ecoclimatic lake type classification. White space indicates cells with no lakes present.",
-            "title": "Global-Gridded Daily Methane Emissions Climatology from Lake Systems, 2003-2015",
-            "graphic-preview-file": "https://daac.ornl.gov/CLIMATE/guides/Global_Lakes_Methane_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/Global_Lakes_Methane/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_climate/Global_Lakes_Methane/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/Global_Lakes_Methane.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/Global_Lakes_Methane.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2008",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2008",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.earthdata.nasa.gov/",
-                    "description": "USE SERVICE API",
                     "@type": "dcat:Distribution",
+                    "description": "USE SERVICE API",
+                    "downloadURL": "https://opendap.earthdata.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/Global_Lakes_Methane/comp/Global_Lakes_Methane.pdf",
-                    "description": "Global-Gridded Daily Methane Emissions Climatology from Lake Systems, 2003-2015: Global_Lakes_Methane.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Global-Gridded Daily Methane Emissions Climatology from Lake Systems, 2003-2015: Global_Lakes_Methane.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_climate/Global_Lakes_Methane/comp/Global_Lakes_Methane.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/Global_Lakes_Methane_Fig1.jpg",
-                    "description": "a) Lake area density (fraction of cell area) and b) ecoclimatic lake type classification. White space indicates cells with no lakes present.",
                     "@type": "dcat:Distribution",
+                    "description": "a) Lake area density (fraction of cell area) and b) ecoclimatic lake type classification. White space indicates cells with no lakes present.",
+                    "downloadURL": "https://daac.ornl.gov/CLIMATE/guides/Global_Lakes_Methane_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "a) Lake area density (fraction of cell area) and b) ecoclimatic lake type classification. White space indicates cells with no lakes present.",
+            "graphic-preview-file": "https://daac.ornl.gov/CLIMATE/guides/Global_Lakes_Methane_Fig1.jpg",
+            "identifier": "C2764746271-ORNL_CLOUD",
+            "issued": "2023-01-25",
+            "keyword": [
+                "carbon flux",
+                "earth science",
+                "cryospheric indicators",
+                "biosphere",
+                "land surface/agriculture indicators",
+                "terrestrial hydrosphere",
+                "biospheric indicators",
+                "snow/ice",
+                "paleoclimate indicators",
+                "climate indicators",
+                "ecosystems"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2008",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-09-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-01T00:00:00Z/2012-12-31T23:59:59Z",
             "theme": [
                 "Climate",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global-Gridded Daily Methane Emissions Climatology from Lake Systems, 2003-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3537",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Schwartz, M., Livesey, N., Read, W., and Fuller, R.. 2021-04-29. ML3MBGPH. Version 005. MLS/Aura Level 3 Monthly Binned Geopotential Height (GPH) on Assorted Grids V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA/3537. https://disc.gsfc.nasa.gov/datacollection/ML3MBGPH_005.html. Digital Science Data.",
-            "issued": "2021-04-29",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-04-29",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "altitude"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NATHANIEL LIVESEY",
                 "hasEmail": "mailto:livesey@mls.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2042567845-GES_DISC",
-            "description": "ML3MBGPH is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for geopotential height (GPH) derived from radiances measured by the 118 and 240 GHz radiometers. The data version is 5.1. Data coverage is from August 2005 to current. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is between 261 and 0.001 hPa, and the vertical resolution varies between ~3.6 and 6 km. Users of the ML3MBGPH data product should read chapter 4 and section 3.8 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML3MBGPH",
             "creator": "Schwartz, M., Livesey, N., Read, W., and Fuller, R.",
-            "title": "MLS/Aura Level 3 Monthly Binned Geopotential Height (GPH) on Assorted Grids V005 (ML3MBGPH) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBGPH_005.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML3MBGPH is the EOS Aura Microwave Limb Sounder (MLS) monthly binned on various vertical grids product for geopotential height (GPH) derived from radiances measured by the 118 and 240 GHz radiometers. The data version is 5.1. Data coverage is from August 2005 to current. Spatial coverage is near-global (-82 to +82 degrees latitude) at a spatial resolution of 4 degrees latitude by 5 degrees longitude. The recommended useful vertical range is between 261 and 0.001 hPa, and the vertical resolution varies between ~3.6 and 6 km. Users of the ML3MBGPH data product should read chapter 4 and section 3.8 of the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data files are archived in the netCDF4 format, which is also compatible with HDF5 readers and tools. Each file contains six group objects: lat-lon map vs pressure, lat vs pressure zonal mean, lat-lon map vs theta, lat vs theta zonal mean, equivalent lat vs theta zonal mean, and vortex average vs theta. Each group has a set of data (average, min, max, std dev, rms) and geolocation fields, grid attributes, and metadata.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3537",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA%2F3537",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -3710,115 +3688,113 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBGPH_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML3MBGPH_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBGPH.005/",
-                    "description": "Access the data via HTTPS..",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS..",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level3/ML3MBGPH.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBGPH.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_MLS_Level3/ML3MBGPH.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBGPH_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML3MBGPH_005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/v5-0_data_quality_document.pdf",
-                    "description": "Data Quality and Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Quality and Description Document",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/v5-0_data_quality_document.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mls.jpl.nasa.gov/publications.php",
-                    "description": "List of publications.",
                     "@type": "dcat:Distribution",
+                    "description": "List of publications.",
+                    "downloadURL": "https://mls.jpl.nasa.gov/publications.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mls.jpl.nasa.gov/forms/reguser.php",
-                    "description": "Users are encouraged to register with the MLS science team to obtain updates and information about this data product.",
                     "@type": "dcat:Distribution",
+                    "description": "Users are encouraged to register with the MLS science team to obtain updates and information about this data product.",
+                    "downloadURL": "https://mls.jpl.nasa.gov/forms/reguser.php",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://mls.jpl.nasa.gov/data/eos_algorithm_atbd.pdf",
-                    "description": "EOS MLS Retrieval Process Algorithm Theoretical Basis",
                     "@type": "dcat:Distribution",
+                    "description": "EOS MLS Retrieval Process Algorithm Theoretical Basis",
+                    "downloadURL": "https://mls.jpl.nasa.gov/data/eos_algorithm_atbd.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mls.jpl.nasa.gov/",
-                    "description": "MLS Science Team Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "MLS Science Team Home Page.",
+                    "downloadURL": "https://mls.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML3MBGPH_005.png",
+            "identifier": "C2042567845-GES_DISC",
+            "issued": "2021-04-29",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA/3537",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-04-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ML3MBGPH",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 3 Monthly Binned Geopotential Height (GPH) on Assorted Grids V005 (ML3MBGPH) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://spotthestation.nasa.gov",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-03-02",
-            "temporal": "2021-03-02T00:00:00Z/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "coords",
-                "coordinates",
-                "trajectory",
-                "topo",
-                "station",
-                "space",
-                "location",
-                "iss",
-                "international",
-                "ephemeris"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Scott Goodwin",
                 "hasEmail": "mailto:scott.goodwin@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "TOPO"
-            },
-            "identifier": "nasa-iss-data_2021-03-02",
+            "dataQuality": true,
             "description": "This data represents the best estimated real-time trajectory and local sightings opportunities for the International Space Station (ISS) as generated by the Trajectory Operations and Planning (TOPO) flight controllers at Johnson Space Center.",
-            "title": "ISS_COORDS_2021-03-02",
-            "programCode": [
-                "026:004"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3941,882 +3917,880 @@
                     "title": "XMLsightingData_natparksUSA02"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "nasa-iss-data_2021-03-02",
+            "issued": "2021-03-02",
+            "keyword": [
+                "coords",
+                "coordinates",
+                "trajectory",
+                "topo",
+                "station",
+                "space",
+                "location",
+                "iss",
+                "international",
+                "ephemeris"
+            ],
+            "landingPage": "https://spotthestation.nasa.gov",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P1D",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:004"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "TOPO"
+            },
+            "temporal": "2021-03-02T00:00:00Z/P1D",
             "theme": [
                 "Space Science"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ISS_COORDS_2021-03-02"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3YCMVN_L3.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2012-09-20. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Terra/MISR/MI3YCMVN_L3.002. https://asdc.larc.nasa.gov/project/MISR.",
-            "issued": "2012-07-30",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Diner",
                 "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C194517136-LARC",
             "description": "MI3YCMVN_2 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 3 Cloud Motion Vector yearly Product in netCDF format version 2. It contains retrievals of cloud motion determined by geometrically triangulating the position and motion of cloud features observed by MISR from multiple perspectives and times during the overpass of the Terra platform over each cloud scene. Estimates of cloud motion are a valuable proxy observation of the horizontal atmospheric wind field at the retrieved altitude of the cloud. Data collection for this product is ongoing.\r\rThe MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward, and four cameras pointing aftward. It takes seven minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally Gaussian, centered at 443, 555, 670, and 865 nm.\r\rMISR itself is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the affects of sunlight on Earth, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Cloud Motion Vector yearly Product in netCDF format V002",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3YCMVN_L3.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTerra%2FMISR%2FMI3YCMVN_L3.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C194517136-LARC",
-                    "description": "Earthdata Search for MI3YCMVN_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MI3YCMVN_2 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C194517136-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
-                    "description": "NASA EOS ATB Documents: MISR",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MISR",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v50_RevS.pdf",
-                    "description": "Data Product Specification for MISR - Revision S, April 15, 2011   ",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR - Revision S, April 15, 2011   ",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v50_RevS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "description": "ASDC Data and Information for MISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/",
-                    "description": "MISR project home page",
                     "@type": "dcat:Distribution",
+                    "description": "MISR project home page",
+                    "downloadURL": "https://misr.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR/cgi-bin/MISR/main.cgi",
-                    "description": "MISR Order and Customization Tool",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Order and Customization Tool",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR/cgi-bin/MISR/main.cgi",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3YCMVN.002/contents.html",
-                    "description": "OPeNDAP data access for MI3YCMVN_2",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MI3YCMVN_2",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MI3YCMVN.002/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_CMV_V002.pdf",
-                    "description": "Data Product Specification for the MISR Cloud Motion Vector Product - Incorporating the Science Data Processing Interface Control Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for the MISR Cloud Motion Vector Product - Incorporating the Science Data Processing Interface Control Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_CMV_V002.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_CMV_Product.pdf",
-                    "description": "MISR Cloud Motion Vector Quality Statement - September 30, 2014",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Cloud Motion Vector Quality Statement - September 30, 2014",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_CMV_Product.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MISR",
-                    "description": "NASA Earthdata Forum - MISR Project Specific Forum",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - MISR Project Specific Forum",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MISR",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MI3YCMVN_L3.002",
-                    "description": "DOI data set landing page for MI3YCMVN_2",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MI3YCMVN_2",
+                    "downloadURL": "https://doi.org/10.5067/Terra/MISR/MI3YCMVN_L3.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
-                    "description": "MISR Peer-Reviewed Publications",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Peer-Reviewed Publications",
+                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3YCMVN.002/",
-                    "description": "ASDC Direct Data Download for MI3YCMVN.002",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MI3YCMVN.002",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MI3YCMVN.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/misr_loc/misr_date_orbit.cgi",
-                    "description": "MISR Orbit Tool",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Orbit Tool",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/misr_loc/misr_date_orbit.cgi",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR_BROWSE_INFO/",
-                    "description": "MISR Browse Tool",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Browse Tool",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/MISR_BROWSE_INFO/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc.html",
-                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc.html",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/LarcECSColL3newCloud.cgi",
-                    "description": "MISR Processing Status: Level 3 New Cloud Motion Vector Product",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Processing Status: Level 3 New Cloud Motion Vector Product",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/LarcECSColL3newCloud.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/ecs_pge_history_L3new_monthly_PR.cgi",
-                    "description": "MISR Level 3 New Monthly, Seasonal and Annual Production Report",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 3 New Monthly, Seasonal and Annual Production Report",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/public/cgi-bin/DUE/ecs_pge_history_L3new_monthly_PR.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
-                    "description": "MISR Science Data Product Guide - May 7, 2012",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Science Data Product Guide - May 7, 2012",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/tools-and-services",
-                    "description": "Links to tools available through the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Links to tools available through the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/tools-and-services",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
-                    "description": "MISR Paths Tool - Direct File Download (.kml)",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Paths Tool - Direct File Download (.kml)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2015.pdf",
-                    "description": "Overview of MISR Data at the ASDC, 2015",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of MISR Data at the ASDC, 2015",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
-                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/overview_misr.pdf",
-                    "description": "Multi-angle Imaging SpectroRadiometer (MISR) Overview Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-angle Imaging SpectroRadiometer (MISR) Overview Fact Sheet",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/overview_misr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/observing_concept.pdf",
-                    "description": "MISR Observing Concept Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Observing Concept Fact Sheet",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/observing_concept.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.ms-powerpoint",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/obtaining_misr_data.ppt",
-                    "description": "Obtaining MISR Data and Information, Presented by Jeff Walter Atmospheric Science Data Center - April 17, 2009 - Direct File Download (.ppt)",
                     "@type": "dcat:Distribution",
+                    "description": "Obtaining MISR Data and Information, Presented by Jeff Walter Atmospheric Science Data Center - April 17, 2009 - Direct File Download (.ppt)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/obtaining_misr_data.ppt",
+                    "mediaType": "application/vnd.ms-powerpoint",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_workshop.pdf",
-                    "description": "MISR Workshop Presentations, June 2002 - August 2010",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Workshop Presentations, June 2002 - August 2010",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_workshop.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropicalcyclone.jpl.nasa.gov/",
-                    "description": "JPL Tropical Cyclone Information System",
                     "@type": "dcat:Distribution",
+                    "description": "JPL Tropical Cyclone Information System",
+                    "downloadURL": "https://tropicalcyclone.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.google.com/earth/",
-                    "description": "Google Earth",
                     "@type": "dcat:Distribution",
+                    "description": "Google Earth",
+                    "downloadURL": "https://www.google.com/earth/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_Cloud_V001.pdf",
-                    "description": "Data Product Specification for the MISR Level 2 Cloud Product - Incorporating the Science Data Processing Interface Control Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for the MISR Level 2 Cloud Product - Incorporating the Science Data Processing Interface Control Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_Cloud_V001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/90764/looking-at-the-moon-to-better-see-earth",
-                    "description": "NASA Earth Observatory Article: Looking at the Moon to Better See Earth - Terra satellite performs manuver that allows all nine of MISR's camera to capture images of the moon.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Looking at the Moon to Better See Earth - Terra satellite performs manuver that allows all nine of MISR's camera to capture images of the moon.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/90764/looking-at-the-moon-to-better-see-earth",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://photojournal.jpl.nasa.gov/catalog/PIA21945",
-                    "description": "NASA JPL Photojournal: New Images of Irma's Towering Clouds - MISR passes over Irma over the Dominican Republic as a Category 5 hurricane.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Photojournal: New Images of Irma's Towering Clouds - MISR passes over Irma over the Dominican Republic as a Category 5 hurricane.",
+                    "downloadURL": "https://photojournal.jpl.nasa.gov/catalog/PIA21945",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Earthquake",
-                    "description": "NASA Earth Observatory Article: Squeezing Water from Rock\u00a0-\u00a0Survivors of the New Madrid earthquakes reported not only intense ground shaking and land movement, but also an unfamiliar phenomenon of water and sand spouting up through cracks in the Earth's surface.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Squeezing Water from Rock\u00a0-\u00a0Survivors of the New Madrid earthquakes reported not only intense ground shaking and land movement, but also an unfamiliar phenomenon of water and sand spouting up through cracks in the Earth's surface.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Earthquake",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/tracking",
-                    "description": "NASA Earth Observatory Article: Tracking Clouds\u00a0-\u00a0Tune in to the evening weather report on any given day, and you'll no doubt see satellite images of clouds.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Tracking Clouds\u00a0-\u00a0Tune in to the evening weather report on any given day, and you'll no doubt see satellite images of clouds.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/tracking",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
-                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
+                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.html",
-                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge33b.html",
-                    "description": "ASDC List of MISR Level 3 Cloud Motion Vector Versioning for Cloud Motion Vector Product (CMV) - Monthly, Quarterly, and Yearly products",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR Level 3 Cloud Motion Vector Versioning for Cloud Motion Vector Product (CMV) - Monthly, Quarterly, and Yearly products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge33b.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.html",
-                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.html",
-                    "description": "ASDC Overview of MISR Data Versioning Index",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR Data Versioning Index",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.html",
-                    "description": "MISR Quality Statements - September 30, 2014",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements - September 30, 2014",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_new.html",
-                    "description": "MISR Quality Statements - September 30, 2014",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements - September 30, 2014",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_new.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/dps.html",
-                    "description": "Data Product Specification for MISR Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/dps.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.html",
-                    "description": "Data Product Specification for Specific Products MISR Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for Specific Products MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v42_RevP.pdf",
-                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007 ",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007 ",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v42_RevP.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-                    "description": "ASDC List of MISR Imagery and Articles",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR Imagery and Articles",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://terra.nasa.gov/?section=60",
-                    "description": "TERRA Overview",
                     "@type": "dcat:Distribution",
+                    "description": "TERRA Overview",
+                    "downloadURL": "https://terra.nasa.gov/?section=60",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C194517136-LARC",
+            "issued": "2012-07-30",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Terra/MISR/MI3YCMVN_L3.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-06-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Cloud Motion Vector yearly Product in netCDF format V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-51",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-51.",
-            "issued": "2019-05-08",
-            "temporal": "2006-06-12T00:00:00Z/2023-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-30",
-            "keyword": [
-                "earth science",
-                "clouds",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JACQUES PELON",
                 "hasEmail": "mailto:jacques.pelon@aero.jussieu.fr"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2762334323-LARC_ASDC",
             "description": "CAL_IIR_L2_Track-Standard-V4-51 is the Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) Infrared Imaging Radiometer (IIR) Level 2 Track, Version 4-51 data product. Data for this product was collected using the CALIPSO IIR instrument. This product contains emissivity and cloud particle data related to pixels co-located to the lidar track. The version of this product was changed to V4-51 to account for a change in the operating system of the CALIPSO production cluster.\r\n\r\nCALIPSO was launched on April 28, 2006, to study the impact of clouds and aerosols on the Earth's radiation budget and climate. The CALIPSO satellite comprises three instruments: Cloud-Aerosol Lidar with Orthogonal Polarization (CALIOP), IIR, and Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency CNES (Centre national d'\u00e9tudes spatiales).",
-            "graphic-preview-description": "Mission Logo",
-            "title": "CALIPSO Infrared Imaging Radiometer (IIR) Level 2 Track, V4-51",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/calipso.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIR%2FCALIPSO%2FCAL_IIR_L2_Track-Standard-V4-51",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIIR%2FCALIPSO%2FCAL_IIR_L2_Track-Standard-V4-51",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/",
-                    "description": "CALIPSO Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Project Home Page",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CALIPSO",
-                    "description": "ASDC Data and Information for CALIPSO",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CALIPSO",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CALIPSO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_iir_l2_trackswath_v4-51_qs.php",
-                    "description": "Detailed quality summary of the V4.51 IIR Level 2 data product",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed quality summary of the V4.51 IIR Level 2 data product",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/qs/cal_iir_l2_trackswath_v4-51_qs.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_desc/cal_iir_l2_track_v4-51_desc.php",
-                    "description": "User's guide description document of the V4.51 IIR Level 2 Track data product",
                     "@type": "dcat:Distribution",
+                    "description": "User's guide description document of the V4.51 IIR Level 2 Track data product",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/data_desc/cal_iir_l2_track_v4-51_desc.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x96.pdf",
-                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.96",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Management System - Data Products Catalog - Release 4.96",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/CALIPSO_DPC_Rev4x96.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
-                    "description": "CALIPSO - List of publications",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of publications",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/publications.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
-                    "description": "CALIPSO - Data Availability Site",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data Availability Site",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/tools/data_avail/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
-                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - Data User's Guide - Browse Image Tutorial",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/browse/index.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/project_documentation.php",
-                    "description": "CALIPSO - List of project documentation (Data Products Catalog and ATBDs)",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO - List of project documentation (Data Products Catalog and ATBDs)",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/project_documentation.php",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
-                    "description": "CALIPSO Data User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/faq.php",
-                    "description": "CALIPSO Data User\u2019s Guide - Frequently Asked Questions",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Data User\u2019s Guide - Frequently Asked Questions",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/resources/calipso_users_guide/faq.php",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
-                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO: Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations Fact Sheet",
+                    "downloadURL": "https://www.nasa.gov/pdf/137028main_FS-2005-09-120-LaRC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://calipso.cnes.fr/fr",
-                    "description": "French (CNES) CALIPSO Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "French (CNES) CALIPSO Home Page",
+                    "downloadURL": "https://calipso.cnes.fr/fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.icare.univ-lille.fr",
-                    "description": "ICARE Data and Services Center Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ICARE Data and Services Center Home Page",
+                    "downloadURL": "https://www.icare.univ-lille.fr",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/tools-and-services",
-                    "description": "Links to tools available through the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Links to tools available through the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/tools-and-services",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
-                    "description": "NASA Mission Overview of CALIPSO",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Mission Overview of CALIPSO",
+                    "downloadURL": "https://www.nasa.gov/mission_pages/calipso/main/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
-                    "description": "Overview of CALIPSO Data Product Maturity",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of CALIPSO Data Product Maturity",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/calipso/data_product_maturity.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
-                    "description": "CALIPSO Products Overview",
                     "@type": "dcat:Distribution",
+                    "description": "CALIPSO Products Overview",
+                    "downloadURL": "https://www-calipso.larc.nasa.gov/products/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2762334323-LARC_ASDC",
-                    "description": "Earthdata Search for CAL_IIR_L2_Track-Standard-V4-51_V4-51 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAL_IIR_L2_Track-Standard-V4-51_V4-51 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2762334323-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-51",
-                    "description": "DOI data set landing page for CAL_IIR_L2_Track-Standard-V4-51_V4-51",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAL_IIR_L2_Track-Standard-V4-51_V4-51",
+                    "downloadURL": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-51",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/calipso.png",
-                    "description": "Mission Logo",
                     "@type": "dcat:Distribution",
+                    "description": "Mission Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/calipso.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/IIR_L2_Track-Standard-V4-51/",
-                    "description": "ASDC Direct Data Download for CAL_IIR_L2_Track-Standard-V4-51_V4-51",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAL_IIR_L2_Track-Standard-V4-51_V4-51",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CALIPSO/IIR_L2_Track-Standard-V4-51/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/IIR_L2_Track-Standard-V4-51/contents.html",
-                    "description": "OPeNDAP data access for CAL_IIR_L2_Track-Standard-V4-51_V4-51",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CAL_IIR_L2_Track-Standard-V4-51_V4-51",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CALIPSO/IIR_L2_Track-Standard-V4-51/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Mission Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/calipso.png",
+            "identifier": "C2762334323-LARC_ASDC",
+            "issued": "2019-05-08",
+            "keyword": [
+                "earth science",
+                "clouds",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/IIR/CALIPSO/CAL_IIR_L2_Track-Standard-V4-51",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-06-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2006-06-12T00:00:00Z/2023-06-30T23:59:59.999Z",
             "theme": [
                 "CALIPSO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CALIPSO Infrared Imaging Radiometer (IIR) Level 2 Track, V4-51"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-3-CR5-CALIBRATED-V9.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "international rosetta mission",
-                "checkout"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the CRUISE 5\n(CR5) phase from February 24, 2010 until April 27, 2010 of the ROSETTA\norbiter magnetometer RPCMAG.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-3-cr5-calibrated-v9.0_2347-smt9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "checkout"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-RPCMAG-3-CR5-CALIBRATED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rpcmag-3-cr5-calibrated-v9.0_2347-smt9",
-            "description": "This dataset contains CALIBRATED (CODMAC LEVEL 3) DATA of the CRUISE 5\n(CR5) phase from February 24, 2010 until April 27, 2010 of the ROSETTA\norbiter magnetometer RPCMAG.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER CHECK RPCMAG 3 CR5 CALIBRATED V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER CHECK RPCMAG 3 CR5 CALIBRATED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SWTPR-GLID1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SWOT pre-launch field campaign. 2022-05-31. GPS sea surface height, Conductivity, Temperature and Depth (CTD) data from the 2019-2020 SWOT pre-launch field campaign. Version 1.0. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/JPL/PODAAC. https://doi.org/10.5067/SWTPR-GLID1. https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf .",
-            "issued": "2022-03-02",
-            "temporal": "2019-09-05T00:00:00Z/2019-12-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-28",
-            "references": [
-                "https://doi.org/10.1175/jtech-d-21-0039.1"
-            ],
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean pressure",
-                "ocean temperature",
-                "salinity/density"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2229635647-POCLOUD",
-            "description": "This dataset provides the Conductivity, Temperature, and Depth measurements carried by a Slocum glider. The measurements were collected during the 2019-2020 SWOT prelaunch field campaign conducted near the SWOT crossover location in the California Currents, 300km west of Monterey, California, USA. It has 883 CTD profiles with glider diving depths varying between 500 m and 1000 m.  Details can be found in the user guide and the journal reference given in the documentation section.",
-            "graphic-preview-description": "Thumbnail",
             "creator": "SWOT pre-launch field campaign",
-            "title": "SWOT 2019-2020 Prelaunch Oceanography Field Campaign Rutgers Slocum Gliders",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_GLIDER_V1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides the Conductivity, Temperature, and Depth measurements carried by a Slocum glider. The measurements were collected during the 2019-2020 SWOT prelaunch field campaign conducted near the SWOT crossover location in the California Currents, 300km west of Monterey, California, USA. It has 883 CTD profiles with glider diving depths varying between 500 m and 1000 m.  Details can be found in the user guide and the journal reference given in the documentation section.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWTPR-GLID1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSWTPR-GLID1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/web-misc/SWOT/SWOT_Prelaunch_2019_2020/User_Guide_SWOT_Prelaunch_2019_2020.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://podaac.jpl.nasa.gov/swot",
-                    "description": "Field Campaign and Instrument Overview for SWOT",
                     "@type": "dcat:Distribution",
+                    "description": "Field Campaign and Instrument Overview for SWOT",
+                    "downloadURL": "http://podaac.jpl.nasa.gov/swot",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_GLIDER_V1.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_GLIDER_V1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/CitingPODAAC",
-                    "description": "Data Use and Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "Data Use and Citation Policy",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/CitingPODAAC",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2229635647-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2229635647-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2229635647-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2229635647-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic data readers",
                     "@type": "dcat:Distribution",
+                    "description": "Generic data readers",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/SWOT_PRELAUNCH_L2_GLIDER_V1.jpg",
+            "identifier": "C2229635647-POCLOUD",
+            "issued": "2022-03-02",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean pressure",
+                "ocean temperature",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/SWTPR-GLID1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-12-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1175/jtech-d-21-0039.1"
+            ],
             "spatial": "-125.2 35.8 -125.0 36.2",
+            "temporal": "2019-09-05T00:00:00Z/2019-12-28T23:59:59.999Z",
             "theme": [
                 "SWOT",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SWOT 2019-2020 Prelaunch Oceanography Field Campaign Rutgers Slocum Gliders"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1627523794-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2004), Terra/MISR Level 3, Component Global Land Product covering a day subset for the UAE region, version 4, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
-            "issued": "2019-07-31",
-            "temporal": "2004-07-06T00:00:00Z/2004-10-12T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-01",
-            "keyword": [
-                "vegetation",
-                "atmosphere",
-                "atmospheric radiation",
-                "biosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Diner",
                 "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1627523794-LARC",
             "description": "The Multi-angle Imaging SpectroRadiometer (MISR) Level 3 Component Global Land Product covering a day subset for the UAE region V004 contains a daily statistical summary of directional hemispherical reflectance (DHR), photosynthetically active spectral region (DHR-PAR), DHR for near-infrared band (DHR-NIR), fractional absorbed photosynthetically active radiation (FPAR), DHR-based normalized difference vegetation index (NDVI) and land surface bidirectional reflectance factor (BRF) model parameters, classified into six vegetated and one non-vegetated types. This data product is a regional summary of the Level 2 land/surface parameters of interest averaged over a day and reported on a geographic grid, with resolution of 0.5 degree by 0.5 degree. The MISR instrument consists of nine pushbroom cameras which measure radiance in four spectral bands. Global coverage is achieved in nine days. The cameras are arranged with one camera pointing toward the nadir, four cameras pointing forward and four cameras pointing aftward. It takes 7 minutes for all nine cameras to view the same surface location. The view angles relative to the surface reference ellipsoid, are 0, 26.1, 45.6, 60.0, and 70.5 degrees. The spectral band shapes are nominally gaussian, centered at 443, 555, 670, and 865 nm.",
-            "title": "MISR Level 3 Component Global Land Product covering a day subset for the UAE region V004",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1627523794-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1627523794-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1627523794-LARC",
+            "issued": "2019-07-31",
+            "keyword": [
+                "vegetation",
+                "atmosphere",
+                "atmospheric radiation",
+                "biosphere",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1627523794-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-07-06T00:00:00Z/2004-10-12T23:59:59Z",
             "theme": [
                 "UAE_2004",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Component Global Land Product covering a day subset for the UAE region V004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/0JRNK6HDB9ZG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Charles Gatebe; Michael King; Rajesh Poudyal. 2019-05-29. CAR_CLASIC_BRDF. Version 2. CAR CLASIC BRDF Measurements V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/0JRNK6HDB9ZG. https://disc.gsfc.nasa.gov/datacollection/CAR_CLASIC_BRDF_2.html.",
-            "issued": "2019-01-27",
-            "temporal": "2007-06-13T00:00:00Z/2007-06-25T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-01-27",
-            "keyword": [
-                "atmosphere",
-                "ocean optics",
-                "atmospheric radiation",
-                "land surface",
-                "earth science",
-                "surface radiative properties",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHARLES GATEBE",
                 "hasEmail": "mailto:gatebe@climate.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1617621682-GES_DISC",
-            "description": "CLASIC (Cloud and Land Surface Interaction Campaign) focuses on advancing the understanding of how land surface processes influence cumulus convection. CLASIC was conducted in the Southern Great Plains (SGP &#8211; a region comprising Kansas, Oklahoma, and Texas) of the United States during June 2007. The SGP site consists of in situ and remote-sensing instrument clusters arrayed across approximately 55,000 square miles (143,000 square kilometers) in north-central Oklahoma, making it the largest and most extensive climate research field site in the world. The CAR flew aboard Sky Research Jetstream-31 and measured spectral and angular distribution of scattered light by clouds and aerosols, and provided bidirectional reflectance of various surfaces, and imagery of cloud and Earth surface features. By making such diverse measurements, our goal is to widen the audience of potential end-users and to foster collaborations among campaign participants and with outside users.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CAR_CLASIC_BRDF",
             "creator": "Charles Gatebe; Michael King; Rajesh Poudyal",
-            "title": "CAR CLASIC BRDF Measurements V2 (CAR_CLASIC_BRDF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_CLASIC_L1C_1.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "CLASIC (Cloud and Land Surface Interaction Campaign) focuses on advancing the understanding of how land surface processes influence cumulus convection. CLASIC was conducted in the Southern Great Plains (SGP &#8211; a region comprising Kansas, Oklahoma, and Texas) of the United States during June 2007. The SGP site consists of in situ and remote-sensing instrument clusters arrayed across approximately 55,000 square miles (143,000 square kilometers) in north-central Oklahoma, making it the largest and most extensive climate research field site in the world. The CAR flew aboard Sky Research Jetstream-31 and measured spectral and angular distribution of scattered light by clouds and aerosols, and provided bidirectional reflectance of various surfaces, and imagery of cloud and Earth surface features. By making such diverse measurements, our goal is to widen the audience of potential end-users and to foster collaborations among campaign participants and with outside users.\n\nThis data set consists of observations made with the CAR instrument and includes values for bidirectional reflectance factor at varying spectral bands.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0JRNK6HDB9ZG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F0JRNK6HDB9ZG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -4826,69 +4800,97 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_CLASIC_BRDF_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CAR_CLASIC_BRDF_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://car.gsfc.nasa.gov/",
-                    "description": "CAR Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "CAR Project Home Page",
+                    "downloadURL": "https://car.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/hyrax/CAR/CAR_CLASIC_BRDF.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/hyrax/CAR/CAR_CLASIC_BRDF.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_CLASIC_BRDF.2/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/CAR/CAR_CLASIC_BRDF.2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CAR/CAR_BRDF_README-v2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CAR/CAR_BRDF_README-v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_CLASIC_BRDF",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CAR_CLASIC_BRDF",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CAR_CLASIC_L1C_1.jpg",
+            "identifier": "C1617621682-GES_DISC",
+            "issued": "2019-01-27",
+            "keyword": [
+                "atmosphere",
+                "ocean optics",
+                "atmospheric radiation",
+                "land surface",
+                "earth science",
+                "surface radiative properties",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/0JRNK6HDB9ZG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CAR_CLASIC_BRDF",
             "spatial": "-98.0795 34.9401 -97.0694 36.8193",
+            "temporal": "2007-06-13T00:00:00Z/2007-06-25T23:59:59.999Z",
             "theme": [
                 "CAR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAR CLASIC BRDF Measurements V2 (CAR_CLASIC_BRDF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI-C-HRII%2FHRIV%2FMRI%2FITS-6-DOC-SET-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set is the collection of documentation for the raw and calibrated data sets from the Deep Impact and EPOXI missions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-c-hrii-hriv-mri-its-6-doc-set-v2.0_23am-tteh",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "deep impact",
                 "wasp-3",
@@ -4905,61 +4907,36 @@
                 "9p/tempel 1 (1867 g1)",
                 "103p/hartley 2 (1986 e2)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI-C-HRII%2FHRIV%2FMRI%2FITS-6-DOC-SET-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-c-hrii-hriv-mri-its-6-doc-set-v2.0_23am-tteh",
-            "description": "This data set is the collection of documentation for the raw and calibrated data sets from the Deep Impact and EPOXI missions.",
-            "title": "DEEP IMPACT/EPOXI DOCUMENTATION SET V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT/EPOXI DOCUMENTATION SET V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://turbmodels.larc.nasa.gov/bradshaw.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://turbmodels.larc.nasa.gov/index.html"
-            ],
-            "keyword": [
-                "compressible",
-                "cases",
-                "turbulence",
-                "models",
-                "incompressible",
-                "flow"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Christopher Rumsey",
                 "hasEmail": "mailto:c.l.rumsey@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-847__3",
             "description": "This grouping contains more recent compressible-flow cases.",
-            "title": "Collaborative Testing of Turbulence Models: Other Flow Cases",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4967,516 +4944,515 @@
                     "mediaType": "application/x-gzip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-847__3",
+            "issued": "2018-06-25",
+            "keyword": [
+                "compressible",
+                "cases",
+                "turbulence",
+                "models",
+                "incompressible",
+                "flow"
+            ],
+            "landingPage": "http://turbmodels.larc.nasa.gov/bradshaw.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:023"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
+            ],
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Collaborative Testing of Turbulence Models: Other Flow Cases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/KKPPL39PEIGE",
             "citation": "Dan Goldberg at George Washington University. 2024-03-15. HAQ_TROPOMI_NO2_GLOBAL_M_L3. Version 2.4. HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) GLOBAL Monthly Level 3 0.1 x 0.1 Degree Gridded Data Version 2.4. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/KKPPL39PEIGE. https://disc.gsfc.nasa.gov/datacollection/HAQ_TROPOMI_NO2_GLOBAL_M_L3_2.4.html. Digital Science Data.",
-            "issued": "2024-05-15",
-            "temporal": "2019-01-01T00:00:00Z/2024-08-26T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-19",
-            "references": [
-                "https://doi.org/10.1029/2020EF001665"
-            ],
-            "keyword": [
-                "air quality",
-                "earth science",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Xiaohua Pan",
                 "hasEmail": "mailto:xiaohua.pan@nasa.gov"
             },
+            "creator": "Dan Goldberg at George Washington University",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C3087325222-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This product provides level 3 monthly averages of tropospheric Nitrogen dioxide (NO2) vertical column density derived from the level 2 Tropospheric Monitoring Instrument (TROPOMI) across the globe oversampled to a spatial resolution of 0.1\u02da x 0.1\u02da (~10 km2) using a consistent algorithm from the European Space Agency (ESA) version 2.4 that can be used for trend analysis of air pollution. The dataset record began in January 2019 and continues to the present. \n\nThis L3 product was developed by the George Washington University Air, Climate and Health Laboratory as part of the NASA Health Air Quality Applied Science Team (HAQAST) using Level 2 version 2.4 TROPOMI NO2 files from the ESA. The TROPOMI instrument on Sentinel-5 Precursor acquires tropospheric NO2 column contents from low Earth orbit (~824 km above ground level) once per day globally at approximately 13:30 local time.\n\nNO2 is an air pollutant that adversely affects the human respiratory system and leads to premature mortality. NO2 is also an important precursor for ozone and fine particulates, which also have severe health impacts. In urban areas, the majority of NO2 originates from anthropogenic NOx (=NO+NO2; most NOx is emitted as NO, which rapidly cycles to NO2) emissions during high-temperature fossil fuel combustion. Tropospheric NO2 vertical column contents are qualitatively representative of near-surface NO2 concentrations and NOx emissions in urban/polluted locations.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "HAQ_TROPOMI_NO2_GLOBAL_M_L3",
-            "creator": "Dan Goldberg at George Washington University",
-            "graphic-preview-description": "Sample image",
-            "title": "HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) GLOBAL Monthly Level 3 0.1 x 0.1 Degree Gridded Data Version 2.4 (HAQ_TROPOMI_NO2_GLOBAL_M_L3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKKPPL39PEIGE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKKPPL39PEIGE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4.png",
-                    "description": "Sample image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample image",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4/doc/README_TROPOMI_Level3_GLOBAL_TropNO2_DG_05282024.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4/doc/README_TROPOMI_Level3_GLOBAL_TropNO2_DG_05282024.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQ_TROPOMI_NO2_GLOBAL_M_L3_2.4.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/HAQ_TROPOMI_NO2_GLOBAL_M_L3_2.4.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/HAQAST/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQ_TROPOMI_NO2_GLOBAL_M_L3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=HAQ_TROPOMI_NO2_GLOBAL_M_L3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HAQAST/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto",
-                    "description": "Documentation with step-by-step instructions on accessing and reading data at GES DISC",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation with step-by-step instructions on accessing and reading data at GES DISC",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 }
             ],
+            "graphic-preview-description": "Sample image",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/HAQ_TROPOMI_NO2_GLOBAL_M_L3.2.4.png",
+            "identifier": "C3087325222-GES_DISC",
+            "issued": "2024-05-15",
+            "keyword": [
+                "air quality",
+                "earth science",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/KKPPL39PEIGE",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2020EF001665"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "HAQ_TROPOMI_NO2_GLOBAL_M_L3",
             "spatial": "-179.5 -60.0 179.5 75.0",
+            "temporal": "2019-01-01T00:00:00Z/2024-08-26T00:00:00Z",
             "theme": [
                 "HAQAST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HAQAST Sentinel-5P TROPOMI Nitrogen Dioxide (NO2) GLOBAL Monthly Level 3 0.1 x 0.1 Degree Gridded Data Version 2.4 (HAQ_TROPOMI_NO2_GLOBAL_M_L3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/535/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-02-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID SCHUSTER",
                 "hasEmail": "mailto:david.m.schuster@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_535",
             "description": "not available",
-            "title": "RSW-CFL3D-Schuster-Fine Grid",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/octet-stream",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW-CFL3D-Fine.g",
-                    "description": "RSW-CFL3D-Fine.g",
                     "@type": "dcat:Distribution",
+                    "description": "RSW-CFL3D-Fine.g",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/dataset/RSW-CFL3D-Fine.g",
+                    "mediaType": "application/octet-stream",
                     "title": "RSW-CFL3D-Fine.g"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_535",
+            "issued": "2012-02-13",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/535/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "RSW-CFL3D-Schuster-Fine Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-4-DND-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "2001 mars odyssey",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Odyssey GRS Derived Neutron Data (DND) data set includes prism counting rates, normalizations, corrections, and thermal, epithermal, and fast neutron counting rates derived from neutron data collected by the Neutron Spectrometer of the Odyssey GRS instrument suite.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-4-dnd-v1.0_23cg-iiyc",
+            "issued": "2018-06-26",
+            "keyword": [
+                "2001 mars odyssey",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-4-DND-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-4-dnd-v1.0_23cg-iiyc",
-            "description": "The Odyssey GRS Derived Neutron Data (DND) data set includes prism counting rates, normalizations, corrections, and thermal, epithermal, and fast neutron counting rates derived from neutron data collected by the Neutron Spectrometer of the Odyssey GRS instrument suite.",
-            "title": "ODY MARS GAMMA RAY SPECTROMETER 4 DND V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ODY MARS GAMMA RAY SPECTROMETER 4 DND V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/POC/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/POC/2022.",
-            "issued": "2022-09-14",
-            "temporal": "2012-01-02T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "oceans",
-                "ocean chemistry",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sdps@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C2340494429-OB_DAAC",
             "description": "The Visible and Infrared Imager/Radiometer Suite (VIIRS) is a multi-disciplinary instrument that is being flown on the Joint Polar Satellite System (JPSS) series of spacecraft, including the Suomi National Polar-orbiting Partnership (S-NPP) that launched in October 2011. JPSS is a multi-platform, multi-agency program that consolidates the polar orbiting spacecraft of NASA and the National Oceanic and Atmospheric Administration (NOAA). S-NPP is the initial spacecraft in this series, and VIIRS is the successor to MODIS for Earth science data product generation. VIIRS has 22 spectral bands ranging from 412 nm to 12 nm. There are 16 moderate-resolution bands (750m at nadir), 5 image-resolution bands (375m), and one day-night band (DNB).",
-            "title": "Suomi-NPP VIIRS Global Mapped Particulate Organic Carbon (POC) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FPOC%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSUOMI-NPP%2FVIIRS%2FL3M%2FPOC%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
-                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/",
-                    "description": "NASA Ocean Color Web - Processing History",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Processing History",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/citations/",
-                    "description": "NASA Ocean Color Web - Data Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Citation Policy",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/citations/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/POC/2022",
-                    "description": "VIIRS-Suomi-NPP L3M Particulate Organic Carbon (POC) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS-Suomi-NPP L3M Particulate Organic Carbon (POC) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/SUOMI-NPP/VIIRS/L3M/POC/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRS/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Suomi-NPP VIIRS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Suomi-NPP VIIRS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/VIIRS/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2340494429-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "oceans",
+                "ocean chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SUOMI-NPP/VIIRS/L3M/POC/2022",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-02T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suomi-NPP VIIRS Global Mapped Particulate Organic Carbon (POC) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRIMAG-3-EDR-HALLEY-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains the infrared images collected and archived by the International Halley Watch (IHW) Infrared Studies Network (IRSN). Raw and calibrated data are included, as well as calibration observations of standard stars. These data have been reformatted and the accompanying documentation updated in this revised version.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irimag-3-edr-halley-v2.0_23ev-men7",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "1p/halley 1 (1682 q1)",
                 "international halley watch",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRIMAG-3-EDR-HALLEY-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irimag-3-edr-halley-v2.0_23ev-men7",
-            "description": "This data set contains the infrared images collected and archived by the International Halley Watch (IHW) Infrared Studies Network (IRSN). Raw and calibrated data are included, as well as calibration observations of standard stars. These data have been reformatted and the accompanying documentation updated in this revised version.",
-            "title": "IHW COMET HALLEY INFRARED IMAGE DATA, V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY INFRARED IMAGE DATA, V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-RSS-5-LOS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "moon",
-                "lunar prospector"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation. For information on Lunar Prospector (LP) gravity investigations see [KONOPLIVETAL1998 CARRANZAETAL1999].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-rss-5-los-v1.0_23fq-gz7d",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "lunar prospector"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-RSS-5-LOS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-rss-5-los-v1.0_23fq-gz7d",
-            "description": "Line of Sight Acceleration Profile Data Records (LOSAPDR) consist of data from Doppler tracking of the orbiting spacecraft. The relative motion of the spacecraft and the earth-based radio receiver is measured very precisely, and known motions are removed a priori (i.e. earth rotation, planetary motions, spacecraft orbital motion, solar pressure, drag), leaving small velocity changes caused by variations in the mass distribution of the planet. The residual Doppler frequency shifts are linearly proportional to the component of velocity in the Earth direction. Numerical differentiation of these velocity residuals with respect to time produces line-of-sight (LOS) gravity. These measures are accelerations at spacecraft altitude which can be modeled for geophysical interpretation. For information on Lunar Prospector (LP) gravity investigations see [KONOPLIVETAL1998 CARRANZAETAL1999].",
-            "title": "LP L RSS LINE OF SIGHT ACCELERATION PROFILES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "LP L RSS LINE OF SIGHT ACCELERATION PROFILES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NKOACUH8VF34",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "IceBridge Scintrex CS-3 Cesium Magnetometer L0 Raw Magnetic Field, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NKOACUH8VF34.",
-            "issued": "2011-03-15",
-            "temporal": "2011-03-15T00:00:00Z/2012-05-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-05-17",
-            "keyword": [
-                "geomagnetism",
-                "solid earth",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Cochran",
                 "hasEmail": "mailto:jrc@ldeo.columbia.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386246579-NSIDCV0",
             "description": "This data set contains magnetic field readings and fluxgate values taken over Greenland using the Scintrex CS-3 Cesium Magnetometer. The data were collected as part of Operation IceBridge funded aircraft survey campaigns.",
-            "title": "IceBridge Scintrex CS-3 Cesium Magnetometer L0 Raw Magnetic Field, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNKOACUH8VF34",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNKOACUH8VF34",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IMCS30_LDEOcsMagRaw_v01/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/ICEBRIDGE/IMCS30_LDEOcsMagRaw_v01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NKOACUH8VF34",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NKOACUH8VF34",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NKOACUH8VF34",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NKOACUH8VF34",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246579-NSIDCV0",
+            "issued": "2011-03-15",
+            "keyword": [
+                "geomagnetism",
+                "solid earth",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/NKOACUH8VF34",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-05-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-74.0 59.0 -12.0 83.0",
+            "temporal": "2011-03-15T00:00:00Z/2012-05-17T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "IceBridge Scintrex CS-3 Cesium Magnetometer L0 Raw Magnetic Field, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-ESC3-SAMPLES-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCOMET ESCORT 3 mission phase. This release supersedes version 2.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-esc3-samples-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-MIDAS-3-ESC3-SAMPLES-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-midas-3-esc3-samples-v3.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCOMET ESCORT 3 mission phase. This release supersedes version 2.0.",
-            "title": "ROSETTA-ORBITER 67P MIDAS 3 ESC3 SAMPLES V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P MIDAS 3 ESC3 SAMPLES V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/14396",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2012-01-01",
-            "temporal": "2012-01-01T00:00:00Z/2020-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://techport.nasa.gov/home",
-                "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
-                "http://techport.nasa.gov/fetchFile?objectId=6561",
-                "http://techport.nasa.gov/fetchFile?objectId=3456",
-                "http://techport.nasa.gov/fetchFile?objectId=3447",
-                "http://techport.nasa.gov/fetchFile?objectId=6584",
-                "http://techport.nasa.gov/fetchFile?objectId=6560",
-                "http://techport.nasa.gov/fetchFile?objectId=3448"
-            ],
-            "keyword": [
-                "project",
-                "armstrong flight research center",
-                "active"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Claudia Herrera",
                 "hasEmail": "mailto:claudia.herrera-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Chief Technologist"
-            },
-            "identifier": "TECHPORT_14396",
             "description": "&lt;p&gt;This research is part of an innovative effort to use hyperelastic materials&amp;nbsp;to produce flexible and seamless aircraft structures that reduce drag&amp;nbsp;and minimize acoustic noise. Hyperelastic materials, such as rubber,&amp;nbsp;have a non-linear stress-strain relationship, which often complicates the&amp;nbsp;modeling process. Therefore, CIF funding is being used to gain increased&amp;nbsp;knowledge regarding the properties of hyperelastic materials and develop&amp;nbsp;improved finite element analysis (FEA) models. This research effort&amp;nbsp;builds on the knowledge gained from the Adaptive Compliant Trailing&amp;nbsp;Edge (ACTE) experimental flight research project. The ACTE project&amp;nbsp;will demonstrate the structure technology in flight, and this technology&amp;nbsp;has been shown to improve aircraft aerodynamic efficiency and reduce&amp;nbsp;airport-area noise generated during takeoffs and landings.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Work to date:&lt;/strong&gt; The Armstrong development team has fabricated the biaxial&amp;nbsp;strain test hardware and completed initial bubble test planning. The team&amp;nbsp;is working to obtain biaxial strain properties and develop an FEA model&amp;nbsp;that simulates the material properties and failure characteristics. In 2014, the team fine-tuned the modeling by&amp;nbsp;comparing the predicted output to an actual bubble test of the material.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Partner:&lt;/strong&gt; FlexSys Inc. is the industry partner on this effort, as it owns the&amp;nbsp;design patent.&lt;/p&gt;&lt;p&gt;&lt;strong&gt;Benefits&lt;/strong&gt;&lt;/p&gt;&lt;ul&gt;&lt;li&gt;&lt;strong&gt;Economical:&lt;/strong&gt; Use of hyperelastic material&amp;nbsp;increases fuel efficiency by reducing drag&lt;/li&gt;&lt;li&gt;&lt;strong&gt;Quieter:&lt;/strong&gt; Novel wing flap reduces noise&amp;nbsp;associated with takeoffs and landings both in&amp;nbsp;the aircraft cabin and on the ground&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;&lt;strong&gt;Applications&lt;/strong&gt;&lt;/p&gt;&lt;ul&gt;&lt;li&gt;Aircraft wing flaps&lt;/li&gt;&lt;li&gt;Helicopter blades&lt;/li&gt;&lt;li&gt;Motor vehicles&lt;/li&gt;&lt;li&gt;Trains&lt;/li&gt;&lt;li&gt;Ships&lt;/li&gt;&lt;/ul&gt;",
-            "title": "Fundamental Hyperelastic Material Study Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/14396",
                     "mediaType": "application/xml"
                 }
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/14383",
-            "bureauCode": [
-                "026:00"
             ],
-            "issued": "2013-10-01",
-            "temporal": "2013-10-01T00:00:00Z/2014-10-01T00:00:00Z",
-            "@type": "dcat:Dataset",
+            "identifier": "TECHPORT_14396",
+            "issued": "2012-01-01",
+            "keyword": [
+                "project",
+                "armstrong flight research center",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/14396",
             "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Chief Technologist"
+            },
             "references": [
                 "http://techport.nasa.gov/home",
                 "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
@@ -5487,71 +5463,72 @@
                 "http://techport.nasa.gov/fetchFile?objectId=6560",
                 "http://techport.nasa.gov/fetchFile?objectId=3448"
             ],
-            "keyword": [
-                "active",
-                "project",
-                "jet propulsion laboratory"
+            "temporal": "2012-01-01T00:00:00Z/2020-01-01T00:00:00Z",
+            "title": "Fundamental Hyperelastic Material Study Project"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Keith Patterson",
                 "hasEmail": "mailto:keith.d.patterson@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_14383",
             "description": "&lt;p&gt;The goal is to complete process development to make OFET&amp;rsquo;s on flexible substrates compatible with ultra-lightweight deformable mirrors and to demonstrate simplified active device integration process with a functional deformable mirror as a precursor for future integrated circuit development.&lt;/p&gt;",
-            "title": "Development of Organic FET (OFET)-Based Flexible Integrated Controller for Deformable Mirrors Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/14383",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_14383",
+            "issued": "2013-10-01",
+            "keyword": [
+                "active",
+                "project",
+                "jet propulsion laboratory"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/14383",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Space Technology Mission Directorate"
+            },
+            "references": [
+                "http://techport.nasa.gov/home",
+                "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
+                "http://techport.nasa.gov/fetchFile?objectId=6561",
+                "http://techport.nasa.gov/fetchFile?objectId=3456",
+                "http://techport.nasa.gov/fetchFile?objectId=3447",
+                "http://techport.nasa.gov/fetchFile?objectId=6584",
+                "http://techport.nasa.gov/fetchFile?objectId=6560",
+                "http://techport.nasa.gov/fetchFile?objectId=3448"
+            ],
+            "temporal": "2013-10-01T00:00:00Z/2014-10-01T00:00:00Z",
+            "title": "Development of Organic FET (OFET)-Based Flexible Integrated Controller for Deformable Mirrors Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3113907977-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "UW-Madison Space Science and Engineering Center: Joe Taylor; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow. 2024-07-01. SNDRJ2CrISL1BIMG. Version 3.0. JPSS-2 CrIS IMG: Collocated VIIRS level 1 / cloud mask statistical summary V3.0. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/SNDRJ2CrISL1BIMG_3.0.html. Digital Science Data.",
-            "issued": "2023-02-22",
-            "temporal": "2023-02-22T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-26",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C3113907977-GES_DISC",
-            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Full Spectral Resolution (FSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Joint Polar Satellite System-2 (JPSS-2) platform. This platform is also know as NOAA-21 (National Oceanic and Atmospheric Administration). \n\nThe IMG product supplements the CrIS Level 1B (L1B) hyperspectral radiance product by providing collocated high-spatial resolution data from the Visible Infrared Imaging Radiometer Suite (VIIRS) imager located on the same platform. VIIRS radiance and cloud mask values are grouped and aggregated for every CrIS field of view (FOV) and made available in a format intended for use alongside the CrIS L1B data. The collocated VIIRS level 1 / cloud mask statistical summary is the main product and consists of collocated CrIS field of views with the VIIRS cloud mask and radiances/reflectances. This can be thought of as a match-up between CrIS and VIIRS. The supplementary product, array indices for collocated VIIRS observations (collection name SNDRJ2CrISL1BIMGC), consists of array indices for collocated VIIRS observations and provides the collocated indices of the VIIRS pixels within each CrIS footprint. \n\nThe FSR files have 2,223 channels (*2211 apodized channels): 637 (*633) shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 869 (*865) midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 (*713)longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nThe Visible Infrared Imaging Radiometer Suite (VIIRS) has 22 imaging and radiometric bands covering wavelengths from 0.41 to 12.5 microns. It provides the sensor data records for clouds, sea surface temperature, ocean color, and others. This IMG product primarily contains statistics of the VIIRS cloud mask and VIIRS L1B data within each CrIS footprint.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "SNDRJ2CrISL1BIMG",
             "creator": "UW-Madison Space Science and Engineering Center: Joe Taylor; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow",
-            "title": "JPSS-2 CrIS IMG: Collocated VIIRS level 1 / cloud mask statistical summary V3.0 (SNDRJ2CrISL1BIMG) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ2CrISL1BIMG_3.0.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Full Spectral Resolution (FSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Joint Polar Satellite System-2 (JPSS-2) platform. This platform is also know as NOAA-21 (National Oceanic and Atmospheric Administration). \n\nThe IMG product supplements the CrIS Level 1B (L1B) hyperspectral radiance product by providing collocated high-spatial resolution data from the Visible Infrared Imaging Radiometer Suite (VIIRS) imager located on the same platform. VIIRS radiance and cloud mask values are grouped and aggregated for every CrIS field of view (FOV) and made available in a format intended for use alongside the CrIS L1B data. The collocated VIIRS level 1 / cloud mask statistical summary is the main product and consists of collocated CrIS field of views with the VIIRS cloud mask and radiances/reflectances. This can be thought of as a match-up between CrIS and VIIRS. The supplementary product, array indices for collocated VIIRS observations (collection name SNDRJ2CrISL1BIMGC), consists of array indices for collocated VIIRS observations and provides the collocated indices of the VIIRS pixels within each CrIS footprint. \n\nThe FSR files have 2,223 channels (*2211 apodized channels): 637 (*633) shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 869 (*865) midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 (*713)longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nThe Visible Infrared Imaging Radiometer Suite (VIIRS) has 22 imaging and radiometric bands covering wavelengths from 0.41 to 12.5 microns. It provides the sensor data records for clouds, sea surface temperature, ocean color, and others. This IMG product primarily contains statistics of the VIIRS cloud mask and VIIRS L1B data within each CrIS footprint.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5560,1576 +5537,1610 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ2CrISL1BIMG_3.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRJ2CrISL1BIMG_3.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS2_Sounder_Level1/SNDRJ2CrISL1BIMG.3.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/JPSS2_Sounder_Level1/SNDRJ2CrISL1BIMG.3.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ2CrISL1BIMG+3.0",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRJ2CrISL1BIMG+3.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS2_Sounder_Level1/SNDRJ2CrISL1BIMG.3.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/JPSS2_Sounder_Level1/SNDRJ2CrISL1BIMG.3.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/D0001-M01-S01-002_JPSS_ATBD_CrIS-SDR_C.pdf",
-                    "description": "Joint Polar Satellite System (JPSS) Cross-track Infrared Sounder (CrIS) Sensor Data Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) Cross-track Infrared Sounder (CrIS) Sensor Data Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/D0001-M01-S01-002_JPSS_ATBD_CrIS-SDR_C.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_L1B_SNPP.DeltaATBD_V2.0.pdf",
-                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_L1B_SNPP.DeltaATBD_V2.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/README.beta.SNDRJ2CrISL1BIMGC.v3.0.pdf",
-                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) IMG/IMG_COL Product Users\u2019 Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) IMG/IMG_COL Product Users\u2019 Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/README.beta.SNDRJ2CrISL1BIMGC.v3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.5_ProductQuality/NASA_SNPP_CrIS_L1B_Quality_Flags_V2.0.pdf",
-                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SNPP Cross-track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.5_ProductQuality/NASA_SNPP_CrIS_L1B_Quality_Flags_V2.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRJ2CrISL1BIMG_3.0.png",
+            "identifier": "C3113907977-GES_DISC",
+            "issued": "2023-02-22",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C3113907977-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "SNDRJ2CrISL1BIMG",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-02-22T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "JPSS-2 CrIS IMG: Collocated VIIRS level 1 / cloud mask statistical summary V3.0 (SNDRJ2CrISL1BIMG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTEROID-SPIN-VECTORS-V4.1",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "asteroid",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Asteroid pole orientation determinations, collected from the literature by P. Magnusson.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-asteroid-spin-vectors-v4.1_23px-37gx",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-ASTEROID-SPIN-VECTORS-V4.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-asteroid-spin-vectors-v4.1_23px-37gx",
-            "description": "Asteroid pole orientation determinations, collected from the literature by P. Magnusson.",
-            "title": "ASTEROID SPIN VECTORS V4.1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ASTEROID SPIN VECTORS V4.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-4-ESC4-RESAMPLED-V9.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "international rosetta mission",
-                "67p/churyumov-gerasimenko 1 (1969 r1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the\nCOMET ESCORT 4 Phase from October 21, 2015 until January 12, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Data are averaged to 1s means and\n60s means. Observations are done in the vicinity of comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-4-esc4-resampled-v9.0_23t7-nhnw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-4-ESC4-RESAMPLED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-4-esc4-resampled-v9.0_23t7-nhnw",
-            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the\nCOMET ESCORT 4 Phase from October 21, 2015 until January 12, 2016\nof the ROSETTA orbiter magnetometer RPCMAG. Data are averaged to 1s means and\n60s means. Observations are done in the vicinity of comet\n67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 4 ESC4 RESAMPLED V9.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RPCMAG 4 ESC4 RESAMPLED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/MEASURES/WATERCYCLE/DATA312",
             "citation": "Colorado State University (Christian Kummerow). 2015-09-01. WC_MULTISEN_PREC_025. Version 001. TMI/TRMM precipitation and uncertainty (TMPA) L3 3 hour 0.25 degree x 0.25 degree V001. Greenbelt, MD USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/MEASURES/WATERCYCLE/DATA312. https://disc.gsfc.nasa.gov/datacollection/WC_MULTISEN_PREC_025_001.html. Digital Science Data.",
-            "issued": "2015-05-04",
-            "temporal": "1998-01-01T00:00:00Z/2010-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-05-04",
-            "references": [
-                "https://doi.org/10.1175/JHM560.1",
-                "https://doi.org/10.1002/jgrd.50607"
-            ],
-            "keyword": [
-                "earth science",
-                "precipitation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CHRISTIAN KUMMEROW",
                 "hasEmail": "mailto:kummerow@atmos.colostate.edu"
             },
+            "creator": "Colorado State University (Christian Kummerow)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1242287793-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "TMI/TRMM precipitation and uncertainty (TMPA) L3 3 hour 0.25 degree x 0.25 degree V001 provides estimates of accumulated precipitation from the Tropical Rainfall Measuring Mission (TRMM) and Other Data Precipitation Data Set (TRMM 3B42; Huffman et al., 2007), along with estimates of the uncertainty in the TRMM 3B42 made by Bytheway and Kummerow (2013). The data set covers both ocean and land from 50 degree North to 50 degree South.",
-            "release-place": "Greenbelt, MD USA",
-            "series-name": "WC_MULTISEN_PREC_025",
-            "creator": "Colorado State University (Christian Kummerow)",
-            "graphic-preview-description": "3-hourly accumulated precipitation from TRMM 3B42 product and associated uncertainty (root mean square error), version 001 (WC_MULTISEN_PREC_025_001), 0.25-degree, for June 1, 2010, 03Z",
-            "title": "TMI/TRMM precipitation and uncertainty (TMPA) L3 3 hour 0.25 degree x 0.25 degree V001 (WC_MULTISEN_PREC_025) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/WC_MULTISEN_PREC_025_001.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWATERCYCLE%2FDATA312",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMEASURES%2FWATERCYCLE%2FDATA312",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/WC_MULTISEN_PREC_025_001.png",
-                    "description": "3-hourly accumulated precipitation from TRMM 3B42 product and associated uncertainty (root mean square error), version 001 (WC_MULTISEN_PREC_025_001), 0.25-degree, for June 1, 2010, 03Z",
                     "@type": "dcat:Distribution",
+                    "description": "3-hourly accumulated precipitation from TRMM 3B42 product and associated uncertainty (root mean square error), version 001 (WC_MULTISEN_PREC_025_001), 0.25-degree, for June 1, 2010, 03Z",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/WC_MULTISEN_PREC_025_001.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/WC_MULTISEN_PREC_025_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/WC_MULTISEN_PREC_025_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/TerrestrialWaterCycle/WC_MULTISEN_PREC_025.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/TerrestrialWaterCycle/WC_MULTISEN_PREC_025.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=WC_MULTISEN_PREC_025",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=WC_MULTISEN_PREC_025",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/TerrestrialWaterCycle/WC_MULTISEN_PREC_025.001/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/opendap/TerrestrialWaterCycle/WC_MULTISEN_PREC_025.001/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/TerrestrialWaterCycle/WC_MULTISEN_PREC_025.001/doc/README.WC_MULTISEN_PREC_025_V001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://measures.gesdisc.eosdis.nasa.gov/data/TerrestrialWaterCycle/WC_MULTISEN_PREC_025.001/doc/README.WC_MULTISEN_PREC_025_V001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-description": "3-hourly accumulated precipitation from TRMM 3B42 product and associated uncertainty (root mean square error), version 001 (WC_MULTISEN_PREC_025_001), 0.25-degree, for June 1, 2010, 03Z",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/WC_MULTISEN_PREC_025_001.png",
+            "identifier": "C1242287793-GES_DISC",
+            "issued": "2015-05-04",
+            "keyword": [
+                "earth science",
+                "precipitation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MEASURES/WATERCYCLE/DATA312",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-05-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1175/JHM560.1",
+                "https://doi.org/10.1002/jgrd.50607"
+            ],
+            "release-place": "Greenbelt, MD USA",
+            "series-name": "WC_MULTISEN_PREC_025",
             "spatial": "-180.0 -50.0 180.0 50.0",
+            "temporal": "1998-01-01T00:00:00Z/2010-12-31T23:59:59Z",
             "theme": [
                 "MEaSUREs",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TMI/TRMM precipitation and uncertainty (TMPA) L3 3 hour 0.25 degree x 0.25 degree V001 (WC_MULTISEN_PREC_025) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/U54WBM8OXJO7",
             "citation": "Kevin W. Bowman. 2021-03-08. TRPSDL2NH3CRSWCF. Version 1. TROPESS CrIS-SNPP L2 Ammonia for West Coast Fires, Standard Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/U54WBM8OXJO7. https://disc.gsfc.nasa.gov/datacollection/TRPSDL2NH3CRSWCF_1.html. Digital Science Data.",
-            "issued": "2021-01-22",
-            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-22",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460",
-                "https://doi.org/10.1109/TGRS.2006.871234",
-                "https://doi.org/10.5194/amt-8-1323-2015",
-                "https://doi.org/10.5194/acp-11-10743-2011"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KEVIN BOWMAN",
                 "hasEmail": "mailto:kevin.w.bowman@jpl.nasa.gov"
             },
+            "creator": "Kevin W. Bowman",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1980429433-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS CrIS-SNPP L2 Ammonia for West Coast Fires, Standard Product contains the vertical distribution of the retrieved atmospheric state of ammonia (NH3), formal uncertainties, and diagnostic information measured by the CrIS instrument on the Suomi-NPP satellite. This product focuses on the CONUS region (20N-60N; 150W-40W) for the time period from 2020-08-01 to 2020-10-31, during the outbreak of U.S. West Coast wildfires. The NASA TRopospheric Ozone and Precursors from Earth System Sounding (TROPESS) project, uses an optimal estimation algorithm, known as the MUlti-SpEctra, MUlti-SpEcies, Multi-SEnsors (MUSES).\n\nThe data files are written in the netCDF version 4 file format, and each file contains one day of data. The data have a spatial resolution of 14 km (CrIS nadir FOV), and are reported at 15 vertical levels from the surface to 0.1 hPa. The principal investigator for the TROPESS project is Kevin W. Bowman.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSDL2NH3CRSWCF",
-            "creator": "Kevin W. Bowman",
-            "graphic-preview-description": "TROPESS CrIS/SNPP NH3 (West Coast Fires, Special Product) at 681 hPa on 12 September 2020.",
-            "title": "TROPESS CrIS-SNPP L2 Ammonia for West Coast Fires, Standard Product V1 (TRPSDL2NH3CRSWCF) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2NH3CRSWCF_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FU54WBM8OXJO7",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FU54WBM8OXJO7",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2NH3CRSWCF_Sample.png",
-                    "description": "TROPESS CrIS/SNPP NH3 (West Coast Fires, Special Product) at 681 hPa on 12 September 2020.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS/SNPP NH3 (West Coast Fires, Special Product) at 681 hPa on 12 September 2020.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2NH3CRSWCF_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2NH3CRSWCF_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSDL2NH3CRSWCF_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2NH3CRSWCF.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2NH3CRSWCF.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2NH3CRSWCF_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSDL2NH3CRSWCF_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2NH3CRSWCF.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TROPESS_Special/TRPSDL2NH3CRSWCF.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2NH3CRSWCF.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TROPESS_Special/TRPSDL2NH3CRSWCF.1/doc/TROPESS_West_Coast_Fires_README_2-23-21.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_NH3_L2_Product_User_Guide_2-22-21.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/User_Guides/TROPESS-AIRS-CrIS_NH3_L2_Product_User_Guide_2-22-21.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tes.jpl.nasa.gov/tropess/",
-                    "description": "TROPESS Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS Project Home Page.",
+                    "downloadURL": "https://tes.jpl.nasa.gov/tropess/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "TROPESS CrIS/SNPP NH3 (West Coast Fires, Special Product) at 681 hPa on 12 September 2020.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSDL2NH3CRSWCF_Sample.png",
+            "identifier": "C1980429433-GES_DISC",
+            "issued": "2021-01-22",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/U54WBM8OXJO7",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-01-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460",
+                "https://doi.org/10.1109/TGRS.2006.871234",
+                "https://doi.org/10.5194/amt-8-1323-2015",
+                "https://doi.org/10.5194/acp-11-10743-2011"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSDL2NH3CRSWCF",
             "spatial": "-150.0 20.0 -40.0 60.0",
+            "temporal": "2020-08-02T00:00:00Z/2020-10-26T23:59:59.999Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS CrIS-SNPP L2 Ammonia for West Coast Fires, Standard Product V1 (TRPSDL2NH3CRSWCF) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N5K072F8",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Sea Ice Index, Version 3. Version 3. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N5K072F8.",
-            "issued": "1978-10-26",
-            "temporal": "1978-10-26T00:00:00Z/2024-07-15T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
-            "keyword": [
-                "sea ice",
-                "cryosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florence Fetterer",
                 "hasEmail": "mailto:fetterer@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1430594808-NSIDCV0",
             "description": "The <a href=\"/data/seaice_index/\">Sea Ice Index</a> provides a quick look at Arctic- and Antarctic-wide changes in sea ice. It is a source for consistent, up-to-date sea ice extent and concentration images, in PNG format, and data values, in GeoTIFF and ASCII text files, from November 1978 to the present. Sea Ice Index images also depict trends and anomalies in ice cover calculated using a 30-year reference period of 1981 through 2010.\n\nThe images and data are produced in a consistent way that makes the Index time-series appropriate for use when looking at long-term trends in sea ice cover. Both monthly and daily products are available. However, monthly products are better to use for long-term trend analysis because errors in the daily product tend to be averaged out in the monthly product and because day-to-day variations are often the result of short-term weather.",
-            "title": "Sea Ice Index, Version 3",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5K072F8",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN5K072F8",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02135/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02135/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/seaice_index/",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://nsidc.org/data/seaice_index/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02135/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02135/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/seaice_index/",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://nsidc.org/data/seaice_index/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02135/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02135/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/seaice_index/",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://nsidc.org/data/seaice_index/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02135/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://noaadata.apps.nsidc.org/NOAA/G02135/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/seaice_index/",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://nsidc.org/data/seaice_index/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5K072F8",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N5K072F8",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N5K072F8",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N5K072F8",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1430594808-NSIDCV0",
+            "issued": "1978-10-26",
+            "keyword": [
+                "sea ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7265/N5K072F8",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-180.0 -90.0 180.0 -39.23",
+            "temporal": "1978-10-26T00:00:00Z/2024-07-15T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sea Ice Index, Version 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amagellan_stereo_topography&version=1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "magellan",
-                "venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Stereo-derived topography produced from the Magellan stereo data.",
+            "identifier": "urn:nasa:pds:magellan_stereo_topography",
+            "issued": "2021-05-21",
+            "keyword": [
+                "magellan",
+                "venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Amagellan_stereo_topography&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:magellan_stereo_topography",
-            "description": "Stereo-derived topography produced from the Magellan stereo data.",
-            "title": "Magellan Venus Stereo-Derived Topography Bundle",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Magellan Venus Stereo-Derived Topography Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0855-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "international rosetta mission",
-                "67p/churyumov-gerasimenko 1 (1969 r1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-23T21:02:50.000 to 2015-06-24T00:21:03.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0855-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0855-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0855-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-06-23T21:02:50.000 to 2015-06-24T00:21:03.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0855 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0855 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-ESC2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 2 mission phase, which took place between 2015-03-11 and 2015-06-30.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-esc2-v1.0_244c-up9f",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "calibration",
                 "67p/churyumov-gerasimenko 1 (1969 r1)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-3-ESC2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-3-esc2-v1.0_244c-up9f",
-            "description": "This data set contains CODMAC Level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 2 mission phase, which took place between 2015-03-11 and 2015-06-30.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 ESC2 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 3 ESC2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-EARTH-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "near earth asteroid rendezvous",
-                "eros"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-earth-v1.0_244z-z2me",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "eros"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-SPICE-6-EARTH-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-spice-6-earth-v1.0_244z-z2me",
-            "description": "This data set includes the complete set of SPICE data for one NEAR mission phase in the form of SPICE kernels, which can be accessed using SPICE software available to read these files.",
-            "title": "NEAR SPICE KERNELS EARTH",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR SPICE KERNELS EARTH"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0488-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-13T12:54:10.000 to 2014-12-13T19:29:14.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0488-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC1-0488-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc1-0488-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 1 phase 2014-11-20 to 2015-03-10. It is a Global Gravity measurement at the comet 67P and covers the time 2014-12-13T12:54:10.000 to 2014-12-13T19:29:14.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0488 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 1 0488 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2152",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Fichot, C.G., and J. Harringmeyer. 2023. Delta-X: AVIRIS-NG L3-derived Water Quality, TSS, and Turbidity, MRD, V3. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2152",
-            "issued": "2023-11-02",
-            "temporal": "2021-03-27T00:00:00Z/2021-09-24T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-08",
-            "keyword": [
-                "water quality/water chemistry",
-                "earth science",
-                "surface water",
-                "terrestrial hydrosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2797469962-ORNL_CLOUD",
             "description": "This dataset includes estimates of total suspended solids (TSS) concentration and turbidity for waters of the Atchafalaya River and Terrebonne Basins of the Mississippi River Delta (MRD) in coastal Louisiana. Estimates were derived from Level 2 (L2) BRDF-corrected imagery from NASA's Next Generation Airborne Visible Infrared Imaging Spectrometer (AVIRIS-NG). AVIRIS-NG imagery was collected from March 27-April 6 (spring) and August 20-25 (fall), 2021, as part of the 2021 Delta-X campaign. Algorithms for TSS and turbidity estimation were developed using in-situ remote-sensing reflectance measured at field sampling stations paired with in-situ measures of turbidity from a water quality probe and TSS from water samples. Using the in-situ data, a partial least squares regression (PLSR) model was developed for each AVIRIS-NG wavelength. A subset of the in-situ data, collected during relatively clear AVIRIS-NG overflights, was held out to validate the PLSR model. The PLSR algorithm was then applied to AVIRIS-NG imagery to retrieve TSS and turbidity across the study area. The measurement units for TSS and turbidity estimates are mg L-1 and Formazin Nephelometric Units (FNU), respectively, and the spatial resolution is 3.8 to 5.4 m as determined by the AVIRIS-NG imagery. The dataset includes binary cloud and water masks. These data quantify the mesoscale (i.e., on the order of 1 ha) patterns of soil accretion that control land loss and gain and predict the resilience of deltaic floodplains under projected relative sea-level rise. Gridded estimates are provided in netCDF format, and regression coefficients are included in a comma-separated values (CSV) file. This is Version 3 of this dataset. All previously released data were updated to the latest available versions.",
-            "graphic-preview-description": "Map of total suspended solids (TSS) in the Terrebonne basin of the Mississippi River Delta of coastal Louisiana. TSS was estimated from AVIRIS-NG imagery using a regression model derived from in-situ measurements of surface reflectance and TSS.",
-            "title": "Delta-X: AVIRIS-NG L3-derived Water Quality, TSS, and Turbidity, MRD, V3",
-            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Water_V3_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2152",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F2152",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_L3_AVIRIS-NG_Water_V3/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/deltax/DeltaX_L3_AVIRIS-NG_Water_V3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Water_V3.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Water_V3.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2152",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/2152",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.earthdata.nasa.gov/",
-                    "description": "USE SERVICE API",
                     "@type": "dcat:Distribution",
+                    "description": "USE SERVICE API",
+                    "downloadURL": "https://opendap.earthdata.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L3_AVIRIS-NG_Water_V3/comp/DeltaX_L3_AVIRIS-NG_Water_V3.pdf",
-                    "description": "Delta-X: AVIRIS-NG L3-derived Water Quality, TSS, and Turbidity, MRD, V3: DeltaX_L3_AVIRIS-NG_Water_V3.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X: AVIRIS-NG L3-derived Water Quality, TSS, and Turbidity, MRD, V3: DeltaX_L3_AVIRIS-NG_Water_V3.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/deltax/DeltaX_L3_AVIRIS-NG_Water_V3/comp/DeltaX_L3_AVIRIS-NG_Water_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Water_V3_Fig1.jpg",
-                    "description": "Map of total suspended solids (TSS) in the Terrebonne basin of the Mississippi River Delta of coastal Louisiana. TSS was estimated from AVIRIS-NG imagery using a regression model derived from in-situ measurements of surface reflectance and TSS.",
                     "@type": "dcat:Distribution",
+                    "description": "Map of total suspended solids (TSS) in the Terrebonne basin of the Mississippi River Delta of coastal Louisiana. TSS was estimated from AVIRIS-NG imagery using a regression model derived from in-situ measurements of surface reflectance and TSS.",
+                    "downloadURL": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Water_V3_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://deltax.jpl.nasa.gov/",
-                    "description": "Delta-X Project Site",
                     "@type": "dcat:Distribution",
+                    "description": "Delta-X Project Site",
+                    "downloadURL": "https://deltax.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Map of total suspended solids (TSS) in the Terrebonne basin of the Mississippi River Delta of coastal Louisiana. TSS was estimated from AVIRIS-NG imagery using a regression model derived from in-situ measurements of surface reflectance and TSS.",
+            "graphic-preview-file": "https://daac.ornl.gov/DELTAX/guides/DeltaX_L3_AVIRIS-NG_Water_V3_Fig1.jpg",
+            "identifier": "C2797469962-ORNL_CLOUD",
+            "issued": "2023-11-02",
+            "keyword": [
+                "water quality/water chemistry",
+                "earth science",
+                "surface water",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/2152",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-91.59 29.06 -90.18 29.81",
+            "temporal": "2021-03-27T00:00:00Z/2021-09-24T23:59:59Z",
             "theme": [
                 "Delta-X",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Delta-X: AVIRIS-NG L3-derived Water Quality, TSS, and Turbidity, MRD, V3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/EGEE5/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/EGEE5/DATA001.",
-            "issued": "2007-06-06",
-            "temporal": "2007-06-06T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean temperature",
-                "earth science",
-                "ocean optics",
-                "salinity/density",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:data@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C1633360227-OB_DAAC",
             "description": "Measurements made in the Gulf of Guinea off of west-central Africa in 2007 as part of the fifth cruise in the EGEE project (Gulf of Guinea climate and ocean circulation study, which is the oceanographic strand of the AMMA -African Monsoon Multidisciplinary Analyses program).",
-            "title": "Gulf of Guinea climate and ocean circulation study (EGEES)",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FEGEE5%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FEGEE5%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/EGEE5/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/EGEE5/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360227-OB_DAAC",
+            "issued": "2007-06-06",
+            "keyword": [
+                "ocean chemistry",
+                "ocean temperature",
+                "earth science",
+                "ocean optics",
+                "salinity/density",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/EGEE5/DATA001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-04-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2007-06-06T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gulf of Guinea climate and ocean circulation study (EGEES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GHNMA-3CO02",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "EUMETSAT/OSI SAF. 2015-02-02. GHRSST Level 3C North Atlantic Regional (NAR) subskin Sea Surface Temperature from SNPP/VIIRS and Metop-A/AVHRR (GDS V2) produced by OSI SAF. Version 1. AVHRR NAR SST data set. EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France. Archived by National Aeronautics and Space Administration, U.S. Government, EUMETSAT Ocean and Sea Ice Satellite Application Facility, Meteo-France/CMS, Lannion, France. https://doi.org/10.5067/GHNMA-3CO02. http://www.osi-saf.org. EUMETSAT/OSI SAF, EUMETSAT Ocean and Sea Ice Satellite Application Facility, Meteo-France/CMS, Lannion, France, 2015-02-02, GHRSST Level 3C North Atlantic Regional (NAR) subskin Sea Surface Temperature from SNPP/VIIRS and Metop-A/AVHRR (GDS V2) produced by OSI SAF, www.osi-saf.org.",
-            "issued": "2014-05-30",
-            "temporal": "2013-06-04T05:30:00Z/2016-11-22T23:41:34Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "oceans",
-                "ocean temperature",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491735295-POCLOUD",
-            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) dataset for the North Atlantic Region (NAR) derived from the Advanced Very High Resolution Radiometer (AVHRR) on the European Meteorological Operational-A (MetOp-A) platform (launched 19 Oct 2006). \n\nThe European Organization for the Exploitation of Meteorological Satellites (EUMETSAT), Ocean and Sea Ice Satellite Application Facility (OSI SAF) is producing SST products in near real time from Metop/AVHRR and SNPP/VIIRS. Global AVHRR level 1b data are acquired at Meteo-France/Centre de Meteorologie Spatiale (CMS) through the EUMETSAT/EUMETCAST system. NAR SNPP/VIIRS level 0 data are acquired through direct readout and converted into l1b at CMS. SST is retrieved from the AVHRR and VIIRS infrared channels using a multispectral algorithm.\nThis product is delivered as four six hourly collated files per day on a regular 2km grid. The product format is compliant with the GHRSST Data Specification (GDS) version 2.",
-            "release-place": "EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France",
-            "series-name": "GHRSST Level 3C North Atlantic Regional (NAR) subskin Sea Surface Temperature from SNPP/VIIRS and Metop-A/AVHRR (GDS V2) produced by OSI SAF",
-            "graphic-preview-description": "Thumbnail",
             "creator": "EUMETSAT/OSI SAF",
-            "title": "GHRSST Level 3C North Atlantic Regional (NAR) subskin Sea Surface Temperature from SNPP/VIIRS and Metop-A/AVHRR (GDS V2) produced by OSI SAF",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR_SST_METOP_A_NAR-OSISAF-L3C-v1.0.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "A Group for High Resolution Sea Surface Temperature (GHRSST) dataset for the North Atlantic Region (NAR) derived from the Advanced Very High Resolution Radiometer (AVHRR) on the European Meteorological Operational-A (MetOp-A) platform (launched 19 Oct 2006). \n\nThe European Organization for the Exploitation of Meteorological Satellites (EUMETSAT), Ocean and Sea Ice Satellite Application Facility (OSI SAF) is producing SST products in near real time from Metop/AVHRR and SNPP/VIIRS. Global AVHRR level 1b data are acquired at Meteo-France/Centre de Meteorologie Spatiale (CMS) through the EUMETSAT/EUMETCAST system. NAR SNPP/VIIRS level 0 data are acquired through direct readout and converted into l1b at CMS. SST is retrieved from the AVHRR and VIIRS infrared channels using a multispectral algorithm.\nThis product is delivered as four six hourly collated files per day on a regular 2km grid. The product format is compliant with the GHRSST Data Specification (GDS) version 2.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHNMA-3CO02",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHNMA-3CO02",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.ghrsst.org",
-                    "description": "Description of the GHRSST Project",
                     "@type": "dcat:Distribution",
+                    "description": "Description of the GHRSST Project",
+                    "downloadURL": "http://www.ghrsst.org",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop2_ss1_pum_leo_sst.pdf",
-                    "description": "Product User Manual",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual",
+                    "downloadURL": "https://osi-saf.eumetsat.int/lml/doc/osisaf_cdop2_ss1_pum_leo_sst.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR_SST_METOP_A_NAR-OSISAF-L3C-v1.0.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR_SST_METOP_A_NAR-OSISAF-L3C-v1.0.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "Group for High Resolution Sea Surface Temperature Information",
                     "@type": "dcat:Distribution",
+                    "description": "Group for High Resolution Sea Surface Temperature Information",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/CitingPODAAC",
-                    "description": "Data Use and Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "Data Use and Citation Policy",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/CitingPODAAC",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491735295-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491735295-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491735295-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491735295-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic data readers",
                     "@type": "dcat:Distribution",
+                    "description": "Generic data readers",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AVHRR_SST_METOP_A_NAR-OSISAF-L3C-v1.0.jpg",
+            "identifier": "C2491735295-POCLOUD",
+            "issued": "2014-05-30",
+            "keyword": [
+                "oceans",
+                "ocean temperature",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHNMA-3CO02",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "EUMETSAT Ocean and Sea Ice Satellite Application Facility, Lannion, France",
+            "series-name": "GHRSST Level 3C North Atlantic Regional (NAR) subskin Sea Surface Temperature from SNPP/VIIRS and Metop-A/AVHRR (GDS V2) produced by OSI SAF",
             "spatial": "-76.02 23.59 72.97 78.24",
+            "temporal": "2013-06-04T05:30:00Z/2016-11-22T23:41:34Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 3C North Atlantic Regional (NAR) subskin Sea Surface Temperature from SNPP/VIIRS and Metop-A/AVHRR (GDS V2) produced by OSI SAF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-MSNVIS-3-RDR-HALLEY-ETA-AQUAR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The visual data for Eta Aquarid contains 579 observations, spanning dates 1984 April 27 through 1987 May 11.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-msnvis-3-rdr-halley-eta-aquar-v1.0_2496-7rgs",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "eta-aquarid",
                 "international halley watch",
                 "halley"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-MSNVIS-3-RDR-HALLEY-ETA-AQUAR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-msnvis-3-rdr-halley-eta-aquar-v1.0_2496-7rgs",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The visual data for Eta Aquarid contains 579 observations, spanning dates 1984 April 27 through 1987 May 11.",
-            "title": "IHW COMET HALLEY METEOR ETA AQUARID VISUAL DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY METEOR ETA AQUARID VISUAL DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SOFEX3867ECJ",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx20 Grand Mesa IOP BSU 1 GHz Multi-polarization GPR CMP Snow Water Equivalent V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/SOFEX3867ECJ.",
-            "issued": "2020-01-31",
-            "temporal": "2020-01-31T00:00:00Z/2020-02-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-01",
-            "keyword": [
-                "snow/ice",
-                "terrestrial hydrosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NSIDC Services",
                 "hasEmail": "mailto:nsidc@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1998359549-NSIDC_ECS",
             "description": "This data set was collected during the SnowEx 2020 Intensive Observation Period (IOP) in Grand Mesa, Colorado. These data contain snow water equivalent (SWE) estimates. SWE is derived from Sensors & Software pulseEKKO PRO 1 GHz multi-polarization ground penetrating radar (GPR) two-way travel times. \nData were collected at three locations around Grand Mesa IOP snow pits 2N12 and 1S8 (see DOI: 10.5067/DUD2VZEVBJ7S for more details on Grand Mesa IOP snow pits). Data at snow pit 2N12 were acquired on the groomed snowmobile road (CMP1), in the fresh snow behind the snow pit wall (CMP2), and in the right rut of the SUSV track (CMP3). Data at snow pit 1S8  were acquired in the right rut of the SUSV track (CMP1), in the left rut of the SUSV track (CMP2), and in the fresh snow behind the snow pit wall (CMP3). \nThe raw version of these data (DOI: 10.5067/CL5ZRBCEF8G3) are also archived at NSIDC.",
-            "title": "SnowEx20 Grand Mesa IOP BSU 1 GHz Multi-polarization GPR CMP Snow Water Equivalent V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSOFEX3867ECJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSOFEX3867ECJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1998359549-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_BSU_CMP_SWE&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643427%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1998359549-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_BSU_CMP_SWE&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643427%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BSU_CMP_SWE.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BSU_CMP_SWE.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BSU_CMP_SWE/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BSU_CMP_SWE/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1998359549-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_BSU_CMP_SWE&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643427%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1998359549-NSIDC_ECS&pg%5B0%5D%5Bgsk%5D=-start_date&q=SNEX20_BSU_CMP_SWE&m=38.35552775499695%21-113.57226562500001%215%211%210%210%2C2&tl=1596643427%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BSU_CMP_SWE.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX20_BSU_CMP_SWE.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BSU_CMP_SWE/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX20_BSU_CMP_SWE/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SOFEX3867ECJ",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/SOFEX3867ECJ",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/SOFEX3867ECJ",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/SOFEX3867ECJ",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1998359549-NSIDC_ECS",
+            "issued": "2020-01-31",
+            "keyword": [
+                "snow/ice",
+                "terrestrial hydrosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SOFEX3867ECJ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.19 39.02 -108.19 39.02",
+            "temporal": "2020-01-31T00:00:00Z/2020-02-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx20 Grand Mesa IOP BSU 1 GHz Multi-polarization GPR CMP Snow Water Equivalent V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-2-EPOXI-HARTLEY2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "epoxi",
-                "103p/hartley 2 (1986 e2)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains raw images of comet 103/P Hartley 2 acquired by the Medium Resolution Visible CCD (MRI) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Clear-filter and CN images of the comet were acquired throughout this phase; OH, C2, and dust continuum images were only acquired for several days spanning closest approach.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-2-epoxi-hartley2-v1.0_24af-7rkf",
+            "issued": "2018-06-26",
+            "keyword": [
+                "epoxi",
+                "103p/hartley 2 (1986 e2)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-C-MRI-2-EPOXI-HARTLEY2-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-c-mri-2-epoxi-hartley2-v1.0_24af-7rkf",
-            "description": "This dataset contains raw images of comet 103/P Hartley 2 acquired by the Medium Resolution Visible CCD (MRI) from 05 September through 26 November 2010 during the Hartley 2 encounter phase of the EPOXI mission. Clear-filter and CN images of the comet were acquired throughout this phase; OH, C2, and dust continuum images were only acquired for several days spanning closest approach.",
-            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - MRI RAW IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI 103P/HARTLEY2 ENCOUNTER - MRI RAW IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL3YCOD.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/MISR/MIL3YCOD.001. http://eosweb.larc.nasa.gov/project/misr/misr_table.",
-            "issued": "2018-06-27",
-            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID, DR. DINER",
                 "hasEmail": "mailto:david.j.diner@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1644916757-LARC",
             "description": "MIL3YCOD_1 is the Multi-angle Imaging SpectroRadiometer (MISR) Level 3 Cloud Top Height-Optical Depth Product covering a year version 1. MISR itself is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure.",
-            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
-            "title": "MISR Level 3 Cloud Top Height-Optical Depth Product covering a year V001",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL3YCOD.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMISR%2FMIL3YCOD.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/",
-                    "description": "MISR project home page",
                     "@type": "dcat:Distribution",
+                    "description": "MISR project home page",
+                    "downloadURL": "https://misr.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
-                    "description": "NASA EOS ATB Documents: MISR",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MISR",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_CFbA_Product.pdf",
-                    "description": "MISR Level 3 Cloud Fraction by Altitude Product Quality Statement - January 04, 2018",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Level 3 Cloud Fraction by Altitude Product Quality Statement - January 04, 2018",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/quality_summaries/L3_CFbA_Product.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "description": "ASDC Data and Information for MISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS-CTHOD.cmm4_2019-10-03.pdf",
-                    "description": "Data Product Specification for the MISR Cloud Top Height-Optical Depth Product, October 03, 2019",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for the MISR Cloud Top Height-Optical Depth Product, October 03, 2019",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS-CTHOD.cmm4_2019-10-03.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_CFbA.pdf",
-                    "description": "Data Products Specifications - Incorporating the Science Data Processing Interface Control Document",
                     "@type": "dcat:Distribution",
+                    "description": "Data Products Specifications - Incorporating the Science Data Processing Interface Control Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_CFbA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MISR",
-                    "description": "NASA Earthdata Forum - MISR Project Specific Forum",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - MISR Project Specific Forum",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MISR",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MIL3YCOD.001",
-                    "description": "DOI data set landing page for MIL3YCOD_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for MIL3YCOD_1",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/MISR/MIL3YCOD.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
-                    "description": "MISR Peer-Reviewed Publications",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Peer-Reviewed Publications",
+                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.google.com/earth/",
-                    "description": "Google Earth",
                     "@type": "dcat:Distribution",
+                    "description": "Google Earth",
+                    "downloadURL": "https://www.google.com/earth/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/tools-and-services",
-                    "description": "Links to tools available through the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Links to tools available through the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/tools-and-services",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/observing_concept.pdf",
-                    "description": "MISR Observing Concept Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Observing Concept Fact Sheet",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/observing_concept.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
-                    "description": "MISR Paths Tool - Direct File Download (.kml)",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Paths Tool - Direct File Download (.kml)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2015.pdf",
-                    "description": "Overview of MISR Data at the ASDC, 2015",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of MISR Data at the ASDC, 2015",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
-                    "description": "MISR Science Data Product Guide - May 7, 2012",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Science Data Product Guide - May 7, 2012",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_workshop.pdf",
-                    "description": "MISR Workshop Presentations, June 2002 - August 2010",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Workshop Presentations, June 2002 - August 2010",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_workshop.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/overview_misr.pdf",
-                    "description": "Multi-angle Imaging SpectroRadiometer (MISR) Overview Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-angle Imaging SpectroRadiometer (MISR) Overview Fact Sheet",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/overview_misr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
-                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/vnd.ms-powerpoint",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/obtaining_misr_data.ppt",
-                    "description": "Obtaining MISR Data and Information, Presented by Jeff Walter Atmospheric Science Data Center - April 17, 2009 - Direct File Download (.ppt)",
                     "@type": "dcat:Distribution",
+                    "description": "Obtaining MISR Data and Information, Presented by Jeff Walter Atmospheric Science Data Center - April 17, 2009 - Direct File Download (.ppt)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/obtaining_misr_data.ppt",
+                    "mediaType": "application/vnd.ms-powerpoint",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc.html",
-                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc.html",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MIL3YCOD.001/contents.html",
-                    "description": "OPeNDAP data access for MIL3YCOD_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for MIL3YCOD_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/MISR/MIL3YCOD.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MIL3YCOD.001/",
-                    "description": "ASDC Direct Data Download for MIL3YCOD_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for MIL3YCOD_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/MISR/MIL3YCOD.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1644916757-LARC",
-                    "description": "Earthdata Search for MIL3YCOD_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for MIL3YCOD_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1644916757-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/90764/looking-at-the-moon-to-better-see-earth",
-                    "description": "NASA Earth Observatory Article: Looking at the Moon to Better See Earth - Terra satellite performs manuver that allows all nine of MISR's camera to capture images of the moon.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Looking at the Moon to Better See Earth - Terra satellite performs manuver that allows all nine of MISR's camera to capture images of the moon.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/90764/looking-at-the-moon-to-better-see-earth",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://photojournal.jpl.nasa.gov/catalog/PIA21945",
-                    "description": "NASA JPL Photojournal: New Images of Irma's Towering Clouds - MISR passes over Irma over the Dominican Republic as a Category 5 hurricane.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Photojournal: New Images of Irma's Towering Clouds - MISR passes over Irma over the Dominican Republic as a Category 5 hurricane.",
+                    "downloadURL": "https://photojournal.jpl.nasa.gov/catalog/PIA21945",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Earthquake",
-                    "description": "NASA Earth Observatory Article: Squeezing Water from Rock\u00a0-\u00a0Survivors of the New Madrid earthquakes reported not only intense ground shaking and land movement, but also an unfamiliar phenomenon of water and sand spouting up through cracks in the Earth's surface.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Squeezing Water from Rock\u00a0-\u00a0Survivors of the New Madrid earthquakes reported not only intense ground shaking and land movement, but also an unfamiliar phenomenon of water and sand spouting up through cracks in the Earth's surface.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Earthquake",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/tracking",
-                    "description": "NASA Earth Observatory Article: Tracking Clouds\u00a0-\u00a0Tune in to the evening weather report on any given day, and you'll no doubt see satellite images of clouds.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Tracking Clouds\u00a0-\u00a0Tune in to the evening weather report on any given day, and you'll no doubt see satellite images of clouds.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/tracking",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
-                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
+                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.html",
-                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge30b.html",
-                    "description": "ASDC List of MISR Level 3 Cloud Fraction by Altitude Versioning for Cloud Fraction by Altitude Product (CFbA) - Daily, Monthly, Quarterly, and Yearly Products",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR Level 3 Cloud Fraction by Altitude Versioning for Cloud Fraction by Altitude Product (CFbA) - Daily, Monthly, Quarterly, and Yearly Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/pge30b.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.html",
-                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR File Naming and Versioning Conventions",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/file_descriptions.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.html",
-                    "description": "ASDC Overview of MISR Data Versioning Index",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Overview of MISR Data Versioning Index",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/version/index.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.html",
-                    "description": "MISR Quality Statements - September 30, 2014",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements - September 30, 2014",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_current.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_new.html",
-                    "description": "MISR Quality Statements - September 30, 2014",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Quality Statements - September 30, 2014",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_qual_stmts_new.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/dps.html",
-                    "description": "Data Product Specification for MISR Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/dps.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.html",
-                    "description": "Data Product Specification for Specific Products MISR Data Products",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for Specific Products MISR Data Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/dps/specific_products.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v42_RevP.pdf",
-                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007 ",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR V4.2 Software Delivery Updates - Revision P, November 19, 2007 ",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v42_RevP.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-                    "description": "ASDC List of MISR Imagery and Articles",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR Imagery and Articles",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://terra.nasa.gov/?section=60",
-                    "description": "TERRA Overview",
                     "@type": "dcat:Distribution",
+                    "description": "TERRA Overview",
+                    "downloadURL": "https://terra.nasa.gov/?section=60",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 }
             ],
+            "graphic-preview-description": "ASDC List of MISR Imagery and Articles",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+            "identifier": "C1644916757-LARC",
+            "issued": "2018-06-27",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "clouds"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MISR/MIL3YCOD.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-06-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1999-12-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "MISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 3 Cloud Top Height-Optical Depth Product covering a year V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/707",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Morisette, J.T., L. Giglio, I.A. Csiszar, and C.O. Justice. 2004. SAFARI 2000 ASTER and MODIS Fire Data Comparison, Dry Season 2001. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/707",
-            "issued": "2023-10-18",
-            "temporal": "2001-08-05T00:00:00Z/2001-10-05T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "earth science",
-                "ngda",
-                "land surface",
-                "surface thermal properties",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2788368969-ORNL_CLOUD",
             "description": "These data relate to a paper (Morisette et al., 2005) that describes the use of high spatial resolution ASTER data to determine the accuracy of the moderate resolution MODIS active fire product. Our main objective was to develop a methodology to use ASTER data for quantitative evaluation of the MODIS active fire product and to apply it to fires in Southern Africa during the 2001 burning season. We utilize 18 ASTER scenes distributed throughout Southern Africa covering the time period 5 August 2001 to 6 October 2001.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 ASTER and MODIS Fire Data Comparison, Dry Season 2001",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F707",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F707",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/modis_aster_fire/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/remote_sensing/modis_aster_fire/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_modis_aster_fire.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/s2k_modis_aster_fire.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/707",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/707",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/modis_aster_fire/comp/read_me.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/modis_aster_fire/comp/read_me.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/modis_aster_fire/comp/s2k_modis_aster_fire.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/remote_sensing/modis_aster_fire/comp/s2k_modis_aster_fire.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
+            "identifier": "C2788368969-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "earth science",
+                "ngda",
+                "land surface",
+                "surface thermal properties",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/707",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "16.31 -26.83 44.26 -11.29",
+            "temporal": "2001-08-05T00:00:00Z/2001-10-05T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 ASTER and MODIS Fire Data Comparison, Dry Season 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/24c2-frj2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John M. Kusterer",
+                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
+            },
+            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmclay-prov-v1-10_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000172",
             "issued": "2018-06-25",
-            "temporal": "2006-06-13/2007-03-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "satellite",
                 "radiation",
@@ -7139,866 +7150,822 @@
                 "aerosol",
                 "cloud"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/24c2-frj2",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000172",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 5 km Cloud Layer Data V1-10",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_05kmclay-prov-v1-10_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2007-03-13",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 5 km Cloud Layer Data V1-10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9-M-IRIS-3-RDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "mars",
-                "mariner71"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The dataset contains measurements from the infrared interferometer spectrometer and ancillary data. Each record of the dataset consists of a header and a spectral observation of Mars geometry of the observation. The dataset is ordered by time as measured by the Data Acquisition System (DAS) time (1 DAS count is approximately 1.2 sec.). Two IRIS frames are completed every 35 DAS counts calibration observation (alternately of interstellar space and an internal calibration blackbody), and is therefore absent from the calibrated dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-m-iris-3-rdr-v1.0_24d4-kaxm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mariner71"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MR9-M-IRIS-3-RDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mr9-m-iris-3-rdr-v1.0_24d4-kaxm",
-            "description": "The dataset contains measurements from the infrared interferometer spectrometer and ancillary data. Each record of the dataset consists of a header and a spectral observation of Mars geometry of the observation. The dataset is ordered by time as measured by the Data Acquisition System (DAS) time (1 DAS count is approximately 1.2 sec.). Two IRIS frames are completed every 35 DAS counts calibration observation (alternately of interstellar space and an internal calibration blackbody), and is therefore absent from the calibrated dataset.",
-            "title": "MARINER9 IRIS RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARINER9 IRIS RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-10-23. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1.",
-            "issued": "2020-07-20",
-            "temporal": "2019-08-24T00:00:00Z/2019-10-05T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-24",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Gao Chen",
                 "hasEmail": "mailto:gao.chen@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1954736905-LARC_ASDC",
             "description": "CAMP2Ex_Cloud_AircraftInSitu_P3_Data are in-situ cloud measurements conducted onboard the P-3 aircraft during the Clouds, Aerosol and Monsoon Processes-Philippines Experiment (CAMP2Ex) NASA field study. Data collection for this product is complete.\r\n\r\nCAMP2Ex was a NASA field study, with three main science objectives: aerosol effect on cloud microphysical and optical properties, aerosol and cloud influence on radiation as well as radiative feedback, and meteorology effect on aerosol distribution and aerosol-cloud interactions. Research on these three main objectives requires a comprehensive characterization of aerosol, cloud, and precipitation properties, as well as the associated meteorological and radiative parameters. Trace gas tracers are also needed for airmass type analysis to characterize the role of anthropogenic and natural aerosols. To deliver these observations, CAMP2Ex utilized a combination of remote sensing and in-situ measurements. NASA\u2019s P-3B aircraft was equipped with a suite of in-situ instruments to conduct measurements of aerosol and cloud properties, trace gases, meteorological parameters, and radiative fluxes. The P-3B was also equipped passive remote sensors (i.e. lidar, polarimeter, radar, and radiometers). A second aircraft, the SPEC Learjet 35A, was primarily dedicated to measuring detailed cloud microphysical properties. The sampling strategy designed for CAMP2Ex coordinated flight plans for both aircraft to maximize the science return. The P-3B was used primarily to conduct remote sensing measurements of cloud and precipitation structure and aerosol layers and vertical profiles of atmospheric state variable, while the Learjet flew below the P-3B to obtain the detailed cloud microphysical properties. During the 2019 field deployment in the vicinity of the Philippines, completed from August 20-October 10, the P-3B conducted 19 science flights and the SPEC Learjet conducted 11 flights. Ground-based aerosol observations were also recorded in 2018 and 2019. CAMP2Ex was completed in partnership with Philippine research and operational weather communities. Measurements completed during CAMP2EX provide a 4-D observational view of the environment of the Philippines and its neighboring waters in terms of microphysical, hydrological, dynamical, thermodynamical and radiative properties of the environment, targeting the environment of shallow cumulus and cumulus congestus clouds.",
-            "title": "CAMP2Ex P-3 In-Situ Cloud Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FCAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FCAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/camp2ex",
-                    "description": "CAMP2EX ESPO Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "CAMP2EX ESPO Project Home Page",
+                    "downloadURL": "https://espo.nasa.gov/camp2ex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/camp2ex/docs/CAMP2Ex-overview-27NOV2015.pdf",
-                    "description": "NASA.gov CAMP2Ex Feature \u201cPhilippine Airborne Campaign Targets Weather, Climate Science\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov CAMP2Ex Feature \u201cPhilippine Airborne Campaign Targets Weather, Climate Science\u201d",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/camp2ex/docs/CAMP2Ex-overview-27NOV2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/philippine-airborne-campaign-targets-weather-climate-science",
-                    "description": "CAMP2Ex Mission Overview/White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "CAMP2Ex Mission Overview/White Paper",
+                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/philippine-airborne-campaign-targets-weather-climate-science",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1954736905-LARC_ASDC",
-                    "description": "Earthdata Search for CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1954736905-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
-                    "description": "DOI data set landing page for CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/camp2ex/",
-                    "description": "NASA Earth Expeditions CAMP2Ex Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions CAMP2Ex Posts",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/camp2ex/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/Cloud_AircraftInSitu_P3_Data_1/",
-                    "description": "ASDC Direct Data Download for CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/Cloud_AircraftInSitu_P3_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1954736905-LARC_ASDC",
+            "issued": "2020-07-20",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Airborne/CAMP2Ex_Cloud_AircraftInSitu_P3_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-02-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>0.0 -30.0 0.0 135.0 45.0 135.0 45.0 -30.0 0.0 -30.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-08-24T00:00:00Z/2019-10-05T23:59:59.999Z",
             "theme": [
                 "CAMP2Ex",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMP2Ex P-3 In-Situ Cloud Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-UVS-2-EDR-JUPITER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-uvs-2-edr-jupiter-v1.0_24kx-brmw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-UVS-2-EDR-JUPITER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-uvs-2-edr-jupiter-v1.0_24kx-brmw",
-            "description": "TBD",
-            "title": "GALILEO ORBITER UVS JUPITER OPERATIONS EDR DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO ORBITER UVS JUPITER OPERATIONS EDR DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-SWPLAS-3-RDR-GIACOBIN-ZIN-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "giacobini-zinner",
-                "international cometary explorer"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "These data were obtained from the LANL plasma experiment on ICE (Principal Investigator: S.J. Bame assistance from K. Sofaly and S. Kedge). The instrument measures the 2-D electron distribution function in one spacecraft rotation (3 s) once every 24 s, by obtaining 16 evenly spaced energy spectra, each with 15 contiguous levels covering the energy range 8.5 eV to 1140 eV. From these 2-D distributions the density, velocity, and temperature of the electrons are then derived. A 2-D temperature matrix is calculated which is subsequently diagonalized. Then nominally the maximum temperature corresponds to the parallel temperature and the minimum temperature corresponds to the perpendicular temperature. This is done independently of the magnetic field measurements however, the direction of maximum temperature determined in this manner is usually found to be within 15 degrees of the magnetic field direction inferred from the magnetometer measurements. The time resolution is 24 sec from the start of Day 253 (September 10) until Day 255 (September 12), 18:38. At that time the bit rate dropped from 1024 to 512 bps, and the nominal time resolution went to 48 sec.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-swplas-3-rdr-giacobin-zin-v1.0_24ky-x5un",
+            "issued": "2018-06-26",
+            "keyword": [
+                "giacobini-zinner",
+                "international cometary explorer"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ICE-C-SWPLAS-3-RDR-GIACOBIN-ZIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ice-c-swplas-3-rdr-giacobin-zin-v1.0_24ky-x5un",
-            "description": "These data were obtained from the LANL plasma experiment on ICE (Principal Investigator: S.J. Bame assistance from K. Sofaly and S. Kedge). The instrument measures the 2-D electron distribution function in one spacecraft rotation (3 s) once every 24 s, by obtaining 16 evenly spaced energy spectra, each with 15 contiguous levels covering the energy range 8.5 eV to 1140 eV. From these 2-D distributions the density, velocity, and temperature of the electrons are then derived. A 2-D temperature matrix is calculated which is subsequently diagonalized. Then nominally the maximum temperature corresponds to the parallel temperature and the minimum temperature corresponds to the perpendicular temperature. This is done independently of the magnetic field measurements however, the direction of maximum temperature determined in this manner is usually found to be within 15 degrees of the magnetic field direction inferred from the magnetometer measurements. The time resolution is 24 sec from the start of Day 253 (September 10) until Day 255 (September 12), 18:38. At that time the bit rate dropped from 1024 to 512 bps, and the nominal time resolution went to 48 sec.",
-            "title": "ICE SOLAR WIND PLASMA ELECTRON ANALYSER DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ICE SOLAR WIND PLASMA ELECTRON ANALYSER DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/14563",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-10-01",
-            "temporal": "2013-10-01T00:00:00Z/2014-09-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://techport.nasa.gov/home",
-                "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
-                "http://techport.nasa.gov/fetchFile?objectId=6561",
-                "http://techport.nasa.gov/fetchFile?objectId=3456",
-                "http://techport.nasa.gov/fetchFile?objectId=3447",
-                "http://techport.nasa.gov/fetchFile?objectId=6584",
-                "http://techport.nasa.gov/fetchFile?objectId=6560",
-                "http://techport.nasa.gov/fetchFile?objectId=3448"
-            ],
-            "keyword": [
-                "goddard space flight center",
-                "completed",
-                "project"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Julie Crooke",
                 "hasEmail": "mailto:julie.a.crooke@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "N/A"
-            },
-            "identifier": "TECHPORT_14563",
             "description": "&lt;p&gt;Precisely identifying the species of cosmic-ray nuclei detected by a satellite or balloon instrument requires the use of several complementary detector systems. In particular, determining the nuclear charge of an incident nucleus, and so the element to which it belongs, requires precise measurements of the differential energy loss of the particle passing through a well-characterized layer of material, the velocity of the particle, and its trajectory. The goal of this project is to improve detectors for these measurements.&lt;/p&gt;",
-            "title": "HNX/DragonTIGER Instrument Development Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/14563",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_14563",
+            "issued": "2013-10-01",
+            "keyword": [
+                "goddard space flight center",
+                "completed",
+                "project"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/14563",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "N/A"
+            },
+            "references": [
+                "http://techport.nasa.gov/home",
+                "http://techport.nasa.gov/doc/home/TechPort_Advanced_Search.pdf",
+                "http://techport.nasa.gov/fetchFile?objectId=6561",
+                "http://techport.nasa.gov/fetchFile?objectId=3456",
+                "http://techport.nasa.gov/fetchFile?objectId=3447",
+                "http://techport.nasa.gov/fetchFile?objectId=6584",
+                "http://techport.nasa.gov/fetchFile?objectId=6560",
+                "http://techport.nasa.gov/fetchFile?objectId=3448"
+            ],
+            "temporal": "2013-10-01T00:00:00Z/2014-09-01T00:00:00Z",
+            "title": "HNX/DragonTIGER Instrument Development Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L3M/KD/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/TERRA/MODIS/L3M/KD/2022.",
-            "issued": "2019-06-23",
-            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-08-08",
-            "keyword": [
-                "ngda",
-                "earth science",
-                "national geospatial data asset",
-                "ocean optics",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sdps@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C2331487774-OB_DAAC",
             "description": "MODIS (or Moderate-Resolution Imaging Spectroradiometer) is a key instrument aboard the Terra (EOS AM) and Aqua (EOS PM) satellites. Terra's orbit around the Earth is timed so that it passes from north to south across the equator in the morning, while Aqua passes south to north over the equator in the afternoon. Terra MODIS and Aqua MODIS are viewing the entire Earth's surface every 1 to 2 days, acquiring data in 36 spectral bands, or groups of wavelengths (see MODIS Technical Specifications). These data will improve our understanding of global dynamics and processes occurring on the land, in the oceans, and in the lower atmosphere. MODIS is playing a vital role in the development of validated, global, interactive Earth system models able to predict global change accurately enough to assist policy makers in making sound decisions concerning the protection of our environment.",
-            "title": "Terra MODIS Global Mapped Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL3M%2FKD%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FMODIS%2FL3M%2FKD%2F2022",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
-                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/",
-                    "description": "NASA Ocean Color Web - Processing History",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Processing History",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/citations/",
-                    "description": "NASA Ocean Color Web - Data Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Citation Policy",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/citations/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/KD/2022",
-                    "description": "MODIS-Terra L3M Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Terra L3M Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/TERRA/MODIS/L3M/KD/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODIST/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Terra MODIS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Terra MODIS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/MODIST/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2331487774-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "ngda",
+                "earth science",
+                "national geospatial data asset",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/MODIS/L3M/KD/2022",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-08-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Terra MODIS Global Mapped Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/SSF1DEGMONTH_L3.001B",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2020-05-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NOAA20/CERES/SSF1DEGMONTH_L3.001B.",
-            "issued": "2021-10-22",
-            "temporal": "2018-05-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-14",
-            "keyword": [
-                "atmospheric pressure",
-                "aerosols",
-                "earth science",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmosphere",
-                "clouds",
-                "atmospheric winds",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DAVID DOELLING",
                 "hasEmail": "mailto:ceres-help@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2246001791-LARC_ASDC",
             "description": "The Clouds and the Earth's Radiant Energy System (CERES) Single Scanner Footprint One Degree (SSF1deg) Month provides monthly averages of regional constant meteorology temporally interpolated CERES Top of Atmosphere (TOA) fluxes, clouds derived from a co-located imager and aerosols on a 1-degree latitude and longitude grid. One degree zonally and global averaged values for the parameters are also provided. This is a single satellite product that uses the primary CERES instrument in cross-track mode. TOA fluxes are provided for clear-sky and all-sky conditions for longwave (LW), shortwave (SW), and window wavelength bands. The incoming solar daily irradiance is from the Solar Radiation and Climate Experiment9 SORCE), Total Solar Irradiance (TSI). The cloud properties are averaged for both day and night (24-hour) and day-only time periods. Cloud properties are stratified into 4 atmospheric layers (surface-700 hPa, 700 hPa - 500 hPa, 500 hPa - 300 hPa, 300 hPa - 100 hPa) and a total of all layers. The aerosols are averaged instantaneous values from the co-located imager.CERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument (PFM) was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the EOS flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board EOS Aqua on May 4, 2002. The CERES instrument (FM5) was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite on November 18, 2017.",
-            "title": "CERES Time-Interpolated TOA Fluxes, Clouds and Aerosols Monthly NOAA-20 Edition1B",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FSSF1DEGMONTH_L3.001B",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNOAA20%2FCERES%2FSSF1DEGMONTH_L3.001B",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/",
-                    "description": "CERES project home page",
                     "@type": "dcat:Distribution",
+                    "description": "CERES project home page",
+                    "downloadURL": "https://ceres.larc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/SSF1DEGMONTH_L3.001B",
-                    "description": "DOI data set landing page for CER_SSF1deg-Month_NOAA20-VIIRS_Edition1B",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_SSF1deg-Month_NOAA20-VIIRS_Edition1B",
+                    "downloadURL": "https://doi.org/10.5067/NOAA20/CERES/SSF1DEGMONTH_L3.001B",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001791-LARC_ASDC",
-                    "description": "Earthdata Search for CER_SSF1deg-Month_NOAA20-VIIRS_Edition1B (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_SSF1deg-Month_NOAA20-VIIRS_Edition1B (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2246001791-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
-                    "description": "How to cite ASDC data",
                     "@type": "dcat:Distribution",
+                    "description": "How to cite ASDC data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/citing-data",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SSF1deg_Ed4A_DQS.pdf",
-                    "description": "Quality Summary: CERES_SSF1deg-Hour/Day/Month_Ed4A (3/13/2018)",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES_SSF1deg-Hour/Day/Month_Ed4A (3/13/2018)",
+                    "downloadURL": "https://ceres.larc.nasa.gov/documents/DQ_summaries/CERES_SSF1deg_Ed4A_DQS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/CERES",
-                    "description": "ASDC Data and Information for CERES",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for CERES",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/CERES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/ceres_data_products_catalogs.pdf",
-                    "description": "CERES Data Products Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Catalog",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/ceres_data_products_catalogs.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/level_table.pdf",
-                    "description": "CERES Processing Level Details",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Processing Level Details",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/level_table.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/product_level_details.pdf",
-                    "description": "CERES Product Level Details",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Product Level Details",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/product_level_details.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/40",
-                    "description": "NASA EOS ATB Documents: CERES",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: CERES",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/40",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/",
-                    "description": "CERES Data Products Browse, Subset, and Order",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Browse, Subset, and Order",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/SSF1degNOAA20Selection.jsp",
-                    "description": "CERES Data Products Browse, Subset, and Order: Single Scanner Footprint (SSF) 1degree",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Products Browse, Subset, and Order: Single Scanner Footprint (SSF) 1degree",
+                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/jsp/SSF1degNOAA20Selection.jsp",
+                    "mediaType": "text/html",
                     "title": "Subset this dataset using a web based subsetter"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/general-product-info/",
-                    "description": "CERES General Product Info",
                     "@type": "dcat:Distribution",
+                    "description": "CERES General Product Info",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/general-product-info/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/general-product-info/#ceres-input-data-sources",
-                    "description": "CERES Input Data Sources",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Input Data Sources",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/general-product-info/#ceres-input-data-sources",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#noaa20",
-                    "description": "CERES Overview of NOAA-20",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of NOAA-20",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#noaa20",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ssf1deg-month.pdf",
-                    "description": "CERES Time-Interpolated TOA/Surface Fluxes, Clouds and Aerosols(SSF1deg-Day/Month)Data Set Abstract",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Time-Interpolated TOA/Surface Fluxes, Clouds and Aerosols(SSF1deg-Day/Month)Data Set Abstract",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/guide/cer_ssf1deg-month.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/hdf_sds_info.pdf",
-                    "description": "HDF Science Data Set (SDS) Information Tool Overview",
                     "@type": "dcat:Distribution",
+                    "description": "HDF Science Data Set (SDS) Information Tool Overview",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/hdf_sds_info.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/hdf_sds_info_readme.txt",
-                    "description": "HDF Scientific Data Set (SDS) Information Utility Readme",
                     "@type": "dcat:Distribution",
+                    "description": "HDF Scientific Data Set (SDS) Information Utility Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/hdf_sds_info_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/hdf.pdf",
-                    "description": "Hierarchical Data Format (HDF) Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Hierarchical Data Format (HDF) Overview",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/hdf.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/ftp_instruct.pdf",
-                    "description": "Directions on downloading and installing the HDF libraries",
                     "@type": "dcat:Distribution",
+                    "description": "Directions on downloading and installing the HDF libraries",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/ftp_instruct.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/hdf_data_manipulation.pdf",
-                    "description": "HDF data manipulation software (applications to open a Hierarchical Data Format (HDF) file and display a browse image and/or data file information)",
                     "@type": "dcat:Distribution",
+                    "description": "HDF data manipulation software (applications to open a Hierarchical Data Format (HDF) file and display a browse image and/or data file information)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/hdf_data_manipulation.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/view_hdf_UG5.0.pdf",
-                    "description": "CERES Data Management System View HDF User's Guide - Version 5.0, November 2007",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Data Management System View HDF User's Guide - Version 5.0, November 2007",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/view_hdf_UG5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/view_hdf.pdf",
-                    "description": "View HDF: A Visualization and Analysis Tool for HDF Files (overview of and resources for using view_hdf)",
                     "@type": "dcat:Distribution",
+                    "description": "View HDF: A Visualization and Analysis Tool for HDF Files (overview of and resources for using view_hdf)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/view_hdf.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF1deg-Month/NOAA20-VIIRS_Edition1B/",
-                    "description": "ASDC Direct Data Download for CER_SSF1deg-Month_NOAA20-VIIRS_Edition1B",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_SSF1deg-Month_NOAA20-VIIRS_Edition1B",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/SSF1deg-Month/NOAA20-VIIRS_Edition1B/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF1deg-Month/NOAA20-VIIRS_Edition1B/contents.html",
-                    "description": "OPeNDAP data access for CER_SSF1deg-Month_NOAA20-VIIRS_Edition1B",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_SSF1deg-Month_NOAA20-VIIRS_Edition1B",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/SSF1deg-Month/NOAA20-VIIRS_Edition1B/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2246001791-LARC_ASDC",
+            "issued": "2021-10-22",
+            "keyword": [
+                "atmospheric pressure",
+                "aerosols",
+                "earth science",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere",
+                "clouds",
+                "atmospheric winds",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/NOAA20/CERES/SSF1DEGMONTH_L3.001B",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2018-05-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Time-Interpolated TOA Fluxes, Clouds and Aerosols Monthly NOAA-20 Edition1B"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/921/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-08-11",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Daigle",
                 "hasEmail": "mailto:matthew.j.daigle@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_921",
             "description": "Complex engineering systems require efficient on-line fault diagnosis methodologies to improve safety and reduce maintenance costs. Traditionally, diagnosis approaches are centralized, but these solutions do not scale well. Also, centralized diagnosis solutions are difficult to implement on increasingly prevalent distributed, networked embedded systems. This paper presents a distributed diagnosis framework for physical systems with continuous behavior. Using Possible Conflicts, a structural model decomposition method from the Artificial Intelligence model-based diagnosis (DX) community, we develop a distributed diagnoser design algorithm to build local event-based diagnosers. These diagnosers are constructed based on global diagnosability analysis of the system, enabling them to generate local diagnosis results that are globally correct without the use of a centralized coordinator. We also use Possible Conflicts to design local parameter estimators that are integrated with the local diagnosers to form a comprehensive distributed diagnosis framework. Hence, this is a fully distributed approach to fault detection, isolation, and identification. We evaluate the developed scheme on a four-wheeled rover for different design scenarios to show the advantages of using Possible Conflicts, and generate on-line diagnosis results in simulation to demonstrate the approach.",
-            "title": "An Event-based Distributed Diagnosis Framework using Structural Model Decomposition",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/BregonEtAl-DistributedDiagnosis-AI.pdf",
-                    "description": "BregonEtAl-DistributedDiagnosis-AI.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "BregonEtAl-DistributedDiagnosis-AI.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/BregonEtAl-DistributedDiagnosis-AI.pdf",
+                    "mediaType": "application/pdf",
                     "title": "BregonEtAl-DistributedDiagnosis-AI.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_921",
+            "issued": "2014-08-11",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/921/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "An Event-based Distributed Diagnosis Framework using Structural Model Decomposition"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-HYDROGEN-MAP_V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "dawn mission to vesta and ceres",
-                "1 ceres"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "A global map of the                     concentration of hydrogen within the regolith of asteroid 1 Ceres       on twenty-degree quasi-equal-area pixels is provided. Hydrogen          concentrations were determined from thermal+epithermal neutron          counting data acquired by the NASA Dawn mission's Gamma Ray and Neutron Detector (GRaND) while in low altitude mapping orbit, about 385 km from Ceres' surface (about 0.8 body radii altitude).  The concentrations are representative of Ceres's bulk  regolith to depths up to a few          decimeters with a spatial resolution of about 600-km                    full-width-at-half-maximum of arc length on the surface. The methods    used to determine hydrogen concentration are described by               PRETTYMANETAL2017.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-hydrogen-map_v1.0_24vs-mivw",
+            "issued": "2018-06-26",
+            "keyword": [
+                "dawn mission to vesta and ceres",
+                "1 ceres"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DAWN-A-GRAND-5-CERES-HYDROGEN-MAP_V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dawn-a-grand-5-ceres-hydrogen-map_v1.0_24vs-mivw",
-            "description": "A global map of the                     concentration of hydrogen within the regolith of asteroid 1 Ceres       on twenty-degree quasi-equal-area pixels is provided. Hydrogen          concentrations were determined from thermal+epithermal neutron          counting data acquired by the NASA Dawn mission's Gamma Ray and Neutron Detector (GRaND) while in low altitude mapping orbit, about 385 km from Ceres' surface (about 0.8 body radii altitude).  The concentrations are representative of Ceres's bulk  regolith to depths up to a few          decimeters with a spatial resolution of about 600-km                    full-width-at-half-maximum of arc length on the surface. The methods    used to determine hydrogen concentration are described by               PRETTYMANETAL2017.",
-            "title": "DAWN GRAND MAP CERES                    \n                                      HYDROGEN MAP V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DAWN GRAND MAP CERES                    \n                                      HYDROGEN MAP V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-2-EDR-CRUISE1-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "near earth asteroid rendezvous",
-                "solar system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-2-edr-cruise1-v1.0_24wr-w7b4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "near earth asteroid rendezvous",
+                "solar system"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-NLR-2-EDR-CRUISE1-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-nlr-2-edr-cruise1-v1.0_24wr-w7b4",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR NLR DATA FOR CRUISE1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEAR NLR DATA FOR CRUISE1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/683",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Zinke, P.J., A.G. Stangenberger, W.M. Post, W.R. Emanuel, and J.S. Olson. 2003. LBA Regional Organic Soil Carbon and Nitrogen Data (Zinke et al.). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/683",
-            "issued": "2023-10-03",
-            "temporal": "1940-01-01T00:00:00Z/1984-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "earth science",
-                "soils",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2777326924-ORNL_CLOUD",
             "description": "The data set contains a subset of a global organic soil carbon and nitrogen data set (Zinke et al. 1986). The subset was created for the study area of the Large Scale Biosphere-Atmosphere Experiment in Amazonia (LBA) in South America (i.e., 10 N to 25 S, 30 to 85 W). The point data are available in three formats: a comma-delimited ASCII file (*.csv), an ESRI shapefile, and an ESRI export file (*.e00).The data for the global data set (Zinke et al. 1986) were obtained from soil surveys conducted by Zinke in 1965-1984 and from soil survey literature. The main samples for laboratory analyses were collected at uniform soil increments and included bulk density determinations. Many samples reported in the literature did not have uniform soil increments or bulk density determinations. Only soil profiles that had been sampled either to a meter in depth or to actual depth were included in this database from soil survey literature. When carbon content was known but bulk densities were absent from soil samples reported in the literature, densities were estimated by regression analysis on the basis of the relationship between organic carbon content and measured bulk density in 1800 soil profiles for which bulk densities were known.Further information can be found at ftp://daac.ornl.gov/data/lba/carbon_dynamics/Zinke_soil/comp/zinke_readme.pdf.LBA was a cooperative international research initiative led by Brazil. NASA was a lead sponsor for several experiments. LBA was designed to create the new knowledge needed to understand the climatological, ecological, biogeochemical, and hydrological functioning of Amazonia; the impact of land use change on these functions; and the interactions between Amazonia and the Earth system. More information about LBA can be found at http://www.daac.ornl.gov/LBA/misc_amazon.html.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA Regional Organic Soil Carbon and Nitrogen Data (Zinke et al.)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F683",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F683",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/Zinke_soil/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/Zinke_soil/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_zinke.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_zinke.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/683",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/683",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/Zinke_soil/comp/readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/Zinke_soil/comp/readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/Zinke_soil/comp/zinke_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/Zinke_soil/comp/zinke_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
+            "identifier": "C2777326924-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "soils",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/683",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-85.0 -25.0 -30.0 10.0",
+            "temporal": "1940-01-01T00:00:00Z/1984-12-31T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA Regional Organic Soil Carbon and Nitrogen Data (Zinke et al.)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GWHRZEL8SA21",
             "citation": "Vrije Universiteit Amsterdam (Richard de Jeu) and NASA GSFC (Manfred Owe). Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng). 2012-04-16. LPRM_TMI_NT_SOILM3. TMI/TRMM surface soil moisture (LPRM) L3 1 day 25 km x 25 km nighttime V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/GWHRZEL8SA21. https://disc.gsfc.nasa.gov/datacollection/LPRM_TMI_NT_SOILM3_001.html.",
-            "issued": "2012-04-06",
-            "temporal": "1997-12-07T23:57:18Z/2015-04-08T15:25:03Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-04-06",
-            "references": [
-                "https://doi.org/10.1029/2007JF000769",
-                "https://doi.org/10.1007/s10712-008-9044-0",
-                "https://doi.org/10.1029/2008JD010257",
-                "https://doi.org/10.1109/LGRS.2011.2114872"
-            ],
-            "keyword": [
-                "land surface",
-                "earth science",
-                "soils",
-                "biosphere",
-                "surface thermal properties",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RICHARD DE JEU",
                 "hasEmail": "mailto:Richard.de.jeu@falw.vu.nl"
             },
-            "identifier": "C1235338554-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "description": "TMI/TRMM surface soil moisture (LPRM) L3 1 day 25 km x 25 km nighttime V001 is Level 3 (gridded) data set. Its land surface parameters, surface soil moisture, land surface (skin) temperature, and vegetation water content, are derived from passive microwave remote sensing data from the Tropical Rainfall Measuring Mission (TRMM) Microwave Imager (TMI), using the Land Parameter Retrieval Model (LPRM). There are two files per day, one daytime and one nighttime, archived as two different products. This document is for the nighttime product. The data set covers the period from December 1997 to April 2015 (when the instruments on the TRMM satellite were shut down in preparation for its reentry into the earth's atmosphere).\n\nThe LPRM is based on a forward radiative transfer model to retrieve surface soil moisture and vegetation optical depth. The land surface temperature is derived separately from TMI's Ka-band (37 GHz). A unique feature of this method is that it can be applied at any microwave frequency, making it very suitable to exploit all the available passive microwave data from various satellites.\n\nInput data are from the TMI Brightness Temperatures (1B-11) product, nighttime passes, as processed using LPRM (i.e., LPRM/TMI/TRMM Level 2 product, LPRM_TMI_SOILM2_V001).",
-            "editor": "Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng)",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "LPRM_TMI_NT_SOILM3",
             "creator": "Vrije Universiteit Amsterdam (Richard de Jeu) and NASA GSFC (Manfred Owe)",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface\n(Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "TMI/TRMM surface soil moisture (LPRM) L3 1 day 25 km x 25 km nighttime V001 (LPRM_TMI_NT_SOILM3) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=&endtime=&dataKeyword=LPRM_TMI_NT_SOILM3",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "TMI/TRMM surface soil moisture (LPRM) L3 1 day 25 km x 25 km nighttime V001 is Level 3 (gridded) data set. Its land surface parameters, surface soil moisture, land surface (skin) temperature, and vegetation water content, are derived from passive microwave remote sensing data from the Tropical Rainfall Measuring Mission (TRMM) Microwave Imager (TMI), using the Land Parameter Retrieval Model (LPRM). There are two files per day, one daytime and one nighttime, archived as two different products. This document is for the nighttime product. The data set covers the period from December 1997 to April 2015 (when the instruments on the TRMM satellite were shut down in preparation for its reentry into the earth's atmosphere).\n\nThe LPRM is based on a forward radiative transfer model to retrieve surface soil moisture and vegetation optical depth. The land surface temperature is derived separately from TMI's Ka-band (37 GHz). A unique feature of this method is that it can be applied at any microwave frequency, making it very suitable to exploit all the available passive microwave data from various satellites.\n\nInput data are from the TMI Brightness Temperatures (1B-11) product, nighttime passes, as processed using LPRM (i.e., LPRM/TMI/TRMM Level 2 product, LPRM_TMI_SOILM2_V001).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGWHRZEL8SA21",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGWHRZEL8SA21",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -8008,427 +7975,437 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LPRM_TMI_NT_SOILM3_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LPRM_TMI_NT_SOILM3_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_TMI_NT_SOILM3.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_TMI_NT_SOILM3.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=&endtime=&dataKeyword=LPRM_TMI_NT_SOILM3",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface\n(Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface\n(Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=&endtime=&dataKeyword=LPRM_TMI_NT_SOILM3",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LPRM_TMI_NT_SOILM3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LPRM_TMI_NT_SOILM3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/LPRM_TMI_NT_SOILM3.001/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/LPRM_TMI_NT_SOILM3.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_TMI_NT_SOILM3.001/doc/README_LPRM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_TMI_NT_SOILM3.001/doc/README_LPRM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Hydrology+Documentation",
-                    "description": "GES DISC Hydrology Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "GES DISC Hydrology Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Hydrology+Documentation",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/tools?title=Hydrology+Data+Rods",
-                    "description": "GES DISC Data Rods Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "GES DISC Data Rods Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/tools?title=Hydrology+Data+Rods",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "editor": "Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng)",
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface\n(Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#service=TmAvMp&starttime=&endtime=&dataKeyword=LPRM_TMI_NT_SOILM3",
+            "identifier": "C1235338554-GES_DISC",
+            "issued": "2012-04-06",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "soils",
+                "biosphere",
+                "surface thermal properties",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/GWHRZEL8SA21",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-04-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2007JF000769",
+                "https://doi.org/10.1007/s10712-008-9044-0",
+                "https://doi.org/10.1029/2008JD010257",
+                "https://doi.org/10.1109/LGRS.2011.2114872"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "LPRM_TMI_NT_SOILM3",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "1997-12-07T23:57:18Z/2015-04-08T15:25:03Z",
             "theme": [
                 "TRMM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TMI/TRMM surface soil moisture (LPRM) L3 1 day 25 km x 25 km nighttime V001 (LPRM_TMI_NT_SOILM3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/KRWSPR2J1N2N",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "CLPX-Airborne: Infrared Orthophotography and Lidar Topographic Mapping, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/KRWSPR2J1N2N.",
-            "issued": "2003-04-08",
-            "temporal": "2003-04-08T00:00:00Z/2003-09-19T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-09-19",
-            "keyword": [
-                "topography",
-                "spectral/engineering",
-                "lidar",
-                "earth science",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Miller",
                 "hasEmail": "mailto:stevem@jkanda.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386203856-NSIDCV0",
             "description": "The data set consists of color infrared orthophotography (TerrainVision\u00ae - High resolution Topographic Mapping & Aerial Photography, with 6-inch pixel resolution), lidar elevation returns (raw/combined, filtered to bare ground/snow, and filtered to top of vegetation), elevation contours (0.5 meter) and snow depth contours (0.1 meter).",
-            "title": "CLPX-Airborne: Infrared Orthophotography and Lidar Topographic Mapping, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKRWSPR2J1N2N",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FKRWSPR2J1N2N",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/CLP/data/airborne/nsidc0157_lidar/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KRWSPR2J1N2N",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/KRWSPR2J1N2N",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/KRWSPR2J1N2N",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/KRWSPR2J1N2N",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386203856-NSIDCV0",
+            "issued": "2003-04-08",
+            "keyword": [
+                "topography",
+                "spectral/engineering",
+                "lidar",
+                "earth science",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/KRWSPR2J1N2N",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-09-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-107.5 39.5 -105.0 41.0",
+            "temporal": "2003-04-08T00:00:00Z/2003-09-19T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CLPX-Airborne: Infrared Orthophotography and Lidar Topographic Mapping, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-4-RDR-STEP-12.8MIN-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Description of the PDS LECP Neptune Step data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-4-rdr-step-12.8min-v1.0_252d-fy7u",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "neptune",
                 "comet sl9/jupiter collision",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-LECP-4-RDR-STEP-12.8MIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-lecp-4-rdr-step-12.8min-v1.0_252d-fy7u",
-            "description": "Description of the PDS LECP Neptune Step data.",
-            "title": "VG2 NEP LECP RESAMPLED RDR STEPPING SECTOR 12.8MIN V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 NEP LECP RESAMPLED RDR STEPPING SECTOR 12.8MIN V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/CPEXAW-ADM-Aeolus_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2022-07-21. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/CPEXAW-ADM-Aeolus_1.",
-            "issued": "2022-07-12",
-            "temporal": "2021-08-06T00:00:00Z/2021-09-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-21",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kristopher Bedka",
                 "hasEmail": "mailto:kristopher.m.bedka@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2404262719-LARC_ASDC",
             "description": "CPEXAW-ADM-Aeolus_1 is the ESA ADM-Aeolus Datasets for the Convective Processes Experiment - Aerosols & Winds (CPEX-AW) sub-orbital campaign. Data collection for this product is complete.\r\n\r\nThe Convective Processes Experiment \u2013 Aerosols & Winds (CPEX-AW) campaign was a joint effort between the US National Aeronautics and Space Administration (NASA) and the European Space Agency (ESA) with the primary goal of conducting a post-launch calibration and validation activities of the Atmospheric Dynamics Mission-Aeolus (ADM-AEOLUS) Earth observation wind Lidar satellite in St. Croix. CPEX-AW is a follow-on to the Convective Processes Experiment (CPEX) field campaign which took place in the summer of 2017. In addition to joint calibration/validation of ADM-AEOLUS, CPEX-AW studied the dynamics related to the Saharan Air Layer, African Easterly Waves and Jets, Tropical Easterly Jet, and deep convection in the InterTropical Convergence Zone (ITCZ). CPEX-AW science goals include:\r\n\u2022 Better understanding interactions of convective cloud systems and tropospheric winds as part of the joint NASA-ESA Aeolus Cal/Val effort over the tropical Atlantic;\r\n\u2022 Observing the vertical structure and variability of the marine boundary layer in relation to initiation and lifecycle of the convective cloud systems, convective processes (e.g., cold pools), and environmental conditions within and across the ITCZ;\r\n\u2022 Investigating how the African easterly waves and dry air and dust associated with Sahara Air Layer control the convectively suppressed and active periods of the ITCZ;\r\n\u2022 Investigating interactions of wind, aerosol, clouds, and precipitation and effects on long range dust transport and air quality over the western Atlantic.\r\nIn order to successfully achieve the objectives of the campaign, NASA deployed its DC-8 aircraft equipped with an Airborne Third Generation Precipitation Radar (APR-3), Doppler Aerosol WiNd Lidar (DAWN), High Altitude Lidar Observatory (HALO), High Altitude Monolithic Microwave Integrated Circuit (MMIC) Sounding Radiometer (HAMSR), and dropsondes. This campaign aims to provide useful material to atmospheric scientists, meteorologists, lidar experts, air quality experts, professors, and students. The Atmospheric Science Data Center (ASDC) archives the dropsonde, HALO, and DAWN data products for CPEX-AW. For additional datasets please visit the Global Hydrometeorology Resource Center (GHRC).",
-            "title": "CPEX-AW ADM-Aeolus Datasets",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FCPEXAW-ADM-Aeolus_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FCPEXAW-ADM-Aeolus_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/cpex-aw/content/CPEX-AW",
-                    "description": "CPEX-AW Project Overview",
                     "@type": "dcat:Distribution",
+                    "description": "CPEX-AW Project Overview",
+                    "downloadURL": "https://espo.nasa.gov/cpex-aw/content/CPEX-AW",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/101/10/BAMSD190020.xml",
-                    "description": "An Eye on the Storm: Integrating a Wealth of Data for Quickly Advancing the Physical Understanding and Forecasting of Tropical Cyclones",
                     "@type": "dcat:Distribution",
+                    "description": "An Eye on the Storm: Integrating a Wealth of Data for Quickly Advancing the Physical Understanding and Forecasting of Tropical Cyclones",
+                    "downloadURL": "https://journals.ametsoc.org/view/journals/bams/101/10/BAMSD190020.xml",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://meetingorganizer.copernicus.org/EGU21/EGU21-8975.html",
-                    "description": "NASA\u2019s Contributions to the 2021 Aeolus Field Campaign: CPEX-AW",
                     "@type": "dcat:Distribution",
+                    "description": "NASA\u2019s Contributions to the 2021 Aeolus Field Campaign: CPEX-AW",
+                    "downloadURL": "https://meetingorganizer.copernicus.org/EGU21/EGU21-8975.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cpex.jpl.nasa.gov/cpex-aw/index.php",
-                    "description": "CPEX-AW JPL Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "CPEX-AW JPL Project Home Page",
+                    "downloadURL": "https://cpex.jpl.nasa.gov/cpex-aw/index.php",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/cpex-aw",
-                    "description": "GHRC CPEX-AW Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRC CPEX-AW Home Page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/cpex-aw",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_details/collections/cpexawC.html",
-                    "description": "GHRC CPEX-AW Data",
                     "@type": "dcat:Distribution",
+                    "description": "GHRC CPEX-AW Data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_details/collections/cpexawC.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earth.esa.int/web/eoportal/satellite-missions/a/adm-aeolus",
-                    "description": "ESA ADM-Aeolus Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ESA ADM-Aeolus Home Page",
+                    "downloadURL": "https://earth.esa.int/web/eoportal/satellite-missions/a/adm-aeolus",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/CPEXAW-ADM-Aeolus_1",
-                    "description": "DOI for CPEXAW-ADM-AEOLUS_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for CPEXAW-ADM-AEOLUS_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/CPEXAW-ADM-Aeolus_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2404262719-LARC_ASDC",
-                    "description": "Earthdata Search client for CPEXAW-ADM-AEOLUS_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for CPEXAW-ADM-AEOLUS_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2404262719-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/CPEXAW/2021",
-                    "description": "CPEX-AW Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "CPEX-AW Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/CPEXAW/2021",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the Sub-Orbital Order Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CPEX-AW/ADM-Aeolus_1/",
-                    "description": "ASDC Direct Data Download for CPEXAW-ADM-Aeolus_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CPEXAW-ADM-Aeolus_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CPEX-AW/ADM-Aeolus_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CPEX-AW/ADM-Aeolus_1/contents.html",
-                    "description": "OPeNDAP data access for CPEXAW-ADM-Aeolus_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CPEXAW-ADM-Aeolus_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CPEX-AW/ADM-Aeolus_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2404262719-LARC_ASDC",
+            "issued": "2022-07-12",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/CPEXAW-ADM-Aeolus_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>11.0 -125.0 11.0 -45.0 35.0 -45.0 35.0 -125.0 11.0 -125.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2021-08-06T00:00:00Z/2021-09-17T23:59:59.999Z",
             "theme": [
                 "CPEX-AW",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CPEX-AW ADM-Aeolus Datasets"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-9.60SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "jupiter",
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes Voyager 1 Jupiter encounter magnetometer data that have been resampled at a 9.6 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979 Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-9.60sec_254h-wtkb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-9.60SEC",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-9.60sec_254h-wtkb",
-            "description": "This data set includes Voyager 1 Jupiter encounter magnetometer data that have been resampled at a 9.6 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979 Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
-            "title": "VOYAGER 1 JUPITER MAGNETOMETER RESAMPLED DATA 9.60 SEC",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VOYAGER 1 JUPITER MAGNETOMETER RESAMPLED DATA 9.60 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "NHSNOWM",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/JIJNARIFGY4G",
             "citation": "Peter Romanov, PhD. 2006-10-20. NHSNOWM. Version 001. Northern Hemisphere Snow Cover Monthly Statistics at 1 Degree Resolution V001. NASA GSFC. NHSNOWM. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/JIJNARIFGY4G. https://disc.gsfc.nasa.gov/datacollection/NHSNOWM_001.html. Digital Science Data.",
-            "issued": "2009-03-10",
-            "temporal": "2000-01-01T00:00:00Z/2014-11-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-11-30",
-            "keyword": [
-                "snow/ice",
-                "cryosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PETER ROMANOV, PHD",
                 "hasEmail": "mailto:Peter.Romanov@noaa.gov"
             },
+            "creator": "Peter Romanov, PhD",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1239898025-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This product is Snow Cover Statistics. The dataset was prepared by Dr. Peter Romanov at Cooperative Institute for Climate Studies(CICS) of the University of Maryland for Northern Eurasia Earth Science Partnership Initiative (NEESPI) program. \n                        \n The product includes the monthly snow statistics (frequency of occurrence) for Northern Hemisphere at 1x1 degree spatial resolution. The dataset covers the time period from January 2000 to November 2014.\n \n Monthly data were derived from daily snow cover charts produced at NOAA/NESDIS within Interactive Multisensor Ice Mapping System (IMS).",
-            "release-place": "NASA GSFC",
-            "series-name": "NHSNOWM",
-            "creator": "Peter Romanov, PhD",
-            "title": "Northern Hemisphere Snow Cover Monthly Statistics at 1 Degree Resolution V001 (NHSNOWM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NHSNOWM_001.gif",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJIJNARIFGY4G",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJIJNARIFGY4G",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -8438,972 +8415,973 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NHSNOWM_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NHSNOWM_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Snow_Ice/NHSNOWM.001",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Snow_Ice/NHSNOWM.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Snow_Ice/NHSNOWM.001/doc/README.NHSNOWICE.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://reason.gesdisc.eosdis.nasa.gov/data/Snow_Ice/NHSNOWM.001/doc/README.NHSNOWICE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NHSNOWM_001.gif",
+            "identifier": "C1239898025-GES_DISC",
+            "issue-identification": "NHSNOWM",
+            "issued": "2009-03-10",
+            "keyword": [
+                "snow/ice",
+                "cryosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/JIJNARIFGY4G",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-11-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "NASA GSFC",
+            "series-name": "NHSNOWM",
             "spatial": "-180.0 0.0 180.0 90.0",
+            "temporal": "2000-01-01T00:00:00Z/2014-11-30T23:59:59.999Z",
             "theme": [
                 "NEESPI NASA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Northern Hemisphere Snow Cover Monthly Statistics at 1 Degree Resolution V001 (NHSNOWM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-VMC-2-EDR-EXT3-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "mars express",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "N/A",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-vmc-2-edr-ext3-v1.0_25bp-bzrn",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-VMC-2-EDR-EXT3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-vmc-2-edr-ext3-v1.0_25bp-bzrn",
-            "description": "N/A",
-            "title": "MEX MARS VMC RAW DATA EXT3 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MEX MARS VMC RAW DATA EXT3 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/RADIOMETER/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Derksen, Chris.2013. GPM GROUND VALIDATION ENVIRONMENT CANADA (EC) PASSIVE MICROWAVE RADIOMETER AND SOIL MOISTURE-TEMPERATURE DATA GCPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/GCPEX/RADIOMETER/DATA101",
-            "issued": "2013-10-18",
-            "temporal": "2011-12-05T19:15:00Z/2012-03-03T10:30:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-23",
-            "keyword": [
-                "soils",
-                "snow/ice",
-                "microwave",
-                "agriculture",
-                "earth science",
-                "terrestrial hydrosphere",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-ghrc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/MSFC/GHRC"
-            },
-            "identifier": "C1979695109-GHRC_DAAC",
             "description": "The GPM Ground Validation Environment Canada (EC) Passive Microwave Radiometer and Soil Moisture-Temperature Data GCPEx dataset is consisted of data during the GPM Cold-season Precipitation Experiment (GCPEx) at the Centre for Atmospheric Research Experiments (CARE) site in Ontario, Canada during the winter season 2011-2012. GCPEx addressed shortcomings in the GPM snowfall retrieval algorithm by collecting microphysical properties, associated remote sensing observations, and coordinated model simulations of precipitating snow. Data collected includes microwave brightness temperatures, snow and soil/snow-air interface (ground surface temperatures), soil surface temperatures, and soil volumetric water content. These data were acquired by multiple instruments: a passive microwave radiometer, a water content reflectometer, thermistors, soil moisture probe.",
-            "title": "GPM GROUND VALIDATION ENVIRONMENT CANADA (EC) PASSIVE MICROWAVE RADIOMETER AND SOIL MOISTURE-TEMPERATURE DATA GCPEX V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FRADIOMETER%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FGCPEX%2FRADIOMETER%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmradpmgcpex",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmradpmgcpex",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/GCPEX/DATA101",
-                    "description": "GCPEx Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "GCPEx Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/GCPEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_pm_CARE/doc/gpmpmradgcpex_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_pm_CARE/doc/gpmpmradgcpex_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_pm_CARE/doc/TechnicianDailyNotes_pm_radiometer_data_Dec2011-March2012-EC_CARE_LogBook.pdf",
-                    "description": "Technician Daily Notes, Radiometer Dec 2011 - March 2012",
                     "@type": "dcat:Distribution",
+                    "description": "Technician Daily Notes, Radiometer Dec 2011 - March 2012",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_pm_CARE/doc/TechnicianDailyNotes_pm_radiometer_data_Dec2011-March2012-EC_CARE_LogBook.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_pm_CARE/doc/TechnicianNotes_soil_moisture_temperature_data_Dec2011-March2012-EC_CARE.doc",
-                    "description": "Soil Moisture and Surface Temperature Summary -Up for GCpex 2011/2012",
                     "@type": "dcat:Distribution",
+                    "description": "Soil Moisture and Surface Temperature Summary -Up for GCpex 2011/2012",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_pm_CARE/doc/TechnicianNotes_soil_moisture_temperature_data_Dec2011-March2012-EC_CARE.doc",
+                    "mediaType": "application/msword",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_pm_CARE/doc/MetadataFormatInformation_pm_radiometer_soil_moisture_data_Dec2011-March2012-EC_CARE.xlsx",
-                    "description": "Meta data, Radiometer soil moisture data Dec 2011 - March 2012",
                     "@type": "dcat:Distribution",
+                    "description": "Meta data, Radiometer soil moisture data Dec 2011 - March 2012",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/gcpex/radiometer_pm_CARE/doc/MetadataFormatInformation_pm_radiometer_soil_moisture_data_Dec2011-March2012-EC_CARE.xlsx",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/GCPEx",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/GCPEx",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/lake-effect-snow",
-                    "description": "Lake Effect Snow Micro Article",
                     "@type": "dcat:Distribution",
+                    "description": "Lake Effect Snow Micro Article",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/lake-effect-snow",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
-                    "description": "Instructions for citing GHRC data",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for citing GHRC data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/about-ghrc/citing-ghrc-daac-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1979695109-GHRC_DAAC",
+            "issued": "2013-10-18",
+            "keyword": [
+                "soils",
+                "snow/ice",
+                "microwave",
+                "agriculture",
+                "earth science",
+                "terrestrial hydrosphere",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/GCPEX/RADIOMETER/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-79.7906 44.2232 -79.7706 44.2432",
+            "temporal": "2011-12-05T19:15:00Z/2012-03-03T10:30:00Z",
             "theme": [
                 "GCPEx",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM GROUND VALIDATION ENVIRONMENT CANADA (EC) PASSIVE MICROWAVE RADIOMETER AND SOIL MOISTURE-TEMPERATURE DATA GCPEX V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-4-SUMM-LUNARCRDS-5SEC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "moon",
-                "lunar prospector"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-4-summ-lunarcrds-5sec-v1.0_25g4-6zif",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "lunar prospector"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-MAG-4-SUMM-LUNARCRDS-5SEC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-mag-4-summ-lunarcrds-5sec-v1.0_25g4-6zif",
-            "description": "not applicable",
-            "title": "LP MAGER SPINAVG MAGNETIC FIELD LUNAR COORDS 5SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LP MAGER SPINAVG MAGNETIC FIELD LUNAR COORDS 5SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_LUNAR_LAKE_2001_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2002-08-01. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/AIRMISR_LUNAR_LAKE_2001_1.",
-            "issued": "2004-03-24",
-            "temporal": "2001-06-30T00:00:00Z/2001-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "visible wavelengths",
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CAROL BRUEGGE",
                 "hasEmail": "mailto:carol.j.bruegge@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000704-LARC_ASDC",
             "description": "The AIRMISR_LUNAR_LAKE_2001 data were acquired during a flight over Lunar Lake, Nevada on June 30, 2001. The Jet Propulsion Laboratory (JPL) in Pasadena, California provided the data. The Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) is an airborne instrument for obtaining multi-angle imagery similar to that of the satellite-borne Multi-angle Imaging SpectroRadiometer (MISR) instrument, which is designed to contribute to studies of the Earth's ecology and climate. AirMISR flies on the NASA ER-2 aircraft. The Jet Propulsion Laboratory in Pasadena, California built the instrument for NASA. Unlike the satellite-borne MISR instrument, which has nine cameras oriented at various angles, AirMISR uses a single camera in a pivoting gimbal mount. A data run by the ER-2 aircraft is divided into nine segments, each with the camera positioned to a MISR look angle. The gimbal rotates between successive segments, such that each segment acquires data over the same area on the ground as the previous segment. This process is repeated until all nine angles of the target area are collected. The swath width, which varies from 11 km in the nadir to 32 km at the most oblique angle, is governed by the camera's instantaneous field-of-view of 7 meters cross-track x 6 meters along-track in the nadir view and 21 meters x 55 meters at the most oblique angle. The along-track image length at each angle is dictated by the timing required to obtain overlap imagery at all angles, and varies from about 9 km in the nadir to 26 km at the most oblique angle. Thus, the nadir image dictates the area of overlap that is obtained from all nine angles. A complete flight run takes approximately 13 minutes. The 9 camera viewing angles are:0 degrees or nadir26.1 degrees, fore and aft45.6 degrees, fore and aft60.0 degrees, fore and aft70.5 degrees, fore and aft For each of the camera angles, images are obtained at 4 spectral bands. The spectral bands can be used to identify vegetation and aerosols, estimate surface reflectance and ocean color studies. The center wavelengths of the 4 spectral bands are:443 nanometers, blue555 nanometers, green670 nanometers, red865 nanometers, near-infrared Two types of AirMISR data products are available - the Level 1 Radiometric product (L1B1) and the Level 1 Georectified radiance product (L1B2).",
-            "graphic-preview-description": "AirMISR Campaign Imagery: AirMISR Red Band Browse Images from the LUNAR_LAKE_2001 Field Campaign, June 30, 2001",
-            "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the Lunar Lake 2001 Campaign",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_LUNAR_LAKE_2001_images.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_LUNAR_LAKE_2001_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FAIRMISR_LUNAR_LAKE_2001_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMISR",
-                    "description": "ASDC Data and Information for AirMISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for AirMISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/AIRMISR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/Mission/airMISR/",
-                    "description": "AirMISR project home page",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR project home page",
+                    "downloadURL": "https://misr.jpl.nasa.gov/Mission/airMISR/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000704-LARC_ASDC",
-                    "description": "Earthdata Search for AIRMISR_LUNAR_LAKE_2001_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for AIRMISR_LUNAR_LAKE_2001_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000704-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/read_software/read_airmisr.pro",
-                    "description": "Readme to open and read AIRMISR L1B2 GP (Georectified Radiance Product) HDF-EOS data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to open and read AIRMISR L1B2 GP (Georectified Radiance Product) HDF-EOS data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/read_software/read_airmisr.pro",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_lunar_lake_2001",
-                    "description": "Readme Information about the AirMISR Data During a Flight over Lunar Lake, Nevada on June 30, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "Readme Information about the AirMISR Data During a Flight over Lunar Lake, Nevada on June 30, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/readme_airmisr_lunar_lake_2001",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/quality_summaries/airmisr_lunar_lake_2001.pdf",
-                    "description": "Quality Summary: AirMISR LUNAR_LAKE_2001",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: AirMISR LUNAR_LAKE_2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/quality_summaries/airmisr_lunar_lake_2001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_LUNAR_LAKE_2001_1",
-                    "description": "DOI data set landing page for AIRMISR_LUNAR_LAKE_2001_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for AIRMISR_LUNAR_LAKE_2001_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_LUNAR_LAKE_2001_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_F01.pdf",
-                    "description": "AirMISR Data Products Specifications, December 21, 2000",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Data Products Specifications, December 21, 2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_F01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS.pdf",
-                    "description": "AirMISR Data Products Specifications, Rev. A, December 21,2000",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Data Products Specifications, Rev. A, December 21,2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_RevC.pdf",
-                    "description": "AirMISR Data Products Specifications, Rev. C, December 21,2000",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Data Products Specifications, Rev. C, December 21,2000",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/AirMISR_DPS_RevC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.tar",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
-                    "description": "ASDC Data and Information for MISR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for MISR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/MISR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/using_airmisr_data.pdf",
-                    "description": "ASDC Documents for Using AirMISR Data",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Documents for Using AirMISR Data",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/using_airmisr_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v50_RevS.pdf",
-                    "description": "Data Product Specification for MISR - Revision S, April 15, 2011   ",
                     "@type": "dcat:Distribution",
+                    "description": "Data Product Specification for MISR - Revision S, April 15, 2011   ",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/DPS_v50_RevS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/FieryTemperament",
-                    "description": "NASA Earth ObservatoryArticle: \"Fiery Temperament\" By Michon Scott, May 14, 2002",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth ObservatoryArticle: \"Fiery Temperament\" By Michon Scott, May 14, 2002",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/FieryTemperament",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.google.com/earth/",
-                    "description": "Google Earth",
                     "@type": "dcat:Distribution",
+                    "description": "Google Earth",
+                    "downloadURL": "https://www.google.com/earth/",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based map viewerf"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolMonterey.pdf",
-                    "description": "Journal of Geophysical Research Article: \"Aerosol properties derived from aircraft multiangle imagingover Monterey Bay\" by Ralph Kahn, Pranab Banerjee, Duncan McDonald, and John Martonchik, June 16, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "Journal of Geophysical Research Article: \"Aerosol properties derived from aircraft multiangle imagingover Monterey Bay\" by Ralph Kahn, Pranab Banerjee, Duncan McDonald, and John Martonchik, June 16, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolMonterey.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolRetrieval.pdf",
-                    "description": "Journal of Geophysical Research Article: \"Sensitivity of multiangle imaging to natural mixturesof aerosols over ocean\" by Ralph Kahn, Pranab Banerjee, and Duncan McDonald, August 27, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "Journal of Geophysical Research Article: \"Sensitivity of multiangle imaging to natural mixturesof aerosols over ocean\" by Ralph Kahn, Pranab Banerjee, and Duncan McDonald, August 27, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/readme/MultiangleAerosolRetrieval.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/tools-and-services",
-                    "description": "Links to tools available through the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Links to tools available through the ASDC",
+                    "downloadURL": "https://asdc.larc.nasa.gov/tools-and-services",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MISR",
-                    "description": "NASA Earthdata Forum - MISR Project Specific Forum",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Forum - MISR Project Specific Forum",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/app.php/tag/MISR",
+                    "mediaType": "text/html",
                     "title": "Access this dataset's users feedback page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/observing_concept.pdf",
-                    "description": "MISR Observing Concept Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Observing Concept Fact Sheet",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/observing_concept.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kml+xml",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
-                    "description": "MISR Paths Tool - Direct File Download (.kml)",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Paths Tool - Direct File Download (.kml)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/tools/misr_paths.kml",
+                    "mediaType": "application/vnd.google-earth.kml+xml",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
-                    "description": "MISR Peer-Reviewed Publications",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Peer-Reviewed Publications",
+                    "downloadURL": "https://misr.jpl.nasa.gov/publications/peerReviewed/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://misr.jpl.nasa.gov/",
-                    "description": "MISR project home page",
                     "@type": "dcat:Distribution",
+                    "description": "MISR project home page",
+                    "downloadURL": "https://misr.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2015.pdf",
-                    "description": "Overview of MISR Data at the ASDC, 2015",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of MISR Data at the ASDC, 2015",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/ASDC_MISR_Overview_2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
-                    "description": "MISR Science Data Product Guide - May 7, 2012",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Science Data Product Guide - May 7, 2012",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/MISR_Science_Data_Product_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_workshop.pdf",
-                    "description": "MISR Workshop Presentations, June 2002 - August 2010",
                     "@type": "dcat:Distribution",
+                    "description": "MISR Workshop Presentations, June 2002 - August 2010",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/misr_workshop.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/overview_misr.pdf",
-                    "description": "Multi-angle Imaging SpectroRadiometer (MISR) Overview Fact Sheet",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-angle Imaging SpectroRadiometer (MISR) Overview Fact Sheet",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/overview_misr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
-                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "Multi-angle Imaging SpectroRadiometer Project Handbook",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/guide/misr_ov2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
-                    "description": "NASA EOS ATB Documents: MISR",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: MISR",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/45",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/vnd.ms-powerpoint",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/obtaining_misr_data.ppt",
-                    "description": "Obtaining MISR Data and Information, Presented by Jeff Walter Atmospheric Science Data Center - April 17, 2009 - Direct File Download (.ppt)",
                     "@type": "dcat:Distribution",
+                    "description": "Obtaining MISR Data and Information, Presented by Jeff Walter Atmospheric Science Data Center - April 17, 2009 - Direct File Download (.ppt)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/obtaining_misr_data.ppt",
+                    "mediaType": "application/vnd.ms-powerpoint",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc/misr_loc.html",
-                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
                     "@type": "dcat:Distribution",
+                    "description": "Tool to identify MISR Paths/Blocks intersecting a specified lat/lon box",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/misr_loc/misr_loc.html",
+                    "mediaType": "text/html",
                     "title": "Use this dataset in a web based tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.fs.usda.gov/rmrs/groups/larse",
-                    "description": "USDA Overview of Laboratory for Applications of Remote Sensing in Ecology (LARSE)",
                     "@type": "dcat:Distribution",
+                    "description": "USDA Overview of Laboratory for Applications of Remote Sensing in Ecology (LARSE)",
+                    "downloadURL": "https://www.fs.usda.gov/rmrs/groups/larse",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.pro",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool IDL source code - Direct File Download (.pro)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool IDL source code - Direct File Download (.pro)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.sav",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool  IDL executable save file (use with the IDL Virtual Machine) - Direct File Download (.sav)",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool  IDL executable save file (use with the IDL Virtual Machine) - Direct File Download (.sav)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/coregister_L1B2_L2AS.sav",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/readme_L1B2_L2AS_coregistration_tool.txt",
-                    "description": "AirMISR L1B2/L2AS Coregistration Tool Readme",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR L1B2/L2AS Coregistration Tool Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/tools/readme_L1B2_L2AS_coregistration_tool.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Smoke over Athens\u00a0-\u00a0The effects of forest fires show up in a multi-satellite view of pollution.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1240/NASA_SOP_2009_Smoke_over_Athens.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Aerosols over Australia\u00a0-\u00a0Researchers explore the links between atmospheric aerosols, climate change, and ultraviolet rays.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1194/NASA_SOP_2008_Aerosols_over_Australia.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Cloudy with a chance of Drizzle\u00a0-\u00a0By analyzing data from the MISR instrument, scientists discover that a unique type of cloud formation is much more prevalent than was previously believed.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1257/NASA_SOP_2005_Cloudy_with_a_Chance_of_Drizzle.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
-                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earthdata Content Delivery Network (CDN) Article: Following the World Trade Center plume\u00a0-\u00a0Remote sensing helps track the drift of harmful pollutants following the World Trade Center collapse.",
+                    "downloadURL": "https://cdn.earthdata.nasa.gov/conduit/upload/1187/NASA_SOP_2007_Following_the_World_Trade_Center_plume.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/90764/looking-at-the-moon-to-better-see-earth",
-                    "description": "NASA Earth Observatory Article: Looking at the Moon to Better See Earth - Terra satellite performs manuver that allows all nine of MISR's camera to capture images of the moon.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Looking at the Moon to Better See Earth - Terra satellite performs manuver that allows all nine of MISR's camera to capture images of the moon.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/90764/looking-at-the-moon-to-better-see-earth",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://photojournal.jpl.nasa.gov/catalog/PIA21945",
-                    "description": "NASA JPL Photojournal: New Images of Irma's Towering Clouds - MISR passes over Irma over the Dominican Republic as a Category 5 hurricane.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Photojournal: New Images of Irma's Towering Clouds - MISR passes over Irma over the Dominican Republic as a Category 5 hurricane.",
+                    "downloadURL": "https://photojournal.jpl.nasa.gov/catalog/PIA21945",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Earthquake",
-                    "description": "NASA Earth Observatory Article: Squeezing Water from Rock\u00a0-\u00a0Survivors of the New Madrid earthquakes reported not only intense ground shaking and land movement, but also an unfamiliar phenomenon of water and sand spouting up through cracks in the Earth's surface.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Squeezing Water from Rock\u00a0-\u00a0Survivors of the New Madrid earthquakes reported not only intense ground shaking and land movement, but also an unfamiliar phenomenon of water and sand spouting up through cracks in the Earth's surface.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Earthquake",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/tracking",
-                    "description": "NASA Earth Observatory Article: Tracking Clouds\u00a0-\u00a0Tune in to the evening weather report on any given day, and you'll no doubt see satellite images of clouds.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Tracking Clouds\u00a0-\u00a0Tune in to the evening weather report on any given day, and you'll no doubt see satellite images of clouds.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/tracking",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
-                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA JPL Images: Tropical Storm Harvey over Texas - After making landfall as a Category 4 hurricane the day before, striking images are captured by MISR as the storm maintained a dangerous tropical storm status.",
+                    "downloadURL": "https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA21927",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.html",
-                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Terra Spacecraft Loss of Accurate Orbit Data Record",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/terra-maneuvers.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
-                    "description": "ASDC List of MISR Imagery and Articles",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of MISR Imagery and Articles",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/misr/imagery.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_LUNAR_LAKE_2001_images.html",
-                    "description": "AirMISR Campaign Imagery: AirMISR Red Band Browse Images from the LUNAR_LAKE_2001 Field Campaign, June 30, 2001",
                     "@type": "dcat:Distribution",
+                    "description": "AirMISR Campaign Imagery: AirMISR Red Band Browse Images from the LUNAR_LAKE_2001 Field Campaign, June 30, 2001",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_LUNAR_LAKE_2001_images.html",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMISR/AIRMISR_LUNAR_LAKE_2001/",
-                    "description": "ASDC Direct Data Download for AIRMISR_LUNAR_LAKE_2001_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for AIRMISR_LUNAR_LAKE_2001_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/AirMISR/AIRMISR_LUNAR_LAKE_2001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMISR/AIRMISR_LUNAR_LAKE_2001/contents.html",
-                    "description": "OPeNDAP data access for AIRMISR_LUNAR_LAKE_2001_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for AIRMISR_LUNAR_LAKE_2001_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/AirMISR/AIRMISR_LUNAR_LAKE_2001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "graphic-preview-description": "AirMISR Campaign Imagery: AirMISR Red Band Browse Images from the LUNAR_LAKE_2001 Field Campaign, June 30, 2001",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/documents/airmisr/airmisr_LUNAR_LAKE_2001_images.html",
+            "identifier": "C1000000704-LARC_ASDC",
+            "issued": "2004-03-24",
+            "keyword": [
+                "visible wavelengths",
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/AIRMISR_LUNAR_LAKE_2001_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-04-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>38.13 -116.32 38.13 -115.36 38.73 -115.36 38.73 -116.32 38.13 -116.32</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2001-06-30T00:00:00Z/2001-06-30T23:59:59.999Z",
             "theme": [
                 "AIRMISR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airborne Multi-angle Imaging SpectroRadiometer (AirMISR) Data from the Lunar Lake 2001 Campaign"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/25in-69gj",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "keyword": [
-                "library construction",
-                "spaceflight",
-                "nucleic acid sequencing",
-                "sequence analysis data transformation",
-                "sample processing",
-                "sample collection"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "GeneLab Outreach",
                 "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "nasa_genelab_GLDS-66_25in-69gj",
             "description": "The environmental samples were collected with the polyester wipes from eight different locations in the International Space Station (ISS) during two consecutive sampling sessions (three months apart) within the ISS Microbial Observatory Experiment. DNA extracted from each of the samples was used to create amplicon libraries based on customized panel of 500 antimicrobial resistance genes followed by next-generation sequencing. This is the first study of that shows the reservoir of antimicrobial genes in the ISS. The International Space Station (ISS) as a closed built environment has its own environmental microbiome which is shaped by microgravity radiation and limited human presence. The microbial diversity associated with ISS environmental surfaces was investigated during this study. Polyester wipes and contact slides were used for sampling of eight various surface locations on the ISS at different time periods. The samples were retrieved and analyzed immediately upon the return to the Earth (via Soyuz TMA-14M or Dragon capsule from SpaceX). After surface sample collection contact slides containing nutrient media for the growth of bacteria and fungi were incubated at 25 xcb x9aC. The polyester wipes were processed to measure microbial burden (R2A Blood Agar and Potato Dextrose Agar) and recover cultivable bacteria as well as fungi. Subsequently viable microbial burden was assessed using Adenosine Triphosphate (ATP) assay and quantitative polymerase chain reaction (PCR) methods after propidium monoazide (PMA) treatment. The 16S-tag and metagenome analyses were used to elucidate viable microbial diversity. The cultivable bacterial population yield from the polyester wipes was very high (5 to 7-logs) when compared with the contact slides (102 to 103 CFU/m2). The PMA-qPCR analysis showed considerable variation of viable bacterial population (105 to 109 16S rDNA gene copies/m2) among locations sampled. Unlike contact slides polyester wipes cover much larger sample surface (~1 m2) and produce much more reliable results of the microbial diversity of the ISS covering both cultivable and non-cultivable species. The cultivable total and viable microbial diversity was determined utilizing state-of-the art molecular techniques. The implementation of the PMA assay before DNA extraction allowed distinguishing viable microorganisms which is crucial for determining their role to the crew health the ISS maintenance and the general knowledge of the closed environmentally controlled built systems.",
-            "title": "Microbial Observatory (ISS-MO): Antimicrobial resistance genes",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-66",
-                    "description": "GeneLab Study Page",
                     "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-66",
+                    "mediaType": "text/html",
                     "title": "Microbial Observatory (ISS-MO): Antimicrobial resistance genes"
                 }
             ],
+            "identifier": "nasa_genelab_GLDS-66_25in-69gj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "library construction",
+                "spaceflight",
+                "nucleic acid sequencing",
+                "sequence analysis data transformation",
+                "sample processing",
+                "sample collection"
+            ],
+            "landingPage": "https://data.nasa.gov/d/25in-69gj",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microbial Observatory (ISS-MO): Antimicrobial resistance genes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-1-EXT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "mars",
-                "mars global surveyor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains archival raw, partially processed, and      ancillary/supporting radio science data acquired during the        Extended Mission (EXT) phase of the Mars Global Surveyor (MGS)     mission.  The radio observations were carried out using the MGS    spacecraft and Earth-based receiving stations of the NASA Deep     Space Network (DSN).  The observations were designed to test       the spacecraft radio system, the DSN ground system, and MGS        operations procedures; to be used in generating high-resolution    gravity field models of Mars; and for estimating density and       structure of the Mars atmosphere.  Of most interest are likely     to be the Orbit Data File and Radio Science Receiver files, in     the ODF and RSR directories, respectively, which provided the      raw input to gravity and atmospheric investigations.  The EXT      phase began on 1 February 2001.  Data were organized in            approximately chronological order and delivered on a set of        several hundred CD volumes at the rate of 2-3 CD's per week        or DVD volumes at the rate of about 2 per month.  Typical          volume of a one-day ODF was 300-400 kB.  Typical volume of an      RSR was 5-10 MB, and there could be 0-30 RSR's per day depending   on DSN schedules and observing geometry.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-1-ext-v1.0_25ji-yc6z",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars global surveyor"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-RSS-1-EXT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-rss-1-ext-v1.0_25ji-yc6z",
-            "description": "This data set contains archival raw, partially processed, and      ancillary/supporting radio science data acquired during the        Extended Mission (EXT) phase of the Mars Global Surveyor (MGS)     mission.  The radio observations were carried out using the MGS    spacecraft and Earth-based receiving stations of the NASA Deep     Space Network (DSN).  The observations were designed to test       the spacecraft radio system, the DSN ground system, and MGS        operations procedures; to be used in generating high-resolution    gravity field models of Mars; and for estimating density and       structure of the Mars atmosphere.  Of most interest are likely     to be the Orbit Data File and Radio Science Receiver files, in     the ODF and RSR directories, respectively, which provided the      raw input to gravity and atmospheric investigations.  The EXT      phase began on 1 February 2001.  Data were organized in            approximately chronological order and delivered on a set of        several hundred CD volumes at the rate of 2-3 CD's per week        or DVD volumes at the rate of about 2 per month.  Typical          volume of a one-day ODF was 300-400 kB.  Typical volume of an      RSR was 5-10 MB, and there could be 0-30 RSR's per day depending   on DSN schedules and observing geometry.",
-            "title": "MARS GLOBAL SURVEYOR RAW         \n                                      DATA SET - EXT V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MARS GLOBAL SURVEYOR RAW         \n                                      DATA SET - EXT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/8nva-pd74",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Voices from the Frontlines of Changing Bering Sea, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/8nva-pd74.",
-            "issued": "2019-01-01",
-            "temporal": "2019-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-31",
-            "keyword": [
-                "public health",
-                "earth science",
-                "biospheric indicators",
-                "weather/climate advisories",
-                "infrastructure",
-                "environmental advisories",
-                "sustainability",
-                "human dimensions",
-                "climate indicators"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NSIDC Services",
                 "hasEmail": "mailto:nsidc@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C2041711035-NSIDCV0",
             "description": "The Bering Sea is home to over 70 Indigenous communities of the I\u00f1upiat, Central Yup\u2019ik, Cup\u2019ik, St. Lawrence Island Yupik, Unangan, and Chukchi Peoples. In recent years, the Bering Sea has experienced unprecedented declines in sea ice, threatening community food security, infrastructure, and travel. In winters 2018 and 2019, sea ice coverage was by far the lowest observed in at least the last 160 years. Such loss of ice, together with increasing air temperatures and recent winter storm activity, has shifted much focus to the region with renewed questions regarding how local communities and ecosystems are affected. In 2019, scientists from the Study of Environmental Arctic Change (SEARCH) partnered with the Bering Sea Elders Group (BSEG) to create opportunities for Elders to communicate their experiences and knowledge regarding rapid environmental change across their region. In September 2019, ten Elders from eight communities came together for a two-day round-table gathering in Nome, Alaska to share their perspectives, observations, and stories about what sea ice loss means to their villages, the resources they depend on, and their collective future as Arctic Indigenous Peoples.",
-            "title": "Voices from the Frontlines of Changing Bering Sea, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F8nva-pd74",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2F8nva-pd74",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eloka-arctic.org/bering-sea-voices/voices-frontlines-changing-bering-sea",
-                    "description": "Product website where you can access the data.",
                     "@type": "dcat:Distribution",
+                    "description": "Product website where you can access the data.",
+                    "downloadURL": "https://eloka-arctic.org/bering-sea-voices/voices-frontlines-changing-bering-sea",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/8nva-pd74",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/8nva-pd74",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/8nva-pd74",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/8nva-pd74",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
-            "theme": [
-                "geospatial"
+            "identifier": "C2041711035-NSIDCV0",
+            "issued": "2019-01-01",
+            "keyword": [
+                "public health",
+                "earth science",
+                "biospheric indicators",
+                "weather/climate advisories",
+                "infrastructure",
+                "environmental advisories",
+                "sustainability",
+                "human dimensions",
+                "climate indicators"
             ],
+            "landingPage": "https://doi.org/10.7265/8nva-pd74",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2020-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
+            "temporal": "2019-01-01T00:00:00Z/2020-12-31T23:59:59.999Z",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Voices from the Frontlines of Changing Bering Sea, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331331173-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "oceans",
-                "ocean optics",
-                "ocean chemistry",
-                "ngda",
-                "national geospatial data asset",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sdps@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C2331331173-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Global Binned Chlorophyll (CHL) - NRT Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
-                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Algorithm Description Documentation",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/atbd/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/",
-                    "description": "NASA Ocean Color Web - Processing History",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Processing History",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/reprocessing/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/citations/",
-                    "description": "NASA Ocean Color Web - Data Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Citation Policy",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/citations/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/CHL/2022",
-                    "description": "MODIS-Aqua L3B Chlorophyll (CHL) - NRT Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3B Chlorophyll (CHL) - NRT Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3B/CHL/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C2331331173-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "oceans",
+                "ocean optics",
+                "ocean chemistry",
+                "ngda",
+                "national geospatial data asset",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331331173-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua MODIS Global Binned Chlorophyll (CHL) - NRT Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-UBV-MEAN-VALUES-V1.2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "asteroid",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set is a compilation of mean U-B and B-V color indices of asteroids, collected from the published literature and from the unpublished Lowell Observatory UBV Asteroid Survey.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-ubv-mean-values-v1.2_25pe-ch5v",
+            "issued": "2021-05-21",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-5-DDR-UBV-MEAN-VALUES-V1.2",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-5-ddr-ubv-mean-values-v1.2_25pe-ch5v",
-            "description": "This data set is a compilation of mean U-B and B-V color indices of asteroids, collected from the published literature and from the unpublished Lowell Observatory UBV Asteroid Survey.",
-            "title": "UBV MEAN ASTEROID COLORS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "UBV MEAN ASTEROID COLORS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SA-ISSNA-5-TETHYSSHAPE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "s3 tethys",
-                "cassini-huygens"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The shape model of Tethys derived by Robert Gaskell from Cassini Imaging Science Subsystem narrow and wide angle camera (ISSNA and ISSWA) images. The model is provided in the implicitly connected quadrilateral (ICQ) format. This version of the model was prepared on July 25, 2012. Vertex-facet versions of the models are also provided.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sa-issna-5-tethysshape-v1.0_25pn-hdsr",
+            "issued": "2018-06-26",
+            "keyword": [
+                "s3 tethys",
+                "cassini-huygens"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SA-ISSNA-5-TETHYSSHAPE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-sa-issna-5-tethysshape-v1.0_25pn-hdsr",
-            "description": "The shape model of Tethys derived by Robert Gaskell from Cassini Imaging Science Subsystem narrow and wide angle camera (ISSNA and ISSWA) images. The model is provided in the implicitly connected quadrilateral (ICQ) format. This version of the model was prepared on July 25, 2012. Vertex-facet versions of the models are also provided.",
-            "title": "GASKELL TETHYS SHAPE MODEL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GASKELL TETHYS SHAPE MODEL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/OZZPDWENP2NC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "UW-Madison Space Science and Engineering Center: Hank Revercomb; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow. 2020-12-01. SNPPCrISL1BNSR. Version 3. Suomi NPP CrIS Level 1B Normal Spectral Resolution V3. Greenbelt, MD. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/OZZPDWENP2NC. https://disc.gsfc.nasa.gov/datacollection/SNPPCrISL1BNSR_3.html. Digital Science Data.",
-            "issued": "2012-04-19",
-            "temporal": "2012-01-20T12:42:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "infrared wavelengths"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1952167492-GES_DISC",
-            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Normal Spectral Resolution (NSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Suomi National Polar-orbiting Partnership Project (SNPP). In December 2014, the CrIS instrument on the SNPP satellite doubled the spectral resolution of shortwave infrared data being transmitted to the ground.  In November 2015, additional points were included at the ends of the longwave and shortwave interferograms to improve the quality of the calibration.  Prior to November 2, 2015 the data are only available in Normal Spectral Resolution, after November 2, 2015 at 16:06 UTC, the data are available in both NSR and Full Spectral Resolution (FSR). \n\nThe NSR files have 1,317 channels: 163 shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 437 midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nCrIS is designed to be used with the ATMS (Advanced Technology Microwave Sounder) instrument. Processing the data from both of these instruments together is referred to as CrIMSS (Cross-Track Infrared and Microwave Sounder Suite).\n\n\nIf you were redirected to this page from a DOI from\nan older version, please note this is the current\nversion of the product. Please contact the GES DISC\nuser support if you need information about previous\ndata collections.",
-            "release-place": "Greenbelt, MD",
-            "series-name": "SNPPCrISL1BNSR",
             "creator": "UW-Madison Space Science and Engineering Center: Hank Revercomb; UMBC Atmospheric Spectroscopy Laboratory: Larrabee Strow",
-            "title": "Suomi NPP CrIS Level 1B Normal Spectral Resolution V3 (SNPPCrISL1BNSR) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNPPCrISL1BNSR_v3.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Cross-track Infrared Sounder (CrIS) Level 1B Normal Spectral Resolution (NSR) data files contain radiance measurements along with ancillary spacecraft, instrument, and geolocation data of the CrIS instrument on the Suomi National Polar-orbiting Partnership Project (SNPP). In December 2014, the CrIS instrument on the SNPP satellite doubled the spectral resolution of shortwave infrared data being transmitted to the ground.  In November 2015, additional points were included at the ends of the longwave and shortwave interferograms to improve the quality of the calibration.  Prior to November 2, 2015 the data are only available in Normal Spectral Resolution, after November 2, 2015 at 16:06 UTC, the data are available in both NSR and Full Spectral Resolution (FSR). \n\nThe NSR files have 1,317 channels: 163 shortwave channels from 3.9 to 4.7 microns (2555 to 2150 cm-1), 437 midwave channels from 5.7 to 8.05 microns (1752.5 to 1242.5 cm-1), and 717 longwave channels from 9.1 to 15.41 microns (1096.25 to 648.75 cm-1). Each CrIS field-of-regard (FOR) contains 9 field-of-views (FOVs) arranged in a 3X3 array. The Level 1B files contain 30 FORs in the cross track direction and 45 in the along track direction. Data products are constructed on six minute boundaries.\n\nCrIS is designed to be used with the ATMS (Advanced Technology Microwave Sounder) instrument. Processing the data from both of these instruments together is referred to as CrIMSS (Cross-Track Infrared and Microwave Sounder Suite).\n\n\nIf you were redirected to this page from a DOI from\nan older version, please note this is the current\nversion of the product. Please contact the GES DISC\nuser support if you need information about previous\ndata collections.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOZZPDWENP2NC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOZZPDWENP2NC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -9413,712 +9391,748 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNPPCrISL1BNSR_3.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNPPCrISL1BNSR_3.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level1/SNPPCrISL1BNSR.3/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level1/SNPPCrISL1BNSR.3/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNPPCrISL1BNSR+003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNPPCrISL1BNSR+003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level1/SNPPCrISL1BNSR.3/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level1/SNPPCrISL1BNSR.3/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/D0001-M01-S01-002_JPSS_ATBD_CrIS-SDR_C.pdf",
-                    "description": "Joint Polar Satellite System (JPSS) Cross Track Infrared Sounder (CrIS) Sensor Data Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
                     "@type": "dcat:Distribution",
+                    "description": "Joint Polar Satellite System (JPSS) Cross Track Infrared Sounder (CrIS) Sensor Data Records (SDR) Algorithm Theoretical Basis Document (ATBD).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/SNPP_Sounder/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/D0001-M01-S01-002_JPSS_ATBD_CrIS-SDR_C.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_L1B_DeltaATBD_V3.0.pdf",
-                    "description": "NASA SNPP Cross Track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD)",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SNPP Cross Track Infrared Sounder (CrIS) Level 1B Delta Algorithm Theoretical Basis Document (ATBD)",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/SNPP/CrIS_L1B_DeltaATBD_V3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Users_Guide_v3RevC.pdf",
-                    "description": "NASA Cross Track Infrared Sounder (CrIS) Level 1B Product Users\u2019 Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Cross Track Infrared Sounder (CrIS) Level 1B Product Users\u2019 Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Users_Guide_v3RevC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Quality_Flags_V3.pdf",
-                    "description": "NASA SNPP Cross Track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
                     "@type": "dcat:Distribution",
+                    "description": "NASA SNPP Cross Track Infrared Sounder (CrIS) Level 1B Quality Flags Description Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Quality_Flags_V3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Test_Report_v3RevA.pdf",
-                    "description": "CrIS L1B Version 3 Product Test Report",
                     "@type": "dcat:Distribution",
+                    "description": "CrIS L1B Version 3 Product Test Report",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Product_Test_Report_v3RevA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Radiometric_Uncertainty_v3.pdf",
-                    "description": "CrIS L1B v3 Radiometric Uncertainty document",
                     "@type": "dcat:Distribution",
+                    "description": "CrIS L1B v3 Radiometric Uncertainty document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/NASA_CrIS_L1B_Radiometric_Uncertainty_v3.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNPPCrISL1BNSR_v3.png",
+            "identifier": "C1952167492-GES_DISC",
+            "issued": "2012-04-19",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/OZZPDWENP2NC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD",
+            "series-name": "SNPPCrISL1BNSR",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-20T12:42:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Suomi NPP CrIS Level 1B Normal Spectral Resolution V3 (SNPPCrISL1BNSR) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/405",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Atkinson, G.B., and B. Funk. 1998. BOREAS/AES Campbell Scientific 15-minute Surface Meteorological Data: 1995. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/405",
-            "issued": "2023-11-22",
-            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "snow/ice",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "atmosphere",
-                "earth science",
-                "precipitation",
-                "terrestrial hydrosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2808090046-ORNL_CLOUD",
             "description": "Contains data from 1995 from the Atmospheric Environment Service Campbell Scientific autostations collecting continuous fifteen minute data for BOREAS.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS/AES Campbell Scientific 15-minute Surface Meteorological Data: 1995",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F405",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F405",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/ams_cs95/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/STAFF/ams_cs95/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AES_CS.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/AES_CS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/405",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/405",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs95/comp/AES_CS.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs95/comp/AES_CS.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs95/comp/AES_CS.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs95/comp/AES_CS.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs95/comp/AES_CS.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs95/comp/AES_CS.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs95/comp/ams_cs95.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/STAFF/ams_cs95/comp/ams_cs95.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
+            "identifier": "C2808090046-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "snow/ice",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "atmosphere",
+                "earth science",
+                "precipitation",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/405",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-108.52 50.95 -94.7 58.18",
+            "temporal": "1995-01-01T00:00:00Z/1995-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS/AES Campbell Scientific 15-minute Surface Meteorological Data: 1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-SOLAR-OPS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "mars",
-                "mars exploration rover"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-solar-ops-v1.0_25tx-63n9",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-PANCAM-5-SOLAR-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-pancam-5-solar-ops-v1.0_25tx-63n9",
-            "description": "not applicable",
-            "title": "MER 1 MARS PANORAMIC CAMERA SOLAR RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "MER 1 MARS PANORAMIC CAMERA SOLAR RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-HAD-3-ENTRY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "jupiter",
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set is most accurately described in [VONZAHN&HUNTEN1996]:",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-had-3-entry-v1.0_25ub-ym7h",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GP-J-HAD-3-ENTRY-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gp-j-had-3-entry-v1.0_25ub-ym7h",
-            "description": "This data set is most accurately described in [VONZAHN&HUNTEN1996]:",
-            "title": "GALILEO PROBE HELIUM ABUNDANCE DETECTOR DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "GALILEO PROBE HELIUM ABUNDANCE DETECTOR DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3YMDE",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3YMDE. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "salinity/density"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "User Services",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491757153-POCLOUD",
-            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and\nseasonal time scales. This particular data set is the Monthly, Descending rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 sea surface salinity (SSS) rain-flagged standard mapped image data contains gridded 1 degree spatial resolution SSS averaged over daily, 7 day, monthly, and\nseasonal time scales. This particular data set is the Monthly, Descending rain-flagged sea surface salinity product for version 5.0 of the Aquarius data set. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YMDE",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3YMDE",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
-                    "description": "Aquarius Data User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Aquarius Data User's Guide",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/aquarius",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
-                    "description": "Information on observatory maneuvers, anomalies and other events",
                     "@type": "dcat:Distribution",
+                    "description": "Information on observatory maneuvers, anomalies and other events",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/sdpscgi/public/aquarius_report.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aquarius.nasa.gov/",
-                    "description": "NASA Aquarius/SAC-D mission website",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Aquarius/SAC-D mission website",
+                    "downloadURL": "https://aquarius.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/CitingPODAAC",
-                    "description": "Data Use and Citation Policy",
                     "@type": "dcat:Distribution",
+                    "description": "Data Use and Citation Policy",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/CitingPODAAC",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data citation policy"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757153-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757153-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757153-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757153-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-010-UG-0008_AquariusUserGuide_DatasetV5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0006_ProposalForFlags&Masks_DatasetVersion3.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0006_ProposalForFlags&Masks_DatasetVersion3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0016_AquariusSalinityDataValidationAnalysis_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0016_AquariusSalinityDataValidationAnalysis_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_Addendum5_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_Addendum5_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_EndofMission_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusATBD_Level2_EndofMission_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusScatterometerCalibrationReview.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_AquariusScatterometerCalibrationReview.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission_Supplements.zip",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_ATBD-EndOfMission_Supplements.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_AntennaPatternCoefficientUpdates_DatasetVersion3.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_AntennaPatternCoefficientUpdates_DatasetVersion3.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_L2toL3ATBD_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Aquarius_L2toL3ATBD_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Performance_Degradation_and_QC_Flagging_of_Aquarius_L2_Salinity_Retrievals_V4.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0017_Performance_Degradation_and_QC_Flagging_of_Aquarius_L2_Salinity_Retrievals_V4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_AquariusLevel2specification_DatasetVersion5.0.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_AquariusLevel2specification_DatasetVersion5.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_Ocean_Level-3_Standard_Mapped_Image_Products.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0018_Ocean_Level-3_Standard_Mapped_Image_Products.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0028_V5_AVDS_Tech_Memo.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0028_V5_AVDS_Tech_Memo.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0029_Aquarius_counts_to_TA.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0029_Aquarius_counts_to_TA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0030_Full_Range_Cal_27Feb18.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-014-PS-0030_Full_Range_Cal_27Feb18.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-017-AquariusMissionSummary.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AQ-017-AquariusMissionSummary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AquariusATBDdocuments_10.5067-DOCUM-AQR04.zip",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/AquariusATBDdocuments_10.5067-DOCUM-AQR04.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_RFI_products_UserGuide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_V5.0-V4.0_SummaryOfChanges.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/Aquarius_V5.0-V4.0_SummaryOfChanges.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/EDinnat_etal_Paper_SkyTBMap_Lband.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
-                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD, Validation Analysis, Product Specifications, etc",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/aquarius/open/docs/v5/UserGuideAquariusCelestialSkyMicrowaveEmissionMapProduct.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_SSS-RainFlagged_SMID_MONTHLY_V5.jpg",
+            "identifier": "C2491757153-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "salinity/density"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3YMDE",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
+            "series-name": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Rain-flagged Sea Surface Salinity Standard Mapped Image Descending Monthly Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/1M7605BUVA9U",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 QuikSCAT/SeaWinds Backscatter Data, Oklahoma, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/1M7605BUVA9U.",
-            "issued": "2003-05-01",
-            "temporal": "2003-05-01T00:00:00Z/2003-08-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-08-31",
-            "keyword": [
-                "radar",
-                "microwave",
-                "spectral/engineering",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Long",
                 "hasEmail": "mailto:long@et.byu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386205629-NSIDCV0",
             "description": "This data set includes data collected over the Soil Moisture Experiment 2003 (SMEX03) areas of Alabama, Georgia, and Oklahoma, USA.",
-            "title": "SMEX03 QuikSCAT/SeaWinds Backscatter Data, Oklahoma, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1M7605BUVA9U",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F1M7605BUVA9U",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/satellite/QUIKSCAT/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/satellite/QUIKSCAT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/satellite/QUIKSCAT/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/satellite/QUIKSCAT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/satellite/QUIKSCAT/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/satellite/QUIKSCAT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/satellite/QUIKSCAT/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/satellite/QUIKSCAT/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1M7605BUVA9U",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/1M7605BUVA9U",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/1M7605BUVA9U",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/1M7605BUVA9U",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205629-NSIDCV0",
+            "issued": "2003-05-01",
+            "keyword": [
+                "radar",
+                "microwave",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/1M7605BUVA9U",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-103.0 30.0 -93.0 40.0",
+            "temporal": "2003-05-01T00:00:00Z/2003-08-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 QuikSCAT/SeaWinds Backscatter Data, Oklahoma, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0797-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "international rosetta mission",
-                "67p/churyumov-gerasimenko 1 (1969 r1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-21T09:28:25.000 to 2015-05-21T17:30:06.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0797-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0797-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0797-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-21T09:28:25.000 to 2015-05-21T17:30:06.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0797 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0797 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUM-IONWINDFIT-96S-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "saturn",
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-sum-ionwindfit-96s-v1.0_25wc-vuja",
+            "issued": "2021-05-21",
+            "keyword": [
+                "saturn",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-S-PLS-5-SUM-IONWINDFIT-96S-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-s-pls-5-sum-ionwindfit-96s-v1.0_25wc-vuja",
-            "description": "not applicable",
-            "title": "VG1 SAT PLS DERIVED ION SOLAR WIND 96SEC V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VG1 SAT PLS DERIVED ION SOLAR WIND 96SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566433-USGS_LTA.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "USGS EROS. 1993-01-01. North American Landscape Characterization. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, U.S. Geological Survey. Remote Sensing Image.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "EROS CENTER",
+                "hasEmail": "mailto:lta@usgs.gov"
+            },
+            "creator": "USGS EROS",
+            "data-presentation-form": "Remote Sensing Image",
+            "description": "The North American Landscape Characterization (NALC) project is a  component of the Landsat Pathfinder Program, which is part of a larger  Pathfinder Program initiated by the National Aeronautics and Space Administration (NASA) in 1989.  The NALC project is a cooperative effort between NASA, the U.S.  Environmental Protection Agency, and the U.S. Geological Survey to make Landsat data available to the  widest possible user community for scientific research and for the general public interest.  The objectives of the NALC project are to develop standardized remotely sensed data sets and analysis methods in support of investigations of changes in land cover, to  develop inventories of terrestrial carbon stocks, to assess carbon cycling dynamics, and to map terrestrial sources of greenhouse gas (CO, CO2, CH4, and N2) emissions. The NALC data set is comprised of hundreds of triplicates (i.e., multispectral scanner (MSS) data acquired in the years 1973, 1986, and 1991 plus or minus 1 year, thus, the name triplicate).  The NALC triplicates also include digital elevation model data.  The specific temporal windows vary for geographical regions based on the seasonal characteristics of the vegetation cover.  In accordance with the Landsat  Pathfinder Program concept, the Pathfinder basic data sets are to be comprised of data which have had systematic radiometric and systematic geometric corrections applied to them.  The NALC triplicates, however, are precision corrected for geocoding purposes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\n         EarthExplorer is a complete search and order tool for aerial photos, elevation data and satellite products distributed by the USGS.\n      ",
+                    "downloadURL": "http://earthexplorer.usgs.gov",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1220566433-USGS_LTA",
             "issued": "1972-07-23",
-            "temporal": "1972-07-23T00:00:00Z/1992-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1992-12-31",
             "keyword": [
                 "visible wavelengths",
                 "land use/land cover",
@@ -10128,125 +10142,122 @@
                 "earth science",
                 "topography"
             ],
-            "data-presentation-form": "Remote Sensing Image",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "EROS CENTER",
-                "hasEmail": "mailto:lta@usgs.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1220566433-USGS_LTA.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1992-12-31",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DOI/USGS/EROS"
             },
-            "identifier": "C1220566433-USGS_LTA",
-            "description": "The North American Landscape Characterization (NALC) project is a  component of the Landsat Pathfinder Program, which is part of a larger  Pathfinder Program initiated by the National Aeronautics and Space Administration (NASA) in 1989.  The NALC project is a cooperative effort between NASA, the U.S.  Environmental Protection Agency, and the U.S. Geological Survey to make Landsat data available to the  widest possible user community for scientific research and for the general public interest.  The objectives of the NALC project are to develop standardized remotely sensed data sets and analysis methods in support of investigations of changes in land cover, to  develop inventories of terrestrial carbon stocks, to assess carbon cycling dynamics, and to map terrestrial sources of greenhouse gas (CO, CO2, CH4, and N2) emissions. The NALC data set is comprised of hundreds of triplicates (i.e., multispectral scanner (MSS) data acquired in the years 1973, 1986, and 1991 plus or minus 1 year, thus, the name triplicate).  The NALC triplicates also include digital elevation model data.  The specific temporal windows vary for geographical regions based on the seasonal characteristics of the vegetation cover.  In accordance with the Landsat  Pathfinder Program concept, the Pathfinder basic data sets are to be comprised of data which have had systematic radiometric and systematic geometric corrections applied to them.  The NALC triplicates, however, are precision corrected for geocoding purposes.",
             "release-place": "Sioux Falls, South Dakota, USA",
-            "creator": "USGS EROS",
-            "title": "North American Landscape Characterization",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://earthexplorer.usgs.gov",
-                    "description": "\n         EarthExplorer is a complete search and order tool for aerial photos, elevation data and satellite products distributed by the USGS.\n      ",
-                    "@type": "dcat:Distribution",
-                    "title": "Download this dataset"
-                }
-            ],
             "spatial": "-175.0 5.0 -60.0 72.0",
+            "temporal": "1972-07-23T00:00:00Z/1992-12-31T23:59:59.999Z",
             "theme": [
                 "ELTA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "North American Landscape Characterization"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-RANGE-OPS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "mars exploration rover",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-range-ops-v1.0_269y-brb9",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-NAVCAM-5-RANGE-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-navcam-5-range-ops-v1.0_269y-brb9",
-            "description": "not applicable",
-            "title": "MER 1 MARS NAVIGATION CAMERA RANGE RDR OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS NAVIGATION CAMERA RANGE RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-POS-4-48.0SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "voyager",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes Voyager 1 Jupiter encounter position data that have been generated at a 48.0 second sample rate using the NAIF SPICE kernals. The data set is composed of 4 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) r - this column contains the radial distance from Jupiter in Rj = 71398 km, 3) longitude - this column contains the east longitude of the spacecraft in degrees, 4) latitude - this column contains the latitude of the spacecraft in degrees. Position data is given in Minus System III coordinates.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pos-4-48.0sec_26c6-kmpc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-POS-4-48.0SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-pos-4-48.0sec_26c6-kmpc",
-            "description": "This data set includes Voyager 1 Jupiter encounter position data that have been generated at a 48.0 second sample rate using the NAIF SPICE kernals. The data set is composed of 4 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) r - this column contains the radial distance from Jupiter in Rj = 71398 km, 3) longitude - this column contains the east longitude of the spacecraft in degrees, 4) latitude - this column contains the latitude of the spacecraft in degrees. Position data is given in Minus System III coordinates.",
-            "title": "VOYAGER 1 JUPITER POSITION RESAMPLED DATA 48.0 SECONDS",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "VOYAGER 1 JUPITER POSITION RESAMPLED DATA 48.0 SECONDS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/26e8-p68t",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Robert O. Shelton",
+                "hasEmail": "mailto:Robert.o.Shelton@nasa.gov"
+            },
+            "description": "Earth+ makes NASA satellite photos and data accessible to blind students.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://prime.jsc.nasa.gov/earthplus/Rita/RitaCoordinates.doc",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "NASA-0000033__7",
             "issued": "2018-06-25",
-            "temporal": "2004-01-01/2005-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "education outreach",
                 "radiometry",
@@ -10256,203 +10267,164 @@
                 "climatology",
                 "atmospheric science data center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Robert O. Shelton",
-                "hasEmail": "mailto:Robert.o.Shelton@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/26e8-p68t",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000033__7",
-            "description": "Earth+ makes NASA satellite photos and data accessible to blind students.",
-            "title": "Earth+",
-            "programCode": [
-                "026:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://prime.jsc.nasa.gov/earthplus/Rita/RitaCoordinates.doc",
-                    "mediaType": "application/msword"
-                }
-            ],
             "spatial": "Earth",
-            "accrualPeriodicity": "irregular"
+            "temporal": "2004-01-01/2005-01-01",
+            "title": "Earth+"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1948",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Griffin, K., S.C. Schmiege, S.G. Bruner, N. Boelman, L. Vierling, J. Eitel, and Z.M. Griffin. 2022. Spruce Leaf, Tree Traits, and Respiration at Range Extremes, AK and NY, USA, 2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1948",
-            "issued": "2022-10-12",
-            "temporal": "2018-06-06T00:00:00Z/2018-06-23T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "ecosystems",
-                "ecological dynamics",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:uso@daac.ornl.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "ORNL_DAAC"
-            },
-            "identifier": "C2515313617-ORNL_CLOUD",
             "description": "This dataset provides in situ measurements of needle-level gas-exchange and leaf traits from Picea glauca (white spruce) from a field site located in the northern latitudinal forest-tundra ecotone (FTE) near the Dalton Highway in northern Alaska, and from one study site located in Black Rock Forest, New York, USA. Measurements were collected with an open flow portable photosynthesis system (Li6400XT) and custom-built temperature-controlled cuvette. Respiration as a function of leaf temperature was measured continuously as the needle temperature was ramped from approximately 5 to 65 degrees C, at a constant rate of 1 degree C per minute. Additional data include tree diameter at breast height (dbh), leaf area, photosynthetic rate, intercellular C02, conductance to H20, tree height, and data from raw temperature curves. Results are reported on both a leaf area and leaf mass basis. The data are for the period 2018-06-06 to 2018-06-23 and are provided in comma-separated (CSV) format.",
-            "graphic-preview-description": "Species distribution for white spruce, Picea glauca. The southern range limit site, Black Rock Forest, Cornwall, NY, is marked with the red star. The arctic treeline site in northern Alaska is marked with a yellow star. Map from USGS from Thompson et al. (1999), in Griffin et al. (2022).",
-            "title": "Spruce Leaf, Tree Traits, and Respiration at Range Extremes, AK and NY, USA, 2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/ArcticTreeLine_Spruce_CO2_WV_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1948",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1948",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/ArcticTreeLine_Spruce_CO2_WV/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/ArcticTreeLine_Spruce_CO2_WV/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ArcticTreeLine_Spruce_CO2_WV.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/ArcticTreeLine_Spruce_CO2_WV.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1948",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1948",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
```

