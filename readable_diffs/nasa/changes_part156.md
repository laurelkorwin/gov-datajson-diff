# Change History for nasa.json (Part 156)

### Changes from 31606f9 to dd2190f (Part 145/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67p-m33-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 3 mission phase, covering the period  from 2016-08-09T23:25:00.000 to 2016-09-02T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP033 RDR-INFLDSTR V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP033 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CR2-V1.0",
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
-                "calibration",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR2 (Cruise 2) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cr2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CR2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cr2-v1.0",
-            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the CR2 (Cruise 2) phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL\n                           CONSERT 2 CR2 V1.0",
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
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL\n                           CONSERT 2 CR2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://pds.jpl.nasa.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "CIPS, HRD, INMS, ISS, MAG, MIMI, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120703.shtml",
+                    "mediaType": "application/html"
+                }
             ],
+            "identifier": "NASA-505",
+            "issued": "2018-06-25",
             "keyword": [
                 "inms",
                 "cips",
@@ -1525362,240 +1525371,245 @@
                 "spice",
                 "uvis"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-505",
-            "description": "CIPS, HRD, INMS, ISS, MAG, MIMI, RADAR, RPWS, RSS, SPICE, UVIS, VIMS",
-            "title": "PDS Cassini Data Release 30",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-20120703.shtml",
-                    "mediaType": "application/html"
-                }
+            "references": [
+                "https://pds.jpl.nasa.gov/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PDS Cassini Data Release 30"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0223-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-19T19:00:25.000 to 2014-08-20T01:37:20.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0223-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0223-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0223-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-19T19:00:25.000 to 2014-08-20T01:37:20.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0223 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0223 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO3ANCQA.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Joshua Fisher. 2019-06-20. ECO3ANCQA.001. ECOSTRESS L3/L4 Ancillary data Quality Assurance (QA) flags L3 Global 70 m V001. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC. https://doi.org/10.5067/ECOSTRESS/ECO3ANCQA.001. https://doi.org/10.5067/ECOSTRESS/ECO3ANCQA.001. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2018-07-15",
-            "temporal": "2018-07-15T00:00:00Z/2023-03-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-25",
-            "keyword": [
-                "clouds",
-                "surface radiative properties",
-                "surface thermal properties",
-                "land use/land cover",
-                "land surface",
-                "aerosols",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1534730053-LPDAAC_ECS",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data over the conterminous United States (CONUS) as well as key biomes and agricultural zones around the world and selected FLUXNET (http://fluxnet.fluxdata.org/about/) validation sites. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO3ANCQA Version 1 is a Level 3 (L3) product that provides Quality Assessment (QA) fields for all ancillary data used in L3 and Level 4 (L4) products generated by Jet Propulsion Laboratory (JPL). No quality flags are generated for the L3 or L4 products. Instead, the quality flags of the source data products are resampled by nearest neighbor onto the geolocation of the ECOSTRESS scene. A quality flag array for each input dataset, when available, is collected into the combined QA product.\r\n\r\nThe ECO3ANCQA Version 1 data product contains layers of quality flags for ECOSTRESS cloud mask, Landsat 8, land cover type, albedo, MODIS Terra aerosol, MODIS Terra Cloud 1 km, MODIS Terra Cloud 5 km, MODIS Terra atmospheric profile, vegetation indices, MODIS Terra gross primary productivity, and MODIS water mask.\r\n\r\nData acquisition gaps: ECOSTRESS was launched on June 29, 2018 and moved to autonomous science operations on August 20, 2018 following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity).",
-            "series-name": "ECO3ANCQA.001",
             "creator": "Simon Hook, Joshua Fisher",
-            "title": "ECOSTRESS L3/L4 Ancillary data Quality Assurance (QA) flags L3 Global 70m V001",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data over the conterminous United States (CONUS) as well as key biomes and agricultural zones around the world and selected FLUXNET (http://fluxnet.fluxdata.org/about/) validation sites. A map of the acquisition coverage can be found on the ECOSTRESS website (https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO3ANCQA Version 1 is a Level 3 (L3) product that provides Quality Assessment (QA) fields for all ancillary data used in L3 and Level 4 (L4) products generated by Jet Propulsion Laboratory (JPL). No quality flags are generated for the L3 or L4 products. Instead, the quality flags of the source data products are resampled by nearest neighbor onto the geolocation of the ECOSTRESS scene. A quality flag array for each input dataset, when available, is collected into the combined QA product.\r\n\r\nThe ECO3ANCQA Version 1 data product contains layers of quality flags for ECOSTRESS cloud mask, Landsat 8, land cover type, albedo, MODIS Terra aerosol, MODIS Terra Cloud 1 km, MODIS Terra Cloud 5 km, MODIS Terra atmospheric profile, vegetation indices, MODIS Terra gross primary productivity, and MODIS water mask.\r\n\r\nData acquisition gaps: ECOSTRESS was launched on June 29, 2018 and moved to autonomous science operations on August 20, 2018 following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO3ANCQA.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO3ANCQA.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534730053-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534730053-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO3ANCQA.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO3ANCQA.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ANCQA.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ANCQA.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/424/ECO3ETPTJPL_User_Guide_V1.pdf",
-                    "description": "The technical information in the ECO3ETPTJPL User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the ECO3ETPTJPL User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/424/ECO3ETPTJPL_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/335/ECO3ETPTJPL_ATBD_V1.pdf",
-                    "description": "The ECO3ETPTJPL ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ECO3ETPTJPL ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/335/ECO3ETPTJPL_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ANCQA.001",
-                    "description": "Digital Object Identifier",
                     "@type": "dcat:Distribution",
+                    "description": "Digital Object Identifier",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO3ANCQA.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/425/ECO4ESIPTJPL_User_Guide_V1.pdf",
-                    "description": "The technical information in the ECO4ESIPTJPL User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the ECO4ESIPTJPL User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/425/ECO4ESIPTJPL_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/342/ECO4ESIPTJPL_ATBD_V1.pdf",
-                    "description": "The ECO4ESIPTJPL ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ECO4ESIPTJPL ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/342/ECO4ESIPTJPL_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/381/ECO3ETPTJPL_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECO3ETPTJPL product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECO3ETPTJPL product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/381/ECO3ETPTJPL_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/382/ECO4ESIPTJPL_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECO4ESIPTJPL product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECO4ESIPTJPL product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/382/ECO4ESIPTJPL_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1573/Quick_Guide_for_Accessing_ECOSTRESS_Swath_Data_in_NASA_Earthdata_Search.pdf",
-                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1573/Quick_Guide_for_Accessing_ECOSTRESS_Swath_Data_in_NASA_Earthdata_Search.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthexplorer.usgs.gov/",
-                    "description": "USGS EarthExplorer provides users the ability to query, search, and dowload products available from the LP DAAC.",
                     "@type": "dcat:Distribution",
+                    "description": "USGS EarthExplorer provides users the ability to query, search, and dowload products available from the LP DAAC.",
+                    "downloadURL": "https://earthexplorer.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through USGS Earth Explorer"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOB/ECOSTRESS/ECO2LSTE.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOB/ECOSTRESS/ECO2LSTE.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1534730053-LPDAAC_ECS",
+            "issued": "2018-07-15",
+            "keyword": [
+                "clouds",
+                "surface radiative properties",
+                "surface thermal properties",
+                "land use/land cover",
+                "land surface",
+                "aerosols",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO3ANCQA.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "series-name": "ECO3ANCQA.001",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-07-15T00:00:00Z/2023-03-06T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS L3/L4 Ancillary data Quality Assurance (QA) flags L3 Global 70m V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2010.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY10 NASA Budget Overview",
+                    "downloadURL": "http://www.nasa.gov/home/hqnews/2009/may/HQ_09-102_FY2010Budget.html",
+                    "mediaType": "application/htmlf",
+                    "title": "FY10 NASA Budget Overview"
+                }
+            ],
+            "identifier": "OCIO-Fitara-77",
             "issued": "2009-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "strategic",
                 "budget",
@@ -1525604,368 +1525618,356 @@
                 "performance",
                 "plan"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA HQ"
             },
-            "identifier": "OCIO-Fitara-77",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2010.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2010: NASA Budget Overview",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/htmlf",
-                    "downloadURL": "http://www.nasa.gov/home/hqnews/2009/may/HQ_09-102_FY2010Budget.html",
-                    "description": "FY10 NASA Budget Overview",
-                    "@type": "dcat:Distribution",
-                    "title": "FY10 NASA Budget Overview"
-                }
-            ],
-            "accrualPeriodicity": "R/PT1S",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2010: NASA Budget Overview"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L3B/KD/2022",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L3B/KD/2022.",
-            "issued": "2022-09-14",
-            "temporal": "1997-09-04T00:00:00Z/2010-12-11T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-14",
-            "keyword": [
-                "oceans",
-                "earth science",
-                "ocean optics"
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
-            "identifier": "C1449645590-OB_DAAC",
             "description": "The SeaWiFS instrument was launched by Orbital Sciences Corporation on the OrbView-2 (a.k.a. SeaStar) satellite in August 1997, and collected data from September 1997 until the end of mission in December 2010. SeaWiFS had 8 spectral bands from 412 to 865 nm. It collected global data at 4 km resolution, and local data (limited onboard storage and direct broadcast) at 1 km. The mission and sensor were optimized for ocean color measurements, with a local noon (descending) equator crossing time orbit, fore-and-aft tilt capability, full dynamic range, and low polarization sensitivity.",
-            "title": "OrbView-2 SeaWiFS Global Binned Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FORBVIEW-2%2FSeaWiFS%2FL3B%2FKD%2F2022",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FORBVIEW-2%2FSeaWiFS%2FL3B%2FKD%2F2022",
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ORBVIEW-2/SeaWiFS/L3B/KD/2022",
-                    "description": "SeaWiFS L3B Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "SeaWiFS L3B Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/ORBVIEW-2/SeaWiFS/L3B/KD/2022",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1449645590-OB_DAAC",
+            "issued": "2022-09-14",
+            "keyword": [
+                "oceans",
+                "earth science",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/ORBVIEW-2/SeaWiFS/L3B/KD/2022",
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
+            "temporal": "1997-09-04T00:00:00Z/2010-12-11T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OrbView-2 SeaWiFS Global Binned Diffuse Attenuation Coefficient for Downwelling Irradiance (KD) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-3-EAR3-SPM-V1.0",
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
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the EAR2 (Earth fly-by 3) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-3-ear3-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-E-ROMAP-3-EAR3-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-e-romap-3-ear3-spm-v1.0",
-            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the EAR2 (Earth fly-by 3) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER EARTH ROMAP 3 EAR3 SPM V1.0",
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
+            "title": "ROSETTA-LANDER EARTH ROMAP 3 EAR3 SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-5-ROUGHNESS-OPS-V1.0",
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
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-5-roughness-ops-v1.0_vmuw-mk2k",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER2-M-HAZCAM-5-ROUGHNESS-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer2-m-hazcam-5-roughness-ops-v1.0_vmuw-mk2k",
-            "description": "NULL",
-            "title": "MER 2 MARS HAZARD AVOID CAMERA\n                                     SURFACE ROUGH RDR OPS V1.0",
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
+            "title": "MER 2 MARS HAZARD AVOID CAMERA\n                                     SURFACE ROUGH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OUVS-5-IMIDR-V1.0",
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
-                "venus",
-                "pioneer venus"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-ouvs-5-imidr-v1.0_vmva-ybdx",
+            "issued": "2018-06-26",
+            "keyword": [
+                "venus",
+                "pioneer venus"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PVO-V-OUVS-5-IMIDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.pvo-v-ouvs-5-imidr-v1.0_vmva-ybdx",
-            "description": "not applicable",
-            "title": "PVO V OUVS INBOUND MONOCHROME IMAGE DATA RECORD V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "PVO V OUVS INBOUND MONOCHROME IMAGE DATA RECORD V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/APR3/DATA201",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Durden, Stephen L. and Simone  Tanelli.2018. GPM Ground Validation Airborne Precipitation Radar 3rd Generation (APR-3) OLYMPEX V2 [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/APR3/DATA201",
-            "issued": "2018-06-15",
-            "temporal": "2015-11-12T16:24:18Z/2015-12-19T03:21:08Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-18",
-            "keyword": [
-                "earth science",
-                "radar",
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
-            "identifier": "C1979127310-GHRC_DAAC",
             "description": "The GPM Ground Validation Airborne Precipitation Radar 3rd Generation (APR-3) OLYMPEX V2 dataset was collected from November 12, 2015 to December 19, 2015 during the GPM Ground Validation Olympic Mountains Experiment (OLYMPEX) field campaign held in the Pacific Northwest. This dataset is version -2 (V2) of the APR-3, an enhanced and upgraded instrument derived from the APR-2 used in previous field campaigns.  APR-3 has the addition of W-band measurement capability, and scans cross-track from +/- 25\u00b0 to the right and left of nadir.  Ku-band, Ka-band, and W-band frequency Doppler measurements are made by APR-3 from the DC-8 aircraft at 10 km altitude during OLYMPEX.  The APR-3 dataset files are in HDF-5 format with JPG format browse images.  This dataset contains radar reflectivity, Doppler velocity for all bands, linear depolarization ratio at Ku-band, and normalized radar cross section measurements at Ka and Ku-bands.",
-            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
-            "title": "GPM Ground Validation Airborne Precipitation Radar 3rd Generation (APR-3) OLYMPEX V2",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FAPR3%2FDATA201",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FAPR3%2FDATA201",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmapr3olyx2",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmapr3olyx2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/browse/olympex_apr3_20151113_181052_R2_KUsKAsWs.jpg",
-                    "description": "Sample Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Browse Image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/browse/olympex_apr3_20151113_181052_R2_KUsKAsWs.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://olympex.atmos.washington.edu/",
-                    "description": "University of Washington OLYMPEX project web site",
                     "@type": "dcat:Distribution",
+                    "description": "University of Washington OLYMPEX project web site",
+                    "downloadURL": "http://olympex.atmos.washington.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/doc/gpmapr3olyx2_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/doc/gpmapr3olyx2_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/doc/APR3_OLYMPEX_Format_R2_180609.pdf",
-                    "description": "Product Handbook for Airborne Precipitation Radar Third Generation (APR3) OLYMPEX Data",
                     "@type": "dcat:Distribution",
+                    "description": "Product Handbook for Airborne Precipitation Radar Third Generation (APR3) OLYMPEX Data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/doc/APR3_OLYMPEX_Format_R2_180609.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://airbornescience.nasa.gov/sites/default/files/documents/pr2-mwj.pdf",
-                    "description": "Development of an advanced airborne precipitation radar.(Technical Feature)",
                     "@type": "dcat:Distribution",
+                    "description": "Development of an advanced airborne precipitation radar.(Technical Feature)",
+                    "downloadURL": "https://airbornescience.nasa.gov/sites/default/files/documents/pr2-mwj.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/LGRS.2006.872929",
-                    "description": "Simultaneous Measurements of Ku- and Ka-band Sea Surface Cross-Sections by an Airborne Radar",
                     "@type": "dcat:Distribution",
+                    "description": "Simultaneous Measurements of Ku- and Ka-band Sea Surface Cross-Sections by an Airborne Radar",
+                    "downloadURL": "https://doi.org/10.1109/LGRS.2006.872929",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dx.doi.org/10.1175/BAMS-D-16-0182.1",
-                    "description": "The Olympic Mountains Experiment (OLYMPEX)",
                     "@type": "dcat:Distribution",
+                    "description": "The Olympic Mountains Experiment (OLYMPEX)",
+                    "downloadURL": "https://dx.doi.org/10.1175/BAMS-D-16-0182.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/olympex",
-                    "description": "GHRC OLYMPEX project web page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRC OLYMPEX project web page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/olympex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/olympic-mountains-experiment-olympex",
-                    "description": "Olympic Mountains Experiment (OLYMPEX) Micro Article",
                     "@type": "dcat:Distribution",
+                    "description": "Olympic Mountains Experiment (OLYMPEX) Micro Article",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/olympic-mountains-experiment-olympex",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/browse/",
-                    "description": "Browse images illustrate the nature and coverage of the data",
                     "@type": "dcat:Distribution",
+                    "description": "Browse images illustrate the nature and coverage of the data",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/browse/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
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
+            "graphic-preview-description": "Browse images illustrate the nature and coverage of the data",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/APR3_V2/browse/",
+            "identifier": "C1979127310-GHRC_DAAC",
+            "issued": "2018-06-15",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/APR3/DATA201",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-129.14 46.1711 -122.026 49.4321",
+            "temporal": "2015-11-12T16:24:18Z/2015-12-19T03:21:08Z",
             "theme": [
                 "OLYMPEX",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Airborne Precipitation Radar 3rd Generation (APR-3) OLYMPEX V2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.2_vmwe-sfwp",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "rhea",
                 "phoebe",
@@ -1525999,69 +1526001,44 @@
                 "atlas",
                 "pandora"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-S-UVIS-2-SSB-V1.2",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-s-uvis-2-ssb-v1.2_vmwe-sfwp",
-            "description": "Photometric observations of stellar occultations by Saturnian rings, satellites, atmospheres, and Jovian atmosphere.",
-            "title": "CASSINI SATURN UVIS SOLAR STELLAR BRIGHTNESS TIME SERIES 1.2",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CASSINI SATURN UVIS SOLAR STELLAR BRIGHTNESS TIME SERIES 1.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "issue-identification": "ACOS_L2S_9r",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/OSGTIL9OV0PN",
             "citation": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering. 2019-10-04. ACOS_L2S. Version 9r. ACOS GOSAT/TANSO-FTS Level 2 Full Physics Standard Product V9r. Greenbelt, MD, USA. ACOS_L2S_9r. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/OSGTIL9OV0PN. https://disc.gsfc.nasa.gov/datacollection/ACOS_L2S_9r.html. Digital Science Data.",
-            "issued": "2019-10-02",
-            "temporal": "2009-04-20T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-04-14",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANDREY SAVTCHENKO",
                 "hasEmail": "mailto:Andrey.Savtchenko@nasa.gov"
             },
+            "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1633158704-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "Version 9r is the current version of the data set. Older versions will no longer be available and are superseded by Version 9r.\n\nThis data set is currently provided by the OCO (Orbiting Carbon Observatory) Project. In expectation of the OCO-2 launch, the algorithm was developed by the Atmospheric CO2 Observations from Space (ACOS) Task as a preparatory project, using GOSAT TANSO-FTS spectra. After the OCO-2 launch,  \"ACOS\" data are still produced and improved, using approaches applied to the OCO-2 spectra.\n\nThe \"ACOS\" data set contains Carbon Dioxide (CO2) column averaged dry air mole fraction for all soundings for which retrieval was attempted. These are the highest-level products made available by the OCO Project, using TANSO-FTS spectral radiances, and algorithm build version 7.3.\n\nThe GOSAT team at JAXA produces GOSAT TANSO-FTS Level 1B (L1B) data products for internal use and for distribution to collaborative partners, such as ESA and NASA. These calibrated products are augmented by the OCO Project with additional geolocation information and further corrections. Thus produced Level 1B products (with calibrated radiances and geolocation) are the input to the \"ACOS\" Level 2 production process.\n\nEven though the GES DISC is not publicly distributing Level 1B ACOS products, it should be known that changes in this version are affecting both Level 1B and Level 2 data. An important enhancement in Level1B will address the degradation in the number of quality-passed soundings. \n\nElimination of many systematic biases, and better agreement with TCCON (Total Carbon Column Observing Network), is expected in Level 2 retrievals. The key changes to the L2 algorithm include scaling the O2-A band spectroscopy (reducing XCO2 bias by 4 or 5 ppm); using interpolation with the instrument lineshape [ ILS ] (reducing XCO2 bias by 1.5 ppm); and fitting a zero level offset to the A-band. Users have to also carefully familiarize themselves with the disclaimer in the new documentation. \n\nAn important element to note are the updates on data screening. Although a Master Quality Flag is provided in the data product, further analysis of a larger set of data has allowed the science team to provide an updated set of screening criteria. These are listed in the data user's guide, and are recommended instead of the Master Quality Flag.\n\n\nLastly, users should continue to carefully observe and weigh information from three important flags:\n \n\n      \"sounding_qual_flag\" - quality of input data provided to the retrieval processing    \n\n      \"outcome_flag\" - retrieval quality based upon certain internal thresholds (not thoroughly evaluated)",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ACOS_L2S",
-            "creator": "OCO-2 Science Team/Michael Gunson, Annmarie Eldering",
-            "title": "ACOS GOSAT/TANSO-FTS Level 2 Full Physics Standard Product V9r (ACOS_L2S) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/ACOS.v9.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOSGTIL9OV0PN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FOSGTIL9OV0PN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1526071,140 +1526048,175 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ACOS_L2S_9r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ACOS_L2S_9r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/GOSAT_TANSO_Level2/ACOS_L2S.9r/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/GOSAT_TANSO_Level2/ACOS_L2S.9r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ACOS_L2S+9r",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ACOS_L2S+9r",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/ACOS_L2S.9r/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/ACOS_L2S.9r/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.gosat.nies.go.jp/index_e.html",
-                    "description": "GOSAT site",
                     "@type": "dcat:Distribution",
+                    "description": "GOSAT site",
+                    "downloadURL": "http://www.gosat.nies.go.jp/index_e.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/ACOS_v9_DataUsersGuide.pdf",
-                    "description": "User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/ACOS_v9_DataUsersGuide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/ACOS_L2_DQ_Statement.v9.pdf",
-                    "description": "ACOS Data Quality Statment",
                     "@type": "dcat:Distribution",
+                    "description": "ACOS Data Quality Statment",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/ACOS_L2_DQ_Statement.v9.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ocov2.jpl.nasa.gov/science/publications/",
-                    "description": "OCO-2 Publications from the Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-2 Publications from the Science Team",
+                    "downloadURL": "https://ocov2.jpl.nasa.gov/science/publications/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ocov3.jpl.nasa.gov/science/publications/",
-                    "description": "OCO-3 Publications from the Science Team",
                     "@type": "dcat:Distribution",
+                    "description": "OCO-3 Publications from the Science Team",
+                    "downloadURL": "https://ocov3.jpl.nasa.gov/science/publications/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/KnownDataIssues.ACOS.html",
-                    "description": "ACOS Data Gaps",
                     "@type": "dcat:Distribution",
+                    "description": "ACOS Data Gaps",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/KnownDataIssues.ACOS.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.gosat.nies.go.jp/en/about_%EF%BC%92_observe.html",
-                    "description": "Instrument Description",
                     "@type": "dcat:Distribution",
+                    "description": "Instrument Description",
+                    "downloadURL": "http://www.gosat.nies.go.jp/en/about_%EF%BC%92_observe.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/ACOS.v9.png",
+            "identifier": "C1633158704-GES_DISC",
+            "issue-identification": "ACOS_L2S_9r",
+            "issued": "2019-10-02",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/OSGTIL9OV0PN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-04-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "ACOS_L2S",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2009-04-20T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "OCO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ACOS GOSAT/TANSO-FTS Level 2 Full Physics Standard Product V9r (ACOS_L2S) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-3-EAR2-CALIBRATED-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains CALIBRATED DATA of the second Earth Flyby(EAR2). The closest approach (CA) took place on November 13, 2007 at 20:57",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-3-ear2-calibrated-v3.0_vmyt-by58",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "unknown",
                 "earth",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-3-EAR2-CALIBRATED-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-3-ear2-calibrated-v3.0_vmyt-by58",
-            "description": "This dataset contains CALIBRATED DATA of the second Earth Flyby(EAR2). The closest approach (CA) took place on November 13, 2007 at 20:57",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 3 EAR2 CALIBRATED V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 3 EAR2 CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985619-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "Sentinel-1B Single-pol ground projected high and full resolution metadata",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1327985619-ASF",
             "issued": "2016-08-20",
-            "temporal": "2016-04-25T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
             "keyword": [
                 "landscape",
                 "frozen ground",
@@ -1526231,50 +1526243,47 @@
                 "tectonics",
                 "terrestrial ecosystems"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985619-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-17",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1327985619-ASF",
-            "description": "Sentinel-1B Single-pol ground projected high and full resolution metadata",
-            "title": "SENTINEL-1B_SINGLE_POL_METADATA_GRD_HIGH_RES",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
-                    "description": "Vertex, the ASF search and download interface",
-                    "@type": "dcat:Distribution",
-                    "title": "Download this dataset"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-04-25T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SENTINEL-1B_SINGLE_POL_METADATA_GRD_HIGH_RES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://itunes.apple.com/us/itunes-u/nasas-journey-to-project-management/id443158587?i=125444483",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://km.nasa.gov/knowledge-map/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ed Hoffman",
+                "hasEmail": "mailto:ehoffman@nasa.gov"
+            },
+            "description": "NASA's Path to Project Management Excellence eBook. Leadership plays a critical role in the success of today\u2019s programs and projects. In an increasingly global and dynamic project environment, the ability to for organizations to foster and develop project leaders who can lead in and deliver unique, innovative products and missions on time and budget has never been more important.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://itunes.apple.com/us/podcast/art-science-systems-engineering/id443158587?i=126031039&mt=2",
+                    "mediaType": "application/x-itunes-itlp"
+                }
             ],
+            "identifier": "NASA-864__1",
+            "issued": "2018-06-25",
             "keyword": [
                 "training",
                 "ebook",
@@ -1526285,679 +1526294,650 @@
                 "leadership",
                 "knowledge"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ed Hoffman",
-                "hasEmail": "mailto:ehoffman@nasa.gov"
-            },
+            "landingPage": "https://itunes.apple.com/us/itunes-u/nasas-journey-to-project-management/id443158587?i=125444483",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-864__1",
-            "description": "NASA's Path to Project Management Excellence eBook. Leadership plays a critical role in the success of today\u2019s programs and projects. In an increasingly global and dynamic project environment, the ability to for organizations to foster and develop project leaders who can lead in and deliver unique, innovative products and missions on time and budget has never been more important.",
-            "title": "Academy of Program/Project & Engineering Leadership: NASA's Path to Project Management Excellence",
-            "programCode": [
-                "026:045"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://itunes.apple.com/us/podcast/art-science-systems-engineering/id443158587?i=126031039&mt=2",
-                    "mediaType": "application/x-itunes-itlp"
-                }
+            "references": [
+                "http://km.nasa.gov/knowledge-map/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Academy of Program/Project & Engineering Leadership: NASA's Path to Project Management Excellence"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-E-HRIV-3%2F4-EPOXI-EARTH-V2.0",
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
-                "earth"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains calibrated, narrow band filter images (350-950 nm) of Earth acquired by the Deep Impact High Resolution Visible CCD (HRIV) during the EPOCh and Cruise 2 phases of the EPOXI mission. Five sets of observations were acquired on 18-19 March, 28-29 May and 04-05 June 2008 and on 27-28 March and 04-05 October 2009 to characterize Earth as an analog for extrasolar planets. Each observing period lasted approximately 24 hours. HRIV images were acquired once per hour with the filters centered on 350, 750 and 950 nm, whereas the 450-, 550-, 650-, and 850-nm data were taken every 15 minutes. During the observing period in May 2008, the Moon transited across Earth as seen from the spacecraft. On 27 September 2009 during the first attempt of an Earth south polar observation, only seven HRIV frames were acquired before fault protection turned that instrument off; the full sequence was successfully rerun on 04-05 October 2009. Version 2.0 includes the application of a horizontal destriping process and revised electronic crosstalk calibration files.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-e-hriv-3-4-epoxi-earth-v2.0_vn4h-2833",
+            "issued": "2018-06-26",
+            "keyword": [
+                "epoxi",
+                "earth"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-E-HRIV-3%2F4-EPOXI-EARTH-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-e-hriv-3-4-epoxi-earth-v2.0_vn4h-2833",
-            "description": "This data set contains calibrated, narrow band filter images (350-950 nm) of Earth acquired by the Deep Impact High Resolution Visible CCD (HRIV) during the EPOCh and Cruise 2 phases of the EPOXI mission. Five sets of observations were acquired on 18-19 March, 28-29 May and 04-05 June 2008 and on 27-28 March and 04-05 October 2009 to characterize Earth as an analog for extrasolar planets. Each observing period lasted approximately 24 hours. HRIV images were acquired once per hour with the filters centered on 350, 750 and 950 nm, whereas the 450-, 550-, 650-, and 850-nm data were taken every 15 minutes. During the observing period in May 2008, the Moon transited across Earth as seen from the spacecraft. On 27 September 2009 during the first attempt of an Earth south polar observation, only seven HRIV frames were acquired before fault protection turned that instrument off; the full sequence was successfully rerun on 04-05 October 2009. Version 2.0 includes the application of a horizontal destriping process and revised electronic crosstalk calibration files.",
-            "title": "EPOXI EARTH OBS - HRIV CALIBRATED IMAGES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "EPOXI EARTH OBS - HRIV CALIBRATED IMAGES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M12-STR-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m12-str-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC1-67P-M12-STR-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc1-67p-m12-str-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in in reflectance units (normalized and thus without unit), acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 1 mission phase, covering the period from 2015-01-13T23:25:00.000 to 2015-02-10T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP012 RDR-STR-REFL V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC1-MTP012 RDR-STR-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-3-KEM1-V2.0",
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
-                "new horizons kuiper belt extended mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach field where MU69 was expected to reside during the MU69 encounter on Jan. 1, 2019. The data also covers the actual MU69 encounter.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-3-kem1-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LORRI-3-KEM1-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-lorri-3-kem1-v2.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the KEM1 ENCOUNTER mission phase. This is VERSION 2.0 of this data set. This data set contains data acquired by the spacecraft between 08/14/2018 and 01/31/2019. It only includes data downlinked before 02/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 01/31/2019. It includes a number of distant Kuiper Belt Objects (DKBOs). It also includes images of the approach field where MU69 was expected to reside during the MU69 encounter on Jan. 1, 2019. The data also covers the actual MU69 encounter.",
-            "title": "NEW HORIZONS\n      LORRI KEM1\n      CALIBRATED V2.0",
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
+            "title": "NEW HORIZONS\n      LORRI KEM1\n      CALIBRATED V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC4-MTP022-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase 4 from 20th Oct 2015 to 17th Nov 2015 when at the vicinity of target 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc4-mtp022-v1.0_vn9y-8zcm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-NAVCAM-2-ESC4-MTP022-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-navcam-2-esc4-mtp022-v1.0_vn9y-8zcm",
-            "description": "This dataset contains ROSETTA NAVCAM RAW DATA of the Escort Phase 4 from 20th Oct 2015 to 17th Nov 2015 when at the vicinity of target 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 4 MTP022 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P NAVCAM 2 COMET ESCORT 4 MTP022 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/5RSOL3F0VBBO",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX04 Landsat Thematic Mapper Imagery, Sonora, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/5RSOL3F0VBBO.",
-            "issued": "2004-06-11",
-            "temporal": "2004-06-11T00:00:00Z/2004-08-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2004-08-30",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "visible wavelengths",
-                "infrared wavelengths"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Jackson",
                 "hasEmail": "mailto:tom.jackson@ars.usda.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386205616-NSIDCV0",
             "description": "This data set provides imagery developed from Landsat 5 Thematic Mapper (TM) data for use in studying land cover features during the Soil Moisture Experiment 2004 (SMEX04). Three false color images are provided for the regional study areas in Arizona, USA and Sonora, Mexico.",
-            "title": "SMEX04 Landsat Thematic Mapper Imagery, Sonora, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5RSOL3F0VBBO",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F5RSOL3F0VBBO",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/satellite/TM_GEOTIFF/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/satellite/TM_GEOTIFF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/satellite/TM_GEOTIFF/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX04/Sonora/satellite/TM_GEOTIFF/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/5RSOL3F0VBBO",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/5RSOL3F0VBBO",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/5RSOL3F0VBBO",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/5RSOL3F0VBBO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205616-NSIDCV0",
+            "issued": "2004-06-11",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "visible wavelengths",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/5RSOL3F0VBBO",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2004-08-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-111.4 29.33 -108.56 32.69",
+            "temporal": "2004-06-11T00:00:00Z/2004-08-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX04 Landsat Thematic Mapper Imagery, Sonora, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/IHHLJSPI5W3O",
             "citation": "Chris Barnet. 2019-12-15. SNDRSNIML3SMCCP. Version 2. Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS Full Spectral Resolution V2. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/IHHLJSPI5W3O. https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3SMCCP_2.html.html. Digital Science Data.",
-            "issued": "2015-11-01",
-            "temporal": "2015-11-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-01",
-            "references": [
-                "https://doi.org/10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2012.2220369",
-                "https://doi.org/10.3390/rs11101227",
-                "https://doi.org/10.1109/TGRS.2002.808236",
-                "https://doi.org/10.1029/2005/JD007020",
-                "https://doi.org/10.5194/amt-13-4437-2020"
-            ],
-            "keyword": [
-                "atmospheric pressure",
-                "air quality",
-                "altitude",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "clouds",
-                "earth science",
-                "land surface",
-                "oceans",
-                "ocean temperature",
-                "precipitation",
-                "surface radiative properties",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lena Iredell",
                 "hasEmail": "mailto:lena.iredell@nasa.gov"
             },
+            "creator": "Chris Barnet",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1692982089-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
             "description": "WARNING: To users of the derived product \u201cco_mmr_midtrop\u201d (carbon monoxide mass mixing ratio to dry air [kg/kg] at ~500 hPa). This variable has a significant bias due to a conversion error: the molecular weight of carbon dioxide (CO2, 44.01 g/mol) was used instead of carbon monoxide (CO, 28.01 g/mol). To correct, simply multiply \u201cco_mmr_midtrop\u201d by 28.01/44.01. Alternatively, derive a profile of mass mixing ratio from scratch using the retrieved column density values (\u201cmol_lay/co_mol_lay\u201d) in the Level 2 files. For further questions or concerns please contact the Sounder SIPS at: sounder.sips@jpl.nasa.gov\n\nThe CLIMCAPS (Community Long-term Infrared Microwave Coupled Product System) algorithm is used to analyze data from the Cross-track Infrared Sounder/Advanced Technology Microwave Sounder (CrIS/ATMS) instruments, also known as CrIMSS (Cross-track Infrared and Microwave Sounding Suite). The CrIS/ATMS instruments used for this product are on board the Suomi National Polar-orbiting Partnership (SNPP) platform and use the Full Spectral Resolution (FSR) data. The CrIS instrument is a Fourier transform spectrometer with a total of 2211 FSR infrared sounding channels covering the longwave (645-1095 cm-1), midwave (1210-1750 cm-1), and shortwave (2000-2550 cm-1) spectral regions. The ATMS instrument  is a cross-track scanner with 22 channels in spectral bands from 23 GHz through 183 GHz.\n \nThe CLIMCAPS algorithm uses an Optimal Estimation methodology and uses an a-priori first guess to start the process. A CLIMCAPS sounding is comprised of a set of parameters that characterizes the full atmospheric state and includes a variety of geophysical parameters derived from the CrIMSS data. These include surface temperature and infrared emissivity; full atmosphere profiles of temperature, water vapor and ozone; infrared effective cloud top characteristics; carbon monoxide, methane, carbon dioxide, sulfur dioxide, nitrous oxide, and nitric acid.\n \nThis monthly one degree latitude by one degree longitude level-3 product starts with level-2 retrieval products with QC values of 0 (best), 1 (good), and 2 (don't use) which are provided for each variable. Specific QC accepts profile level from the top of the atmosphere down to the level where the QC determines that it is still good. Below this level, the data is rejected.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "SNDRSNIML3SMCCP",
-            "creator": "Chris Barnet",
-            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
-            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS Full Spectral Resolution V2 at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SMCCP_2.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIHHLJSPI5W3O",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIHHLJSPI5W3O",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SMCCP_2.png",
-                    "description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
                     "@type": "dcat:Distribution",
+                    "description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SMCCP_2.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3SMCCP_2.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/SNDRSNIML3SMCCP_2.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level3/SNDRSNIML3SMCCP.2",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/data/SNPP_Sounder_Level3/SNDRSNIML3SMCCP.2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level3/SNDRSNIML3SMCCP.2/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://sounder.gesdisc.eosdis.nasa.gov/opendap/SNPP_Sounder_Level3/SNDRSNIML3SMCCP.2/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML3SMCCP+2",
-                    "description": "Search the Earthdata website",
                     "@type": "dcat:Distribution",
+                    "description": "Search the Earthdata website",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNDRSNIML3SMCCP+2",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.L3.V2.README.pdf",
-                    "description": "CLIMCAPS Product User Guide:File Format and Definition",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS Product User Guide:File Format and Definition",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.L3.V2.README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.ATBD.pdf",
-                    "description": "CLIMCAPS ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "CLIMCAPS ATBD",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Sounder/CLIMCAPS.V2.ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-description": "Sample plot of CrIS/ATMS Level 3 monthly surface skin temperature (K).",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/SNDRSNIML3SMCCP_2.png",
+            "identifier": "C1692982089-GES_DISC",
+            "issued": "2015-11-01",
+            "keyword": [
+                "atmospheric pressure",
+                "air quality",
+                "altitude",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science",
+                "land surface",
+                "oceans",
+                "ocean temperature",
+                "precipitation",
+                "surface radiative properties",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/IHHLJSPI5W3O",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-06-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/10.3390/rs11101227",
+                "https://doi.org/10.1109/TGRS.2012.2220369",
+                "https://doi.org/10.3390/rs11101227",
+                "https://doi.org/10.1109/TGRS.2002.808236",
+                "https://doi.org/10.1029/2005/JD007020",
+                "https://doi.org/10.5194/amt-13-4437-2020"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "SNDRSNIML3SMCCP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2015-11-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "SUOMI-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sounder SIPS: Suomi NPP CrIMSS Level 3 Specific Quality Control Gridded Monthly CLIMCAPS Full Spectral Resolution V2 at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CVP-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the Commissioning phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cvp-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO%2FRL-CAL-CONSERT-2-CVP-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-rl-cal-consert-2-cvp-v1.0",
-            "description": "This archive contains data from the CONSERT instrument onboard ROSETTA Orbiter and Lander, acquired during the Commissioning phase. It also contains documentation which describes the CONSERT experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                            2 CVP V1.0",
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
+            "title": "ROSETTA-ORBITER/ROSETTA-LANDER CAL CONSERT\n                            2 CVP V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386246127-NSIDCV0.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "High-Resolution QuickBird Imagery and Related GIS Layers for Barrow, Alaska, USA, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center.",
-            "issued": "2002-08-01",
-            "temporal": "2002-08-01T00:00:00Z/2002-08-02T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-08-02",
-            "keyword": [
-                "spectral/engineering",
-                "land surface",
-                "visible wavelengths",
-                "surface radiative properties",
-                "infrared wavelengths",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Craig Tweedie",
                 "hasEmail": "mailto:ctweedie@utep.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386246127-NSIDCV0",
             "description": "This data set contains high-resolution QuickBird imagery and geospatial data for the entire Barrow QuickBird image area (156.15\u00b0 W - 157.07\u00b0 W, 71.15\u00b0 N - 71.41\u00b0 N) and Barrow B4 Quadrangle (156.29\u00b0 W - 156.89\u00b0 W, 71.25\u00b0 N - 71.40\u00b0 N), for use in Geographic Information Systems (GIS) and remote sensing software. The original QuickBird data sets were acquired by DigitalGlobe from 1 to 2 August 2002, and consist of orthorectified satellite imagery. Federal Geographic Data Committee (FGDC)-compliant metadata for all value-added data sets are provided in text, HTML, and XML formats.\n\nAccessory layers include: 1:250,000- and 1:63,360-scale USGS Digital Raster Graphic (DRG) mosaic images (GeoTIFF format); 1:250,000- and 1:63,360-scale USGS quadrangle index maps (ESRI Shapefile format); an index map for the 62 QuickBird tiles (ESRI Shapefile format); and a simple polygon layer of the extent of the Barrow QuickBird image area and the Barrow B4 quadrangle area (ESRI Shapefile format).\n\nUnmodified QuickBird data comprise 62 data tiles in Universal Transverse Mercator (UTM) Zone 4 in GeoTIFF format. Standard release files describing the QuickBird data are included, along with the DigitalGlobe license agreement and product handbooks.\n\nThe baseline geospatial data support education, outreach, and multi-disciplinary research of environmental change in Barrow, which is an area of focused scientific interest. Data are provided on four DVDs. This product is available only to investigators funded specifically from the National Science Foundation (NSF), Office of Polar Programs (OPP), Arctic Sciences Section. An NSF OPP award number must be provided when ordering this data.",
-            "title": "High-Resolution QuickBird Imagery and Related GIS Layers for Barrow, Alaska, USA, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/data/barrow/digitalglobe_license_form.html",
-                    "description": "Place an order for data not available for immediate download.",
                     "@type": "dcat:Distribution",
+                    "description": "Place an order for data not available for immediate download.",
+                    "downloadURL": "http://nsidc.org/data/barrow/digitalglobe_license_form.html",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/data/barrow/digitalglobe_license_form.html",
-                    "description": "Place an order for data not available for immediate download.",
                     "@type": "dcat:Distribution",
+                    "description": "Place an order for data not available for immediate download.",
+                    "downloadURL": "http://nsidc.org/data/barrow/digitalglobe_license_form.html",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/data/barrow/digitalglobe_license_form.html",
-                    "description": "Place an order for data not available for immediate download.",
                     "@type": "dcat:Distribution",
+                    "description": "Place an order for data not available for immediate download.",
+                    "downloadURL": "http://nsidc.org/data/barrow/digitalglobe_license_form.html",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://nsidc.org/data/barrow/digitalglobe_license_form.html",
-                    "description": "Place an order for data not available for immediate download.",
                     "@type": "dcat:Distribution",
+                    "description": "Place an order for data not available for immediate download.",
+                    "downloadURL": "http://nsidc.org/data/barrow/digitalglobe_license_form.html",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/ARCSS304/versions/1",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://nsidc.org/data/ARCSS304/versions/1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/ARCSS304/versions/1",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://nsidc.org/data/ARCSS304/versions/1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386246127-NSIDCV0",
+            "issued": "2002-08-01",
+            "keyword": [
+                "spectral/engineering",
+                "land surface",
+                "visible wavelengths",
+                "surface radiative properties",
+                "infrared wavelengths",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1386246127-NSIDCV0.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-08-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "-157.07033 71.14764 -156.14847 71.405",
+            "temporal": "2002-08-01T00:00:00Z/2002-08-02T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "High-Resolution QuickBird Imagery and Related GIS Layers for Barrow, Alaska, USA, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/F4FE5VWM9501",
             "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRNO2M3D. Version 1. TROPESS Chemical Reanalysis NO2 Monthly 3-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/F4FE5VWM9501. https://disc.gsfc.nasa.gov/datacollection/TRPSCRNO2M3D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2837626422-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis NO2 Monthly 3-dimensional Product contains vertical concentrations of nitrogen dioxide. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at monthly resolution, and a spatial resolution of 1.125 x 1.125 degrees at 27 pressure levels between 1000 and 60 hPa. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRNO2M3D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis NO2 Monthly 3-dimensional Product V1 (TRPSCRNO2M3D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRNO2M3D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FF4FE5VWM9501",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FF4FE5VWM9501",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRNO2M3D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRNO2M3D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRNO2M3D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRNO2M3D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRNO2M3D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRNO2M3D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRNO2M3D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRNO2M3D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRNO2M3D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_VERTCONCS/TRPSCRNO2M3D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRNO2M3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRNO2M3D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tes.jpl.nasa.gov/tes/chemical-reanalysis/",
-                    "description": "Chemical Reanalysis Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "Chemical Reanalysis Project Home Page.",
+                    "downloadURL": "https://tes.jpl.nasa.gov/tes/chemical-reanalysis/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRNO2M3D_Sample.png",
+            "identifier": "C2837626422-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/F4FE5VWM9501",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSCRNO2M3D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis NO2 Monthly 3-dimensional Product V1 (TRPSCRNO2M3D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-COSAC-2-PHC-V1.0",
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
-                "calibration",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains edited data (CODMAC level 2) from the COSAC instrument onboard ROSETTA Lander, acquired during the PHC (comet) phase. It also contains documentation which describes the COSAC experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-cosac-2-phc-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-COSAC-2-PHC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-cosac-2-phc-v1.0",
-            "description": "This archive contains edited data (CODMAC level 2) from the COSAC instrument onboard ROSETTA Lander, acquired during the PHC (comet) phase. It also contains documentation which describes the COSAC experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL COSAC 2 PHC V1.0",
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
+            "title": "ROSETTA-LANDER CAL COSAC 2 PHC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://earth.gsfc.nasa.gov/climate/missions/icecube",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2021-04-01",
-            "@type": "dcat:Dataset",
-            "temporal": "June 13, 2017 - September 30, 2018",
-            "modified": "2023-01-31",
-            "keyword": [
-                "earth remote sensing instruments",
-                "clouds",
-                "cubesat",
-                "sub-millimeter radiometer",
-                "snow/ice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jie Gong; Dong L. Wu",
                 "hasEmail": "mailto:jie.gong@nasa.gov; Dong.L.Wu@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Jie Gong"
-            },
-            "identifier": "https://data.nasa.gov/api/views/vnjm-idc4",
+            "dataQuality": true,
             "description": "This zipped meta data file can be expanded into two folders. One folder contains the daily calibrated Level 1 radiance and geolocation data in HDF5 format, and the other folder contains the main IDL codes that process the data and make plots (mainly for generating plots for the paper Gong et al. 2021 that is under review for Earth Science System Data journal). Both folders contain a README file in each to guide readers through the file name, variable namelist, quality flag, code's usage, etc.",
-            "title": "IceCube Level 1 Radiance Data and Codes",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1526966,1028 +1526946,1049 @@
                     "title": "IceCube_L1B_data_code_v1"
                 }
             ],
-            "spatial": "67S - 67N",
-            "dataQuality": true,
+            "identifier": "https://data.nasa.gov/api/views/vnjm-idc4",
+            "issued": "2021-04-01",
+            "keyword": [
+                "earth remote sensing instruments",
+                "clouds",
+                "cubesat",
+                "sub-millimeter radiometer",
+                "snow/ice"
+            ],
+            "landingPage": "https://earth.gsfc.nasa.gov/climate/missions/icecube",
+            "language": [
+                "English"
+            ],
             "license": "http://creativecommons.org/licenses/by/4.0/legalcode",
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Jie Gong"
+            },
+            "spatial": "67S - 67N",
+            "temporal": "June 13, 2017 - September 30, 2018",
             "theme": [
                 "Level 1 calibrated radiance"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "IceCube Level 1 Radiance Data and Codes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/LIS/LIS-OTD/DATA309",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Cecil, Daniel J.2006. LIS/OTD 2.5 Degree Low Resolution Monthly Climatology Time Series (LRMTS) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/LIS/LIS-OTD/DATA309",
-            "issued": "2006-09-13",
-            "temporal": "1995-05-04T00:00:00Z/2015-04-08T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric electricity",
-                "weather events"
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
-            "identifier": "C1995865015-GHRC_DAAC",
             "description": "The LIS/OTD 2.5 Degree Low Resolution Monthly Climatology Time Series (LRMTS) contains a variety of gridded climatologies of total lightning flash rates obtained from two lightning detection sensors - the spaceborne Optical Transient Detector (OTD) on Orbview-1 and the Lightning Imaging Sensor (LIS) onboard the Tropical Rainfall Measuring Mission (TRMM) satellite. The long LIS (equatorward of about 38 degree) record makes the merged climatology most robust in the tropics and subtropics, while the high latitude data is entirely from OTD. The LRMTS dataset include monthly flash rate time series data in MP4 format.",
-            "graphic-preview-description": "N/A",
-            "title": "LIS/OTD 2.5 Degree Low Resolution Monthly Climatology Time Series (LRMTS) V2.3.2015",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS-OTD/LRMTS/animations/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLIS-OTD%2FDATA309",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLIS%2FLIS-OTD%2FDATA309",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=lolrmts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=lolrmts",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/ghrc/lis/lisotd/lolrmts/LRMTS_COM_V2.3.2015.jpg",
-                    "description": "Browse Sample",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Sample",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/browse_sample/ghrc/lis/lisotd/lolrmts/LRMTS_COM_V2.3.2015.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20110015779.pdf",
-                    "description": "The 13 years of TRMM Lightning Imaging Sensor: From individual flash characteristics to decadal tendencies",
                     "@type": "dcat:Distribution",
+                    "description": "The 13 years of TRMM Lightning Imaging Sensor: From individual flash characteristics to decadal tendencies",
+                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20110015779.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dx.doi.org/10.1029/2002JD002347",
-                    "description": "Global frequency and distribution of lightning as observed from space by the Optical Transient Detector",
                     "@type": "dcat:Distribution",
+                    "description": "Global frequency and distribution of lightning as observed from space by the Optical Transient Detector",
+                    "downloadURL": "https://dx.doi.org/10.1029/2002JD002347",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dx.doi.org/10.5067/LIS/LIS-OTD/DATA311",
-                    "description": "Digital Object Identifier for a collection of related datasets",
                     "@type": "dcat:Distribution",
+                    "description": "Digital Object Identifier for a collection of related datasets",
+                    "downloadURL": "https://dx.doi.org/10.5067/LIS/LIS-OTD/DATA311",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/LISOTD_climatology_dataset.pdf",
-                    "description": "LIS/OTD Climatology Dataset Collection User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "LIS/OTD Climatology Dataset Collection User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/LISOTD_climatology_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/LISOTD_Climo_prod_table.doc",
-                    "description": "Products in LIS-OTD gridded climatology files",
                     "@type": "dcat:Distribution",
+                    "description": "Products in LIS-OTD gridded climatology files",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/LISOTD_Climo_prod_table.doc",
+                    "mediaType": "application/msword",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.1016/j.atmosres.2012.06.028",
-                    "description": "Gridded lightning climatology from TRMM-LIS and OTD: Dataset description",
                     "@type": "dcat:Distribution",
+                    "description": "Gridded lightning climatology from TRMM-LIS and OTD: Dataset description",
+                    "downloadURL": "http://dx.doi.org/10.1016/j.atmosres.2012.06.028",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/getgrid.pro",
-                    "description": "Read SDS Arrays From an A HDF file",
                     "@type": "dcat:Distribution",
+                    "description": "Read SDS Arrays From an A HDF file",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/getgrid.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/read_sds.pro",
-                    "description": "Read an SDS grid from the LIS/OTD HDF climatology files",
                     "@type": "dcat:Distribution",
+                    "description": "Read an SDS grid from the LIS/OTD HDF climatology files",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/lis_climatology/read_sds.pro",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/",
-                    "description": "Lightning Imaging Sensor (LIS) Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Lightning Imaging Sensor (LIS) Overview",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/lightning/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS-OTD/LRMTS/animations/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS-OTD/LRMTS/animations/",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
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
-            "spatial": "-178.75 -88.75 178.75 88.75",
-            "theme": [
-                "LIS",
-                "geospatial"
+            "graphic-preview-description": "N/A",
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/lis/climatology/LIS-OTD/LRMTS/animations/",
+            "identifier": "C1995865015-GHRC_DAAC",
+            "issued": "2006-09-13",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric electricity",
+                "weather events"
             ],
+            "landingPage": "https://doi.org/10.5067/LIS/LIS-OTD/DATA309",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/ABDPEPHV3MMM",
-            "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRECOTM2D. Version 1. TROPESS Chemical Reanalysis Surface Total CO emissions Monthly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ABDPEPHV3MMM. https://disc.gsfc.nasa.gov/datacollection/TRPSCRECOTM2D_1.html. Digital Science Data.",
-            "issued": "2023-01-09",
-            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
-            "references": [
-                "https://doi.org/10.1126/sciadv.abf7460"
+            "modified": "2022-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
+            "spatial": "-178.75 -88.75 178.75 88.75",
+            "temporal": "1995-05-04T00:00:00Z/2015-04-08T23:59:59Z",
+            "theme": [
+                "LIS",
+                "geospatial"
             ],
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "atmosphere"
+            "title": "LIS/OTD 2.5 Degree Low Resolution Monthly Climatology Time Series (LRMTS) V2.3.2015"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "026:00"
             ],
+            "citation": "Miyazaki, Kazuyuki. 2024-02-06. TRPSCRECOTM2D. Version 1. TROPESS Chemical Reanalysis Surface Total CO emissions Monthly 2-dimensional Product V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/ABDPEPHV3MMM. https://disc.gsfc.nasa.gov/datacollection/TRPSCRECOTM2D_1.html. Digital Science Data.",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "KAZUYUKI MIYAZAKI",
                 "hasEmail": "mailto:kazuyuki.miyazaki@jpl.nasa.gov"
             },
+            "creator": "Miyazaki, Kazuyuki",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C2837624963-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The TROPESS Chemical Reanalysis Surface Total CO emissions Monthly 2-dimensional Product contains carbon monoxide emissions from the total of all sources. The data are part of the Tropospheric Chemical Reanalysis v2 (TCR-2) for the period 2005-2021. TCR-2 uses JPL's Multi-mOdel Multi-cOnstituent Chemical (MOMO-Chem) data assimilation framework that simultaneously optimizes both concentrations and emissions of multiple species from multiple satellite sensors.\n\nThe data files are written in the netCDF version 4 file format, and each file contains a year of data at monthly resolution, and a spatial resolution of 1.125 x 1.125 degrees. The principal investigator for the TCR-2 data is Miyazaki, Kazuyuki.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "TRPSCRECOTM2D",
-            "creator": "Miyazaki, Kazuyuki",
-            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
-            "title": "TROPESS Chemical Reanalysis Surface Total CO emissions Monthly 2-dimensional Product V1 (TRPSCRECOTM2D) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRECOTM2D_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FABDPEPHV3MMM",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FABDPEPHV3MMM",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRECOTM2D_Sample.png",
-                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
                     "@type": "dcat:Distribution",
+                    "description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRECOTM2D_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRECOTM2D_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/TRPSCRECOTM2D_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRECOTM2D.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_VERTCONCS/TRPSCRECOTM2D.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRECOTM2D_1",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=TRPSCRECOTM2D_1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_EMISSIONS/TRPSCRECOTM2D.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/opendap/TCR2_MON_EMISSIONS/TRPSCRECOTM2D.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_EMISSIONS/TRPSCRECOTM2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://tropess.gesdisc.eosdis.nasa.gov/data/TCR2_MON_EMISSIONS/TRPSCRECOTM2D.1/doc/TROPESS_ChemReanalysis_Forward_Stream_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tes.jpl.nasa.gov/tes/chemical-reanalysis/",
-                    "description": "Chemical Reanalysis Project Home Page.",
                     "@type": "dcat:Distribution",
+                    "description": "Chemical Reanalysis Project Home Page.",
+                    "downloadURL": "https://tes.jpl.nasa.gov/tes/chemical-reanalysis/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "TROPESS CrIS-SNPP Los Angeles Megacity (Forward Stream, Summary Product) at 681 hPa on 01 April 2021.",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/TROPESS/images/TRPSCRECOTM2D_Sample.png",
+            "identifier": "C2837624963-GES_DISC",
+            "issued": "2023-01-09",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ABDPEPHV3MMM",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1126/sciadv.abf7460"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "TRPSCRECOTM2D",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2005-01-01T00:00:00Z/2024-02-12T00:00:00Z",
             "theme": [
                 "TROPESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TROPESS Chemical Reanalysis Surface Total CO emissions Monthly 2-dimensional Product V1 (TRPSCRECOTM2D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NIMBUS-7/CZCS/L3M/RRS/2014",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, OB.DAAC. https://doi.org/10.5067/NIMBUS-7/CZCS/L3M/RRS/2014.",
-            "issued": "2018-02-22",
-            "temporal": "1978-10-30T00:00:00Z/1986-06-22T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "oceans",
-                "atmosphere",
-                "earth science",
-                "ocean optics",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sdps@oceancolor.gsfc.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "OB.DAAC"
-            },
-            "identifier": "C1200034493-OB_DAAC",
             "description": "The Coastal Zone Color Scanner Experiment (CZCS) was the first instrument devoted to the measurement of ocean color and flown on a spacecraft. Although other instruments flown on other spacecraft had sensed ocean color, their spectral bands, spatial resolution and dynamic range were optimized for land or meteorological use and had limited sensitivity in this area, whereas in CZCS, every parameter was optimized for use over water to the exclusion of any other type of sensing. CZCS had six spectral bands, four of which were used primarily for ocean color. These were of a 20 nanometer bandwidth centered at 443, 520, 550, and 670 nm. Band 5 had a 100 nm bandwidth centered at 750 nm and a dynamic range more suited to land. Band 6 operated in the 10.5 to 12.5 micrometer region and sensed emitted thermal radiance for derivation of equivalent black body temperature. (This thermal band failed within the first year of the mission, and so was not used in the global processing effort.) Bands 1-4 were preset to view water only and saturated when the IFOV was over most types of land surfaces, or clouds.",
-            "title": "Nimbus-7 CZCS Global Mapped Remote-Sensing Reflectance (RRS) Data, version 2014",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS-7%2FCZCS%2FL3M%2FRRS%2F2014",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS-7%2FCZCS%2FL3M%2FRRS%2F2014",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/CZCS/L3SMI/",
-                    "description": "NASA Ocean Color Web - Data Distribution Site",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Ocean Color Web - Data Distribution Site",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/directaccess/CZCS/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/docs/format/czcs_l1_spec/",
-                    "description": "CZCS Level-1A Data Users Guide",
                     "@type": "dcat:Distribution",
+                    "description": "CZCS Level-1A Data Users Guide",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/docs/format/czcs_l1_spec/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/czcs/instrument/",
-                    "description": "CZCS Instrument Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "CZCS Instrument Documentation",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/czcs/instrument/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's calibration documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NIMBUS-7/CZCS/L3M/RRS/2014",
-                    "description": "CZCS L3M Remote-Sensing Reflectance (RRS) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "CZCS L3M Remote-Sensing Reflectance (RRS) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/NIMBUS-7/CZCS/L3M/RRS/2014",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/CZCS/L3SMI/",
-                    "description": "OB.DAAC OPeNDAP Site for Nimbus-7 CZCS Standard Mapped Image (SMI) Product",
                     "@type": "dcat:Distribution",
+                    "description": "OB.DAAC OPeNDAP Site for Nimbus-7 CZCS Standard Mapped Image (SMI) Product",
+                    "downloadURL": "https://oceandata.sci.gsfc.nasa.gov/opendap/CZCS/L3SMI/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1200034493-OB_DAAC",
+            "issued": "2018-02-22",
+            "keyword": [
+                "oceans",
+                "atmosphere",
+                "earth science",
+                "ocean optics",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/NIMBUS-7/CZCS/L3M/RRS/2014",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "OB.DAAC"
+            },
             "spatial": "-180.0 90.0 -180.0 90.0",
+            "temporal": "1978-10-30T00:00:00Z/1986-06-22T23:59:59Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus-7 CZCS Global Mapped Remote-Sensing Reflectance (RRS) Data, version 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IS-40e/TEMPO/DRK_L1.003",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/IS-40e/TEMPO/DRK_L1.003.",
-            "issued": "2024-04-03",
-            "temporal": "2023-06-08T00:00:00Z/2025-01-06T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Raid Suleiman",
                 "hasEmail": "mailto:rsuleiman@cfa.harvard.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2930729926-LARC_CLOUD",
             "description": "Level 1 dark files provide the processed dark currents, corresponding to either solar irradiance measurements or radiance measurements. Each file includes the measured dark currents for all the North-South cross-track pixels. The files are provided in netCDF4 format, and contain information on dark current rates of all frames and their average for the UV and visible bands, pixel quality flags and other ancillary information. The product is produced using the image processing of L0-1b processor. These data reached provisional validation on December 9, 2024.",
-            "graphic-preview-description": "TEMPO Logo",
-            "title": "TEMPO dark exposure V03 (PROVISIONAL)",
-            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIS-40e%2FTEMPO%2FDRK_L1.003",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIS-40e%2FTEMPO%2FDRK_L1.003",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://tempo.si.edu",
-                    "description": "TEMPO project page",
                     "@type": "dcat:Distribution",
+                    "description": "TEMPO project page",
+                    "downloadURL": "http://tempo.si.edu",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/IS-40e/TEMPO/DRK_L1.003",
-                    "description": "DOI data set landing page for TEMPO_DRK_L1_V03",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TEMPO_DRK_L1_V03",
+                    "downloadURL": "https://doi.org/10.5067/IS-40e/TEMPO/DRK_L1.003",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
-                    "description": "TEMPO Logo",
                     "@type": "dcat:Distribution",
+                    "description": "TEMPO Logo",
+                    "downloadURL": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization through WORLDVIEW"
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2930729926-LARC_CLOUD",
-                    "description": "Earthdata Search for TEMPO_DRK_L1_V03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TEMPO_DRK_L1_V03 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2930729926-LARC_CLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/TEMPO",
-                    "description": "ASDC Data and Information for TEMPO",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for TEMPO",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/TEMPO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/guide/TEMPO_Level-1_user_guide_V1.2_20241204.pdf",
-                    "description": "Tropospheric Emissions: Monitoring Pollution (TEMPO) Project Level 1 Data Products: User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Tropospheric Emissions: Monitoring Pollution (TEMPO) Project Level 1 Data Products: User Guide",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tempo/guide/TEMPO_Level-1_user_guide_V1.2_20241204.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "graphic-preview-description": "TEMPO Logo",
+            "graphic-preview-file": "https://asdc.larc.nasa.gov/static/images/project_logos/tempo.png",
+            "identifier": "C2930729926-LARC_CLOUD",
+            "issued": "2024-04-03",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/IS-40e/TEMPO/DRK_L1.003",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>10.0 -170.0 10.0 -10.0 80.0 -10.0 80.0 -170.0 10.0 -170.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2023-06-08T00:00:00Z/2025-01-06T00:00:00Z",
             "theme": [
                 "TEMPO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TEMPO dark exposure V03 (PROVISIONAL)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1893",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Berner, L.T., R. Massey, and S.J. Goetz. 2021. ABoVE: Landsat Tundra Greenness and Summer Air Temperatures, Arctic Tundra, 1985-2016. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1893",
-            "issued": "2021-09-17",
-            "temporal": "1985-07-01T00:00:00Z/2016-08-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "earth science",
-                "ecosystems",
-                "land surface",
-                "land use/land cover",
-                "vegetation",
-                "atmospheric temperature",
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
-            "identifier": "C2143401680-ORNL_CLOUD",
             "description": "This dataset provides annual tundra greenness and summer air temperatures at a resolution of 50 km over the pan-Arctic tundra biome above 31.5 degrees over the time period 1985 to 2016. Annual tundra greenness was assessed using the maximum Normalized Difference Vegetation Index (NDVImax) derived from surface reflectance measured by sensors on the Landsat satellites. Summer air temperatures were quantified using the Summer Warmth Index (SWI) derived from an ensemble of five global temperature datasets. Tabular data include NDVImax, SWI, and estimates of uncertainty using Monte Carlo simulations at 45,334 vegetated sampling sites. Raster data provide (1) annual SWI from 1985 to 2016; (2) temporal trends in annual NDVImax and SWI from 1985 to 2016 and from 2000 to 2016; and (3) temporal correlations between annual NDVImax - SWI during these two periods. Each raster also includes estimates of uncertainty that were generated using Monte Carlo simulations. This dataset provides a new pan-Arctic product for assessing inter-annual variability in tundra using moderate resolution observations from the Landsat satellites.",
-            "graphic-preview-description": "Tundra greenness and summer air temperature trends and correlations across the Arctic. Top panels (a-d) depict Landsat annual maximum Normalized Difference Vegetation Index (NDVImax) trends, summer warmth index (SWI) trends derived using an ensemble of five temperature datasets, and mean Spearman's correlation (rs) between annual NDVImax and SWI among sites from 1985 to 2016, while bottom panels (e-h) depict trends and correlations from 2000 to 2016. Areas that are barren or lacked adequate Landsat data for trend and correlation assessments are shown in black. Source: Berner et al., (2020)",
-            "title": "ABoVE: Landsat Tundra Greenness and Summer Air Temperatures, Arctic Tundra, 1985-2016",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Tundra_Greeness_Temp_Trends_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1893",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1893",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Tundra_Greeness_Temp_Trends/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Tundra_Greeness_Temp_Trends/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Tundra_Greeness_Temp_Trends.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Tundra_Greeness_Temp_Trends.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1893",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1893",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Tundra_Greeness_Temp_Trends/comp/Tundra_Greeness_Temp_Trends.pdf",
-                    "description": "ABoVE: Landsat Tundra Greenness and Summer Air Temperatures, Arctic Tundra, 1985-2016: Tundra_Greeness_Temp_Trends.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Landsat Tundra Greenness and Summer Air Temperatures, Arctic Tundra, 1985-2016: Tundra_Greeness_Temp_Trends.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Tundra_Greeness_Temp_Trends/comp/Tundra_Greeness_Temp_Trends.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Tundra_Greeness_Temp_Trends_Fig1.png",
-                    "description": "Tundra greenness and summer air temperature trends and correlations across the Arctic. Top panels (a-d) depict Landsat annual maximum Normalized Difference Vegetation Index (NDVImax) trends, summer warmth index (SWI) trends derived using an ensemble of five temperature datasets, and mean Spearman's correlation (rs) between annual NDVImax and SWI among sites from 1985 to 2016, while bottom panels (e-h) depict trends and correlations from 2000 to 2016. Areas that are barren or lacked adequate Landsat data for trend and correlation assessments are shown in black. Source: Berner et al., (2020)",
                     "@type": "dcat:Distribution",
+                    "description": "Tundra greenness and summer air temperature trends and correlations across the Arctic. Top panels (a-d) depict Landsat annual maximum Normalized Difference Vegetation Index (NDVImax) trends, summer warmth index (SWI) trends derived using an ensemble of five temperature datasets, and mean Spearman's correlation (rs) between annual NDVImax and SWI among sites from 1985 to 2016, while bottom panels (e-h) depict trends and correlations from 2000 to 2016. Areas that are barren or lacked adequate Landsat data for trend and correlation assessments are shown in black. Source: Berner et al., (2020)",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Tundra_Greeness_Temp_Trends_Fig1.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://above.nasa.gov",
-                    "description": "ABoVE project site",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE project site",
+                    "downloadURL": "https://above.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Tundra greenness and summer air temperature trends and correlations across the Arctic. Top panels (a-d) depict Landsat annual maximum Normalized Difference Vegetation Index (NDVImax) trends, summer warmth index (SWI) trends derived using an ensemble of five temperature datasets, and mean Spearman's correlation (rs) between annual NDVImax and SWI among sites from 1985 to 2016, while bottom panels (e-h) depict trends and correlations from 2000 to 2016. Areas that are barren or lacked adequate Landsat data for trend and correlation assessments are shown in black. Source: Berner et al., (2020)",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Tundra_Greeness_Temp_Trends_Fig1.png",
+            "identifier": "C2143401680-ORNL_CLOUD",
+            "issued": "2021-09-17",
+            "keyword": [
+                "earth science",
+                "ecosystems",
+                "land surface",
+                "land use/land cover",
+                "vegetation",
+                "atmospheric temperature",
+                "atmosphere",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1893",
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
             "spatial": "-180.0 31.49 180.0 90.0",
+            "temporal": "1985-07-01T00:00:00Z/2016-08-31T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Landsat Tundra Greenness and Summer Air Temperatures, Arctic Tundra, 1985-2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-CR5-CRUISE5-V1.0",
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
-                "unknown"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Payload Checkout 12 (PC12) was an active checkout where a target independent opportunity to perform interactive operations and to request spacecraft pointing was given to all Rosetta payload teams. All Rosetta payload took part in this scenario The Active Payload Checkout 12 ran for 23 consecutive days starting on the 23th April 2010 until the 14th May 2010.During PC12 GIADA performs only a passive test (GD01) similar to the previous Passive Payload Checkouts. This passive test (GD01), which includes standard procedures and full functional verification, was executed by switching on Main and Redundant I/Fs in sequence and executing similar procedures for the two cases. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-cr5-cruise5-v1.0_vny9-g3zm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-GIA-2-CR5-CRUISE5-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-gia-2-cr5-cruise5-v1.0_vny9-g3zm",
-            "description": "Payload Checkout 12 (PC12) was an active checkout where a target independent opportunity to perform interactive operations and to request spacecraft pointing was given to all Rosetta payload teams. All Rosetta payload took part in this scenario The Active Payload Checkout 12 ran for 23 consecutive days starting on the 23th April 2010 until the 14th May 2010.During PC12 GIADA performs only a passive test (GD01) similar to the previous Passive Payload Checkouts. This passive test (GD01), which includes standard procedures and full functional verification, was executed by switching on Main and Redundant I/Fs in sequence and executing similar procedures for the two cases. The data reported in this data set have been converted from ADC counts to engineering values. The quality of the Housekeeping and Calibration data is good. Scientific data are due to noise, as no grain event is expected during this mission phase. These data must be only considered to evaluate GIADA behaviour and not as real scientific data. Data reported by GDS and IS are due to noise as no dust event is expected during this mission phase. MBS frequency changes, once normalised for frequency vs. temperature dependence, if present, are due to deposition of contaminants existing in the S/C environment. Housekeeping and Calibration data from all GIADA sub-systems are useful to evaluate instrument health and behaviour when compared with similar data acquired during other mission phases.",
-            "title": "ROSETTA-ORBITER CHECK GIADA 2 CR5 CRUISE5 V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CHECK GIADA 2 CR5 CRUISE5 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0694-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-06T06:28:45.000 to 2015-04-06T09:38:01.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0694-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0694-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0694-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-04-06T06:28:45.000 to 2015-04-06T09:38:01.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0694 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0694 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/935/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2015-07-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EDWARD BALABAN",
                 "hasEmail": "mailto:edward.balaban@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_935",
             "description": "The ability to utilize prognostic system health information in operational decision making, especially when fused with information about future operational, environmental, and mission requirements, is becoming desirable for both manned and unmanned aerospace vehicles. A vehicle capable of evaluating its own health state and making (or assisting the crew in making) decisions with respect to its system health evolution over time will be able to go further and accomplish more mission objectives than a vehicle fully dependent on human control. This paper describes the development of a hardware testbed for integration and testing of prognostics-enabled decision making technologies. Although the testbed is based on a planetary rover platform (K11), the algorithms being developed on it are expected to be applicable to a variety of aerospace vehicle types, from unmanned aerial vehicles and deep space probes to manned aircraft and spacecraft. A variety of injectable fault modes is being investigated for electrical, mechanical, and power subsystems of the testbed. A software simulator of the K11 has been developed, for both nominal and off-nominal operating modes, which allows prototyping and validation of algorithms prior to their deployment on hardware. The simulator can also aid in the decision-making process. The testbed is designed to have interfaces that allow reasoning software to be integrated and tested quickly, making it possible to evaluate and compare algorithms of various types and from different sources. Currently, algorithms developed (or being developed) at NASA Ames - a diagnostic system, a prognostic system, a decision-making module, a planner, and an executive - are being used to complete the software architecture and validate design of the testbed.",
-            "title": "A Mobile Robot Testbed for Prognostics-Enabled Autonomous Decision Making",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Balaban_et_al._-_2011_-_A_Mobile_Robot_Testbed_for_Prognostics-Enabled_Autonomous_Decision_Making.pdf",
-                    "description": "Balaban et al. - 2011 - A Mobile Robot Testbed for Prognostics-Enabled Autonomous Decision Making.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "Balaban et al. - 2011 - A Mobile Robot Testbed for Prognostics-Enabled Autonomous Decision Making.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/Balaban_et_al._-_2011_-_A_Mobile_Robot_Testbed_for_Prognostics-Enabled_Autonomous_Decision_Making.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Balaban et al. - 2011 - A Mobile Robot Testbed for Prognostics-Enabled Autonomous Decision Making.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_935",
+            "issued": "2015-07-31",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/935/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Mobile Robot Testbed for Prognostics-Enabled Autonomous Decision Making"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD19A1.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Alexei Lyapustin, Yujie Wang. 2022-07-06. MODIS/Terra+Aqua Land Surface BRF Daily L2G Global 500m and 1km SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD19A1.061. https://doi.org/10.5067/MODIS/MCD19A1.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2022-07-06",
-            "temporal": "2000-02-24T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-07-06",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "national geospatial data asset",
-                "surface radiative properties",
-                "ngda"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alexei Lyapustin",
                 "hasEmail": "mailto:Alexei.I.Lyapustin@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2484086031-LPCLOUD",
-            "description": "The MCD19A1 Version 6.1 data product is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Land Surface Bidirectional Reflectance Factor (BRF) gridded Level 2 product produced daily at 500 meter (m) and 1 kilometer (km) pixel resolutions. The MCD19A1 product is corrected for atmospheric gases and aerosols using a Multi-Angle Implementation of Atmospheric Correction (MAIAC)  algorithm that is based on a time series analysis and a combination of pixel- and image-based processing. The MODIS MAIAC Land Surface BRF products provide an estimate of the surface spectral reflectance as it would be measured at ground-level in the absence of atmospheric scattering or absorption.\n\nThe MCD19A1 MAIAC Surface Reflectance data product includes 31 Science Dataset (SDS) layers: surface reflectance for bands 1-12, BRF uncertainty for bands 1-2, Quality Assessment (QA) bits at 1 km, surface reflectance for bands 1-7 at 500 m, cosine of solar zenith angle, cosine of view zenith angle, relative azimuth angle, scattering angle, solar azimuth angle, view azimuth angle, glint angle, RossThick/Li-Sparse (RTLS) volumetric kernel, and RTLS geometric kernel at 5 km. A low-resolution browse image is also included showing surface reflectance band combination 1, 4, 3 created using a composite of all available orbits.\n\nEach SDS layer within each MCD19A1 Hierarchical Data Format 4 (HDF4) file contains a third dimension that represents the number of orbit overpasses. This factor could affect the total number of bands for each SDS layer.\n\nValidation at stage 1 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) has been achieved for the MCD19A1 data product. Further details regarding MODIS land product validation for MCD19 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD19).\n\nImprovements/Changes from Previous Versions\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\n* The MCD19 Version 6.1 products have added 250 m resolution bands.\n* The previous BRDF product (MCD19A3) was reported once every eight days and the new MCD19A3D is a daily product.\n* MCD19A3D introduces gap-filled NDVI and gap-filled 250 m NBAR. \n* Snow Fraction, Snow Fit, and Snow Grain size layers were moved from MCD19A1 to the MCD19A3D.\n* There are four additional Climate Modeling Grid (CMG) products: MCD19A1CMGL, MCD19A1GO, MCD19A2CMG, and MCD19A3CMG.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Alexei Lyapustin, Yujie Wang",
-            "title": "MODIS/Terra+Aqua Land Surface BRF Daily L2G Global 500m and 1km SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2563761782-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD19A1 Version 6.1 data product is a Moderate Resolution Imaging Spectroradiometer (MODIS) Terra and Aqua combined Land Surface Bidirectional Reflectance Factor (BRF) gridded Level 2 product produced daily at 500 meter (m) and 1 kilometer (km) pixel resolutions. The MCD19A1 product is corrected for atmospheric gases and aerosols using a Multi-Angle Implementation of Atmospheric Correction (MAIAC)  algorithm that is based on a time series analysis and a combination of pixel- and image-based processing. The MODIS MAIAC Land Surface BRF products provide an estimate of the surface spectral reflectance as it would be measured at ground-level in the absence of atmospheric scattering or absorption.\n\nThe MCD19A1 MAIAC Surface Reflectance data product includes 31 Science Dataset (SDS) layers: surface reflectance for bands 1-12, BRF uncertainty for bands 1-2, Quality Assessment (QA) bits at 1 km, surface reflectance for bands 1-7 at 500 m, cosine of solar zenith angle, cosine of view zenith angle, relative azimuth angle, scattering angle, solar azimuth angle, view azimuth angle, glint angle, RossThick/Li-Sparse (RTLS) volumetric kernel, and RTLS geometric kernel at 5 km. A low-resolution browse image is also included showing surface reflectance band combination 1, 4, 3 created using a composite of all available orbits.\n\nEach SDS layer within each MCD19A1 Hierarchical Data Format 4 (HDF4) file contains a third dimension that represents the number of orbit overpasses. This factor could affect the total number of bands for each SDS layer.\n\nValidation at stage 1 (https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QA_WWW/newPage.cgi?fileName=maturity) has been achieved for the MCD19A1 data product. Further details regarding MODIS land product validation for MCD19 data products are available from the MODIS Land Team Validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD19).\n\nImprovements/Changes from Previous Versions\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).\n* The MCD19 Version 6.1 products have added 250 m resolution bands.\n* The previous BRDF product (MCD19A3) was reported once every eight days and the new MCD19A3D is a daily product.\n* MCD19A3D introduces gap-filled NDVI and gap-filled 250 m NBAR. \n* Snow Fraction, Snow Fit, and Snow Grain size layers were moved from MCD19A1 to the MCD19A3D.\n* There are four additional Climate Modeling Grid (CMG) products: MCD19A1CMGL, MCD19A1GO, MCD19A2CMG, and MCD19A3CMG.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD19A1.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD19A1.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD19A1.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD19A1.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2484086031-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2484086031-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD19A1.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD19A1.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1500/MCD19_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1500/MCD19_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/111/MCD19_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/111/MCD19_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD19A1",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MCD19A1",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD19A1.006/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/MCD19A1.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 1 has been achieved for the MODIS MAIAC products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the MODIS MAIAC products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD19",
-                    "description": "Further details regarding MODIS land product validation for the MCD19 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD19 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD19",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2563761782-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2563761782-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2563761782-LPCLOUD?h=85&w=85",
+            "identifier": "C2484086031-LPCLOUD",
+            "issued": "2022-07-06",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "national geospatial data asset",
+                "surface radiative properties",
+                "ngda"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD19A1.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-07-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-24T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra+Aqua Land Surface BRF Daily L2G Global 500m and 1km SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/PTLO/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/PTLO/DATA001.",
-            "issued": "2001-09-05",
-            "temporal": "2001-09-05T20:49:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean chemistry",
-                "ocean temperature",
-                "earth science",
-                "salinity/density",
-                "oceans",
-                "ocean optics"
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
-            "identifier": "C1633360626-OB_DAAC",
             "description": "Measurements from Monterey Bay from 2001 to 2003.",
-            "title": "Measurements from Monterey Bay from 2001 to 2003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPTLO%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPTLO%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PTLO/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PTLO/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360626-OB_DAAC",
+            "issued": "2001-09-05",
+            "keyword": [
+                "ocean chemistry",
+                "ocean temperature",
+                "earth science",
+                "salinity/density",
+                "oceans",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/PTLO/DATA001",
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
+            "temporal": "2001-09-05T20:49:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements from Monterey Bay from 2001 to 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/209",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Pieper, R.D. 2014. NPP Grassland: Jornada, USA, 1970-1972, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/209",
-            "issued": "2023-08-17",
-            "temporal": "1954-01-01T00:00:00Z/1992-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "ecological dynamics",
-                "vegetation",
-                "earth science",
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
-            "identifier": "C2752582478-ORNL_CLOUD",
             "description": "This data set contains three ASCII files (.txt format). Two files contain above- and below-ground biomass and productivity data for a desert grassland in the Jornada Experimental Range, New Mexico, one file for an ungrazed treatment and the other for a light to moderately grazed treatment. The study site (32.60 N, -106.85 W, Elevation 1,350 m) is located in the Basin and Range geomorphic province at the northernmost extent of the Chihuahuan Desert, near the city of Las Cruces, New Mexico, about 60-km northwest of El Paso, Texas. The third file contains climate data for the period 1954-1992 obtained from a weather station located near the study site (32.62 N, -106.73 W, Elevation 1,300 m).Dynamics of above-and below-ground plant biomass were monitored at roughly 2-week intervals during the growing season from 1970 to 1972. Data on above-ground live biomass, recent and old dead matter, and root-crown biomass are available for one to two replications of grazed and \"ungrazed\" (relatively undisturbed) treatments. Total below-ground biomass was also sampled. Data were collected as part of a coordinated study over 1-3 years at ten grassland sites of the central and western United States, under the US GrasslandBiome Project of the International Biological Program (IBP).Annual above-ground net primary production (ANPP) was estimated, conservatively, by summing peak biomass of individual species, and annual below-ground net primary production (BNPP) estimated as the sum of positive increments in total root biomass.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Jornada, USA, 1970-1972, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F209",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F209",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_JRN/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_JRN/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_JRN.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_JRN.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/209",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/209",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_JRN/comp/NPP_JRN.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_JRN/comp/NPP_JRN.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
+            "identifier": "C2752582478-ORNL_CLOUD",
+            "issued": "2023-08-17",
+            "keyword": [
+                "ecological dynamics",
+                "vegetation",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/209",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "32.6 -106.85",
+            "temporal": "1954-01-01T00:00:00Z/1992-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Jornada, USA, 1970-1972, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD02HKM.NRT.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2017-09-10. MODIS/Terra Calibrated Radiances 5-Min L1B Swath 500 m - NRT. Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/MODIS/MOD02HKM.NRT.061. https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data.",
-            "issued": "2017-10-11",
-            "temporal": "2017-10-11T00:00:00Z/2023-07-24T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-20",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "visible wavelengths",
-                "infrared wavelengths",
-                "ngda",
-                "national geospatial data asset"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MODAPS USER SUPPORT TEAM",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/EOS/ESDIS/LANCEMODIS"
-            },
-            "identifier": "C1426415307-LANCEMODIS",
-            "description": "The 500 meter MODIS Level 1B Near Real Time (NRT) data set contains calibrated and geolocated at-aperture radiances for 7 discrete bands located in the 0.45 to 2.20 micron region of the electromagnetic spectrum. These data are generated from the MODIS Level 1A scans of raw radiance and in the process converted to geophysical units of W/(m^2 um sr). Additional data are provided including quality flags, error estimates and calibration data.\n\nVisible, shortwave infrared, and near infrared measurements are only made during the daytime (except band 26), while radiances for the thermal infrared region (bands 20-25, 27-36) are measured continuously.\nChannel locations for the MODIS 500 meter data are as follows:\n            \n            Band   Center Wavelength (um)    Primary Use\n            ----   ----------------------    -----------\n            1          0.620  - 0.670        Land/Cloud Boundaries\n            2          0.841  - 0.876        Land/Cloud Boundaries\n            3          0.459  - 0.479        Land/Cloud Properties\n            4          0.545  - 0.565        Land/Cloud Properties\n            5          1.230  - 1.250        Land/Cloud Properties\n            6          1.628  - 1.652        Land/Cloud Properties\n            7          2.105  - 2.155        Land/Cloud Properties\n            \nChannels 1 and 2 have 250 m resolution, channels 3 through 7 have 500 m resolution. However, for the MODIS L1B 500 m product, the 250 m band radiance data and their associated uncertainties have been aggregated to 500m resolution. Thus the entire channel data set has been co-registered to the same spatial scale in the 500 m product. Separate L1B products are available for the 250 m resolution channels (MOD02QKM) and 1 km resolution channels (MOD021KM). For the latter product, the 250 m and 500 m channel data (bands 1 through 7) have been aggregated into equivalent 1 km pixel values.\n            \nSpatial resolution for pixels at nadir is 500 km, degrading to 2.4 km in the along-scan direction at the scan extremes. However, thanks to the overlapping of consecutive swaths and respectively pixels there, the resulting resolution at the scan extremes is about 1 km. A 55 degree scanning pattern at the EOS orbit of 705 km results in a 2330 km orbital swath width and provides global coverage every one to two days. A single MODIS Level 1B 500 m granule will contain a scene built from 203 scans sampled 2708 times in the cross-track direction, corresponding to approximately 5 minutes worth of data; thus 288 granules will be produced per day. Since an individual MODIS scan will contain 20 along-track spatial elements for the 500 m channels, the scene will be composed of (2708 x 4060) pixels, resulting in a spatial coverage of (2330 km x 2040 km). Due to the MODIS scan geometry, there will be increasing scan overlap beyond about 20 degrees scan angle.      \n\nTo summarize, the MODIS L1B 500 m data product consists of:\n            \n1. Calibrated radiances, uncertainties and number of samples for (2) 250 m reflected solar bands aggregated to 500 m resolution\n            \n2. Calibrated radiances and uncertainties for (5) 500 m reflected solar bands\n            \n3. Geolocation for 1km pixels, that must be interpolated to get 500 m pixel locations. For the relationship of 1km pixels to 500m pixels, see the Geolocation ATBD ttp://modis.gsfc.nasa.gov/data/atbd/atbd_mod28_v3.pdf .\n            \n4. Calibration data for all channels (scale and offset) \n            \n5. Comprehensive set of file-level metadata summarizing the spatial, temporal and parameter attributes of the data, as well as auxiliary information pertaining to instrument status and data quality characterization Users requiring all geolocation and solar/satellite geometry fields at 1km resolution can obtain the separate MODIS Level 1 Geolocation product (MOD03) from LAADS  http://ladsweb.nascom.nasa.gov/ . \n            \nThe Shortname for this product is MOD02HKM and is stored in the Earth Ob",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Terra Calibrated Radiances 5-Min L1B Swath 500m - NRT",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The 500 meter MODIS Level 1B Near Real Time (NRT) data set contains calibrated and geolocated at-aperture radiances for 7 discrete bands located in the 0.45 to 2.20 micron region of the electromagnetic spectrum. These data are generated from the MODIS Level 1A scans of raw radiance and in the process converted to geophysical units of W/(m^2 um sr). Additional data are provided including quality flags, error estimates and calibration data.\n\nVisible, shortwave infrared, and near infrared measurements are only made during the daytime (except band 26), while radiances for the thermal infrared region (bands 20-25, 27-36) are measured continuously.\nChannel locations for the MODIS 500 meter data are as follows:\n            \n            Band   Center Wavelength (um)    Primary Use\n            ----   ----------------------    -----------\n            1          0.620  - 0.670        Land/Cloud Boundaries\n            2          0.841  - 0.876        Land/Cloud Boundaries\n            3          0.459  - 0.479        Land/Cloud Properties\n            4          0.545  - 0.565        Land/Cloud Properties\n            5          1.230  - 1.250        Land/Cloud Properties\n            6          1.628  - 1.652        Land/Cloud Properties\n            7          2.105  - 2.155        Land/Cloud Properties\n            \nChannels 1 and 2 have 250 m resolution, channels 3 through 7 have 500 m resolution. However, for the MODIS L1B 500 m product, the 250 m band radiance data and their associated uncertainties have been aggregated to 500m resolution. Thus the entire channel data set has been co-registered to the same spatial scale in the 500 m product. Separate L1B products are available for the 250 m resolution channels (MOD02QKM) and 1 km resolution channels (MOD021KM). For the latter product, the 250 m and 500 m channel data (bands 1 through 7) have been aggregated into equivalent 1 km pixel values.\n            \nSpatial resolution for pixels at nadir is 500 km, degrading to 2.4 km in the along-scan direction at the scan extremes. However, thanks to the overlapping of consecutive swaths and respectively pixels there, the resulting resolution at the scan extremes is about 1 km. A 55 degree scanning pattern at the EOS orbit of 705 km results in a 2330 km orbital swath width and provides global coverage every one to two days. A single MODIS Level 1B 500 m granule will contain a scene built from 203 scans sampled 2708 times in the cross-track direction, corresponding to approximately 5 minutes worth of data; thus 288 granules will be produced per day. Since an individual MODIS scan will contain 20 along-track spatial elements for the 500 m channels, the scene will be composed of (2708 x 4060) pixels, resulting in a spatial coverage of (2330 km x 2040 km). Due to the MODIS scan geometry, there will be increasing scan overlap beyond about 20 degrees scan angle.      \n\nTo summarize, the MODIS L1B 500 m data product consists of:\n            \n1. Calibrated radiances, uncertainties and number of samples for (2) 250 m reflected solar bands aggregated to 500 m resolution\n            \n2. Calibrated radiances and uncertainties for (5) 500 m reflected solar bands\n            \n3. Geolocation for 1km pixels, that must be interpolated to get 500 m pixel locations. For the relationship of 1km pixels to 500m pixels, see the Geolocation ATBD ttp://modis.gsfc.nasa.gov/data/atbd/atbd_mod28_v3.pdf .\n            \n4. Calibration data for all channels (scale and offset) \n            \n5. Comprehensive set of file-level metadata summarizing the spatial, temporal and parameter attributes of the data, as well as auxiliary information pertaining to instrument status and data quality characterization Users requiring all geolocation and solar/satellite geometry fields at 1km resolution can obtain the separate MODIS Level 1 Geolocation product (MOD03) from LAADS  http://ladsweb.nascom.nasa.gov/ . \n            \nThe Shortname for this product is MOD02HKM and is stored in the Earth Ob",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD02HKM.NRT.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD02HKM.NRT.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/modis-nrt",
-                    "description": "NASA LANCE Near Real Time data set descriptions and access links.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA LANCE Near Real Time data set descriptions and access links.",
+                    "downloadURL": "https://earthdata.nasa.gov/earth-observation-data/near-real-time/download-nrt-data/modis-nrt",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LANCE"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
-                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page(download server).",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data set from the MODAPS LANCE-MODIS page(download server).",
+                    "downloadURL": "http://lance3.modaps.eosdis.nasa.gov/data_products/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD02HKM/",
-                    "description": "Direct access to the download site and directory hosting the MOD02HKM C6.1 NRT data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to the download site and directory hosting the MOD02HKM C6.1 NRT data set.",
+                    "downloadURL": "https://nrt3.modaps.eosdis.nasa.gov/archive/allData/61/MOD02HKM/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through MODAPS"
                 }
             ],
+            "identifier": "C1426415307-LANCEMODIS",
+            "issued": "2017-10-11",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "visible wavelengths",
+                "infrared wavelengths",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD02HKM.NRT.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/EOS/ESDIS/LANCEMODIS"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2017-10-11T00:00:00Z/2023-07-24T00:00:00Z",
             "theme": [
                 "DODS",
                 "EOSDIS",
@@ -1527996,204 +1527997,205 @@
                 "TERRA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Calibrated Radiances 5-Min L1B Swath 500m - NRT"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-PLUTOCRUISE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-plutocruise-v1.0_vpdi-iwjy",
+            "issued": "2018-09-05",
+            "keyword": [
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-PLUTOCRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-plutocruise-v1.0_vpdi-iwjy",
-            "description": "This data set contains Calibrated data taken by the New Horizons         Pluto Energetic Particle Spectrometer Science Investigation            instrument during the                                                    pluto cruise                                                           mission phase.  This is VERSION 1.0 of this data set.",
-            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO CRUISE                                                     \n      CALIBRATED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS                            \n      PEPSSI PLUTO CRUISE                                                     \n      CALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIDAS-3-CVP-FULL-V3.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCOMMISSIONING mission phase. This release supersedes version 1.0. Version 2.0 was never generated\nfor pre-comet phases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-midas-3-cvp-full-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIDAS-3-CVP-FULL-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-midas-3-cvp-full-v3.0",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the\nROSETTA Orbiter that will provide 3D images and statistical parameters\nof pristine cometary particles, collected in the vicinity of comet\n67P/Churyumov-Gerasimenko. This data set includes all data from the\nCOMMISSIONING mission phase. This release supersedes version 1.0. Version 2.0 was never generated\nfor pre-comet phases.",
-            "title": "ROSETTA-ORBITER CAL MIDAS 3 CVP FULL V3.0",
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
+            "title": "ROSETTA-ORBITER CAL MIDAS 3 CVP FULL V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/379",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bubier, J.L., P.M. Crill, R.K. Varner, and T.R. Moore. 1998. BOREAS TGB-01/TGB-03 NEE Data over the NSA Fen. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/379",
-            "issued": "2023-11-22",
-            "temporal": "1994-06-06T00:00:00Z/1996-10-23T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-28",
-            "keyword": [
-                "atmosphere",
-                "vegetation",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
-                "atmospheric chemistry"
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
-            "identifier": "C2808131414-ORNL_CLOUD",
             "description": "Contains TGB-03 NET Ecosystem Exchange data from the combined TGB-01 and TGB-03 teams.",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS TGB-01/TGB-03 NEE Data over the NSA Fen",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F379",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F379",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgbfenne/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/TGB/tgbfenne/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB01_TGB03_NEE.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/TGB01_TGB03_NEE.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/379",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/379",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenne/comp/TGB01_TGB03_NEE.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenne/comp/TGB01_TGB03_NEE.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenne/comp/TGB01_TGB03_NEE.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenne/comp/TGB01_TGB03_NEE.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenne/comp/TGB01_TGB03_NEE.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenne/comp/TGB01_TGB03_NEE.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenne/comp/tgbfenne.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/TGB/tgbfenne/comp/tgbfenne.def",
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
+            "identifier": "C2808131414-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "atmosphere",
+                "vegetation",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/379",
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
             "spatial": "55.92 -98.42",
+            "temporal": "1994-06-06T00:00:00Z/1996-10-23T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS TGB-01/TGB-03 NEE Data over the NSA Fen"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-METEORITE-SPECTRA-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Laboratory spectra of meteorite samples, obtained by M. J. Gaffey.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-meteorite-spectra-v2.0_vppn-d6um",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "farmington",
                 "elenovka",
@@ -1528302,280 +1528304,256 @@
                 "alais",
                 "abee"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-3-RDR-METEORITE-SPECTRA-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-3-rdr-meteorite-spectra-v2.0_vppn-d6um",
-            "description": "Laboratory spectra of meteorite samples, obtained by M. J. Gaffey.",
-            "title": "GAFFEY METEORITE SPECTRA V2.0",
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
+            "title": "GAFFEY METEORITE SPECTRA V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/148",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Knapp, A.K., and D.S. Ojima. 2014. NPP Grassland: Konza Prairie, USA, 1984-1990, R1 . ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/148",
-            "issued": "2014-08-19",
-            "temporal": "1891-01-01T00:00:00Z/1998-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
-            "keyword": [
-                "biosphere",
-                "vegetation",
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
-            "identifier": "C2751937858-ORNL_CLOUD",
             "description": "This data set contains three ASCII files (.txt format). Two files contain above-ground biomass and productivity data for a humid temperate tall-grass prairie grassland located in the Konza Prairie Natural Research Area, Kansas. One file provides data for an unburned treatment and the other for a burned treatment for 1975 to 1990. The third file contains climate data for the period 1891-1988 obtained from a weather station at Konza. The above-ground net primary productivity measurement presented here (394 g/m2/year) is a 10-year average (1975-1984) based on peak seasonal live biomass values averaged for burned and unburned lowland and upland grasslands. The Konza study site (39.10 N, - 96.61 W, Elevation 400 m) is situated near the town of Manhattan in north-eastern Kansas, about 170-km west of Kansas City. The Konza research program is built upon a long-term database on ecological pattern and process data derived from a fully replicated watershed-level experimental design, in place at the Konza Prairie Biological Station since 1977. This design includes replicate watersheds subject to different fire and grazing treatments. Within the watersheds, permanent sampling transects are replicated at various topographic positions, where plant species composition, plant and consumer populations, above-ground net primary production (ANPP), soil properties, and other key above- and below-ground processes are measured. In addition to these watershed-level studies, the Konza Long Term Ecological Research (LTER) program includes a number of long-term plot-level experiments.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Grassland: Konza Prairie, USA, 1984-1990, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F148",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F148",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_KNZ/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/grassland/NPP_KNZ/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_KNZ.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_KNZ.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/148",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/148",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_KNZ/comp/NPP_KNZ.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/grassland/NPP_KNZ/comp/NPP_KNZ.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
+            "identifier": "C2751937858-ORNL_CLOUD",
+            "issued": "2014-08-19",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "ecological dynamics",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/148",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "39.1 -96.61",
+            "temporal": "1891-01-01T00:00:00Z/1998-12-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Grassland: Konza Prairie, USA, 1984-1990, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-ESC1-NEL-V1.0",
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
+            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the COMET ESCORT 1 mission\nphase where the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1\n(1969 R1). It contains electron density at higher time resolution than\nin the DERIV2 data sets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-esc1-nel-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-5-ESC1-NEL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-5-esc1-nel-v1.0",
-            "description": "This data set contains DERIVED\ndata from Rosetta RPC-LAP, acquired during the COMET ESCORT 1 mission\nphase where the primary target was the comet 67P/CHURYUMOV-GERASIMENKO 1\n(1969 R1). It contains electron density at higher time resolution than\nin the DERIV2 data sets.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nESC1 NEL V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RPCLAP 5\nESC1 NEL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/PERU/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/PERU/DATA001.",
-            "issued": "2003-05-27",
-            "temporal": "2003-05-27T16:08:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "earth science",
-                "ocean optics",
-                "salinity/density",
-                "ocean chemistry",
-                "oceans",
-                "ocean temperature"
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
-            "identifier": "C1633360594-OB_DAAC",
             "description": "Measurements made along the northern coast of Peru in 2003.",
-            "title": "Optical measurements along the northern coast of Peru in 2003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPERU%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPERU%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PERU/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PERU/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360594-OB_DAAC",
+            "issued": "2003-05-27",
+            "keyword": [
+                "earth science",
+                "ocean optics",
+                "salinity/density",
+                "ocean chemistry",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/PERU/DATA001",
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
+            "temporal": "2003-05-27T16:08:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Optical measurements along the northern coast of Peru in 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0209-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-15T13:42:05.000 to 2014-08-15T19:01:29.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0209-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0209-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0209-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-15T13:42:05.000 to 2014-08-15T19:01:29.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0209 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0209 V1.0"
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
-                "incompressible",
-                "turbulence",
-                "cases",
-                "flow",
-                "models"
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
-            "identifier": "NASA-844__20",
             "description": "This grouping contains the incompressible-flow cases from the 1980-81 Data Library.",
-            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1528583,44 +1528561,45 @@
                     "mediaType": "application/txt"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-844__20",
+            "issued": "2018-06-25",
+            "keyword": [
+                "incompressible",
+                "turbulence",
+                "cases",
+                "flow",
+                "models"
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
+            "title": "Collaborative Testing of Turbulence Models: Incompressible Flow Cases from 1980-81 Data Library"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://appel.nasa.gov/ask-academy/ask-the-academy-past-issues/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://km.nasa.gov/knowledge-map/"
-            ],
-            "keyword": [
-                "sharing",
-                "appel",
-                "knowledge",
-                "ask the academy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ed Hoffman",
                 "hasEmail": "mailto:ehoffman@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-862__48",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1528628,448 +1528607,483 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__48",
+            "issued": "2018-06-25",
+            "keyword": [
+                "sharing",
+                "appel",
+                "knowledge",
+                "ask the academy"
+            ],
+            "landingPage": "http://appel.nasa.gov/ask-academy/ask-the-academy-past-issues/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://km.nasa.gov/knowledge-map/"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-SCE-4-SUMM-RANGING-10MIN-V1.0",
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
-                "ulysses"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Ulysses spacecraft was occulted by the Io Plasma Torus (IPT) during its Jupiter encounter on 8 February 1992. The Ulysses dual-frequency radio subsystem used by the Ulysses Solar Corona Experiment (SCE) was utilized to measure the electron content (column density) of the IPT [BIRDETAL1992B]. In the nominal mode for radio-sounding observations [BIRDETAL1992A], both downlinks (S-band: f_s = 2.3 GHz X-band: f_x = 8.4 GHz) are phase coherent with the uplink (S-band: f_u = 2.1 GHz). The dual-frequency radio-sounding technique exploits the dispersive nature of ionized media on the propagation of the two downlinks. The tiny Doppler shift due to plasma moving in and out of the ray path is greater at S-band than at the higher frequency X-band.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-sce-4-summ-ranging-10min-v1.0_vpvx-imbb",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-SCE-4-SUMM-RANGING-10MIN-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-sce-4-summ-ranging-10min-v1.0_vpvx-imbb",
-            "description": "The Ulysses spacecraft was occulted by the Io Plasma Torus (IPT) during its Jupiter encounter on 8 February 1992. The Ulysses dual-frequency radio subsystem used by the Ulysses Solar Corona Experiment (SCE) was utilized to measure the electron content (column density) of the IPT [BIRDETAL1992B]. In the nominal mode for radio-sounding observations [BIRDETAL1992A], both downlinks (S-band: f_s = 2.3 GHz X-band: f_x = 8.4 GHz) are phase coherent with the uplink (S-band: f_u = 2.1 GHz). The dual-frequency radio-sounding technique exploits the dispersive nature of ionized media on the propagation of the two downlinks. The tiny Doppler shift due to plasma moving in and out of the ray path is greater at S-band than at the higher frequency X-band.",
-            "title": "ULYSSES JUPITER SOLAR CORONA EXPER. RANGING DATA 10 MIN AVG",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULYSSES JUPITER SOLAR CORONA EXPER. RANGING DATA 10 MIN AVG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1626189761-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MISR Science Team (2007), Terra/MISR Level 1, Terrain Product subset for the VBBE region, version 3, Hampton, VA, USA: NASA Atmospheric Science Data Center (ASDC), Accessed <author citing data inserts date here> at doi: TBD",
-            "issued": "2019-07-25",
-            "temporal": "2007-08-07T02:05:48.503Z/2007-09-13T05:00:26.136Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-07-25",
-            "keyword": [
-                "earth science",
-                "visible wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Veljko Jovanovic",
                 "hasEmail": "mailto:veljko.m.jovanovic@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1626189761-LARC",
             "description": "Multi-angle Imaging SpectroRadiometer (MISR) is an instrument designed to view Earth with cameras pointed in 9 different directions. As the instrument flies overhead, each piece of Earth's surface below is successively imaged by all 9 cameras, in each of 4 wavelengths (blue, green, red, and near-infrared). The goal of MISR is to improve our understanding of the fate of sunlight in Earth environment, as well as distinguish different types of clouds, particles and surfaces. Specifically, MISR monitors the monthly, seasonal, and long-term trends in three areas: 1) amount and type of atmospheric particles (aerosols), including those formed by natural sources and by human activities; 2) amounts, types, and heights of clouds, and 3) distribution of land surface cover, including vegetation canopy structure. MISR Level 1B2 Terrain Product subset for the VBBE region V003 contains Terrain-projected TOA Radiance, resampled at the surface and topographically corrected, as well as geometrically corrected by PGE22.",
-            "title": "MISR Level 1B2 Terrain Product subset for the VBBE region V003",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1626189761-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1626189761-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1626189761-LARC",
+            "issued": "2019-07-25",
+            "keyword": [
+                "earth science",
+                "visible wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1626189761-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-07-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2007-08-07T02:05:48.503Z/2007-09-13T05:00:26.136Z",
             "theme": [
                 "VBBE_2007",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR Level 1B2 Terrain Product subset for the VBBE region V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-A-FPA-3-RDR-IMPS-V5.0",
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
-                "infrared astronomical satellite",
-                "asteroid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Derived diameters and albedoes of asteroids, plus associated data on sighting and non-sightings, extracted from the IRAS archives.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-a-fpa-3-rdr-imps-v5.0_vpxm-zygs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "infrared astronomical satellite",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IRAS-A-FPA-3-RDR-IMPS-V5.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.iras-a-fpa-3-rdr-imps-v5.0_vpxm-zygs",
-            "description": "Derived diameters and albedoes of asteroids, plus associated data on sighting and non-sightings, extracted from the IRAS archives.",
-            "title": "IRAS MINOR PLANET SURVEY ASTEROIDS V5.0",
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
+            "title": "IRAS MINOR PLANET SURVEY ASTEROIDS V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC2-RAW-V6.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nCOMET ESCORT 2 Phase  (ESC2) from March 11 until June 30, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc2-raw-v6.0_vpye-gu3j",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC2-RAW-V6.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc2-raw-v6.0_vpye-gu3j",
-            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nCOMET ESCORT 2 Phase  (ESC2) from March 11 until June 30, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC2 RAW V6.0",
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
+            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC2 RAW V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSCN-3-EDR-HALLEY-V1.0",
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
-                "halley",
-                "international halley watch"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Radio Studies Continuum Subnetwork has one data file stored as a 2-d array for 1986 April 12.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rscn-3-edr-halley-v1.0_vpzr-2ai4",
+            "issued": "2018-06-26",
+            "keyword": [
+                "halley",
+                "international halley watch"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-RSCN-3-EDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-rscn-3-edr-halley-v1.0_vpzr-2ai4",
-            "description": "NASA's International Halley Watch (IHW) has created a Comet Halley Archive. The collection of data spans the full wavelength range as submitted by scientists to the IHW. The observations belong to one of the following Disciplines: Amateur, Astrometry, Infrared Studies, Large-Scale Phenomena, Meteor Studies, Near-Nucleus Studies, Photometry and Polarimetry, Radio Studies, and Spectroscopy and Spectrophotometry. The data collected by these nine disciplines were augmented by Spacecraft measurements. The data were submitted to IHW, but the evaluation and selection for the Archive has been the primary responsibility of the Discipline Specialist Teams for each network in cooperation with the Lead Center. The data from the Radio Studies Continuum Subnetwork has one data file stored as a 2-d array for 1986 April 12.",
-            "title": "IHW COMET HALLEY RADIO CONTINUUM ARRAY DATA V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY RADIO CONTINUUM ARRAY DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GFOCN-3C634",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Felix Landerer. 2024-10-01. CSR TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly. Version RL06.3v04. CSR TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GFOCN-3C634.",
-            "issued": "2023-10-02",
-            "temporal": "2018-05-22T00:00:00Z/2024-10-14T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-02",
-            "keyword": [
-                "ocean pressure",
-                "earth science",
-                "oceans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C3193289116-POCLOUD",
-            "description": "This data set is produced by the Center for Space Research (CSR) GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the ocean bottom pressure (OBP) anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents sea floor pressure changes due to the integral effect of ocean and atmosphere processes, including global mean ocean bottom pressure changes (mean ocean mass and mean atmosphere mass over the global oceans). A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. \n<br><br>\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the ocean bottom pressure data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this release 06.3 is an updated version of the Level 3 products in coordination with the release of the analogous Level 2 products used to generate them. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
-            "release-place": "PO.DAAC",
-            "series-name": "CSR TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Felix Landerer",
-            "title": "CSR TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_CSR_RL06_OCN_v04.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This data set is produced by the Center for Space Research (CSR) GRACE-FO (Gravity Recovery and Climate Experiment Follow-On) program and derives the ocean bottom pressure (OBP) anomaly given as equivalent water thickness. These monthly grids are derived from GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. This quantity represents sea floor pressure changes due to the integral effect of ocean and atmosphere processes, including global mean ocean bottom pressure changes (mean ocean mass and mean atmosphere mass over the global oceans). A glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters have been applied to reduce correlated errors. Data grids are provided in ASCII/netCDF/GeoTIFF formats. \n<br><br>\nGRACE-FO was launched on 22 May 2018, and extends the original GRACE mission (2002 \u2013 2017) and expands its legacy of scientific achievements in tracking earth surface mass changes. Version 04 (v04) of the ocean bottom pressure data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Additionally, this release 06.3 is an updated version of the Level 3 products in coordination with the release of the analogous Level 2 products used to generate them. It differs from RL06.1 only in the Level-1B accelerometer transplant data that is used for the GF2 (GRACE-FO 2) satellite; see respective L-2 data descriptions. RL06.3 uses the ACX2-L1B data products. All GRACE-FO RL06.3 Level-3 fields are fully compatible with the GRACE RL06 data.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFOCN-3C634",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGFOCN-3C634",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
-                    "description": "GRACE-FO Project Website (external to PO.DAAC)",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE-FO Project Website (external to PO.DAAC)",
+                    "downloadURL": "https://gracefo.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
-                    "description": "PODAAC GRACE-FO Mission-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC GRACE-FO Mission-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L3_Handbook_JPL.pdf",
-                    "description": "User guidance documentation for this dataset",
                     "@type": "dcat:Distribution",
+                    "description": "User guidance documentation for this dataset",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L3_Handbook_JPL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_CSR_RL06_OCN_v04.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_CSR_RL06_OCN_v04.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193289116-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3193289116-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193289116-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3193289116-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
-                    "description": "Page that includes all GRACE-FO Documentation and Technical Notes",
                     "@type": "dcat:Distribution",
+                    "description": "Page that includes all GRACE-FO Documentation and Technical Notes",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRFO_L3_CSR_RL06_OCN_v04.jpg",
+            "identifier": "C3193289116-POCLOUD",
+            "issued": "2023-10-02",
+            "keyword": [
+                "ocean pressure",
+                "earth science",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/GFOCN-3C634",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "PO.DAAC",
+            "series-name": "CSR TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly",
             "spatial": "-180.0 -89.5 180.0 89.5",
+            "temporal": "2018-05-22T00:00:00Z/2024-10-14T00:00:00Z",
             "theme": [
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CSR TELLUS GRACE-FO Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.3 version 04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP15A2H.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ranga Myneni. 2023-08-21. VIIRS/NPP Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VNP15A2H.002. https://doi.org/10.5067/VIIRS/VNP15A2H.002. This data set was provided by the NASA/NOAA NPP Project..",
-            "issued": "2023-08-21",
-            "temporal": "2012-01-01T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-21",
-            "keyword": [
-                "earth science",
-                "biosphere",
-                "vegetation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ranga Myneni",
                 "hasEmail": "mailto:rmyneni@bu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2545314545-LPCLOUD",
-            "description": "The Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Leaf Area Index (LAI) and Fraction of Photosynthetically Active Radiation (FPAR) Version 2 data product (VNP15A2H) provides information about the vegetative canopy layer at 500 meter resolution. The VIIRS sensor is located aboard the NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) satellite. LAI is an index that quantifies the one-sided leaf area of a canopy, while FPAR is the fraction of incoming solar energy absorbed through photosynthesis at 400 to 700 nanometers. This product is intentionally designed after the Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) LAI/FPAR operational algorithm to promote the continuity of the Earth Observation System (EOS) mission.\r\n\r\nThe VNP15A2H product includes six Science Data Set Layers for the analysis of key factors in LAI/FPAR measurements. These include the LAI and FPAR measurements, quality detail for LAI/FPAR, extra quality detail for FPAR, and the standard deviation for LAI and FPAR. Two low resolution browse images are also available for each VNP15A2H granule: LAI and FPAR.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Ranga Myneni",
-            "title": "VIIRS/NPP Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V002",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2746588255-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Leaf Area Index (LAI) and Fraction of Photosynthetically Active Radiation (FPAR) Version 2 data product (VNP15A2H) provides information about the vegetative canopy layer at 500 meter resolution. The VIIRS sensor is located aboard the NASA/NOAA Suomi National Polar-orbiting Partnership (Suomi NPP) satellite. LAI is an index that quantifies the one-sided leaf area of a canopy, while FPAR is the fraction of incoming solar energy absorbed through photosynthesis at 400 to 700 nanometers. This product is intentionally designed after the Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) LAI/FPAR operational algorithm to promote the continuity of the Earth Observation System (EOS) mission.\r\n\r\nThe VNP15A2H product includes six Science Data Set Layers for the analysis of key factors in LAI/FPAR measurements. These include the LAI and FPAR measurements, quality detail for LAI/FPAR, extra quality detail for FPAR, and the standard deviation for LAI and FPAR. Two low resolution browse images are also available for each VNP15A2H granule: LAI and FPAR.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP15A2H.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP15A2H.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314545-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314545-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QS/new/index.cgi",
-                    "description": "The LDOPE Land Product Quality Assessment website provides known issues, maneuvers, and product quality of the land products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LDOPE Land Product Quality Assessment website provides known issues, maneuvers, and product quality of the land products.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QS/new/index.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP15A2H.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP15A2H.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/126/VNP15_User_Guide.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/126/VNP15_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/125/VNP15_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/125/VNP15_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2746588255-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2746588255-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LAI_Fpar_Val.html",
-                    "description": "Validation at stage 1 has been achieved for the VIIRS LAI/FPAR product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the VIIRS LAI/FPAR product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LAI_Fpar_Val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val_overview.html",
-                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val_overview.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2746588255-LPCLOUD?h=85&w=85",
+            "identifier": "C2545314545-LPCLOUD",
+            "issued": "2023-08-21",
+            "keyword": [
+                "earth science",
+                "biosphere",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP15A2H.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-21",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-01T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/vqb8-588u",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Spaceflight imposes numerous adaptive challenges for terrestrial life. The reduction in gravity or microgravity represents a novel environment that can disrupt homeostasis of many physiological processes. Additionally it is becoming increasingly clear that an organism  s microbiome is critical for host health and examining its resiliency in microgravity represents a new frontier for space biology research. In this study we examine the impact of microgravity on the interactions between the squid Euprymna scolopes and its beneficial symbiont Vibrio fischeri which form a highly specific binary mutualism. First animals inoculated with V. fischeri aboard the space shuttle showed effective colonization of the host light organ the site of the symbiosis during spaceflight. Second RNA-Seq analysis of squid exposed to modeled microgravity conditions exhibited extensive differential gene expression in the presence and absence of the symbiotic partner. Transcriptomic analyses revealed in the absence of the symbiont during modeled microgravity there was an enrichment of genes and pathways associated with the innate immune and oxidative stress response. The results suggest that V. fischeri may help modulate the host stress responses under modeled microgravity. This study provides a window into the adaptive responses that the host animal and its symbiont use during modeled microgravity.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-119",
+                    "mediaType": "text/html",
+                    "title": "Effect of microgravity on an animal-bacteria symbiosis"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-119_vqb8-588u",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "sequence analysis data transformation",
                 "nucleic acid sequencing",
@@ -1529078,84 +1529092,72 @@
                 "sample collection",
                 "simulated microgravity"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/vqb8-588u",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-119_vqb8-588u",
-            "description": "Spaceflight imposes numerous adaptive challenges for terrestrial life. The reduction in gravity or microgravity represents a novel environment that can disrupt homeostasis of many physiological processes. Additionally it is becoming increasingly clear that an organism  s microbiome is critical for host health and examining its resiliency in microgravity represents a new frontier for space biology research. In this study we examine the impact of microgravity on the interactions between the squid Euprymna scolopes and its beneficial symbiont Vibrio fischeri which form a highly specific binary mutualism. First animals inoculated with V. fischeri aboard the space shuttle showed effective colonization of the host light organ the site of the symbiosis during spaceflight. Second RNA-Seq analysis of squid exposed to modeled microgravity conditions exhibited extensive differential gene expression in the presence and absence of the symbiotic partner. Transcriptomic analyses revealed in the absence of the symbiont during modeled microgravity there was an enrichment of genes and pathways associated with the innate immune and oxidative stress response. The results suggest that V. fischeri may help modulate the host stress responses under modeled microgravity. This study provides a window into the adaptive responses that the host animal and its symbiont use during modeled microgravity.",
-            "title": "Effect of microgravity on an animal-bacteria symbiosis",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-119",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Effect of microgravity on an animal-bacteria symbiosis"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Effect of microgravity on an animal-bacteria symbiosis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-AIS-EXT2-V1.0",
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
-                "mars express",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Mars Express MARSIS Active Ionospheric Sounder (AIS) full resolution data set includes all spectral information calibrated in units of spectral density for the entire Mars Express nominal mission.  The data set consists of a transmit frequency followed by a time series of spectral density measurements of the received power.  Browse products contain a spectrogram overview plot and individual ionograms for each sounding  activity.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ais-ext2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-3-RDR-AIS-EXT2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-3-rdr-ais-ext2-v1.0",
-            "description": "The Mars Express MARSIS Active Ionospheric Sounder (AIS) full resolution data set includes all spectral information calibrated in units of spectral density for the entire Mars Express nominal mission.  The data set consists of a transmit frequency followed by a time series of spectral density measurements of the received power.  Browse products contain a spectrogram overview plot and individual ionograms for each sounding  activity.",
-            "title": "MARS EXPRESS MARSIS RDR ACTIVE IONOSPHERE SOUNDING EXT2 V1.0",
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
+            "title": "MARS EXPRESS MARSIS RDR ACTIVE IONOSPHERE SOUNDING EXT2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-3-EAR3-EARTHSWINGBY3-V1.2",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the EARTH SWING-BY 3 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-3-ear3-earthswingby3-v1.2",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "vega",
                 "moon",
@@ -1529166,243 +1529168,255 @@
                 "checkout",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-3-EAR3-EARTHSWINGBY3-V1.2",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-3-ear3-earthswingby3-v1.2",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the EARTH SWING-BY 3 mission phase",
-            "title": "ROSETTA-ORBITER EARTH SWING-BY 3 OSINAC 3 RDR data",
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
+            "title": "ROSETTA-ORBITER EARTH SWING-BY 3 OSINAC 3 RDR data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0424-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-19. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-12T07:00:45.000 to 2014-11-12T11:04:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0424-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0424-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0424-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-19. It is a Global Gravity measurement at the comet 67P and covers the time 2014-11-12T07:00:45.000 to 2014-11-12T11:04:59.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0424 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0424 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/760",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lloyd, J., O. Kolle, E.M. Veenendaal, A. Arneth, and P. Wolski. 2004. SAFARI 2000 Meteorological and Flux Tower Measurements in Maun, Botswana, 2000. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/760",
-            "issued": "2023-10-18",
-            "temporal": "2000-02-01T00:00:00Z/2000-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-24",
-            "keyword": [
-                "atmospheric radiation",
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "vegetation",
-                "surface radiative properties",
-                "biosphere",
-                "soils",
-                "precipitation",
-                "land surface",
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
-            "identifier": "C2789038485-ORNL_CLOUD",
             "description": "To investigate potential contributions of savanna ecosystems to the Earth's carbon balance, an eddy covariance system was used to measure the seasonal variation in carbon dioxide, water vapor, and energy flux at the Maun micrometerological tower site in a broadleaf semi-arid savanna in Southern Africa, approximately 20 km east of Maun in northeastern Botswana.",
-            "graphic-preview-description": "Browse Image",
-            "title": "SAFARI 2000 Meteorological and Flux Tower Measurements in Maun, Botswana, 2000",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/safari_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F760",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F760",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/climate_meteorology/maun_met_flux/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/safari2k/climate_meteorology/maun_met_flux/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/S2K/guides/maun_met_flux.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/S2K/guides/maun_met_flux.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/760",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/760",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/maun_met_flux/comp/maun_met_flux_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/safari2k/climate_meteorology/maun_met_flux/comp/maun_met_flux_readme.pdf",
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
+            "identifier": "C2789038485-ORNL_CLOUD",
+            "issued": "2023-10-18",
+            "keyword": [
+                "atmospheric radiation",
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "vegetation",
+                "surface radiative properties",
+                "biosphere",
+                "soils",
+                "precipitation",
+                "land surface",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/760",
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
             "spatial": "-19.9 23.55",
+            "temporal": "2000-02-01T00:00:00Z/2000-09-30T23:59:59Z",
             "theme": [
                 "SAFARI 2000",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFARI 2000 Meteorological and Flux Tower Measurements in Maun, Botswana, 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-L-JIRAM-3-RDR-V3.0",
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
-                "juno"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains the scientific telemetry produced by the JIRAM instrument , together with geometric information computed on ground to locate observations in space and time.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-l-jiram-3-rdr-v3.0_vqm6-exzz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "juno"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=JNO-L-JIRAM-3-RDR-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.jno-l-jiram-3-rdr-v3.0_vqm6-exzz",
-            "description": "This dataset contains the scientific telemetry produced by the JIRAM instrument , together with geometric information computed on ground to locate observations in space and time.",
-            "title": "JUNO MOON JIRAM REDUCED DATA\n                                      RECORD V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "JUNO MOON JIRAM REDUCED DATA\n                                      RECORD V3.0"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0762-V1.0",
-            "bureauCode": [
-                "026:00"
-            ],
-            "issued": "2021-05-21",
             "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
-            "keyword": [
-                "international rosetta mission",
-                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "026:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-09T21:05:35.000 to 2015-05-10T07:11:19.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0762-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0762-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0762-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-05-09T21:05:35.000 to 2015-05-10T07:11:19.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0762 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0762 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/vqng-7euz",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Arabidopsis thaliana was evaluated for its response to the spaceflight environment in three replicated experiments on the International Space Station. Two approaches were used; GFP reporter genes were used to collect gene expression data in real time within unique GFP imaging hardware and plants were harvested on orbit to RNAlater for subsequent analyses of gene expression with using Affymetrix and SAGE transcriptome analyses. Three tissue types were examined (leaves hypocotyls and roots) and compared to analyses conducted with whole plants. Transcriptome analyses with whole plants suggested that the spaceflight environment had little impact on the transcriptome of arabidopsis however closer examination of selected tissues revealed that there are a number of tissue-specific responses that arabidopsis employs to respond to this novel environment",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-7",
+                    "mediaType": "text/html",
+                    "title": "The Arabidopsis spaceflight transcriptome: a comparison of whole plants to discrete root hypocotyl and shoot responses to the orbital environment"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-7_vqng-7euz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "genelab microarray data processing protocol",
                 "reverse_transcription",
@@ -1529422,360 +1529436,360 @@
                 "p-mtab-28107",
                 "labeling"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/vqng-7euz",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-7_vqng-7euz",
-            "description": "Arabidopsis thaliana was evaluated for its response to the spaceflight environment in three replicated experiments on the International Space Station. Two approaches were used; GFP reporter genes were used to collect gene expression data in real time within unique GFP imaging hardware and plants were harvested on orbit to RNAlater for subsequent analyses of gene expression with using Affymetrix and SAGE transcriptome analyses. Three tissue types were examined (leaves hypocotyls and roots) and compared to analyses conducted with whole plants. Transcriptome analyses with whole plants suggested that the spaceflight environment had little impact on the transcriptome of arabidopsis however closer examination of selected tissues revealed that there are a number of tissue-specific responses that arabidopsis employs to respond to this novel environment",
-            "title": "The Arabidopsis spaceflight transcriptome: a comparison of whole plants to discrete root hypocotyl and shoot responses to the orbital environment",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-7",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "The Arabidopsis spaceflight transcriptome: a comparison of whole plants to discrete root hypocotyl and shoot responses to the orbital environment"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "The Arabidopsis spaceflight transcriptome: a comparison of whole plants to discrete root hypocotyl and shoot responses to the orbital environment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LROC-2-EDR-V1.0",
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
-                "lunar reconnaissance orbiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set comprises Un-calibrated data from the LROC NAC and WAC cameras. The science data is comprised of Un-calibrated raw images, along with pointing data and housekeeping information.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lroc-2-edr-v1.0_vqnh-g66j",
+            "issued": "2018-06-26",
+            "keyword": [
+                "moon",
+                "lunar reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LRO-L-LROC-2-EDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lro-l-lroc-2-edr-v1.0_vqnh-g66j",
-            "description": "This data set comprises Un-calibrated data from the LROC NAC and WAC cameras. The science data is comprised of Un-calibrated raw images, along with pointing data and housekeeping information.",
-            "title": "LRO MOON LROC 2 EDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LRO MOON LROC 2 EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3357-V1.0",
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
-                "mars express",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-22T04:28:51.000 to 2012-07-22T06:55:13.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3357-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3357-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3357-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-22T04:28:51.000 to 2012-07-22T06:55:13.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3357 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3357 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOC-4-SAMPLER-V1.0",
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
-                "mars global surveyor",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Mars Orbiter Camera (MOC) data  products on this volume are nine Narrow Angle Camera images  selected from orbits between 13 and 100; i.e., some images are  from outside the Assessment Orbits range of 19-36. The images  are in GIF format with detached PDS labels, and they have had  some cosmetic corrections applied (see VOLINFO for description).  As the images are large, reduced-size versions have also been  included for browsing. To assist in locating the images on the  planet, 'finder frames' have been provided; these are Viking  Orbiter MDIMs showing the outlines of the MOC images in the  context of the larger area. The locations of the MOC images  are also shown on the Mercator and South Polar Stereographic  orbit ground track maps below. (Note: MOC image files are named  according to the form NAnnnnxx, where nnnn is the orbit number  and xx is the image number within the orbit.)",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-moc-4-sampler-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars global surveyor",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGS-M-MOC-4-SAMPLER-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgs-m-moc-4-sampler-v1.0",
-            "description": "Mars Orbiter Camera (MOC) data  products on this volume are nine Narrow Angle Camera images  selected from orbits between 13 and 100; i.e., some images are  from outside the Assessment Orbits range of 19-36. The images  are in GIF format with detached PDS labels, and they have had  some cosmetic corrections applied (see VOLINFO for description).  As the images are large, reduced-size versions have also been  included for browsing. To assist in locating the images on the  planet, 'finder frames' have been provided; these are Viking  Orbiter MDIMs showing the outlines of the MOC images in the  context of the larger area. The locations of the MOC images  are also shown on the Mercator and South Polar Stereographic  orbit ground track maps below. (Note: MOC image files are named  according to the form NAnnnnxx, where nnnn is the orbit number  and xx is the image number within the orbit.)",
-            "title": "MGS SAMPLER MARS ORBITER CAMERA IMAGES",
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
+            "title": "MGS SAMPLER MARS ORBITER CAMERA IMAGES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/WK4WA91H9B1Z",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX02 SSM/I Brightness Temperature Data, Iowa, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/WK4WA91H9B1Z.",
-            "issued": "2002-04-29",
-            "temporal": "2002-04-29T00:00:00Z/2002-07-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-07-13",
-            "keyword": [
-                "spectral/engineering",
-                "land surface",
-                "microwave",
-                "earth science",
-                "agriculture",
-                "soils"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Jackson",
                 "hasEmail": "mailto:tom.jackson@ars.usda.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386250239-NSIDCV0",
             "description": "This data set provides brightness temperature data, acquired during the Soil Moisture Experiment 2002 (SMEX02) by the Special Sensor Microwave/Imagery (SSM/I).",
-            "title": "SMEX02 SSM/I Brightness Temperature Data, Iowa, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWK4WA91H9B1Z",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWK4WA91H9B1Z",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/satellite_remote_sensing/SSMI/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/satellite_remote_sensing/SSMI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/satellite_remote_sensing/SSMI/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX02/satellite_remote_sensing/SSMI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/WK4WA91H9B1Z",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/WK4WA91H9B1Z",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/WK4WA91H9B1Z",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/WK4WA91H9B1Z",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250239-NSIDCV0",
+            "issued": "2002-04-29",
+            "keyword": [
+                "spectral/engineering",
+                "land surface",
+                "microwave",
+                "earth science",
+                "agriculture",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/WK4WA91H9B1Z",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-07-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-100.0 34.5 -90.0 44.5",
+            "temporal": "2002-04-29T00:00:00Z/2002-07-13T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX02 SSM/I Brightness Temperature Data, Iowa, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TEOCN-3AC64",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Felix Landerer. 2021-06-11. CSR TELLUS GRACE Level-3 Monthly OCEAN Water-Equivalent-Thickness Surface-Mass Anomaly Release 6.0. Version RL06 v04. TELLUS_GRAC_L3_CSR_RL06_OCN_v04. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/TEOCN-3AC64. https://grace.jpl.nasa.gov/data/get-data/monthly-mass-grids-ocean/. Felix Landerer, PO.DAAC, 2021-06-11, CSR TELLUS GRACE Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.0 version 04 in netCDF/ASCII/GeoTIFF Formats, https://grace.jpl.nasa.gov/data/get-data/monthly-mass-grids-ocean/.",
-            "issued": "2021-03-11",
-            "temporal": "2002-04-04T00:00:00Z/2017-10-25T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-11",
-            "keyword": [
-                "oceans",
-                "gravity/gravitational field",
-                "ocean pressure",
-                "solid earth",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:cmr-support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2077042363-POCLOUD",
-            "description": "The monthly ocean bottom pressure anomaly grids are given as equivalent water thickness changes derived from GRACE & GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. The Equivalent water thickness represent sea floor pressure changes due to the integral effect of ocean and atmosphere processes, including global mean ocean bottom pressure changes (mean ocean mass and mean atmosphere mass over the global oceans). The Level-2 GAD product has been added back, a glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters (i.e., de-striping and spatial smoothing) have been applied to reduce correlated errors. Version 04 (v04) of the ocean bottom pressure data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Data grids are provided in ASCII/netCDF/GeoTIFF formats. For the RL06 version, all GRACE products in the ASCII format have adopted the YAML encoding header, which is in full compliance with the PODAAC metadata best practices.",
-            "release-place": "JPL",
-            "series-name": "CSR TELLUS GRACE Level-3 Monthly OCEAN Water-Equivalent-Thickness Surface-Mass Anomaly Release 6.0",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Felix Landerer",
-            "title": "CSR TELLUS GRACE Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.0 version 04",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRAC_L3_CSR_RL06_OCN_v04.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The monthly ocean bottom pressure anomaly grids are given as equivalent water thickness changes derived from GRACE & GRACE-FO time-variable gravity observations during the specified timespan, and relative to the specified time-mean reference period. The Equivalent water thickness represent sea floor pressure changes due to the integral effect of ocean and atmosphere processes, including global mean ocean bottom pressure changes (mean ocean mass and mean atmosphere mass over the global oceans). The Level-2 GAD product has been added back, a glacial isostatic adjustment (GIA) correction has been applied, and standard corrections for geocenter (degree-1), C20 (degree-20) and C30 (degree-30) are incorporated. Post-processing filters (i.e., de-striping and spatial smoothing) have been applied to reduce correlated errors. Version 04 (v04) of the ocean bottom pressure data uses updated and consistent C20 and Geocenter corrections (i.e., Technical Notes TN-14 and TN-13), as well as an ellipsoidal correction to account for the non-spherical shape of the Earth when mapping gravity anomalies to surface mass change. Data grids are provided in ASCII/netCDF/GeoTIFF formats. For the RL06 version, all GRACE products in the ASCII format have adopted the YAML encoding header, which is in full compliance with the PODAAC metadata best practices.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEOCN-3AC64",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEOCN-3AC64",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L3_Handbook_JPL.pdf",
-                    "description": "User guidance documentation for this dataset",
                     "@type": "dcat:Distribution",
+                    "description": "User guidance documentation for this dataset",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE-FO_L3_Handbook_JPL.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRAC_L3_CSR_RL06_OCN_v04.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRAC_L3_CSR_RL06_OCN_v04.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://grace.jpl.nasa.gov/",
-                    "description": "GRACE Project",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE Project",
+                    "downloadURL": "https://grace.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthdata.nasa.gov/esdis/eso/standards-and-references/yaml-encoding-ascii-format-for-grace-grace-fo-mission-data",
-                    "description": "YAML Encoding ASCII Format for GRACE/GRACE-FO Mission Data",
                     "@type": "dcat:Distribution",
+                    "description": "YAML Encoding ASCII Format for GRACE/GRACE-FO Mission Data",
+                    "downloadURL": "https://earthdata.nasa.gov/esdis/eso/standards-and-references/yaml-encoding-ascii-format-for-grace-grace-fo-mission-data",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_Months_RL06.csv",
-                    "description": "GRACE monthly data integration range",
                     "@type": "dcat:Distribution",
+                    "description": "GRACE monthly data integration range",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_Months_RL06.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
-                    "description": "PO.DAAC GRACE Mission Information",
                     "@type": "dcat:Distribution",
+                    "description": "PO.DAAC GRACE Mission Information",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic netCDF readers provided in multiple programming languages",
                     "@type": "dcat:Distribution",
+                    "description": "Generic netCDF readers provided in multiple programming languages",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2077042363-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2077042363-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2077042363-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2077042363-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/TELLUS_GRAC_L3_CSR_RL06_OCN_v04.jpg",
+            "identifier": "C2077042363-POCLOUD",
+            "issued": "2021-03-11",
+            "keyword": [
+                "oceans",
+                "gravity/gravitational field",
+                "ocean pressure",
+                "solid earth",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TEOCN-3AC64",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-03-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "release-place": "JPL",
+            "series-name": "CSR TELLUS GRACE Level-3 Monthly OCEAN Water-Equivalent-Thickness Surface-Mass Anomaly Release 6.0",
             "spatial": "-180.0 -89.5 180.0 89.5",
+            "temporal": "2002-04-04T00:00:00Z/2017-10-25T00:00:00Z",
             "theme": [
                 "GRACE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CSR TELLUS GRACE Level-3 Monthly Ocean Bottom Pressure Anomaly Release 6.0 version 04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/vqvj-d5cb",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Space travel presents unlimited opportunities for exploration and discovery but requires a more complete understanding of the immunological consequences of long-term exposure to the conditions of spaceflight. To understand these consequences better and to contribute to design of effective countermeasures we used the Drosophila model to compare innate immune responses to bacteria and fungi in flies that were either raised on earth or in outer space aboard the NASA Space Shuttle Discovery (STS-121). Microarrays were used to characterize changes in gene expression that occur in response to infection by bacteria and fungus in drosophila that were either hatched and raised in outer space (microgravity) or on earth (normal gravity). Whole Oregon R strain drosophila melanogaster fruit flies either raised on earth or in space that were (1) uninfected (2) infected with bacteria (Escherichia coli) or (3) infected with fungus (Beauveria bassiana) were used for RNA extraction and hybridization on Affymetrix microarrays.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-1",
+                    "mediaType": "text/html",
+                    "title": "Expression data from drosophila melanogaster"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-1_vqvj-d5cb",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "p-gse53196-3",
                 "normalization data transformation protocol",
@@ -1529794,48 +1529808,36 @@
                 "radiation dosimetry",
                 "spaceflight"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/vqvj-d5cb",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-1_vqvj-d5cb",
-            "description": "Space travel presents unlimited opportunities for exploration and discovery but requires a more complete understanding of the immunological consequences of long-term exposure to the conditions of spaceflight. To understand these consequences better and to contribute to design of effective countermeasures we used the Drosophila model to compare innate immune responses to bacteria and fungi in flies that were either raised on earth or in outer space aboard the NASA Space Shuttle Discovery (STS-121). Microarrays were used to characterize changes in gene expression that occur in response to infection by bacteria and fungus in drosophila that were either hatched and raised in outer space (microgravity) or on earth (normal gravity). Whole Oregon R strain drosophila melanogaster fruit flies either raised on earth or in space that were (1) uninfected (2) infected with bacteria (Escherichia coli) or (3) infected with fungus (Beauveria bassiana) were used for RNA extraction and hybridization on Affymetrix microarrays.",
-            "title": "Expression data from drosophila melanogaster",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-1",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Expression data from drosophila melanogaster"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Expression data from drosophila melanogaster"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-3-FBIRTFSPEC-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The data set contains observations       obtained with the NASA IRTF SpeX instrument covering the 0.7 to 2.5    micron near-infrared portion of the spectrum.  The data set archives   reduced, calibrated spectra which were obtained and used in Sherry     Fieber-Beyer's Ph.D. dissertation at the                               University of North Dakota and archives reduced, calibrated spectra    subsequent 2010. The research focused on asteroids in a zone centered  on the 3:1 resonance. These spectra were used to mineralogically       characterize asteroids in this zone in an attempt to identify their    meteorite analogs.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-3-fbirtfspec-v3.0_vqxs-qvmw",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "421 zahringia",
                 "787 moskva",
@@ -1529892,426 +1529894,426 @@
                 "1036 ganymed",
                 "1018 arnolda"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0046-3-FBIRTFSPEC-V3.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0046-3-fbirtfspec-v3.0_vqxs-qvmw",
-            "description": "The data set contains observations       obtained with the NASA IRTF SpeX instrument covering the 0.7 to 2.5    micron near-infrared portion of the spectrum.  The data set archives   reduced, calibrated spectra which were obtained and used in Sherry     Fieber-Beyer's Ph.D. dissertation at the                               University of North Dakota and archives reduced, calibrated spectra    subsequent 2010. The research focused on asteroids in a zone centered  on the 3:1 resonance. These spectra were used to mineralogically       characterize asteroids in this zone in an attempt to identify their    meteorite analogs.",
-            "title": "FIEBER-BEYER IRTF MAINBELT ASTEROID     \n        SPECTRA V3.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "FIEBER-BEYER IRTF MAINBELT ASTEROID     \n        SPECTRA V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-EXT3-MTP031-V1.0",
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
+            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the EXTENSION 3 MTP031 phase, which occurred from 2016-06-29 to 2016-07-27",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-ext3-mtp031-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-VIRTIS-2-EXT3-MTP031-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-virtis-2-ext3-mtp031-v1.0",
-            "description": "This release contains the digital numbers (DN) contained in the telemetry (TM) packages of the VIRTIS instrument on board of the spacecraft Rosetta. This volume contains data at the vicinity of comet 67P, from the EXTENSION 3 MTP031 phase, which occurred from 2016-06-29 to 2016-07-27",
-            "title": "ROSETTA-ORBITER 67P VIRTIS 2 EXTENSION 3 MTP031 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P VIRTIS 2 EXTENSION 3 MTP031 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-LAUNCH-V1.1",
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
-                "solar wind",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-launch-v1.1_vqzg-g9t2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar wind",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-PEPSSI-3-LAUNCH-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-pepssi-3-launch-v1.1_vqzg-g9t2",
-            "description": "This data set contains Calibrated data taken by the New Horizons Pluto Energetic Particle Spectrometer Science Investigation instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS PEPSSI POST-LAUNCH CHECKOUT V1.1",
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
+            "title": "NEW HORIZONS PEPSSI POST-LAUNCH CHECKOUT V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LEISA-3-KEM1-V3.0",
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
+            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the KEM1 ENCOUNTER mission phase.  This is VERSION 3.0 of this data set. This data set contains LEISA observations taken for functional testing, and Arrokoth [ASTEROID 486958 (2014 MU69)] Encounter operations, including a test of a slow scan rate. Many LEISA Composition and System Scans along with some LEISA Scans as a LORRI Rider. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-leisa-3-kem1-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons kuiper belt extended mission",
+                "vega"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-A-LEISA-3-KEM1-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-a-leisa-3-kem1-v3.0",
-            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the KEM1 ENCOUNTER mission phase.  This is VERSION 3.0 of this data set. This data set contains LEISA observations taken for functional testing, and Arrokoth [ASTEROID 486958 (2014 MU69)] Encounter operations, including a test of a slow scan rate. Many LEISA Composition and System Scans along with some LEISA Scans as a LORRI Rider. This data set contains data acquired by the spacecraft between 08/14/2018 and 07/31/2019. It only includes data downlinked before 08/01/2019. Future datasets may include more data acquired by the spacecraft after 08/13/2018 but downlinked after 07/31/2019.",
-            "title": "NEW HORIZONS\n      LEISA KEM1\n      CALIBRATED V3.0",
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
+            "title": "NEW HORIZONS\n      LEISA KEM1\n      CALIBRATED V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/MELVILLE/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/MELVILLE/DATA001.",
-            "issued": "1999-10-01",
-            "temporal": "1999-10-01T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean temperature",
-                "salinity/density",
-                "earth science",
-                "ocean optics",
-                "oceans",
-                "ocean chemistry"
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
-            "identifier": "C1633360478-OB_DAAC",
             "description": "Measurements taken in the eastern Pacific Ocean off the coast of Baja California in 1999.",
-            "title": "Measurements off the coast of Baja California onboard R/V Melville in 1999",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMELVILLE%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FMELVILLE%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MELVILLE/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/MELVILLE/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360478-OB_DAAC",
+            "issued": "1999-10-01",
+            "keyword": [
+                "ocean temperature",
+                "salinity/density",
+                "earth science",
+                "ocean optics",
+                "oceans",
+                "ocean chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/MELVILLE/DATA001",
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
+            "temporal": "1999-10-01T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements off the coast of Baja California onboard R/V Melville in 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1010",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ehleringer, J.R., L.A. Martinelli, C. Cook, T.F. Domingues, L. Flanagan, J.A. Berry, and J.P.H.B. Ometto. 2011. LBA-ECO CD-02 Leaf Level Gas Exchange, Chemistry, and Isotopes, Amazonia, Brazil. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1010",
-            "issued": "2023-10-03",
-            "temporal": "1999-10-28T00:00:00Z/2003-12-17T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-05",
-            "keyword": [
-                "terrestrial hydrosphere",
-                "water quality/water chemistry",
-                "biosphere",
-                "ecological dynamics",
-                "earth science",
-                "vegetation"
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
-            "identifier": "C2777837446-ORNL_CLOUD",
             "description": "This data set reports leaf gas flux and leaf properties from samples collected from trees, liana, pasture saplings, and pasture grass located at eight different sampling locations in the states of Para (south of Santarem) and Amazonas (near Manaus) from November 1999 through December 2003. Data are reported on photosynthesis measurements, CO2 response curves, light response curves, humidity response curves, and stomatal responses to variations of the leaf-to-air water vapor mole fraction deficit. Leaf weight, carbon and nitrogen concentrations as well as stable isotope signatures for 13C and 15N are reported for a subset of the samples. There is one comma-delimited ASCII data file with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-02 Leaf Level Gas Exchange, Chemistry, and Isotopes, Amazonia, Brazil",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1010",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1010",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD02_Leaf_Level_Gas_Exchange/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD02_Leaf_Level_Gas_Exchange/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD02_Leaf_Level_Gas_Exchange.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD02_Leaf_Level_Gas_Exchange.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1010",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1010",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD02_Leaf_Level_Gas_Exchange/comp/CD02_Leaf_Level_Gas_Exchange.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD02_Leaf_Level_Gas_Exchange/comp/CD02_Leaf_Level_Gas_Exchange.pdf",
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
+            "identifier": "C2777837446-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "terrestrial hydrosphere",
+                "water quality/water chemistry",
+                "biosphere",
+                "ecological dynamics",
+                "earth science",
+                "vegetation"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1010",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-60.12 -3.02 54.58 2.0",
+            "temporal": "1999-10-28T00:00:00Z/2003-12-17T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-02 Leaf Level Gas Exchange, Chemistry, and Isotopes, Amazonia, Brazil"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1089",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Mendoza, E.R.H., I.F. Brown, and D.C. Nepstad. 2012. LBA-ECO LC-02 Forest Flammability Data, Catuaba Experimental Farm, Acre, Brazil: 1998. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1089",
-            "issued": "2023-10-03",
-            "temporal": "1998-06-01T00:00:00Z/1999-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-10",
-            "keyword": [
-                "earth science",
-                "human dimensions",
-                "natural hazards",
-                "environmental impacts"
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
-            "identifier": "C2780119221-ORNL_CLOUD",
             "description": "This data set provides the results of controlled burns conducted to assess the flammability of mature forests on the Catuaba Experimental Farm of the Federal University of Acre - Rio Branco, Acre, Brazil. Controlled burns were conducted in 1998, and the rate of fire spread was calculated based on the duration of the fire and the measured extent of the burned area. Environmental variables measured included type of forest, canopy openness, leaf area index, number of days without rainfall, precipitation, height of litter, litter humidity, brushwood humidity, amount of water in the ground, air temperature, and relative humidity. Results from 50 fires set in 1998 are reported. There is one comma-delimited data file with this data set.These data are part of a larger study reported in the thesis by Elsa Renee Huamon Mendoza, Susceptibility of primary forest to fire in 1998 and 1999: A case study in Acre, south-eastern Amazonia, Brazil. The thesis, in Portuguese, is included as a companion file with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-02 Forest Flammability Data, Catuaba Experimental Farm, Acre, Brazil: 1998",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1089",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1089",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC02_Forest_Flammability_Acre/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC02_Forest_Flammability_Acre/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC02_Forest_Flammability_Acre.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC02_Forest_Flammability_Acre.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1089",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1089",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC02_Forest_Flammability_Acre/comp/Dissertacao_2003_ElsaMendonza.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC02_Forest_Flammability_Acre/comp/Dissertacao_2003_ElsaMendonza.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC02_Forest_Flammability_Acre/comp/LC02_Forest_Flammability_Acre.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC02_Forest_Flammability_Acre/comp/LC02_Forest_Flammability_Acre.pdf",
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
+            "identifier": "C2780119221-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "human dimensions",
+                "natural hazards",
+                "environmental impacts"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1089",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-10.07 -67.63",
+            "temporal": "1998-06-01T00:00:00Z/1999-09-30T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-02 Forest Flammability Data, Catuaba Experimental Farm, Acre, Brazil: 1998"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CON-CAL-TLM-1-EDR-GROUND-GSE-V1.0",
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
-                "contour mission",
-                "unknown"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains the raw telemetry from the Ground Support Equipment (GSE) facilities used to integrate the spacecraft components at JHU/APL in 2002. The documentation on volume CON_0001 under /DOCUMENT/HARCH describes when tests were run.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.con-cal-tlm-1-edr-ground-gse-v1.0_vr8t-s9bj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "contour mission",
+                "unknown"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CON-CAL-TLM-1-EDR-GROUND-GSE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.con-cal-tlm-1-edr-ground-gse-v1.0_vr8t-s9bj",
-            "description": "This dataset contains the raw telemetry from the Ground Support Equipment (GSE) facilities used to integrate the spacecraft components at JHU/APL in 2002. The documentation on volume CON_0001 under /DOCUMENT/HARCH describes when tests were run.",
-            "title": "CONTOUR TELEMETRY GSE DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CONTOUR TELEMETRY GSE DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0052-8-S3OS2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains the visible spectra of 820 asteroids obtained between November 1996 and May 2001 at the 1.52m telescope at ESO (La Silla). The useful spectral range is between about 4900 and 9200 Angstroms. The global spatial distribution of the objects covers the region between 2.2 and 3.3 AU. Some concentrations are apparent, since part of the survey was focused on particuarly interesting groups or families of asteroids. The observed asteroids have been classified according to the Tholen and the Bus taxonomies, with a good agreement between both in most of the cases.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0052-8-s3os2-v1.0_vra2-2rmg",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2448 sholokhov",
                 "241 germania",
@@ -1531129,69 +1531131,45 @@
                 "2464 nordenskiold",
                 "2463 sterpin"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-I0052-8-S3OS2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-i0052-8-s3os2-v1.0_vra2-2rmg",
-            "description": "This dataset contains the visible spectra of 820 asteroids obtained between November 1996 and May 2001 at the 1.52m telescope at ESO (La Silla). The useful spectral range is between about 4900 and 9200 Angstroms. The global spatial distribution of the objects covers the region between 2.2 and 3.3 AU. Some concentrations are apparent, since part of the survey was focused on particuarly interesting groups or families of asteroids. The observed asteroids have been classified according to the Tholen and the Bus taxonomies, with a good agreement between both in most of the cases.",
-            "title": "SMALL SOLAR SYSTEM OBJECTS SPECTROSCOPIC SURVEY V1.0",
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
+            "title": "SMALL SOLAR SYSTEM OBJECTS SPECTROSCOPIC SURVEY V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/OMI/DATA1402",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Quintus Kleipool. 2021-08-09. OML1BRUG. Version 004. OMI/Aura Level 1B UV Global Geolocated Earthshine Radiances V004. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/AURA/OMI/DATA1402. https://disc.gsfc.nasa.gov/datacollection/OML1BRUG_004.html. Digital Science Data.",
-            "issued": "2021-07-01",
-            "temporal": "2004-10-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-01",
-            "keyword": [
-                "earth science",
-                "ultraviolet wavelengths",
-                "spectral/engineering"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Quintus Kleipool",
                 "hasEmail": "mailto:quintus.kleipool@knmi.nl"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2045794784-GES_DISC",
-            "description": "The Aura Ozone Monitoring Instrument (OMI) Level 1B (L1B) Geolocated Earthshine UV Radiance, Global-mode (shortname OML1BRUG) Version 4 product contains geolocated Earth view spectral radiances from the UV detectors in the wavelength range of 264 to 383 nm taken in the global measurement mode. In the global mode, OMI observes 60 ground pixels (13 km x 24 km at nadir) across the swath (~2600 km) for each of the 557 channels of Band 2 (307-383 nm) and 30 ground pixels (13 km x 48 km at nadir) for the 159 channels of Band 1 (264-311 nm). There are approximately 14 files of orbital data per day. Each file contains data from the daylit portion of an orbit and is roughly 210 MB in size. This OML1BRUG global-mode product is occasionally unavailable when the instrument is collecting data in the zoom-mode or is making special calibration measurements. The data in the OML1BRUG files are stored in the Network Common Data Form (netCDF) format. The lead algorithm scientist for the OMI Level 1 products is Dr. Quintus Kleipool of the Royal Netherlands Meteorological Institude (KNMI).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OML1BRUG",
             "creator": "Quintus Kleipool",
-            "title": "OMI/Aura Level 1B UV Global Geolocated Earthshine Radiances V004 (OML1BRUG) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BRUG_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Aura Ozone Monitoring Instrument (OMI) Level 1B (L1B) Geolocated Earthshine UV Radiance, Global-mode (shortname OML1BRUG) Version 4 product contains geolocated Earth view spectral radiances from the UV detectors in the wavelength range of 264 to 383 nm taken in the global measurement mode. In the global mode, OMI observes 60 ground pixels (13 km x 24 km at nadir) across the swath (~2600 km) for each of the 557 channels of Band 2 (307-383 nm) and 30 ground pixels (13 km x 48 km at nadir) for the 159 channels of Band 1 (264-311 nm). There are approximately 14 files of orbital data per day. Each file contains data from the daylit portion of an orbit and is roughly 210 MB in size. This OML1BRUG global-mode product is occasionally unavailable when the instrument is collecting data in the zoom-mode or is making special calibration measurements. The data in the OML1BRUG files are stored in the Network Common Data Form (netCDF) format. The lead algorithm scientist for the OMI Level 1 products is Dr. Quintus Kleipool of the Royal Netherlands Meteorological Institude (KNMI).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FOMI%2FDATA1402",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FOMI%2FDATA1402",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1531201,66 +1531179,66 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BRUG_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OML1BRUG_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRUG.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRUG.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BRUG_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OML1BRUG_004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRUG.004/doc/AURA-OMI-KNMI-L01B-0013-RP-prf-v024148-20210702.pdf",
-                    "description": "OMI v4 L1B README Document",
                     "@type": "dcat:Distribution",
+                    "description": "OMI v4 L1B README Document",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level1/OML1BRUG.004/doc/AURA-OMI-KNMI-L01B-0013-RP-prf-v024148-20210702.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0002-SD-atbd-v024170-20210716.pdf",
-                    "description": "OMI v4 L01B Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI v4 L01B Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0002-SD-atbd-v024170-20210716.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0005-SD-iods-v024148-20210702.pdf",
-                    "description": "OMI v4 L01B Input Output Data Specification",
                     "@type": "dcat:Distribution",
+                    "description": "OMI v4 L01B Input Output Data Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0005-SD-iods-v024148-20210702.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0007-SD-metadata_specs-v024148-20210702.pdf",
-                    "description": "OMI v4 L01B Metadata Specification",
                     "@type": "dcat:Distribution",
+                    "description": "OMI v4 L01B Metadata Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0007-SD-metadata_specs-v024148-20210702.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gsfc.nasa.gov/",
-                    "description": "Aura Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Aura Project Home Page",
+                    "downloadURL": "https://aura.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.knmiprojects.nl/projects/ozone-monitoring-instrument",
-                    "description": "OMI KNMI Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OMI KNMI Home Page",
+                    "downloadURL": "https://www.knmiprojects.nl/projects/ozone-monitoring-instrument",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
@@ -1531270,542 +1531248,536 @@
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OML1BRUG_004.png",
+            "identifier": "C2045794784-GES_DISC",
+            "issued": "2021-07-01",
+            "keyword": [
+                "earth science",
+                "ultraviolet wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/OMI/DATA1402",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-07-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OML1BRUG",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Level 1B UV Global Geolocated Earthshine Radiances V004 (OML1BRUG) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TERRA/CERES/CRS_TERRA-FM1_L2.004A",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/TERRA/CERES/CRS_TERRA-FM1_L2.004A.",
-            "issued": "2023-02-13",
-            "temporal": "2019-01-01T00:00:00Z/2023-05-15T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-13",
-            "keyword": [
-                "land surface",
-                "clouds",
-                "aerosols",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "ngda",
-                "national geospatial data asset",
-                "surface radiative properties",
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NORMAN LOEB",
                 "hasEmail": "mailto:ceres-help@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2645080346-LARC_ASDC",
             "description": "CER_CRS_Terra-FM1-MODIS_Edition4A is the Clouds and the Earth's Radiant Energy System (CERES) Clouds and Radiative Swath (CRS) Terra Flight Model 1 (FM1) Moderate-Resolution Imaging Spectroradiometer (MODIS) Edition4A data product, which was collected using the CERES-FM1 instrument on the Terra platform. Please note that only a few variables from the SSF have been included and this product should be used in conjunction with the CER_SSF_Terra-FM1-MODIS_Edition4A product.\r\n\r\nThe Clouds and Radiative Swath (CRS) product contains one hour of instantaneous CERES data for a single scanner instrument. The CRS contains geolocation, geometry, packet identification, and minimal cloud properties, and TOA fluxes from the CERES SSF product. For each CERES footprint on the Single Scanner Footprint (SSF), the CRS product also contains vertical flux profiles evaluated at six levels in the atmosphere: the surface, 850-, 500-, 200-, 70-, and 0.01-hPa for both clear-sky and total-sky.\r\n\r\nCERES is a key component of the Earth Observing System (EOS) program. The CERES instruments provide radiometric measurements of the Earth's atmosphere from three broadband channels. The CERES missions are a follow-on to the successful Earth Radiation Budget Experiment (ERBE) mission. The first CERES instrument, protoflight model (PFM), was launched on November 27, 1997 as part of the Tropical Rainfall Measuring Mission (TRMM). Two CERES instruments (FM1 and FM2) were launched into polar orbit on board the Earth Observing System (EOS) flagship Terra on December 18, 1999. Two additional CERES instruments (FM3 and FM4) were launched on board Earth Observing System (EOS) Aqua on May 4, 2002. The CERES FM5 instrument was launched on board the Suomi National Polar-orbiting Partnership (NPP) satellite on October 28, 2011. The newest CERES instrument (FM6) was launched on board the Joint Polar-Orbiting Satellite System 1 (JPSS-1) satellite, now called NOAA-20, on November 18, 2017.",
-            "title": "CERES Clouds and Radiative Swath Terra FM1 MODIS Edition4A",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FCRS_TERRA-FM1_L2.004A",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTERRA%2FCERES%2FCRS_TERRA-FM1_L2.004A",
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
-                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/CRS_TERRA-FM1_L2.004A",
-                    "description": "DOI data set landing page for CER_CRS_Terra-FM1-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CER_CRS_Terra-FM1-MODIS_Edition4A",
+                    "downloadURL": "https://doi.org/10.5067/TERRA/CERES/CRS_TERRA-FM1_L2.004A",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2645080346-LARC_ASDC",
-                    "description": "Earthdata Search for CER_CRS_Terra-FM1-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for CER_CRS_Terra-FM1-MODIS_Edition4A (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2645080346-LARC_ASDC",
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
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/product_level_details.pdf",
-                    "description": "CERES Product Level Details",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Product Level Details",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/product_level_details.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
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
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/DelicateBalance/balance2.php",
-                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Signs of Change in the Tropics - New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring...",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observeratory Article: A Delicate Balance: Signs of Change in the Tropics - New data sets were also used from NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments that fly aboard the Tropical Rainfall Measuring...",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/DelicateBalance/balance2.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
-                    "description": "NASA Earth Observatory Article: Aqua CERES First Light: Image of the Day - The Clouds and the Earth's Radiant Energy System (CERES) instrument is one of six on board the Aqua satellite.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Aqua CERES First Light: Image of the Day - The Clouds and the Earth's Radiant Energy System (CERES) instrument is one of six on board the Aqua satellite.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/2654/aqua-ceres-first-light",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
-                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day - Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Detects Earth's Heat and Energy: Image of the Day - Clouds and the Earth's Radiant Energy System (CERES) monitors solar energy reflected from the Earth and heat energy emitted from the Earth.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/563/ceres-detects-earths-heat-and-energy",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
-                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day - These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES First Light Images: Image of the Day - These two Terra instruments join a previous CERES scanner on the Tropical Rainfall Measuring Mission (TRMM) which was launched on November 27, 1997",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/535/ceres-first-light-images",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
-                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction - Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: CERES Global Cloud Fraction - Each map combines observations from the CERES sensors on NASA's Terra and Aqua satellites collected on December 27, 2008",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/36518/ceres-global-cloud-fraction",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
-                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog - Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Does the Earth Have an Iris Analog - Sensors on the TRMM and Terra satellite missions routinely measure these cloud physical properties, which scientists will match in time and space with CERES.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Iris/iris3.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
-                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation - These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: First Monthly CERES Global Longwave and Shortwave Radiation - These measurements were acquired by NASA's Clouds and the Earth's Radiant Energy System (CERES) sensors during March 2000.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/600/first-monthly-ceres-global-longwave-and-shortwave-radiation",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/global-maps/CERES_NETFLUX_M",
-                    "description": "NASA Earth Observatory Article: Net Radiation - The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Net Radiation - The measurements were made by the Clouds and the Earth's Radiant Energy System (CERES) sensors on NASA's Terra and Aqua satellites.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/global-maps/CERES_NETFLUX_M",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Observing/obs_5.php",
-                    "description": "NASA Earth Observatory Article: Space-based Observations of the Earth (Thermal radiation emitted from the Earth's surface and clouds on March 1, 2000 as seen by the Clouds and Earth's Radiant Energy System (CERES))",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Space-based Observations of the Earth (Thermal radiation emitted from the Earth's surface and clouds on March 1, 2000 as seen by the Clouds and Earth's Radiant Energy System (CERES))",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Observing/obs_5.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/AM1/terra_animations.php",
-                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet - Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that...",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Terra Spacecraft Fact Sheet - Clouds and the Earth's Radiant Energy System (CERES) CERES will measure the Earth's energy balance\u2014comparing the amount of energy from the sun that...",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/AM1/terra_animations.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
-                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight - The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Arctic Is Absorbing More Sunlight - The radiation measurements were made by NASA's Clouds and the Earth's Radiant Energy System (CERES) instruments which fly on multiple satellites.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/84930/the-arctic-is-absorbing-more-sunlight",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
-                    "description": "NASA Earth Observatory Article: The Water Cycle - MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: The Water Cycle - MODIS, CERES, and AIRS all collect data relevant to the study of clouds.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/Water/page4.php",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/images/2984/tropical-cloud-systems-and-ceres",
-                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day - CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Tropical Cloud Systems and CERES: Image of the Day - CERES detects the amount of outgoing heat and reflected sunlight leaving the planet.",
+                    "downloadURL": "https://earthobservatory.nasa.gov/images/2984/tropical-cloud-systems-and-ceres",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tools/hdf.pdf",
-                    "description": "Overview of HDF",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of HDF",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tools/hdf.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tools/view_hdf.pdf",
-                    "description": "Overview of view hdf: A Visualization and Analysis Tool for HDF Files",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of view hdf: A Visualization and Analysis Tool for HDF Files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tools/view_hdf.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Use this dataset in a web based map viewerf"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/examples.html",
-                    "description": "ASDC List of CERES Examples: Spatial Extent and Scan Modes",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC List of CERES Examples: Spatial Extent and Scan Modes",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/examples.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthobservatory.nasa.gov/features/CloudsInBalance",
-                    "description": "NASA Earth Observatory Article: Clouds in the Balance",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Observatory Article: Clouds in the Balance",
+                    "downloadURL": "https://earthobservatory.nasa.gov/features/CloudsInBalance",
+                    "mediaType": "text/html",
                     "title": "View a micro article on this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/documentation/",
-                    "description": "CERES Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Documentation",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/documentation/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/data/documentation/#data-products-catalog",
-                    "description": "CERES Documentation: Data Products Catalog",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Documentation: Data Products Catalog",
+                    "downloadURL": "https://ceres.larc.nasa.gov/data/documentation/#data-products-catalog",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
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
                     "title": "View this dataset's requirements and design documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#aqua",
-                    "description": "CERES Overview of Aqua",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of Aqua",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#aqua",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#terra",
-                    "description": "CERES Overview of Terra",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of Terra",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#terra",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_CRS_Terra_Edition4A.pdf",
-                    "description": "Quality Summary: CERES Terra Edition4A CRS",
                     "@type": "dcat:Distribution",
+                    "description": "Quality Summary: CERES Terra Edition4A CRS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/quality_summaries/CER_CRS_Terra_Edition4A.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#trmm",
-                    "description": "CERES Overview of TRMM",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Overview of TRMM",
+                    "downloadURL": "https://ceres.larc.nasa.gov/instruments/satellite-missions/#trmm",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/CWG.TELCON.9.01.pdf",
-                    "description": "CERES Cloud Working Group Teleconference",
                     "@type": "dcat:Distribution",
+                    "description": "CERES Cloud Working Group Teleconference",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/CWG.TELCON.9.01.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/README.txt",
-                    "description": "View HDF Version 5 Readme",
                     "@type": "dcat:Distribution",
+                    "description": "View HDF Version 5 Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/ceres/readme/README.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/products?CERESProducts=SSFlevel2_Ed4",
-                    "description": "CERES CRS Odering Tool",
                     "@type": "dcat:Distribution",
+                    "description": "CERES CRS Odering Tool",
+                    "downloadURL": "https://ceres-tool.larc.nasa.gov/ord-tool/products?CERESProducts=SSFlevel2_Ed4",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through the CERES Ordering Tool"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CRS/Terra-FM1-MODIS_Edition4A/",
-                    "description": "ASDC Direct Data Download for CER_CRS_Terra-FM1-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CER_CRS_Terra-FM1-MODIS_Edition4A",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CERES/CRS/Terra-FM1-MODIS_Edition4A/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CRS/Terra-FM1-MODIS_Edition4A/contents.html",
-                    "description": "OPeNDAP data access for CER_CRS_Terra-FM1-MODIS_Edition4A",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for CER_CRS_Terra-FM1-MODIS_Edition4A",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/CERES/CRS/Terra-FM1-MODIS_Edition4A/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2645080346-LARC_ASDC",
+            "issued": "2023-02-13",
+            "keyword": [
+                "land surface",
+                "clouds",
+                "aerosols",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "ngda",
+                "national geospatial data asset",
+                "surface radiative properties",
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/TERRA/CERES/CRS_TERRA-FM1_L2.004A",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-02-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-01-01T00:00:00Z/2023-05-15T00:00:00Z",
             "theme": [
                 "CERES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CERES Clouds and Radiative Swath Terra FM1 MODIS Edition4A"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103MODLL.021",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Guoqing Lin. 2023-08-29. VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m Light V021. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/VIIRS/VJ103MODLL.021. https://doi.org/10.5067/VIIRS/VJ103MODLL.021. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2023-08-29",
-            "temporal": "2018-01-01T00:00:00Z/2024-06-03T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-29",
-            "keyword": [
-                "earth science",
-                "sensor characteristics",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Guoqing Lin",
                 "hasEmail": "mailto:guoqing.lin-1@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2545314612-LPCLOUD",
-            "description": "The Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Moderate Resolution Terrain Correction Geolocation (VJ103MODLL) Version 2.1 product from the NOAA-20 VIIRS sensor is produced in 6 minute temporal satellite increments (swaths) at 750 meter resolution.  Intersecting the VIIRS line of sight vector with Earth\u2019s geoid and the World Geodetic System (WGS) ellipsoid, this product is based on the SRTM30 Version 2 digital elevation model (DEM), which uses GTOPO30 data for areas from 60\u00b0 North to 60\u00b0 South. VJ103MODLL is a terrain correction geolocation product that provides the spatial location for various VIIRS data products.  Each swath of data is approximately 3,060 kilometers along track (long) and 3,060 kilometers across track (wide). \r\n\r\nProvided in the VJ103MODLL product are layers for height, latitude, and longitude. \r\n\r\nThese Science Data Sets (SDS) layers are used in conjunction with the (VJ114) (https://doi.org/10.5067/viirs/vj114.002) swath product for accurate geolocation information.",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Guoqing Lin",
-            "title": "VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m Light V021",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Visible Infrared Imaging Radiometer Suite (VIIRS) (https://lpdaac.usgs.gov/dataset_discovery/viirs) Moderate Resolution Terrain Correction Geolocation (VJ103MODLL) Version 2.1 product from the NOAA-20 VIIRS sensor is produced in 6 minute temporal satellite increments (swaths) at 750 meter resolution.  Intersecting the VIIRS line of sight vector with Earth\u2019s geoid and the World Geodetic System (WGS) ellipsoid, this product is based on the SRTM30 Version 2 digital elevation model (DEM), which uses GTOPO30 data for areas from 60\u00b0 North to 60\u00b0 South. VJ103MODLL is a terrain correction geolocation product that provides the spatial location for various VIIRS data products.  Each swath of data is approximately 3,060 kilometers along track (long) and 3,060 kilometers across track (wide). \r\n\r\nProvided in the VJ103MODLL product are layers for height, latitude, and longitude. \r\n\r\nThese Science Data Sets (SDS) layers are used in conjunction with the (VJ114) (https://doi.org/10.5067/viirs/vj114.002) swath product for accurate geolocation information.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103MODLL.021",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVJ103MODLL.021",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314612-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2545314612-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QS/new/index.cgi",
-                    "description": "The LDOPE Land Product Quality Assessment website provides known issues, maneuvers, and product quality of the land products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LDOPE Land Product Quality Assessment website provides known issues, maneuvers, and product quality of the land products.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/QS/new/index.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ103MODLL.021",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VJ103MODLL.021",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1334/VNP03_User_Guide_V1.2.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1334/VNP03_User_Guide_V1.2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/135/VNP03_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/135/VNP03_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "identifier": "C2545314612-LPCLOUD",
+            "issued": "2023-08-29",
+            "keyword": [
+                "earth science",
+                "sensor characteristics",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VJ103MODLL.021",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-01-01T00:00:00Z/2024-06-03T00:00:00Z",
             "theme": [
                 "JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/JPSS1 Moderate Resolution Terrain Corrected Geolocation 6-Min L1 Swath 750m Light V021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA3008",
             "citation": "Can Li, Nickolay A. Krotkov, and Peter Leonard. 2020-10-16. OMSO2e. Version 003. OMI/Aura Sulfur Dioxide (SO2) Total Column L3 1 day Best Pixel in 0.25 degree x 0.25 degree V3. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA3008. https://disc.gsfc.nasa.gov/datacollection/OMSO2e_003.html. Digital Science Data.",
-            "issued": "2004-10-01",
-            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-10-15",
-            "references": [
-                "https://doi.org/10.5194/amt-13-6175-2020",
-                "https://doi.org/10.5194/amt-10-445-2017",
-                "https://doi.org/10.1002/2013GL058134"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CAN LI",
                 "hasEmail": "mailto:Can.Li@nasa.gov"
             },
+            "creator": "Can Li, Nickolay A. Krotkov, and Peter Leonard",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1266136112-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The OMI science team produces this Level-3 Aura/OMI Global OMSO2e Data Products (0.25 degree Latitude/Longitude grids). In this Level-3 daily global SO2 data product, each grid contains only one observation of Total Column Density of SO2 in the Planetary Boundary Layer (PBL), based on an improved Principal Component Analysis (PCA) Algorithm. This single observation is the \"best pixel\", selected from all \"good\" L2 pixels of OMSO2 that overlap this grid and have UTC time between UTC times of 00:00:00 and 23:59:59.999. In addition to the SO2 Vertical column value some ancillary parameters, e.g., cloud fraction, terrain height, scene number, solar and satellite viewing angles, row anomaly flags, and quality flags have been also made available corresponding to the best selected SO2 data pixel in each grid.\n\nThe OMSO2e files are stored in the version 5 EOS Hierarchical Data Format (HDF-EOS5) using the grid model.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OMSO2e",
-            "creator": "Can Li, Nickolay A. Krotkov, and Peter Leonard",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "OMI/Aura Sulfur Dioxide (SO2) Total Column Daily L3 1 day Best Pixel in 0.25 degree x 0.25 degree V3 (OMSO2e) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMSO2e",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA3008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA3008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1531815,111 +1531787,148 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMSO2e_003.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMSO2e_003.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMSO2e.003/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMSO2e.003/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMSO2e",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMSO2e",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMSO2e_003",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMSO2e_003",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level3/OMSO2e.003/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/HDF-EOS5/Aura_OMI_Level3/OMSO2e.003/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMSO2e.003/doc/README.OMSO2e_2020-10-16.txt",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level3/OMSO2e.003/doc/README.OMSO2e_2020-10-16.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/README.OMI_DUG.pdf",
-                    "description": "OMI Data User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "OMI Data User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/OMI/3.3_ScienceDataProductDocumentation/3.3.2_ProductRequirements_Designs/README.OMI_DUG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMSO2e_2020-11-25.fs",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMSO2e_2020-11-25.fs",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gsfc.nasa.gov/",
-                    "description": "Aura Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Aura Project Home Page",
+                    "downloadURL": "https://aura.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://projects.knmi.nl/omi/research/news/newsWrap.php?language=only_enhttps%3A%2F%2Fwww.knmi.nl%2FomitimeFrame%3Dlatesthttps%3A%2F%2Fwww.knmi.nl%2Fomichoise%3Dpage",
-                    "description": "OMI KNMI Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OMI KNMI Home Page",
+                    "downloadURL": "http://projects.knmi.nl/omi/research/news/newsWrap.php?language=only_enhttps%3A%2F%2Fwww.knmi.nl%2FomitimeFrame%3Dlatesthttps%3A%2F%2Fwww.knmi.nl%2Fomichoise%3Dpage",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://so2.gsfc.nasa.gov/",
-                    "description": "SO2 Monitoring Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "SO2 Monitoring Home Page",
+                    "downloadURL": "https://so2.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://projects.knmi.nl/omi/research/documents/",
-                    "description": "List of OMI publications",
                     "@type": "dcat:Distribution",
+                    "description": "List of OMI publications",
+                    "downloadURL": "https://projects.knmi.nl/omi/research/documents/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=OMSO2e",
+            "identifier": "C1266136112-GES_DISC",
+            "issued": "2004-10-01",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA3008",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-10-15",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5194/amt-13-6175-2020",
+                "https://doi.org/10.5194/amt-10-445-2017",
+                "https://doi.org/10.1002/2013GL058134"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OMSO2e",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OMI/Aura Sulfur Dioxide (SO2) Total Column Daily L3 1 day Best Pixel in 0.25 degree x 0.25 degree V3 (OMSO2e) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://itunes.apple.com/us/itunes-u/nasas-journey-to-project-management/id443158587?i=125444483",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://km.nasa.gov/knowledge-map/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ed Hoffman",
+                "hasEmail": "mailto:ehoffman@nasa.gov"
+            },
+            "description": "NASA's Path to Project Management Excellence eBook. Leadership plays a critical role in the success of today\u2019s programs and projects. In an increasingly global and dynamic project environment, the ability to for organizations to foster and develop project leaders who can lead in and deliver unique, innovative products and missions on time and budget has never been more important.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://itunes.apple.com/us/podcast/nasas-journey-to-project-management/id443158587?i=313090804&mt=2",
+                    "mediaType": "application/x-itunes-itlp"
+                }
             ],
+            "identifier": "NASA-864",
+            "issued": "2018-06-25",
             "keyword": [
                 "ebook",
                 "management",
@@ -1531930,362 +1531939,333 @@
                 "training",
                 "sharing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ed Hoffman",
-                "hasEmail": "mailto:ehoffman@nasa.gov"
-            },
+            "landingPage": "https://itunes.apple.com/us/itunes-u/nasas-journey-to-project-management/id443158587?i=125444483",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-864",
-            "description": "NASA's Path to Project Management Excellence eBook. Leadership plays a critical role in the success of today\u2019s programs and projects. In an increasingly global and dynamic project environment, the ability to for organizations to foster and develop project leaders who can lead in and deliver unique, innovative products and missions on time and budget has never been more important.",
-            "title": "Academy of Program/Project & Engineering Leadership: NASA's Path to Project Management Excellence",
-            "programCode": [
-                "026:045"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://itunes.apple.com/us/podcast/nasas-journey-to-project-management/id443158587?i=313090804&mt=2",
-                    "mediaType": "application/x-itunes-itlp"
-                }
+            "references": [
+                "http://km.nasa.gov/knowledge-map/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Academy of Program/Project & Engineering Leadership: NASA's Path to Project Management Excellence"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCICA-2-EXT3-RAW-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during Rosetta extension 3.\nData contains measurements of solar wind interaction\nwith the atmosphere of target comet 67P.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcica-2-ext3-raw-v1.0_vrd8-qa3d",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCICA-2-EXT3-RAW-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcica-2-ext3-raw-v1.0_vrd8-qa3d",
-            "description": "This dataset contains RAW DATA from the RPCICA instrument on\nmission ROSETTA during Rosetta extension 3.\nData contains measurements of solar wind interaction\nwith the atmosphere of target comet 67P.",
-            "title": "ROSETTA-ORBITER 67P RPCICA 2 EXT3 UNCALIBRATED V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RPCICA 2 EXT3 UNCALIBRATED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MYD10C1.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS/Aqua Snow Cover Daily L3 Global 0.05Deg CMG V061. Version 61. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MYD10C1.061.",
-            "issued": "2002-07-04",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-09",
-            "keyword": [
-                "earth science",
-                "cryosphere",
-                "snow/ice",
-                "ngda",
-                "national geospatial data asset"
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
-            "identifier": "C1646610053-NSIDC_ECS",
             "description": "This global Level-3 (L3) data set provides the percentage of snow-covered land and cloud-covered land observed daily, within 0.05\u00b0 (approx. 5 km) MODIS Climate Modeling Grid (CMG) cells. Percentages are computed from snow cover observations in the 'MODIS/Aqua Snow Cover Daily L3 Global 500m Grid' data set (DOI:10.5067/MODIS/MYD10A1.061).\n\nThe terms \"Version 61\" and \"Collection 6.1\" are used interchangeably in reference to this release of MODIS data.",
-            "title": "MODIS/Aqua Snow Cover Daily L3 Global 0.05Deg CMG V061",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD10C1.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMYD10C1.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/daac/subscriptions.html",
-                    "description": "Subscribe to have new data automatically sent when the data become available.",
                     "@type": "dcat:Distribution",
+                    "description": "Subscribe to have new data automatically sent when the data become available.",
+                    "downloadURL": "https://nsidc.org/daac/subscriptions.html",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOSA/MYD10C1.061",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MOSA/MYD10C1.061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MYD10C1+V061",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=MYD10C1+V061",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/MYD10C1/versions/61/",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/MYD10C1/versions/61/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10C1.061",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10C1.061",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10C1.061",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MYD10C1.061",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1646610053-NSIDC_ECS",
+            "issued": "2002-07-04",
+            "keyword": [
+                "earth science",
+                "cryosphere",
+                "snow/ice",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MYD10C1.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2025-01-13T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Snow Cover Daily L3 Global 0.05Deg CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA131",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Brodzik, Stacy .2022. KVWX NEXRAD IMPACTS [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/IMPACTS/NEXRAD/DATA131",
-            "issued": "2022-03-23",
-            "temporal": "2020-01-01T00:08:12Z/2020-03-01T00:06:38Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-31",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "radar"
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
-            "identifier": "C2020265507-GHRC_DAAC",
             "description": "The KVWX NEXRAD IMPACTS dataset consists of Next Generation Weather Radar (NEXRAD) Level II surveillance data that were collected at 31 NEXRAD sites from January 1 to March 1, 2020 during the Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms  (IMPACTS) field campaign. IMPACTS was a three-year sequence of winter season deployments conducted to study snowstorms over the U.S Atlantic Coast. The campaign aimed to (1) Provide observations critical to understanding the mechanisms of snowband formation, organization, and evolution; (2) Examine how the microphysical characteristics and likely growth mechanisms of snow particles vary across snowbands; and (3) Improve snowfall remote sensing interpretation and modeling to significantly advance prediction capabilities. There are currently 160 Weather Surveillance Radar-1988 Doppler (WSR-88D) or NEXRAD sites throughout the United States and abroad. These Level II datasets contain meteorological and dual-polarization base data quantities including: radar reflectivity, radial velocity, spectrum width, differential reflectivity, differential phase, and cross correlation ratio. The IMPACTS NEXRAD Level II data files are available in netCDF-4 format. It should be noted that this dataset will be updated in subsequent years of the IMPACTS campaign.",
-            "title": "KVWX NEXRAD IMPACTS V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA131",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FIMPACTS%2FNEXRAD%2FDATA131",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kvwximpacts",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=kvwximpacts",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh-11B-2005.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part B: Doppler Radar Theory and Meteorology",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part B: Doppler Radar Theory and Meteorology",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh-11B-2005.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/FMH11D-2006.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part D: WSR-88D Unit Description and Operational Applications",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part D: WSR-88D Unit Description and Operational Applications",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/FMH11D-2006.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part A: System Concepts, Responsibilities, and Procedures",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/2016FMH11PTA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
-                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
                     "@type": "dcat:Distribution",
+                    "description": "Federal Meteorological Handbook No. 11 Part C: WSR-88D Products and Algorithms",
+                    "downloadURL": "http://www.ofcm.gov/publications/fmh/FMH11/fmh11partC.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_details/collections/impactsC.html",
-                    "description": "IMPACTS Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Collection DOI",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/uso/ds_details/collections/impactsC.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/impacts",
-                    "description": "IMPACTS Field Campaign Information",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Information",
+                    "downloadURL": "https://espo.nasa.gov/impacts",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ncdc.noaa.gov/data-access/radar-data/nexrad",
-                    "description": "NEXRAD Information",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD Information",
+                    "downloadURL": "https://www.ncdc.noaa.gov/data-access/radar-data/nexrad",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://catalog.data.gov/dataset/noaa-next-generation-radar-nexrad-products",
-                    "description": "NOAA NEXt-Generation RADar (NEXRAD) Products",
                     "@type": "dcat:Distribution",
+                    "description": "NOAA NEXt-Generation RADar (NEXRAD) Products",
+                    "downloadURL": "https://catalog.data.gov/dataset/noaa-next-generation-radar-nexrad-products",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KVWX/doc/nexrad_datasets.pdf",
-                    "description": "NEXRAD IMPACTS User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "NEXRAD IMPACTS User Guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/impacts/NEXRAD/KVWX/doc/nexrad_datasets.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://go.gale.com/ps/anonymous?id=GALE%7CA9215749&sid=googleScholar&v=2.1&it=r&linkaccess=abs&issn=01926225&p=AONE&sw=w",
-                    "description": "Nexrad: next generation weather radar (WSR-88D)",
                     "@type": "dcat:Distribution",
+                    "description": "Nexrad: next generation weather radar (WSR-88D)",
+                    "downloadURL": "https://go.gale.com/ps/anonymous?id=GALE%7CA9215749&sid=googleScholar&v=2.1&it=r&linkaccess=abs&issn=01926225&p=AONE&sw=w",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docs.lib.purdue.edu/jto/vol1/iss2/art4",
-                    "description": "A Review of NEXRAD Level II: Data, Distribution, and Applications",
                     "@type": "dcat:Distribution",
+                    "description": "A Review of NEXRAD Level II: Data, Distribution, and Applications",
+                    "downloadURL": "https://docs.lib.purdue.edu/jto/vol1/iss2/art4",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/IGARSS46834.2022.9883693",
-                    "description": "Investigation of Microphysics and Precipitation for Atlantic Coast Threatening Snowstorms (Impacts): The 2022 Deployment",
                     "@type": "dcat:Distribution",
+                    "description": "Investigation of Microphysics and Precipitation for Atlantic Coast Threatening Snowstorms (Impacts): The 2022 Deployment",
+                    "downloadURL": "https://doi.org/10.1109/IGARSS46834.2022.9883693",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-20-0246.1",
-                    "description": "Chasing Snowstorms: The Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) Campaign",
                     "@type": "dcat:Distribution",
+                    "description": "Chasing Snowstorms: The Investigation of Microphysics and Precipitation for Atlantic Coast-Threatening Snowstorms (IMPACTS) Campaign",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-20-0246.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/impacts",
-                    "description": "IMPACTS Field Campaign Project Homepage",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Project Homepage",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/impacts",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/investigation-microphysics-and-precipitation-atlantic-coast-threatening-snowstorms",
-                    "description": "IMPACTS Field Campaign Micro Article",
                     "@type": "dcat:Distribution",
+                    "description": "IMPACTS Field Campaign Micro Article",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/micro-articles/investigation-microphysics-and-precipitation-atlantic-coast-threatening-snowstorms",
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
+            "identifier": "C2020265507-GHRC_DAAC",
+            "issued": "2022-03-23",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "radar"
+            ],
+            "landingPage": "https://doi.org/10.5067/IMPACTS/NEXRAD/DATA131",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-01-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-92.9872 34.1302 -82.4619 42.3903",
+            "temporal": "2020-01-01T00:08:12Z/2020-03-01T00:06:38Z",
             "theme": [
                 "IMPACTS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KVWX NEXRAD IMPACTS V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "https://pds.jpl.nasa.gov/"
-            ],
-            "keyword": [
-                "lgrs",
-                "pds",
-                "data"
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
-            "identifier": "NASA-446",
             "description": "LGRS",
-            "title": "PDS GRAIL (Gravity Recovery and Interior Laboratory) Release 4",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1532293,53 +1532273,51 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-446",
+            "issued": "2018-06-25",
+            "keyword": [
+                "lgrs",
+                "pds",
+                "data"
+            ],
+            "landingPage": "https://pds.jpl.nasa.gov/tools/subscription_service/SS-Release.shtml",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "https://pds.jpl.nasa.gov/"
+            ],
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "PDS GRAIL (Gravity Recovery and Interior Laboratory) Release 4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VV622VHH2LXV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "AIRS project. 2007-07-26. AIRIBQAP. Version 005. AIRS/Aqua L1B Infrared (IR) quality assurance subset V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/VV622VHH2LXV. https://disc.gsfc.nasa.gov/datacollection/AIRIBQAP_005.html. Digital Science Data.",
-            "issued": "2002-08-30",
-            "temporal": "2002-08-30T00:00:00Z/2024-12-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-24",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "infrared wavelengths"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1243477368-GES_DISC",
-            "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The AIRS IR Level 1B QA Subset contains Quality Assurance (QA) parameters that a user of may use to filter AIRS IR Level 1B radiance data to create a subset of analysis. QA parameters indicate quality of granule-per-channel, scan-per-channel, field of view, and channel and should be accessed before any data of analysis. It also contains \"glintlat\", \"glintlon\", and \"sun_glint_distant\" that users can use to check for possibility of solar glint contamination.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRIBQAP",
             "creator": "AIRS project",
-            "title": "AIRS/Aqua L1B Infrared (IR) quality assurance subset V005 (AIRIBQAP) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRIBQAP_005.gif",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. The AIRS IR Level 1B QA Subset contains Quality Assurance (QA) parameters that a user of may use to filter AIRS IR Level 1B radiance data to create a subset of analysis. QA parameters indicate quality of granule-per-channel, scan-per-channel, field of view, and channel and should be accessed before any data of analysis. It also contains \"glintlat\", \"glintlon\", and \"sun_glint_distant\" that users can use to check for possibility of solar glint contamination.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVV622VHH2LXV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVV622VHH2LXV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1532349,107 +1532327,112 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRIBQAP_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRIBQAP_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level1/AIRIBQAP.005/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://airsl1.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level1/AIRIBQAP.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airsl1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level1/AIRIBQAP.005/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://airsl1.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level1/AIRIBQAP.005/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRIBQAP+005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRIBQAP+005",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
-                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument, algorithms, and other AIRS-related activities can be found.",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS home page at NASA/JPL. General information on the AIRS instrument, algorithms, and other AIRS-related activities can be found.",
+                    "downloadURL": "https://airs.jpl.nasa.gov/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=AIRS+Documentation",
-                    "description": "AIRS Documentation Page",
                     "@type": "dcat:Distribution",
+                    "description": "AIRS Documentation Page",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=AIRS+Documentation",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRIBRAD.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.3_ScienceDataProductDocumentation/3.3.4_ProductGenerationAlgorithms/README.AIRIBRAD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.7_ScienceDataProductValidation/V5_CalVal_Status_Summary.pdf",
-                    "description": "Summary of validation status of products",
                     "@type": "dcat:Distribution",
+                    "description": "Summary of validation status of products",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/AIRS/3.7_ScienceDataProductValidation/V5_CalVal_Status_Summary.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/sites/default/files/atbd/AIRS_L1B_ATBD_Part_1.pdf",
-                    "description": "ATBD documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ATBD documentation",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/sites/default/files/atbd/AIRS_L1B_ATBD_Part_1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRIBQAP_005.gif",
+            "identifier": "C1243477368-GES_DISC",
+            "issued": "2002-08-30",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "infrared wavelengths"
+            ],
+            "landingPage": "https://doi.org/10.5067/VV622VHH2LXV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRIBQAP",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-08-30T00:00:00Z/2024-12-30T00:00:00Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L1B Infrared (IR) quality assurance subset V005 (AIRIBQAP) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000011-CDDIS.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS.",
-            "issued": "2000-11-05",
-            "temporal": "2000-11-05T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-06-14",
-            "keyword": [
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-cddis@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
-            },
-            "identifier": "C1000000011-CDDIS",
             "description": "Satellite and receiver clock products derived from analysis of Global Navigation Satellite System (GNSS) data. These products are the generated by analysis centers in support of the International GNSS Service (IGS) and combined by the IGS analysis coordinator to form the official IGS rapid clock product (daily).",
-            "title": "CDDIS_GNSS_products_clocks_rapid",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1532458,141 +1532441,170 @@
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1000000011-CDDIS",
+            "issued": "2000-11-05",
+            "keyword": [
+                "nasa"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000011-CDDIS.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-06-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-11-05T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CDDIS_GNSS_products_clocks_rapid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/945/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2016-01-14",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kai Goebel",
                 "hasEmail": "mailto:kai.goebel@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_945",
             "description": "This paper proposes a recursive receding horizon path planning algorithm for unmanned vehicles\r\nin nonuniform environments. In the proposed algorithm, the map is described by grids in which nodes are defined on corners of grids. The planning algorithm considers the map as four areas, namely, implementation, observation, explored, and unknown. The Implementation area is a subset\r\nof the Observation area, whereas the Explored area is the union of all the previous Observation areas. The path is planned with a receding horizon planning strategy to generate waypoints and in-between map updates. When a new map update occurs, the path is replanned within the current Observation area if necessary. If no such path exists, the search is extended to the Explored area. Paths can be planned by recursively searching available nodes inside the Explored area that can be connected to available nodes on the boundary of the Explored area. A robot platform is employed to conduct a series of experiments in a laboratory environment to verify the proposed path planning algorithm.",
-            "title": "A Recursive Receding Horizon Planning for Unmanned Vehicles",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2015_RecedingHorizon_Zhang.pdf",
-                    "description": "paper",
                     "@type": "dcat:Distribution",
+                    "description": "paper",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2015_RecedingHorizon_Zhang.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2015_RecedingHorizon_Zhang.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_945",
+            "issued": "2016-01-14",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/945/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "A Recursive Receding Horizon Planning for Unmanned Vehicles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-SA-COMPIL-3-SATPOL-V1.0",
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
-                "satellite",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This compilation of polarimetry of planetary satellites has been compiled from the published literature and from unpublished results by Zaitsev, Rosenbush, and Kiselev. Geometric observational circumstances, calculated using the JPL Horizons ephemeris system, are also included. This version of the compilation is dated April 15, 2012.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-sa-compil-3-satpol-v1.0_vrkx-ss8k",
+            "issued": "2021-05-21",
+            "keyword": [
+                "satellite",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-SA-COMPIL-3-SATPOL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-sa-compil-3-satpol-v1.0_vrkx-ss8k",
-            "description": "This compilation of polarimetry of planetary satellites has been compiled from the published literature and from unpublished results by Zaitsev, Rosenbush, and Kiselev. Geometric observational circumstances, calculated using the JPL Horizons ephemeris system, are also included. This version of the compilation is dated April 15, 2012.",
-            "title": "POLARIMETRY OF PLANETARY SATELLITES V1.0",
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
+            "title": "POLARIMETRY OF PLANETARY SATELLITES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-3-AST2-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Lutetia flyby mission phase, which took place between 2010-06-07 and 2010-09-10.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-3-ast2-v1.0_vrnc-7hmz",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "21 lutetia",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-A%2FCAL-ALICE-3-AST2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-a-cal-alice-3-ast2-v1.0_vrnc-7hmz",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Lutetia flyby mission phase, which took place between 2010-06-07 and 2010-09-10.",
-            "title": "ROSETTA-ORBITER LUTETIA/CAL ALICE 3 AST2 V1.0",
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
+            "title": "ROSETTA-ORBITER LUTETIA/CAL ALICE 3 AST2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985645-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "Sentinel-1B Dual-pol ground projected high and full resolution images",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1327985645-ASF",
             "issued": "2016-08-20",
-            "temporal": "2016-04-25T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
             "keyword": [
                 "solid earth",
                 "topography",
@@ -1532619,242 +1532631,211 @@
                 "biosphere",
                 "agriculture"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1327985645-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-17",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1327985645-ASF",
-            "description": "Sentinel-1B Dual-pol ground projected high and full resolution images",
-            "title": "SENTINEL-1B_DUAL_POL_GRD_HIGH_RES",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
-                    "description": "Vertex, the ASF search and download interface",
-                    "@type": "dcat:Distribution",
-                    "title": "Download this dataset"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-04-25T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SENTINEL-1B_DUAL_POL_GRD_HIGH_RES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-HIRISE-3-RDR-V1.0",
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
-                "mars",
-                "mars reconnaissance orbiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset includes reduced data records from the HiRISE instrument on MRO.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-hirise-3-rdr-v1.0_vrpr-rcwj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "mars reconnaissance orbiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MRO-M-HIRISE-3-RDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mro-m-hirise-3-rdr-v1.0_vrpr-rcwj",
-            "description": "This dataset includes reduced data records from the HiRISE instrument on MRO.",
-            "title": "MRO MARS HIGH RESOLUTION IMAGE SCIENCE EXPERIMENT RDR V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MRO MARS HIGH RESOLUTION IMAGE SCIENCE EXPERIMENT RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M22-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m22-strlight-v1.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "vega",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-ESC4-67P-M22-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-esc4-67p-m22-strlight-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the COMET ESCORT 4 mission phase, covering the period from 2015-10-20T23:25:00.000 to 2015-11-17T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP022 RDR-STRLIGHT V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 ESC4-MTP022 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/666",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Huete, A. R. 2003. PROVE MQUALS Reflectance at Jornada Experimental Range, New Mexico, 1997. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/666",
-            "issued": "2023-11-19",
-            "temporal": "1997-05-23T00:00:00Z/1997-05-25T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-20",
-            "keyword": [
-                "earth science",
-                "surface radiative properties",
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
-            "identifier": "C2804795305-ORNL_CLOUD",
             "description": "This study utilized low flying, aircraft-based radiometers for optical characterization of top-of-the-canopy reflectance at Jornada Experimental Range in New Mexico during the Prototype Validation Experiment (PROVE) in May 1997. The objective was to examine the usefulness of low-flying aircraft for Moderate Resolution Imaging Spectroradiometer (MODIS) validation of land products.",
-            "graphic-preview-description": "Browse Image",
-            "title": "PROVE MQUALS Reflectance at Jornada Experimental Range, New Mexico, 1997",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F666",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F666",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/prove/jornada_mquals/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/prove/jornada_mquals/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/PROVE/guides/prove_mquals_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/PROVE/guides/prove_mquals_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/666",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/666",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_mquals/comp/MQUALS_radiometer.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_mquals/comp/MQUALS_radiometer.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_mquals/comp/prove_mquals_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/prove/jornada_mquals/comp/prove_mquals_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/prove_logo_square.png",
+            "identifier": "C2804795305-ORNL_CLOUD",
+            "issued": "2023-11-19",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/666",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "32.5 -106.75",
+            "temporal": "1997-05-23T00:00:00Z/1997-05-25T23:59:59Z",
             "theme": [
                 "PROVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PROVE MQUALS Reflectance at Jornada Experimental Range, New Mexico, 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR_L3.01",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR_L3.01.",
-            "issued": "2021-02-17",
-            "temporal": "2015-06-13T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-17",
-            "keyword": [
-                "ocean optics",
-                "oceans",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Frouin",
                 "hasEmail": "mailto:rfrouin@ucsd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2081907121-LARC_ASDC",
             "description": "DSCOVR_EPIC_L3_PAR_01 is the Deep Space Climate Observatory (DSCOVR) Earth Polychromatic Imaging Camera (EPIC) Level 3 photosynthetically available radiation (PAR) version 1 data product. The EPIC observations of the Earth\u2019s surface lit by the Sun made 13 times during the day in spectral bands centered on 443, 551, and 680 nm are used to estimate daily mean PAR at the ice-free ocean surface. PAR is defined as the quantum energy flux from the Sun in the 400-700 nm range. Daily mean PAR is the 24-hour averaged planar flux in that spectral range reaching the surface. It is expressed in E.m-2.d-1 (Einstein per meter squared per day). The factor required to convert E.m-2 d-1 units to mW.cm-2.\u00b5m-1 units is equal to 0.838 to an inaccuracy of a few percent regardless of meteorological conditions. The EPIC daily mean PAR product is generated on Plate Carr\u00e9e (equal-angle) grid with 18.4 km resolution at the equator and on 18.4 km equal-area grid, i.e., the product is compatible with Ocean Biology Processing Group ocean color products.\r\nThe EPIC PAR algorithm uses a budget approach, in which the solar irradiance reaching the surface is obtained by subtracting from the irradiance arriving at the top of the atmosphere (known), the irradiance reflected to space (estimated from the EPIC Level 1b radiance data), taking into account atmospheric transmission (modeled). Clear and cloudy regions within a pixel do not need to be distinguished, which dismisses the need for often-arbitrary assumptions about cloudiness distribution and is therefore adapted to the relatively large EPIC pixels. A daily mean PAR is estimated on the source grid for each EPIC instantaneous daytime observation, assuming no cloudiness change during the day, and the individual estimates are remapped and weight-averaged using the cosine of the Sun zenith angle. In the computations, wind speed, surface pressure, and water vapor amount are extracted from NCEP (National Centers for Environmental Prediction) Reanalysis 2 data, aerosol optical thickness and angstrom coefficient from MERRA-2 (Modern-Era Retrospective analysis for Research and Applications, Version 2) data, and ozone amount from EPIC Level 2 data. Areas contaminated by sun glint are excluded using a threshold on sun glint reflectance calculated using wind data. Ice masking is based on NSIDC (National Snow and Ice Data Center) near real time ice fraction data. \r\nAdditional information about the EPIC ocean surface PAR products can be found at the NASA DSCOVR: EPIC website: https://epic.gsfc.nasa.gov/, under \u201cScience -> Products -> Ocean Surface\u201d (https://epic.gsfc.nasa.gov/science/products/ocean).",
-            "title": "DSCOVR EPIC Level 3 PAR",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR%2FDSCOVR_EPIC_L3_PAR_L3.01",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEPIC%2FDSCOVR%2FDSCOVR_EPIC_L3_PAR_L3.01",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1532864,132 +1532845,133 @@
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2081907121-LARC_ASDC",
-                    "description": "Earthdata Search for DSCOVR_EPIC_L3_PAR_01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for DSCOVR_EPIC_L3_PAR_01 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2081907121-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/DSCOVR",
-                    "description": "ASDC Data and Information for DSCOVR",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for DSCOVR",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/DSCOVR",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_EPIC_PAR-Data-access.pdf",
-                    "description": "DSCOVR EPIC PAR DATA Access instructions",
                     "@type": "dcat:Distribution",
+                    "description": "DSCOVR EPIC PAR DATA Access instructions",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/dscovr/DSCOVR_EPIC_PAR-Data-access.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR_L3.01",
-                    "description": "DOI data set landing page for DSCOVR_EPIC_L3_PAR_L3.01",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for DSCOVR_EPIC_L3_PAR_L3.01",
+                    "downloadURL": "https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR_L3.01",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L3_PAR_01/",
-                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L3_PAR_01",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for DSCOVR_EPIC_L3_PAR_01",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/DSCOVR/EPIC/L3_PAR_01/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DSCOVR/EPIC/L3_PAR_01/contents.html",
-                    "description": "OPeNDAP data access for DSCOVR_EPIC_L3_PAR_01",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for DSCOVR_EPIC_L3_PAR_01",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/DSCOVR/EPIC/L3_PAR_01/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2081907121-LARC_ASDC",
+            "issued": "2021-02-17",
+            "keyword": [
+                "ocean optics",
+                "oceans",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/EPIC/DSCOVR/DSCOVR_EPIC_L3_PAR_L3.01",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -180.0 -90.0 180.0 90.0 180.0 90.0 -180.0 -90.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2015-06-13T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "DSCOVR",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "DSCOVR EPIC Level 3 PAR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-SUMM-SECTOR-15MIN-V1.1",
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
+            "description": "This data set consists of resampled data from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was in the vicinity of Jupiter. This instrument measures the intensities of in-situ charged particles (>26 keV electrons and >30 keV ions) with various levels of discrimination based on energy, mass species, and angular arrival direction. A subset of almost 100 LECP channels are included with this data set. The LECP data are globally calibrated to the extent possible (see below) and they are time averaged to about 15 minute time intervals with the exact beginning and ending times for those intervals matching the LECP instrumental cycle periods (the angular scanning periods). The data is in the form of 'rate' data which has not been converted  to the usual physical units. Data records for the version 1.1 data set provide all data for a given channel and time period (8 sectors, plus the average for all sectors) in a single record.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-summ-sector-15min-v1.1_vrwj-5phw",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-LECP-4-SUMM-SECTOR-15MIN-V1.1",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-lecp-4-summ-sector-15min-v1.1_vrwj-5phw",
-            "description": "This data set consists of resampled data from the Low Energy Charged Particle (LECP) experiment on Voyager 2 while the spacecraft was in the vicinity of Jupiter. This instrument measures the intensities of in-situ charged particles (>26 keV electrons and >30 keV ions) with various levels of discrimination based on energy, mass species, and angular arrival direction. A subset of almost 100 LECP channels are included with this data set. The LECP data are globally calibrated to the extent possible (see below) and they are time averaged to about 15 minute time intervals with the exact beginning and ending times for those intervals matching the LECP instrumental cycle periods (the angular scanning periods). The data is in the form of 'rate' data which has not been converted  to the usual physical units. Data records for the version 1.1 data set provide all data for a given channel and time period (8 sectors, plus the average for all sectors) in a single record.",
-            "title": "VG2 JUP LECP CALIBRATED RESAMPLED SECTORED 15MIN V1.1",
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
+            "title": "VG2 JUP LECP CALIBRATED RESAMPLED SECTORED 15MIN V1.1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/vrxq-dqar",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1977-01-01/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "geography",
-                "wise",
-                "nen",
-                "space science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jennifer Blue",
                 "hasEmail": "mailto:jblue@usgs.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000038__67",
+            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
             "description": "Planetary nomenclature, like terrestrial nomenclature, is used to uniquely identify a feature on the surface of a planet or satellite so that the feature can be easily located, described, and discussed. This gazetteer contains detailed information about all names of topographic and albedo features on planets and satellites (and some planetary ring and ring-gap systems) that the International Astronomical Union (IAU) has named and approved from its founding in 1919 through the present time.",
-            "title": "Gazetteer of Planetary Nomenclature",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1532997,276 +1532979,296 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "describedBy": "http://planetarynames.wr.usgs.gov/Page/Website",
-            "accrualPeriodicity": "irregular"
+            "identifier": "NASA-0000038__67",
+            "issued": "2018-06-25",
+            "keyword": [
+                "geography",
+                "wise",
+                "nen",
+                "space science"
+            ],
+            "landingPage": "https://data.nasa.gov/d/vrxq-dqar",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "temporal": "1977-01-01/2014-01-01",
+            "title": "Gazetteer of Planetary Nomenclature"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CYGNS-L1X32",
             "citation": "CYGNSS. 2024-03-05. CYGNSS Level 1 Science Data Record Version 3.2. Version 3.2. CYGNSS Level 1 Science Data Record Version 3.2.  PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government,  PO.DAAC. https://doi.org/10.5067/CYGNS-L1X32. https://cygnss.engin.umich.edu/. CYGNSS, PO.DAAC, 2024-01-31, CYGNSS Level 1 Science Data Record Version 3.2, https://cygnss.engin.umich.edu/.",
-            "issued": "2024-01-01",
-            "temporal": "2018-08-01T00:00:00Z/2024-11-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-30",
-            "references": [
-                "https://doi.org/10.1109/TGRS.2021.3120026",
-                "https://doi.org/10.3390/rs13214313",
-                "https://doi.org/10.1109/TGRS.2021.3070238"
-            ],
-            "keyword": [
-                "earth science",
-                "radar",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2832195379-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This CYGNSS Level 1 (L1) science data record dataset contains the version 3.2 geo-located Delay Doppler Maps (DDMs) calibrated into Power Received (Watts) and Bistatic Radar Cross Section (BRCS) expressed in units of m2 from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. This version supersedes Version 3.1: https://doi.org/10.5067/CYGNS-L1X31. Other useful scientific and engineering measurement parameters include the DDM of Normalized Bistatic Radar Cross Section (NBRCS), the Delay Doppler Map Average (DDMA) of the NBRCS near the specular reflection point, and the Leading Edge Slope (LES) of the integrated delay waveform. The L1 dataset contains a number of other engineering and science measurement parameters, including sets of quality flags/indicators, error estimates, and bias estimates as well as a variety of orbital, spacecraft/sensor health, timekeeping, and geolocation parameters. At most, 8 netCDF data files (each file corresponding to a unique spacecraft in the CYGNSS constellation) are provided each day; under nominal conditions, there are typically 6-8 spacecraft retrieving data each day, but this can be maximized to 8 spacecraft under special circumstances in which higher than normal retrieval frequency is needed (i.e., during tropical storms and or hurricanes). Latency is approximately 6 days (or better) from the last recorded measurement time. <br><br>\r\nThe correction for coarse quantization effects that was implemented in v3.1 for the signal portion of the DDM has been updated to include a correction to the noise floor portion of the DDM. This update is found to improve the sensitivity to soil moisture over land and to have a minimal effect on the sensitivity to wind speed over ocean. An update is made to the correction for the temperature dependence of the receiver electronics. This update reduces slow variations in calibration bias associated with a ~60 day oscillation in the mean temperature of the satellites. L1 variables over land and ocean are now combined in common netcdf data files, with additional details added regarding the specular point calculation over land. Nadir (science) antenna pattern and NBRCS rescaling has been updated to improve the inter-satellite consistency of the L1 calibration.<br><br>\r\nThe CYGNSS is a NASA Earth System Science Pathfinder Mission that is intended to collect the first frequent space\u2010based measurements of surface wind speeds in the inner core of tropical cyclones. Made up of a constellation of eight micro-satellites, the observatories provide nearly gap-free Earth coverage using an orbital inclination of approximately 35\u00b0 from the equator, with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours. This inclination allows CYGNSS to measure ocean surface winds between approximately 38\u00b0 N and 38\u00b0 S latitude. This range includes the critical latitude band for tropical cyclone formation and movement.",
-            "release-place": "PO.DAAC",
-            "series-name": "CYGNSS Level 1 Science Data Record Version 3.2",
             "creator": "CYGNSS",
-            "title": "CYGNSS Level 1 Science Data Record Version 3.2",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_V3.2.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This CYGNSS Level 1 (L1) science data record dataset contains the version 3.2 geo-located Delay Doppler Maps (DDMs) calibrated into Power Received (Watts) and Bistatic Radar Cross Section (BRCS) expressed in units of m2 from the Delay Doppler Mapping Instrument aboard the CYGNSS satellite constellation. This version supersedes Version 3.1: https://doi.org/10.5067/CYGNS-L1X31. Other useful scientific and engineering measurement parameters include the DDM of Normalized Bistatic Radar Cross Section (NBRCS), the Delay Doppler Map Average (DDMA) of the NBRCS near the specular reflection point, and the Leading Edge Slope (LES) of the integrated delay waveform. The L1 dataset contains a number of other engineering and science measurement parameters, including sets of quality flags/indicators, error estimates, and bias estimates as well as a variety of orbital, spacecraft/sensor health, timekeeping, and geolocation parameters. At most, 8 netCDF data files (each file corresponding to a unique spacecraft in the CYGNSS constellation) are provided each day; under nominal conditions, there are typically 6-8 spacecraft retrieving data each day, but this can be maximized to 8 spacecraft under special circumstances in which higher than normal retrieval frequency is needed (i.e., during tropical storms and or hurricanes). Latency is approximately 6 days (or better) from the last recorded measurement time. <br><br>\r\nThe correction for coarse quantization effects that was implemented in v3.1 for the signal portion of the DDM has been updated to include a correction to the noise floor portion of the DDM. This update is found to improve the sensitivity to soil moisture over land and to have a minimal effect on the sensitivity to wind speed over ocean. An update is made to the correction for the temperature dependence of the receiver electronics. This update reduces slow variations in calibration bias associated with a ~60 day oscillation in the mean temperature of the satellites. L1 variables over land and ocean are now combined in common netcdf data files, with additional details added regarding the specular point calculation over land. Nadir (science) antenna pattern and NBRCS rescaling has been updated to improve the inter-satellite consistency of the L1 calibration.<br><br>\r\nThe CYGNSS is a NASA Earth System Science Pathfinder Mission that is intended to collect the first frequent space\u2010based measurements of surface wind speeds in the inner core of tropical cyclones. Made up of a constellation of eight micro-satellites, the observatories provide nearly gap-free Earth coverage using an orbital inclination of approximately 35\u00b0 from the equator, with a mean (i.e., average) revisit time of seven hours and a median revisit time of three hours. This inclination allows CYGNSS to measure ocean surface winds between approximately 38\u00b0 N and 38\u00b0 S latitude. This range includes the critical latitude band for tropical cyclone formation and movement.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L1X32",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCYGNS-L1X32",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://forum.earthdata.nasa.gov/viewtopic.php?t=5657",
-                    "description": "Forum Post Capturing Changes to CYGNSS Sampling Rate",
                     "@type": "dcat:Distribution",
+                    "description": "Forum Post Capturing Changes to CYGNSS Sampling Rate",
+                    "downloadURL": "https://forum.earthdata.nasa.gov/viewtopic.php?t=5657",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docs.google.com/spreadsheets/d/1AFAZanVGDApLSnJQAAdPfOKoJQs0jnB8ZvIuD1Z5mAc/edit#gid=0",
-                    "description": "Google Sheet Log of Anomalous CYGNSS Sampling Events",
                     "@type": "dcat:Distribution",
+                    "description": "Google Sheet Log of Anomalous CYGNSS Sampling Events",
+                    "downloadURL": "https://docs.google.com/spreadsheets/d/1AFAZanVGDApLSnJQAAdPfOKoJQs0jnB8ZvIuD1Z5mAc/edit#gid=0",
+                    "mediaType": "text/html",
                     "title": "View this dataset's documented anomalies"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2015.2502245",
-                    "description": "Gleason, S., C. Ruf, M. P. Clarizia, A. O'Brien, 'Calibration and Unwrapping of the Normalized Scattering Cross Section for the Cyclone Global Navigation Satellite System (CYGNSS)', IEEE Trans. Geosci. Remote Sens., doi:10.1109/TGRS.2015.2502245, 2016.",
                     "@type": "dcat:Distribution",
+                    "description": "Gleason, S., C. Ruf, M. P. Clarizia, A. O'Brien, 'Calibration and Unwrapping of the Normalized Scattering Cross Section for the Cyclone Global Navigation Satellite System (CYGNSS)', IEEE Trans. Geosci. Remote Sens., doi:10.1109/TGRS.2015.2502245, 2016.",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2015.2502245",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/doi/10.1175/BAMS-D-14-00218.1",
-                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., R. Atlas, P. Chang, M. Clarizia, J. Garrison, S. Gleason, S. Katzberg, Z. Jelenak, J. Johnson, S. Majumdar, A. O'Brien, D. Posselt, A. Ridley, R. Rose, V. Zavorotny (2015). New Ocean Winds Satellite Mission to Probe Hurricanes and Tropical Convection. Bull. Amer. Meteor. Soc., doi:10.1175/BAMS-D-14-00218.1.",
+                    "downloadURL": "https://journals.ametsoc.org/doi/10.1175/BAMS-D-14-00218.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2019GL085134",
-                    "description": "A CYGNSS-based algorithm for the detection of inland waterbodies",
                     "@type": "dcat:Distribution",
+                    "description": "A CYGNSS-based algorithm for the detection of inland waterbodies",
+                    "downloadURL": "https://doi.org/10.1029/2019GL085134",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
-                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser, 2019. In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
                     "@type": "dcat:Distribution",
+                    "description": "Ruf, C., S. Asharaf, R. Balasubramaniam, S. Gleason, T. Lang, D. McKague, D. Twigg, and D. Waliser, 2019. In-Orbit Performance of the Constellation of CYGNSS Hurricane Satellites. Bull. Amer. Meteor. Soc., 100, 2009 - 2023, https://doi.org/10.1175/BAMS-D-18-0337.1.",
+                    "downloadURL": "https://doi.org/10.1175/BAMS-D-18-0337.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0136_L1A_DDM_Calibration_ATBD_R4.pdf",
-                    "description": "Level 1A DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0136, Rev 4, 8 December 2023.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1A DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0136, Rev 4, 8 December 2023.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0136_L1A_DDM_Calibration_ATBD_R4.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0137_L1B_DDM_Calibration_ATBD_R6.pdf",
-                    "description": "Level 1B DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0137, Rev 6, 8 December 2023.",
                     "@type": "dcat:Distribution",
+                    "description": "Level 1B DDM Calibration Algorithm Theoretical Basis Document, S. Gleason, CYGNSS Project Document 148-0137, Rev 6, 8 December 2023.",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0137_L1B_DDM_Calibration_ATBD_R6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/06/CYGNSS_Handbook_April2016.pdf",
-                    "description": "Deriving Surface Winds from Tropical Cyclones",
                     "@type": "dcat:Distribution",
+                    "description": "Deriving Surface Winds from Tropical Cyclones",
+                    "downloadURL": "https://cygnss.engin.umich.edu/wp-content/uploads/sites/534/2021/06/CYGNSS_Handbook_April2016.pdf",
+                    "mediaType": "application/pdf",
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
-                    "downloadURL": "https://github.com/podaac/data-readers",
-                    "description": "Generic Data Readers",
                     "@type": "dcat:Distribution",
+                    "description": "Generic Data Readers",
+                    "downloadURL": "https://github.com/podaac/data-readers",
+                    "mediaType": "text/html",
                     "title": "View this dataset's data recipes"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0346-10_Level_1_netCDF_Data_Dictionary.xlsx",
-                    "description": "CYGNSS L1 V3.2 netCDF Data Dictionary",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS L1 V3.2 netCDF Data Dictionary",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/148-0346-10_Level_1_netCDF_Data_Dictionary.xlsx",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_V3.2.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_V3.2.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2021.3120026",
-                    "description": "Gleason, S., M. M. Al-Khaldi, C. Ruf, D. S. McKague, T. Wang, A. Russel (2021). Characterizing and Mitigating Digital Sampling Effects on the CYGNSS Level 1 Calibration. IEEE Trans. Geosci. Remote Sens., doi: 10.1109/TGRS.2021.3120026.",
                     "@type": "dcat:Distribution",
+                    "description": "Gleason, S., M. M. Al-Khaldi, C. Ruf, D. S. McKague, T. Wang, A. Russel (2021). Characterizing and Mitigating Digital Sampling Effects on the CYGNSS Level 1 Calibration. IEEE Trans. Geosci. Remote Sens., doi: 10.1109/TGRS.2021.3120026.",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2021.3120026",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3390/rs13214313",
-                    "description": "Pascual, D., M. P. Clarizia, C. S. Ruf (2021). Improved CYGNSS Wind Speed Retrieval Using Significant Wave Height Correction. Remote Sensing, doi: 10.3390/rs13214313.",
                     "@type": "dcat:Distribution",
+                    "description": "Pascual, D., M. P. Clarizia, C. S. Ruf (2021). Improved CYGNSS Wind Speed Retrieval Using Significant Wave Height Correction. Remote Sensing, doi: 10.3390/rs13214313.",
+                    "downloadURL": "https://doi.org/10.3390/rs13214313",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2832195379-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2832195379-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2832195379-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2832195379-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1109/TGRS.2021.3070238",
-                    "description": "Wang, T., Ruf, C. S., Gleason, S., O'Brien, A. J., McKague, D. S., Block, B. P., Russel, A. 2021. Dynamic Calibration of GPS Effective Isotropic Radiated Power for GNSS-Reflectometry Earth Remote Sensing, IEEE Trans. Geosci. Remote Sens. 10.1109/TGRS.2021.3070238.",
                     "@type": "dcat:Distribution",
+                    "description": "Wang, T., Ruf, C. S., Gleason, S., O'Brien, A. J., McKague, D. S., Block, B. P., Russel, A. 2021. Dynamic Calibration of GPS Effective Isotropic Radiated Power for GNSS-Reflectometry Earth Remote Sensing, IEEE Trans. Geosci. Remote Sens. 10.1109/TGRS.2021.3070238.",
+                    "downloadURL": "https://doi.org/10.1109/TGRS.2021.3070238",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_1.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_1.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_2.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_2.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_3.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_3.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_4.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_4.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_5.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_5.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_6.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_6.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_7.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_7.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_8.txt",
-                    "description": "Updated Monthly",
                     "@type": "dcat:Distribution",
+                    "description": "Updated Monthly",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/cygnss/open/L1/docs/att_tables/Attitude_Table_FM_8.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3998/mpub.12741920",
-                    "description": "CYGNSS Handbook",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Handbook",
+                    "downloadURL": "https://doi.org/10.3998/mpub.12741920",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cygnss.engin.umich.edu/",
-                    "description": "CYGNSS Mission Page at University of Michigan",
                     "@type": "dcat:Distribution",
+                    "description": "CYGNSS Mission Page at University of Michigan",
+                    "downloadURL": "https://cygnss.engin.umich.edu/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/CYGNSS_L1_V3.2.jpg",
+            "identifier": "C2832195379-POCLOUD",
+            "issued": "2024-01-01",
+            "keyword": [
+                "earth science",
+                "radar",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/CYGNS-L1X32",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1109/TGRS.2021.3120026",
+                "https://doi.org/10.3390/rs13214313",
+                "https://doi.org/10.1109/TGRS.2021.3070238"
+            ],
+            "release-place": "PO.DAAC",
+            "series-name": "CYGNSS Level 1 Science Data Record Version 3.2",
             "spatial": "-180.0 -40.0 180.0 40.0",
+            "temporal": "2018-08-01T00:00:00Z/2024-11-04T00:00:00Z",
             "theme": [
                 "CYGNSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CYGNSS Level 1 Science Data Record Version 3.2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LORRI-2-PLUTO-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons                Long Range Reconnaissance Imager                                       instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains LORRI observations taken during the               the Approach (Jan-Jul, 2015) and Encounter mission sub-phases,           including flyby observations taken on 14 July, 2015; the data are        limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.  Refer to the data         set description above and the sequence table provided in the             documentation for more detail about which observations are present       in this data set.                                                        This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  These include Pluto Charon, Nix and Hydra observations   from Approach, the day of the flyby, and Departure, lossless downlinks   of images downlinked with lossy compression in version 1.0, Nix orbit    determination observations, Multi-maps and VIS-UV maps taken in          coordination with ALICE, High-phase and departure imaging, satellite     photometry, non-critical navigation imaging, Kerberos and Styx           imaging, KBO 1994 JR1 observations and departure ring-search             observations taken in November, 2015, Charon dark side lit by            Pluto-shine, and several other observations.                             The lossy images from Version 1.0 were recalibrated, including           expanding the 'bad' pixel designation of 8x8 boxes affected by the       first 34 pixels of header information in the calibrated quality map.     Also, updates were made to the documentation and catalog files,          primarily to resolve liens from the V1.0 peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-lorri-2-pluto-v2.0_vrxy-r5wm",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "nix",
                 "kerberos",
@@ -1533276,473 +1533278,483 @@
                 "new horizons",
                 "pluto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-P-LORRI-2-PLUTO-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-p-lorri-2-pluto-v2.0_vrxy-r5wm",
-            "description": "This data set contains Raw data taken by the New Horizons                Long Range Reconnaissance Imager                                       instrument during the                                                    Pluto encounter                                                        mission phase.  This is VERSION 2.0 of this data set.                    This data set contains LORRI observations taken during the               the Approach (Jan-Jul, 2015) and Encounter mission sub-phases,           including flyby observations taken on 14 July, 2015; the data are        limited to those downlinked from the spacecraft as of the end of         January, 2016.  The rest of the downlinked data for this mission         phase will be delivered in a future data set.  Refer to the data         set description above and the sequence table provided in the             documentation for more detail about which observations are present       in this data set.                                                        This is version 2.0 of this data set.  Changes since version 1.0         include data downlinked between the end of July, 2015 and the end of     January, 2016.  These include Pluto Charon, Nix and Hydra observations   from Approach, the day of the flyby, and Departure, lossless downlinks   of images downlinked with lossy compression in version 1.0, Nix orbit    determination observations, Multi-maps and VIS-UV maps taken in          coordination with ALICE, High-phase and departure imaging, satellite     photometry, non-critical navigation imaging, Kerberos and Styx           imaging, KBO 1994 JR1 observations and departure ring-search             observations taken in November, 2015, Charon dark side lit by            Pluto-shine, and several other observations.                             The lossy images from Version 1.0 were recalibrated, including           expanding the 'bad' pixel designation of 8x8 boxes affected by the       first 34 pixels of header information in the calibrated quality map.     Also, updates were made to the documentation and catalog files,          primarily to resolve liens from the V1.0 peer review.",
-            "title": "NEW HORIZONS                            \n      LORRI PLUTO ENCOUNTER                                                   \n      RAW V2.0",
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
+            "title": "NEW HORIZONS                            \n      LORRI PLUTO ENCOUNTER                                                   \n      RAW V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4GH9FVG",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for International Earth Science Information Network - CIESIN - Columbia University, International Food Policy Research Institute - IFPRI, The World Bank, and Centro Internacional de Agricultura Tropical - CIAT. 2011-09-26. Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extents Grid. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4GH9FVG. https://doi.org/10.7927/H4GH9FVG.",
-            "issued": "2011-09-26",
-            "temporal": "1995-07-01T00:00:00Z/1995-07-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2011-09-26",
-            "references": [
-                "https://doi.org/10.7927/H4VT1Q1H",
-                "https://doi.org/10.7927/H4CR5R8J",
-                "https://doi.org/10.7927/H44B2Z74",
-                "https://doi.org/10.7927/H40K26HS",
-                "https://doi.org/10.7927/H4R20Z93",
-                "https://doi.org/10.7927/H4M906KR",
-                "https://doi.org/10.7927/H48050JH"
-            ],
-            "keyword": [
-                "earth science",
-                "boundaries",
-                "human dimensions"
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
-            "identifier": "C2210245038-SEDAC",
-            "description": "The Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extents Grid distinguishes urban and rural areas based on a combination of population counts (persons), settlement points, and the presence of Nighttime Lights. Areas are defined as urban where contiguous lighted cells from the Nighttime Lights or approximated urban extents based on buffered settlement points  for which the total population is greater than 5,000 persons. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the International Food Policy Research Institute (IFPRI), The World Bank, and Centro Internacional de Agricultura Tropical (CIAT).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for International Earth Science Information Network - CIESIN - Columbia University, International Food Policy Research Institute - IFPRI, The World Bank, and Centro Internacional de Agricultura Tropical - CIAT",
-            "title": "Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extents Grid",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extents Grid distinguishes urban and rural areas based on a combination of population counts (persons), settlement points, and the presence of Nighttime Lights. Areas are defined as urban where contiguous lighted cells from the Nighttime Lights or approximated urban extents based on buffered settlement points  for which the total population is greater than 5,000 persons. This data set is produced by the Columbia University Center for International Earth Science Information Network (CIESIN) in collaboration with the International Food Policy Research Institute (IFPRI), The World Bank, and Centro Internacional de Agricultura Tropical (CIAT).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4GH9FVG",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4GH9FVG",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-urban-extents/globalextents-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/grump-v1/grump-v1-urban-extents/globalextents-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/grump-v1-urban-extents/maps",
+            "identifier": "C2210245038-SEDAC",
+            "issued": "2011-09-26",
+            "keyword": [
+                "earth science",
+                "boundaries",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4GH9FVG",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2011-09-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4VT1Q1H",
+                "https://doi.org/10.7927/H4CR5R8J",
+                "https://doi.org/10.7927/H44B2Z74",
+                "https://doi.org/10.7927/H40K26HS",
+                "https://doi.org/10.7927/H4R20Z93",
+                "https://doi.org/10.7927/H4M906KR",
+                "https://doi.org/10.7927/H48050JH"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -56.0 180.0 84.0",
+            "temporal": "1995-07-01T00:00:00Z/1995-07-01T00:00:00Z",
             "theme": [
                 "GRUMP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Rural-Urban Mapping Project, Version 1 (GRUMPv1): Urban Extents Grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/J1JMR-ENH0C",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Shannon Brown. 2010-10-06. JASON-1 ENHANCED JASON MICROWAVE RADIOMETER. Version 1. JASON-1_JMR_ENH. JPL. Archived by National Aeronautics and Space Administration, U.S. Government, JPL. https://doi.org/10.5067/J1JMR-ENH0C. https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/preview/L2/jmr_enh/docs/AMR_EXP_README_TXT.txt. Shannon Brown, JPL, 2010-10-06, JASON-1 ENHANCED JASON MICROWAVE RADIOMETER, https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/preview/L2/jmr_enh/docs/AMR_EXP_README_TXT.txt.",
-            "issued": "2010-11-30",
-            "temporal": "2002-01-15T06:07:00Z/2012-02-11T17:50:28Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-04-28",
-            "keyword": [
-                "oceans",
-                "atmosphere",
-                "atmospheric water vapor",
-                "earth science",
-                "sea surface topography"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jessica Hausman",
                 "hasEmail": "mailto:Jessica.K.Hausman@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "identifier": "C2491735244-POCLOUD",
-            "description": "The enhanced Jason-1 Microwave Radiometer (JMR) corrections contains better wet tropospheric path delay corrections along with better land, rain and ice flagging for coastal regions than that found in the Jason-1 Geophysical Data Records (GDR).  The enhanced corrections can be used in place of the GDR wet troposphere correction to provide more accurate Sea Surface Height Anomalies for coastal regions.",
-            "release-place": "JPL",
-            "series-name": "JASON-1 ENHANCED JASON MICROWAVE RADIOMETER",
-            "graphic-preview-description": "Thumbnail",
             "creator": "Shannon Brown",
-            "title": "JASON-1 ENHANCED JASON MICROWAVE RADIOMETER",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON-1_JMR_ENH.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The enhanced Jason-1 Microwave Radiometer (JMR) corrections contains better wet tropospheric path delay corrections along with better land, rain and ice flagging for coastal regions than that found in the Jason-1 Geophysical Data Records (GDR).  The enhanced corrections can be used in place of the GDR wet troposphere correction to provide more accurate Sea Surface Height Anomalies for coastal regions.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ1JMR-ENH0C",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FJ1JMR-ENH0C",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON-1_JMR_ENH.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON-1_JMR_ENH.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/preview/L2/jmr_enh/docs/AMR_EXP_README_TXT.txt",
-                    "description": "README file",
                     "@type": "dcat:Distribution",
+                    "description": "README file",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/jason1/preview/L2/jmr_enh/docs/AMR_EXP_README_TXT.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491735244-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491735244-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491735244-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491735244-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON-1_JMR_ENH.jpg",
+            "identifier": "C2491735244-POCLOUD",
+            "issued": "2010-11-30",
+            "keyword": [
+                "oceans",
+                "atmosphere",
+                "atmospheric water vapor",
+                "earth science",
+                "sea surface topography"
+            ],
+            "landingPage": "https://doi.org/10.5067/J1JMR-ENH0C",
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
+            "release-place": "JPL",
+            "series-name": "JASON-1 ENHANCED JASON MICROWAVE RADIOMETER",
             "spatial": "-180.0 -66.15 180.0 66.15",
+            "temporal": "2002-01-15T06:07:00Z/2012-02-11T17:50:28Z",
             "theme": [
                 "JASON-1",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "JASON-1 ENHANCED JASON MICROWAVE RADIOMETER"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/473",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Weaver, P.L. 2001. NPP Tropical Forest: Cinnamon Bay, U.S. Virgin Islands, 1982-1993, R1. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/473",
-            "issued": "2023-08-20",
-            "temporal": "1917-07-01T00:00:00Z/2003-07-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-23",
-            "keyword": [
-                "ecological dynamics",
-                "biosphere",
-                "vegetation",
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
-            "identifier": "C2755523295-ORNL_CLOUD",
             "description": "This data set contains three ASCII files (.txt format). One data file contains above-ground biomass, litter, litterfall, herbivory, biomass change, and above-ground net primary productivity (ANPP) estimates for a late secondary moist subtropical forest based on measurements from 16 permanent study plots located along an elevational (60-290 m) and topological gradient within the 132-ha Cinnamon Bay watershed on St. John, U.S. Virgin Islands. The purpose of the study was to provide information on forest structure, species composition, and forest productivity along environmental gradients, including the effects of hurricanes and drought. The other two files provide climate records from nearby weather stations (1917-1981).Above-ground biomass was measured every 5 years (1983-2003). Litterfall accumulation was determined in 1992-1993. In 1983, total above-ground biomass on all plots combined averaged 13,870 g/m2; by 2003 during a post-hurricane recovery period, it had declined by nearly 7 percent. In 1983, biomass was greatest on the summit, intermediate on slopes and valleys, and least on ridges; by 2003, the quantities for all sites had converged except on the summit plot.In 1992, ANPP was estimated based on annual litterfall accumulation (897 g/m2/year) plus biomass change due to delayed mortality (142 g/m2/year) plus estimated herbivory (25 g/m2/year), giving a total ANPP of 1,064 g/m2/year. Periodic storms and drought appear to maintain the forest in a disturbed state.",
-            "graphic-preview-description": "Browse Image",
-            "title": "NPP Tropical Forest: Cinnamon Bay, U.S. Virgin Islands, 1982-1993, R1",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F473",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F473",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_CBAY/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/npp/tropical_forest/NPP_CBAY/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_CBAY.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/NPP/guides/NPP_CBAY.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/473",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/473",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_CBAY/comp/NPP_CBAY.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/npp/tropical_forest/NPP_CBAY/comp/NPP_CBAY.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/npp_logo_square.png",
+            "identifier": "C2755523295-ORNL_CLOUD",
+            "issued": "2023-08-20",
+            "keyword": [
+                "ecological dynamics",
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/473",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-08-23",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "18.33 -64.8",
+            "temporal": "1917-07-01T00:00:00Z/2003-07-31T23:59:59Z",
             "theme": [
                 "NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NPP Tropical Forest: Cinnamon Bay, U.S. Virgin Islands, 1982-1993, R1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GLM/GRID/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Rudlosky, Scott .2022. GOES-R Geostationary Lightning Mapper (GLM) Gridded Data Products [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GLM/GRID/DATA101",
-            "issued": "2022-05-26",
-            "temporal": "2017-12-18T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-26",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric electricity"
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
-            "identifier": "C2278812167-GHRC_DAAC",
             "description": "The GOES-R Geostationary Lightning Mapper (GLM) Gridded Data Products consist of full disk extent gridded lightning flash data collected by the Geostationary Lightning Mapper (GLM) onboard the Geostationary Operational Environmental Satellite 16 and 17 (GOES-16 and GOES-17). These satellites are a part of the GOES-R series program: a four satellite series within the National Aeronautics and Space Administration (NASA) and National Oceanic and Atmospheric Association (NOAA) GOES program. GLM is the first operational geostationary optical lightning detector that provides total lightning data (in-cloud, cloud-to-cloud, and cloud-to-ground flashes). While it detects each of these types of lightning, the GLM is unable to distinguish between each type. The GLM GOES L3 dataset files contain gridded lightning flash data over the Western Hemisphere in netCDF-4 format from December 31, 2017 to present as this is an ongoing dataset.",
-            "title": "GOES-R Geostationary Lightning Mapper (GLM) Gridded Data Products V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGLM%2FGRID%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGLM%2FGRID%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=glmgoesL3%2Fdata%2F",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=glmgoesL3%2Fdata%2F",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.goes-r.gov/education/docs/Factsheet_GLM.pdf",
-                    "description": "Geostationary Lightning Mapper (GLM) GOES-R Series",
                     "@type": "dcat:Distribution",
+                    "description": "Geostationary Lightning Mapper (GLM) GOES-R Series",
+                    "downloadURL": "https://www.goes-r.gov/education/docs/Factsheet_GLM.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.goes-r.gov/mission/mission.html",
-                    "description": "GOES-R: Mission Overview",
                     "@type": "dcat:Distribution",
+                    "description": "GOES-R: Mission Overview",
+                    "downloadURL": "https://www.goes-r.gov/mission/mission.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.goes-r.gov/products/docs/PUG-L2+-vol5.pdf",
-                    "description": "GOES-R Series Product Definition and Users\u2019 Guide (PUG)",
                     "@type": "dcat:Distribution",
+                    "description": "GOES-R Series Product Definition and Users\u2019 Guide (PUG)",
+                    "downloadURL": "https://www.goes-r.gov/products/docs/PUG-L2+-vol5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.goes-r.gov/spacesegment/glm.html",
-                    "description": "Instruments: Geostationary Lightning Mapper (GLM)",
                     "@type": "dcat:Distribution",
+                    "description": "Instruments: Geostationary Lightning Mapper (GLM)",
+                    "downloadURL": "https://www.goes-r.gov/spacesegment/glm.html",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/goesr/documents/ATBDs/Baseline/ATBD_GOES-R_GLM_v3.0_Jul2012.pdf",
-                    "description": "GLM Lightning Cluster-Filter Algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "GLM Lightning Cluster-Filter Algorithm",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/goesr/documents/ATBDs/Baseline/ATBD_GOES-R_GLM_v3.0_Jul2012.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/glm/grid/doc/glmgoesL3_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/glm/grid/doc/glmgoesL3_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2019JD030874",
-                    "description": "Meteorological Imagery for the Geostationary Lightning Mapper",
                     "@type": "dcat:Distribution",
+                    "description": "Meteorological Imagery for the Geostationary Lightning Mapper",
+                    "downloadURL": "https://doi.org/10.1029/2019JD030874",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1016/j.atmosres.2013.01.006",
-                    "description": "The GOES-R Geostationary Lightning Mapper (GLM)",
                     "@type": "dcat:Distribution",
+                    "description": "The GOES-R Geostationary Lightning Mapper (GLM)",
+                    "downloadURL": "https://doi.org/10.1016/j.atmosres.2013.01.006",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
+            "identifier": "C2278812167-GHRC_DAAC",
+            "issued": "2022-05-26",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric electricity"
+            ],
+            "landingPage": "https://doi.org/10.5067/GLM/GRID/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-05-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "162.9 -57.0 -76.2 57.0",
+            "temporal": "2017-12-18T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "NOT APPLICABLE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GOES-R Geostationary Lightning Mapper (GLM) Gridded Data Products V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-ENG-6-RMC-OPS-V1.0",
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
+            "description": "This archive contains position and orientation information for various coordinate systems indexed by the Rover Motion Counter (RMC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-eng-6-rmc-ops-v1.0_vs5u-aag2",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars exploration rover",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-ENG-6-RMC-OPS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-eng-6-rmc-ops-v1.0_vs5u-aag2",
-            "description": "This archive contains position and orientation information for various coordinate systems indexed by the Rover Motion Counter (RMC).",
-            "title": "MER 1 MARS ENGINEERING ROVER MOTION COUNTER OPS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MER 1 MARS ENGINEERING ROVER MOTION COUNTER OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phil Newman",
+                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
+            },
+            "description": "Fermi is a powerful space observatory that will open a wide window on the universe. Gamma rays are the highest-energy form of light, and the gamma-ray sky is spectacularly different from the one we perceive with our own eyes. With a huge leap in all key capabilities, Fermi data will enable scientists to answer persistent questions across a broad range of topics, including supermassive black-hole systems, pulsars, the origin of cosmic rays, and searches for signals of new physics.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/p6v3/",
+                    "mediaType": "image/fits"
+                }
+            ],
+            "identifier": "NASA-0000214",
             "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "particle physics",
                 "astrophysics",
@@ -1533755,159 +1533767,149 @@
                 "gbm",
                 "space science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Phil Newman",
-                "hasEmail": "mailto:panewman@lheapop.gsfc.nasa.gov"
-            },
+            "landingPage": "http://fermi.gsfc.nasa.gov/ssc/data/access/lat/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:014"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000214",
-            "description": "Fermi is a powerful space observatory that will open a wide window on the universe. Gamma rays are the highest-energy form of light, and the gamma-ray sky is spectacularly different from the one we perceive with our own eyes. With a huge leap in all key capabilities, Fermi data will enable scientists to answer persistent questions across a broad range of topics, including supermassive black-hole systems, pulsars, the origin of cosmic rays, and searches for signals of new physics.",
-            "title": "LAT Pass 6 (V3) Archived Weekly files",
-            "programCode": [
-                "026:014"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://heasarc.gsfc.nasa.gov/FTP/fermi/data/lat/weekly/p6v3/",
-                    "mediaType": "image/fits"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "LAT Pass 6 (V3) Archived Weekly files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/111/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "ames",
-                "nasa",
-                "dashlink"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kamalika Das",
                 "hasEmail": "mailto:kamalika.das@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_111",
             "description": "CIDU 2010 Student Travel Award Application Form",
-            "title": "CIDU 2010 Student Travel Award",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/cidu10_travel_application.doc",
-                    "description": "Travel Award Application",
                     "@type": "dcat:Distribution",
+                    "description": "Travel Award Application",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/cidu10_travel_application.doc",
+                    "mediaType": "application/msword",
                     "title": "cidu10_travel_application.doc"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_111",
+            "issued": "2010-09-10",
+            "keyword": [
+                "ames",
+                "nasa",
+                "dashlink"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/111/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "CIDU 2010 Student Travel Award"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC2-MTP016-V2.0",
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
+            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 2\nMTP016 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-ESC2-MTP016-V1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc2-mtp016-v2.0_vs9y-dcpc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC2-MTP016-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc2-mtp016-v2.0_vs9y-dcpc",
-            "description": "This data set contains\nEDITED data from Rosetta RPC-LAP, acquired during the COMET ESCORT 2\nMTP016 mission phase. Comet C-G/67P was the primary target.\nThis data set supersedes RO-C-RPCLAP-2-ESC2-MTP016-V1.0.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC2 MTP016 V2.0",
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
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2\nESC2 MTP016 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0337-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-05T08:41:35.000 to 2014-10-05T11:41:24.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0337-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0337-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0337-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-05T08:41:35.000 to 2014-10-05T11:41:24.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0337 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0337 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V%2FE-SSI-2-REDR-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-e-ssi-2-redr-v1.0_vsbt-mxdd",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "black sky",
                 "moon",
@@ -1533916,740 +1533918,752 @@
                 "earth",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-V%2FE-SSI-2-REDR-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-v-e-ssi-2-redr-v1.0_vsbt-mxdd",
-            "description": "not applicable",
-            "title": "GALILEO VENUS AND EARTH SOLID STATE IMAGING 2 RAW EDR V1",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO VENUS AND EARTH SOLID STATE IMAGING 2 RAW EDR V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-ER-4-SUMM-OMNIDIRELEFLUX-V1.0",
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
+            "description": "Time ordered low resolution data\nfrom the Lunar Prospector Electron Reflectometer, averaged over 16\nspacecraft spins, in units of particles/cm**2/sec/steradian/eV,\nfor dates 1998-01-16 to 1999-07-29.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-er-4-summ-omnidireleflux-v1.0_vses-q3k8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "moon",
+                "lunar prospector"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LP-L-ER-4-SUMM-OMNIDIRELEFLUX-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lp-l-er-4-summ-omnidireleflux-v1.0_vses-q3k8",
-            "description": "Time ordered low resolution data\nfrom the Lunar Prospector Electron Reflectometer, averaged over 16\nspacecraft spins, in units of particles/cm**2/sec/steradian/eV,\nfor dates 1998-01-16 to 1999-07-29.",
-            "title": "LP ELECTRON REFLECTOMETER OMNI DIR.\n        ELECTRON FLUX 80SEC V1.0",
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
+            "title": "LP ELECTRON REFLECTOMETER OMNI DIR.\n        ELECTRON FLUX 80SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NVAP-M/NVAP_WEATHER_TOTAL-PRECIPITABLE-WATER_L3.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2013-07-02. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/NVAP-M/NVAP_WEATHER_TOTAL-PRECIPITABLE-WATER_L3.001.",
-            "issued": "2013-10-30",
-            "temporal": "1988-01-01T00:00:00Z/2009-12-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-04-26",
-            "keyword": [
-                "atmospheric water vapor",
-                "earth science",
-                "atmosphere"
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
-            "identifier": "C1600355222-LARC_ASDC",
             "description": "NVAP_WEATHER_Total-Precipitable-Water data set is designed to provide higher spatial and temporal resolution products for use in studies on shorter time scales as well as weather case studies. The new NVAP data sets are produced under the NASA Making Earth Science Data Records for Use in Research Environments (MEaSUREs) program and is named NVAP-M. It supersedes the previous NVAP data set. NVAP-M continues the legacy of providing high-quality, model-independent global estimates of total column and layered water vapor. The use of improved, intercalibrated data sets and algorithms that were not available for the heritage NVAP data set results in an improved and extended water vapor data set that is stable enough for climate research and of a resolution appropriate for studies on smaller spatial and temporal scales. The true value of NVAP-M will be seen in outcomes from applied and research users of the data set in various fields. Some initial NVAP-M findings are presented in Vonder Haar et al. (2012). In addition to the time-dependent artifacts present in the previous NVAP data set, a wealth of new data has become available since the last NVAP processing in 2003. These include an additional SSM/I instrument, additional NOAA satellites, the NASA Earth Observing System (EOS)-Aqua Satellite, which carries the Atmospheric Infrared Sounder (AIRS), as well as water vapor information from Global Positioning System (GPS) satellites. This extension and reprocessing effort increases the temporal coverage from 14 to 22 (1988-2009) years, making the data set more useful and consistent for investigation of the long-term trends which are hypothesized to occur as Earth warms. In addition to the long-standing daily, 1-degree gridded Total Precipitable Water (TPW) and layered Precipitable Water (PW) products, NVAP-M includes additional products geared towards different scientific needs. Three separate processing streams produced products directed towards specific research goals. These are NVAP-M Climate, designed to provide the most stable water vapor data set over time for use in climate applications, and NVAP-M Weather, designed to provide higher spatial and temporal resolution products for use in studies on shorter time scales as well as weather case studies. Additionally, an ocean-only (NVAP-M Ocean) version includes only data from the SSM/I and is intended to mirror other available SSM/I-only water vapor data sets.",
-            "title": "NASA Water Vapor Project MEaSUREs (NVAP-M) NVAP WEATHER Total Precipitable Water",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNVAP-M%2FNVAP_WEATHER_TOTAL-PRECIPITABLE-WATER_L3.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNVAP-M%2FNVAP_WEATHER_TOTAL-PRECIPITABLE-WATER_L3.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/NVAP-M",
-                    "description": "ASDC Data and Information for NVAP-M",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for NVAP-M",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/NVAP-M",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NVAP-M/NVAP_WEATHER_TOTAL-PRECIPITABLE-WATER_L3.001",
-                    "description": "DOI data set landing page for NVAP_WEATHER_Total-Precipitable-Water_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for NVAP_WEATHER_Total-Precipitable-Water_1",
+                    "downloadURL": "https://doi.org/10.5067/NVAP-M/NVAP_WEATHER_TOTAL-PRECIPITABLE-WATER_L3.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1600355222-LARC_ASDC",
-                    "description": "Earthdata Search for NVAP_WEATHER_Total-Precipitable-Water_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for NVAP_WEATHER_Total-Precipitable-Water_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1600355222-LARC_ASDC",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/read_software/read_nvapm.pro.txt",
-                    "description": "Readme to open and read NVAP-M data files",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to open and read NVAP-M data files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/read_software/read_nvapm.pro.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/guide/NVAPM_User_Guide.pdf",
-                    "description": "NVAP-MEaSUREs (NVAP-M) ReadMe",
                     "@type": "dcat:Distribution",
+                    "description": "NVAP-MEaSUREs (NVAP-M) ReadMe",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/guide/NVAPM_User_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/NVAP_M_ATBD_Feb2013.pdf",
-                    "description": "NASA Water Vapor Project \u2013 MEaSUREs (NVAP-M) Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Water Vapor Project \u2013 MEaSUREs (NVAP-M) Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/nvap/NVAP_M_ATBD_Feb2013.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/NVAP-M/NVAP-M_Weather/NVAP_WEATHER_Total-Precipitable-Water/",
-                    "description": "ASDC Direct Data Download for NVAP_WEATHER_Total-Precipitable-Water_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for NVAP_WEATHER_Total-Precipitable-Water_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/NVAP-M/NVAP-M_Weather/NVAP_WEATHER_Total-Precipitable-Water/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/NVAP-M/NVAP-M_Weather/NVAP_WEATHER_Total-Precipitable-Water/contents.html",
-                    "description": "OPeNDAP data access for NVAP_WEATHER_Total-Precipitable-Water_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for NVAP_WEATHER_Total-Precipitable-Water_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/NVAP-M/NVAP-M_Weather/NVAP_WEATHER_Total-Precipitable-Water/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1600355222-LARC_ASDC",
+            "issued": "2013-10-30",
+            "keyword": [
+                "atmospheric water vapor",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/NVAP-M/NVAP_WEATHER_TOTAL-PRECIPITABLE-WATER_L3.001",
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
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-90.0 -179.9 -90.0 180.0 90.0 180.0 90.0 -179.9 -90.0 -179.9</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1988-01-01T00:00:00Z/2009-12-01T23:59:59.999Z",
             "theme": [
                 "NVAP-M",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NASA Water Vapor Project MEaSUREs (NVAP-M) NVAP WEATHER Total Precipitable Water"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1124-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-23T20:53:30.000 to 2015-10-23T23:45:11.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1124-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1124-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1124-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-23T20:53:30.000 to 2015-10-23T23:45:11.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1124 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1124 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC1-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V3.0 data set supersedes the previous V2.0 data set with improved documentation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc1-v3.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "calibration",
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C%2FCAL-ALICE-2-ESC1-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-cal-alice-2-esc1-v3.0",
-            "description": "This data set contains CODMAC Level 2 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the comet 67P/Churyumov-Gerasimenko Comet Escort 1 mission phase, which took place between 2014-11-20 and 2015-03-10.  The current V3.0 data set supersedes the previous V2.0 data set with improved documentation.",
-            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC1 V3.0",
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
+            "title": "ROSETTA-ORBITER 67P/CAL ALICE 2 ESC1 V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1701",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Douglas, T.A. 2019. ABoVE: Soil Active Layer Thaw Depths at CRREL sites near Fairbanks, Alaska, 2014-2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1701",
-            "issued": "2019-08-28",
-            "temporal": "2014-10-15T00:00:00Z/2018-10-15T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "biosphere",
-                "earth science",
-                "ecosystems",
-                "terrestrial hydrosphere",
-                "snow/ice",
-                "vegetation",
-                "frozen ground",
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
-            "identifier": "C2143403378-ORNL_CLOUD",
             "description": "This dataset provides soil active layer thaw depth measurements collected along transects at three sites near Fairbanks, Alaska, USA. Measurements were made during the late summers of 2014-2018. The sites were located at Creamer's Field, the Permafrost Tunnel, and Farmer's Loop (two transects). Vegetation ecotypes along the transects are also reported. The US Army Corps of Engineers, Cold Regions Research and Engineering Laboratory (CRREL) owns and operates facilities at the Permafrost Tunnel and Farmer's Loop. The sites are suitable for manipulation experiments, installing permanent equipment, and establishing long-term measurements.",
-            "graphic-preview-description": "Thaw depths recorded along Farmer\u00c3\u00a2\u00c2\u0080\u00c2\u0099s Loop Transect 2. Photo provided by Tom Douglas.",
-            "title": "ABoVE: Soil Active Layer Thaw Depths at CRREL sites near Fairbanks, Alaska, 2014-2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Active_Layer_Thaw_Depths_Fig1.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1701",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1701",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/above/Active_Layer_Thaw_Depths/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/above/Active_Layer_Thaw_Depths/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Active_Layer_Thaw_Depths.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Active_Layer_Thaw_Depths.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1701",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1701",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Active_Layer_Thaw_Depths/comp/Active_Layer_Thaw_Depths.pdf",
-                    "description": "ABoVE: Soil Active Layer Thaw Depths at CRREL sites near Fairbanks, Alaska, 2014-2018: Active_Layer_Thaw_Depths.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Soil Active Layer Thaw Depths at CRREL sites near Fairbanks, Alaska, 2014-2018: Active_Layer_Thaw_Depths.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Active_Layer_Thaw_Depths/comp/Active_Layer_Thaw_Depths.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/vnd.google-earth.kmz",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Active_Layer_Thaw_Depths/comp/active_layer_thaw_depths_all_sites.kmz",
-                    "description": "ABoVE: Thaw Depth at Four Transects near Fairbanks, Alaska, 2014-2018: active_layer_thaw_depths_all_sites.kmz",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Thaw Depth at Four Transects near Fairbanks, Alaska, 2014-2018: active_layer_thaw_depths_all_sites.kmz",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Active_Layer_Thaw_Depths/comp/active_layer_thaw_depths_all_sites.kmz",
+                    "mediaType": "application/vnd.google-earth.kmz",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Active_Layer_Thaw_Depths/comp/active_layer_thaw_depths_all_sites.zip",
-                    "description": "ABoVE: Thaw Depth at Four Transects near Fairbanks, Alaska, 2014-2018: active_layer_thaw_depths_all_sites.zip",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Thaw Depth at Four Transects near Fairbanks, Alaska, 2014-2018: active_layer_thaw_depths_all_sites.zip",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Active_Layer_Thaw_Depths/comp/active_layer_thaw_depths_all_sites.zip",
+                    "mediaType": "application/zip",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Active_Layer_Thaw_Depths_Fig1.jpg",
-                    "description": "Thaw depths recorded along Farmer\u00c3\u00a2\u00c2\u0080\u00c2\u0099s Loop Transect 2. Photo provided by Tom Douglas.",
                     "@type": "dcat:Distribution",
+                    "description": "Thaw depths recorded along Farmer\u00c3\u00a2\u00c2\u0080\u00c2\u0099s Loop Transect 2. Photo provided by Tom Douglas.",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Active_Layer_Thaw_Depths_Fig1.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://above.nasa.gov",
-                    "description": "ABoVE project site",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE project site",
+                    "downloadURL": "https://above.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-description": "Thaw depths recorded along Farmer\u00c3\u00a2\u00c2\u0080\u00c2\u0099s Loop Transect 2. Photo provided by Tom Douglas.",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Active_Layer_Thaw_Depths_Fig1.jpg",
+            "identifier": "C2143403378-ORNL_CLOUD",
+            "issued": "2019-08-28",
+            "keyword": [
+                "biosphere",
+                "earth science",
+                "ecosystems",
+                "terrestrial hydrosphere",
+                "snow/ice",
+                "vegetation",
+                "frozen ground",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1701",
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
             "spatial": "-147.74 64.87 -147.61 64.95",
+            "temporal": "2014-10-15T00:00:00Z/2018-10-15T23:59:59Z",
             "theme": [
                 "ABoVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ABoVE: Soil Active Layer Thaw Depths at CRREL sites near Fairbanks, Alaska, 2014-2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/88HRIQUYP6VO",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Geolocation Information: Oklahoma, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/88HRIQUYP6VO.",
-            "issued": "2003-07-01",
-            "temporal": "2003-07-01T00:00:00Z/2003-07-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-01",
-            "keyword": [
-                "land surface",
-                "earth science",
-                "soils"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Cosh",
                 "hasEmail": "mailto:mcosh@hydrolab.arsusda.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386250442-NSIDCV0",
             "description": "Notice to Data Users: The documentation for this data set was provided solely by the Principal Investigator(s) and was not further developed, thoroughly reviewed, or edited by NSIDC. Thus, support for this data set may be limited.\n\nThis ancillary data set consists of geographic coordinates for the Soil Moisture Experiment 2003 (SMEX03).",
-            "title": "SMEX03 Geolocation Information: Oklahoma, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F88HRIQUYP6VO",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F88HRIQUYP6VO",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/geolocation/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/geolocation/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/geolocation/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/geolocation/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/88HRIQUYP6VO",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/88HRIQUYP6VO",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/88HRIQUYP6VO",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/88HRIQUYP6VO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386250442-NSIDCV0",
+            "issued": "2003-07-01",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/88HRIQUYP6VO",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-07-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.33 34.44 -97.71 35.41",
+            "temporal": "2003-07-01T00:00:00Z/2003-07-01T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Geolocation Information: Oklahoma, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7265/N56H4FB3",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Meteorological Data from the Russian Arctic, 1961-2000, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, National Snow and Ice Data Center. https://doi.org/10.7265/N56H4FB3.",
-            "issued": "1961-01-01",
-            "temporal": "1961-01-01T00:00:00Z/2000-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2000-12-31",
-            "keyword": [
-                "atmospheric pressure",
-                "atmosphere",
-                "precipitation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "clouds",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florence Fetterer",
                 "hasEmail": "mailto:nsidc@nsidc.org"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NSIDC"
-            },
-            "identifier": "C1386206504-NSIDCV0",
             "description": "This data set contains monthly means of meteorological observation data from Russian stations from 1961-2000 (for most stations). The Russian station observations were provided by Vladimir Radionov, Arctic and Antarctic Research Institute (AARI), St. Petersburg, and include 2-meter air temperature, sea level pressure, total and low cloud amount, precipitation, and relative humidity.",
-            "title": "Meteorological Data from the Russian Arctic, 1961-2000, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN56H4FB3",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7265%2FN56H4FB3",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/forms/G02141_or.html?major_version=1",
-                    "description": "Direct download, with optional registration page.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download, with optional registration page.",
+                    "downloadURL": "https://nsidc.org/forms/G02141_or.html?major_version=1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N56H4FB3",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.7265/N56H4FB3",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.7265/N56H4FB3",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.7265/N56H4FB3",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386206504-NSIDCV0",
+            "issued": "1961-01-01",
+            "keyword": [
+                "atmospheric pressure",
+                "atmosphere",
+                "precipitation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "clouds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.7265/N56H4FB3",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2000-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NSIDC"
+            },
             "spatial": "14.25 59.96667 179.1 78.06667",
+            "temporal": "1961-01-01T00:00:00Z/2000-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Meteorological Data from the Russian Arctic, 1961-2000, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1288-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-26T07:31:35.000 to 2015-12-26T15:20:48.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1288-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1288-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1288-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-26T07:31:35.000 to 2015-12-26T15:20:48.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1288 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1288 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CH1-ORB-L-M3-4-L1B-RADIANCE-V2.0",
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
-                "chandrayaan-1",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains pixel located, radiometrically-calibrated data collected by M3 instrument on Chandrayaan-1.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ch1-orb-l-m3-4-l1b-radiance-v2.0_vstq-i92q",
+            "issued": "2018-06-26",
+            "keyword": [
+                "chandrayaan-1",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CH1-ORB-L-M3-4-L1B-RADIANCE-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ch1-orb-l-m3-4-l1b-radiance-v2.0_vstq-i92q",
-            "description": "This dataset contains pixel located, radiometrically-calibrated data collected by M3 instrument on Chandrayaan-1.",
-            "title": "CH1-ORB MOON M3 4 L1B RADIANCE NEAR-IR SPECTRAL IMAGES V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "CH1-ORB MOON M3 4 L1B RADIANCE NEAR-IR SPECTRAL IMAGES V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0242-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-25T22:42:05.000 to 2014-08-26T00:42:04.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0242-v1.0_vsub-vzt2",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0242-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0242-v1.0_vsub-vzt2",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-08-25T22:42:05.000 to 2014-08-26T00:42:04.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0242 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0242 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/296",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Kimball, J.S. 1999. BOREAS RSS-08 BIOME-BGC SSA Simulations of Annual Water and Carbon Fluxes. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/296",
-            "issued": "2023-11-22",
-            "temporal": "1994-01-01T00:00:00Z/1996-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-07",
-            "keyword": [
-                "vegetation",
-                "ecological dynamics",
-                "earth science",
-                "atmospheric water vapor",
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
-            "identifier": "C2813394229-ORNL_CLOUD",
             "description": "Derived maps of landcover type and crown and stem biomass as model inputs to determine annual evapotranspiration, gross primary production, autotrophic respiration and net primary productivity within the BOREAS SSA-MSA, at a 30 m spatial resolution.  Mode",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS RSS-08 BIOME-BGC SSA Simulations of Annual Water and Carbon Fluxes",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F296",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F296",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/biomebg2/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/RSS/biomebg2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS08_BIOME_BGC_Imgs.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/guides/RSS08_BIOME_BGC_Imgs.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/296",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/296",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/biomebg2/comp/README",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/biomebg2/comp/README",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/biomebg2/comp/RSS08_BIOME_BGC_Imgs.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/biomebg2/comp/RSS08_BIOME_BGC_Imgs.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/biomebg2/comp/RSS08_BIOME_BGC_Imgs.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/biomebg2/comp/RSS08_BIOME_BGC_Imgs.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/biomebg2/comp/RSS08_BIOME_BGC_Imgs.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/RSS/biomebg2/comp/RSS08_BIOME_BGC_Imgs.txt",
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
+            "identifier": "C2813394229-ORNL_CLOUD",
+            "issued": "2023-11-22",
+            "keyword": [
+                "vegetation",
+                "ecological dynamics",
+                "earth science",
+                "atmospheric water vapor",
+                "atmosphere",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/296",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-07",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-111.0 49.0 -89.0 60.0",
+            "temporal": "1994-01-01T00:00:00Z/1996-12-31T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS RSS-08 BIOME-BGC SSA Simulations of Annual Water and Carbon Fluxes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2016.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "FY16 NASA Budget Overview FY14-FY16 PDF",
+                    "downloadURL": "http://www.nasa.gov/sites/default/files/files/NASA_FY14_APR-FY16_APP_Complete.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NASA Budget Overview FY14-FY16"
+                }
+            ],
+            "identifier": "OCIO-Fitara-58",
             "issued": "2014-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "plan",
                 "finance",
@@ -1534658,75 +1534672,32 @@
                 "financial",
                 "strategic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/news/budget/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NASA HQ"
             },
-            "identifier": "OCIO-Fitara-58",
-            "description": "NASA Financial Budget Documents, Strategic Plans and Performance Reports for fiscal year 2016.",
-            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2016: NASA Budget Overview FY14-FY16",
-            "programCode": [
-                "026:046"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/sites/default/files/files/NASA_FY14_APR-FY16_APP_Complete.pdf",
-                    "description": "FY16 NASA Budget Overview FY14-FY16 PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "NASA Budget Overview FY14-FY16"
-                }
-            ],
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA Financial Budget Documents, Strategic Plans and Performance Reports 2016: NASA Budget Overview FY14-FY16"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10482",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-12-01",
-            "temporal": "2011-12-01T00:00:00Z/2014-12-01T00:00:00Z",
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
-                "active",
-                "project",
-                "nasa headquarters"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "George Komar",
                 "hasEmail": "mailto:george.komar@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10482",
             "description": "&lt;p&gt;\r\n\tDevelop a compact, efficient 2&amp;micro;m pulsed laser for a lidar instrument to make accurate, high-resolution atmospheric CO2 column measurements in support of the ASCENDS mission.&lt;br /&gt;\r\n\tDevelop a pulsed 2&amp;micro;m laser that is based on a Thulium fiber-laser pumped Holmium (Ho) solid state laser in a Master Oscillator Power Amplifier (MOPA) configuration.&lt;br /&gt;\r\n\tDemonstrate 65mJ at 50Hz needed for the space&amp;nbsp; Integrated Path Differential Absorption (IPDA) instrument in a robust prototype format.&lt;/p&gt;",
-            "title": "A 2-Micron Pulsed Laser Transmitter for Direct Detection Column CO2 Measurement from Space Project",
-            "programCode": [
-                "026:005"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1534734,685 +1534705,716 @@
                     "mediaType": "application/xml"
                 }
             ],
+            "identifier": "TECHPORT_10482",
+            "issued": "2011-12-01",
+            "keyword": [
+                "active",
+                "project",
+                "nasa headquarters"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10482",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:005"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Science Mission Directorate"
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
+            "temporal": "2011-12-01T00:00:00Z/2014-12-01T00:00:00Z",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "A 2-Micron Pulsed Laser Transmitter for Direct Detection Column CO2 Measurement from Space Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2PANLN.007",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2004-07-15. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/AURA/TES/TL2PANLN.007. https://asdc.larc.nasa.gov/project/TES.",
-            "issued": "2015-10-15",
-            "temporal": "2004-08-01T00:00:00Z/2015-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "earth science",
-                "air quality",
-                "atmospheric chemistry",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "SCOTT GLUCK",
                 "hasEmail": "mailto:scott.gluck@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1603490305-LARC",
             "description": "TL2PANLN_7 is the Tropospheric Emission Spectrometer (TES)/Aura Level 2 Atmospheric Temperatures Limb Version 7 data product. It contains atmospheric vertical profile estimates and associated errors including the mapping matrix to relate the reduced-size retrieval vectors, covariances, and averaging kernels back to the TES forward model pressure grid. TES Level 2 data contain retrieved species (or temperature) profiles at the observation targets and the estimated errors. The geolocation, quality and other data (e.g., surface characteristics for nadir observations) are also provided. L2 modeled spectra are evaluated using radiative transfer modeling algorithms. The process, referred to as retrieval, compares observed spectra to the modeled spectra and iteratively updates the atmospheric parameters. L2 standard product files include information for one molecular species (or temperature) for an entire global survey or special observation run. A global survey consists of a maximum of 16 consecutive orbits. \r\rA nadir sequence within the TES Global Survey is a fixed number of observations within an orbit for a Global Survey. Prior to April 24, 2005, it consisted of two low resolution scans over the same ground locations. After April 24, 2005, Global Survey data consisted of three low resolution scans. The Nadir standard product consists of four files, where each file is composed of the Global Survey Nadir observations from one of four focal planes for a single orbit, i.e. 72 orbit sequences. The Global Survey Nadir observations currently only use a single set of filter mix. A Global Survey consists of observations along 16 consecutive orbits at the start of a two day cycle, over which 3,200 retrievals are performed. Each observation is the input for retrievals of species Volume Mixing Ratios (VMR), temperature profiles, surface temperature and other data parameters with associated pressure levels, precision, total error, vertical resolution, total column density and other diagnostic quantities. Each TES Level 2 standard product reports information in a swath format conforming to the HDF-EOS Aura File Format Guidelines. Each Swath object is bounded by the number of observations in a global survey and a predefined set of pressure levels representing slices through the atmosphere. Each standard product can have a variable number of observations depending upon the Global Survey configuration and whether averaging is employed. Also, missing or bad retrievals are not reported. \r\rThe organization of data within the Swath object is based on a superset of the UARS pressure levels used to report concentrations of trace atmospheric gases. The reporting grid is the same pressure grid used for modeling. There are 67 reporting levels from 1211.53 hPa, which allows for very high surface pressure conditions, to 0.1 hPa, about 65 km. In addition, the products will report values directly at the surface when possible or at the observed cloud top level. Thus, in the Standard Product files each observation can potentially contain estimates for the concentration of a particular molecule at 67 different pressure levels within the atmosphere. However, for most retrieved profiles, the highest pressure levels are not observed due to a surface at lower pressure or cloud obscuration. For pressure levels corresponding to altitudes below the cloud top or surface, where measurements were not possible, a fill value will be applied. \r\rTo minimize the duplication of information between the individual species standard products, data fields common to each species (such as spacecraft coordinates, emissivity, and other data fields) have been collected into a separate standard product, termed the TES L2 Ancillary Data product (ESDT short name: TL2ANC). Users of this product should also obtain the Ancillary Data product.",
-            "title": "TES/Aura L2 Peroxyacyl Nitrate Lite Nadir V007",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2PANLN.007",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAURA%2FTES%2FTL2PANLN.007",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://portal.hdfgroup.org/display/HDFVIEW/HDFView",
-                    "description": "HDFView Overview and Download",
                     "@type": "dcat:Distribution",
+                    "description": "HDFView Overview and Download",
+                    "downloadURL": "https://portal.hdfgroup.org/display/HDFVIEW/HDFView",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
-                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
                     "@type": "dcat:Distribution",
+                    "description": "Report of TES Level 2 Global Survey Products Available from the ASDC",
+                    "downloadURL": "https://l0dup05.larc.nasa.gov/cgi-bin/DUE/tes_L2GlbSrvy.cgi",
+                    "mediaType": "text/html",
                     "title": "View this dataset's production history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/53",
-                    "description": "NASA EOS ATB Documents: TES",
                     "@type": "dcat:Distribution",
+                    "description": "NASA EOS ATB Documents: TES",
+                    "downloadURL": "https://eospso.gsfc.nasa.gov/atbd-category/53",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tes.jpl.nasa.gov/",
-                    "description": "TES project home page",
                     "@type": "dcat:Distribution",
+                    "description": "TES project home page",
+                    "downloadURL": "https://tes.jpl.nasa.gov/",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Lite_Products_Users_Guide.pdf",
-                    "description": "AVDC TES Lite products user\u2019s guide",
                     "@type": "dcat:Distribution",
+                    "description": "AVDC TES Lite products user\u2019s guide",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TES_Lite_Products_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_2_std.pdf",
-                    "description": "TES Level 2 Versioning - Level 2 Standard and Special Observation Products",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 2 Versioning - Level 2 Standard and Special Observation Products",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/level_2_std.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's processing history"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
-                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
                     "@type": "dcat:Distribution",
+                    "description": "Basic IDL Tools for extraction information from TES L2 HDF Product files",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/readme/README_L2_ReadSoftware.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2PANLN.007",
-                    "description": "DOI data set landing page for TL2PANLN_7",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for TL2PANLN_7",
+                    "downloadURL": "https://doi.org/10.5067/AURA/TES/TL2PANLN.007",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tes.jpl.nasa.gov/science/publications/",
-                    "description": "TES Publications",
                     "@type": "dcat:Distribution",
+                    "description": "TES Publications",
+                    "downloadURL": "https://tes.jpl.nasa.gov/science/publications/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2PANLN.007/contents.html",
-                    "description": "OPeNDAP data access for TL2PANLN_7",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TL2PANLN_7",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TES/TL2PANLN.007/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1603490305-LARC",
-                    "description": "Earthdata Search for TL2PANLN_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TL2PANLN_7 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1603490305-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2PANLN.007/",
-                    "description": "ASDC Direct Data Download for TL2PANLN_7",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TL2PANLN_7",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TES/TL2PANLN.007/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_products_V007.pdf",
-                    "description": "Aura-TES L2 Products: Version 7 Data Quality Description",
                     "@type": "dcat:Distribution",
+                    "description": "Aura-TES L2 Products: Version 7 Data Quality Description",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_products_V007.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TESDataUsersGuideV8_0_March_27_2020_FV-8_rh.pdf",
-                    "description": "TES Level 2 (L2) Data User's Guide (Up to & including Version 8 data)",
                     "@type": "dcat:Distribution",
+                    "description": "TES Level 2 (L2) Data User's Guide (Up to & including Version 8 data)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/guide/TESDataUsersGuideV8_0_March_27_2020_FV-8_rh.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_products_v002.pdf",
-                    "description": "Aura-TES L2 Products: Version 2 Data Quality Description",
                     "@type": "dcat:Distribution",
+                    "description": "Aura-TES L2 Products: Version 2 Data Quality Description",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/tes/quality_summaries/L2_products_v002.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's data quality document"
                 }
             ],
+            "identifier": "C1603490305-LARC",
+            "issued": "2015-10-15",
+            "keyword": [
+                "earth science",
+                "air quality",
+                "atmospheric chemistry",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/AURA/TES/TL2PANLN.007",
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
+            "temporal": "2004-08-01T00:00:00Z/2015-12-31T23:59:59.999Z",
             "theme": [
                 "TES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TES/Aura L2 Peroxyacyl Nitrate Lite Nadir V007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0029",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0029.",
-            "issued": "2000-03-16",
-            "temporal": "1992-06-02T00:00:00Z/1992-06-23T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-06",
-            "keyword": [
-                "clouds",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES SPINHIRNE",
                 "hasEmail": "mailto:james.d.spinhirne@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000994-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems. The development of parameterizations requires an understanding of the processes that generate, maintain, and dissipate boundary layer clouds. This development is currently impeded by lack of understanding of the transition from stratocumulus clouds to trade cumulus clouds and the factors that control cloud type and amount in the boundary layer. ASTEX was designed to address key issues related to stratocumulus to trade cumulus transition and mode selection. ASTEX involved intensive measurements from several platforms operating from June 1-28, 1992 in the area of the Azores and Madeira Islands. The purpose was to study how the transition and mode selection are effected by 1) cloud-top entrainment instability, 2) diurnal decoupling and clearing due to solar absorption, 3) patchy drizzle and a transition to horizontally inhomogeneous clouds through decoupling, 4) mesoscale variability in cloud thickness and associated mesoscale circulations, and 5) episodic strong subsidence lowering the inversion below the LCL. Detailed descriptions of the scientific goals of ASTEX are in the FIRE Phase II: Research plan (1989) and in the ASTEX Operations Plan (1992). The Cloud Lidar System (CLS) instrument was flown aboard the NASA ER-2 airplane. This instrument was used to determine cloud altitudes. Information pertaining to the number of cloud layers detected; the heights of the boundaries for up to 5 cloud layers; geo-physical location information; and time were recorded.Four channels of data were recorded. The first channel recorded wave lengths at 532 nanometers in the parallel plane. The second channel recorded wave lengths of 532 nanometers in the perpendicular plane. The third channel recorded wavelengths of 1064 nanometers total. The forth channel was a linear amplifier which received the digitized signal from one of the three previously mentioned CLS detectors. The data are organized so that there is a single header record for the file. This header record is followed by a series of pairs of records. The first record of each pair contains the CLS calibrated data and the second record of the pair contains the CLS analyzed data.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) NASA ER-2 Cloud Lidar System Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0029",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0029",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000994-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_ER2_LIDAR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_ER2_LIDAR_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000994-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_read_er2_lidar.c",
-                    "description": "Readme to read the FIRE ASTEX ER2 LIDAR Data Granules - Direct File Download (.c)",
                     "@type": "dcat:Distribution",
+                    "description": "Readme to read the FIRE ASTEX ER2 LIDAR Data Granules - Direct File Download (.c)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fax_read_er2_lidar.c",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_er2_lidar_dataset.pdf",
-                    "description": "FIRE Cloud Lidar System Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cloud Lidar System Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_er2_lidar_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_er2_lidar_part1",
-                    "description": "Description of Tapes Created for the ASTEX Project Readme",
                     "@type": "dcat:Distribution",
+                    "description": "Description of Tapes Created for the ASTEX Project Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_er2_lidar_part1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0029",
-                    "description": "DOI data set landing page for FIRE_AX_ER2_LIDAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_ER2_LIDAR_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0029",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_ER2_LIDAR/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_ER2_LIDAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_ER2_LIDAR_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_ER2_LIDAR/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_ER2_LIDAR/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_ER2_LIDAR_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_ER2_LIDAR_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_ER2_LIDAR/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000994-LARC_ASDC",
+            "issued": "2000-03-16",
+            "keyword": [
+                "clouds",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0029",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>30.55 -27.54 30.55 -15.41 39.91 -15.41 39.91 -27.54 30.55 -27.54</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-06-02T00:00:00Z/1992-06-23T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) NASA ER-2 Cloud Lidar System Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1195-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-19T19:15:15.000 to 2015-11-20T00:52:26.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1195-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1195-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1195-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-19T19:15:15.000 to 2015-11-20T00:52:26.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1195 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1195 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L2-V5.2",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2017-03-17. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L2-V5.2. https://asdc.larc.nasa.gov/project/SAGE%20III-ISS.",
-            "issued": "2018-08-22",
-            "temporal": "2017-06-07T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-06-19",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "earth science",
-                "aerosols",
-                "atmospheric water vapor"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DR. Flittner",
                 "hasEmail": "mailto:david.e.flittner@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2066317190-LARC",
             "description": "g3bssp_52 is the Stratospheric Aerosol and Gas Experiment III (SAGE III) on the International Space Station (ISS) (SAGE III/ISS) Level 2 Solar Event Species Profiles (HDF5) V052 data product. It contains all the species products for a single solar event. SAGE III was Launched on February 19, 2017 on a SpaceX Falcon 9 from Kennedy Space Center, SAGE III-ISS is the second instrument from the SAGE III project, externally mounted on the ISS. This ISS-based instrument uses a technique known as occultation, which involves looking at the light from the Sun or Moon as it passes through Earth's atmosphere at the edge, or limb, of the planet to provide long-term monitoring of ozone vertical profiles of the stratosphere and mesosphere. The data provided by SAGE III-ISS includes key components of atmospheric composition and their long-term variability, focusing on the study of aerosols, chlorine dioxide, clouds, nitrogen dioxide, nitrogen trioxide, pressure and temperature, and water vapor. SAGE data has historically been used by the World Meteorological Organization to inform their periodic assessments of ozone depletion. These new observations from the International Space Station will continue the SAGE team's contributions to ongoing scientific understanding of the Earth's atmosphere.",
-            "title": "SAGE III/ISS L2 Solar Event Species Profiles (HDF5) V052",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FSOLAR_HDF5_L2-V5.2",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FISS%2FSAGEIII%2FSOLAR_HDF5_L2-V5.2",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sage.nasa.gov/",
-                    "description": "SAGE project home page",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE project home page",
+                    "downloadURL": "https://sage.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG-G3B.docx",
-                    "description": "SAGE III/ISS Data Products User\u2019s Guide, April 2021",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Data Products User\u2019s Guide, April 2021",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/DPUG-G3B.docx",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/sageiii_iss_readers.tar",
-                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.tar)",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Data Read Software Package - Direct File Download (.tar)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/sageiii_iss_readers.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/Release_Notes_v5.2.docx",
-                    "description": "SAGE III/ISS Version 5.2 Release Notes",
                     "@type": "dcat:Distribution",
+                    "description": "SAGE III/ISS Version 5.2 Release Notes",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/guide/Release_Notes_v5.2.docx",
+                    "mediaType": "text/html",
                     "title": "View an important notice for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
-                    "description": "NASA Open Source Agreement for Computer Software",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Open Source Agreement for Computer Software",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/sageiii-iss/read_software/19529_SAGE_III_NOSA_1.3_License.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L2-V5.2",
-                    "description": "DOI data set landing page for g3bssp_52",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for g3bssp_52",
+                    "downloadURL": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L2-V5.2",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2066317190-LARC",
-                    "description": "Earthdata Search for g3bssp_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for g3bssp_52 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2066317190-LARC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SAGE_III_ISS/g3bssp.052/",
-                    "description": "ASDC Direct Data Download for g3bssp_52",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for g3bssp_52",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SAGE_III_ISS/g3bssp.052/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/project/SAGE%20III-ISS",
-                    "description": "ASDC Data and Information for SAGE III-ISS",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Data and Information for SAGE III-ISS",
+                    "downloadURL": "https://asdc.larc.nasa.gov/project/SAGE%20III-ISS",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2066317190-LARC",
+            "issued": "2018-08-22",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "earth science",
+                "aerosols",
+                "atmospheric water vapor"
+            ],
+            "landingPage": "https://doi.org/10.5067/ISS/SAGEIII/SOLAR_HDF5_L2-V5.2",
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
+            "temporal": "2017-06-07T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "SAGE III-ISS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAGE III/ISS L2 Solar Event Species Profiles (HDF5) V052"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0346-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-09T15:45:45.000 to 2014-10-09T22:22:26.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0346-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0346-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0346-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-09T15:45:45.000 to 2014-10-09T22:22:26.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0346 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0346 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Airborne/CAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Airborne/CAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1.",
-            "issued": "2020-07-20",
-            "temporal": "2019-08-03T00:00:00Z/2019-10-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-18",
-            "keyword": [
-                "atmosphere",
-                "atmospheric chemistry",
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
-            "identifier": "C1954731260-LARC_ASDC",
             "description": "CAMP2Ex_TraceGas_AircraftInSitu_P3_Data are in-situ trace gas measurements conducted onboard the P-3 aircraft during the Clouds, Aerosol and Monsoon Processes-Philippines Experiment (CAMP2Ex) NASA field study. Data collection for this product is complete.\r\n\r\nCAMP2Ex was a NASA field study, with three main science objectives: aerosol effect on cloud microphysical and optical properties, aerosol and cloud influence on radiation as well as radiative feedback, and meteorology effect on aerosol distribution and aerosol-cloud interactions. Research on these three main objectives requires a comprehensive characterization of aerosol, cloud, and precipitation properties, as well as the associated meteorological and radiative parameters. Trace gas tracers are also needed for airmass type analysis to characterize the role of anthropogenic and natural aerosols. To deliver these observations, CAMP2Ex utilized a combination of remote sensing and in-situ measurements. NASA\u2019s P-3B aircraft was equipped with a suite of in-situ instruments to conduct measurements of aerosol and cloud properties, trace gases, meteorological parameters, and radiative fluxes. The P-3B was also equipped passive remote sensors (i.e. lidar, polarimeter, radar, and radiometers). A second aircraft, the SPEC Learjet 35A, was primarily dedicated to measuring detailed cloud microphysical properties. The sampling strategy designed for CAMP2Ex coordinated flight plans for both aircraft to maximize the science return. The P-3B was used primarily to conduct remote sensing measurements of cloud and precipitation structure and aerosol layers and vertical profiles of atmospheric state variable, while the Learjet flew below the P-3B to obtain the detailed cloud microphysical properties. During the 2019 field deployment in the vicinity of the Philippines, completed from August 20-October 10, the P-3B conducted 19 science flights and the SPEC Learjet conducted 11 flights. Ground-based aerosol observations were also recorded in 2018 and 2019. CAMP2Ex was completed in partnership with Philippine research and operational weather communities. Measurements completed during CAMP2EX provide a 4-D observational view of the environment of the Philippines and its neighboring waters in terms of microphysical, hydrological, dynamical, thermodynamical and radiative properties of the environment, targeting the environment of shallow cumulus and cumulus congestus clouds.",
-            "title": "CAMP2Ex P-3 In-Situ Trace Gas Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FCAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAirborne%2FCAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
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
-                    "description": "CAMP2Ex Mission Overview/White Paper",
                     "@type": "dcat:Distribution",
+                    "description": "CAMP2Ex Mission Overview/White Paper",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/camp2ex/docs/CAMP2Ex-overview-27NOV2015.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/philippine-airborne-campaign-targets-weather-climate-science",
-                    "description": "NASA.gov CAMP2Ex Feature \u201cPhilippine Airborne Campaign Targets Weather, Climate Science\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov CAMP2Ex Feature \u201cPhilippine Airborne Campaign Targets Weather, Climate Science\u201d",
+                    "downloadURL": "https://www.nasa.gov/feature/goddard/2019/philippine-airborne-campaign-targets-weather-climate-science",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1954731260-LARC_ASDC",
-                    "description": "Earthdata Search forCAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search forCAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1954731260-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Airborne/CAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
-                    "description": "DOI data set landing page for CAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for CAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Airborne/CAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/CAMP2EX/2018",
-                    "description": "CAMP2Ex Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "CAMP2Ex Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/CAMP2EX/2018",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/TraceGas_AircraftInSitu_P3_Data_1/",
-                    "description": "ASDC Direct Data Download for CAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for CAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/CAMP2Ex/TraceGas_AircraftInSitu_P3_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C1954731260-LARC_ASDC",
+            "issued": "2020-07-20",
+            "keyword": [
+                "atmosphere",
+                "atmospheric chemistry",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/Airborne/CAMP2Ex_TraceGas_AircraftInSitu_P3_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-11-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>5.0 -80.0 5.0 130.0 45.0 130.0 45.0 -80.0 5.0 -80.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2019-08-03T00:00:00Z/2019-10-06T23:59:59.999Z",
             "theme": [
                 "CAMP2Ex",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CAMP2Ex P-3 In-Situ Trace Gas Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0938-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-03T14:38:45.000 to 2015-08-03T15:58:19.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0938-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0938-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0938-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-08-03T14:38:45.000 to 2015-08-03T15:58:19.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0938 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0938 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-MIR1-3-CAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Calibrated image data from the Mid Infrared Camera 1 (MIR1) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-mir1-3-cal-v1.0_vtar-kh9s",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "moon",
                 "calibration",
@@ -1535420,58 +1535422,36 @@
                 "test image",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-MIR1-3-CAL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-mir1-3-cal-v1.0_vtar-kh9s",
-            "description": "Calibrated image data from the Mid Infrared Camera 1 (MIR1) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS EARTH/MOON 1ST MID IR CAMERA 3 CAL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "LCROSS EARTH/MOON 1ST MID IR CAMERA 3 CAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://turbmodels.larc.nasa.gov/nut92.html",
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
-                "models",
-                "nut-92",
-                "turbulence"
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
-            "identifier": "NASA-831",
             "description": "This web page gives detailed information on the equations for various forms of the Nut-92 one-equation turbulence model.",
-            "title": "Nut-92 Turbulence Model",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1535479,294 +1535459,292 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-831",
+            "issued": "2018-06-25",
+            "keyword": [
+                "models",
+                "nut-92",
+                "turbulence"
+            ],
+            "landingPage": "http://turbmodels.larc.nasa.gov/nut92.html",
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
+            "title": "Nut-92 Turbulence Model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-ESC2-V1.0",
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
+            "description": "This data set contains CODMAC\nlevel 4 science data acquired by the ROSINA COPS sensor between\n2015-03-11 and 2015-06-30 during the Escort phase 2 of the\nRosetta mission to comet 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-esc2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-ESC2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-esc2-v1.0",
-            "description": "This data set contains CODMAC\nlevel 4 science data acquired by the ROSINA COPS sensor between\n2015-03-11 and 2015-06-30 during the Escort phase 2 of the\nRosetta mission to comet 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 4 ESC2 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P ROSINA 4 ESC2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/ICEPOP/APU/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A and Ali  Tokay.2019. GPM Ground Validation Autonomous Parsivel Unit (APU) ICE POP [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/ICEPOP/APU/DATA101",
-            "issued": "2019-09-06",
-            "temporal": "2015-10-13T01:47:00Z/2018-07-01T15:18:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "radar",
-                "precipitation",
-                "earth science",
-                "clouds",
-                "atmosphere",
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
-            "identifier": "C1979127770-GHRC_DAAC",
             "description": "The GPM Ground Validation Autonomous Parsivel Unit (APU) ICE POP dataset was collected during the International Collaborative Experiments for Pyeongchang 2018 Olympic and Paralympic Winter Games (ICE POP) field campaign in South Korea. The two major objectives of ICE POP were to study severe winter weather events in regions of complex terrain and improve the short-term forecasting of such events. These data contributed to Global Precipitation Measurements mission Ground Validation (GPM GV) campaign efforts to improve satellite estimates of orographic winter precipitation. This dataset consists of precipitation data including precipitation amount, precipitation rate, reflectivity in Rayleigh regime, liquid water content, drop diameter, and drop concentration. Data are available in ASCII format from October 31, 2015 through July 1, 2018. It should be noted that this dataset extends prior to the field campaign.",
-            "title": "GPM Ground Validation Autonomous Parsivel Unit (APU) ICE POP V1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FICEPOP%2FAPU%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FICEPOP%2FAPU%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmapuicepop",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmapuicepop",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/ICEPOP/DATA101",
-                    "description": "ICE POP Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "ICE POP Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/ICEPOP/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20160013407.pdf",
-                    "description": "ICE POP and the NASA Global Precipitation Measurement (GPM) Mission",
                     "@type": "dcat:Distribution",
+                    "description": "ICE POP and the NASA Global Precipitation Measurement (GPM) Mission",
+                    "downloadURL": "https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20160013407.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/icepop/APU/doc/gpmapuicepop_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/icepop/APU/doc/gpmapuicepop_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0469(1976)033%3C0851:TVASOC%3E2.0.CO;2",
-                    "description": "Terminal Velocity and Shape of Cloud and Precipitation Drops Aloft",
                     "@type": "dcat:Distribution",
+                    "description": "Terminal Velocity and Shape of Cloud and Precipitation Drops Aloft",
+                    "downloadURL": "https://doi.org/10.1175/1520-0469(1976)033%3C0851:TVASOC%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2083:CODSDM%3E2.0.CO;2",
-                    "description": "Comparison of Drop Size Distribution Measurements by Impact and Optical Disdrometers",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison of Drop Size Distribution Measurements by Impact and Optical Disdrometers",
+                    "downloadURL": "https://doi.org/10.1175/1520-0450(2001)040%3C2083:CODSDM%3E2.0.CO;2",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-13-00174.1",
-                    "description": "Evaluation of the New Version of the Laser-OPtical Disdrometer, OTT Parsivel\u00b2",
                     "@type": "dcat:Distribution",
+                    "description": "Evaluation of the New Version of the Laser-OPtical Disdrometer, OTT Parsivel\u00b2",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-13-00174.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
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
+            "identifier": "C1979127770-GHRC_DAAC",
+            "issued": "2019-09-06",
+            "keyword": [
+                "radar",
+                "precipitation",
+                "earth science",
+                "clouds",
+                "atmosphere",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/ICEPOP/APU/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "128.378 37.3779 129.124 38.2509",
+            "temporal": "2015-10-13T01:47:00Z/2018-07-01T15:18:00Z",
             "theme": [
                 "ICE POP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GPM Ground Validation Autonomous Parsivel Unit (APU) ICE POP V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/4RNTRRE4JCYD",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs Greenland Ice Mapping Project (GIMP) 2000 Image Mosaic V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/4RNTRRE4JCYD.",
-            "issued": "1999-06-30",
-            "temporal": "1999-06-30T00:00:00Z/2002-09-04T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2002-09-04",
-            "keyword": [
-                "earth science",
-                "glaciers/ice sheets",
-                "cryosphere"
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
-            "identifier": "C1602494076-NSIDC_ECS",
             "description": "This data set, part of the NASA's Making Earth System Data Records for Use in Research Environments (MEaSUREs) program, provides a complete 15 m resolution image mosaic of the Greenland ice sheet, derived from USGS Landsat 7 ETM+ imagery and Canadian Space Agency's (CSA) RADARSAT-1 imagery from the years 1999 to 2002. Additional bands (some at 30 m resolution) are provided for each tile in the mosaic and are useful for understanding surface properties, such as snow grain size, bedrock outcrops, mapping layering in the snow, and blue ice or lake-filled regions, during the spring and summer months. The panchromatic (band 8) mosaic provides the highest-resolution view of the ice sheet surface at 15 m, resolving topographic features, large crevasses, and other geophysical structures.\n\nSee <a href=\"http://nsidc.org/data/measures/gimp\">Greenland Ice Mapping Project (GIMP)</a> for related data.",
-            "title": "MEaSUREs Greenland Ice Mapping Project (GIMP) 2000 Image Mosaic V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4RNTRRE4JCYD",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F4RNTRRE4JCYD",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0713.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0713.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1602494076-NSIDC_ECS&q=nsidc-0713&m=34.875%21-102.515625%212%211%210%210%2C2&tl=1576701501%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1602494076-NSIDC_ECS&q=nsidc-0713&m=34.875%21-102.515625%212%211%210%210%2C2&tl=1576701501%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0713/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0713/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0713.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0713.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1602494076-NSIDC_ECS&q=nsidc-0713&m=34.875%21-102.515625%212%211%210%210%2C2&tl=1576701501%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1602494076-NSIDC_ECS&q=nsidc-0713&m=34.875%21-102.515625%212%211%210%210%2C2&tl=1576701501%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0713/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0713/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4RNTRRE4JCYD",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/4RNTRRE4JCYD",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/4RNTRRE4JCYD",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/4RNTRRE4JCYD",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1602494076-NSIDC_ECS",
+            "issued": "1999-06-30",
+            "keyword": [
+                "earth science",
+                "glaciers/ice sheets",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/4RNTRRE4JCYD",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2002-09-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-70.0 60.0 -20.0 82.0",
+            "temporal": "1999-06-30T00:00:00Z/2002-09-04T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs Greenland Ice Mapping Project (GIMP) 2000 Image Mosaic V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/fss",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
-            ],
-            "keyword": [
-                "carrier",
-                "flight system support",
-                "shuttle",
-                "3d model"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Beth Beck",
                 "hasEmail": "mailto:beth.beck@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-343",
             "description": "Polygons: 1563 Vertices: 1316",
-            "title": "NASA 3D Models: Flight System Support",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1535774,221 +1535752,257 @@
                     "mediaType": "image/x-3ds"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-343",
+            "issued": "2018-06-25",
+            "keyword": [
+                "carrier",
+                "flight system support",
+                "shuttle",
+                "3d model"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/fss",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045",
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Flight System Support"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XGRS-2-EDR-CRUISE3-V1.0",
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
-                "solar system",
-                "near earth asteroid rendezvous"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xgrs-2-edr-cruise3-v1.0_vtip-m293",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar system",
+                "near earth asteroid rendezvous"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NEAR-A-XGRS-2-EDR-CRUISE3-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.near-a-xgrs-2-edr-cruise3-v1.0_vtip-m293",
-            "description": "NEAR EDR volume sets contain a single data set, from one instrument and one mission phase (defined in the phase table in /AAREADME.TXT).",
-            "title": "NEAR XGRS SPECTRA FOR CRUISE3",
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
+            "title": "NEAR XGRS SPECTRA FOR CRUISE3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V2.0",
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
-                "asteroid",
-                "support archives"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "We present data tables giving basic orbital and physical parameters for well-observed or suspected binary/multiple minor planets and the Pluto system, based on a literature review. In total 173 companions in 165 systems are included. Listed data include: minor planet number, name, and provisional designation, dynamical type, and heliocentric semimajor axis and eccentricity; primary and secondary diameter; primary spin period and albedo; companion semimajor axis and orbital period; system mass and density; secondary designation; discovery method and year of announcement. This data set is complete for binary/multiple components reported through 10 March 2009, with some additional data through 4 May 2009.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v2.0_vtjc-8ms5",
+            "issued": "2018-06-26",
+            "keyword": [
+                "asteroid",
+                "support archives"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-5-BINMP-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-5-binmp-v2.0_vtjc-8ms5",
-            "description": "We present data tables giving basic orbital and physical parameters for well-observed or suspected binary/multiple minor planets and the Pluto system, based on a literature review. In total 173 companions in 165 systems are included. Listed data include: minor planet number, name, and provisional designation, dynamical type, and heliocentric semimajor axis and eccentricity; primary and secondary diameter; primary spin period and albedo; companion semimajor axis and orbital period; system mass and density; secondary designation; discovery method and year of announcement. This data set is complete for binary/multiple components reported through 10 March 2009, with some additional data through 4 May 2009.",
-            "title": "BINARY MINOR PLANETS V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "BINARY MINOR PLANETS V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPSTOKE-3-RDR-HALLEY-V2.0",
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
-                "international halley watch",
-                "1p/halley 1 (1682 q1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set presents polarimetric observations of comet 1P/Halley reported as normalized Stokes parameters. All data were contributed by a single observer, A. Dolphus, working at the European Southern Observatory. This revised version of the data set includes updated documentation and data formats.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppstoke-3-rdr-halley-v2.0_vtkb-jw24",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international halley watch",
+                "1p/halley 1 (1682 q1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-PPSTOKE-3-RDR-HALLEY-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-ppstoke-3-rdr-halley-v2.0_vtkb-jw24",
-            "description": "This data set presents polarimetric observations of comet 1P/Halley reported as normalized Stokes parameters. All data were contributed by a single observer, A. Dolphus, working at the European Southern Observatory. This revised version of the data set includes updated documentation and data formats.",
-            "title": "IHW COMET HALLEY POLARIMETRIC STOKES PARAMETERS DATA, V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "IHW COMET HALLEY POLARIMETRIC STOKES PARAMETERS DATA, V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1008",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ehleringer, J.R., L.A. Martinelli, C. Cook, T.F. Domingues, L. Flanagan, J.A. Berry, and J.P.H.B. Ometto. 2011. LBA-ECO CD-02 Oxygen Isotopes of Plant Tissue Water and Atmospheric Water Vapor. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1008",
-            "issued": "2023-10-03",
-            "temporal": "1999-03-01T00:00:00Z/2004-09-30T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-05",
-            "keyword": [
-                "atmosphere",
-                "land surface",
-                "biosphere",
-                "vegetation",
-                "atmospheric chemistry",
-                "atmospheric water vapor",
-                "soils",
-                "earth science",
-                "ecological dynamics"
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
-            "identifier": "C2777836092-ORNL_CLOUD",
             "description": "This data set reports the oxygen isotope signatures of water extracted from plant tissue (xylem from the stems and leaf tissue) and of atmospheric water vapor from twelve different sites (including both pasture and forest) throughout the Amazon region of Brazil. Samples were collected approximately every 4 months between 1999 and 2003 with additional samples collected monthly between January and May of 2003. In 2004 the collection of water samples from plant tissue continued at two sites, though water vapor collections were discontinued, and measurements of deuterium signatures were added to the analyses. In addition, water vapor from the troposphere was collected during a series of aircraft flights over the Tapajos National Forest in May of 2003 and analyzed for oxygen isotopes using the same methodology. There is one comma-delimited ASCII data file with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO CD-02 Oxygen Isotopes of Plant Tissue Water and Atmospheric Water Vapor",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1008",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1008",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD02_O_H_Isotopes/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/carbon_dynamics/CD02_O_H_Isotopes/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD02_O_H_Isotopes.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/CD02_O_H_Isotopes.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1008",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1008",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD02_O_H_Isotopes/comp/CD02_O_H_Isotopes.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/carbon_dynamics/CD02_O_H_Isotopes/comp/CD02_O_H_Isotopes.pdf",
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
+            "identifier": "C2777836092-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "atmosphere",
+                "land surface",
+                "biosphere",
+                "vegetation",
+                "atmospheric chemistry",
+                "atmospheric water vapor",
+                "soils",
+                "earth science",
+                "ecological dynamics"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1008",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-62.36 -10.76 54.58 1.0",
+            "temporal": "1999-03-01T00:00:00Z/2004-09-30T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO CD-02 Oxygen Isotopes of Plant Tissue Water and Atmospheric Water Vapor"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition09/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "Press kit for ISS mission Expedition 09 from 04/2004-10/2004. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Press Kit PDF",
+                    "downloadURL": "http://www.shuttlepresskit.com/EXPEDITION9/Expd-9_PK.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "ISS 09 Press Kit"
+                }
+            ],
+            "identifier": "OCIO-Fitara-21",
             "issued": "2004-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "9",
                 "iss",
@@ -1536000,138 +1536014,136 @@
                 "press kit",
                 "launch"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition09/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:037"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "JSC"
             },
-            "identifier": "OCIO-Fitara-21",
-            "description": "Press kit for ISS mission Expedition 09 from 04/2004-10/2004. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
-            "title": "ISS Expedition 09 Press Kit",
-            "programCode": [
-                "026:037"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.shuttlepresskit.com/EXPEDITION9/Expd-9_PK.pdf",
-                    "description": "Press Kit PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "ISS 09 Press Kit"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ISS Expedition 09 Press Kit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-ESC4-V2.0",
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
+            "description": "This data set contains CODMAC level 4 science data acquired by the ROSINA COPS sensor between 2015-10-20 and 2016-02-09 during the Escort phase 4 of the Rosetta mission to comet 67P/CG. V2.0: Minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-esc4-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-ESC4-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-esc4-v2.0",
-            "description": "This data set contains CODMAC level 4 science data acquired by the ROSINA COPS sensor between 2015-10-20 and 2016-02-09 during the Escort phase 4 of the Rosetta mission to comet 67P/CG. V2.0: Minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 4\n                                      ESC4 V2.0",
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
+            "title": "ROSETTA-ORBITER 67P ROSINA 4\n                                      ESC4 V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/OCEANIA/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/OCEANIA/DATA001.",
-            "issued": "1998-06-22",
-            "temporal": "1998-06-22T00:00:02Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "ocean optics",
-                "ocean chemistry",
-                "oceans",
-                "ocean temperature",
-                "salinity/density",
-                "earth science"
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
-            "identifier": "C1633360536-OB_DAAC",
             "description": "Measurements taken during 1998 to 2000 in the Norwegian Sea.",
-            "title": "Measurements taken onboard the R/V Oceania during 1998 to 2000",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FOCEANIA%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FOCEANIA%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Oceania/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Oceania/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360536-OB_DAAC",
+            "issued": "1998-06-22",
+            "keyword": [
+                "ocean optics",
+                "ocean chemistry",
+                "oceans",
+                "ocean temperature",
+                "salinity/density",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/OCEANIA/DATA001",
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
+            "temporal": "1998-06-22T00:00:02Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements taken onboard the R/V Oceania during 1998 to 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C184964539-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, LaRC.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "William Chu",
+                "hasEmail": "mailto:William.P.Chu@nasa.gov"
+            },
+            "description": "A Level 2 data file containing all the species products for a single lunar event",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The product quality assessment may be downloaded directly from this link",
+                    "downloadURL": "http://eosweb.larc.nasa.gov/PRODOCS/sage3/Quality_Summaries/sage3_quality_summary_v3.html",
+                    "mediaType": "text/html",
+                    "title": "View documentation related to this dataset"
+                }
+            ],
+            "identifier": "C184964539-LARC",
             "issued": "2004-06-14",
-            "temporal": "2001-12-10T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2013-11-05",
             "keyword": [
                 "atmospheric chemistry",
                 "atmospheric chemistry/oxygen compounds",
@@ -1536141,280 +1536153,235 @@
                 "atmosphere",
                 "atmospheric chemistry/nitrogen compounds"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "William Chu",
-                "hasEmail": "mailto:William.P.Chu@nasa.gov"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C184964539-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-11-05",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "LaRC"
             },
-            "identifier": "C184964539-LARC",
-            "description": "A Level 2 data file containing all the species products for a single lunar event",
-            "title": "SAGE III Meteor-3M L2 Lunar Event Species Profiles (Native) V003",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://eosweb.larc.nasa.gov/PRODOCS/sage3/Quality_Summaries/sage3_quality_summary_v3.html",
-                    "description": "The product quality assessment may be downloaded directly from this link",
-                    "@type": "dcat:Distribution",
-                    "title": "View documentation related to this dataset"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2001-12-10T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAGE III Meteor-3M L2 Lunar Event Species Profiles (Native) V003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1227-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-01T22:02:05.000 to 2015-12-01T23:45:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1227-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1227-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1227-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-01T22:02:05.000 to 2015-12-01T23:45:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1227 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1227 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/VIIRS/VNP09A1.001",
             "citation": "Eric Vermote, Belen Franch, Martin Claverie\r\n. 2017-03-24. VNP09A1. Version 001. VIIRS/NPP Surface Reflectance 8-Day L3 Global 1km SIN Grid V001\r\n. Sioux Falls, SD, USA\r\n. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes DAAC\r\n. https://doi.org/10.5067/VIIRS/VNP09A1.001. https://doi.org/10.5067/VIIRS/VNP09A1.001. Digital Science Data. This data set was provided by the NASA/NOAA NPP Project. The DOI landing page provides citations in APA and Chicago styles.\r\n.",
-            "issued": "2017-02-15",
-            "temporal": "2012-01-17T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-27",
-            "keyword": [
-                "earth science",
-                "surface radiative properties",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:lpdaac@usgs.gov"
             },
+            "creator": "Eric Vermote, Belen Franch, Martin Claverie",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1373412073-LPDAAC_ECS",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
             "description": "The 8-day Visible Infrared Imaging Radiometer Suite (VIIRS) surface reflectance (VNP09A1) Version 1 composite product provides an estimate of land surface reflectance from the Suomi National Polar-Orbiting Partnership (Suomi NPP) VIIRS sensor for nine moderate resolution bands (M1 - M5, M7, M8, M10, M11) at nominal 1 kilometer resolution (~926 meter). The 1 kilometer dataset is derived through resampling the native 750 meter VIIRS resolution in the Level 2 input product. The data are corrected for atmospheric conditions such as the effects of molecular gases, including ozone and water vapor, and for the effects of atmospheric aerosols. Each pixel represents the best possible Level 2G observation during an 8-day period that is selected on the basis of high observation coverage, low sensor angle, the absence of clouds or cloud shadow, and aerosol loading. Included in the product along with the nine reflectance bands are day of year, reflectance band quality, control, reflectance state quality assurance, relative azimuth angle, sensor zenith angle, and solar zenith angle layers.",
-            "release-place": "Sioux Falls, SD, USA",
-            "series-name": "VNP09A1",
-            "creator": "Eric Vermote, Belen Franch, Martin Claverie",
-            "title": "VIIRS/NPP Surface Reflectance 8-Day L3 Global 1km SIN Grid V001",
-            "graphic-preview-description": "Browse image for Earthdata Search",
-            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.12.19/BROWSE.VNP09A1.A2019345.h10v05.001.2019353100716.1.jpg?_ga=2.101102721.1452435467.1577973160-2066674673.1574795892",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP09A1.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FVNP09A1.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
-                    "description": "Product Quality Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Product Quality Documentation",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/NPP_QA/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product quality assessment"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP09A1.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/VNP09A1.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP09A1.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/VIIRS/VNP09A1.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://earthexplorer.usgs.gov/",
-                    "description": "USGS EarthExplorer provides users the ability to query, search, and order products available from the LP DAAC.",
                     "@type": "dcat:Distribution",
+                    "description": "USGS EarthExplorer provides users the ability to query, search, and order products available from the LP DAAC.",
+                    "downloadURL": "https://earthexplorer.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through USGS Earth Explorer"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1373412073-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1373412073-LPDAAC_ECS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP09A1.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/VNP09A1.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/",
-                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC website provides detailed information on discovery, distribution, access, and support of land data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/123/VNP09_User_Guide_V1.1.pdf",
-                    "description": "The technical information in the Version 1.1 User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the Version 1.1 User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/123/VNP09_User_Guide_V1.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/124/VNP09_User_Guide_V1.6.pdf",
-                    "description": "The technical information in the Version 1.6 User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the Version 1.6 User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/124/VNP09_User_Guide_V1.6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/122/VNP09_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/122/VNP09_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaacsvc.cr.usgs.gov/appeears/",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://lpdaacsvc.cr.usgs.gov/appeears/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.12.19/BROWSE.VNP09A1.A2019345.h10v05.001.2019353100716.1.jpg?_ga=2.101102721.1452435467.1577973160-2066674673.1574795892",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.12.19/BROWSE.VNP09A1.A2019345.h10v05.001.2019353100716.1.jpg?_ga=2.101102721.1452435467.1577973160-2066674673.1574795892",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LSR_Val.html",
-                    "description": "Validation at stage 1 has been achieved for the VIIRS surface reflectance product suite.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 1 has been achieved for the VIIRS surface reflectance product suite.",
+                    "downloadURL": "https://viirsland.gsfc.nasa.gov/Val/LSR_Val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/NPP_QA/NPPpage.cgi?fileName=maturity&subdir=forPage%23",
-                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding VIIRS product validation and maturity status are available from VIIRS Land Product Quality Assessment site.",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/cgi-bin/NPP_QA/NPPpage.cgi?fileName=maturity&subdir=forPage%23",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://e4ftl01.cr.usgs.gov//WORKING/BRWS/Browse.001/2019.12.19/BROWSE.VNP09A1.A2019345.h10v05.001.2019353100716.1.jpg?_ga=2.101102721.1452435467.1577973160-2066674673.1574795892",
+            "identifier": "C1373412073-LPDAAC_ECS",
+            "issued": "2017-02-15",
+            "keyword": [
+                "earth science",
+                "surface radiative properties",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/VNP09A1.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-07-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, SD, USA",
+            "series-name": "VNP09A1",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-01-17T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "NPP-JPSS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/NPP Surface Reflectance 8-Day L3 Global 1km SIN Grid V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/CGDEOBASZ178",
             "citation": "Vrije Universiteit Amsterdam (Richard de Jeu) and NASA GSFC (Manfred Owe). Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng). 2014-09-15. LPRM_AMSR2_D_SOILM3. Version 001. AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/CGDEOBASZ178. https://disc.gsfc.nasa.gov/datacollection/LPRM_AMSR2_D_SOILM3_001.html.",
-            "issued": "2014-09-17",
-            "temporal": "2012-07-03T00:57:31Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2014-09-17",
-            "references": [
-                "https://doi.org/10.1029/2007JF000769",
-                "https://doi.org/10.1007/s10712-008-9044-0",
-                "https://doi.org/10.1029/2008JD010257",
-                "https://doi.org/10.1109/LGRS.2011.2114872",
-                "https://doi.org/10.1175/JHM-D-13-0200.1"
-            ],
-            "keyword": [
-                "land surface",
-                "earth science",
-                "surface thermal properties",
-                "vegetation",
-                "soils",
-                "biosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "RICHARD DE JEU",
                 "hasEmail": "mailto:Richard.de.jeu@falw.vu.nl"
             },
-            "identifier": "C1235316217-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "description": "AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V001 is a Level 3 (gridded) data set. Its land surface parameters, surface soil moisture, land surface (skin) temperature, and vegetation water content, are derived from passive microwave remote sensing data from the Advanced Microwave Scanning Radiometer 2 (AMSR2), using the Land Parameter Retrieval Model (LPRM). There are two files per day, one ascending (daytime) and one descending (nighttime), archived as two different products. This document is for the nighttime product. The data set covers the period from May 2012, when the Japan Aerospace Exploration Agency (JAXA) Global Change Observation Mission-1st Water GCOM-W1 satellite was launched, to the present.\n\nThe LPRM is based on a forward radiative transfer model to retrieve surface soil moisture and vegetation optical depth. The land surface temperature is derived separately from the AMSR2's Ka-band (36.5 GHz). A unique feature of this method is that it can be applied at any microwave frequency, making it very suitable to exploit all the available passive microwave data from various satellites.\n\nInput data are from the AMSR2 spatial-resolution-matched brightness temperatures (L1SGRTBR) product, nighttime passes, as processed using LPRM (i.e., LPRM/AMSR2/GCOM-W1 Level 2 product, LPRM_AMSR2_SOILM2_V001).",
-            "editor": "Goddard Earth Sciences Data and Information Services Center (GES DISC) (Bill Teng)",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "LPRM_AMSR2_D_SOILM3",
             "creator": "Vrije Universiteit Amsterdam (Richard de Jeu) and NASA GSFC (Manfred Owe)",
-            "title": "AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V001 (LPRM_AMSR2_D_SOILM3) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LPRM_AMSR2_D_SOILM3_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V001 is a Level 3 (gridded) data set. Its land surface parameters, surface soil moisture, land surface (skin) temperature, and vegetation water content, are derived from passive microwave remote sensing data from the Advanced Microwave Scanning Radiometer 2 (AMSR2), using the Land Parameter Retrieval Model (LPRM). There are two files per day, one ascending (daytime) and one descending (nighttime), archived as two different products. This document is for the nighttime product. The data set covers the period from May 2012, when the Japan Aerospace Exploration Agency (JAXA) Global Change Observation Mission-1st Water GCOM-W1 satellite was launched, to the present.\n\nThe LPRM is based on a forward radiative transfer model to retrieve surface soil moisture and vegetation optical depth. The land surface temperature is derived separately from the AMSR2's Ka-band (36.5 GHz). A unique feature of this method is that it can be applied at any microwave frequency, making it very suitable to exploit all the available passive microwave data from various satellites.\n\nInput data are from the AMSR2 spatial-resolution-matched brightness temperatures (L1SGRTBR) product, nighttime passes, as processed using LPRM (i.e., LPRM/AMSR2/GCOM-W1 Level 2 product, LPRM_AMSR2_SOILM2_V001).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCGDEOBASZ178",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FCGDEOBASZ178",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -1536424,208 +1536391,219 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LPRM_AMSR2_D_SOILM3_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/LPRM_AMSR2_D_SOILM3_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSR2_D_SOILM3.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSR2_D_SOILM3.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LPRM_AMSR2_D_SOILM3",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=LPRM_AMSR2_D_SOILM3",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/LPRM_AMSR2_D_SOILM3.001/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/LPRM_AMSR2_D_SOILM3.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSR2_D_SOILM3.001/doc/README_LPRM.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/WAOB/LPRM_AMSR2_D_SOILM3.001/doc/README_LPRM.pdf",
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
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/LPRM_AMSR2_D_SOILM3_001.png",
+            "identifier": "C1235316217-GES_DISC",
+            "issued": "2014-09-17",
+            "keyword": [
+                "land surface",
+                "earth science",
+                "surface thermal properties",
+                "vegetation",
+                "soils",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/CGDEOBASZ178",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2014-09-17",
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
+                "https://doi.org/10.1109/LGRS.2011.2114872",
+                "https://doi.org/10.1175/JHM-D-13-0200.1"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "LPRM_AMSR2_D_SOILM3",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-07-03T00:57:31Z/2022-01-17T00:00:00Z",
             "theme": [
                 "GCOM-W",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AMSR2/GCOM-W1 surface soil moisture (LPRM) L3 1 day 25 km x 25 km descending V001 (LPRM_AMSR2_D_SOILM3) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/167",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F. G., K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods. 1996. NWS Daily Climatology Data: 1980 (SNF). [National Weather Service Daily Climatology Data: 1980 (Superior National Forest)]. Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Based on F. G. Hall, K. F. Huemmrich, D. E. Strebel, S. J. Goetz, J. E. Nickeson, and K. D. Woods, Biophysical, Morphological, Canopy Optical Property, and Productivity Data from the Superior National Forest, NASA Technical Memorandum 104568, National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A., 1992. doi:10.3334/ORNLDAAC/167",
-            "issued": "2024-03-01",
-            "temporal": "1980-01-01T00:00:00Z/1980-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
-            "keyword": [
-                "atmospheric radiation",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmosphere",
-                "precipitation",
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
-            "identifier": "C2884977545-ORNL_CLOUD",
             "description": "Daily min, max, average temperature (F), precipitation (water equivalent in inches), and daily insolation (Langleys) for the Superior National Forest area as collected by NWS and U. of Minnesota",
-            "graphic-preview-description": "Browse Image",
-            "title": "NWS Daily Climatology Data: 1980 (SNF)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F167",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F167",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1980/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/snf/SNF_MET_1980/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/SNF/guides//nws_daily_climate_1980.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/SNF/guides//nws_daily_climate_1980.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/167",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/167",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1980/comp/met_1980.def",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1980/comp/met_1980.def",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1980/comp/met_1980.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1980/comp/met_1980.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1980/comp/nws_daily_climate_1980.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1980/comp/nws_daily_climate_1980.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1980/comp/nws_daily_climate_1980.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/snf/SNF_MET_1980/comp/nws_daily_climate_1980.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/snf_logo_square.png",
+            "identifier": "C2884977545-ORNL_CLOUD",
+            "issued": "2024-03-01",
+            "keyword": [
+                "atmospheric radiation",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmosphere",
+                "precipitation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/167",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-03-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-92.51 47.66 -91.77 48.17",
+            "temporal": "1980-01-01T00:00:00Z/1980-12-31T23:59:59Z",
             "theme": [
                 "SNF",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NWS Daily Climatology Data: 1980 (SNF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://asrs.arc.nasa.gov/search/reportsets.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://asrs.arc.nasa.gov/"
-            ],
-            "keyword": [
-                "aviation",
-                "conflict",
-                "aircraft",
-                "safety",
-                "parachute"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda J. Connell",
                 "hasEmail": "mailto:linda.j.connell@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-819",
             "description": "A sampling of reports involving parachuting activity and conflicts with aircraft.",
-            "title": "Aviation Safety Reporting System: Parachutist / Aircraft Conflicts",
-            "programCode": [
-                "026:021"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1536633,172 +1536611,173 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-819",
+            "issued": "2018-06-25",
+            "keyword": [
+                "aviation",
+                "conflict",
+                "aircraft",
+                "safety",
+                "parachute"
+            ],
+            "landingPage": "http://asrs.arc.nasa.gov/search/reportsets.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:021"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://asrs.arc.nasa.gov/"
+            ],
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Aviation Safety Reporting System: Parachutist / Aircraft Conflicts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO_L1B_RAD.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Mike Smyth, Tom Logan, William Johnson. 2022-11-14. ECOSTRESS Swath Top of Atmosphere Calibrated Radiance Instantaneous L1B Global 70 m v002. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO_L1B_RAD.002. https://doi.org/10.5067/ECOSTRESS/ECO_L1B_RAD.002. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2022-11-14",
-            "temporal": "2018-07-09T00:00:00Z/2024-12-23T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Simon Hook",
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2076116385-LPCLOUD",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\nThe ECOSTRESS Swath Top of Atmosphere Calibrated Radiance Instantaneous L1B Global 70 m (ECO_L1B_RAD) Version 2 data product provides at-sensor calibrated radiance values retrieved for five thermal infrared (TIR) bands operating between 8 and 12.5 \u00b5m. Additionally, the digital numbers (DN) for the shortwave infrared (SWIR) band are provided. The TIR bands are spatially co-registered to produce a variable spatial resolution between 70 meters (m) and 90 m at the edge of the swath. The ECO_L1B_RAD data product is provided as swath data and does not contain geolocation information. The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L1B_RAD data product. The geographic coverage of acquisitions for the ECO_L1B_RAD Version 2 data product extends to areas outside of those indicated on the coverage map. \nThe ECO_L1B_RAD Version 2 data product contains layers of radiance values for the five TIR bands, DN values for the SWIR band, associated data quality indicators, and ancillary data distributed in HDF5 format.\n\nImprovements/Changes from Previous Versions\n\n-\tA radiance calibration has been applied to correct the ~1K cold bias that has been observed in previous studies. These values are described in Section 3 of the User Guide (https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf).\n\nKnown Issues\n\n-\tCannot perform spatial query on ECO_L1B_RAD in NASA Earthdata Search: ECO_L1B_RAD does not contain spatial attributes, so granules cannot be searched by geographic location. Users should search for ECO_L1B_RAD data products by orbit number instead.\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tMissing scan data/striping features: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see Section 3.3.2 of the User Guide (https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf).\n\n-\tScan overlap: An overlap between ECOSTRESS scans results in a clear line overlap and repeating data. Additional information is available in Section 3.2 of the User Guide (",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "title": "ECOSTRESS Swath Top of Atmosphere Calibrated Radiance Instantaneous L1B Global 70 m V002",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\nThe ECOSTRESS Swath Top of Atmosphere Calibrated Radiance Instantaneous L1B Global 70 m (ECO_L1B_RAD) Version 2 data product provides at-sensor calibrated radiance values retrieved for five thermal infrared (TIR) bands operating between 8 and 12.5 \u00b5m. Additionally, the digital numbers (DN) for the shortwave infrared (SWIR) band are provided. The TIR bands are spatially co-registered to produce a variable spatial resolution between 70 meters (m) and 90 m at the edge of the swath. The ECO_L1B_RAD data product is provided as swath data and does not contain geolocation information. The corresponding ECO_L1B_GEO (https://doi.org/10.5067/ECOSTRESS/ECO_L1B_GEO.002) data product is required to georeference the ECO_L1B_RAD data product. The geographic coverage of acquisitions for the ECO_L1B_RAD Version 2 data product extends to areas outside of those indicated on the coverage map. \nThe ECO_L1B_RAD Version 2 data product contains layers of radiance values for the five TIR bands, DN values for the SWIR band, associated data quality indicators, and ancillary data distributed in HDF5 format.\n\nImprovements/Changes from Previous Versions\n\n-\tA radiance calibration has been applied to correct the ~1K cold bias that has been observed in previous studies. These values are described in Section 3 of the User Guide (https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf).\n\nKnown Issues\n\n-\tCannot perform spatial query on ECO_L1B_RAD in NASA Earthdata Search: ECO_L1B_RAD does not contain spatial attributes, so granules cannot be searched by geographic location. Users should search for ECO_L1B_RAD data products by orbit number instead.\n\n-\tData acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly, temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented, and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\n\n-\tData acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\n\n-\tMissing scan data/striping features: During testing, an instrument artifact was encountered in ECOSTRESS bands 1 and 5, resulting in missing values. A machine learning algorithm has been applied to interpolate missing values. For more information on the missing scan filling techniques and outcomes, see Section 3.3.2 of the User Guide (https://lpdaac.usgs.gov/documents/1491/ECO1B_User_Guide_V2.pdf).\n\n-\tScan overlap: An overlap between ECOSTRESS scans results in a clear line overlap and repeating data. Additional information is available in Section 3.2 of the User Guide (",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L1B_RAD.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO_L1B_RAD.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076116385-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2076116385-LPCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L1B_RAD.002",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO_L1B_RAD.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://lpdaac.usgs.gov/",
```

